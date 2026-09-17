# Gap pulls — the four things wave 2a could not source

Wave 1c, 2026-09-17. Closes the four gaps named in wave 2a's attack list (`../plan/idea-set.md`, items #3, #7, #8, #12). Does not evaluate the idea set, does not edit `idea-set.md` — that is 2b's file to own. Each raw pull is in `../../raw/gap{1,2,3,4}-*-2026-09-17.md`.

## Gap 1 — does a cheap competitor-price tracker already exist for small B2B SaaS?

The one that can kill candidate B. Full detail: `../../raw/gap1-price-tracker-tools-2026-09-17.md`.

| Tool | Segment | Cheapest paid tier | Interprets or only diffs | Targets B2B SaaS pricing pages? |
|---|---|---|---|---|
| Visualping | page-change monitor | $14/mo ($10/mo annual) | AI summary of a diff, every tier | No — general web monitoring |
| Distill.io | page-change monitor | $15/mo | Diff-based, no AI-interpretation claim found | No — dev/QA/power-user framing |
| ChangeTower | page-change monitor | $12/mo | "AI monitoring on every monitor"; ships an MCP integration at $78/mo tier | No — general, but closest to AI-native of this segment |
| Hexowatch | page-change monitor | unknown — only Enterprise ($999/mo) tier surfaced | unknown, not surfaced | No — agency/mid-market framing at the visible tier |
| Wachete | page-change monitor | unknown — pricing page 404'd twice | Diff-based, no AI-interpretation claim | No — general (prices, content, uptime, jobs, compliance) |
| Fluxguard | page-change monitor | $110/mo | unknown, not surfaced | No — enterprise QA/legal/brand framing |
| Versionista | page-change monitor | unknown — no price surfaced anywhere fetched | unknown | unknown |
| Prisync | e-commerce repricer | $99/mo | Diff + dynamic-pricing recommendation | No — explicit e-commerce SKU tracking |
| Price2Spy | e-commerce repricer | unknown — no numeric price published | unknown | No — explicit retailer/e-commerce framing |
| Competera | e-commerce repricer | unknown — contact-us only | Recommendation engine, not a memo | No — enterprise omnichannel retail at scale |
| Klue | competitive-intel suite | unknown — contact-us only | Aggregates many sources into battlecards | No — enterprise sales/GTM, many competitors |
| Crayon | competitive-intel suite | unknown — contact-us only | Aggregates into battlecards | No — enterprise CI programs |
| Kompyte | competitive-intel suite | unknown — contact-us only | Aggregates across many channels | No — enterprise sales/marketing teams |

**What this means for candidate B**: no vendor across 13 checked, in any of the 3 adjacent segments, sells "a dated, interpreted pricing fact for a SaaS founder" as its product. The nearest things are AI-summarized page-diffs (Visualping, ChangeTower) bundled into general-purpose monitoring tools at $12-35/mo — that is a commodity feature, not a researched pricing fact with a memo cadence, and it is not SaaS-pricing-specific. E-commerce repricers and enterprise CI suites both explicitly serve different buyers (retail SKU pricing; enterprise GTM teams tracking many competitors) at price points and feature sets that don't match a 3-10-person SaaS founder watching one competitor's one pricing page. **Candidate B, scoped exactly as idea-set.md scopes it (recorded fact, not the repricing recommendation), is not directly served by any tool found.** The risk that remains: a generic page-diff tool plus a prompt is a build any of these vendors could ship in a sprint if they wanted the SaaS-founder segment — this pull found no evidence they have, not evidence they can't.

**Gap 1: partially closed.** Closed for the 13 named tools with a public or near-public pricing page (11 of 13 gave usable pricing; 2 — Hexowatch's lower tiers, Versionista — gave none). Not closed in the sense of an exhaustive market scan; a narrower or newer entrant aimed exactly at "SaaS pricing page + AI memo" was not searched for by name (budget was spent confirming the named list from the brief, not discovering new entrants).

## Gap 2 — Claude Pro/Max subscription allowance, in numbers

Full detail: `../../raw/gap2-claude-subscription-limits-2026-09-17.md`.

| Figure | Value | Label | Date |
|---|---|---|---|
| Current (2026-09) exact token/message/hour figure for the 5-hr or weekly window | **not published anywhere checked** | — | checked claude.com/pricing 2026-09-17 |
| Pro weekly Sonnet 4 allowance (2025 baseline) | 40-80 hrs/week | company-stated (to TechCrunch) | effective 2025-08-28 |
| Max $100/mo weekly allowance (2025 baseline) | 140-280 hrs Sonnet 4 + 15-35 hrs Opus 4/week | company-stated (to TechCrunch) | effective 2025-08-28 |
| Max $200/mo weekly allowance (2025 baseline) | 240-480 hrs Sonnet 4 + 24-40 hrs Opus 4/week | company-stated (to TechCrunch) | effective 2025-08-28 |
| 5-hour rate limits doubled | — (no absolute figure given) | third-party-reported, citing Anthropic | 2026-05-06 |
| Temporary weekly boost | +50% | company-stated, third-party-relayed | ran 2026-05-13 through ~2026-09-13 |
| "Permanent" weekly increase | +25% over pre-boost 2025 baseline | company-stated (@ClaudeDevs post, third-party-relayed) | effective 2026-09-14 |
| Net change vs. the boosted level in place through mid-Sept | **-17%** | company-stated (Anthropic's own clarification, third-party-relayed) | as of 2026-09-14 |

**What this means**: Anthropic confirms no exact current number publicly — this itself is the answer to half the question. It has, however, twice given the press/public concrete company-stated figures: absolute hours at the 2025 launch, and percentage deltas since. No source anywhere gives an updated absolute-hours figure for the current (post-2026-09-14) level; the two data points must be combined (25% up from a known 2025 baseline) to get even a rough current estimate, and that combination is this pull's own arithmetic, not an Anthropic-published number — flagged as such in the raw file. Directional estimate for a Pro seat: roughly 50-100 hrs/week of Sonnet-class usage, not a confirmed figure.

**Gap 2: partially closed.** The "does Anthropic publish a number" question is fully closed (no, confirmed absent from current docs). The "what is the number" question is only partially closed — company-stated absolute figures exist but are 14 months stale relative to 2026-09, and only percentage changes have been published since.

## Gap 3 — payment rail out of Vietnam for recurring USD

`../../../../docs/markets/vietnam-sg-access.md` checked first, per instruction — it already covers Stripe (VN unsupported), Paddle as a concept, Upwork+Payoneer working from VN today, and the Singapore route. This pull adds only what that file left open. Full detail: `../../raw/gap3-vietnam-payment-rails-2026-09-17.md`.

| Option | Accepts a Vietnam-registered business? | Requires | Fee |
|---|---|---|---|
| **Paddle** (MoR) | Not on its 28-country exclusion list — supported by omission, not by named inclusion | Standard KYC, "further information...for risk and compliance purposes" at Paddle's discretion | 5% + $0.50/transaction; +1.5-2% FX spread if payout currency differs; Retain (dunning) 10-15% of recovered revenue if used |
| **Lemon Squeezy** (MoR) | **Yes — Vietnam named explicitly** in its bank-payout supported-country list | Standard onboarding (not detailed in fetched page) | 5% + $0.50/transaction base; +1.5% international, +1.5% PayPal, +0.5% subscriptions, +5% abandoned-cart recovery, +3% affiliate (third-party-reported add-ons) |
| **Payoneer** | Yes — already confirmed working from Vietnam in the existing research file | SBV-approved rail already in use per existing file | Up to 3.99%+$0.49 on card-funded receipts; 0.5% balance conversion; 1.2-4% (min $20) VND withdrawal conversion; $29.95/yr if <$6,000/yr received |
| **Wise Business** | **Unresolved** — third-party-reported as NOT available for a Vietnam-registered company (country greyed out in signup flow per a secondary source); Wise's own eligibility page 404'd, not independently confirmed | — | one data point only: SWIFT USD receipt ~$6.11, not VN-corridor-specific |

**Contradiction flagged for wave 2b**: `idea-set.md`'s own caveats section states Paddle's "Vietnam-specific seller eligibility" was left unstated either way. This pull resolves it to **likely-yes-by-omission** (Paddle) and **explicit-yes** (Lemon Squeezy, a second MoR option not previously named in the project's files) — both stronger than "unstated," neither is a first-party "yes" in the way Lemon Squeezy's named list is for itself.

**Gap 3: closed** for the two MoR options and Payoneer (each has vendor-page-level evidence). **Partially closed** for Wise Business (a real, unresolved gap — its own eligibility page could not be reached).

## Gap 4 — Shopify App Store volume (timeboxed)

Full detail: `../../raw/gap4-shopify-marketplace-volume-2026-09-17.md`.

| Figure | Value | Label |
|---|---|---|
| App count | 18,488 (one aggregator) vs. ~13,000 (another aggregator) | third-party-reported, conflicting, unreconciled |
| Active stores tracked | 2,111,146+ | third-party-reported (StoreCensus's own proprietary tracking, explicitly not Shopify's published data) |
| Total app installs | 13.0 million+ | third-party-reported (StoreCensus) |
| Avg apps/store | 6.2 | third-party-reported (StoreCensus) |
| Cumulative developer earnings | $1B (attributed to a Shopify Q2 2026 earnings release, per a secondary source — not independently verified) vs. $1.5B (unattributed aggregator claim) | conflicting, unreconciled, neither independently verified against a Shopify-first-party page |
| Median app earnings | under $1,000/month | third-party-reported (weekonelabs.com, via search summary only, not fetched directly) |

**What this means for candidate G**: directionally large and power-law-distributed (a few apps do very well, the median app earns under $1,000/mo per one unverified source), but no figure here was traced to a Shopify-first-party page, and two headline figures (app count, cumulative earnings) conflict across sources.

**Gap 4: unreachable at this timebox for a precise or first-party number** — the directional shape (large market, power-law earnings, median app trivial) is as far as the budget allotted for this gap goes.

---

## Closing status, one line per gap

1. **Gap 1 (competitor-price tracker): partially closed.** No tool found matches candidate B's exact scope across 13 checked vendors; absence of a discovered competitor is not proof none exists.
2. **Gap 2 (Claude subscription allowance): partially closed.** Confirmed Anthropic publishes no current exact figure; company-stated absolute figures exist but are from 2025, updated only by percentage since.
3. **Gap 3 (Vietnam payment rail): closed** for Paddle, Lemon Squeezy, and Payoneer; **partially closed** for Wise Business (primary eligibility page unreachable).
4. **Gap 4 (Shopify marketplace volume): unreachable** for a precise, first-party, non-conflicting number within the timebox; directional shape only.
