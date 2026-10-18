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
transcripts/              full transcripts, synced automatically (see INDEX.md)
scripts/                  transcript sync and fetch scripts
.claude/settings.json     session hook that keeps transcripts/ current
SOURCES.md                every source, linked
OPEN-QUESTIONS.md         gaps and conflicts only you can answer
```

## Setup

**Fulcrum OS / Claude Code:** copy this folder into the workspace (or clone it) so `CLAUDE.md` sits at the root of what the AI reads. Nothing else to configure.

**Claude.ai Projects:** upload the folders to the project's knowledge. Upload `CLAUDE.md` too and tell the project to read it first.

## Transcripts fill themselves

Nothing to run. The first time the AI opens this repo, a session hook starts a background sync that pulls the full transcript of every video on your channel, the testimonials channel, and each podcast appearance into `transcripts/` (about 10 to 15 minutes, then a refresh every 3 days). The six videos whose breakdowns are still incomplete are fetched first, and the AI rebuilds those breakdowns as soon as their transcripts land. Needs Python 3.9+ on a normal internet connection. Details in [transcripts/README.md](transcripts/README.md).

## Make it more accurate

Go through [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md). It lists numbers that don't match across your videos, gaps (Instagram reels and LinkedIn weren't readable from public sources), and facts to confirm. Ten minutes of answers there makes everything else sharper.

## How this was built

Researched from your YouTube channels, podcast appearances, the Meteoric Boost site, Whop, and the Epiphanies newsletter, as of October 18, 2026. Every claim traces back to a source in [SOURCES.md](SOURCES.md). Client results and revenue figures are as you've stated them publicly.

Put together by Aarya at Fulcrum Labs.
