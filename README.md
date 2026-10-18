# Moksh Vasant: second brain context

Everything you've published publicly, turned into structured context an AI can work from: how you think about personal brands, how Meteoric Boost runs, how you sell, and how you script and package your videos.

Built for Fulcrum OS (or any Claude Code setup). Drop the folder in and the AI reads `CLAUDE.md` first, which routes it to the right files for each task.

## What's inside

```
CLAUDE.md                 start here (for the AI): who you are, rules, which files to load per task
00-identity/              profile, timeline, influences
01-mental-models/         personal brand, content and distribution, offers and sales,
                          business and operations, mindset and life
02-meteoric-boost/        company, Meteoric Engine, offer and sales process, case studies, positioning
03-content-playbook/      video types, titles, hooks, CTAs, voice, script templates
04-videos/                one breakdown per YouTube video (2021 to 2026)
05-appearances/           Wiser Together EP.28, EP.52, EP.60, The Sanskar Show #226, Breaking down businesses
06-writing/               the Epiphanies newsletter
transcripts/              drop zone for full transcripts
scripts/                  fetch_transcripts.py
SOURCES.md                every source, linked
OPEN-QUESTIONS.md         gaps and conflicts only you can answer
```

## Setup

**Fulcrum OS / Claude Code:** copy this folder into the workspace (or clone it) so `CLAUDE.md` sits at the root of what the AI reads. Nothing else to configure.

**Claude.ai Projects:** upload the folders to the project's knowledge. Upload `CLAUDE.md` too and tell the project to read it first.

## Add your full transcripts (5 minutes)

The video files here are detailed breakdowns. For word-for-word context, pull your transcripts on your own laptop:

```bash
pip install yt-dlp youtube-transcript-api
python scripts/fetch_transcripts.py
```

It grabs every video on your channel and the testimonials channel and saves them to `transcripts/`. Details in [transcripts/README.md](transcripts/README.md).

## Make it more accurate

Go through [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md). It lists numbers that don't match across your videos, gaps (Instagram reels and LinkedIn weren't readable from public sources), and facts to confirm. Ten minutes of answers there makes everything else sharper.

## How this was built

Researched from your YouTube channels, podcast appearances, the Meteoric Boost site, Whop, and the Epiphanies newsletter, as of October 18, 2026. Every claim traces back to a source in [SOURCES.md](SOURCES.md). Client results and revenue figures are as you've stated them publicly.

Put together by Aarya at Fulcrum Labs.
