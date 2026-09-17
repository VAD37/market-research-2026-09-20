# Raw pull — competitor-price / page-change monitoring tools

Pull date: 2026-09-17. Method: WebFetch direct on each vendor's own pricing page (or homepage where /pricing 404'd), one call per tool, prompt asked for verbatim tier names/prices/features. No search used for this gap except where noted. No signups, no trials.

Purpose: close wave 2a's gap #3 (idea-set.md attack list item #3) — is there already a cheap incumbent that watches competitor prices, and does anything already deliver "a dated, interpreted pricing fact for a SaaS founder" specifically (as opposed to generic page-diffing or e-commerce SKU repricing).

---

## Segment A — generic page/price-change monitors

### Visualping
Source: https://visualping.io/pricing, fetched 2026-09-17.
- Free: $0/mo — 150 checks/mo, 5 pages, every 60 min, AI summaries included
- Personal 1K: $14/mo monthly, $120/yr ($10/mo) annual — 1,000 checks/mo, 10 pages, every 15 min, AI summaries included
- Personal 5K: $35/mo, $300/yr ($25/mo) — 5,000 checks/mo, 20 pages, every 5 min, AI summaries
- Personal 10K: $70/mo, $600/yr ($50/mo) — 10,000 checks/mo, 40 pages, every 2 min, AI summaries
- Business 20K: $140/mo, $1,200/yr ($100/mo) — 20,000 checks/mo, 200 pages, every 2 min, AI summaries
- Business 30K: $210/mo, $1,800/yr ($150/mo) — 30,000 checks/mo, 300 pages, every 2 min
- Business 40K: $280/mo, $2,400/yr ($200/mo) — 40,000 checks/mo, 400 pages, every 2 min
- Business 50K: $350/mo, $3,000/yr ($250/mo) — 50,000 checks/mo, 500 pages, every 2 min
- Solutions: custom quote, "AI summaries: Premium with custom prompts"
Interprets or diffs: "AI summaries" on every tier per the page — an LLM-generated summary of what changed on a page, not a researched/verified pricing fact. Targets: general web monitoring, not SaaS-pricing-page-specific.

### Distill.io
Source: https://distill.io/pricing, fetched 2026-09-17.
- Free: $0/mo — 25 monitors (5 cloud), 6-hr min cloud interval, 1,000 checks/mo, 2 devices, 30 email alerts/mo, 100 push/mo
- Starter: $15/mo — 50 monitors, 10-min min interval, 30,000 checks/mo, 3 devices, 2,000 alerts/mo, unlimited push, 100 SMS/mo, macros
- Professional: $35/mo — 150 monitors, 5-min min interval, 100,000 checks/mo, 3 devices, unlimited alerts/push, 250 SMS/mo, version history
- Flexi: $80+/mo (pay-as-you-go overages) — 500+ monitors, 2-min min interval, 200,000+ checks/mo
- 20% discount for annual billing.
Interprets or diffs: page does not specify AI interpretation vs raw diff — reads as diff-based. Targets: developers/QA and general power users, not SaaS-pricing-specific.

### ChangeTower
Source: https://changetower.com/pricing, fetched 2026-09-17.
- Free: $0 — 3 pages, daily checks, email alerts, "AI monitoring, content change detection, keyword tracking"
- Lite: $12/mo — 25 pages, daily, "AI monitoring on every monitor"
- Essential: $36/mo — 100 pages, hourly, selective monitoring by section, custom interactions, lazy-load support
- Business: $78/mo — 200 pages, every 20 min, Slack/webhook/"MCP for AI assistants" alerts, monitoring down to page elements
- Enterprise: custom, custom page counts/schedules, multi-region monitoring, full archiving
- 20% discount annual.
Interprets or diffs: markets itself as "AI monitoring" — closest of this segment to an interpreted-change product, and explicitly ships an MCP integration for AI assistants (Business tier, $78/mo). Still general web-change monitoring, not SaaS-pricing-fact-specific.

### Hexowatch
Source: https://hexowatch.com/pricing, fetched 2026-09-17. Page returned only its Enterprise tier in fetched content plus a mention that lower tiers exist unnamed.
- Enterprise: "Starting from just $999/monthly" — personalized onboarding, team training, campaign setup/management, dedicated strategy consultant, premium proxy credit add-on (0.12 credit/MB)
- Lower/standard tiers exist per page copy ("All the benefits of Business+") but names, prices, monitor counts and frequencies were not present in the fetched content. `unknown — checked https://hexowatch.com/pricing 2026-09-17, page did not surface non-enterprise tier details to the fetch`.
Targets: page framing (campaigns, dedicated consultant) reads mid-market/agency, not solo-founder self-serve at the tiers that were visible.

### Wachete
Source: https://wachete.com (root) — /pricing returned HTTP 404 twice (https://www.wachete.com/pricing and https://wachete.com/pricing). Fetched 2026-09-17.
- Homepage states "Free to start, no credit card needed" but no tier names or prices surfaced in fetched content. `unknown — checked https://wachete.com 2026-09-17, price page 404'd`.
- Monitors: product prices, competitor pages/pricing changes, general website content, uptime, job postings, compliance-relevant changes.
- Interprets or diffs: page diffing — "tells you the moment it changes," monitors "a whole page, or just the part you care about." No AI-interpretation claim found.

### Fluxguard
Source: https://app.fluxguard.com/pricing (redirected from fluxguard.com/pricing, 301), fetched 2026-09-17.
- Free (Gyroscope): $0/mo — monitor 3 sites/mo
- Standard (Periscope): $110/mo — monitor 25 sites/mo
- Plus (Telescope): $220/mo — monitor 50 sites/mo
- Premium (Horoscope): $550/mo — monitor 100 sites/mo
- 7-day free trial on paid tiers; annual = 2 months free; no enterprise/custom tier listed, all self-service.
Targets: page framing pitches "regional capabilities," "advanced filtering," "rapid crawling" — reads enterprise QA/legal/brand-monitoring shaped despite self-service pricing, priced well above the other generic monitors for equivalent monitor counts.

### Versionista
Source: https://versionista.com/pricing (404), https://versionista.com/plans/ (404), https://versionista.com (root, fetched successfully) — 2026-09-17.
- No pricing tiers, plan names, or prices found anywhere in fetched content. Homepage tagline: "Monitor Website Changes for Free."
- `unknown — checked https://versionista.com, /pricing, /plans/ 2026-09-17 — no public price surfaced`.
- Target customer: could not be determined from fetched content.

---

## Segment B — e-commerce repricers (SKU/product price tracking)

### Prisync
Source: https://prisync.com/pricing/, fetched 2026-09-17. Explicitly targets e-commerce competitor price tracking and dynamic pricing.
- URL-based model: Professional $99/mo (100 products, unlimited competitors, price updates 3x/day, Excel reports); Premium $199/mo (1,000 products, dynamic pricing engine, daily email, marketplace tracking); Platinum $399/mo (5,000 products, instant notifications, price history, MAP monitoring)
- Channel-based model: Professional $199/mo (100 products, 1 sales channel, +$100/mo per additional channel); Premium $399/mo (1,000 products, +$200/mo/channel); Platinum $599/mo (5,000 products, +$200/mo/channel)
- Hybrid model: Professional $299/mo, Premium $599/mo, Platinum $799/mo
- API access: +20% of subscription fee. 14-day trial, no credit card.
Targets: e-commerce SKU tracking explicitly, not SaaS pricing pages.

### Price2Spy
Source: https://www.price2spy.com/pricing/, fetched 2026-09-17.
- Starter: price not disclosed on page (self-service) — price monitoring, analytics reports, dashboard, feed integration, up to 10 competitors
- Basic: price not disclosed — adds chat/email support, 1 automated report, marketplace monitoring, MAP monitoring
- Premium: "Price upon request" — adds API access, up to 8 daily checks, 3 seats, 5 custom reports
- `unknown — checked https://www.price2spy.com/pricing/ 2026-09-17 — no numeric price published for any tier`.
Targets: explicitly "online retailers," "eCommerce businesses," "large brands" — retail repricing, not B2B SaaS pricing pages.

### Competera
Source: https://competera.net/pricing → redirected (302) to https://competera.ai/pricing (404) → https://competera.ai (root, fetched), 2026-09-17.
- No public price anywhere; contact-us/demo-request only. `unknown — checked https://competera.ai 2026-09-17 — enterprise sales-led pricing, no number published`.
- Targets: enterprise retailers, omnichannel demand-elasticity pricing optimization at scale (grocery, apparel, electronics, beauty, automotive). Not SaaS, not solo-founder-priced.

---

## Segment C — competitive-intelligence suites (enterprise GTM)

### Klue
Source: https://klue.com/pricing, fetched 2026-09-17. No public price; contact-us/enterprise only. Targets enterprise sales/GTM teams ("250,000+ users," Autodesk/Blackbaud/Gainsight/HubSpot/Salesforce named as customers); tracks competitors, win-loss, buyer feedback, market intel across many sources — not a single dated pricing fact for a solo founder.

### Crayon
Source: https://www.crayon.co/pricing, fetched 2026-09-17. No public price; "tailored to the needs of your competitive intelligence program," Request an Estimate form only. Targets enterprise competitive-intelligence programs; aggregates battlecards and competitive assets across teams.

### Kompyte
Source: https://www.kompyte.com/pricing (404) → https://www.semrush.com/kompyte/ (404) → https://www.kompyte.com (root, fetched), 2026-09-17. No public price; "PLANS" link with no numbers shown, contact-us only. Targets sales/marketing teams tracking competitor websites, reviews, content, social, ads, job postings across "hundreds of sources."

---

## Summary read for candidate B

No tool found across 13 vendors, 3 segments, produces the specific product candidate B proposes: a dated, interpreted pricing fact for a solo/small B2B SaaS founder, delivered as a memo. The closest matches (Visualping, ChangeTower) ship "AI summary of a page diff" as a feature inside a general-purpose page-monitoring tool priced $12-$350/mo — that is AI-summarized diffing, not researched/verified pricing intelligence with an interpreted memo cadence. E-commerce repricers (Prisync $99-799+/mo, Price2Spy, Competera) are explicitly SKU/retail-shaped and do not address SaaS pricing pages. Enterprise CI suites (Klue, Crayon, Kompyte) are GTM-team tools with no public price, sized for enterprise sales orgs tracking many competitors across many channels, not a single competitor's pricing page for a 3-10 person shop.
