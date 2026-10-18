# transcripts/

Drop zone for the full, word-for-word transcripts of your videos.

The rest of this repo holds structured breakdowns of each video (in `videos/`). This folder is for the raw source, so the AI can quote you exactly and pick up phrasing the breakdowns don't capture.

## Option 1: one command (recommended)

Run this on your own laptop. YouTube blocks most cloud servers, so it won't work from a hosted environment.

```bash
pip install yt-dlp youtube-transcript-api
python scripts/fetch_transcripts.py
```

It lists every video on `@mokshvasant` (long-form, Shorts, lives) and the Meteoric Boost testimonials channel, then saves one file per video here:

```
transcripts/<video_id>__<title-slug>.md
```

Each file has a small header (title, URL, date, duration, views, description) and the transcript with timestamps. Re-running skips videos already saved, so you can run it after every upload.

Useful flags:

```bash
python scripts/fetch_transcripts.py --ids Ze4JOAAvAq8 qYIKwqRvIyU   # specific videos
python scripts/fetch_transcripts.py --langs en hi                    # language priority
python scripts/fetch_transcripts.py --overwrite                      # refresh everything
```

## Option 2: YouTube Studio

Studio > Content > pick a video > Subtitles > the "..." next to a language > Download (.srt or .txt). Save it here as `<video_id>__<title>.txt`.

## Podcasts

Wiser Together and the Sanskar Goyal episode are on other people's channels. Their YouTube versions work with `--ids`:

```bash
python scripts/fetch_transcripts.py --ids 6SYJFqH-RPQ n1vbE3e8XuE Y0fC8dizX0o k-f2AMd8-ek
```

## Scripts and drafts

If you have the original scripts you wrote before filming, put them in `transcripts/scripts/`. Those are even more valuable than transcripts for teaching the AI how you write, because they show the structure before delivery.
