#!/usr/bin/env python3
"""
Pull full transcripts of Moksh's own YouTube videos into ./transcripts/.

Run this on your own machine (YouTube blocks most cloud servers):

    pip install yt-dlp youtube-transcript-api
    python scripts/fetch_transcripts.py

Options:
    --channels   one or more channel URLs (defaults to both of Moksh's channels)
    --ids        specific video IDs instead of whole channels
    --langs      transcript languages in priority order (default: en hi)
    --overwrite  re-download transcripts that already exist

Each video is saved as transcripts/<video_id>__<slug>.md with a small header
and one line per caption segment, timestamped, so the AI can cite moments.
"""

import argparse
import re
import sys
import time
from pathlib import Path

try:
    import yt_dlp
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    sys.exit("Missing packages. Run: pip install yt-dlp youtube-transcript-api")

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "transcripts"

DEFAULT_CHANNELS = [
    "https://www.youtube.com/@mokshvasant/videos",
    "https://www.youtube.com/@mokshvasant/shorts",
    "https://www.youtube.com/@mokshvasant/streams",
    "https://www.youtube.com/channel/UCsqGTbGrDsq6CNxczCZmaJA/videos",  # Meteoric Boost testimonials
]


def slugify(text: str, limit: int = 60) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text[:limit].rstrip("-") or "untitled"


def ts(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def list_videos(channel_url: str):
    opts = {"extract_flat": True, "quiet": True, "skip_download": True, "ignoreerrors": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(channel_url, download=False) or {}
    for entry in info.get("entries") or []:
        if entry and entry.get("id"):
            yield entry["id"], entry.get("title") or entry["id"]


def video_meta(video_id: str):
    opts = {"quiet": True, "skip_download": True, "ignoreerrors": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False) or {}
    return {
        "title": info.get("title", video_id),
        "upload_date": info.get("upload_date", "unknown"),
        "duration": info.get("duration_string") or str(info.get("duration", "unknown")),
        "views": info.get("view_count", "unknown"),
        "channel": info.get("channel", "unknown"),
        "description": (info.get("description") or "").strip(),
    }


def fetch_transcript(video_id: str, langs):
    api = YouTubeTranscriptApi()
    try:
        fetched = api.fetch(video_id, languages=langs)
    except Exception:
        # Fall back to any available transcript (auto-generated included)
        transcript_list = api.list(video_id)
        transcript = next(iter(transcript_list))
        fetched = transcript.fetch()
    return [(s.start, s.text.replace("\n", " ").strip()) for s in fetched]


def save(video_id: str, langs, overwrite: bool) -> str:
    existing = list(OUT.glob(f"{video_id}__*.md"))
    if existing and not overwrite:
        return f"skip   {video_id} (already saved)"
    meta = video_meta(video_id)
    lines = fetch_transcript(video_id, langs)
    path = OUT / f"{video_id}__{slugify(meta['title'])}.md"
    date = meta["upload_date"]
    if len(date) == 8 and date.isdigit():
        date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    header = [
        "---",
        f"title: \"{meta['title']}\"",
        f"video_id: {video_id}",
        f"url: https://www.youtube.com/watch?v={video_id}",
        f"channel: {meta['channel']}",
        f"published: {date}",
        f"duration: {meta['duration']}",
        f"views_at_fetch: {meta['views']}",
        "---",
        "",
        f"# {meta['title']}",
        "",
        "## Description",
        "",
        meta["description"] or "(none)",
        "",
        "## Transcript",
        "",
    ]
    body = [f"[{ts(start)}] {text}" for start, text in lines if text]
    path.write_text("\n".join(header + body) + "\n", encoding="utf-8")
    return f"saved  {video_id} -> {path.name} ({len(body)} lines)"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--channels", nargs="*", default=DEFAULT_CHANNELS)
    p.add_argument("--ids", nargs="*")
    p.add_argument("--langs", nargs="*", default=["en", "en-IN", "hi"])
    p.add_argument("--overwrite", action="store_true")
    args = p.parse_args()

    OUT.mkdir(exist_ok=True)
    ids = args.ids or []
    if not ids:
        seen = set()
        for url in args.channels:
            print(f"listing {url}")
            for vid, title in list_videos(url):
                if vid not in seen:
                    seen.add(vid)
                    ids.append(vid)
        print(f"found {len(ids)} videos\n")

    ok = failed = 0
    for vid in ids:
        try:
            print(save(vid, args.langs, args.overwrite))
            ok += 1
        except Exception as e:  # no captions, private, rate limited, etc.
            print(f"FAILED {vid}: {type(e).__name__}: {str(e).splitlines()[0][:120]}")
            failed += 1
        time.sleep(1)  # be gentle; YouTube rate-limits bursts

    print(f"\ndone: {ok} ok, {failed} failed. Files are in {OUT}")


if __name__ == "__main__":
    main()
