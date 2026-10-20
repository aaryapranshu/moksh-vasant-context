# transcripts/

Full, word-for-word, timestamped transcripts of Moksh's YouTube videos, the Meteoric Boost testimonials channel, and every podcast appearance. [INDEX.md](INDEX.md) lists all of them, grouped, with links to their breakdowns.

## What's here (as of 20 Oct 2026)

- **161 transcripts:** 21 long-form videos from the Meteoric Boost era (including the Aryan Mahajan conversation), 6 podcast appearances (Wiser Together x3, The Sanskar Show and its re-edit, Breaking down businesses), 10 testimonial videos, 75 creator-era videos (2018 to 2024) and 49 Shorts.
- **137 from YouTube captions** (auto-generated, fetched with yt-dlp). Names and some numbers are garbled; breakdowns record the confirmed spellings.
- **24 transcribed locally with Whisper** (large-v3-turbo) from the audio, because YouTube has no captions for them. These include six of his most important 2026 videos, the PE info-product live build, and 13 Shorts. Whisper is cleaner than auto-captions but still not authoritative on names.
- **Not fetched:** 13 uploads from 2017 to 2019 (music covers and school vlogs) that YouTube put behind a sign-in wall, and music covers with no speech.
- 12 creator-era transcripts are unreadable: YouTube mis-detected the language and output Hindi script. Their breakdowns or index rows say so.

## File format

`<video_id>__<title-slug>.md`. Front matter holds the title, URL, channel, published date, duration, views at fetch, `transcript_source` (captions or Whisper) and fetch date. Then the video description, then the transcript in roughly 10-second lines: `[mm:ss] text`. Cite moments as `video_id [mm:ss]`.

There are no speaker labels. In podcasts, collabs and case studies, the breakdown files mark who said what.

## Keeping it current

The repo's Claude Code session hook (`.claude/settings.json`) runs `scripts/sync_transcripts.py` each session. Every 3 days it starts a background job that pulls new uploads into this folder and rebuilds INDEX.md (via `scripts/build_index.py`). It skips videos already here. When a new upload has no breakdown yet, the hook says so and `CLAUDE.md` tells the AI to add one.

It needs Python 3.9+ and a normal home or office connection (YouTube blocks most cloud servers). New uploads with no captions won't get a transcript from the sync; transcribe those from audio with Whisper, as was done for the 24 above.

If this folder sits inside a bigger workspace, the hook won't fire (Claude Code only runs the workspace root's hooks). Copy the `SessionStart` block from `.claude/settings.json` into the workspace's settings and point it at `<this-folder>/scripts/sync_transcripts.py`.

```bash
python3 scripts/sync_transcripts.py --now     # full sync in the foreground, with a log
python3 scripts/sync_transcripts.py --index   # rebuild INDEX.md only
```

## Still missing (and worth adding)

- **Instagram reels.** The Shorts here look like re-posts of his 2024 to 2025 reels, but nothing from 2025 to 2026 Instagram. Exporting his top 20 reels' scripts and captions into `transcripts/instagram/` would sharpen the short-form playbook more than anything else.
- **Original scripts.** Scripts written before filming teach the AI how he writes better than transcripts do. Drop them in `transcripts/scripts/`.
