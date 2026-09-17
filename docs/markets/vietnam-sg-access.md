# Vietnam, Singapore, and the US access problem

Pass 3, 2026-09-16. Compiled from `../raw/sg-hcmc-scene-pulls.md` (33 blocks) and `../raw/sg-hcmc-scene-source-index.md`. Pulled with browser access after the user confirmed the team is in Ho Chi Minh City with no US market access.

Companion to `../findings/localization-play.md` when that lands — this file is the ecosystem and the access mechanics, not the localization theory.

## The load-bearing fact

**Stripe supports Singapore. Stripe does not support Vietnam.**

From Stripe's own country list, fetched 2026-09-16: Australia, Austria, Belgium, Brazil, Bulgaria, Canada, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Gibraltar, Greece, Hong Kong SAR, Hungary, **India (Preview)**, **Indonesia (Preview)**, Ireland, Italy, Japan, Latvia, Liechtenstein, Lithuania, Luxembourg, **Malaysia**, Malta, Mexico, Netherlands, New Zealand, Norway, Poland, Portugal, **Singapore**, Slovakia, Slovenia, Spain, Sweden, Switzerland, **Thailand**, UAE, UK, US, plus several extended-network African markets.

Vietnam is absent. Malaysia, Thailand and Indonesia are all ahead of it.

Stripe's own stated workaround for unsupported countries: *"Use Stripe Treasury with stablecoins to manage your money globally... Payments not supported yet."* That is not a payments answer.

Everything below is a consequence of this one line.

## Three routes out, priced

| Route | Setup | Ongoing | What it gets you |
|---|---|---|---|
| **Singapore Pte Ltd** | **S$315** ACRA fee | Nominee director **SGD 1,200–6,000/yr** | Stripe, regional banking, VC-legible entity |
| **US LLC direct** (Wyoming) | **$251–$649** | $179–$809/yr | Stripe + Mercury on US terms. No SG layer |
| **Stripe Atlas** (Delaware) | **$500** | $100/yr | EIN, US bank, SAFE tooling, **$2,500 Stripe credit**, 2 business days |
| **Merchant of record** (Paddle) | **$0** | **5% + 50¢ per transaction** | No entity at all. Paddle is the seller |

Incorporating in Singapore is cheap. **The resident-director requirement is the real cost** — a nominee carries personal legal exposure, runs SGD 1,200–6,000/year, and can trigger bank scrutiny.

The merchant-of-record route deserves more weight than it usually gets. Paddle at 5%+50¢ versus Stripe's ~2.9%+30¢ is roughly double the transaction cost, and in exchange **there is no entity work at all** — Paddle becomes the seller of record and handles *"full tax registration, filing and remittance"* globally. For a two-person team selling digital products, that trades a fixed structural problem for a variable fee.

Tax note that applies to every route: **there is no income tax treaty between the United States and Vietnam.** US-source royalties, dividends and interest face 30% withholding. Service income earned in Vietnam does not. And Vietnam taxes residents on worldwide income regardless of where the entity sits — the structure does not move the founders' tax home.

## The US-entity route is more broken than its vendor page says

**Added 2026-09-16 from `../raw/recovery-pulls.md`, after this file's first draft.** A browser recovery pass reached Reddit, which had been blocked, and found dated first-person accounts that change the ranking above.

**Stripe now requires the account representative to have a real US presence.** From a non-US founder who incorporated through Stripe Atlas:

> "If I enter my actual non-US residential address as the account representative's address, Stripe rejects it and says that the representative must have a US address. If I enter a US address... Stripe requires a full SSN, which I do not have."

> "Update 2026/06/16: I reached out to u/stripesupport on Twitter, and they confirmed that 'US-based accounts must have a physical presence in the United States.'"

Dated **2026-06-16**, confirmed by Stripe support. A Delaware LLC formed from Vietnam does not by itself produce a working Stripe account.

**Banking fails at the same step.** A non-US founder with a Stripe-Atlas Delaware entity:

> "I've received a request from Brex to update Proof of Residential address. We incorporated our company in Delaware (Stripe Atlas), we are non-US founders, we don't live in US, so we could not meet this requirement."

Mercury and Brex — the two banks Stripe itself names, since *"Stripe and Atlas do not provide banking services"* — apply US residential-address KYC.

**And there is an undisclosed annual tax filing with a $25,000 penalty:**

> "if you're a non-U.S. founder, the IRS expects you to file Form 5472 + pro forma 1120 every year... Even just putting money into the company from my own pocket counts as a 'reportable transaction.' The scary part is the $25k penalty for missing it."

Stripe's own copy says the EIN step *"typically takes 2-4 weeks"* for non-US founders and says nothing about any of the three. A Pakistan-based team reported an Atlas application *"sitting in review for about four weeks with very little communication."*

**Revised ranking of the three routes:**

1. **Merchant of record (Paddle, ~5%+50¢)** — no entity, no KYC wall, no Form 5472. The only route with no residency requirement anywhere in it. Costs the most per transaction and does not work for services billing.
2. **Singapore Pte Ltd (S$315 + nominee)** — a real resident director is the *point*, not a workaround. Stripe supports Singapore natively. This is what Sky Mavis did.
3. **US LLC from Vietnam** — cheapest on paper, and the paper is misleading. Three separate residency and KYC walls, plus an annual filing with a $25k penalty.

The vendor page selling Wyoming LLCs to Vietnamese founders claims *"Vietnamese founders receive approvals regularly."* Four dated first-person accounts say the approval is not the hard part.

## What Singapore does not solve

**AWS Marketplace excludes Vietnam and Singapore both.** From AWS's own seller-eligibility documentation: eligible jurisdictions are Australia, Bahrain, Colombia, EU member states, Hong Kong SAR, India, Israel, Japan, New Zealand, Norway, Qatar, South Korea, Switzerland, UAE, UK, US.

Singapore is not on that list. A Singapore holdco does not unlock AWS Marketplace. **A US entity does.** This is a concrete case where the assumed answer is wrong, and it matters because `../customers/first-customers.md` flagged marketplaces as disproportionately important for a team that cannot reach buyers directly.

**Singapore's own founder programmes exclude this team as currently constituted:**

| Programme | Requirement that blocks |
|---|---|
| **Startup SG Founder** | **51% Singapore-citizen or PR ownership** |
| **Tech.Pass** | **S$20,000/month** prior salary |
| **EntrePass** | **SGD 100,000** already raised, or equivalent traction |

Singapore will take the incorporation fee. It will not fund or sponsor two foreign founders at the starting line.

## The one documented SG-over-Vietnam case

**Sky Mavis.** Vietnamese-founded studio, CEO Nguyen Thanh Trung, Axie Infinity built in Vietnam, operating through **Sky Mavis Pte Ltd** — a Singapore private limited. It raised a **$152M Series B led by a16z**, with Accel and Paradigm, at close to **$3B valuation**, announced 2021-10-05. Wikipedia records that the project generated $21M in its first two-to-three years and then *"raised $485 million between July and August 2021 alone."*

That is the structure working, at scale, with top-tier US capital.

Two honest limits. The registry page itself returned HTTP 403 — the entity name and jurisdiction come from a search listing, not from a read filed record. And **no founder has ever narrated publicly why they chose Singapore or what the friction was.** Multiple targeted searches found no first-person account. The structure is documented; the reasoning is not.

Sky Mavis is also crypto/gaming at unicorn scale. It proves the route exists. It does not price it at seed.

## What already works from Vietnam today

Not everything requires restructuring. **Upwork and Payoneer work from Vietnam now**, through SBV-approved rails, with Vietcombank, Techcombank and VPBank handling international receipts. Vietnam is described as a top-5 growth market for Upwork.

The constraint named: *"mandatory dong conversion means USD reserves cannot sit in a Vietnamese account long-term."*

So the freelance and services rails are open. **It is the product and marketplace rails that are closed.** That asymmetry points at services before product — which is where `../markets/ai-attack-defense-services.md` already pointed, now for a second and independent reason.

## The local ecosystem, named

**AI Hay** is the clearest current case. From VnEconomy, 2025-07-02, in Vietnamese:

> "Startup công nghệ AI Hay vừa huy động thành công 10 triệu USD trong vòng gọi vốn Series A"
> "AI Hay đã ghi nhận hơn 15 triệu lượt tải, với hơn 100 triệu câu hỏi được đặt và trả lời mỗi tháng"

**$10M Series A led by Argor Capital**, with Square Peg, Northstar Ventures, AppWorks and Phoenix Holdings following. **Total raised over $18M. 15M+ downloads, 100M+ questions answered monthly.** Corroborated same-day by Thanh Niên and bbw.vn. Founders not named in the coverage.

Other named local companies: **Filum AI** (HCMC, already runs a Singapore office, backed by Nextrans and VinVentures), **Bizzi** (Do Ventures portfolio, AI + RPA invoice automation, clients Tiki / Circle K / PNJ), **Vbee** (2M+ users), **SnapEdit / SilverAI** — bootstrapped, solo founder Nam Le, which is the closest shape to this team found anywhere in the pull, though no revenue figure surfaced.

**YC has ten Vietnam-matching companies, of which four are genuinely HCMC-headquartered** — Infina, Anfin, Reforged Labs, Homebase — plus two in Hanoi. **None of the ten is tagged AI by YC.** Closest is Reforged Labs (B2B marketing analytics, HCMC, W22).

Ecosystem aggregates, all from a secondary marketing blog with no cited methodology — **treat as directional only**: $130M AI-specific funding in 2025; 765+ AI/ML startups; $509M total VC in 2025, up 28%; **HCMC hosts 50% of Vietnam's startups and 44% of investment**; Vietnam ranked 50th in StartupBlink's 2026 index and second-most-active AI ecosystem in SEA after Singapore. Resolution No. 86/NQ-CP (April 2026) names AI, semiconductors, robotics and quantum as priorities.

## The cost base, which is the actual advantage

**ITviec's own 2025–2026 salary report: senior backend developers at ~54.9M VND/month, roughly $27,000/year.** Against the US median developer salary of $133,080 already on file in `ai-trend-suite.md`.

**Roughly 5x.** Vietnamese outsourcing bills $10–60/hour by seniority; no company publishes a named rate card.

HCMC cost of living is genuinely disputed and both figures are on file: Numbeo-style local budget **~$500–780/month**, expat-blog estimates **$2,800–4,500/month**. The gap is a different-lifestyle gap, not a data error.

Read against `../markets/ai-trend-suite.md`: the median profitable indie founder earns ~$4,200 MRR, which reads as under 40% of a US developer salary and as **roughly two years of a senior Vietnamese salary**. The same revenue means something different here. That is the real argument for building from HCMC, and it is an argument about runway, not about market access.

## Failures, named

| Company | Raised | Ended | Stated cause |
|---|---|---|---|
| **Propzy** | **$35M** | 2022 | Negative unit economics, product-market mismatch |
| **NativeX** | **$4M in 8 months** | 2025-12 | Cash crunch |
| **WeFit** | $1.8M | 2020-05 | COVID exposed a fragile prepaid-credit model |

JobHopin and Kilo are named as further failures; details sit behind a DealStreetAsia paywall and were not read.

## Read for this team

- **The access problem has a priced answer, and it is not necessarily Singapore.** For selling digital product, a merchant of record removes the entity question entirely at ~5% of revenue. For raising US capital or listing on AWS Marketplace, a **US** entity — not a Singapore one — is what actually clears the bar. Singapore's value is regional banking and VC legibility, and it costs a nominee director every year.
- **Services rails are already open; product rails are not.** Upwork and Payoneer work from Vietnam today. Stripe and AWS Marketplace do not. Every structural fact in this file points the same direction the services evidence already pointed.
- **The cost base is the durable advantage and market access is the durable constraint.** Those are the two facts that do not change with whichever idea gets picked.
- **Nobody has written down how a Vietnamese founder actually sells into the US.** The single most useful document for this team does not appear to exist in public. That is worth knowing before spending more search budget on it.

No verdict. Per `../../CLAUDE.md` that is the user's.

## Caveats

- **No first-person account of a non-US founder selling into the US was found**, despite targeted searching in English and Vietnamese. The brief required one. It is a genuine gap, not an oversight — recommended next attempts are Indie Hackers' own search, Ask HN threads, and Vietnamese-language queries such as "làm SaaS bán cho khách Mỹ".
- **W-8BEN-E and US vendor-onboarding requirements were not primary-sourced.** IRS returned 404, Rippling 403. The general mechanism — W-8 for non-US vendors — is confirmed only via AWS's documentation.
- The US-LLC-from-Vietnam route comes from **a vendor selling that exact service.** Its claim that "Vietnamese founders receive approvals regularly" is marketing, not audited data. Its fee figures are its own prices.
- **Sky Mavis's Singapore entity is confirmed by a registry search listing, not by reading the filed record** — the registry page 403'd.
- Ecosystem aggregate statistics come from a marketing blog that cites no methodology and no primary report. Every figure in that paragraph is weaker than it looks.
- Stripe Atlas's country list does not name Vietnam in the fetched content. That is an absence of confirmation, **not a denial**.
- Paddle's page states no Vietnam-specific seller eligibility either way.
- Toptal's and Shopify's country eligibility were not checked. AI Hay's founders were not named in any fetched source.
- HCMC cost-of-living figures differ by roughly 5x between sources and are recorded side by side, unreconciled.
