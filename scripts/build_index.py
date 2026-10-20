#!/usr/bin/env python3
"""Rebuild transcripts/INDEX.md for the moksh-vasant-context repo (grouped, with breakdown links).

usage: build_index.py REPO_ROOT
"""
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(sys.argv[1])
TR = ROOT / "transcripts"
YT_ID = re.compile(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})")


def fm(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def val(f, key):
    m = re.search(rf"(?m)^{key}:\s*(.*)$", f)
    return m.group(1).strip().strip('"') if m else ""


breakdowns = {}
for folder in ("04-videos", "05-appearances", "02-meteoric-boost"):
    for f in sorted((ROOT / folder).rglob("*.md")):
        if f.name == "README.md":
            continue
        head = fm(f.read_text(encoding="utf-8"))
        # only the file's own ID fields (or url lines), never IDs cited in `sources`
        ids = set()
        for line in re.findall(r"(?m)^(?:url|urls|youtube):\s*(.*)$", head):
            ids |= set(YT_ID.findall(line))
        for line in re.findall(r"(?m)^video_ids?:\s*(.*)$", head):
            ids |= set(re.findall(r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{11}(?![A-Za-z0-9_-])", line))
        for vid in ids:
            breakdowns.setdefault(vid, str(f.relative_to(ROOT)))

# syntheses that cover many videos in one file (Shorts, early vlogs)
ANY_ID = re.compile(r"(?<![A-Za-z0-9_-])[A-Za-z0-9_-]{11}(?![A-Za-z0-9_-])")
synth = {}
for name in ("shorts-2024-2025.md", "early-vlogs-2020-2022.md", "early-era-synthesis.md"):
    f = ROOT / "04-videos" / name
    if f.exists():
        for vid in ANY_ID.findall(f.read_text(encoding="utf-8")):
            synth.setdefault(vid, f"04-videos/{name}")

rows = []
for f in sorted(TR.glob("*__*.md")):
    head = fm(f.read_text(encoding="utf-8"))
    vid = val(head, "video_id")
    rows.append({
        "vid": vid, "file": f.name, "title": val(head, "title").replace("|", "/"),
        "date": val(head, "published"), "dur": val(head, "duration"),
        "views": val(head, "views_at_fetch"), "channel": val(head, "channel"),
        "src": val(head, "transcript_source"), "bd": breakdowns.get(vid) or synth.get(vid),
    })


def group(r):
    ch = r["channel"].lower()
    secs = 0
    try:
        parts = [int(p) for p in r["dur"].split(":")]
        for p in parts:
            secs = secs * 60 + p
    except ValueError:
        pass
    if "testimonial" in ch or ch.startswith("meteoric"):
        return "Meteoric Boost testimonials channel"
    if "moksh" not in ch:
        return "Appearances on other channels"
    if secs and secs <= 180:
        return "Shorts"
    return "Main channel long-form" if r["date"] >= "2025" else "Main channel, creator era (2020 to 2024)"


order = ["Main channel long-form", "Appearances on other channels", "Meteoric Boost testimonials channel",
         "Main channel, creator era (2020 to 2024)", "Shorts"]
out = ["---", "title: Transcript index", "type: index", f"last_updated: {date.today().isoformat()}", "---", "",
       "# Transcript index", "",
       f"- Transcripts present: **{len(rows)}**",
       f"- With a breakdown or synthesis entry: **{sum(1 for r in rows if r['bd'])}**",
       f"- Whisper-transcribed from audio (no YouTube captions exist): **{sum(1 for r in rows if 'Whisper' in r['src'])}**",
       f"- Last full sync: {date.today().isoformat()}", "",
       "Files are `<video_id>__<slug>.md`: front matter (title, url, published date, duration, views at fetch, "
       "transcript source), the video description, then a timestamped transcript in roughly 10-second lines. "
       "Auto-captions garble names and some numbers; check breakdowns for the confirmed spelling.", ""]
for g in order:
    sel = sorted([r for r in rows if group(r) == g], key=lambda r: r["date"], reverse=True)
    if not sel:
        continue
    out += [f"## {g} ({len(sel)})", "", "| Published | Title | Duration | Transcript | Breakdown |", "|---|---|---|---|---|"]
    for r in sel:
        bd = f"[{Path(r['bd']).name}](../{r['bd']})" if r["bd"] else ""
        mark = " (Whisper)" if "Whisper" in r["src"] else ""
        out.append(f"| {r['date']} | {r['title']} | {r['dur']} | [{r['vid']}]({r['file']}){mark} | {bd} |")
    out.append("")
missing = sorted(set(breakdowns) - {r["vid"] for r in rows})
if missing:
    out += ["## Breakdowns with no transcript file", ""] + [f"- {v}: {breakdowns[v]}" for v in missing] + [""]
(TR / "INDEX.md").write_text("\n".join(out), encoding="utf-8")
print(f"INDEX.md: {len(rows)} transcripts, {len(missing)} breakdown IDs without transcript")
