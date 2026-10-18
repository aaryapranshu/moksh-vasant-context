#!/usr/bin/env python3
"""
Pull full transcripts of Moksh's YouTube videos and podcast appearances into ./transcripts/.

You normally never run this by hand: scripts/sync_transcripts.py runs it in the
background every time the AI opens this repo (see .claude/settings.json).

Manual use (needs: pip install yt-dlp youtube-transcript-api):
    python scripts/fetch_transcripts.py                 # everything
    python scripts/fetch_transcripts.py --ids ID1 ID2   # specific videos
    python scripts/fetch_transcripts.py --overwrite     # refresh all

Each video is saved as transcripts/<video_id>__<slug>.md with a header
(title, URL, date, duration, views, description) and one timestamped line per
caption segment, so the AI can cite moments.
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime, timezone
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

# Appearances on other people's channels
DEFAULT_EXTRA_IDS = [
    "6SYJFqH-RPQ",  # Wiser Together EP.60 (Feb 2026)
    "Y0fC8dizX0o",  # Wiser Together EP.28 (Oct 2023)
    "k-f2AMd8-ek",  # Wiser Together EP.52 (Nov 2024)
    "n1vbE3e8XuE",  # The Sanskar Show #226 (Mar 2026)
    "IEuERGHU3wA",  # Breaking down businesses (Oct 2025)
    "9Ma2bozEqGM",  # Collab with Aryan Mahajan (Aug 2026)
]

# The six videos whose breakdowns are waiting on a transcript: fetched first
PRIORITY_IDS = ["qSNYWCyKGyo", "C4ckCV1xmj8", "w5ONkdV9OZw", "9nLoz2BYIUc", "W3uYWLXJ4-A", "pyYGdcb1V48"]


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
            yield entry["id"]


def video_meta(video_id: str):
    opts = {"quiet": True, "skip_download": True, "ignoreerrors": True, "no_warnings": True}
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
    except Exception as first_error:
        if "block" in str(first_error).lower():
            raise
        transcript = next(iter(api.list(video_id)))  # any track, auto-generated included
        fetched = transcript.fetch()
    return [(s.start, s.text.replace("\n", " ").strip()) for s in fetched]


def existing(video_id: str):
    return list(OUT.glob(f"{video_id}__*.md"))


def save(video_id: str, langs, overwrite: bool) -> str:
    if existing(video_id) and not overwrite:
        return "skip"
    meta = video_meta(video_id)
    lines = fetch_transcript(video_id, langs)
    for old in existing(video_id):
        old.unlink()
    path = OUT / f"{video_id}__{slugify(meta['title'])}.md"
    date = meta["upload_date"]
    if len(date) == 8 and date.isdigit():
        date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    title = meta["title"].replace('"', "'")
    header = [
        "---",
        f'title: "{title}"',
        f"video_id: {video_id}",
        f"url: https://www.youtube.com/watch?v={video_id}",
        f"channel: {meta['channel']}",
        f"published: {date}",
        f"duration: {meta['duration']}",
        f"views_at_fetch: {meta['views']}",
        f"fetched: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
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
    return "saved"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--channels", nargs="*", default=DEFAULT_CHANNELS)
    p.add_argument("--ids", nargs="*")
    p.add_argument("--no-extras", action="store_true", help="skip podcast/collab IDs on other channels")
    p.add_argument("--langs", nargs="*", default=["en", "en-IN", "en-GB", "hi"])
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--sleep", type=float, default=2.0, help="seconds between videos")
    p.add_argument("--status-file", help="write a JSON summary here")
    args = p.parse_args()

    OUT.mkdir(exist_ok=True)
    status = {"started": datetime.now(timezone.utc).isoformat(), "saved": [], "skipped": 0,
              "failed": {}, "listing_errors": [], "blocked": False}

    if args.ids:
        ids = list(args.ids)
    else:
        ids, seen = [], set()
        for vid in PRIORITY_IDS + ([] if args.no_extras else DEFAULT_EXTRA_IDS):
            if vid not in seen:
                seen.add(vid)
                ids.append(vid)
        for url in args.channels:
            print(f"listing {url}", flush=True)
            try:
                for vid in list_videos(url):
                    if vid not in seen:
                        seen.add(vid)
                        ids.append(vid)
            except Exception as e:
                status["listing_errors"].append(f"{url}: {type(e).__name__}: {str(e)[:150]}")
        print(f"{len(ids)} videos to check", flush=True)

    consecutive_blocks = 0
    for vid in ids:
        try:
            result = save(vid, args.langs, args.overwrite)
            if result == "skip":
                status["skipped"] += 1
                continue
            status["saved"].append(vid)
            consecutive_blocks = 0
            print(f"saved  {vid}", flush=True)
        except Exception as e:  # no captions, private, rate limited, etc.
            msg = f"{type(e).__name__}: {str(e).splitlines()[0][:150] if str(e) else ''}"
            status["failed"][vid] = msg
            print(f"FAILED {vid}: {msg}", flush=True)
            if "block" in msg.lower() or "429" in msg:
                consecutive_blocks += 1
                if consecutive_blocks >= 3:
                    status["blocked"] = True
                    print("YouTube is rate-limiting this connection; stopping. The next sync resumes.", flush=True)
                    break
        time.sleep(args.sleep)

    status["finished"] = datetime.now(timezone.utc).isoformat()
    status["total_transcripts"] = len(list(OUT.glob("*__*.md")))
    if args.status_file:
        Path(args.status_file).write_text(json.dumps(status, indent=2), encoding="utf-8")
    print(f"done: {len(status['saved'])} saved, {status['skipped']} already had, "
          f"{len(status['failed'])} failed. Files are in {OUT}", flush=True)


if __name__ == "__main__":
    main()
