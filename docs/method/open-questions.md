# Open research questions

Register of what this repo does not yet know, organised by the decision each question serves. Opened 2026-09-16 at the start of pass 3.

A question leaves this file when a compiled doc answers it with a sourced number, or when it is killed as unanswerable. Answered questions move to `../findings/`.

## Standing frame

Two people. One technical, one business and creative — animator, storyteller, customer-facing. The team shape is fixed; the product is not. Every question below is scored against that shape, not against a generic startup.

## A — the team question

| # | Question | Why it decides something |
|---|---|---|
| A1 | ~~What do successful two-founder AI companies look like?~~ | **Answered** — `../findings/two-founder-cases.md` |
| A2 | In the technical + non-technical pairs, what does the non-technical founder actually do all day? | Defines the collaborator's job before, not after, the handshake |
| A3 | ~~Does the founder-count data favour two?~~ | **Closed as folklore.** Traces to one 2011 survey of 650 survivors; its own author conceded survivorship bias |
| A4 | Which two-founder AI companies failed, and did the split cause it? | Survivorship bias is the default failure of this kind of research |
| A5 | ~~Has a storyteller-plus-engineer pair built anything that earns?~~ | **Answered: none found.** Two independent searches. The winning pattern is technical + *domain expert* |
| A6 | What does a first-time non-technical founder's equity and role agreement normally look like? | Unasked, and it gets expensive later |

## B — the market question

| # | Question | Why it decides something |
|---|---|---|
| B1 | ~~A specific, evidenced, unfilled gap?~~ | **Partly.** Best one is non-US access, broken 2022–2026. Rest are thin — `../findings/market-gaps-2026.md` |
| B2 | Which categories are overcrowded enough to disqualify? | Knowing what not to build is cheaper than knowing what to build |
| B3 | Where do incumbents say on the record they will not go? | Safest gap there is |
| B4 | Which AI products shut down in 2025-2026, and where did their users go? | Orphaned users are pre-qualified demand |
| B5 | Is the AI funding environment open to a two-person team, or only to mega-rounds? | Pass 2 found $510B H1 2026 with falling deal counts. Resolve what that means at seed |
| B6 | ~~Real price for the creative lane?~~ | **Answered.** Bills per deliverable, not per month — `../markets/creative-ai-lane.md` |

## C — the localization question

| # | Question | Why it decides something |
|---|---|---|
| C1 | ~~Does re-pointing a US product at a local market work?~~ | **Answered: only with a slow, capital-intensive moat** — `../findings/localization-play.md` |
| C2 | What specifically has to be localized — payments, language, regulation, sales motion — and which of those a US vendor cannot cheaply copy? | The whole moat lives in this answer |
| C3 | ~~Does the clone playbook survive a rented US model?~~ | **Largely no.** A prompt layer inherits none of the historical moats |
| C4 | Can a local market pay US prices, and does it buy subscriptions or project work? | Decides the business model before the product |
| C5 | ~~A local regulatory wedge?~~ | **Real but inverted.** Vietnam AI Law in force 2026-03-01 burdens small US entrants, not platforms |
| C6 | Who already sells AI locally, at what price, at what size? | Competition, and a hiring or partnering pool |

**Assumption resolved 2026-09-16.** The user confirmed: **Ho Chi Minh City, Vietnam**, abundant local dev talent, **no US market access**. Singapore entered scope as the access layer. Nothing in group C was discarded.

## D — the distribution question

Newest lane, and the one the repo has least on.

| # | Question | Why it decides something |
|---|---|---|
| D1 | How do two-person companies get the first ten paying customers? Channel, not product | Everything above is moot without this |
| D2 | ~~Cold email and LinkedIn conversion rates?~~ | **Answered.** Cold email **3.43%** platform-wide; LinkedIn DM 10.3%. Cybersecurity **4.86%** |
| D3 | Does published research generate inbound for a technical services practice, with numbers? | This repo is itself the test case. If yes, the research is the marketing |
| D4 | Can a storyteller's content produce pipeline, and how long does it take? | The collaborator's half of the business, priced in months |
| D5 | ~~Do marketplaces pay at two-person scale?~~ | **Partly.** Shopify **0% to $1M**; AWS excludes Vietnam entirely. No small-vendor revenue found |
| D6 | ~~What does the first customer cost?~~ | **Closed as unsourceable.** The circulating $536–$702 recurs verbatim across eight SEO domains with no methodology |

## E — carried over from pass 2, unanswered

| # | Question | Status |
|---|---|---|
| E1 | Does anyone actually pay BrandShield for answer-engine integrity? | Open. A launch is not a customer |
| E2 | OpenAI's and Perplexity's ToS on automated querying | **CLOSED 2026-09-16** via browser. Consumer surfaces barred, API path not. See `../raw/tos-browser-pulls.md`. Successor: read both API agreements |
| E3 | Is GEO budget new money or reallocated from SEO? | Open. Two readings of one 250-exec survey |
| E4 | Real engagement price from a published SOW or rate card | Open. Federal procurement returned zero |
| E5 | One named solo or two-person operator earning from AI security work | Open. None found in 246 source blocks |
| E6 | Cato/Aim and Cranium/AIceberg against a primary source | Open. Both sites JS-rendered |
| E7 | YC S26 batch composition | Open. W26 used as substitute |
| E8 | ~~Animation Guild AI provisions, 2026~~ | **Answered.** Ratified 76.1% Dec 2024. Notice and transparency; **no opt-out, no training ban** |

## What this file is not

Not a backlog to clear. Several of these are unanswerable with public sources and will be closed as such. `unknown — checked <channel> <date>` closes a question just as validly as a number does.

## Opened by pass 3 — 2026-09-16

| # | Question | Why |
|---|---|---|
| F1 | Which market makes a storyteller the *domain expert*? | A5 says the pairing works only when the non-technical founder came from the buyer's world. This is the reframed version of the whole team question |
| F2 | Does a Singapore Pte Ltd actually get a working Stripe account for founders resident in Vietnam? | The SG route rests on this and it was never tested — only inferred from Stripe's country list |
| F3 | Will a US buyer contract with a Singapore entity run by Vietnamese founders? | Trust, not payments. Unanswered by any source |
| F4 | What is the real all-in first-year cost of the Singapore structure? | Nominee, filing, accounting, audit-exemption thresholds. S$315 is the incorporation fee only |
| F5 | Is there a Vietnamese-language founder community documenting US sales? | Two independent searches in English found nothing. Try "làm SaaS bán cho khách Mỹ" and local forums |
| F6 | Re-run the gap hunt with browser access to Reddit | `../findings/market-gaps-2026.md` was crippled by the block and its conclusions are provisional |
| F7 | What does the non-technical founder do in months 1–6, specifically? | A2 is still unanswered. The one documented case of this exact split ended with that founder taking a $190K job and keeping 40% |
