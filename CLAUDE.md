---
title: Moksh Vasant context repository (AI entry point)
type: index
last_updated: 2026-10-20
---

# Moksh Vasant: context for AI agents

Read this file first. It tells you who Moksh is, how this repo is organized, and which files to load for a given task. For a single-file version of everything important (to paste into a chat or a Claude Project), use [MOKSH.md](MOKSH.md).

## Who Moksh is (short version)

- Founder and CEO of **Meteoric Boost**, a personal brand studio for founders and wealth creators (first client June 2025). Clients are operators doing about $50k+/month, respected in their industry but unknown outside it. He has said 80+ founders since 2025 (self-reported).
- Core belief: a founder's brand is trust infrastructure for the business. It is extracted from what is already true about the person, not invented. "The brand is the business."
- Born and raised in Jamnagar, Gujarat, in a business family. Based in Bombay today [Aarya, 20 Oct 2026]. Studied economics at the University of Sydney (from Feb 2022). Moved back to India in 2025. Born 16 December; 22 as of Oct 2026.
- Creator since 2017. About 139K Instagram followers (@moksh.vasant) and 10.7K YouTube subscribers (@mokshvasant) as of Oct 2026.
- Before Meteoric Boost: a calisthenics coaching startup called Meteoric (launched May to June 2021, at 17), Notion templates, StuKonnect (student startup, with Aryan Bhatia), an unpaid search-fund / PE internship in Sydney, and the Epiphanies newsletter.
- Meteoric Boost does ₹40L+ a month and runs its systems on FulcrumOS (built by Fulcrum Labs) [Aarya, 20 Oct 2026; private, not for public copy without Moksh's OK].

Full profile: [00-identity/profile.md](00-identity/profile.md)

## Ground rules for using this repo

1. **Transcripts are the source of truth.** Every breakdown in `04-videos/`, `05-appearances/` and `02-meteoric-boost/testimonials/` was rebuilt on 20 Oct 2026 from a full timestamped transcript in `transcripts/`. Citations look like `BU0smWywaw8 [24:10]`. If a breakdown and its transcript disagree, the transcript wins; fix the breakdown.
2. **Numbers are self-reported.** Revenue, client counts and client results come from Moksh's own videos, site and podcasts, and many conflict. Keep the qualifier, give the date and source, never merge figures into a new number, and check [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) before stating one as fact. Video titles often claim more than is said in the video; quote what was said.
3. **Attribution matters.** Transcripts have no speaker labels. In podcasts, collabs and case studies the breakdowns mark who said what. Don't credit a host's, client's or teammate's line to Moksh.
4. **Newer beats older.** His views moved from self-improvement creator (2021 to 2024) to founder and CEO (2025 onward). When sources disagree, prefer the most recent unless the question is about his history.
5. **Don't fill gaps by guessing.** If something isn't in the repo, say so, or ask Moksh. Names marked "captioned as" are unconfirmed.
6. **Writing as Moksh:** follow [03-content-playbook/voice-and-language.md](03-content-playbook/voice-and-language.md). Lowercase "i" in titles, proof before identity, peer-to-peer tone, no generic AI phrasing, no em dashes.

## Repo map

| Folder | What's in it |
|---|---|
| [MOKSH.md](MOKSH.md) | One-file master brief: who he is, how he thinks, how he sells, how he writes |
| [00-identity/](00-identity/) | Profile, full dated timeline, books and people that shaped him |
| [01-mental-models/](01-mental-models/) | How he thinks: personal brand, content and distribution, offers and sales, business and operations, mindset and life |
| [02-meteoric-boost/](02-meteoric-boost/) | The company: team, the Meteoric Engine, offer and ICP, sales process, case studies, positioning |
| [02-meteoric-boost/testimonials/](02-meteoric-boost/testimonials/) | One breakdown per client testimonial video, plus how testimonials are produced |
| [03-content-playbook/](03-content-playbook/) | How he scripts and packages content: video types, titles, hooks, CTAs, voice, reusable templates |
| [04-videos/](04-videos/) | One breakdown per important YouTube video (2021 to 2026), plus syntheses of the Shorts and the creator era |
| [05-appearances/](05-appearances/) | Podcasts and interviews: Wiser Together x3, The Sanskar Show, Breaking down businesses |
| [06-writing/](06-writing/) | The Epiphanies newsletter (Dec 2024 to May 2025) |
| [transcripts/](transcripts/) | 161 full timestamped transcripts; [INDEX.md](transcripts/INDEX.md) maps each to its breakdown |
| [SOURCES.md](SOURCES.md) | Every source used, with links |
| [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) | Gaps and conflicts only Moksh can resolve |

## Which files to load for which task

| Task | Load |
|---|---|
| Quick context for any task | [MOKSH.md](MOKSH.md) |
| Write a YouTube script in his style | `03-content-playbook/script-template.md`, `youtube-script-playbook.md`, `titles-hooks-ctas.md`, `voice-and-language.md`, plus 2 to 3 similar videos from `04-videos/` and their transcripts |
| Write a reel, caption, or story sequence | `03-content-playbook/short-form-and-instagram.md`, `voice-and-language.md`, `04-videos/shorts-2024-2025.md`, `01-mental-models/content-and-distribution.md` |
| Plan or critique a client's personal brand | `01-mental-models/personal-brand.md`, `02-meteoric-boost/meteoric-engine.md`, `02-meteoric-boost/case-studies.md`, `04-videos/2026-05-30__dont-build-personal-brand-2026.md` |
| Build an offer | `01-mental-models/offers-pricing-sales.md` and the three live builds: `04-videos/2025-10-21__build-brand-from-scratch-live.md`, `2026-03-21__high-ticket-offer-best-closer.md`, `2026-04-08__pe-info-product-live.md` |
| Prep a sales call | `02-meteoric-boost/offer-icp-and-sales-process.md`, `01-mental-models/offers-pricing-sales.md`, `02-meteoric-boost/case-studies.md` |
| Use client proof (decks, site, outreach) | `02-meteoric-boost/case-studies.md` ("How to use client proof"), `02-meteoric-boost/testimonials/` |
| Write website, deck, or outreach copy for Meteoric Boost | `02-meteoric-boost/messaging-and-positioning.md`, `02-meteoric-boost/company.md`, `voice-and-language.md` |
| Make a business or hiring decision the way he would | `01-mental-models/business-and-operations.md`, `01-mental-models/mindset-and-life.md` |
| Answer "what did Moksh say about X" | Search `01-mental-models/` first, then `04-videos/` and `05-appearances/`, then grep `transcripts/` for the exact words |
| Bio, intro, or speaker profile | `00-identity/profile.md`, `00-identity/timeline.md` |
| Draft a newsletter issue | `06-writing/epiphanies-newsletter.md`, `voice-and-language.md` |

## Transcript sync (automatic)

A SessionStart hook (`.claude/settings.json`) runs `scripts/sync_transcripts.py` every session. Every 3 days it pulls new uploads into `transcripts/` in the background, rebuilds `transcripts/INDEX.md`, and prints a line beginning `[transcript sync]` into your context.

- If that line lists transcripts with no breakdown, add a breakdown to `04-videos/` for each one about business, brand, sales or content, using the template of `04-videos/2026-01-12__130k-in-6-months.md`. Add new Shorts to `04-videos/shorts-2024-2025.md`. Then update `04-videos/README.md` and fold new models into `01-mental-models/` and `03-content-playbook/`.
- If you see no `[transcript sync]` line (for example because this repo is nested inside a larger workspace, so the hook didn't fire), check `transcripts/_sync_status.json`. If its `finished` time is more than 3 days old, run `python3 scripts/sync_transcripts.py` from this repo's root (it returns immediately and syncs in the background), then carry on.
- A new upload with no YouTube captions won't get a transcript from the sync. Transcribe it from audio with Whisper (as was done for 24 videos) before writing its breakdown. Never write a breakdown from a title alone.

## Keeping this repo current

- When a belief changes, update the model in `01-mental-models/` and note the change under "Evolution" instead of deleting the old view.
- When Moksh answers an item in `OPEN-QUESTIONS.md`, fix the affected files and remove the item.
- When you update a synthesis file, also update [MOKSH.md](MOKSH.md) if the change affects the summary.
