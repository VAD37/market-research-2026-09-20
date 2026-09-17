# Market check — wave 2b, adversarial review of the pick

2026-09-17. Target: `../plan/idea-set.md`, which picks **candidate B** (single-job blind-spot agent: watch a competitor's pricing page, produce a dated fact, deliver a memo) with **candidate H** (cost-and-limit governor for unattended subscription runs) as fallback. Inputs: `../explore/` (6 files), `../../raw/` (12 files, 4 added by this wave), and read-only `../../../../docs/{markets,competitors,findings,customers,method}/`.

New evidence added by this wave: `../../raw/2b-sbi-pricing-report-firsthand-2026-09-17.md`, `../../raw/2b-price-tracker-longtail-2026-09-17.md`, `../../raw/2b-demand-evidence-2026-09-17.md`, `../../raw/2b-governor-already-solved-2026-09-17.md`, `../../raw/2b-allowance-architectural-risk-2026-09-17.md`.

## Verdicts

| # | Claim as 2a stated it | Verdict | One-line reason |
|---|---|---|---|
| 1a | SBI figures: $0-1m band ~54% competitor, ~20% value-based | **SURVIVES** | Re-read first-hand off p.11; figures accurate |
| 1b | n=760, resource-attributed by the source, small-business population | **WEAKENED** | Subgroup n≈82; attribution is the sub-agent's, not SBI's |
| 1c | The statistic supports watching a competitor's price for small SaaS | **KILLED** | Chart shows that cohort already over-uses competitor pricing |
| 2a | No cheap incumbent already watches competitor prices | **KILLED** | Four live sellers found, $19-39/mo, free tiers, 2026 |
| 2b | Absence of supply implies a gap | **WEAKENED** | Supply now exists; buyers still invisible for any of it |
| 3a | No candidate has direct demand evidence | **KILLED — for H only** | 828 dated issues, title-scoped, `anthropics/claude-code` |
| 3b | No direct demand evidence for candidate B | **SURVIVES** | Two weak signals, neither a B2B SaaS founder buying |
| 4 | Scoping to the recorded fact resolves the trust contradiction | **SURVIVES as a fork** | Both forks now lose: one untrusted, one already sold |
| 5 | H is a near-zero-cost fallback worth building | **WEAKENED** | Three of four functions already free; one survives |
| 6a | Unit economics unresolvable until the allowance is known | **KILLED** | Usage credits overflow at published API rates |
| 6b | The allowance is an architectural risk, not just a gap | **SURVIVES, hardened** | Anthropic rewrote then paused `claude -p` billing 2026-06-15 |

**Candidate B does not stand.** See §7.

---

## 1. The SBI pricing statistic

**Claim, 2a**: *"the only candidate whose problem has a size-stratified, dated, resource-attributed source — SBI 2024, n=760"*; the $0-1M ARR cohort runs competitor pricing ~54% and value-based ~20%, *"the source attributes the gap explicitly to research being 'time-consuming and expensive to implement properly'."* 2a flagged its own weaknesses: vendor conflict, chart read second-hand, B2B SaaS not 3-10-person SMB, and "too expensive" compatible with "not valued."

**Checked**: direct `curl` of the primary PDF, 2026-09-17 — HTTP 200, `application/pdf`, 255,857 bytes, 20 pages. Text layer via `pdftotext -layout`. Chart values are not in the text layer, so pp.5 and 11 were rasterised at 200 dpi and read visually by this agent. This replaces the relay chain in `../../raw/smallbiz-blind-spots-pulls.md`.

**Found**:

*The figures are accurate.* p.11, five bands, read off the bars: $0-1m 54/24/21 (competitor/cost-plus/value-based); $1-9m 42/34/24; $10-99m 42/29/29; $100-499m 33/33/33; $500m+ 28/26/45. "We spoke to 760 B2B SaaS leaders" is verbatim, p.4. The headline quote is verbatim, p.11 — with one sentence the relay dropped: *"Even companies as small as $1M ARR should be able to execute this without having to resource a giant in-house team."*

*The n is not 760.* p.5 data-labelled chart: the $0-1m band is **10.8% of respondents ≈ 82**. The two load-bearing percentages are a subgroup of ~82, and the file that carries them presents 760 as the finding's strength.

*The population is not small businesses.* p.4, verbatim: *"The primary B2B target buyer for these businesses is predominantly in the mid-market (50.7%) followed by enterprise (31.1%) and SMB (18.3%)."* 63% are sales-led or sales-assisted. The document never reports headcount and calls respondents "pricing leaders" and "pricing professionals" throughout. There is no methodology section: no fielding dates, no sampling frame, no margin of error.

*The resource attribution is the sub-agent's, not SBI's.* The quoted phrase is real but sits on p.12 inside *"Let's explore the pitfalls of value-based pricing. It can be time-consuming and expensive to implement properly"* — a general statement about the method, unstratified by size. The only size-attributed causal sentence in the document is about large firms having resources, not small firms lacking them.

*The vendor conflict is worse than 2a stated.* The report closes with *"Book yourself a free 30-minute consultation with our pricing experts"* and a **"Book a free pricing audit"** button (p.19). Data attribution is "Source: ProfitWell, By Paddle"; *"SBI acquired Price Intelligently from Paddle in November 2024"* (p.20).

**The finding that decides it**: the chart does not show the $0-1m cohort neglecting competitor pricing. It shows that cohort using competitor pricing **more than any other band**, and the report treats that as the error — p.11 pull-quote: *"The problem with competitive pricing is that you are putting a higher value on your competitors than your customers,"* and *"Mirroring them will likely end up in a 'blind leading the blind' phenomenon."* The under-used practice at $0-1m is value-based pricing (~21%), whose input is willingness-to-pay research on non-customers. Candidate B automates competitor price observation — the behaviour the source calls the mistake, for the cohort that already does it most. 2a's own illustration makes the inversion visible: an agent that dabs at *"you charge $29 because your competitor charges $29"* is mocking the decision candidate B exists to make easier.

Two figures in the same report also cut against "blind", though neither is broken out by band: p.7, *"Over 94% of pricing leaders update pricing and packaging at least once per year, with almost 40% updating as often as once per quarter"*, and *"Since September 2022, 98% of those surveyed have made updates to their pricing or packaging"* (chart: No updates 2%).

*Independent corroboration*: none found. Growth Unhinged, *2026 State of B2B SaaS and AI Monetization* (n=230 software companies, fielded April-May 2026, 22% under $1M ARR) reports no competitor-vs-value-based split. Monetizely's 103-company benchmark (2025-12-22) reports no such split either, and sells pricing consulting. `unknown — checked web search and direct fetch 2026-09-17`. Search-result summaries asserting "78% value-based in 2025" did not survive a direct fetch of the cited page.

**Verdict: 1a SURVIVES, 1b WEAKENED, 1c KILLED.** The numbers are real. What was built on them is not.

---

## 2. The price-tracker absence, hardened

**Claim, 1c** (`../explore/gap-pulls.md`): *"no vendor across 13 checked, in any of the 3 adjacent segments, sells 'a dated, interpreted pricing fact for a SaaS founder' as its product... Candidate B, scoped exactly as idea-set.md scopes it, is not directly served by any tool found."* Self-flagged as a targeted list, not an exhaustive scan.

**Checked**: GitHub search API, Product Hunt, AppSumo, IndieHackers, Y Combinator directory, general web, 2026-09-17 — then the four load-bearing vendors re-fetched first-hand by `curl`, all HTTP 200.

**Found**: the scan missed a live, priced, 2026-vintage cohort selling exactly the scoped product.

| Vendor | Verified | Price | Ships the scoped product? |
|---|---|---|---|
| JABB Watch | first-hand, HTTP 200 | €79 → **€39/mo** early bird | Yes — and more than scoped |
| RivalFlag | first-hand, HTTP 200 | free tier; $19/$39 (relay) | Yes, broader than pricing pages |
| Competiflow | first-hand, HTTP 200 | 100 free checks; $19-99 (relay) | Yes, pricing plus docs/changelog |
| PriceGhost | first-hand, HTTP 200 | free; $19/$39/$99 (relay) | **Pre-launch waitlist, not selling** |
| RivalWatch | relay only, site ECONNRESET | $29/mo (relay) | Claimed, unverified |
| Metrivant | relay only, HTTP 402 | unknown | Wrong buyer — PMM/CI teams |

JABB Watch is candidate B, shipped, verbatim: *"Weekly AI-written brief. What changed, why it matters to your deals, and what to do about it."* Twice-weekly scans of *"pricing pages, plan pages, or promo landing pages"*, severity scoring critical→low, a Friday email, and — decisively for §4 — *"Recommended actions: Each report includes concrete next steps: 'Consider matching within 2 weeks,' 'Monitor for 1 more cycle,' or 'No action needed.'"*

PriceGhost's founder story is 2a's own wedge argument, written by someone already building against it: *"I went looking for a tool. Kompyte, Klue, Crayon — they all start at $10,000 a year... There's literally nothing built for a solo founder watching five competitors. So I built PriceGhost."* It is not yet selling ("Pre-Launch Edition", waitlist, "breakeven is a single customer"), so it is a competitor arriving, not one arrived.

**On the framing question — gap, or market with no buyer?** The supply side no longer looks like a gap. Free tiers exist at $0 and paid entry at $19/mo, which removes candidate B's pricing power regardless of quality. And the demand side is invisible for the incumbents too: no user count, revenue figure or review volume was found for any of them (`unknown — checked vendor sites, Product Hunt, IndieHackers 2026-09-17`). The delegated leg also found at least nine Show HN launches of this same tool between 2020 and 2026 — pricemon.io, spydelta.com, parano.ai, pagedeltas.com, pingchange.com, competitortracker.io, rivalhunt.co, Brandchirps ×2 — essentially none of which drew upvotes or comments. Repeated independent supply with no visible pull is the signature of a market with no buyer, not of an unserved gap.

The graveyard search found no shutdown post in this niche and no archived repo — but Reddit failed (§3), so that negative is weak. The only verifiable shutdown is PoachIt, consumer price tracking, TechCrunch 2015-05-18: wrong vertical, eleven years stale.

**Verdict: 2a KILLED. 2b WEAKENED** — the distinction the brief said would decide the project now leans to "no buyer."

---

## 3. Demand, directly

**Claim, 2a**: *"No candidate in this set has direct demand evidence. Every argument above rests on either an absence of supply or a practice gap. Neither is a customer saying they would pay."*

**Checked**: HN Algolia API, GitHub issue search, Upwork, Freelancer, Fiverr, IndieHackers, agency service pages, 2026-09-17. Volume claims re-verified first-hand with the authenticated `gh` CLI.

**Found — candidate H, verified by me**: `gh api search/issues` on `anthropics/claude-code`, title-scoped, 2026-09-17: **`"usage limit" in:title` = 828**; `"rate limit"` 733; `"cost"` 355; `"weekly limit"` 234; `"budget"` 153. Eight `"usage limit"` issues filed in the four days to 2026-09-16, including #94424, *"Function hooks: an event when session usage or a rate-limit window changes, so trackers do not…"* — a request for the primitive H would consume, whose wording presupposes trackers already exist. A control query (`competitor pricing`, full-text, same repo) returns 42, so GitHub's looser full-text counts are directional only; the title-scoped numbers are the defensible ones. `ccusage/ccusage` 18,591 stars, pushed 2026-09-17.

Relayed verbatim issue text, dated, not re-fetched by me: *"the orchestrating model has no budget awareness... burned ~70% of a weekly Fable 5.1 allowance"* (#94770, 2026-09-16); *"One subagent, resumed 8 times, accounted for 50.7% of that week's entire consumption"* (#91220, 2026-09-01); *"We need strict credit caps and auto-stop safeguards for subagent workflows"* (#92800, 2026-09-08); *"The weekly limit ran out on work I did not ask for... My development stopped"* (#93911, 2026-09-12).

**Found — candidate B**: two weak signals, neither a B2B SaaS founder buying. A Freelancer.com job, posted before ~2025-09, *"Monitor pricing trends and alert us when competitors change their pricing"* at **$2-8 AUD/hour** — buyer is a wine e-commerce retailer. An IndieHackers post, 2026-05-24, *"Every Monday I'd open like 5 tabs... Takes 2-3 hours. And I still miss stuff"* — whose author adds *"Haven't written a single line of code yet. Wanted to talk to real people first,"* i.e. a would-be seller, not a buyer. Its one reply, 2026-05-26: *"yeah this is real, but for me the bigger pain isn't the checking, it's that 90% of the changes don't matter."*

Two "Ask HN" threads that read as demand are vendor fishing, and both drew **0 comments**: id=47661051 (2026-04-06, body is a Peerscope pitch at $29/month) and id=46865447 (2026-02-03, *"Wondering if this is a real pain point or just something people complain about but don't actually prioritize"*).

**The channel that failed**: Reddit was unreachable for both shapes — WebFetch refuses the domain, `curl` on `old.reddit.com/search.json` returns a bot-gated shell, `site:reddit.com` queries surface no reddit.com URL. This is the **third** independent pass in this repo to fail there; `../../../../docs/findings/market-gaps-2026.md` and `../../../../docs/customers/first-customers.md` both record the same wall. r/SaaS and r/microsaas are exactly where B's persona posts, so B's negative is weak-on-an-incomplete-search rather than clean. H's persona is native to GitHub, which was reached at full volume, so H's positive does not depend on Reddit.

**Verdict: 3a KILLED for H — 2a's "no candidate" is now false. 3b SURVIVES for B.** The asymmetry is the finding: the fallback has the demand evidence and the pick does not.

---

## 4. The trust contradiction 2a left in deliberately

**Claim, 2a**: candidate B is picked *"scoped to the recorded fact and explicitly NOT the repricing recommendation — the recommendation version violates the brief's own sub-question-3 trust line."* And, stated against itself: *"the version that is defensible is also the version that is least differentiated from a generic page-change watcher."*

**Checked**: `../../CLAUDE.md` sub-question 3 against the vendor copy fetched in §2, 2026-09-17.

**Found**: the fork is real, and the evidence closes both branches.

The brief's line is: *"do NOT trust agent-authored dashboards and charts by default. DO trust agent execution of small bounded tasks — research a person, record a fact, watch a trend, run a recurring chore."* A repricing recommendation is agent-authored judgement about the operator's business. It sits on the untrusted side. 2a's adjudication of that is correct and is not disturbed.

What is new is what each branch costs:

- **Recommendation branch** — differentiated, and violates the brief's own rule. Also already occupied: JABB Watch ships *"Recommended action: Consider holding your current price and updating marketing to emphasize cost advantage"* at €39/mo, and RivalFlag ships *"Tighter packaging signals confidence in retention. Expect a new objection set from cost-sensitive buyers"* with a free tier.
- **Recorded-fact branch** — trustworthy, and it is a page diff with a timestamp. Wave 1c already priced that commodity: Visualping and ChangeTower ship AI-summarised diffs at $12-35/mo, and the 2026 cohort ships it free.

There is no third position where the product is both trustworthy under the brief's rule and differentiated, because the only differentiator anyone in this category sells **is** the interpretation. The thing that would carry the trusted branch — provenance and a staleness clock, which is candidate F — is a property of the record, not a reason to buy the record.

**Verdict: SURVIVES as a genuine fork, and the fork is now a dead end in both directions.** This is not a choice to hand the user between two live options; it is a second, independent reason candidate B fails.

---

## 5. The fallback, H

**Claim, 2a**: H is *"the smallest candidate and the only one the team needs regardless"* — watches the window, defers work before the wall, kills runaway spend, attributes cost per task; 3-7 days; near-zero expected cost; kill condition *"Anthropic ships adjacent to it every release."*

**Checked**: primary Anthropic docs, GitHub search API, raw READMEs, PyPI, npm, Grafana Labs, two commercial vendors, 2026-09-17. Repo stats and the CLI flag re-verified first-hand.

**Found**: three of the four functions are already free.

| Function | Status |
|---|---|
| (a) watch window, report headroom | **Solved, free** — `/usage` built in; Claude-Code-Usage-Monitor 8,707★ |
| (b) defer or queue work *before* the wall | **Open** — best free tool is claude-session-budget, **8★** |
| (c) kill runaway spend / budget cap | **Solved, built in** — `--max-budget-usd` |
| (d) per-task cost and duration attribution | **Solved, free** — `/usage` Attribution, OTel, Grafana #25255 |

(c) is a shipped CLI flag, verbatim from https://code.claude.com/docs/en/cli-reference fetched 2026-09-17: *"`--max-budget-usd` — Maximum dollar amount to spend on API calls before stopping (print mode only). Spend from subagents counts toward the cap. Once spend reaches the cap, spawning another subagent fails with `Budget limit reached`, and Claude Code stops background subagents that are still running; the cap-enforcement behaviors require Claude Code v2.1.217 or later."* Example given: `claude -p --max-budget-usd 5.00 "query"`. Print mode is precisely H's target mode.

Repo stats verified by me via `gh api`, 2026-09-17: ccusage/ccusage 18,591★ pushed same day; Maciek-roboblog/Claude-Code-Usage-Monitor 8,707★, MIT, pushed 2026-07-05; howincodes/claude-code-limiter 53★; Star001-KR/claude-session-budget 8★; outbit/claude-code-tokenbudget 2★. `autoContinueAtUsageLimit` — *"Wait in the open session and continue the task automatically after a claude.ai usage limit resets"* — resumes after the wall; it does not defer before it.

So H reduces to (b): pre-emptive deferral and queueing, where the only free implementation has 8 stars and the platform has repeatedly closed the request (#33323, 2026-03-11, citing #535 *"The ability to queue up messages"*, 27+ upvotes, auto-closed by a stale bot). That is a real hole with dated demand behind it (§3). It is also a much smaller product than 2a's four-function description.

Two corrections fall out of this check:

- **CrewTower's $9.99 was not re-confirmed.** `../plan/idea-set.md` and `../explore/control-planes.md` both cite it as H's price ceiling. The vendor page was fetched 2026-09-17 and the figure not found. `unknown — checked crewtower.app 2026-09-17`. The nearest verified comparable is SessionWatcher at $6.99-$59 one-time — still a one-time, sub-$60 ceiling, so the conclusion holds while the evidence for it does not.
- **`Stop`/`SubagentStop` cost fields are now contested.** This wave's docs read found no cost or duration field documented on either hook's input JSON, against `../explore/task-telemetry.md` and `idea-set.md` fact 1. Two reads of the same page disagree and neither wave measured it live. `unresolved — checked code.claude.com/docs/en/hooks 2026-09-17`. This is 2a's own attack item #5, still open and now actively contested; it is load-bearing for C, F and H's function (d).

**Verdict: WEAKENED. H survives, narrowed to one function.** The fallback is not gone, but it is one feature, not a product, and its price ceiling is a one-time sub-$60 purchase.

---

## 6. The subscription-allowance hole

**Claim, 2a**: *"Per-customer compute cost is unresolvable until claim #8 is closed"*; the allowance size is `unknown — no primary-doc figure found`.

**Checked**: anthropic.com/legal/consumer-terms and four support.claude.com articles, direct fetch, 2026-09-17.

**Found — the economics are boundable after all.** Usage credits exist, verbatim from https://support.claude.com/en/articles/12429409: *"Usage credits allow individuals subscribed to paid Claude plans (Pro, Max 5x, and Max 20x) to continue using Claude seamlessly after reaching their included usage limits. Instead of being blocked when you hit your session limits, you can switch to consumption-based pricing at standard API rates."* Daily redemption limit $2,000; monthly spending cap and auto-reload are configurable; credits apply to Claude Code terminal usage. So marginal COGS above the allowance is **API list price, which is published**. A plan can be costed at API rates and treat the subscription allowance as a discount of unknown size rather than as the basis. That kills 2a's "unresolvable" — and simultaneously kills the daydream's cost-floor moat, since any competitor can buy the same marginal token at the same published rate.

**Found — the architectural risk is real and already materialised.** From https://support.claude.com/en/articles/15036540, article dated 2026-06-16, verbatim: *"**Update June 15:** We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits. The previously announced monthly credit... isn't available. We're working to update the plan to better support how users build with Claude subscriptions. When we have an update, we'll share it before anything takes effect."* The withdrawn plan would have removed `claude -p` from subscription limits entirely and replaced it with a per-plan monthly credit ($20 Pro / $100 Max 5x / $200 Max 20x).

The billing model for the exact substrate every output-shipping candidate runs on was rewritten, published, scheduled for 2026-06-15, and withdrawn the day before — and another revision is promised. That is the risk, dated, not hypothesised.

Two contract clauses set the outer bound, from anthropic.com/legal/consumer-terms, effective 2025-10-08:

> *"We may sometimes add or remove features, **increase or decrease capacity limits**, offer new Services, or stop offering certain Services... we reserve the right to modify, suspend, or discontinue the Services or your access to the Services, in whole or in part, **at any time without notice to you**."*

> *"Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through **automated or non-human means, whether through a bot, script, or otherwise**."*

The second bears directly on 2a's attack item #1, which this wave was not asked to close and does not close. Note only that the withdrawn June plan explicitly contemplated *"Third-party apps that authenticate with your Claude subscription through the Agent SDK"* as a supported, credited category — which cuts against the strictest reading of the quickstart line 2a's constraint 3 rests on, but was withdrawn, so establishes nothing in force. `unresolved — checked support.claude.com and anthropic.com/legal 2026-09-17`.

Still unpublished, confirmed a third time: no absolute 2026-09 token, message or hour figure for either window. `support.claude.com/en/articles/8324991-about-claude-s-max-plan-usage` now returns **HTTP 404**. Current pages give only relative multipliers (Max 5x = "five times more usage per session than the Pro plan").

**Verdict: 6a KILLED — the economics are plannable at API rates. 6b SURVIVES, hardened.** The answer to "is a product whose COGS is an unpublished allowance investable": yes, if it is priced against the published API rate and the allowance is treated as a revocable discount. No, if the plan requires the allowance to hold.

---

## Reconciling wave 1c's flagged contradiction

1c flagged one contradiction for this wave, on the payment rail. Both statements, side by side:

| Source | Statement |
|---|---|
| `../plan/idea-set.md`, caveats + attack item #7 | *"A Vietnam-based pair can collect recurring USD from foreign buyers — `unknown — not pulled`. Stripe/Paddle/Hyperwallet eligibility unchecked."* Paddle's Vietnam seller eligibility "stated neither way." |
| `../explore/gap-pulls.md`, gap 3 + `../../raw/gap3-vietnam-payment-rails-2026-09-17.md` | Paddle: Vietnam absent from its 28-country exclusion list — supported by omission. **Lemon Squeezy names Vietnam explicitly** in its bank-payout country list. Payoneer already confirmed working. Wise Business unresolved (own eligibility page 404'd). |

**The evidence supports 1c.** 1c fetched vendor pages directly; 2a pulled nothing and recorded the honest `unknown`. 1c's is a first-hand fetch of a named exclusion list plus a first-hand fetch of a named inclusion list, and the inclusion list is the stronger form. `idea-set.md`'s caveat is stale as of 2026-09-17, not wrong as of when it was written.

Two qualifications 2c must carry: Paddle's is supported-by-omission, which is weaker than a named yes and can change without notice; Wise Business remains genuinely unresolved, `unknown — wise.com eligibility page 404'd, checked 2026-09-17`.

**Effect on the pick: none.** The payment rail was never what decided candidate B, and resolving it favourably does not offset §§1-4. A working rail makes it easier to sell a product the evidence says has no buyer.

---

## 7. Does candidate B stand?

**No. Candidate B is killed.** Three independent lines, any one of which would weaken it and which together do not leave a product:

1. Its only quantitative support points the other way. The $0-1m cohort at 54% competitor pricing is the highest of any band, and the source calls that the error to be corrected (§1).
2. At least four vendors sell the scoped product as of 2026-09-17, entry at $19-39/mo with free tiers, one of them shipping the memo-with-recommendations verbatim (§2).
3. No demand evidence, on an incomplete search (§3b) — and the trust fork is closed at both ends (§4).

**H is the candidate the evidence now favours**, on §3's asymmetry: 828 dated, title-scoped issues on the vendor's own tracker is the only direct demand signal this project has found for anything. That recommendation comes with its own damage: H is now one function, not four (§5), its verified price comparable is a one-time sub-$60 purchase, and it sells into a population that overwhelmingly builds rather than buys — five independent free tools already exist for the parts that are solved.

Stated plainly: the evidence favours H **relative to B**, not absolutely. Nothing in this review establishes that H is a business. The verdict is the user's; this file produces the evidence.

No new candidate is proposed here. **C** (recurrence-to-tool graduation) is untouched by this review and remains 2a's watch-not-start, still contingent on hands-on Braintrust Patterns — but its function (d) dependency is now contested (§5), which is new information against it.

---

## 8. What wave 2c must design around

Constraints, not a design.

1. **Do not design a competitor-price watcher.** §§1-4. If any part of the concept is reused, it is the *record* — dated fact, source artifact, staleness clock — never the watching of a price.
2. **Design for H's function (b) only**, pre-emptive deferral and queueing before the window wall. (a), (c) and (d) are free: `/usage`, `--max-budget-usd`, OTel + Grafana #25255, ccusage at 18,591★. Anything rebuilding those is rebuilt-not-built.
3. **Measure the hook payload before depending on it.** Whether `Stop`/`SubagentStop` carry `cost` and `duration_ms` is now contested between two docs reads of the same page. `projects/CLAUDE.md`: measured beats argued. One live `claude -p` run, payload diffed, output in `raw/`. This gates C, F and H(d).
4. **Price against published API rates, not the allowance.** Usage credits overflow at standard API rates with a configurable monthly cap. Treat the subscription allowance as a revocable discount of unknown size, never as the basis of a margin.
5. **Assume the `claude -p` billing model changes again.** It was rewritten, scheduled and withdrawn on 2026-06-15, with another revision promised. Any design must survive the allowance going to zero for non-interactive use. Keep the compute path swappable to an API key from day one.
6. **The contract is the outer bound.** "Increase or decrease capacity limits... at any time without notice", and automated access permitted only via API key "or where we otherwise explicitly permit it". Item #1 on 2a's attack list is still open and this wave did not close it.
7. **Stop treating Reddit as pullable.** Three passes have failed on it. Either route through Discourse-based forums — `../../../../docs/findings/market-gaps-2026.md` documents `/search.json` working on OpenAI's and Cursor's forums — or drop the channel and stop discounting negatives for its absence.
8. **Re-verify any relayed claim before building on it.** Every finding above that changed a verdict came from re-fetching something a prior wave had taken at one remove. 1c's 13-vendor scan missed four live sellers; the SBI mechanism was a sub-agent's synthesis presented as a source quote.

## Caveats

- §2's tier prices for PriceGhost, RivalFlag and Competiflow are relay; only JABB Watch's €39 and the four HTTP 200s are first-hand. RivalWatch and Metrivant are relay-only and their sites were unreachable.
- §1's chart values are this agent's visual reading of an unlabelled bar chart at 200 dpi. They match the relay's independent reading, which is corroboration between two readers of the same unlabelled chart, not a published data table.
- The ≈82 subgroup n is this agent's arithmetic (10.8% × 760), not a published figure.
- §5's function matrix outside `--max-budget-usd` and the five `gh`-verified repo rows is relay from a delegated leg; commercial "no budget cap" findings are absence of a marketing claim, not a tested absence.
- §3's issue counts are GitHub search `total_count`, which counts issues matching a title substring, not curated requests. A control query returns 42 on an unrelated phrase, so treat them as volume, not as 828 distinct asks.
- Reddit was unreachable for every question in this review. Candidate B's demand negative and §2's graveyard negative are both weaker for it.
- No go/no-go is issued. Per `../../../../CLAUDE.md`, the verdict is the user's.
