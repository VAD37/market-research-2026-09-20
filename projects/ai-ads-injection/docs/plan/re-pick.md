# Re-pick — wave 2a-bis

2026-09-17. Written after `../review/market-check.md` (wave 2b) killed wave 2a's pick on four lines. Inputs read in full: `../../CLAUDE.md` chain, `../../STATE.md`, `../review/market-check.md` (**binding**), `../plan/idea-set.md`, all seven `../explore/*.md`, and read-only `../../../../docs/{findings/injection-feasibility.md,findings/cross-read.md,customers/answer-integrity-buyer.md,competitors/ai-search-ads-roster.md,markets/ai-search-ads.md,markets/vietnam-sg-access.md,method/scope.md}`. Every load-bearing claim below was re-opened at its source this wave, not recalled.

One new pull: `../../raw/wave2abis-mor-seller-eligibility-vietnam.md` (direct `curl`, 2026-09-17). WebSearch exhausted 200/200; Chrome extension never connected; `web.archive.org` returned HTTP 429 to this wave.

---

## 1. Post-mortem — the method failure, named

Four compiled claims in this project were found this week to be unsupported by, or opposite to, their own cited sources. Three sat in `../plan/idea-set.md`; the fourth sat in `../explore/policy-ceiling-addendum.md`. They are four instances of one failure.

| # | The claim | The source actually said | File |
|---|---|---|---|
| 1 | Services "Passes all five constraints"; partner scores **Strong** | Those cells are the `ai-attack-defense` **column**; `ai-search-ads` reads "Fails / Fails / Content and GEO storytelling" | `cross-read.md` |
| 2 | Engagements price at $8k–$50k | That band prices security audits in `ai-attack-defense.md`; this market's anchor is $1,500–$5,000 | `answer-integrity-buyer.md` |
| 3 | "Step 4 is what nobody sells" proves unserved demand | Step 4 is defined as live-engine testing against perplexity.ai — prohibited by the same idea file's §1 | `injection-feasibility.md` |
| 4 | OpenAI's ad policies are "Silent" on differential serving | Same raw file carries "Ads must be consistent end-to-end" and "Destination integrity" | `raw/openai-ad-policies.txt` |

**The root cause, stated once: this repo binds a claim to a *file*, and provenance stops at the filename.** The global rule is "every compiled claim traces to a file in `docs/raw/`." All four claims traced to a file. None traced to the right *cell*, the right *subject*, or the right *definition* inside it. The rule as written cannot catch any of the four.

Failures 1 and 2 are the same move — a row read without its column, a price read without its market. Failure 3 is a conclusion phrase quoted without the source's own definition of the term inside it. Failure 4 is a negative finding ("Silent") asserted over a document already sitting in `raw/`, without stating what was searched.

### Proposed amendments to `../../../../docs/method/`

Written as rules a later agent can apply mechanically. Not written into `method/` — out of this wave's write scope.

1. **Cell-level citation.** A claim sourced to a table cites file + row label + column header + the cell text. A claim sourced to prose cites file + the quoted sentence. `See X.md` is not a citation. *(Catches 1, 2.)*
2. **Subject tag, and a fifth source kind.** Every price, verdict or scorecard row carries the market or idea it was measured in. Re-using it for a different subject is not a citation — it is an assumption, labelled `transplanted from <subject>` alongside the existing vendor-reported / analyst-derived / filed / company-stated kinds. *(Catches 2, and 1 again.)*
3. **Definitions travel with quotes.** If a quoted sentence uses a term the source defines elsewhere, the definition is quoted beside it or the quote is not used. *(Catches 3.)*
4. **Negatives carry a method line.** "Silent", "no clause found", "nobody sells" get the same treatment `unknown` already gets: name the file or channel, the strings searched, and the date. An absence asserted over a document already in `raw/` must name the strings searched in it. *(Catches 4.)*
5. **Load-bearing claims are re-opened, not remembered.** Before a pick is written, each claim the pick rests on is re-read at its source in the same pass, and the pick names which ones were re-opened. All four failures survived because the claim was carried forward from an earlier read. *(Catches all four.)*

Rule 5 is the cheap one and it is the one that would have worked alone.

---

## 2. Survivor audit

`never-tested` is not `alive`. Twelve-word cells.

| ID | Shape | Status | Reason, one line |
|---|---|---|---|
| C1 | Crawl-to-answer audit, origin-instrumented | **Dead as scoped; the join alive, unsold** | Origin half free twice over; only fetch→answer-text join survives, unpriced |
| C2 | Crawler-identity dataset + resolver | **Dead** | Known Agents Agent Identification API: 2,000+ agents, verified, $0 tier |
| C3a | Undisclosed differential serving | **Dead — out of scope, permanently** | Three prohibitions; Điều 23.2 disclosure surface does not exist |
| C3b | Content-equivalent machine variant | **Dead on value; untested on law** | Google: "no machine readable files, AI text files, or markup" needed |
| C4 | Brand-side answer monitoring | **Dead** | $131M+ funded field; cross-read scores capital Fails, field sales Fails |
| C5 | Cloaking detection, opposite side | **Dead — out of boundary, never revive** | Product requires systematic third-party fetching under a borrowed crawler identity |
| C6 | Vietnamese answer-visibility measurement | **Alive but changed** | Only sourced spend; competitors not customers; free incumbent tool exists |
| C7 | OAI-AdsBot landing-page observability | **Never-tested, and not testable here** | AdsBot fetches only submitted ad destinations; team cannot buy ChatGPT ads |
| C8 | Research → paid audit engagements | **Dead** | Borrowed verdict, borrowed rate card, inverted citation, no buyer anywhere |

Standing boundary note, restated so it is never quietly reversed: **live-engine transfer testing against a third-party product is barred by the engines' own terms** — OpenAI ToU effective 2026-01-01 bars programmatic extraction of Output; Perplexity ToS s5.2(i) bars it "or engage in any manual process to do the same". It is therefore not a product, not a demo, and not a research method this project may use. `injection-feasibility.md`'s "Step 4 is what nobody sells" describes that activity and is not a market opening.

---

## 3. C7 re-scored — P3 resolved, and it still does not produce a cheque

2b handed this forward because `../explore/policy-ceiling-addendum.md` Gap 3 marked OpenAI's ad policies "Silent" while its own raw file was not. The raw, re-read this wave (`../../raw/openai-ad-policies.txt`, page stamp **"Updated: August 10, 2026"**, Wayback snapshot archived 2026-08-18; `../../raw/openai-advertising-terms.txt`, "Updated: June 12, 2026"):

> "These standards apply to all ad assets, including copy, images or video, **and landing pages**. **Ads must be consistent end-to-end**: approved creatives may not link to destinations that introduce disallowed content."

> "**Destination integrity**: Ads must lead users to destinations that clearly relate to the advertiser and the offer being promoted. **Landing pages and destinations must accurately represent the advertiser, product, or service described in the ad** and may not mislead users through deceptive practices."

> "**Abuse of OpenAI Ads**: Advertisers may not defraud the OpenAI Ads platform or **attempt to circumvent our policies or enforcement processes**."

> Advertising Terms: "'**Destinations**' means the landing pages, mobile applications, and other destinations to which Ads direct users, including URLs, redirects, and waypoints." And: "4.5. Ad Review and Removal. OpenAI may review, reject, remove, or require modification of any Ad at any time, **for any or no reason**."

**The hook exists and resolved exactly the way 2a predicted would favour C7.** It changes less than 2a assumed, for four reasons — three of which are new here.

*One — the rule creates a duty, not an audit market.* Zero occurrences of `crawl`, `AdsBot` or `cloak` across the three ad documents (`wave2b-openai-ad-policies-destination-clauses.md`). The duty is written as an outcome obligation on the advertiser, enforced unilaterally by OpenAI under 4.5. Nothing in the text requires, contemplates or credits third-party evidence. A rule with no attestation requirement obliges nobody to buy proof.

*Two — the team cannot produce the measurement at all.* OAI-AdsBot's vendor-stated purpose is "to validate the safety of web pages **submitted as ads** on ChatGPT" (`injection-feasibility.md`, vendor-stated). It therefore does not visit a page that is not an ad destination. To observe one fetch on owned infrastructure, the founders must first buy a ChatGPT ad — which needs an advertiser account in a market OpenAI serves: US (2026-02-09), self-serve Ads Manager (2026-05-05), UK, Mexico, Brazil, Japan, South Korea (by 2026-08-11) per `ai-search-ads.md`. **Vietnam is not among them.** C7 is the one candidate this team cannot even prototype on its own domain. This is a harder blocker than any demand argument and it was not stated by any prior wave.

*Three — the detection primitive is free and the distribution belongs to someone else.* `../../raw/oai-adsbot.json`: 2 prefixes, `130.131.229.128/25` and `20.168.90.128/25`, 256 addresses, `creationTime 2026-05-12T03:00:00`. OpenAI publishes it; Known Agents identifies 2,000+ agents on a $0 tier. Matching 256 addresses is a lookup, not an asset. The scarce thing is a tag already running on advertisers' landing pages — which DoubleVerify and IAS have and this team does not.

*Four — the only segment with budget is the make-not-buy party.* `../../raw/ad-verification-oai-adsbot-check.md`: no ad-verification vendor watches OAI-AdsBot as of 2026-09-17, and OpenAI's ads lead David Dugan, Digiday 2026-06-30, on record: "I don't have any names to announce on that, but I think it's a natural step." Read the sentence as a buyer signal and it says the slot will be filled by a partner **OpenAI names**.

### Who writes the cheque

| Candidate buyer | Budget exists? | Reachable by this team? | Verdict |
|---|---|---|---|
| Advertiser | Yes — ChatGPT ads, $1B annualized run rate, company-stated | No. Ad markets exclude Vietnam; no US market access (`scope.md`) | Per-origin install, no self-serve route to them |
| Media agency | Unknown — never contacted, by any pass | Same market problem | `unknown — not tested`; interest is outcomes, not crawler telemetry |
| Verification vendor | Yes — DoubleVerify, IAS, HUMAN, named and funded | Enterprise sale, which cross-read scores **Fails on field sales** | They hold the tag; they need only a free CIDR list |

**Verdict: no cheque-writer identified, and C7 is unbuildable from Vietnam.** It is a feature of somebody else's tag, gated behind an advertiser account the founders cannot open. Its demand side has still never been tested — which is not the reason it is out, but it is why it may not be recorded as alive.

One thing C7 keeps, recorded because it is the only one of its kind in the set: it is the single candidate with a named, dated, currently-published rule (2026-08-10) that a measurement could be checked against, in a segment whose platform owner has publicly said the verification slot is unfilled. That is a real observation. It is not reachable from here.

---

## 4. C6 without illusions

What C6 has, all of it sourced: four published VND price lists (`vietnam-ai-visibility-demand.md` — SEODO từ 18tr / 200tr / 350tr; Fast Marketing 32–65tr/tháng; Midas từ 80tr/tháng, 12 months; TopOnSeek quote-only); a buyer in the founders' own city; a clean legal position (measurement is not *quảng cáo* under Điều 2.1; only Điều 23.3(a) tax registration attaches); and a payment rail.

The rail is now better evidenced than 2b could state. New pull, `../../raw/wave2abis-mor-seller-eligibility-vietnam.md`: Polar — "Polar uses Stripe Connect Express to issue payouts to residents or businesses in any of the countries below", list ends "🇺🇿 Uzbekistan 🇻🇳 Vietnam"; Lemon Squeezy — "can offer services to merchants and affiliates who can receive bank or PayPal payouts in one of the hundreds of countries we support", list ends "Uruguay Uzbekistan Vietnam". 2b's constraint 7 ("bill in VND or solve payments first") holds for **services** billing, where `vietnam-sg-access.md`'s finding is undisturbed; it does not hold for a **digital product**, which two MoR vendors document a Vietnam-resident seller can be paid out for. Neither was tested by onboarding — `unknown — not tested`. This removes a structural objection. It supplies no demand.

What C6 does not have: a buyer. Not one, in any channel, by any pass.

### What could a two-person team sell into that room

Checked against the room as it actually is: eight agencies selling GEO/AEO; three of three re-fetched give the audit away free; TopOnSeek already ships a free, unauthenticated, Vietnamese-language AI Visibility Checker with six pillars, competitor comparison, an industry leaderboard, scan history and a prospect-report generator (`wave2b-vn-agency-audit-and-free-tools.md`); and Google's own documentation says the inputs those agencies sell are unnecessary — "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"; "You don't need to create new machine readable files, AI text files, or markup" (`wave2b-google-ai-features-doc.md`).

Three candidate wedges, checked:

- **Origin-side crawler telemetry.** Dead. Free at Cloudflare ("Available on all plans", "Deploy with zero configuration") and at Known Agents ($0 tier, published Cloudflare Worker guide).
- **A better visibility checker.** Dead. The incumbent's is free, in Vietnamese, self-serve, and wired to its own sales team. Competing with free on features is `cross-read.md` pattern 2.
- **Falsification — telling a brand whether the 32–80 triệu/month it pays an agency changed anything an engine does.** This is the only wedge the incumbents' own incentives protect: no agency will build a tool aimed at its own invoice. It is aimed at the brand, not the agency, so it is not sold into the agency room at all.

Stated plainly, as asked. **There is exactly one thing, and it is encumbered on four sides.** (i) It needs the answer half, which is prohibited on consumer surfaces by documents already read and merely *ungoverned* — not permitted — on the API path. (ii) Its buyer is the mid-market brand already paying a retainer, reachable by the field-sales motion the standing brief excludes. (iii) Its honest output, given Google's own documentation, is most often "your other spend did nothing" — a one-time verdict, not a subscription, and the SKU three of three agencies give away free. (iv) Its natural distribution partner is the party it indicts.

So: the room does not want measurement. One buyer outside the room might — the brand paying for optimisation and unable to check it — and nobody has ever asked one.

---

## 5. Recommendation

**Build nothing. Stop as scoped — after one pre-registered demand probe that costs nothing and takes under a week.**

The probe is the closing procedure, not a new phase. Its purpose is to close the single load-bearing unknown 2b named and nobody has touched — whether any Vietnamese organisation will pay for measurement rather than optimisation — so the project closes on evidence rather than on inference, which is exactly what went wrong in §1.

**The case for stopping**, at full strength. Three research passes and four project waves have found no buyer for anything in this idea, in any channel, at any price. Every asset argument died against a free incumbent: origin telemetry (Cloudflare, Known Agents), the crawler-identity dataset (Agent Identification API), the cross-site longitudinal record (Agentic Web Index, free, current to 2026-09-16), detection drift (Web Bot Auth). The one market with sourced spend has eight suppliers giving the deliverable away and a platform owner denying the premise. The mechanism half that is genuinely unsold — fetch joined to answer text — is barred on consumer surfaces and merely unaddressed on the API path. And `cross-read.md` scores this market, in its own `ai-search-ads` column, "No capital: Fails. Competes with $131M" and "No field sales: Fails at enterprise tier".

**The case against stopping**, as hard as it goes. Nothing in four waves tested demand — every negative on file is a search-level or landing-page-level negative, and `answer-integrity-buyer.md`'s "no price found in any channel" is an absence of published prices, not an absence of transactions. Not one agency, brand or advertiser has been contacted by anyone. Closing on a stack of unpulled negatives is the same class of error as §1: a conclusion resting on what a file did not say. The infrastructure cost is ~$0/month plus a sub-$12 domain (`cloudflare-workers-limits-and-pricing.md`: free tier 100,000 req/day; Porkbun .com $11.08 flat), and the payment rail now has a documented Vietnam path for a product. There has never been a cheaper moment to ask a buyer directly, and the probe below costs less than the cost of being wrong.

**What would have to change to reopen it.** Any one of: (a) a named buyer paying for measurement rather than optimisation, anywhere; (b) a mandate that creates a duty someone must evidence — a third-party verification requirement on an AI ad surface, or the implementing decree under Điều 23.8 (`Chính phủ quy định chi tiết Điều này`, still unlocated); (c) written permission under Perplexity ToS s5.2, or an engine documenting that answer sampling is permitted on the API — which would make the fetch→answer join buildable and sellable rather than merely unsold.

---

## 6. The probe — pre-registered, fixed before it runs

Premise under test, single sentence: **some Vietnamese organisation will pay money for measurement of what AI engines do with its content.** If false, C6 is dead, and C1–C5, C7, C8 are already dead or unreachable, so the project closes.

**Sample.** 20 named organisations, list frozen in writing before the first message is sent: the 8 agencies named in `vietnam-ai-visibility-demand.md`, plus 12 Vietnamese brands drawn from those agencies' own published case-study pages. No substitutions after the list is frozen.

**Offer.** One deliverable, one price. A 10-working-day report on one named domain: which AI crawlers fetched it, how often, from which published ranges, and what four engines answer to twenty Vietnamese-language category prompts — origin log by Cloudflare Worker CIDR match, answer sampling **via paid API only** (consumer-surface querying is prohibited and is not part of the offer). Price **15.000.000 VND**, 50% deposit to start. 15tr sits just under SEODO's published entry tier (từ 18 triệu), so "too expensive" is not an available refusal.

**Channel.** Email plus Zalo or LinkedIn. One message each, one follow-up on day 3. No calls initiated, no discounting, no re-scoping of the offer mid-probe.

**Cost.** $0 infrastructure. Optional one-page offer site on a .com at $11.08 first year (Porkbun, vendor-reported, wave 1d). API sampling spend is incurred only after a deposit clears. Effort ≤5 working days.

**Decision rule — written now, not adjustable after.**

| Outcome, measured on day 7 after first contact | Rule |
|---|---|
| **PASS** | ≥2 of the 20 have paid a 7.500.000 VND deposit. Money received, not promised |
| **WEAK** | 0 deposits but ≥3 written replies naming a budget line and asking for a scheduled call |
| **FAIL** | Anything else |

PASS → wave 2c designs delivery for those buyers only. WEAK → exactly one 5-day extension, once, same offer, same price, then the same rule applies with no third extension. FAIL → the project closes and wave 2c writes `../outcome/` instead of a design. Deposits from personal contacts of either founder do not count toward PASS.

**What the probe cannot do, stated before it runs.** A null from cold outreach by an unknown two-person team is weak evidence on its own — cold B2B response rates are low regardless of true demand. A deposit is strong positive evidence; a FAIL is weak negative evidence. The reason FAIL closes the project is not the null alone: it is the null on top of three research passes and four waves that also found nobody. This asymmetry is the honest cost of running the probe, and it is recorded here so that no later wave can re-read a FAIL as inconclusive and reopen on that basis.

---

## 7. What wave 2c designs

**If the probe returns FAIL, there is nothing to design.** 2c writes `../outcome/` — what was measured, what killed it, the policy ceiling — and closes. No prototype, no architecture.

**If PASS**, 2c designs a delivery for the named deposit-payers and nothing more: one owned domain on a free Cloudflare zone; a Worker that CIDR-matches against the published range files on per-file refresh cadences and logs, with detection built as a swappable lookup, never as maintained knowledge; an API-only Vietnamese prompt sampler; and the report template. No cross-site index, no crawl-log tier as the asset, no audit price list, and **no differential-serving branch — that branch is not built, not merely left dark.** All eight of `../review/market-check.md` §9's constraints continue to bind.

---

## Caveats

- This file produces evidence and a recommendation. The go/no-go is the user's, per `../../../../CLAUDE.md`.
- The MoR finding is two vendors' own documentation, never tested by onboarding; both route payouts through Stripe Connect and therefore inherit Stripe-side KYC that neither page describes for a Vietnamese account. Paddle's seller-country position is still `unknown — checked paddle.com + developer.paddle.com direct fetch, 2026-09-17` (four URLs, three 404s).
- Whether ChatGPT Ads has become available in Vietnam since 2026-08-11 is `unknown — checked web.archive.org 2026-09-17, HTTP 429`. The market list used is `ai-search-ads.md`'s, itself press-sourced.
- OpenAI's ad-policy clauses come from a Wayback snapshot of a page stamped 2026-08-10; `openai.com` 403s every direct method across four passes. Live currency on 2026-09-17 is unconfirmed.
- "OAI-AdsBot visits only submitted ad destinations" is an inference from the vendor's stated purpose, not from a vendor sentence saying it visits nothing else, and no AdsBot fetch has ever been observed by this project. `unknown — not measured`.
- Five of the eight Vietnamese agencies have still not been re-fetched, and none has been contacted. Điều 15a and the Điều 23.8 implementing decree are still unread.
- The post-mortem is written from the four instances in this project's own files. The brief reports the same failure pattern in sibling projects; those files were not read this wave and nothing here is compiled from them.
- The probe's price, sample size and thresholds are engineering and commercial judgment, not sourced. They are recorded before the test precisely so they cannot be moved after it.
