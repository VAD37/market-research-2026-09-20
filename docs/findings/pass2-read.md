# Pass 2 — what changed

2026-09-16. Five agents, parallel. Compiled from `../customers/answer-integrity-buyer.md`, `injection-feasibility.md`, `../markets/ai-trend-suite.md`, `../markets/ai-attack-defense-services.md`, and the corrections applied from `../raw/verify-pass2-pulls.md`.

Reads on top of `cross-read.md`, which holds pass 1. Where the two disagree, this file is later.

## The three findings that move the decision

**1. The answer-integrity buyer exists, and one vendor is already selling to it.**

BrandShield launched AI Platforms Protection **2026-04-01**, monitoring ChatGPT, Gemini, Perplexity and Grok for "impersonation, phishing links, misinformation, and counterfeit promotion." Sold into the brand-protection budget.

Seven other DRP vendors were checked individually — Doppel, Memcyco, Bolster, Netcraft, ZeroFox, and two unreachable. None cover answer content. **One of eight moved.** Pass 1's "no buyer found" was a real gap that is now closing at one vendor's pace, not a permanent vacancy.

**2. The services lane's price floor is lower than pass 1 recorded, and automation is visibly eating its discovery half.**

Cobalt publishes **$3,500** for an autonomous pentest, below pass 1's $8k floor. Three vendor price sheets show **no AI premium** — AI testing bands overlap standard web-app bands. XBOW, an autonomous pentester, took **#1 on HackerOne's US leaderboard** and raised $75M then $120M while advertising "coverage without the headcount." HackerOne cut IBB payouts **over 75%** on 2026-05-22, naming AI tooling as the cause, and paused the program.

**3. Nobody is required to buy AI security testing. Auditors demand it anyway.**

Every regime checked — NYDFS, FCA, ISO 42001, SOC 2, EU AI Act — stops short of mandating red-teaming. And yet SOC 2 auditors demand "red-team suites" and "prompt-injection test artifacts" while, in the same source's words, *"the AICPA has published no authoritative AI-specific SOC 2 standard."*

That is a better demand driver than the one pass 1 was waiting for. Auditor discretion pays in 2026. The EU AI Act pays in 2027-12 at the earliest.

## The technical question, answered

Crawler identification from a domain you own: **yes, by published IP range or forward-confirmed rDNS, never by user-agent.** OpenAI, Anthropic, Perplexity, Amazon, Apple and Common Crawl all publish both. `OAI-AdsBot` is separately documented with its own IP file — the ChatGPT ad pipeline is observable independently of search.

Two hard limits:

- **Declared identity is not reliable.** Cloudflare documented Perplexity's undeclared crawler impersonating Chrome, running outside its own published IP range, rotating ASNs to evade robots.txt — 3–6M daily requests against 20–25M declared.
- **The tactic is named in Google's spam policy.** Serving different content on crawler detection is the cloaking definition, verbatim: "inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor." Intent is the hinge.

The reusable asset is the measurement method, published across four papers: real dataset → baseline with no intervention → controlled intervention → **transfer test against a live production engine**. Step four is what nobody sells.

**Resolved 2026-09-16, after this pass closed.** The user granted browser access and the four 403'd ToS pages were read directly. Consumer surfaces are closed — OpenAI bars programmatic extraction of Output; Perplexity licenses "personal, non-commercial use only" and bars automated *and manual* collection. The paid API path carries no such prohibition in the documents read. Full text in `../raw/tos-browser-pulls.md`, read in `injection-feasibility.md`.

## Scorecard, revised

| | `ai-search-ads` | `agent-dashboard` | `ai-attack-defense` |
|---|---|---|---|
| Buyer exists | **Yes, and named** — brand protection, one vendor selling | Yes | Yes |
| Buyer proven to pay | **For visibility, yes. For integrity, one vendor, no price disclosed** | Developer tier only | Yes, $3.5k–$150k |
| Price floor | $29/mo (Otterly). Profound now Enterprise-only | — | **$3,500 published** |
| Consolidation risk | Moderate. Profound at $1.8B as of 2026-09-16 | **Severe** | High for product, nil for services |
| **Automation risk** | Low | Moderate | **High and active — XBOW, $195M raised** |
| Demand driver | Google spam policy — a constraint | None found | **Auditor discretion, live now** |
| Regulatory date | — | — | GPAI in force 2025-08-02; high-risk **2027-12-02** |
| Works at n=1 | No | No | **Yes, still the only one** |

## What pass 2 killed

- **Pass 1's "the services lane is untouched."** Untouched by acquirers. Not by automation.
- **The $8k floor.** It is $3,500, published.
- **The AI premium.** Three price sheets say there isn't one.
- **The idea that government procurement would validate the price band.** Zero hits for "penetration testing" and zero for "prompt injection" across 700 federal AI contracts. The money goes to tooling R&D (HiddenLayer, $1.80M and $1.25M from USAF), not to buying engagements.

## What pass 2 strengthened

- **Services still the only shape that pays at n=1.** Nothing found contradicts that. The wide market read found no two-person AI *product* case earning what one engagement pays: 54% of Stripe-verified indie products earn zero; the median profitable micro-SaaS is ~$4,200 MRR.
- **28% of YC's W26 batch are "AI-native service" companies** — the largest delivery-model slice in the batch, and 64% of the batch is exactly two co-founders.
- **The report is the defensible artifact.** HackerOne's own framing: discovery is commoditised, but "verifying impact, deduplicating reports, making patch decisions, and coordinating disclosure remains an irreducibly human and time-intensive process." Pass 1 called report-writing the non-technical partner's role. That now looks like the durable half rather than the soft half.
- **Bessemer, independently: "Moats form at the data layer, not the model layer."** Same conclusion pass 1 reached from Lakera's adversarial corpus.

## Corrections applied to pass-1 files

| Item | Was | Is |
|---|---|---|
| Hermes Agent stars | 100k / 214k / 246k, unverified | **246,092 confirmed** via GitHub API. 51,404 forks, 401 contributors |
| PyRIT stars | 115 | **4,483** — the 115 was an archived stub repo |
| Digital Omnibus | Status unknown, proposal or law | **Law.** Regulation (EU) 2026/1744, OJ 2026-07-24, in force 2026-07-27 |
| GPAI obligations | 2026-08-02 | **2025-08-02** — in force over a year. Pass 1 conflated it with Art. 50 |
| Annex III / Annex I high-risk | 2027-12-02 / 2028-08-02 | **Confirmed exactly** |
| Google spam-policy date | 2026-05-15 | Wording confirmed; **date unconfirmed**, secondary press only |
| Profound valuation | $1B vs $1.8B "conflict" | **Both right** — Series C 2026-02-24, Series D $180M **2026-09-16** |
| Profound pricing | $99–$399 + Enterprise | **No public self-serve tier at all** |
| AthenaHQ | $595/mo | **Free + Starter $295 + Enterprise** |
| Peec AI ARR | $10M claimed | **$4M+ in 10 months** per the company's own post. $10M untraceable |
| Peec AI founders | Two conflicting lists | **Drabo, Siwonia, Meiners.** Tracxn was wrong |
| Promptfoo acquisition | "Mar 2026," unverified | **2026-03-09**, company-announced, terms undisclosed |
| CalypsoAI $180M | Implied filed | **Absent from F5's 8-K.** Press-reported only |
| Decawork | "IT approval gate" | Policy approval across marketing, HR, IT, security, finance, engineering. Founders Aman Raj, Sarthak Aggarwal |
| Otterly $29/mo | Aggregator | **Confirmed** on the vendor page |

Four SEC filings were read directly (Cisco 8-K, CrowdStrike 8-K, Check Point 6-K, F5 8-K). All four **confirm the acquisition and state no dollar figure.** Only Protect AI's $634.5M is a filed number anywhere on this board.

## Open — pass 3

Ranked by decision impact.

1. **Does anyone pay BrandShield for it?** A launch is not a customer. Find a named buyer, a contract value, or a renewal. That number decides idea 1.
2. **Read OpenAI's and Perplexity's ToS.** Four pages, four 403s. Needs a browser, not a fetch tool. Decides whether a measurement product is operable.
3. **Is the Conductor survey's GEO budget new money or reallocated?** Two readings of the same 250-exec survey disagree. Additive means an integrity line has a source. Zero-sum means it fights SEO for the same dollars.
4. **Price a real engagement.** Government procurement returned nothing. Try a published SOW, a rate card, or ask a boutique directly.
5. **Find one solo or two-person operator earning from AI security work.** None found. This is the closest available proof or disproof of the whole services thesis at team size.
6. **Confirm Cato/Aim and Cranium/AIceberg** against a primary. Both sites are JS-rendered SPAs.
7. **Repeat the YC pull against S26** once independent analyses mature — W26 was the substitute.
8. **2026 status of ratified animation-union AI language.** The best data on file is dated 2024-04-11.

## What this pass still does not say

No verdict. Per `../../CLAUDE.md`, that is the user's. The fourth idea slot in `../method/scope.md` is still blank.
