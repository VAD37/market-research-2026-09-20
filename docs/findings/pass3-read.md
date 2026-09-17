# Pass 3 — the team, the market, and the access problem

Ran 2026-09-16. Six agents: five launched in parallel, one recovery pass with browser access added mid-run. Compiled from `two-founder-cases.md`, `market-gaps-2026.md`, `localization-play.md`, `../markets/creative-ai-lane.md`, `../markets/vietnam-sg-access.md`, `../customers/first-customers.md`.

Reads on top of `pass2-read.md`. Where they disagree, this file is later.

Pass 1 and 2 tested three product ideas. **Pass 3 tested the team.** The geography was confirmed mid-pass: Ho Chi Minh City, abundant dev talent, no US market access.

## The four findings that move the decision

**1. The pairing that wins is technical + domain expert, not technical + business person.**

Two agents searched independently — one across two-founder AI companies generally, one across creative-technical pairs specifically. **Neither found a single company pairing a purely technical founder with an animator, filmmaker or professional storyteller.**

What they found instead: Harvey is a litigator plus a DeepMind researcher, selling to law firms — **$190M revenue in 2025, $550M raised at $15.5B on 2026-09-16.** Photoroom is GoPro's image-editing product lead plus a computer-vision engineer, selling image editing. In both, the non-technical founder *was the customer*.

Every documented failure in the set — Humane, Argo AI, Neeva — was a same-background pair with nobody from the buyer's side.

This does not say the partnership cannot work. It changes the question from *"can a storyteller run the business half"* to **"which market makes a storyteller the domain expert."** That is now F1.

**2. Storytelling is not a moat, tested three ways.**

Tome was named and branded around narrative, reached **20–25M users**, raised **$81.5M**, and died with **ARR under $4M**. Jasper had a real brand and lost most of its revenue when a free substitute appeared. Humane had a TED talk, Sam Altman's money and **fewer than 10,000 units shipped.**

Independently, the localization agent found the same mechanism stated as a rule: *"When your competitive advantage is 'we wrote a better prompt,' you're one API update away from irrelevance."*

**3. Stripe does not support Vietnam, and the workarounds are worse than they look.**

Singapore is on Stripe's list. Vietnam is not — nor are the workarounds clean. A browser pass reached Reddit and found Stripe support confirming, **2026-06-16**, that *"US-based accounts must have a physical presence in the United States."* Mercury and Brex apply US residential-address KYC. Non-US-owned single-member LLCs owe an annual **Form 5472 with a $25,000 penalty** that Stripe Atlas does not mention.

The cheapest-looking route is the most broken one.

**4. The clone playbook does not survive the AI era, and the regulatory wedge protects the wrong party.**

Taobao beat eBay on **Alipay escrow** — share **8%→59%** while eBay fell **79%→36%**. Flipkart on cash-on-delivery logistics. Nubank on credit underwriting. Every historical win rests on infrastructure that takes years and capital. **A prompt layer over a rented US model inherits none of it.**

Vietnam's AI Law — passed 2025-12-10, effective **2026-03-01** — does require foreign high-risk-AI providers to hold a commercial presence or authorized representative. Real. But AWS, Google and Microsoft already clear it. **It burdens a US startup your size, not OpenAI.**

## Scorecard, revised for the team

| | `ai-search-ads` | `agent-dashboard` | `ai-attack-defense` | `creative-AI` |
|---|---|---|---|---|
| Buyer exists | Yes, named | Yes | Yes | Yes |
| Price floor | $29/mo | — | **$3,500 published** | **$500/video** |
| Works at n=1 | No | No | **Yes** | **Yes** |
| Reachable without US presence | No | No | **Partly** | **Yes** |
| Team is the domain expert | No | No | **No** | **Yes — one half** |
| Automation risk | Low | Moderate | **High, active** | **High** |
| Storyteller has a real job | No | No | Report-writing only | **Yes** |

No row wins outright. The two right-hand columns split the criteria between them, which is the actual state of the decision.

## What pass 3 killed

- **"Migrate a US product to Vietnam."** The historical wins needed moats this team cannot build; the AI version of the play is being killed in public right now.
- **"Two founders is ideal" as evidence.** It traces to one 2011 survey of **650 surviving startups** whose own co-founder conceded survivorship bias and a sample *"too small"* for cross-validation. The primary report is offline.
- **The $3,000–$7,000/mo creative retainer.** Wrong pricing unit. Creative AI bills per deliverable.
- **The 2024 animation-apocalypse data.** Otis College, April 2026: *"The jobs disappeared, but the economic data says AI did not cause it"* — and roles most exposed to AI **grew in number**.
- **Any CAC figure.** The circulating $536–$702 recurs near-verbatim across eight SEO domains with no methodology anywhere.

## What pass 3 strengthened

- **Services over product, for a third independent reason.** Upwork and Payoneer work from Vietnam today. Stripe and AWS Marketplace do not. The rails that are open are the services rails.
- **The cost base is real.** Senior Vietnamese backend ~**$27,000/year** against a US median of **$133,080**. The median profitable micro-SaaS at ~$4,200 MRR is under 40% of a US salary and about **two years** of a senior local one.
- **Report-writing as the durable half.** Pass 2 found it in HackerOne's own words. Pass 3 adds that discovery-side channels are measurably decaying: cold email **8.5% (2019) → 3.43% (2026)**, cybersecurity at **4.86%**.

## The tension to sit with

**The best-evidenced acquisition channel requires the access this team does not have.** The one consultant found charging **$10,000/week** built it through 1-on-1 pro-bono help inside Y Combinator's network — San Francisco proximity. The two channels that a remote team can run are the two with quantified failures attached.

And the one documented case of exactly this division of labour, from Reddit, 928 points: the non-technical cofounder *"Brought in our first 8 customers. Ran sales calls."* Then took a **$190K** job and kept **40% of the company.**

That is not an argument against the partnership. It is an argument for settling F7 and A6 — what the non-technical founder does in months 1–6, and what the equity agreement says — before anything gets built.

## Open — pass 4

Ranked in `../method/open-questions.md`, group F. The three that decide something:

1. **F1 — which market makes a storyteller the domain expert?** Everything about the team shape resolves here.
2. **F2 — does a Singapore Pte Ltd actually get a working Stripe account for Vietnam-resident founders?** The whole access strategy rests on an inference from a country list. Nobody tested it.
3. **F5 — find the Vietnamese-language founder community.** Two independent English-language searches found no first-person account of selling into the US from Vietnam. The document this team most needs may exist only in Vietnamese.

## Caveats

- **WebSearch was exhausted at 200/200 before pass 3 began**, session-wide. Five of six agents ran entirely on direct fetch, no-auth APIs and DuckDuckGo Lite scraping. The sixth had browser access and produced the highest-confidence material in the pass — the same pattern as pass 2.
- **Reddit was blocked for two agents and open for the third.** `market-gaps-2026.md` is provisional on a re-run (F6).
- **No first-person account of a non-US founder selling into the US was found by either of the two agents that looked.**
- Wikipedia and trade aggregators carry the historical and company material. No filings were read this pass.
- The founder-count, CAC and AI-wrapper-death sources are all, in different ways, weaker than they present themselves. Each is labelled in its own file.

No verdict. Per `../../CLAUDE.md`, that is the user's. The fourth idea slot in `../method/scope.md` is still blank.
