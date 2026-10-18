# transcripts/

Full, word-for-word transcripts of every video on @mokshvasant, the Meteoric Boost testimonials channel, and each podcast appearance. This folder fills itself. Nobody needs to run anything.

## How it fills

The repo ships with a Claude Code session hook (`.claude/settings.json`). Every time the AI opens this repo, `scripts/sync_transcripts.py` runs for well under a second. When a sync is due, it starts a background job that:

1. Sets up a private Python environment in `.transcript-tools/` on the first run (nothing is installed system-wide).
2. Pulls the six videos whose breakdowns are waiting on a transcript first, then every upload and podcast appearance.
3. Saves one file per video here as `<video_id>__<title-slug>.md`, with the title, URL, date, duration, views, description, and timestamped transcript.
4. Rebuilds [INDEX.md](INDEX.md) and writes `_sync_status.json`.

The first sync takes roughly 10 to 15 minutes in the background. After that it refreshes every 3 days and only downloads new uploads. If YouTube rate-limits the connection, it stops and resumes on the next session.

When transcripts arrive for videos whose breakdowns are incomplete, the hook tells the AI, and `CLAUDE.md` instructs it to rebuild those breakdowns and update the mental models. New uploads get picked up the same way.

## Requirements

Python 3.9 or newer on the machine running the AI. It must be a normal home or office connection: YouTube blocks most cloud servers.

## If the repo sits inside a bigger workspace

Claude Code only runs hooks from the workspace root's `.claude/settings.json`. If this folder is nested inside a larger project, `CLAUDE.md` tells the AI to start the sync itself. To make it a hook too, copy the `SessionStart` block from this repo's `.claude/settings.json` into the workspace's settings and change the path to `<this-folder>/scripts/sync_transcripts.py`.

## Manual commands (optional)

```bash
python3 scripts/sync_transcripts.py --now     # full sync in the foreground, with a log
python3 scripts/sync_transcripts.py --index   # rebuild INDEX.md only
```

## Scripts and drafts

Original scripts written before filming are even more useful than transcripts for teaching the AI how Moksh writes. Drop them in `transcripts/scripts/`.
