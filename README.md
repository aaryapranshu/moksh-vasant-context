# Moksh Vasant: second brain context

Everything you've published publicly, turned into structured context an AI can work from: how you think about personal brands, how Meteoric Boost runs, how you sell, and how you script and package your videos.

Built for FulcrumOS (or any Claude Code setup). Drop the folder in and the AI reads `CLAUDE.md` first, which routes it to the right files for each task. `MOKSH.md` is the one-file version.

Every claim traces to a timestamped moment in one of **161 full transcripts** of your videos, Shorts, client testimonials and podcast appearances.

## What's inside

```
CLAUDE.md                 start here (for the AI): who you are, rules, which files to load per task
MOKSH.md                  the one-file master brief (paste into any chat or Claude Project)
00-identity/              profile, timeline, influences
01-mental-models/         personal brand, content and distribution, offers and sales,
                          business and operations, mindset and life
02-meteoric-boost/        company, Meteoric Engine, offer and sales process, case studies, positioning,
                          testimonials/ (one breakdown per client testimonial video)
03-content-playbook/      video types, titles, hooks, CTAs, voice, script templates
04-videos/                one breakdown per important YouTube video (2021 to 2026), plus Shorts
                          and creator-era syntheses
05-appearances/           Wiser Together EP.28, EP.52, EP.60, The Sanskar Show #226, Breaking down businesses
06-writing/               the Epiphanies newsletter
transcripts/              161 full timestamped transcripts, kept current automatically (see INDEX.md)
scripts/                  transcript sync and fetch scripts
.claude/settings.json     session hook that keeps transcripts/ current
SOURCES.md                every source, linked
OPEN-QUESTIONS.md         gaps and conflicts only you can answer
```

## Setup

**FulcrumOS / Claude Code (one command).** From the root of your workspace (the folder Claude Code opens):

```bash
git clone --depth 1 https://github.com/aaryapranshu/moksh-vasant-context.git /tmp/moksh-ctx && bash /tmp/moksh-ctx/install.sh && rm -rf /tmp/moksh-ctx
```

It copies everything into `context/moksh-vasant/`, adds a short pointer to your `CLAUDE.md`, and adds the transcript-sync hook to `.claude/settings.json` (your existing settings are kept). Re-run the same command any time to update.

**Claude.ai Projects or any chat:** upload `MOKSH.md` for the essentials, or the folders plus `CLAUDE.md` for everything, and tell the project to read `CLAUDE.md` first. Skip `transcripts/` if space is tight: the breakdowns carry the timestamps.

## Transcripts

All 161 are already in `transcripts/`: 137 from YouTube captions and 24 transcribed from the audio with Whisper, because YouTube has no captions for them (including six of your biggest 2026 videos). Every breakdown was rebuilt from them on 20 Oct 2026. After that, a session hook pulls new uploads every 3 days in the background (needs Python 3.9+ on a normal internet connection). Details in [transcripts/README.md](transcripts/README.md).

## Make it more accurate

Go through [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md). It lists numbers that don't match across your videos, client names the captions couldn't settle, and gaps (Instagram reels and LinkedIn weren't readable from public sources). Ten minutes of answers there makes everything else sharper.

## How this was built

Researched from your YouTube channels (main, Shorts, testimonials), podcast appearances, the Meteoric Boost site, Whop, and the Epiphanies newsletter. First pass 18 Oct 2026; rebuilt from full transcripts 20 Oct 2026. Every claim traces back to a source in [SOURCES.md](SOURCES.md), and most to a timestamp. Client results and revenue figures are as stated publicly.

Put together by Aarya at Fulcrum Labs.
