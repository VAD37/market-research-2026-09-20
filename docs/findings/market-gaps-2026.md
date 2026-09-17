# Market gaps, 2026-09 — what is unbuilt, and what only looks unbuilt

Pass 3, 2026-09-16. Compiled from `../raw/market-gaps-2026-pulls.md` (17 blocks) and `../raw/market-gaps-2026-source-index.md`.

**Read the channel problem first, because it shapes everything below.** The brief sent this agent at demand-side complaint channels. Reddit was unreachable all session — curl returns the JS app shell, WebFetch refuses the domain. G2 returned 403. WebSearch was at 200/200 before the agent made a single query. Three of the four intended channels were gone.

What it found instead is the useful part: **Discourse-based product forums expose an open, unauthenticated `/search.json` and `/t/<id>.json` API that is not JS-gated.** OpenAI's community forum and Cursor's forum both run Discourse. That is a reusable channel into real user complaints, dated, with view and like counts, and it is where this pull's best material came from.

So: the gaps below are thin, and they are thin partly because the channels were blocked. Do not read "few gaps found" as "few gaps exist."

## The strongest gap is the one this team is standing in

**Non-US access to AI products is broken, continuously, for four years running.**

Geolocation and verification checks misfire against users in countries that are on the vendor's own supported list. From the OpenAI community forum, verbatim, across ten countries:

> "I'm living in Mauritius and I want to register for OpenAI ChatGPT but I am unable to because I'm getting the 'services are not available in your country'. Mauritius is supposedly in the list of supported countries" — 2023-01-14

> "I'm living in Kazakhstan and want to pay for OpenAI, but I cannot because I'm getting the 'services are not available in your country'. At the same time, Kazakhstan is on the list of supported countries." — 2023-03-09

> "i facing issue 'not available in your country' after i login openAI and it detect my ISP IP from Hong Kong but im using my internet in Malaysia" — 2023-03-23

> "Vietnam appears on OpenAI's supported countries/territories lists, so this may not simply be a country-availability issue..." — **2026-05-25**

> "why does Codex require mandatory phone verification even after I have already paid for a ChatGPT Plus subscription? I paid for the service, but I cannot use Codex because my account is blocked" — 2026-07-21

Mauritius, Uzbekistan, Nepal, South Korea, Libya, Malaysia, Vietnam, Kazakhstan, and Germany/Austria/Hungary for Sora. **2022 through 2026-07. No incumbent fix.** Each case is resolved, when it is resolved, by a manual support ticket.

And the pricing half of the same problem:

> "Dear OpenAI Team, I'm a user of ChatGPT from India... I would like to kindly request that you consider adding support for payments in local currency (INR) and enabling UPI as a payment option" — 2025-05-08, 574 views

> "$20 is like 10 days worth of food for the majority of people here, and I think it seems too costly to afford. It will be nice if we have the same accessibility for such a powerful tool like the rest of developed country." — Indonesia, 2024-11-21

Cursor is one step ahead and only one: it ships an **India-specific INR entry plan**, but premium tiers stay USD-only at roughly a **30% effective markup** (2026-07-28, 6 likes).

**Vietnam appears in this data on 2026-05-25.** This is the only gap in the pull that the team is positioned inside rather than outside.

Honest limit: the forum threads carry 1–2 posts and 1 like each. Low forum visibility, not measured demand. India and Indonesia are widely reported top-10 ChatGPT markets, which was not independently verified this session.

## The other four, ranked and small

**1. Bring-your-own-model meeting notetakers.** Granola-style tools lock the intelligence layer to their own subscription. One Show HN (2026-07-19) built a fix explicitly to escape it — and scored **1 point**. The same complaint surfaces independently in Cursor's forum: "can the remote model support third-party models?" Real complaint, no credible product, and the one attempt got no traction at all.

**2. No programmatic path to file a tax return.** *"There is no Stripe for taxes."* AI can draft a return; a human must click submit. Someone is mid-build on an MCP server for it, with **IRS ATS certification in progress as of 2026-04-14**, unshipped at fetch date. Real gap, and the barrier is a government certification process, not code.

**3. Cursor's ACP integration, deprioritized in writing.** Vendor statement, 2026-09-09: auto-review mode for ACP-connected editors (JetBrains, PyCharm) is **"not on our immediate roadmap."** This is the safest gap shape there is — named, scoped, vendor-confirmed non-support. It is also tiny.

**4. Local, on-device meeting transcription.** Built at least twice within a month by independent developers, both motivated by *"I got tired of uploading my audio to a server."* Near-zero traction each time. Recurring demand, no winner, and two failed attempts is evidence about the market, not only about the builders.

## What not to build

**AI meeting notetakers are saturated.** Nine separate Show HN launches in a five-month window, May–September 2026. Nearly all scored 0–3 points. **One broke out — the YC-backed one, at 88 points.** That is the distribution reality of the category in one line.

**The "AI wrapper" complaint is a recurring pattern 2023 through 2026**, not a moment. It corroborates `../markets/creative-ai-lane.md`'s Jasper case from the demand side: buyers have learned to ask what happens when the underlying model ships the feature free.

## Four gaps that are already filled

Recorded so nobody chases them:

| "Gap" | Already fixed by |
|---|---|
| AI-SDR cold-email spam | "Unspam" for Google Workspace, ~1yr track record as of 2024 |
| AI content flood fatigue — **860 points, 401 comments** | A community tool, hnsansai |
| Cursor dropping Cyrillic/non-Latin keywords | Fix landing in v3.22, per staff reply the same day |
| Cursor India pricing | INR entry tier shipped. Premium tiers still USD-only |

The AI-content-flood thread is the highest-engagement complaint in the entire pull — 860 points — and it already has a fix. That is the shape of a gap that is not one.

## Orphaned users

Shutdowns leave pre-qualified demand. From a crowd-maintained tracker, unconfirmed against primary announcements:

- **Firebase Studio** — an agentic cloud development environment — discontinued 2025-03. Users had to migrate off entirely.
- **Pixel Studio** and **Doppl** — discontinued 2026, no successor named.
- **Amazon** winding down its Nova models and the Adept acqui-hire.
- **Humane AI Pin** — full shutdown 2025-02-18, verbatim terms on file.
- **Botkeeper** — AI bookkeeping, ~$90M raised, reported shutting down. **Unconfirmed by any primary source.**

No orphaned-user population here is large enough to be a business on its own. Recorded for pattern.

## Read for this team

- **The access gap is the only one where being in Ho Chi Minh City is an advantage rather than a cost.** Everything else in this file could be built better by someone closer to the buyer.
- **Every other gap found is small.** A 1-point Show HN, a deprioritized IDE integration, a category with nine competitors. None supports the engagement pricing in `../markets/ai-attack-defense-services.md`, and none is a two-person business on its own.
- **The gap-hunt was crippled by blocked channels and should be re-run.** Reddit is now reachable with browser access. This file's conclusions are provisional on that.

No verdict. Per `../../CLAUDE.md` that is the user's.

## Caveats

- **Reddit was unreachable for the entire session** — r/SaaS, r/Entrepreneur, r/artificial, r/LocalLLaMA, r/ExperiencedDevs all contributed nothing. G2 and Capterra returned 403. WebSearch was exhausted before the agent started.
- Forum engagement counts are **visibility proxies, not demand measurements.** A 1-like thread may mean nobody cares or may mean nobody found it.
- killedbygoogle.com is community-maintained. Every shutdown date here is crowd-derived and unconfirmed against a vendor announcement.
- Botkeeper's shutdown has no primary confirmation.
- Show HN point counts measure Hacker News, a single self-selected audience, on the day of posting.
- The Discourse `/search.json` channel is a genuine methodological find and is reusable. It is also limited to vendors who run Discourse forums publicly.
