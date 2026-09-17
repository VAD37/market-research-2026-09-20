# AI product and solution-suite trends — wide read

Pass 2, 2026-09-16. Compiled from `../raw/ai-trend-suite-pulls.md` (49 blocks) and `../raw/ai-trend-suite-source-index.md`. Wide-angle counterpart to pass 1's three deep reads.

Health warning on this whole file: the category-level claims here lean heavily on VC thesis documents (Bessemer, a16z, Menlo, Euclid) and trade blogs. Those are interested parties. Every number is labeled. Treat the disclosed-revenue rows as strong and the percentage claims as weak.

## Where the capital went

| Figure | Period | Source |
|---|---|---|
| Global venture funding **$510B**, above all of 2025's $440B | H1 2026 | Crunchbase, analyst-derived |
| **70%+** of global capital to AI companies, from just under 50% | Q2 2026 | Crunchbase |
| **80%** of North American investment to AI, across all stages | Q2 2026 | Crunchbase |
| OpenAI and Anthropic alone took **$217B — 43% of all H1 funding** | H1 2026 | Crunchbase |
| Deal count "well below prior high marks" | H1 2026 | Crunchbase |

Last row is the one that matters at two people. Record totals with falling deal counts means a handful of mega-rounds, not a broad funding environment. Seed and angel was ~$4.9B of Q2's $137.2B in North America.

Enterprise spend, from Menlo's survey of ~500 US decision-makers (analyst-derived): **$37B on generative AI in 2025**, up 3.2x from $11.5B. Of that, $19B on applications — Horizontal $8.4B, Departmental $7.3B, Vertical $3.5B.

## Revenue that is actually disclosed

Strongest evidence in this pass. Company-stated or from paid research firms, not forecasts.

| Company | Revenue | As of | Label |
|---|---|---|---|
| Anthropic | $65B run-rate | Jul 2026 | trade press |
| ElevenLabs | $500M ARR | 2026 | trade press |
| Replit | $525M, from $300M in four months | Apr 2026 | analyst-derived |
| Lovable | $500M ARR, from $200M in eight months | Jun 2026 | analyst-derived |
| Perplexity | **$500M** vs **$750M** — two sources, unreconciled | 2026 | analyst-derived, conflicting |
| Harvey | $190M → $300M | Jan → May 2026 | analyst-derived |
| Ironclad | $200M+, 40% YoY | 2026 | analyst-derived |
| Decagon | $100M, from $44M end-2025 | Jul 2026 | Sacra |
| Clay | $100M, $1M→$100M in two years, NRR **200%+** | 2026 | **company-stated** |
| Legora | $100M ARR in 18 months | 2026 | Bessemer |
| Sierra | $150–200M ARR at $15.8B valuation | Feb 2026 | trade press |
| Synthesia | $100M ARR, ~500 staff, $200k/head | 2026 | secondary |
| Midjourney | **$300–500M on $0 raised**, profitable | 2026 | secondary, wide range |

Midjourney is the outlier worth staring at: no capital, profitable, in the creative lane.

Contract values where found: Decagon median ACV **$386,000** (range $95k–$590k, Vendr data). Intercom Fin sells at **$0.99 per resolution** on a $49/mo base. Harvey estimated $1,200–$2,000/seat/mo — Harvey does not publish pricing. LegalOn publishes ~$8,000/user/yr.

## The failure numbers — three, measuring three different things

Do not reconcile these. They are not the same metric.

| Claim | Metric | Source |
|---|---|---|
| **95%** of pilots delivered no measurable P&L impact | Six-month post-pilot ROI | MIT, "The GenAI Divide," Jul 2025 |
| **47%** of AI deals reach production, vs 25% for traditional SaaS | Deal-to-production conversion | Menlo, ~500 respondents |
| **88%** of agent pilots fail to graduate | Pilot-to-production, agents only | unattributed, weak |
| **40%+** of agentic AI projects canceled by end-2027 | Forecast | Gartner, 2025-06-25 |

The MIT study is the one everyone quotes and the one with the thinnest base: 52 interviews the report itself calls "directionally accurate based on individual interviews rather than official company reporting," plus 300 public deployments with undisclosed methodology. The published critique's charge is that it gained traction "not through rigor but because it fit a convenient narrative."

Menlo's number points the opposite way — **AI converts to production better than traditional SaaS.** Also from Menlo: only 16% of enterprise deployments qualify as true agents; the rest are "fixed-sequence or routing-based workflows wrapped around a single model call."

## Consolidation — pass 1's pattern, now in four more categories

Pass 1 found the middle layer being absorbed in observability and security. Same pattern, confirmed elsewhere:

| Category | Absorption |
|---|---|
| Coding | GitHub Copilot bundled into ChatGPT Plus ($20) and Pro ($200). Windsurf's full agent set now requires Cognition's own editor; the VS Code plugin is in maintenance mode |
| Sales / GTM | HubSpot Breeze and Salesforce Einstein ship native AI in-platform |
| Legal | Thomson Reuters bought Casetext/CoCounsel for **$650M** (2023) — the base-rate deal |
| Video | Sora shut down; Kling, Seedance, Vidu, Wan named as replacements |
| Coding, again | SpaceX acquired Cursor/Anysphere at **$60B**, Q2 2026 |

Cognition valuing itself at $10.2B two months after buying Windsurf, then freezing the neutral plugin, is the cleanest single illustration: acquire the point solution, then steer users onto your own surface.

a16z dissents, expecting "continued divergence between AI native apps and AI models" and "Narrow Startups" capturing segments. That is an interested party's thesis, filed against the observed acquisitions.

## Vertical AI and the services thesis

The revenue is real and dated. The *explanation* is not.

Bessemer's claim (Jan 2026, VC thesis document): LLM-native vertical companies grow "approximately 400% year over year" at "roughly 65% gross margins," and the market cap will be "at least 10 times the size of legacy Vertical SaaS" because "vertical AI is not competing for IT budgets; it is competing for **labor budgets**, which are approximately ten times the size of the software market." Moats "form at the data layer, not the model layer."

That last line is the same conclusion pass 1 reached about Lakera's adversarial corpus. Two independent routes to the same place.

The weak figures, flagged: "2.3x higher average ROI" for vertical deployments, and "71% vs 32%" still generating value at six months. Neither names an underlying study. Do not use them.

**Services-as-software / AI roll-ups — real capital, wrong scale.**

| Vehicle | Capital | Note |
|---|---|---|
| General Catalyst Creation Fund | $800M → **$1.5B** | Accounting, legal, IT services, property management |
| Thrive Holdings | **$1B+** | OpenAI holds an ownership stake |
| Circeus | $120M equity, $220M total capital | 18 acquisitions |
| Long Lake ← Amex GBT | **$6.3B** | Single deal |
| Crescendo / PartnerHero | $50M+ ARR | Operating result |

This validates "services pay" at fund scale. It does **not** validate it at n=1. These are PE-shaped roll-up vehicles buying existing service businesses — the opposite shape from a two-person $8k–$50k engagement practice. The thesis and the lane share a name and nothing else.

## What actually works at two people

Two datasets, pointing in opposite directions.

**YC W26, 199 companies** (independent analysis of the public batch): **64% have exactly two co-founders.** 11% are solo. 3x more companies hit $1M annualized revenue than W25. Delivery model split: "AI-native service" 56 companies (28%), "AI-enhanced software" 45 (22%), developer infrastructure 34 (17%). The named traction outlier, Pocket at $27M ARR, is a hardware company — not an analog.

That 28% "AI-native service" share is the single most relevant number in this file. The largest slice of the most recent YC batch is selling a service, not a seat.

**Indie hackers, Stripe-verified data:**

| Tier | Share |
|---|---|
| Zero revenue | **54%** |
| Under $1,000 MRR | ~70% |
| Over $100k MRR | ~5% |
| Median *profitable* micro-SaaS | **~$4,200 MRR** (~$50k/yr) |

Against a US median developer salary of $133,080, the median profitable indie founder earns under 40% of a job. A second dataset with different buckets (50% under $1k, 20% $1k–10k, 10% $10k–100k, under 5% above $100k) is on file beside it, unreconciled.

Read against pass 1: no disclosed two-person AI *product* case was found earning what a single $8k–$50k security engagement pays. Two engagements a quarter beats the median profitable micro-SaaS outright.

## The creative lane — thin, and the good data is two years stale

Relevant because the collaborator is an animator.

Demand side: AI content services run a "performance-plus-retainer" model, **$3,000–$7,000/mo** small and mid-market, **$20,000+/mo** for enterprise ContentOps (secondary, unattributed). The stated economics: "AI production pricing sits well below traditional production costs, while clients still budget against the traditional benchmark — the gap becomes agency margin." A directory lists 282 AI creative agencies. No agency's actual books were found.

Supply side, from an article dated **2024-04-11** — the most specific sourced figures located, and two years old:
- US film, TV and animation employment ~550,000.
- **75%** of industry bosses "eliminated, reduced or consolidated jobs after introducing AI."
- Adam Fowler estimates **100,000+ of 550,000 jobs disrupted**.
- One-third of executives predicted AI would displace 3D modelers; ~15% flagged storyboard artists, illustrators and animators.

Union AI provisions from the 2023 WGA/SAG-AFTRA strikes exist; the Animation Guild round was a later, separate negotiation. **Its 2026 status was not found.** That gap is material to any plan involving animation labour.

Tooling: no revenue or funding figure was found for Runway, Pika, Luma, Kling or Higgsfield despite repeated attempts. All five: unknown — checked 2026-09-16. Higgsfield is described as an aggregator putting fifteen video models under one subscription.

Sora: OpenAI shut it down, with the date given as **2026-03-24** in one source and a September API sunset elsewhere. Cost ~$15M/day against revenue reported as **$3.4B/yr** in one blog and **$2.1M/yr** in another — a 1,600x conflict on the same cost base. Both secondary. Neither usable. Disney reportedly walked from a nine-figure partnership over deepfake risk.

## Claims checked and found false

Recorded so they do not propagate:

- **HubSpot acquiring Warmly (Jun 2026)** — the cited SiliconANGLE article contains no mention of it. Unverified, dropped.
- **Clio acquiring vLex for $1B** — not present in the article expected to carry it. Unverified, dropped.

## Caveats

- **The session's WebSearch quota hit 200/200 mid-pass.** Planned pulls on Gartner corroboration, Menlo's raw PDF, Bessemer's PDF, YC S26 specifics and named creative-agency financials did not run. This file is incomplete by quota, not by scope.
- Gartner's newsroom returns HTTP 403 to automated fetch. Every Gartner figure here is a secondary relay of a primary statement.
- YC data is **W26, not S26** as briefed. S26's demo day was 2026-09-10 — too recent for independent analysis. Repeat the pull when analyses mature.
- Perplexity ($500M vs $750M), Harvey (two as-of dates), Cursor pre-acquisition and Sora all carry conflicting figures, side by side above.
- Bessemer, a16z, Menlo and Euclid all hold positions in what they describe. Their percentage claims are marketing with footnotes.
- The 2.3x ROI and 71%/32% durability figures name no study. Weak.
- Animation figures are dated 2024-04-11 and carried forward for want of anything newer.
- Midjourney's $300–500M is a range from secondary sources with no primary disclosure.
