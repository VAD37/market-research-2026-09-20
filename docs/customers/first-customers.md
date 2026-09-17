# Getting the first ten customers — channel, not product

Pass 3, 2026-09-16. Compiled from `../raw/first-customers-pulls.md` (14 blocks) and `../raw/first-customers-source-index.md`.

**Read the health warning before the findings.** This is the weakest-sourced file in the repo and it says so on purpose. Reddit blocked the agent at the network layer on all three endpoints. WebSearch was already exhausted. What survived is Hacker News' public API plus direct fetches, which means the evidence is first-person founder accounts — strong on mechanism, weak on base rate — and most of it is 2015–2021 vintage. One block is 2026-dated.

Treat channel *mechanics* as durable. Treat every *rate* as stamped to its collection date, not to now.

## What the evidence supports

| Channel | Evidence | Strength |
|---|---|---|
| **Referral via 1-on-1 pro-bono help** | One consultant at 100% capacity, **$10,000/week** | Strongest account, n=1, 2015 |
| **SEO on existing search intent** | Kapwing: **15 paying subs in 3 weeks**, all from Google | Company-stated, product-dependent |
| **Subcontracting from an established firm** | Named as the bootstrap route into a client base | Unquantified |
| **Phone / cold calling** | *"There is literally no other way to build a consultancy business"* | Asserted, zero numbers |
| Cold email | Kapwing ~2% response, **zero conversions** | Failed, quantified |
| Blogging as primary channel | 2 years, 4 hrs/night, flat traffic, $0 | Failed, quantified |
| Paid social | 3 months, **2 sales total** | Failed, quantified |

## The one account that matches this repo's leading idea

A self-described application-security consultant, selling penetration tests, source-code analysis and workshops to seed-to-Series-A companies — the exact shape `../markets/ai-attack-defense.md` describes. In their own words:

> "Through September I'm fully booked at 100% capacity, mostly with Y Combinator companies. I charge a static rate of $10,000/week, though I discount this for certain circumstances (good referral, long term contract, etc)."

And the channel, stated as a negative before it is stated as a positive:

> "I network a lot. I don't go to meetups. I don't have a blog. I don't hand out business cards. I network with people in 1x1 ways that show my value. My best referrals have come from people who I helped pro bono for something seemingly insignificant who turned out to be very well connected... The best way to start this is to literally reach out to people who are in influential groups — not influential people themselves — and help them in an honest manner."

Two more lines from the same account, both operationally specific:

> "I would advise you start out by subcontracting another firm that needs work. Dirty secret — many security firms will subcontract to you, and you can build a client base that way."

> "A blog is helpful for long term leads, but it won't help you in < 6 months usually."

**$10,000/week is the highest per-unit price anywhere in this repo**, against Cobalt's published $3,500 per autonomous pentest and Synack's ~$18,300 market average per engagement in `../markets/ai-attack-defense-services.md`. One practitioner, 2015, no independent verification. Do not plan on it. Do note that it exists.

## What this does to open question D3

D3 asked whether published research generates inbound for a technical services practice. **The only direct evidence found says no, not within six months** — from a practitioner whose own business runs on referral. The repo itself is a bet on the opposite proposition, so this is a finding against the house.

Two qualifications, both real:
- The account predates AI search entirely. `../findings/injection-feasibility.md` establishes that answer engines now retrieve live and cite sources, which is a different distribution surface than 2015 SEO.
- The same account calls a blog "helpful for long term leads." The claim is about *latency*, not about worthlessness.

Unresolved. E5 in `../method/open-questions.md` — find one operator who credits published research with numbers attached — is now the tiebreaker.

## Cold email in 2026

The one current-dated block. A founder describing 2026 conditions:

> "The Catch-All Silent Drop: Enterprise servers (O365/Mimecast) now seem to 'accept' all mail to prevent directory harvest attacks, only to silently drop it or route it to a quarantine folder if the sender isn't on a whitelist."

> "In 2026, it seems Google/Microsoft filters have moved entirely to reputation based on bi-directional interaction. If you don't have a history with a domain, your 'verified' email is effectively treated as shadow-spam."

Reported outcome: a week spent on a clean list, 0% bounce, near-zero opens. Anecdotal, forum-sourced, no sample size.

The vendor benchmark that was supposed to quantify this did not. Woodpecker publishes cold-email figures over **26,000 campaigns** (11 to 1,000+ prospects each) but two fetch attempts returned only relative claims — "personalized campaigns achieve almost twice as high reply rate," personalized subject lines ~10% higher open rate — and **no absolute reply rate anywhere in the retrieved text**. Vendor-reported, self-selected sample, no topline. Unusable as a benchmark.

The structural counter-argument, from the same 2026 thread:

> "Do things that don't scale. No one built a business by starting out with huge email blasts... You start by finding individuals and addressing them as individuals."

## Recovery pass — Reddit, unblocked

**Added 2026-09-16 from `../raw/recovery-pulls.md`.** The browser reached Reddit. Dated, scored, first-person accounts, and they are far more current than the 2015-2021 material above.

**Absolute cold-email numbers now exist.** Two vendor reports with stated samples, reached through an aggregator that footnotes primaries:

| Source | Sample | Reply rate |
|---|---|---|
| **Instantly, 2026 report** | "billions of emails," Jan–Dec 2025 | **3.43% platform-wide.** Top 25% 5.5%+, top 10% 10.7%+ |
| **Belkins, 2025 study** | **16.5M emails, 93 industries** | Cybersecurity **4.86%**, IT Consulting 5.93%, Software Dev 5.89% |
| Expandi, LinkedIn H1 2025 | 70,130+ campaigns, 20M+ attempts | **LinkedIn DM 10.3% vs cold email 5.1%** |
| Belkins, LinkedIn 2025 | — | Personalized message **9.36% vs 5.44%** — a 72% lift |

And the trend line: **8.5% (2019) → ~7% (2023) → ~5.1% (2024) → 3.43% (2026).** Every figure is a sending platform's own customers, not a random sample — the self-selection problem is unchanged, just now attached to real denominators.

**Cybersecurity sits at 4.86%, near the bottom of Belkins' industry table.** That is the lane this repo leads with.

**First-customer accounts, 2025–2026, with the channel named:**

- *"$0-$1 took 7 months. $1-$100k took 12 months"* — 7 months of full-time work for the first $20; then $1,300 at one month, $4,500 at three, $16,500 at six, **$100,000 at twelve.**
- *"I finally got my first paying customer after 8 months"* — **$70**, 472 points. Channel was one direct relationship plus custom feature work. Two failed products before it.
- *"I emailed 130 people to promote my SaaS. 0 said yes."* Personalized, newsletter owners. **Two replies, both no.** The same builder then ran an affiliate program at 40% recurring and got **8 sales in one day**, MRR €255 → €350.
- *"I put $100 into Reddit ads. I got 50 clicks, but not a single conversion."* Same builder. His ninth Indie Hackers post got 468 views and **26 new users, free** — the first eight got nothing.
- A landing-page A/B with numbers: headline explaining the product → 40 signups in two weeks; headline highlighting the technology → **zero for a week**; headline on the result → 8 signups that night. Then 48 signups and no revenue until a **30-second screen recording** produced the first two paying customers within 48 hours.
- The cofounder case, 928 points: *"He was great for the first 4 months. Brought in our first 8 customers. Ran sales calls. I was building and he was selling and it felt like the dream. Then he got a job offer. $190K plus equity... Now I run a SaaS doing $8K MRR, growing it alone, and 40% of the company belongs to someone who contributes nothing."*

That last one is the only documented account in this repo of the exact division of labour this team is proposing. **It worked — eight customers in four months — and then the non-technical founder left for a salary, keeping 40%.**

**The strongest demand-proxy complaint found anywhere in pass 3** — 631 points, 545 comments, r/Entrepreneur, 2026-04:

> "We are paying for 23 separate software subscriptions right now... the total monthly spend across all of them is $4,100 which is almost $50,000 a year on software for a 12 person company." / "five years ago that number was about $1,200/month for roughly the same functionality" / "every tool is creeping their prices up 15 to 20% annually while simultaneously moving features that used to be included into higher tier plans"

Not AI-specific. It is the clearest "we pay $X and it's terrible" signal in the repo, and it points at consolidation, not at another tool.

## Marketplaces

Only one was reachable. Microsoft's Partner Center documentation, updated **2026-09-04**, confirms a services practice can list:

- Three listing types: Free Trial, Contact Me, Get It Now.
- **Professional-service offers support Contact Me listings** and can be sold via Private Offers.
- Private offers are enabled by default on new public offers; requests "are captured as Marketplace leads."

That confirms a two-person services shop is *eligible* to list. It says nothing about volume, and no transaction fee percentage appears on the page.

AWS Marketplace: the docs page rendered in the browser on the second attempt. **The listing-fee percentage is still not recoverable** — but the seller-eligibility list is, and **Vietnam is not on it.** See `../markets/vietnam-sg-access.md`.

**Shopify resolved, and it is the best marketplace economics found:**

> "You keep 100% of your first $1,000,000 USD in gross app revenue earned from January 1, 2025, and 85% of earnings above that. All billing is subject to a 2.9% processing fee" — plus a **one-time $19 registration fee.**

**0% revenue share up to $1M lifetime.** Payouts run through Hyperwallet with a $25 minimum — the same rail Upwork and Airbnb use for cross-border payment, which matters for a team in Vietnam. Shopify publishes no country-eligibility list; Vietnam-specific confirmation was not obtained.

No disclosed revenue from a small vendor was found on any marketplace.

## Costs — a hole, not an estimate

**No CAC benchmark exists that can be sourced.** The recovery pass went back with a browser and a working search engine, and confirmed something more useful than a number.

Every result reciting the *"B2B SaaS companies average $702 overall, ranging from $536 for mid-market"* figure appears **word-for-word or near-word-for-word across eight independent-looking domains** — thezulumethod.com, growthcentr.com, shno.co, saashero.net, digitalapplied.com, enrichlabs.ai, corpify.org and others. None discloses a methodology or a sample. The top-ranking one is a marketing agency selling AI-automated outreach; its benchmark post exists to sell its own services.

The pattern is one ultimate source — an aggregator, or a single LLM-generated content run — recirculated across many SEO domains.

**There is no acquisition-cost figure in this repo for small B2B software or for services, and the reason is now documented rather than assumed.** `unknown — checked eight domains 2026-09-16, no source with disclosed methodology confirmed`.

## Read for a two-person team in Ho Chi Minh City

Geography confirmed by the user 2026-09-16, after this pull ran. It changes the ranking, and not in the team's favour:

- **The strongest channel is the least portable.** Referral through 1-on-1 help inside "influential groups" assumes physical or social proximity to the buyer. The winning account's client base was Y Combinator companies. That is a San Francisco network reached by being adjacent to it.
- **The two quantified failures are the two remotely-runnable channels.** Cold email failed with numbers; content failed with numbers. Those are exactly what a team without market access would reach for first.
- **Marketplaces matter more here than they would for a US team**, because they intermediate trust and payment — and marketplaces are precisely where this pull found nothing. That gap is now assigned to the HCMC/Singapore agent.

This is the sharpest tension pass 3 has surfaced. The best-evidenced channel requires the access the team does not have. Not a verdict — per `../../CLAUDE.md` that is the user's — but it is the constraint the other four questions now have to answer to.

## Caveats

- **Reddit was blocked host-wide** at the network-policy layer — `www`, `old` and `api` endpoints, every User-Agent tried. r/SaaS and r/Entrepreneur contributed nothing. The browser route was granted after this agent finished and would likely work; this is a re-runnable gap, not a permanent one.
- **WebSearch quota was exhausted before the pull started.** Indie Hackers interviews, 2025-2026 benchmark studies and current CAC data were all out of reach.
- Most accounts date 2013–2021. Kapwing 2017, the consulting thread 2015, the failure retrospective 2021. Only the cold-email deliverability block is 2026.
- The three quantified channel failures come from **one serial founder's 12-year retrospective** — same person, three ventures. A repeated-failure pattern from one operator, not three independent companies.
- One block of Indie Hackers material is flagged low-confidence on provenance by the agent itself and is excluded from this file entirely.
- The 2024-02-01 Google/Yahoo bulk-sender thresholds were **not re-verified against a live source** this session. Do not restate them as sourced.
- No account was found of a two-person shop selling AI security services specifically. E5 stays open across three passes.
