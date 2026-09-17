# Recovery pulls — browser-based retry of prior fetch/WebSearch failures

Pulled 2026-09-16. Channel: `browser` (Chrome extension, real logged-out session) unless marked `WebFetch`. This is a recovery pass, not new research direction — every block below maps to one of the six target items an earlier session lost to HTTP 403s, JS-shell pages, or an exhausted WebSearch quota. Quoted material is verbatim (blockquoted); unquoted lines are this session's own paraphrase/summary of what the browser rendered, flagged as such.

A recurring tool artifact: this session's page-text extractor frequently returned the *previous* page's content on the first call after a navigation (a one-call lag), and Google search-result links frequently failed to register clicks (the tab stayed on the SERP). Bing text search and direct URL construction from Bing/Google snippets were the reliable workaround and are used throughout. Noted per block where it mattered.

---

# TARGET 1 — Reddit (previously fully blocked)

## Block 1 — Reddit renders fine in the browser; curl block was network-policy layer only

URL: `https://old.reddit.com/r/SaaS/search?q=first+customer&restrict_sr=1&sort=new`
Fetch date: 2026-09-16. Channel: browser.

Confirmed: old.reddit.com search pages render completely normally in the extension-driven Chrome session — full post bodies, scores, comment counts, timestamps. The prior session's block ("your request has been blocked due to a network policy") was specific to headless curl/WebFetch User-Agents, not a host-wide block. This is itself the finding for target 1's header claim.

## Block 2 — r/SaaS: "Spent a year building a SaaS nobody cared about... $7K MRR" (channel-not-product thread, complaint-adjacent)

Post: "Spent a year building a SaaS nobody cared about. Then I rebuilt it around my own frustration and just hit $7K MRR." — r/SaaS, submitted 2026-09-16 (posted "2 hours ago" relative to fetch), by u/BusyDoughnut1219. 67 points, 30 comments.

> "$7,038.62 MRR. Screenshot attached... A year is a long time to work on something people can comfortably live without... You put in your website. It works out potential buyer audiences, finds relevant people with verified work emails, and writes and sends personalised outreach through managed sending accounts."

Founder-stated. Product: Maila (usemaila.com), an outbound-automation tool. No channel breakdown given beyond "shipping, measuring, talking to users."

## Block 3 — r/SaaS: "We rebuilt our onboarding 50+ times... $0-$4M ARR" (Supademo, numbers-heavy)

Post: "We rebuilt our onboarding 50+ times as we went from $0-$4M ARR. Here are our metrics and lessons" — r/SaaS, submitted 2026-09-16 ("23 hours ago"), by u/jhylee. 31 points, 14 comments.

> "Over the last 3 years, we grew Supademo past $4M ARR, >25% EBITDA margins & 200k+ users." / "~70% of B2B buyers want self-serve. Don't make 'Book a demo' the only door." / "Define activation for real, not vanity milestones. Ours isn't 'created an account.' It's 3 demos + 5 edits + 1 share within 7 days. ~15% hit it. Those users convert at ~26% vs ~10% (~2.6x)." / "43% of users who activated after the trial still opened a later email." / "Lifted activation ~15% MoM" [from an in-product human-touch feature].

Founder-stated, company-stated numbers (Supademo), no independent audit.

## Block 4 — r/SaaS: "I finally got my first paying customer after 8 months" — $70, direct-relationship channel

Post submitted 2026-08-18 (29 days before fetch), by u/Alarming-Match-7464. 472 points, 382 comments.

> "a few days ago, I got my first paying customer for my SaaS. $70... Before Announcify (my current SaaS), I built PDFQuizGen. I got some traffic, people signed up, but nobody paid... That's how I met the person who eventually became my first customer. He was building a CRM in Canada and signed up for Announcify... I didn't know if he would actually pay when I started building them, so I asked him directly. He said he would."

Channel: direct one-to-one relationship building + custom feature work, not a scalable acquisition channel. 8 months elapsed pre-product, 2 years total across two failed prior products.

## Block 5 — r/SaaS: "I just got my first paying customer" — $9, 1,142 points, 323 comments

Post submitted ~2026-08-16 (1 month before fetch), by u/aryanxcreates.

> "I know it's 'just' $9, but I can't stop smiling. Over the last few weeks I've been building a Chrome extension for developers... Today, a complete stranger did [pay]."

No channel detail given — emotional milestone post, high engagement (score/comment count itself is the demand-proxy signal requested).

## Block 6 — r/SaaS: "Co-founder left after 14 months... walked with 40% equity" — first 8 customers via cofounder sales

Post submitted 2026-04-16 (5 months before fetch), by u/Sweet_Concentrate128. 928 points, 326 comments.

> "He was great for the first 4 months. Brought in our first 8 customers. Ran sales calls. I was building and he was selling and it felt like the dream. Then he got a job offer. $190K plus equity at a mid-stage startup. He took it... Now I run a SaaS doing $8K MRR, growing it alone, and 40% of the company belongs to someone who contributes nothing."

Channel for first 8 customers: cofounder-run outbound sales calls. Cautionary tale, not the ask, but directly evidences a "first customers" channel (direct sales by a dedicated non-technical cofounder) and a two-founder-split risk.

## Block 7 — r/SaaS: "4 paying users in one day" — Reddit-forum validation → PH launch

Post: "We did itt! 4 paying users in one day" — r/SaaS, submitted 2026-05-16 (4 months before fetch), by u/LIN3003. 702 points, 312 comments.

> "A few months ago, I started validating an idea across Reddit, forums, and Twitter seeing is people Would want AI meeting notes without sending conversations to the cloud.. and the response surprised me... What worked: talking about the problem, not the product / replying personally to every beta user / shipping feedback fast / staying transparent about what was broken / Releasing on Producthunt, which gave some good traction."

Product: AskMeety (local AI meeting assistant for Mac).

## Block 8 — r/SaaS: Outgrow/VenturePact story — free-tool-as-acquisition-channel (secondhand, cites named founders)

Post: "How a simple free calculator became a SaaS with 3000+ paying users" — r/SaaS, submitted 2026-09-16 ("44 minutes ago"), by u/Ok-Expression-6340. 0 points at fetch time (too new to have votes).

> "Randy Rayess and his co-founder Pratham. Before Outgrow, they were running VenturePact... Their sales team kept spending a huge amount of time on calls with prospects asking 'How much does it cost to build an app?'... around 80% of those calls ended up going nowhere... They built a free interactive calculator... That eventually became Outgrow... They grew it to more than 3,000 paying customers, with plans ranging from roughly $25 to $600/month, while bootstrapping the company."

Secondhand retelling by a third party (poster, not the founders), not founder-stated in the original voice — flagged accordingly. Two-founder company (Randy Rayess + Pratham [surname not given in thread]).

## Block 9 — r/Entrepreneur: SaaS-tool-sprawl complaint thread — demand proxy for "we pay $X and it's terrible" pattern, though not AI-specific

Post: "the SaaS model is quietly falling apart for small businesses and nobody in tech wants to admit it" — r/Entrepreneur, submitted 2026-04-16 (5 months before fetch), by u/Healty_potsmoker. **631 points, 545 comments.**

> "We are paying for 23 separate software subscriptions right now... the total monthly spend across all of them is $4,100 which is almost $50,000 a year on software for a 12 person company." / "five years ago that number was about $1,200/month for roughly the same functionality" / "every tool is creeping their prices up 15 to 20% annually while simultaneously moving features that used to be included into higher tier plans" / "we have separate tools for email finding and email sending and email warmup and CRM and analytics when five years ago your CRM just did all of that... newer platforms trying to reconsolidate like hubspot cramming everything into one suite or smaller ones like instantly and fuseai trying to merge the sales stack back together."

Not AI-specific but directly on-topic for "we pay $X for Y and it's terrible" — high engagement (631/545) makes it the strongest demand-proxy complaint thread found this pass. Names Instantly and "fuseai" as tools trying to reconsolidate the sales/outreach stack.

## Block 10 — r/SaaS: "I'm pivoting my SaaS after realizing Reddit lead gen tools (including mine) are all lying to you" — AI-tool-category complaint from a builder, not a buyer

Post submitted 2026-01-16 (8 months before fetch), by u/No-Common1466. 41 points, 89 comments.

> "You know the pitch: 'Find qualified leads on Reddit! Unlimited leads per month! 30% reply rates!'... We tested it with 4 real paying clients for 90 days... Reply rate was under 1%. Sometimes we'd go weeks without a single reply... I kept seeing other tools launch with the same promises. And I realized we're all selling the same lie."

This is a builder admitting his own AI tool over-promised, rather than a buyer complaint — recorded because it directly quantifies the gap between marketed and real performance for an AI-outreach-tool category (target 5-adjacent), with a real 4-client/90-day test behind it (vendor-self-reported, not audited).

## Block 11 — r/indiehackers: "$0-$1 took 7 months. $1-$100k took 12 months" — timeline with numbers

Post submitted 2025-12-16 (9 months before fetch), by u/felixheikka. 86 points, 91 comments.

> "It took 7 months of real effort and working on my ideas full time just to get my first paying customer. That's 7 months of effort for $20... 1 month after getting my first paying customer I hit $1,300. 3 months after, $4,500. 6 months after, $16,500. 12 months after, $100,000."

## Block 12 — r/indiehackers: "How I got my 5 first users" — headline + demo-video A/B result with numbers

Post submitted 2026-04-16 (5 months before fetch), by u/Extra-Motor-8227. 111 points, 301 comments.

> "I launched PostClaw three weeks ago... So far, I have 58 signups and 5 paying customers. I just reached $150 in monthly recurring revenue... My first headline explained the product... That brought in 40 signups in two weeks. Then I changed the headline to highlight the technology... zero signups for a week... I rewrote the headline to focus on the result... That same night, I got 8 signups... I had 48 signups and no revenue... I made a 30-second screen recording... Within 48 hours, I got my first two paying customers."

## Block 13 — r/indiehackers: "I emailed 130 people to promote my SaaS. 0 said yes." then affiliate channel worked

Post submitted 2026-04-16 (5 months before fetch), by u/Extra-Motor-8227 (same builder as Block 12, later update).

> "Found 130 newsletter owners in the social media / marketing / SaaS space. Personalized every email... Got 2 replies. Both said no." / "Last Wednesday morning... Phone buzzes. New customer. Then another... 5 paid customers before I finished eating... By end of day: 8 sales total. All from affiliates. MRR jumped from €255 to €350."

Direct cold-email-to-newsletter-owners channel: 130 emails, 0% conversion to partnership. Affiliate program (40% recurring commission via Affonso) is what converted.

## Block 14 — r/SaaS: "I put $100 into Reddit ads. I got 50 clicks, but not a single conversion." (same author, prior post)

> "The issue with running ads early on is that you're reaching out to people who aren't looking for your product... My first eight posts there [IndieHackers] got almost no response... on my ninth post, I got 468 views, 25 comments, and 26 new users, all for free."

---

## Block 15 — Vietnam/non-US-founder selling into the US: Stripe Atlas verification breaks specifically for non-US-resident LLC owners

URL: r/stripe via `old.reddit.com/r/SaaS/search?q=Stripe+Atlas+non-US+founder`
Fetch date: 2026-09-16. Channel: browser.

Post: "Is Stripe quietly blocking non-US LLC founders?" — r/stripe, 1 point, 25 comments, submitted 3 months before fetch (~2026-06).

> "I formed a US single-member LLC through Stripe Atlas. I am a non-US resident living outside the US, and I do not have an SSN or ITIN... If I enter my actual non-US residential address as the account representative's address, Stripe rejects it and says that the representative must have a US address. If I enter a US address... Stripe requires a full SSN, which I do not have." / "Update 2026/06/16: I reached out to u/stripesupport on Twitter, and they confirmed that 'US-based accounts must have a physical presence in the United States.'"

This is the single most direct, dated (2026-06-16) confirmation that Stripe now requires either an SSN/ITIN or a genuine US physical presence for the account representative on a non-US-founder LLC — a real, current barrier for a Vietnam-based team, not a hypothetical.

## Block 16 — Same thread cluster: "Bootstrapped, non US founder, first real customer ready to pay and I'm stuck on LLC vs Delaware C-Corp"

r/SaaS, 8 points, 24 comments, ~4 months before fetch.

> "I'm not based in the US even though basically all my customers are. Planning to incorporate through Stripe Atlas or Firstbase... Neither of us are US citizens or residents which I know complicates the tax side... The pass-through taxation thing as a non-US founder still confuses me."

## Block 17 — "Stripe Atlas alternatives for foreign founders" — Pakistan-based team, Stripe Atlas application stuck in review 4 weeks

r/llc_life, 6 points, 18 comments, ~6 months before fetch.

> "My co founders and I are based in Pakistan... Initially we tried using Stripe Atlas to handle the company formation, but the experience was not great. Our application ended up sitting in review for about four weeks with very little communication from support."

## Block 18 — Form 5472 trap for non-US-owned single-member LLCs (IRS penalty risk, not disclosed upfront by Stripe Atlas)

r/Form5472_us, 1 point, 0 comments, ~11 months before fetch.

> "I love Stripe Atlas — it made setting up a U.S. LLC super simple. But what they don't tell you is that if you're a non-U.S. founder, the IRS expects you to file Form 5472 + pro forma 1120 every year... Even just putting money into the company from my own pocket counts as a 'reportable transaction.' The scary part is the $25k penalty for missing it."

## Block 19 — Non-US founder banking: Brex/Mercury require a US residential address for KYC even for a Stripe-Atlas-incorporated Delaware entity

r/startups, 7 points, 16 comments, ~5 months before fetch.

> "I've received a request from Brex to update Proof of Residential address. We incorporated our company in Delaware (Stripe Atlas), we are non-US founders, we don't live in US, so we could not meet this requirement."

## Block 20 — Stripe Atlas's own vendor-published process (company-stated, for comparison against the founder complaints above)

r/StripeTeam AMA post, Stripe employee, all-time.

> "We form a company every 12 minutes (including 1 in 4 YC companies)... One-time fee: $500... For non-US founders, this [EIN] process typically takes 2-4 weeks... Stripe and Atlas do not provide banking services - banking services are provided by separate financial institutions including Mercury, Brex, and others."

**Reading Blocks 15-20 together:** Stripe's own copy says the EIN step "typically takes 2-4 weeks" for non-US founders, but real threads (Blocks 15-19) show account-representative verification, bank KYC (Mercury/Brex address requirements), and Form 5472 as three separate, recurring friction points not mentioned in Stripe's own onboarding copy — each with dated, first-person confirmation. This is the strongest evidence set gathered this pass for "being taken seriously" / entity-formation friction for a non-US (Vietnam-applicable) founding team.

---

# TARGET 2 — Founder-count outcome data

## Block 21 — Wasserman's "The Founder's Dilemmas": book itself remains paywalled; only third-party summaries locatable, no direct primary quote on team-size-vs-outcome obtained this pass

Searched: Google for "Noam Wasserman Founder's Dilemmas solo founder two founders team size equity study 10000 founders." Results were all third-party summaries (Strategia-X blog, Commenda blog, CT Acquisitions blog, Pillsbury Propel law-firm blog, HackMD notes) repeating the "10,000 founders / ~6,000 startups" sample-size claim, none quoting Wasserman's original team-size-and-outcome tables directly. One candidate source (Strategia-X's "The Dangerous Myth of the Technical Co-Founder") turned out, on inspection, to be a low-quality SEO/content-marketing site (internal tag structure "LEOP-2383 / OP-2383 / PUB" visible in its own page furniture) — not cited as a source.

`unknown — checked Google search "Noam Wasserman Founder's Dilemmas solo founder two founders team size equity study" 2026-09-16 — no direct primary quote from the book on team-size-vs-outcome located; the book's actual dataset tables were not accessible without purchase.`

## Block 22 — The number everyone actually cites is Startup Genome's, not Wasserman's — and it traces to a widely-repeated but methodologically contested 2011 report

URL: `https://blog.asmartbear.com/startup-genome-project/` — Jason Cohen ("A Smart Bear"), tech-blogger essay w/ published rebuttal from the Startup Genome team itself
Fetch date: 2026-09-16. Channel: browser. Type: trade-press / peer-reviewed-adjacent methodology critique, with the original researcher's own response reprinted in full.

> "The Startup Genome Project wherein global 'rules of business' have been extrapolated from a survey of **650 startups**." / "Solo founders take 3.6x longer to reach scale" and "Startups that pivot once or twice raise 2.5x more money than those that don't." [as Startup Genome's own headline claims, quoted by Cohen]

Cohen's methodology critique (his own words):

> "It suffers from Survivor Bias... they interviewed 650 companies, which means extant companies, which means we don't know which of these trends contributed to success and which are just trends that everyone is doing, even the companies who failed." / "It suffers from the Pattern-Seeking Fallacy... With hundreds of questions and literally millions of data points correlating one thing to another, they found some data supporting some parts of the model, and some data did not (i.e. was not statistically significant). But they reported only the supporting data."

Startup Genome co-founder **Ron Berman's own reply**, reprinted in the same post (this is the closest thing to a primary-source admission of the study's limits located this session):

> "Survivorship bias may indeed be a valid issue in our sample... Our results therefore apply only to the sample we analyzed. In other words, if you take another sample of startups, they might not apply." / "We have not used [cross-validation]... as **the sample is too small**, but plan on applying it in the future." / "There might be incorrect results being reported. In general whenever you receive a result which is significant with 95% confidence, there is 5% chance it is incorrect."

vendor-reported (Startup Genome) / peer-critiqued (Jason Cohen, tech blogger, not academic peer review) — sample size **n=650 companies**, all survivors at time of survey (survivorship bias explicitly conceded by the study's own co-founder), cross-sectional not longitudinal, statistical-significance thresholds as low as 80% used per the researchers' own admission.

## Block 23 — The specific "3.6x longer" / "2.3x less likely to pivot" figure's original primary URL (startupgenome.com / startupgenomereport.com) is dead; only secondary citations of it remain live

Attempted: `https://startupgenome.com/article/discover-the-patterns-of-successful-internet-startups` — 301-redirected to the current corporate homepage (Startup Genome is now a paid ecosystem-consulting firm; the original 2011 blog post is gone). Attempted: `https://s3.amazonaws.com/startupcompass-public/StartupGenomeReport2_Why_Startups_Fail_v2.pdf` (guessed) — did not resolve to the report. Attempted Wayback Machine on `startupgenomereport.com/report` — "The Wayback Machine has not archived that URL."

`unknown — checked https://startupgenome.com/article/discover-the-patterns-of-successful-internet-startups, a guessed S3 PDF path, and web.archive.org 2026-09-16 — original primary report page no longer resolves; every live citation of the "3.6x longer / 2.3x less likely to pivot" number found this pass (Steve Blank's blog, Fast Company 2011, and dozens of 2026 SEO round-ups) is a secondary retelling of the same 2011 Startup Genome claim, not an independently re-run study.`

**Bottom-line finding for target 2, stated plainly:** the founder-count-vs-outcome number everyone repeats ("solo founders take 3.6x longer to reach scale, are 2.3x less likely to pivot," and its "two is ideal" folklore descendant) traces to one 2011 survey of 650 already-surviving startups, whose own author has since conceded survivorship bias and an under-powered sample for cross-validation — and the primary report itself is no longer online. Wasserman's *Founder's Dilemmas* (n≈10,000 founders / ~6,000 startups, the more rigorous and more commonly *name-checked* source) could not be quoted directly this session — it is real, peer-reviewed-adjacent (Harvard Business School dataset, Princeton University Press), but paywalled, and no secondary source located this pass quoted its actual team-size-and-outcome tables verbatim rather than its equity-split findings. **This is close to "everyone repeats a number and nobody it's actually citing is the rigorous one" — the rigorous study (Wasserman) is real but unquoted; the widely-quoted study (Startup Genome) is real but methodologically thin by its own author's admission.**

---

# TARGET 3 — Marketplace economics

## Block 24 — AWS Marketplace: eligible-jurisdiction list for paid products does NOT include Vietnam

URL: `https://docs.aws.amazon.com/marketplace/latest/userguide/user-guide-for-sellers.html` ("Getting started as an AWS Marketplace seller")
Fetch date: 2026-09-16. Channel: browser (this JS-rendered doc page 404'd/rendered-empty under WebFetch in the prior session; it renders completely in a real Chrome session).

> "To sell paid software in AWS Marketplace, you must be a permanent resident or citizen in one of the following countries or SARs, or a business entity organized or incorporated therein: Australia, Bahrain, Colombia, European Union (EU) member state, Hong Kong SAR, India, Israel, Japan, New Zealand, Norway, Qatar, South Korea, Switzerland, United Arab Emirates (UAE), United Kingdom (UK), United States (US)." / "Non-US sellers are required to provide a (i) W-8 form, value-added tax (VAT) or goods and services tax (GST) registration number, and (ii) bank account with a SWIFT code in an eligible jurisdiction." / "If a business entity is not incorporated in one of the countries or SARs listed above, see Resource for companies outside of AWS Marketplace jurisdictions."

vendor-published, company-stated, dated (page metadata "August 27, 2025" per the "related pages" abstract on the same fetch). **Vietnam is not on this list.** A Vietnam-incorporated entity cannot register as an AWS Marketplace seller of paid products directly — it would need an entity in one of the listed jurisdictions (e.g., a Singapore or US subsidiary) to sell paid listings. Free-product listing has no jurisdiction restriction stated on this page.

## Block 25 — AWS Marketplace: listing-fee percentage itself not recovered this pass either

Multiple guessed doc-page URLs for the "Listings fees" chapter (linked from the sidebar of Block 24's page, titled "Listings fees") returned either the guide's homepage (redirect) or repeated failed in-page navigation clicks; the actual fee percentage table was not reached this session.

`unknown — checked docs.aws.amazon.com/marketplace/latest/userguide/ sidebar navigation and multiple guessed direct URLs 2026-09-16 — the eligible-jurisdiction list (Block 24) was recovered but the specific AWS Marketplace listing-fee percentage was not.`

## Block 26 — Shopify App Store revenue share: exact current rates recovered from the primary developer-docs page

URL: `https://shopify.dev/docs/apps/launch/distribution/revenue-share`
Fetch date: 2026-09-16. Channel: browser. Type: vendor-published, primary (Shopify's own developer platform docs).

> "Shopify's revenue share model is designed to help app developers grow. You keep 100% of your first $1,000,000 USD in gross app revenue earned from January 1, 2025, and 85% of earnings above that. All billing is subject to a 2.9% processing fee and applicable sales tax." / "To access the revenue share plan, you need to register with the Shopify App Store for a one-time fee of $19 USD per Partner account." / Standard-rates table: "First $1,000,000 USD — 0%" revenue share rate; "Above $1,000,000 USD — 15%." / "Developers who earned $20,000,000 USD or more through the Shopify App Store in the prior calendar year, or who have a gross company revenue of $100,000,000 USD or more, pay 15% revenue share on all app revenue. The 0% rate on the first $1,000,000 USD doesn't apply."

This fully resolves the prior session's Shopify 404. Effective commission: **0% up to $1M lifetime gross app revenue, 15% (i.e., seller keeps 85%) above that**, plus a flat 2.9% payment-processing fee on all billing and a one-time $19 registration fee. Large developers ($20M+/yr App Store revenue or $100M+/yr company revenue) lose the $1M free tier and pay 15% on everything.

## Block 27 — Shopify Partner payouts run through Hyperwallet; no explicit country-eligibility list found, but the mechanism is the same one used by many Southeast Asian freelance platforms

URL: `https://help.shopify.com/en/partners/partner-program/getting-paid`
Fetch date: 2026-09-16. Channel: browser.

> "As a Shopify Partner, you earn money based on your contribution to the Shopify ecosystem... All you need is a minimum of $25 in earnings to receive a payout from Shopify... Payments are delivered through Hyperwallet."

`unknown — checked help.shopify.com/en/partners/partner-program/getting-paid 2026-09-16 — page describes payout mechanics (Hyperwallet, $25 threshold, twice-monthly schedule) but does not itself list which countries are eligible; Hyperwallet's own country coverage (widely used by Upwork, Airbnb, etc. for cross-border payouts) is broad but Vietnam-specific confirmation was not independently verified this pass.`

## Block 28 — Upwork + Vietnam: no primary restriction found; Vietnamese-language community guides confirm routine practice

Attempted: `support.upwork.com` article on Payoneer withdrawal (404'd on the guessed article ID) and `upwork.com/nx/hire/where-freelancers-work/` (404'd). Both failures were genuine 404s, not domain blocks (confirmed via retry).

Bing search surfaced, among the results: a Vietnamese-language guide titled **"Hướng Dẫn Rút Tiền Upwork/Payoneer Về Việt Nam (2025) Chi Tiết"** (sinhmmo.com) — "Detailed guide to withdrawing Upwork money to Vietnam via Payoneer 2025: procedure, fees, exchange rate, tips to avoid errors, fastest withdrawal method" — and multiple Vietnamese-language YouTube videos on the same workflow (e.g., "Compare 4 ways to withdraw money from Upwork... Paypal, Payoneer, Local Bank," by a Vietnamese-titled channel).

`unknown (as a primary Upwork/Payoneer statement) — checked support.upwork.com and upwork.com 2026-09-16, both guessed URLs 404'd; not independently re-searched for the correct live article this pass.` However, the volume and specificity of Vietnamese-language community how-to content (trade/community-press, not vendor-stated) is itself decent secondary evidence that Vietnamese freelancers routinely withdraw Upwork earnings via Payoneer today — Upwork does not appear to be one of its short list of embargoed/restricted countries (which typically covers OFAC-sanctioned states, not Vietnam).

---

# TARGET 4 — CAC benchmarks

## Block 29 — Every "B2B SaaS CAC benchmark" result surfaced this pass is a content-marketing/agency page reciting the same $536–$702 figure with no disclosed methodology

Checked directly: `https://www.thezulumethod.com` — its CAC-benchmark blog post ranked #1 for the exact query, but the site itself is "The Marketing Agency for Funded B2B Tech Startups" — its own homepage copy:

> "We currently offer the following AI automated Marketing channels: (1) Email Platform... (2) PPC Campaigns... Each Marketing channel automation includes many AI agents working together under expert human supervision."

i.e., a marketing-services vendor whose CAC-benchmark post exists to sell its own services — no stated sample, no stated methodology, on the page examined.

Also seen repeating the identical "$536–$702" / "B2B SaaS companies average $702 overall, ranging from $536 for mid-market" figure, word-for-word or near-word-for-word, across independent-looking domains: growthcentr.com, shno.co ("Shnoco"), saashero.net, digitalapplied.com, enrichlabs.ai, corpify.org — a pattern consistent with one ultimate source (likely a single aggregator or an LLM-generated content run) being recirculated across many SEO domains, none showing a disclosed primary methodology in the search snippets examined.

Attempted a more credible-looking candidate, **First Page Sage** (`firstpagesage.com/reports/average-customer-acquisition-cost-cac-by-industry-b2b-edition-fc/`) — a marketing-consultancy that does publish named-methodology reports elsewhere on its own site — but the page's real report body did not render in this session's text extraction (only an unrelated "Plastic Surgery Patient Acquisition Costs" cross-link teaser came through on three consecutive extraction attempts).

`unknown — checked firstpagesage.com/reports/average-customer-acquisition-cost-cac-by-industry-b2b-edition-fc/ 2026-09-16 — page loaded (confirmed via tab title) but its methodology/numbers section could not be extracted this session; not confirmed as a good source, not ruled out either.`

**Finding for target 4, per the task's own instruction to record rather than guess:** no B2B SaaS CAC source with a disclosed, checkable methodology was confirmed this pass. The one number in circulation ($536–$702 median) appears on enough obviously-content-marketing domains, phrased almost identically, that it should not be compiled as a sourced fact — record as `unknown — checked thezulumethod.com, growthcentr.com, shno.co, firstpagesage.com and five other domains 2026-09-16, no source with disclosed methodology confirmed`.

## Block 30 — Professional-services CAC: not separately investigated this pass given target-4 time budget and the SaaS-CAC dead end

`unknown — checked (SaaS CAC sources only this pass) 2026-09-16 — professional-services CAC benchmark not separately searched; flag for a future pass.`

---

# TARGET 5 — Cold email benchmark (absolute number, with sample size)

## Block 31 — Instantly's 2026 Cold Email Benchmark Report: absolute reply rate, "billions of emails," with percentile breakdown — recovered via a secondary aggregator that names and dates the primary vendor report

URL: `https://satellyte.ai/tools/reply-rate-benchmark`
Fetch date: 2026-09-16. Channel: browser. Type: secondary aggregator page (Satellyte, a sales-outreach tool) that explicitly footnotes primary sources rather than paraphrasing them — its own stated policy: "We cite original studies (Ehrenberg-Bass, RAIN Group, HubSpot, Bridge Group, Instantly, Belkins) rather than secondhand vendor blog posts." Instantly's own report page (`instantly.ai/blog/cold-email-benchmark-report` and variants) 404'd on every URL guessed this session — recorded as a genuine fetch failure, not a permission block (confirmed via retry showing real 404 page furniture).

> "[1] Cold reply baseline — Instantly Cold Email Benchmark Report 2026 (billions of emails sent Jan to Dec 2025): **3.43% platform-wide cold email reply rate.** Top 25% of senders achieve 5.5%+; the elite top 10% reach 10.7%+." — cited to "INSTANTLY COLD EMAIL BENCHMARK REPORT 2026."

> "[4] Reply rate decline — Cold email reply rate trend: 8.5% (2019) to ~7% (2023) to ~5.1% (2024) to 3.43% platform avg (Instantly 2026). Belkins 2025 study found a 15% YoY decline from 2023 (6.8%) to 2024 (5.8%)."

vendor-reported (Instantly), self-selection caveat: this is Instantly's own platform data (its own customers' campaigns sent through its own tool), not an independent audit — the same self-selection problem flagged in the task brief for Woodpecker applies here too (a sending platform's own aggregate necessarily excludes non-customers and may skew toward whatever list-quality/targeting practices its customer base uses).

## Block 32 — Belkins 2025 Cold Email Response Rate Study: 16.5M emails, 93 industries, absolute industry-level reply rates

Same source/fetch as Block 31.

> "[2] Top industry reply — Belkins 2025 Cold Email Response Rate Study (16.5M emails, 93 industries): Solar, Construction, and Environmental Services lead at 6.3%+ reply with 43 to 48% open rate. IT Consulting 5.93%, Software Development 5.89%, Business Consulting 5.92%, Cloud Solutions 4.97%, Cybersecurity 4.86%."

vendor-reported (Belkins, a cold-email/lead-gen agency) — n=16.5 million emails is a large, stated sample; same self-selection caveat as above (Belkins' own client campaigns only).

## Block 33 — Expandi State of LinkedIn Outreach H1 2025: channel comparison with a large, stated sample

Same source/fetch as Block 31.

> "[3] LinkedIn vs email — Expandi State of LinkedIn Outreach H1 2025 (70,130+ campaigns, 13K accounts, 20M+ attempts): LinkedIn DM reply rate averages 10.3% versus cold email 5.1% (~2x lift)."

## Block 34 — Belkins LinkedIn Outreach Study 2025: personalization lift, absolute numbers

Same source/fetch as Block 31.

> "[5] Personalization lift — Belkins LinkedIn Outreach Study 2025: connection-request acceptance is nearly identical with or without a note (26.42% vs 26.37%), but reply rate jumps to 9.36% with a personalized message vs 5.44% without (72% lift)."

**Finding for target 5:** the Woodpecker-only dead end from the prior pass is resolved — Instantly (3.43% platform-wide, billions of emails, 2026) and Belkins (16.5M emails, 93 industries, 2025) both give absolute, sample-sized, vendor-published reply-rate numbers, reached via a third-party aggregator that footnotes primary sources rather than paraphrasing. All four numbers carry the self-selection caveat the task brief anticipated: they describe each vendor's own paying customers' campaigns, not a random sample of all cold email sent.

---

# TARGET 6 — Two unresolved company facts (worked as time allowed)

## Block 35 — Character.AI / Google deal: $2.7B figure traced to WSJ via trade press; primary WSJ article itself not directly fetched

URL: `https://dataconomy.com/2024/09/26/why-google-paid-2-7-billion-to-reclaim-its-lost-ai-genius/` (title confirmed via tab; full article body did not extract cleanly — extraction returned only an unrelated related-post teaser on three attempts)
Search-snippet text actually read in the browser (Bing SERP, 2026-09-16): "Why Google paid $2.7 billion to reclaim its lost AI genius... As of last year, Character.AI rapidly achieved a valuation of $1 billion. In any case, **according to WSJ, the $2.7 billion**..." [snippet truncated by the search engine, not by this session].

trade-press (Dataconomy), citing a primary source (Wall Street Journal) by name and specific figure, dated 2024-09-26. Also seen independently in the same Bing result set: MacMyths ("Alphabet's..."), FourWeekMBA ("Google-Character.AI Deal: The $2.7B 'Licensing' Deal"), synthlust.com ("In August 2024, Google struck a $2.7B licensing deal with Character.AI that brought back its founders and paid out investors").

`Confirmed as reported (not confirmed as a primary-document figure this pass) — checked dataconomy.com, macmyths.com, fourweekmba.com, synthlust.com 2026-09-16, all trade-press, all attributing the $2.7B figure to WSJ reporting; the WSJ article itself was not directly fetched this session.`

## Block 36 — Clay's second and third co-founders named (resolves prior session's gap — only Kareem Amin was found before)

Source: Bing SERP text, 2026-09-16, citing techfundingnews.com ("Clay hits $7.1B valuation with $115M raise," dated ~6 days before fetch) and egyptinnovate.com ("Founded by Egyptian Entrepreneur, U.S. AI Company Clay Raises...", ~1 day before fetch).

> "Nicolae Rusan co-founded the company alongside Amin, and Varun Anand joined as a third co-founder in 2021 as Clay..." [techfundingnews.com] / "Before founding Clay, Amin co-founded New York-based e-commerce technology company Frame with entrepreneur [name cut off in snippet]..." [egyptinnovate.com]

Also: Varun Anand's own LinkedIn headline, per the SERP snippet: "Co-Founder @ Clay | ... I'm the co-founder and head of operations at Clay."

trade-press-reported: Clay's founding team is **Kareem Amin + Nicolae Rusan** (co-founders), with **Varun Anand** joining as a third co-founder in 2021. This resolves the prior pass's "second co-founder unknown" gap, though it complicates the "exactly two founders" framing — Clay is a three-founder company by this account, with Anand joining ~4 years after founding (chronology of Clay's 2017/2019 founding-date discrepancy already flagged in `two-founder-cases-pulls.md` Block 4).

## Block 37 — Granola's second co-founder named: Sam Stephenson

Source: Bing SERP text, 2026-09-16, citing digitalfrontier.com ("A recipe for everyday AI," dated 2024-12-03).

> "When it came time to create a repository on Github for a new project, Sam Stephenson was eating a bowl of granola... 'That's the story he tells,' says Stephenson's co-founder Chris Pedregal, with a skeptical smile."

trade-press (Digital Frontier interview piece), quoting Pedregal directly calling Stephenson "co-founder." Resolves Granola's second-founder gap: **Chris Pedregal (CEO) + Sam Stephenson**.

## Block 38 — Cal AI's second co-founder named: Henry Langmack

Source: Bing SERP text, 2026-09-16, citing buildr.news ("Two high schoolers built an app that counts calories from a photo," dated ~2026-07-05).

> "How Zach Yadegari and Henry Langmack built Cal AI — an app that logs calories from a food photo — as 17-year-old..." [headline, truncated by search snippet]

Also flagged: Henry Langmack's current LinkedIn headline (per SERP snippet) reads "Cofounder @ Soar / 19 Years Old" — i.e., as of this fetch he is publicly associated with a different venture (Soar), not listed as currently at Cal AI, which may indicate he has since exited Cal AI. Not independently confirmed beyond the snippet; flagged as a caveat, not a fact.

trade-press-reported: Cal AI's founding pair is **Zach Yadegari + Henry Langmack**.

## Block 39 — Gamma's second co-founder: not found this pass

Every source surfaced (LinkedIn, Gamma's own site, Stanford STVP, YouTube interviews) names only **Grant Lee** as "co-founder and CEO" of Gamma; no other individual is named as a co-founder in any snippet read this session.

`unknown — checked Bing SERP for "Gamma app AI presentation startup founders names Grant Lee co-founder" 2026-09-16 — only Grant Lee is named as co-founder across all sources surfaced; a second co-founder, if one exists, was not identified.`
