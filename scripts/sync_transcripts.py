#!/usr/bin/env python3
"""
Keeps transcripts/ filled automatically. Nobody needs to run this by hand.

How it runs: .claude/settings.json calls this script every time a Claude Code
session starts in this repo. It returns in under a second and, when a sync is
due, starts a background worker that:
  1. creates a private Python environment in .transcript-tools/ (first run only),
  2. installs or updates yt-dlp and youtube-transcript-api there,
  3. runs scripts/fetch_transcripts.py (the six incomplete videos first, then
     every upload on both channels and every podcast appearance),
  4. rebuilds transcripts/INDEX.md and writes transcripts/_sync_status.json.

What it prints goes into the AI's context: whether a sync is running, and which
video breakdowns now have a transcript and should be rebuilt (see CLAUDE.md).

Modes:
  python scripts/sync_transcripts.py            hook mode (default)
  python scripts/sync_transcripts.py --now      run the full sync in the foreground
  python scripts/sync_transcripts.py --index    only rebuild transcripts/INDEX.md
"""

import json
import os
import re
import subprocess
import sys
import time
import venv
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TR = ROOT / "transcripts"
TOOLS = ROOT / ".transcript-tools"
STATUS = TR / "_sync_status.json"
LOCK = TR / ".sync.lock"
LOG = TR / "_sync.log"
SYNC_EVERY_HOURS = 72          # full refresh cadence
RETRY_AFTER_BLOCK_HOURS = 6    # wait this long after YouTube rate-limits us
LOCK_STALE_HOURS = 3


# ---------- small helpers ----------

def now():
    return datetime.now(timezone.utc)


def hours_since(iso):
    try:
        return (now() - datetime.fromisoformat(iso)).total_seconds() / 3600
    except Exception:
        return 1e9


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def fm_value(fm, key):
    m = re.search(rf"(?m)^{key}:\s*(.*)$", fm)
    return m.group(1).strip().strip('"') if m else ""


YT_ID = re.compile(r"(?:v=|youtu\.be/|shorts/)([A-Za-z0-9_-]{11})")


# ---------- catalog of breakdowns and transcripts ----------

def catalog():
    """Known videos and appearances, with their breakdown files and access level."""
    items = {}
    for f in sorted((ROOT / "04-videos").glob("*.md")):
        fm = frontmatter(f.read_text(encoding="utf-8"))
        vid = fm_value(fm, "video_id")
        if vid:
            items[vid] = {"title": fm_value(fm, "title"), "breakdown": f"04-videos/{f.name}",
                          "access": fm_value(fm, "transcript_access").lower(), "kind": "video"}
    for f in sorted((ROOT / "05-appearances").glob("*.md")):
        if f.name == "README.md":
            continue
        fm = frontmatter(f.read_text(encoding="utf-8"))
        for vid in YT_ID.findall(fm):
            items.setdefault(vid, {"title": fm_value(fm, "title"), "breakdown": f"05-appearances/{f.name}",
                                   "access": fm_value(fm, "transcript_access").lower(), "kind": "appearance"})
    return items


def transcripts_present():
    found = {}
    for f in TR.glob("*__*.md"):
        found[f.name.split("__", 1)[0]] = f.name
    return found


def incomplete(access):
    return not (access.startswith("full") or access.startswith("partial"))


def build_index():
    items, present = catalog(), transcripts_present()
    rows = []
    for vid, it in items.items():
        tfile = present.get(vid)
        rows.append((it["breakdown"], it["title"], vid, it["breakdown"],
                     f"[{tfile}]({tfile})" if tfile else "pending sync"))
    extra = sorted(set(present) - set(items))
    st = read_json(STATUS) or {}
    out = [
        "---", "title: Transcript index", "type: index", "---", "",
        "# Transcript index", "",
        "Full transcripts sync into this folder automatically each time the AI opens the repo "
        "(see [README.md](README.md)). This index is rebuilt after every sync.", "",
        f"- Transcripts present: **{len(present)}**",
        f"- Last sync: {st.get('finished', 'not run yet')}",
        f"- Last sync result: {len(st.get('saved', []))} new, {len(st.get('failed', {}))} failed"
        + (" (YouTube rate-limited the connection; the next sync resumes)" if st.get('blocked') else ""),
        "", "## Videos and appearances with a breakdown", "",
        "| Title | Video ID | Breakdown | Transcript |", "|---|---|---|---|",
    ]
    for _, title, vid, bd, tr in sorted(rows, reverse=True):
        safe = title.replace("|", "/")
        out.append(f"| {safe} | {vid} | [{Path(bd).name}](../{bd}) | {tr} |")
    if extra:
        out += ["", f"## Transcripts without a breakdown yet ({len(extra)})", "",
                "Mostly Shorts and older vlogs. The AI adds breakdowns for the useful ones (see CLAUDE.md).", ""]
        out += [f"- [{present[v]}]({present[v]})" for v in extra]
    (TR / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")


# ---------- background worker ----------

def tools_python():
    sub = "Scripts/python.exe" if os.name == "nt" else "bin/python"
    return TOOLS / sub


def ensure_tools(log):
    py = tools_python()
    if not py.exists():
        log.write("creating .transcript-tools environment\n"); log.flush()
        venv.EnvBuilder(with_pip=True, clear=True).create(TOOLS)
    log.write("installing/updating yt-dlp and youtube-transcript-api\n"); log.flush()
    subprocess.run([str(py), "-m", "pip", "install", "-q", "-U", "--disable-pip-version-check",
                    "yt-dlp", "youtube-transcript-api"], stdout=log, stderr=log, check=True)
    return py


def run_worker():
    LOCK.write_text(json.dumps({"pid": os.getpid(), "started": now().isoformat()}), encoding="utf-8")
    try:
        with open(LOG, "w", encoding="utf-8") as log:
            log.write(f"sync started {now().isoformat()}\n"); log.flush()
            try:
                py = ensure_tools(log)
                subprocess.run([str(py), str(ROOT / "scripts" / "fetch_transcripts.py"),
                                "--status-file", str(STATUS)], stdout=log, stderr=log, cwd=ROOT)
            except Exception as e:
                log.write(f"sync failed: {type(e).__name__}: {e}\n")
                STATUS.write_text(json.dumps({"finished": now().isoformat(), "saved": [], "failed": {},
                                              "error": f"{type(e).__name__}: {str(e)[:200]}"}, indent=2),
                                  encoding="utf-8")
            build_index()
            log.write(f"sync finished {now().isoformat()}\n")
    finally:
        try:
            LOCK.unlink()
        except FileNotFoundError:
            pass


# ---------- hook mode ----------

def sync_running():
    lock = read_json(LOCK)
    return bool(lock) and hours_since(lock.get("started", "")) < LOCK_STALE_HOURS


def sync_due():
    st = read_json(STATUS)
    if not st or not st.get("finished"):
        return True
    age = hours_since(st["finished"])
    nothing_saved = not st.get("saved") and st.get("failed")
    if st.get("blocked") or st.get("error") or nothing_saved:
        return age >= RETRY_AFTER_BLOCK_HOURS
    return age >= SYNC_EVERY_HOURS


def launch_background():
    kwargs = {"cwd": ROOT, "stdin": subprocess.DEVNULL, "stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
    if os.name == "nt":
        kwargs["creationflags"] = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kwargs["start_new_session"] = True
    subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"], **kwargs)


def hook():
    TR.mkdir(exist_ok=True)
    lines = []
    if sync_running():
        lines.append("Transcript sync is running in the background (log: transcripts/_sync.log).")
    elif sync_due():
        launch_background()
        lines.append("Started a background transcript sync (log: transcripts/_sync.log). "
                     "New transcripts land in transcripts/ over the next several minutes.")
    items, present = catalog(), transcripts_present()
    rebuild = [vid for vid, it in items.items() if vid in present and incomplete(it["access"])]
    no_breakdown = sorted(set(present) - set(items))
    if rebuild:
        lines.append("ACTION per CLAUDE.md: transcripts now exist for these incomplete breakdowns; rebuild them: "
                     + ", ".join(f"{items[v]['breakdown']} (transcripts/{present[v]})" for v in rebuild[:10]))
    if no_breakdown:
        lines.append(f"{len(no_breakdown)} transcripts have no breakdown yet (see transcripts/INDEX.md). "
                     "Add breakdowns for the ones about business, brand, or content when there is time.")
    if lines:
        print("[transcript sync] " + " ".join(lines))


def main():
    if "--worker" in sys.argv:
        run_worker()
    elif "--now" in sys.argv:
        TR.mkdir(exist_ok=True)
        run_worker()
        print(LOG.read_text(encoding="utf-8")[-2000:])
    elif "--index" in sys.argv:
        build_index()
        print("rebuilt transcripts/INDEX.md")
    else:
        try:
            hook()
        except Exception as e:  # never break session start
            print(f"[transcript sync] skipped: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
