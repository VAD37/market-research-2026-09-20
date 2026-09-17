### Source: long-tail scan for an existing seller of candidate B's scoped product

- Pull date: 2026-09-17
- Method: delegated breadth search (GitHub search API, Product Hunt, AppSumo, Reddit, IndieHackers, YC directory, general web) whose findings on the four load-bearing vendors were then **re-fetched first-hand by wave 2b** with `curl -sL` and read verbatim. The delegated leg's full channel/query log and its unverified entries are reproduced below the verified section and are labelled as relay.
- Scope: deliberately excludes the 13 vendors wave 1c already checked (Visualping, Distill.io, ChangeTower, Hexowatch, Wachete, Fluxguard, Versionista, Prisync, Price2Spy, Competera, Klue, Crayon, Kompyte).
- Label: vendor-reported (each vendor's own marketing copy).

---

## PART 1 — FIRST-HAND FETCHES BY WAVE 2b

### JABB Watch — https://jabbwatch.com — `curl` HTTP 200, 23,768 bytes, 2026-09-17

Page title: "JABB Watch — Competitor Price Changes, AI-Summarized". Verbatim:

> "Know when competitors change pricing before your next sales call. **Weekly AI-written brief. What changed, why it matters to your deals, and what to do about it.** First report on Friday, 3-minute setup."

> "1 **Tell us who to watch** — Enter up to 5 competitor URLs — their pricing pages, plan pages, or promo landing pages. Tell us about your business so we can interpret changes in your context.
> 2 **AI monitors twice per week** — Our engine scans each page on Tuesday and Friday, detects changes, and classifies them by significance. No cookie banner noise. Just the pricing changes that matter.
> 3 **Get your actionable Friday email** — Every Friday: what changed at each competitor, why it matters to your positioning, and concrete recommended actions. Two minutes of reading replaces five hours of manual checking."

> "**Recommended actions** — Each report includes concrete next steps: 'Consider matching within 2 weeks,' 'Monitor for 1 more cycle,' or 'No action needed.'"

> "**Priority scoring** — Every change gets a severity rating: critical, high, medium, or low."

Sample report shipped on the page, verbatim (the product's own demonstration of its output):

> "**Critical — Price Increase Detected.** *What changed*: Professional plan increased from €12.50 to €15.00/user/month — a 20% price hike. Annual billing now required for Business+ tier. *Why this matters to YOUR business*: Your Professional plan is currently priced at €14/user/month. Your competitor just moved from €1.50 below you to €1.00 above you. You now have the lower price point for the first time in 18 months. **Recommended action**: Consider holding your current price and updating marketing to emphasize cost advantage. This is also a window to capture switching prospects."

Pricing, verbatim: "Early bird — first 50 customers. **Core** ... **€79 €39 /month**. Locked in for life. Billed monthly. No VAT for EU B2B with valid VAT ID." Includes "Up to 5 competitor URLs monitored / AI-powered weekly summaries / Priority scoring (Critical → Low) / Concrete recommended actions / Email delivery every Friday / Active in 3 minutes."

> "First-report guarantee: if your first Friday report isn't useful, reply to it and we'll refund you. No forms."
> "Cancel anytime. Less than the cost of one hour of your pricing analyst's time, every month."

Launch date: Indie Hackers post dated 2026-04-05 per the delegated leg (relay — not re-fetched by wave 2b).

### PriceGhost — https://priceghost.site/ — `curl` HTTP 200, 39,817 bytes, 2026-09-17

**Status is pre-launch, not shipping.** Page header verbatim: "Est. 2026 · Vol. I · Issue 001 · **Pre-Launch Edition** · ← Join Waitlist". Byline: "Solo dev · Built in public · **Pre-launch** · India, 2026". Verbatim:

> "PriceGhost monitors any competitor pricing page and alerts you the moment something changes — price hike, dropped free tier, new plan. You find out in minutes, not weeks. Built for the people enterprise tools have always ignored: **indie founders, small teams, solo operators who can't justify $10K a year just to stay informed.**"

> "**SaaS Founders** — You have 5–10 direct competitors and you need to know the moment any of them changes their pricing."

Founder story, verbatim — this is the same problem statement as candidate B's, written by someone who hit it:

> "I was manually checking competitor pricing pages every Monday morning. Eight different websites, opening each one, comparing prices to notes from the week before. It took over an hour. Every single week. One Monday I skipped it. Then another. Three weeks later I found out a competitor had dropped their price by 30%. I'd lost multiple deals in that window and didn't even know why prospects were pushing back. I went looking for a tool. Kompyte, Klue, Crayon — they all start at $10,000 a year, require a sales call, and are built for 50-person marketing teams. **There's literally nothing built for a solo founder watching five competitors.** So I built PriceGhost."

> "Building it in public — **breakeven is a single customer**."

Claimed problem sizing (vendor-asserted, unsourced by the vendor): "**3 wks** Average detection delay — The typical SaaS founder finds out about a competitor pricing change 3 weeks after it happens." / "**2–4 hrs** Wasted every single week — Manual competitor checks consume 2–4 hours of founder time per week."

Pricing per the delegated leg: Free $0/mo (2 competitors, weekly); Starter $19/mo (20 competitors, daily); Pro $39/mo (100 competitors, hourly); Agency $99/mo (unlimited, 30-min). **Not confirmed first-hand** — the tier table did not survive wave 2b's HTML-to-text extraction. Relay.

### RivalFlag — https://rivalflag.com — `curl` HTTP 200, 67,757 bytes, 2026-09-17

Verbatim from the live product preview embedded on the page — this is a competitor-pricing memo with an interpretation attached:

> "Helio CRM · critical · Pricing — **Helio bumped Premium from $59 → $99 and removed the Free tier overnight.** Tighter packaging signals confidence in retention. Expect a new objection set from cost-sensitive buyers and a forced-upgrade narrative — your 'still has a free tier' story just got more valuable."

> "Real cards look just like this — written up by AI from your competitors' pricing, careers, and homepage pages."

> "Free to start · No credit card"

Tier pricing per the delegated leg: Free $0 (2 competitors/3 pages, weekly); Scout $19/mo (8 competitors/5 pages, daily); Pro $39/mo (25 competitors/10 pages, daily). **Not confirmed first-hand.** Relay.

### Competiflow — https://competiflow.com — `curl` HTTP 200, 127,196 bytes, 2026-09-17

Verbatim:

> "Competiflow catches the pricing cut, the new feature, the quiet doc edit, before it reaches your deals."
> "Start free — 100 free checks to start. No card required."
> "Most monitors watch pixels or raw HTML. A moved banner, a rotated testimonial, a fresh cookie notice, they all trip the same alarm as a real price hike."

Competiflow's own cited demand quote (third-party-relayed by the vendor, original not verified):

> "'Visual monitors alert you when pixels change. I only care if the actual date changes.' — Reddit r/SaaS, on generic page watchers"

Vendor-asserted market claims, attributed by the vendor but not independently verified: "95% of alerts were noise for one team paying $18k a year, about 40 pings a day. (Segment8, on Klue)" / "#1 complaint about every major CI tool is the same one: irrelevant alerts. (Flares G2 study)" / "$15k+ a year for enterprise CI (Klue, Crayon list pricing)".

Tier pricing per the delegated leg: Starter $19/mo (2,000 checks, daily); Growth $49/mo (5,000 checks, 6-hr); Pro $99/mo (10,000 checks, hourly). **Not confirmed first-hand.** Relay. IndieHackers post 2026-07-21 per the relay.

---

## PART 2 — RELAY ONLY, NOT RE-FETCHED BY WAVE 2b

Everything in this section comes from the delegated leg and carries its confidence, not wave 2b's.

| Product | URL | Claim (relay) | Price (relay) | Date (relay) |
|---|---|---|---|---|
| RivalWatch | rivalwatch.com | "Automatically tracks your competitors' websites and delivers a weekly AI intelligence report... every Monday, monitoring pricing pages, homepages, job boards, and blog posts." "Built for B2B SaaS founders, startup CEOs, and product managers." | $29/month | unknown |
| Metrivant | metrivant.com | "Every signal includes a full evidence chain: the URL that changed, the before-text, the after-text, the signal classification, a confidence score" | unknown (HTTP 402) | blog active to 2026-04-02 |
| Fruitful | producthunt.com/products/fruitful | "Track competitors instantly. Juicy insights every day." | free options | launched 2025-10-06 |
| SaaS Pricing Explorer | producthunt.com/products/saas-pricing-explorer | "Explore, compare and monitor SaaS pricing strategies" | free | launched 2023-06-29 |
| tona | producthunt.com/products/tona-2 | "The fast & easy way to automatically monitor your competitor" | unknown | 2023 |
| PricingHunter | pricinghunter.com | "Track competitor prices daily" — e-commerce (Shopify/WooCommerce/GMC) | 14-day trial | 2026 |
| unnamed, SouravBuilds | indiehackers.com/post/turns-out-most-founders-don-t-track-competitor-pricing-until-it-s-too-late-b72a2e57ee | "Paste a competitor pricing page → get notified if something meaningful changes" | unlaunched | posted 2026-03-13 |

GitHub repos found (relay; star counts and dates from the GitHub search API during the delegated leg):

| Repo | Stars | Last push | License | Scope |
|---|---|---|---|---|
| yassnemo/compete | 10 | 2026-07-03 | MIT | "Scheduled agents track competitors across sites, blogs, pricing, news, and job posts... changes get flagged, and a dashboard plus auto weekly reports surface it all." |
| mikevidotto/trackprice-ai | 2 | 2026-09-14 | — | general competitor price tracking, Go/Postgres/Stripe |
| danishashko/competitor-intel-toolkit | 2 | 2025-11-01 | MIT | general CI toolkit |
| willylam2222-bot/priceprobe | 3 | 2026-07-20 | MIT | "Track competitor prices & stock — free, zero-dependency Python. Optional $19 packaged version for non-devs." |
| joeycatic/PriceVault | 1 | 2026-07-09 | — | "Multi-tenant competitor price tracking SaaS" |
| kevjaeg/CompetitorPriceTracker | 6 | 2026-02-18 | MIT | Amazon/eBay/Shopify, e-commerce |
| changedetection.io | ~34,000 | — | — | general-purpose page-change detection, not SaaS/founder-specific |

---

## PART 3 — CHANNELS SEARCHED AND CHANNELS THAT FAILED

Queries run by the delegated leg, 2026-09-17:

- **GitHub search API**: `pricing+page+monitor`, `competitor+price+tracker`, `pricing+intelligence+agent`, `competitor+pricing+monitor` (sort=updated), `saas+pricing+watcher`, `pricing+page+change+detection`, `competitive+intelligence+founder+solo`, `"pricing change"+alert+competitor`. Two returned empty/malformed responses, likely unauthenticated-endpoint throttling, and were not re-run.
- **Product Hunt**: via general web search plus direct WebFetch on three product pages. No PH search API access.
- **AppSumo**: general web search only, not queried against appsumo.com directly. Surfaced only Boardfy (e-commerce price optimization).
- **Reddit** (r/SaaS, r/Entrepreneur, r/microsaas): three query forms attempted; **none returned actual Reddit thread content** — the general web index returned Shopify app-store and Capterra pages instead. **Reddit is NOT confirmed clean; it was unsuccessfully searched.**
- **IndieHackers**: surfaced JABB Watch, Competiflow, RivalFlag, RivalWatch and the unnamed SouravBuilds post.
- **Y Combinator directory**: `ycombinator.com/companies?query=competitive+intelligence` returned page title only (JS-rendered SPA, not executable by the fetch tool). **Not checked.** Only unrelated BetterBasket (grocery pricing) surfaced via web search.
- Unreachable vendor sites: rivalwatch.com (ECONNRESET, both attempts), pricinghunter.com (HTTP 403), metrivant.com (HTTP 402).

## PART 4 — THE GRAVEYARD QUESTION

Asked: is there evidence that people who tried to sell a narrow competitor-pricing-watch tool failed or shut down?

- Closest verifiable shutdown: **PoachIt**, a consumer price-tracking service — TechCrunch, 2015-05-18, https://techcrunch.com/2015/05/18/price-tracking-service-poachit-shuts-down. Different vertical (consumer shopping, not B2B SaaS CI) and 11 years stale. Weak.
- No archived, abandoned, or "no longer maintained" repo was found in this specific niche. The repos located are all 2025-2026 and low-star, but none carry abandonment signals.
- No "I'm shutting down my pricing tracker" post found on IndieHackers or Reddit despite direct search — though the Reddit channel failed generally (see Part 3), so this negative is weak.
- **Countervailing observation**: at least six independent entrants (PriceGhost, JABB Watch, RivalWatch, RivalFlag, Competiflow, the unnamed SouravBuilds tool) appeared within roughly a twelve-month window to 2026-09. None showed verifiable scale — no user counts, revenue figures, or review volume were found for any of them. `unknown — checked vendor sites, Product Hunt, IndieHackers 2026-09-17`.
