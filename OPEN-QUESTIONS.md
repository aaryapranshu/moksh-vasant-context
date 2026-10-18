---
title: Open questions for Moksh
type: index
last_updated: 2026-10-18
---

# Open questions

Things public sources couldn't settle. Answering these makes every other file more accurate. When one is answered, update the affected files and delete the item.

## Numbers that don't match

1. **Revenue timeline.** Public figures, all self-reported:
   - "$52k in 3.5 months" (video title, Sep 2025), while about $40k is the figure spoken in the talk itself
   - "$130k in 5 months" (Wiser Together EP.60 title) and "$130k in 6 months" (YouTube, Jan 2026)
   - about $110k lifetime from the current offer (2025 recap, Dec 2025)
   - "Rs 1.5 crore in 6 months" and about $152k lifetime, $30k to $40k a month (The Sanskar Show, Mar 2026)

   What is the canonical month-by-month revenue, and which number should the AI use today?
2. **Client count.** About 8 (mid 2025), about 35 (Dec 2025), 80+ founders scaled (site, 2026). Is 80+ total clients, or brands across all offers?
3. **Pricing.** Tickets of $3k to $7k were mentioned in early 2026. The site lists no price, and Whop has a $200 "Meteoric Boost" product. What are the current offers and prices, and what is the Whop product for?

3a. **Playbook numbers that changed between videos.** Which is current?
   - Story sequence length: 6 to 7 frames (Sep 2025) vs 8 to 12 frames (Mar 2026)
   - Reel music tempo: 140 to 180 BPM (Aug 2025) vs 120 to 140 BPM (Mar 2026)
   - Whiteboard videos: the leads format (Sep 2025) vs the reach format (Jan 2026)
   - Founder time on content: 2 to 3, 4 to 8, 8 to 12, or 24 hours a month depending on the source (the site says 4 to 8)
   - Pinned posts: two carousels (Jan 2026) vs three videos (Sep 2026)
   - Funnel: "DM is the only funnel" (Jan 2026) vs the site's application form now
   - Client intake: a long onboarding form (Mar 2026) vs documents built from transcripts (site)
   - Breakout reel: about 1M views and 25K followers in one retelling, 3.2 to 3.4M views and 45K in another (maybe two different reels)

## Biography

4. **Home city.** The newsletter and Wiser Together EP.28 point to Jamnagar. The 2025 recap calls Mumbai home. One source says Delhi. What should the AI say?
5. **Degree.** The newsletter and EP.60 suggest he finished his economics degree at the University of Sydney. The Feb 2026 "Road to $1 million" video mentions dropping out after two $50k months (speaker unclear). Which is right?
6. **The Meteoric name.** A garbled line in the Dec 2021 vlog may mention "Meteoric". Was the calisthenics startup already named then?
7. **Agency co-founder.** The May 2025 newsletter mentions co-founding a creative agency with a mentor. Is that Meteoric Boost, and is the mentor still involved?

8a. **Company start date.** The Breaking down businesses interview (recorded 9 Oct 2025) says about four months in, which fits a June 2025 start and the first client on 8 Jun 2025. The Gstaad video (Sep 2026) mentions about 1.5 years running the company. Which framing should the AI use?
8b. **Internship.** Some sources say search fund, the Breaking down businesses interview says private equity. Which wording is right?
8c. **Podcast count.** In Wiser Together EP.60 he says it's the only podcast he has done, but the Breaking down businesses interview was recorded two months earlier. Minor, but worth a line.
8d. **First Meteoric dates.** He has said he started the calisthenics startup at 17 in 2020, and also during a gap year after school. Which is right?

## Company

8. **Team.** Who does what today? Known from public sources: Adi / Aditya Vohra (COO), Arjun Sharin (sales calls), a creative director, editors, "three principals" and "4 owners" on the site.
9. **Meteoric Engine.** The site shows 5 stages and says 2 of 14 phases are internal. Should the full 14 phases go into the repo (it stays private to your OS)?
10. **"Boost Protocol."** Auto-captions mention a "Meteoric Boost Protocol" or "Boost Protocol". What is it?
11. **Case study identities.** Auto-captions garble client names. Please confirm:
    - "Arian" in the 22-year-old millionaire case study (sD4R8Z4H6U4) and "Darren Mahajin" on The Sanskar Show: Aryan Mahajan?
    - The 24-year-old ecom client (C4ckCV1xmj8) and "Dutch Manocha": Daksh Manocha?
    - The fitness-coach friend in the live build (wi6pyq5nXK8): Dhanil Shah?
    - The creative director and the Jan 2026 head of sales (captioned "Mish" and "Freddy"), and whether Adi the COO is Aditya Vohra.
11a. **Done-with-you vs done-for-you.** The Jan 2026 video argues done-with-you beats done-for-you; the current site sells a done-for-you, no-homework partnership. Has the model changed, and which should the AI describe?
11b. **The 50% acquisition offer** (Monaco and London videos). Who made it, and can it be mentioned publicly?
11c. **Studio or agency?** Which word should external copy use?

## Content not reachable from public sources

12. **Transcripts.** Six recent videos had no readable captions from any public source in October 2026 (YouTube was blocking transcript services): qSNYWCyKGyo, C4ckCV1xmj8, w5ONkdV9OZw, 9nLoz2BYIUc, W3uYWLXJ4-A, pyYGdcb1V48. Their files hold verified metadata only. Pull exactly these six on a laptop with:

    ```bash
    python scripts/fetch_transcripts.py --ids qSNYWCyKGyo C4ckCV1xmj8 w5ONkdV9OZw 9nLoz2BYIUc W3uYWLXJ4-A pyYGdcb1V48
    ```

    Then ask the AI to rebuild those six breakdowns (CLAUDE.md tells it how). Two early videos (EDDyx-uqmLE, 4tQJUr7N14M) have only music or garbled captions; a line on what they cover would help.
13. **The rest of the channel.** @mokshvasant has 169 uploads; about 40 are broken down here. The rest are mostly Shorts and early vlogs. The script pulls all of them.
14. **Instagram.** Reels, captions, and hooks couldn't be read (Instagram blocks automated access). Exporting your top 20 reels' scripts and captions into `transcripts/instagram/` would sharpen the short-form playbook more than anything else.
15. **LinkedIn.** Profile and posts weren't readable. Paste your About section and best posts into `06-writing/`.
16. **Thumbnails.** Not visible to the research. A short note on your thumbnail rules would complete the packaging section.
17. **Scripting workflow.** The Sanskar Show episode describes a Claude-based scripting workflow. Adding the actual prompts and a few finished scripts to `transcripts/scripts/` would let the AI draft in your exact structure.
18. **Unconfirmed Short.** The Wiser Together Short h80LT7xMa8c ("become that person today") isn't confirmed as you, so it's excluded. Is it you?
