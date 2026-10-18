---
title: Moksh Vasant context repository (AI entry point)
type: index
last_updated: 2026-10-18
---

# Moksh Vasant: context for AI agents

Read this file first. It tells you who Moksh is, how this repo is organized, and which files to load for a given task.

## Who Moksh is (short version)

- Founder and CEO of **Meteoric Boost**, a personal brand studio for founders (started 2025). Clients are founders doing $50k+/month who are respected in their industry but unknown outside it.
- Core belief: a founder's brand is trust infrastructure for their business. It should be extracted from what is already true about them, not invented.
- From Jamnagar, Gujarat (he has also called Mumbai home; see OPEN-QUESTIONS). Studied economics at the University of Sydney. Moved back to India in 2025. Turned 21 in December 2024.
- Creator since about 2017. Roughly 139K Instagram followers (@moksh.vasant) and 10.7K YouTube subscribers (@mokshvasant) as of October 2026.
- Before Meteoric Boost: a calisthenics coaching startup called Meteoric (2020), Notion templates, StuKonnect (student startup), a search-fund internship in Sydney, and the Epiphanies newsletter.

Full profile: [00-identity/profile.md](00-identity/profile.md)

## Ground rules for using this repo

1. **Numbers are self-reported.** Revenue, client counts, and client results come from Moksh's own videos, site, and podcasts. They are not audited, and several conflict with each other. Keep the qualifier when you repeat them, and check [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) before stating a number as fact.
2. **Files are paraphrased breakdowns, not transcripts.** For exact wording, use `transcripts/` (empty until Moksh runs `scripts/fetch_transcripts.py`). If a transcript exists for a video, it overrides the breakdown.
3. **Newer beats older.** His views moved from self-improvement creator (2021 to 2024) to founder and CEO (2025 onward). When sources disagree, prefer the most recent unless the question is about his history.
4. **Do not fill gaps by guessing.** If something is not in the repo, say so, or ask Moksh.
5. **Writing as Moksh:** follow [03-content-playbook/voice-and-language.md](03-content-playbook/voice-and-language.md). Lowercase "i" in titles, proof before identity, calm peer-to-peer tone in scripted videos, no generic AI phrasing, no em dashes.

## Repo map

| Folder | What's in it |
|---|---|
| [00-identity/](00-identity/) | Profile, full timeline, books and people that shaped him |
| [01-mental-models/](01-mental-models/) | How he thinks: personal brand, content and distribution, offers and sales, business and operations, mindset and life |
| [02-meteoric-boost/](02-meteoric-boost/) | The company: the Meteoric Engine, offer and ICP, sales process, case studies, positioning |
| [03-content-playbook/](03-content-playbook/) | How he scripts and packages content: video types, titles, hooks, CTAs, voice, reusable templates |
| [04-videos/](04-videos/) | One breakdown per YouTube video, 2021 to 2026 |
| [05-appearances/](05-appearances/) | Podcasts and interviews: Wiser Together x3, The Sanskar Show, Breaking down businesses |
| [06-writing/](06-writing/) | The Epiphanies newsletter (Dec 2024 to May 2025) |
| [transcripts/](transcripts/) | Drop zone for full transcripts, plus instructions |
| [SOURCES.md](SOURCES.md) | Every source used, with links |
| [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) | Gaps and conflicts only Moksh can resolve |

## Which files to load for which task

| Task | Load |
|---|---|
| Write a YouTube script in his style | `03-content-playbook/script-template.md`, `youtube-script-playbook.md`, `titles-hooks-ctas.md`, `voice-and-language.md`, plus 2 to 3 similar videos from `04-videos/` |
| Write a reel, caption, or story sequence | `03-content-playbook/short-form-and-instagram.md`, `voice-and-language.md`, `01-mental-models/content-and-distribution.md` |
| Plan or critique a client's personal brand | `01-mental-models/personal-brand.md`, `02-meteoric-boost/meteoric-engine.md`, `02-meteoric-boost/case-studies.md` |
| Prep a sales call or write an offer | `02-meteoric-boost/offer-icp-and-sales-process.md`, `01-mental-models/offers-pricing-sales.md`, `02-meteoric-boost/case-studies.md` |
| Write website, deck, or outreach copy for Meteoric Boost | `02-meteoric-boost/messaging-and-positioning.md`, `02-meteoric-boost/company.md`, `voice-and-language.md` |
| Make a business or hiring decision the way he would | `01-mental-models/business-and-operations.md`, `01-mental-models/mindset-and-life.md` |
| Answer "what did Moksh say about X" | Search `01-mental-models/` first, then `04-videos/` and `05-appearances/`, then `transcripts/` |
| Bio, intro, or speaker profile | `00-identity/profile.md`, `00-identity/timeline.md` |
| Draft a newsletter issue | `06-writing/epiphanies-newsletter.md`, `voice-and-language.md` |

## Keeping this repo current

- After each new upload: run `python scripts/fetch_transcripts.py` (on a laptop, not a server) to pull the transcript into `transcripts/`, then add a breakdown to `04-videos/` using the same template as the existing files and update `04-videos/README.md`.
- When a belief changes, update the model in `01-mental-models/` and note the change under "Evolution / confidence" instead of deleting the old view.
- When Moksh answers an item in `OPEN-QUESTIONS.md`, fix the affected files and remove the item.
