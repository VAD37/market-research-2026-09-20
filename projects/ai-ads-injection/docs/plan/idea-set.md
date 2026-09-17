# Idea set — eight product shapes from the wave-1 evidence

2026-09-17, wave 2a (idea + daydream). Sources: `../explore/{carrier-state,detection-surface,edge-controls,policy-ceiling,who-sells-this}.md` and the `raw/` files behind them; research layer `../../../../docs/{markets/ai-search-ads.md,competitors/ai-search-ads-roster.md,findings/injection-feasibility.md,findings/cross-read.md,customers/answer-integrity-buyer.md,method/scope.md}`. No architecture here (wave 2c). Not self-fact-checked (wave 2b). Speculation is confined to §5.

`../explore/policy-ceiling-addendum.md` (wave 1b) did not exist when this was written. Every candidate whose legality turns on one of its five documents names the document and states which way it breaks. Those conditionals are §4.

## 0. Pending-document codes

| Code | Document | Never read by any pass |
|---|---|---|
| **P1** | OpenAI Business Terms / Services Agreement | `../explore/carrier-state.md` item 9 |
| **P2** | Perplexity API Terms of Service | `../explore/carrier-state.md` item 10 |
| **P3** | OpenAI Ads Terms (`openai.com/policies/ads-terms/`) | 403 both passes |
| **P4** | Bing / Copilot webmaster cloaking policy | JS shell, 0 hits for "cloak" in 125,562 bytes |
| **P5** | Vietnam Law on Advertising 16/2012/QH13 | 4 URLs failed, WebSearch "unavailable" |

## 1. Standing constraints every candidate is scored against

From `../../../../docs/method/scope.md` (set 2026-09-16, geography confirmed HCMC Vietnam): two people, one technical builder, no funding, remote-first async, **no US market access**, no field-sales motion.

From `raw/local-infra-check.txt` (2026-09-17): no domain, no Cloudflare account, no wrangler/cloudflared/vercel/netlify CLI, no server. Every build estimate below starts from that.

From `../explore/edge-controls.md`: Workers is the only Cloudflare primitive that can vary a response body. WAF custom rules cannot (Block / Managed Challenge / Skip / Log only). Transform Rules cannot ("URI path, query string, and HTTP headers" — body out of scope). Pay per crawl still private beta at the 2026-08-14 page stamp.

**Two prohibitions already settled and cross-cutting** — they hit the answer-sampling half of five candidates below:

- OpenAI Terms of Use (effective 2026-01-01, browser-fetched pass 2): bars "Automatically or programmatically extract data or Output."
- Perplexity ToS (last updated 2026-01-23) s5.2(i): bars automated collection "**or engage in any manual process to do the same**" — the hand-run workaround is closed by name. s5.1 personal/non-commercial only; s5.2(e) bars commercial exploitation.

Consequence, stated once: **any product that reads answers off consumer ChatGPT or perplexity.ai is prohibited today, by a document already read.** The API path is the only route, and the documents governing it are P1 and P2.

Build estimates below are **engineering judgment, not sourced** — flagged for wave 2b.

## 2. Candidate set

| ID | Shape | Who pays | Legal bucket | Build est. (1 dev, zero infra) |
|---|---|---|---|---|
| C1 | Crawl-to-answer audit, origin-instrumented | Site owner / brand | Split: logs permitted, answers pending P1+P2 | 2–4 weeks to first real report |
| C2 | Crawler-identity dataset + resolver library | Nobody directly; distribution asset | Clearly permitted | 3–5 days |
| C3a | Differential serving, undisclosed paid placement | Advertiser | **Prohibited — Google spam policy, UCPD item 11** | 1 week (irrelevant) |
| C3b | Content-equivalent machine variant delivery | Site owner | Permitted, reputationally hazardous; P4 | 1–2 weeks |
| C4 | Brand-side answer monitoring and drift alerting | Comms / brand protection | Pending P1+P2; consumer surfaces prohibited | 3–6 weeks |
| C5 | Cloaking detection sold to the opposite side | Engines, ad verifiers, publishers | **Out of boundary at scale** (third-party fetching) | 2–3 weeks |
| C6 | Vietnamese-language answer-visibility measurement | VN brands / agencies | Pending P1+P2; P5 if it ever places ads | 4–8 weeks |
| C7 | OAI-AdsBot landing-page observability | ChatGPT advertisers | Pending P3 — decides both legality and demand | 1–2 weeks |
| C8 | Original research → paid audit engagements | Client of the audit | Clearly permitted on own-infra half | 3–6 weeks to publishable artifact |

### C1 — Crawl-to-answer audit (origin-instrumented)

**Does:** own domain + Worker logs every assistant fetch by IP-range match, then samples what the assistants say about that page, and joins the two. The join is the product: *this fetch, at this time, became this sentence*.

**Support:** `../explore/detection-surface.md` — IP-range matching works for OpenAI (21/39/215/2 prefixes across four files), Anthropic (26 prefixes, `creationTime 2026-08-18T23:56:36Z`), Perplexity (8 + 4). `../explore/edge-controls.md` — a free-tier Worker doing CIDR match needs no Cloudflare Enterprise bot score. `../../../../docs/findings/injection-feasibility.md`: of the published four-step method, "Step 4 is what nobody sells."

**Who pays:** the site owner. Price anchor, aggregator-sourced, `../../../../docs/customers/answer-integrity-buyer.md`: one-time GEO audit $1,500–$5,000; GEO added to an SEO retainer +20–30% of MRR. No price exists anywhere for a defense-specific line item — that is that file's own finding.

**What kills it:** the crawl-log half is already free — Cloudflare AI Crawl Control is "zero-config on all Cloudflare plans" and tells you a crawler visited. Pass 2's line stands: "The monitoring layer for crawler identity is already free and bundled. That prices the floor." Only the *join* is unpriced, and no buyer has been found paying for it.

**Pending doc:** P1 + P2. **Breaks bad** if OpenAI Business Terms or Perplexity API ToS bar benchmarking, competitive use or output retention — then only the free half survives and there is no product. **Breaks good** if they carry only OpenAI Service Terms' "use APIs in accordance with the applicable documentation" — then the sampling half is contractually clean and C1 is the cleanest shape in this file.

### C2 — Crawler-identity dataset + resolver library

**Does:** normalized, timestamped, diffed CIDR feed for GPTBot / OAI-SearchBot / ChatGPT-User / OAI-AdsBot / Anthropic / PerplexityBot / Perplexity-User / Googlebot / CCBot, plus a Worker-drop-in matcher. Its one non-obvious asset is refresh cadence, measured: `oai-chatgptuser.json` had `creationTime 2026-09-17T05:04:56`, roughly two hours before the pull, while `oai-gptbot.json` has not moved since `2025-10-30T11:00:00` (`raw/crawler-ip-ranges-2026-09-17.md`). A detector caching both on one cycle silently misses addresses.

**Support:** same file; plus `raw/rdns-lookups.txt` — the negative that justifies the library existing at all: 3/3 sampled GPTBot IPs, the sampled SearchBot IP and both sampled AdsBot IPs return `Non-existent domain` against 8.8.8.8; Anthropic resolves to `*.bc.googleusercontent.com` / `ec2-*.us-east-2.compute.amazonaws.com`; Perplexity to `ec2-*.compute-1.amazonaws.com`. Only Google (`crawl-66-249-66-1.googlebot.com`) and CommonCrawl (`18-97-9-169.crawl.commoncrawl.org`) have vanity rDNS. Google's documented forward-confirm procedure is therefore Google-only.

**Who pays:** nobody, directly. This is a distribution and credibility asset, consistent with `../../../../docs/findings/cross-read.md` pattern 5 (Invariant Labs acquired by Snyk Jun 2025 off a published finding; Mindgard's Cursor zero-day as lead marketing asset).

**What kills it:** zero revenue, and Cloudflare's free AI Crawl Control plus each vendor's own JSON make it a convenience, not a need.

**Pending doc:** none. Public vendor files, public DNS. Clearly permitted under everything read.

### C3a — Differential serving with undisclosed paid placement

**Does:** the literal original hypothesis. Detect the assistant fetch, serve it product-placement text a human never sees.

**Kept in this file because deleting it loses the reasoning.** It is prohibited twice over by documents already read:

- Google spam policy, `Last Updated: 2026-08-28`, cloaking defined as "Presenting different content to users and search engines with the intent to manipulate search rankings and mislead users," with the named example "inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor." Same page separately names "attempting to manipulate generative AI responses in Google Search" as spam. Enforcement: demotion or removal.
- UCPD Annex I item 11, verbatim via UK SI 2008/1277 Sch.1 (`raw/policy-and-edge-pulls.md` line 112): "Using editorial content in the media to promote a product where a trader has paid for the promotion without making that clear in the content or by images or sounds clearly identifiable by the consumer (advertorial)." Annex I is the per-se list — unfair "in all circumstances," no balancing test.

**Pending doc:** P5 would add Vietnamese exposure on the team's home turf; P4 would add a second platform. Neither can rescue it — two independent prohibitions are already on file. **Breaks no way.** It is out on evidence, not on caution.

### C3b — Content-equivalent machine variant delivery

**Does:** serve a detected assistant a clean structured rendering of the *same* page — markdown, schema.org, an `/llms.txt`-shaped surface — stripped of nav and script. Semantically identical, mechanically different.

**Support:** `../../../../docs/findings/injection-feasibility.md` names llms.txt plus schema.org as "the sanctioned channel," publisher-side and declarative. `../explore/edge-controls.md` — a Worker can do this; a Transform Rule cannot.

**Who pays:** site owners who want to be legible to assistants. Competes against writing a static `/llms.txt` by hand, which is free.

**What kills it:** two things. The free hand-written substitute. And the drift risk — the distance between "same content, better format" and "enhanced content" is a judgment call the *customer* makes, and one customer crossing it puts the vendor inside C3a's definition with the vendor's own Worker as the instrument.

**Pending doc:** P4. Google's cloaking rule has an intent hinge ("with the intent to manipulate… and mislead users") that C3b survives. **Breaks bad** if Microsoft's webmaster policy states a bright-line "same bytes to bot and human" rule with no intent test — then C3b is cloaking on Bing/Copilot regardless of equivalence, and the shape narrows to Google-and-Anthropic-only. **Breaks good** if Microsoft mirrors Google's intent test or is silent, which leaves C3b permitted everywhere read.

### C4 — Brand-side answer monitoring and drift alerting

**Does:** poll engines about a brand on a schedule, diff the answers, alert on change or on a false claim appearing. No origin instrumentation, so it sells to companies whose page you do not control.

**Support / against:** this is the crowded lane. `../../../../docs/competitors/ai-search-ads-roster.md`: Profound $96M Series C 2026-02-24 at $1B plus $180M Series D 2026-09-16 at $1.8B, ~62 staff (2025), $6.8M revenue 2025; Peec AI $29M and "$0 to $4M+ ARR in 10 months, 1,300+ brands" (company blog); price floor $29/mo Otterly. `../explore/who-sells-this.md` re-checked Profound's pricing 2026-09-17: still trial-plus-Enterprise, no self-serve tier.

The one differentiated sub-shape the evidence supports is *integrity*, not visibility: `../../../../docs/customers/answer-integrity-buyer.md` finds exactly one vendor selling it — BrandShield AI Platforms Protection, launched 2026-04-01, covering ChatGPT / Gemini / Perplexity / Grok, price undisclosed, demo-only — and seven of eight other DRP vendors checked one by one as not covering it.

**What kills it:** `../../../../docs/findings/cross-read.md` team scorecard scores `ai-search-ads` **Fails** on "no capital" and **Fails** on "no field sales" at enterprise tier. And no price for an integrity line item was found in any channel. Demand is discretionary through 2027 at least — EU AI Act high-risk obligations moved to 2027-12-02 / 2028-08-02; FTC's Jul-2026 statement says hallucinations "in and of themselves" do not raise Section 5 issues.

**Pending doc:** P1 + P2, same as C1 and harder — C4 *is* the sampling. **Breaks bad** and the candidate ends: with consumer surfaces already prohibited and the API route closed, there is no legal way to poll. **Breaks good** and it survives contractually into a market with $131M+ of funded competition.

### C5 — Cloaking detection sold to the opposite side

**Does:** fetch a page twice — once as an ordinary browser, once presenting a declared crawler identity — diff, and flag pages serving assistants something humans do not see. Buyers: the engines' own trust-and-safety teams, ad verifiers, publishers.

**Support:** the method is published and reusable — Cloudflare's Aug-2025 Perplexity test (control domain, robots.txt disallow, then query the engine and see if it knows) is exactly this shape. The buyer-adjacency is real and moving: `../../../../docs/customers/answer-integrity-buyer.md` — DoubleVerify DV AI Verification 2025-11-04, SlopStopper for social 2026-04-17 ("500M+ impressions monitored or blocked since Jan 2026," company-stated), HUMAN Ad Integrity Suite 2026-06-16, HUMAN LLM and AI Agent Governance 2026-09-16. Every one of them is "don't put my ad near AI slop." None verifies an answer.

**Out of boundary at scale, and marked so.** The project's hard rule is authorized testing on infrastructure the tester owns plus public endpoints. Fetching one public page is inside that. But C5's product is *systematic third-party fetching while presenting a crawler identity that is not yours*, from IPs outside that crawler's published range — which is the exact behaviour pattern Cloudflare documented as evasion when Perplexity did it (generic Chrome-on-macOS UA, IPs outside the published range, rotating ASNs). **A candidate that requires touching someone else's property is out of scope.** It survives only in a consented form: a panel of sites that opt in and instrument themselves — which collapses C5 back into C1 with more customers.

**Pending doc:** none decides it. The boundary does.

### C6 — Vietnamese-language answer-visibility measurement

**Does:** C1 or C4, pointed at Vietnamese-language prompts and Vietnamese brands, in the team's own market.

**Support:** the geography constraint is the argument. `../../../../docs/method/scope.md`: HCMC confirmed, **no US market access**. Every rostered competitor's evidence is US/EU-English — Semrush's index is "126M US prompts, Jan–Apr 2026, 22 industries," company-stated and Semrush is itself a vendor. No vendor in the roster claims Vietnamese coverage.

**What kills it, and it is severe:** **no demand evidence exists.** Vietnamese AI-assistant usage share, Vietnamese brand willingness to pay, the size of the local SEO-agency market, whether Vietnamese-language prompts even route to the same retrieval pipelines — all `unknown — not pulled`. Absence of a competitor in a market nobody has sized is not a gap, it is an unexamined room. Second problem: a local SMB market is normally won by showing up, which is the field-sales motion the standing brief excludes.

**Pending doc:** P1 + P2 for the sampling half, identically to C1. P5 only if the product ever brokers placement rather than measuring; as pure measurement, Vietnam's advertising law is not the gate — **and stating that is itself a claim P5 could overturn**, since an unread statute may regulate comparative or brand-referencing commercial communications more broadly than the EU/US texts already read.

### C7 — OAI-AdsBot landing-page observability

**Does:** OAI-AdsBot is separately observable from every other pipeline — `raw/oai-adsbot.json`, `creationTime 2026-05-12T03:00:00`, **2 prefixes** (`130.131.229.128/25`, `20.168.90.128/25`, 256 addresses), against GPTBot's 21 and ChatGPT-User's 215. A Worker matching 256 addresses tells a ChatGPT advertiser: your landing page was fetched by OpenAI's ad-safety crawler at time T, and here is the exact byte-for-byte response it received.

**Support:** vendor-stated purpose, "to validate the safety of web pages submitted as ads on ChatGPT," data "not used to train generative AI foundation models" (`../../../../docs/findings/injection-feasibility.md`). Buyer volume: ChatGPT ads went live 2026-02-09 US free tier, self-serve Ads Manager 2026-05-05, UK/Mexico/Brazil/Japan/South Korea by 2026-08-11, "$1B annualized run rate in under 200 days" — company-stated, not filed (`../../../../docs/markets/ai-search-ads.md`).

**What kills it:** it is a feature, not a company; it is worthless to anyone not buying ChatGPT ads; and an advertiser whose page is rejected needs the *reason*, which OpenAI holds and this product does not.

**Pending doc:** P3, and it is the most interesting conditional in this file because **the same document breaks two candidates in opposite directions**. If OpenAI's Ads Terms impose a landing-page-consistency rule on advertisers — the standard ad-platform anti-cloaking clause — then C3a/C3b become a contract breach for any advertiser, *and* C7 becomes a compliance check with a named rule to check against, which is the strongest demand signal available to it. If P3 is silent on page consistency, C7 is a curiosity with no compliance hook and probably no buyer.

### C8 — Original research → paid audit engagements

**Does:** one technical founder instruments a real domain, publishes a reproducible study — every assistant fetch logged at the origin, the join to what the assistants then said, per-engine, with the raw data released. The collaborator writes and sells it. Revenue is engagements, not subscriptions.

**Support:** `../../../../docs/findings/cross-read.md` pattern 3 — "Consolidation cannot absorb a consultancy, and free tooling makes delivery cheaper rather than competing with it… the only one of the three that pays at n=1 customers — $8k–$50k per engagement for a two-person team, with $120–$200/hr senior rates as the floor." Pattern 5 — "a published finding buys reputation faster than a product does." And the same file's constraint scorecard is the only place in this research where the non-technical partner is scored **Strong**: "writing the report, running the relationship, the trust-building side of a security sale."

**Who pays:** the audit client. Same aggregator anchors as C1, plus the services rates above.

**What kills it:** it does not compound into an asset by itself; the research artifact ages; and the scorecard that scores services **Passes** scores them inside `ai-attack-defense`, not inside `ai-search-ads` — importing the verdict across ideas is a move wave 2b should attack.

**Pending doc:** P1 + P2 for the answer half only. **Breaks bad** and C8 still ships: a study of *what assistants fetch from an origin, how often, from which ranges, obeying which directives* needs no engine account at all and is legal under every document read. That asymmetry is C8's whole case.

## 3. The legal axis

| Bucket | Candidates | Deciding document |
|---|---|---|
| **Clearly permitted** | C2; C8's origin half; C1's crawl-log half | Public vendor JSON, public DNS, own infrastructure |
| **Permitted, reputationally hazardous** | C3b; C6 if framed as "make the AI praise you" | Google intent test survives; customer behaviour is the risk |
| **Prohibited by a policy already read** | C3a; **any** consumer-surface querying in C1/C4/C6 | Google spam policy 2026-08-28; UCPD Annex I item 11; OpenAI ToU 2026-01-01; Perplexity ToS s5.1/5.2(e)/5.2(i) |
| **Pending a document** | C1, C4, C6 answer halves (P1+P2); C3b on Bing (P4); C7 entirely (P3); C6's local exposure (P5) | see §0 |
| **Out of boundary** | C5 at scale | Project brief's hard rule, not a statute |

Two structural notes. First, enforcement on the prohibited items is judicial, not arbitral — both OpenAI and Perplexity carve unauthorized use and injunctive relief out of mandatory arbitration, OpenAI venued exclusively in San Francisco. A Vietnam-based two-person team is cheap to sue and expensive to defend. Second, Perplexity s5.2 restrictions apply "unless applicable laws or regulations prohibit these restrictions or **you have our written permission to do so**" — a documented route through, not a loophole, and one nobody has tried.

Also unresolved and not in any of the five: Cloudflare ships the Worker and the verified-bot machinery and says nothing about whether a customer may use them for differential serving on their own zone — `unknown — checked cloudflare.com 2026-09-17` (`../explore/edge-controls.md`).

## 4. Conditional map — what each pending document decides

| Doc | If restrictive | If permissive |
|---|---|---|
| **P1** OpenAI Business Terms | C1, C4, C6 lose the OpenAI half; C8 survives on origin data | C1's join becomes contractually clean |
| **P2** Perplexity API ToS | Same for Perplexity; C4 loses two of four engines | Perplexity stays sampleable via API |
| **P3** OpenAI Ads Terms | C3a/C3b become advertiser contract breach; **C7 gains a compliance hook** | C7 loses its demand hook and is a curiosity |
| **P4** Bing/Copilot policy | C3b is cloaking on Bing regardless of content equivalence | C3b permitted on every platform read |
| **P5** Vietnam ad law | C6 needs local disclosure/licensing review before selling | C6's gate is demand, not law |

**P1 and P2 together are the single highest-leverage unknown in this file.** They gate the answer-sampling half of three candidates and are the difference between the primary pick having a product and having a blog post.

## 5. Daydream — explicitly speculative

Everything in this section is speculation. No number below is sourced; none may be cited elsewhere.

**18 months out (≈ 2028-03), if the winning version won.** The instrumented domain stopped being one domain. Thirty or forty site owners run the same Worker and ship their crawl logs back, consented, and the thing that exists is a longitudinal record of what each assistant actually fetched, from which prefix, how often, and whether it honoured what the page told it. That record cannot be bought from Cloudflare, because Cloudflare sells each customer their own view and does not sell the cross-site join. It cannot be rebuilt quickly, because the value is in the elapsed time.

**What compounds.** Three things, in order of durability. (1) The time series — a competitor starting in 2028 gets a 2028 baseline and cannot manufacture 2026. (2) The published corpus — cross-read's Invariant/Mindgard pattern says a finding buys standing faster than a product does, and the standing is what makes the audit sellable without a sales team. (3) Detection drift as a moat nobody wants: the 215-prefix ChatGPT-User file regenerating hourly means whoever tracks it continuously accumulates knowledge of how ranges move, which is boring, unglamorous, and exactly the kind of thing funded competitors skip.

**What the second product is.** Not more measurement. The second product is the inverse: a conformance statement. Once the record exists, the sellable artifact is "this page served identical substance to humans and to assistants over this period, here is the log" — an anti-cloaking attestation, sold to the party that needs to prove it rather than the party that wants to evade it. That is C5's buyer reached legitimately, through consent instead of through third-party probing, and it is the only path found in this file that gets to the integrity buyer without breaking the boundary.

**The version where it fails, also speculative.** OpenAI ships origin-side analytics for advertisers, Cloudflare adds the cross-site view to AI Crawl Control for free, and the whole surface is a platform feature by mid-2027. The nine-month head start bought a portfolio, not a company.

## 6. The pick

**Primary: C8 executed on C1's instrumentation** — instrument one owned domain, publish the origin-side study, sell audits off it.

The case for, from evidence: it is the only shape whose core asset is legal under every document already read and stays legal whichever way P1 and P2 break. It needs a domain and a free Cloudflare tier — the cheapest start of any candidate, and `raw/local-infra-check.txt` says everything starts from zero regardless. Its revenue shape is the one `../../../../docs/findings/cross-read.md` scores as passing all five team constraints, and the only one in the entire research where the non-technical collaborator scores **Strong** rather than decorative. And the measurement it performs is the step the literature itself says is unsold: "Step 4 is what nobody sells."

The case against, as hard as it goes: `../../../../docs/findings/cross-read.md` scores `ai-search-ads` **Fails** on capital and **Fails** on field sales, and scores the services motion **Passes** inside a *different idea* — C8 borrows a verdict across ideas, which is a real methodological cheat. `../../../../docs/customers/answer-integrity-buyer.md` found **no price, in any channel, for a defense-specific line item**, one vendor selling anything in the shape (BrandShield, 2026-04-01, price undisclosed), and regulators moving away from mandating it (FTC Jul-2026; EU AI Act to 2027-12-02). A services business with no subscription does not compound and is capped at two people's hours. And the audit's most interesting half is the answer join, which two unread contracts may delete.

**Fallback: C6, Vietnamese-language answer-visibility measurement.** It is the only candidate that routes around both binding constraints at once — no US market access, and no capital to fight $131M+ of funded competition — and the team lives in the market. It is a fallback and not the primary for one reason: **its demand is entirely unsourced.** No Vietnamese usage figure, no local willingness-to-pay figure, no local agency-market size was pulled by any pass. Promoting it without those numbers would be exactly the guess this repo's rules forbid.

**The third reading, which the evidence also supports: no candidate clears the bar.** Three passes agree the answer-integrity gap is real; the same three passes failed to find anyone paying for it. Two well-funded adjacent industries have declined to enter, and `../../../../docs/findings/cross-read.md` already names the counter-reading — "a gap two well-funded adjacent industries have both declined to enter may be a gap with no budget behind it." That reading is not refuted by anything wave 1 measured. Wave 1 measured mechanism, not demand. **The verdict is the user's.**

## 7. What wave 2b must attack

Ranked by how much damage a successful attack does.

1. **"C8's origin half is legal whichever way P1/P2 break."** Load-bearing for the pick. Attack: does logging and publishing assistant-fetch data implicate any term not yet read — Cloudflare's own AUP, or a vendor crawler policy nobody looked at?
2. **"Nobody sells the AI-answer-integrity audit."** Three passes, but all three are search-level negatives, `../explore/who-sells-this.md` was an explicit spot-check, and WebSearch returned "unavailable" on 2026-09-17. One vendor found selling it would change the pick.
3. **Build estimates in §2.** Unsourced engineering judgment, every one. Nothing was built. The Workers free-tier request/CPU limits were never pulled — `unknown — not pulled` — and could make C1's logging tier infeasible for free.
4. **"Only a Worker can vary the body."** Read from documentation; no Worker was ever deployed. `../explore/edge-controls.md` admits the "Conditional response" example's script body was never retrieved.
5. **"IP-list matching is the only reliable detection for OpenAI/Anthropic/Perplexity."** Sample size is 2–3 IPs per engine (`raw/rdns-lookups.txt`), ASN via ip-api.com, "not a WHOIS-of-record" by that file's own caveat.
6. **"Content-equivalent variant serving is not cloaking."** My reading of Google's intent hinge. No enforcement action applying it either way was found, by any pass.
7. **"C5 is out of boundary."** I ruled a whole buyer segment out on the project's hard rule. If that reading is too strict, the file discards the one candidate with named, moving, funded adjacent buyers (DoubleVerify, HUMAN).
8. **C6's entire demand side.** `unknown — not pulled`: Vietnamese assistant usage, local willingness to pay, local agency market size, whether any rostered vendor already covers Vietnamese.
9. **"C7 is novel."** No check was run on whether DoubleVerify, IAS, HUMAN or any ad-verification vendor already observes OAI-AdsBot at advertiser origins.
10. **Importing cross-read's services verdict from `ai-attack-defense` into `ai-search-ads`.** Named as a cheat in §6; 2b should decide whether it survives.

## Caveats

- No candidate here was built, priced with a customer, or tested against a buyer. This is an idea file, not evidence of demand.
- `../explore/policy-ceiling-addendum.md` did not exist at write time. Every P1–P5 conditional is unresolved by construction; if the addendum contradicts §4's framing, §4 is wrong and the addendum wins.
- Build estimates, the "who pays" rows, and the §5 daydream are the only unsourced content in this file, and each is labelled at the point of use.
- Pricing anchors ($1,500–$5,000 audit, $8k–$50k engagement, +20–30% MRR) are aggregator-sourced in `../../../../docs/customers/answer-integrity-buyer.md`, not vendor-confirmed.
- ChatGPT ads "$1B annualized run rate" is company-stated, not filed. Profound's $6.8M 2025 revenue and Peec's "$4M+ ARR" are company-stated.
- The 2026-05-15 effective date for Google's AI-answer-manipulation wording remains `unknown — checked developers.google.com 2026-09-16`. The wording itself is confirmed on the page, `Last Updated: 2026-08-28`.
- Vietnam's advertising law, Bing/Copilot's cloaking policy, OpenAI's Ads and Business Terms, and Perplexity's API ToS have never been read by any pass. Five candidates' legality is stated conditionally for that reason and for no other.
