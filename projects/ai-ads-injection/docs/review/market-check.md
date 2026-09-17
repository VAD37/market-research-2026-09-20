# Market check — wave 2b adversarial review of the pick

2026-09-17. Target: `../plan/idea-set.md` (wave 2a) — primary pick **C8 executed on C1's instrumentation**, fallback **C6**. Binding inputs read first: `../explore/policy-ceiling-addendum.md` (1b), `../explore/cost-and-demand-pulls.md` (1d), the five wave-1 explore docs, `STATE.md` in full, and read-only `../../../../docs/{findings/cross-read.md,findings/injection-feasibility.md,customers/answer-integrity-buyer.md,markets/ai-attack-defense.md,markets/vietnam-sg-access.md,method/scope.md}`.

**Method note.** WebSearch was exhausted (200/200) before this wave started; the Chrome extension has never connected this session. Every new pull is direct `curl -L` with a desktop Chrome UA, saved verbatim to `../../raw/`. New raw this wave: `wave2b-crawler-analytics-competitors.md`, `wave2b-vn-agency-audit-and-free-tools.md`, `wave2b-detection-shelf-life.md`, `wave2b-google-ai-features-doc.md`, `wave2b-vn-law-duty-bearers.md`, `wave2b-openai-ad-policies-destination-clauses.md`. No file in `../plan/` or `../explore/` was edited.

## Verdicts

| Claim, as 2a or its sources stated it | Verdict | Reason |
|---|---|---|
| C8 inherits cross-read's services verdict | **KILLED** | Same file scores this market SaaS-shaped, failing capital and sales |
| $8k–$50k engagement band applies here | **KILLED** | That band prices security audits; this market's audit anchor is $1,500–$5,000 |
| "Step 4 is what nobody sells" supports the pick | **KILLED** | Step 4 is live-engine testing, which 2a's own §1 calls prohibited |
| C8 has a buyer at a knowable price | **KILLED** | No audit price found; three of three agencies give audits away |
| C6's demand is "entirely unsourced" | **KILLED** | Eight agencies, four published VND price lists (wave 1d) |
| The eight agencies validate C6's demand | **WEAKENED** | Agency supply, not brand willingness to pay |
| No Vietnamese vendor covers this ground | **KILLED** | TopOnSeek ships a free Vietnamese AI-visibility checker today |
| C3a is out on evidence, not caution | **SURVIVES** | Vietnamese law adds a third prohibition, binding at home |
| A disclosure could make AI placement compliant | **KILLED** | Điều 23.2(a)/(b) need surfaces the founders never control |
| P5 does not gate C6 as pure measurement | **SURVIVES** | Measurement is not "quảng cáo"; only tax registration attaches |
| C1's origin instrumentation is the asset | **KILLED** | Cloudflare free zero-config; Known Agents free tier, 5,000+ sites |
| C2 is a distribution asset worth building | **KILLED** | Known Agents sells it, maintains 2,000+ agents, free tier |
| The cross-site join cannot be bought (§5 daydream) | **KILLED** | Agentic Web Index publishes it free, data through 2026-09-16 |
| The fetch→answer join is still unsold | **SURVIVES** | Narrowly; citation and referral tracking are adjacent and free |
| IP-list matching is the only reliable method | **WEAKENED** | True today; Web Bot Auth shipped at Cloudflare, IETF draft live |
| Detection drift is a moat nobody wants (§5) | **KILLED** | Signatures make detection cheaper for everyone, including entrants |
| P3 unresolved, so C7 has no compliance hook | **KILLED** | Ad policies dated 2026-08-10 carry destination-integrity clauses |
| GEO optimisation is what gets you into AI answers | **WEAKENED** | Google's own doc: no special files, markup or optimisation needed |

---

## 1. The borrowed verdict — does the services argument transfer?

**2a's claim** (`../plan/idea-set.md` §6): "Its revenue shape is the one `cross-read.md` scores as passing all five team constraints, and the only one in the entire research where the non-technical collaborator scores **Strong**." §2 concedes the import is "a real methodological cheat" and hands the adjudication here.

**Checked**: `../../../../docs/findings/cross-read.md` and `../../../../docs/markets/ai-attack-defense.md`, read 2026-09-17.

**Found.** The transfer fails on the source file's own rows, three ways.

*One — the source file scores this market the opposite way, in the same table.* `cross-read.md`'s side-by-side gives `ai-search-ads` **"Revenue shape: Recurring SaaS, needs scale"** and `ai-attack-defense` **"Per-engagement, works at n=1."** The constraint scorecard below it gives `ai-search-ads` **"No capital: Fails. Competes with $131M"** and **"No field sales: Fails at enterprise tier"**, and gives the partner row **"Content and GEO storytelling"** — not "Strong." Every "Passes" 2a imports sits in the `ai-attack-defense` column, and each carries an idea-specific reason: "Passes for services" is qualified by "Consolidation risk: nil for services," and "Weeks. Tooling is free and public" refers to Garak, PyRIT, DeepTeam and Promptfoo — security red-team tooling, not anything in this project.

*Two — the price band does not survive the move.* The $8k–$50k figure traces to `ai-attack-defense.md`'s services table: one-time audit **$8k–$25k**, single-agent red team **$16k–$50k**, senior specialist **$120–$200/hr** (vendor and aggregator-stated). The only audit anchor that exists for *this* market is `answer-integrity-buyer.md`'s **one-time GEO audit $1,500–$5,000** (aggregator). The imported floor is 5x the target market's ceiling. Same shape, different order of magnitude. Conflicting figures, side by side, not averaged — and the pick's economics were argued from the wrong one.

*Three — the pick's demand citation points away from the pick.* 2a's C1 support section, carried into §6, cites `injection-feasibility.md`: **"Step 4 is what nobody sells."** In the source, Step 4 is defined verbatim as *"Test transfer from lab harness to a live production engine. Pfrommer's target was named: perplexity.ai's Sonar Large Online."* That is answer-side querying of a live consumer engine — the exact activity `../plan/idea-set.md` §1 establishes is **prohibited** by OpenAI's ToU (effective 2026-01-01) and Perplexity's ToS s5.2(i), which bars automated collection "or engage in any manual process to do the same." The one sentence offered as proof of an unserved market describes an unserved market partly *because* the engines' terms bar serving it commercially — and it describes the detachable half of the pick, not the origin half 2a says survives whichever way P1/P2 break.

**Verdict: KILLED.** The services conclusion does not transfer. It was scored on a different market, priced from a different rate card, and the one market-specific citation supporting it describes prohibited activity.

---

## 2. C8's buyer, concretely — has anyone bought an AI-answer audit?

**2a's claim** (§2, C8): revenue is "engagements, not subscriptions," priced off "the same aggregator anchors as C1, plus the services rates above."

**Checked**, 2026-09-17: `midas.vn/dich-vu-geo/`, `seodo.vn/dich-vu-geo/`, `toponseek.com/dich-vu-aeo/` and `toponseek.com/ai-visibility-check/` (all HTTP 200, direct fetch); `tryprofound.com/products/agent-analytics` (HTTP 404); plus `answer-integrity-buyer.md` and `who-sells-this.md` re-read. Raw: `../../raw/wave2b-vn-agency-audit-and-free-tools.md`.

**Found.** No buyer of an AI-answer audit was identified in any channel, at any price. What was found instead is a consistent pattern: **the audit is the lead magnet, the retainer is the product.**

| Vendor | Retainer, published | Audit price | Verbatim |
|---|---|---|---|
| TopOnSeek | none, quote-only | **free** | "Chấm điểm AI Visibility trên 6 trụ tín hiệu GEO — miễn phí, chỉ 15 giây" |
| Midas | từ 80 triệu/tháng, 12 months | **free** | "sau buổi khảo sát miễn phí" |
| SEODO | từ 18 triệu / từ 25 triệu / 200tr / 350tr | **free** | "tư vấn 1-1 miễn phí và một bản kế hoạch SEO AIO sơ bộ" |

Three of three agencies checked give the audit away; zero publish a price for one as a standalone deliverable. This sits on top of `answer-integrity-buyer.md`'s own finding, unrevised since 2026-09-16: **"No price found anywhere, in any channel, for a defense-specific line item."** The $1,500–$5,000 anchor that does exist is aggregator-sourced and is for a *visibility* audit, which is the thing the three agencies above hand out free.

Second problem, structural rather than commercial: `../../../../docs/markets/vietnam-sg-access.md` records that the merchant-of-record route — the only payment path with no residency requirement — **"does not work for services billing,"** and that Stripe does not support Vietnam. An engagement business billing non-Vietnamese clients has an unsolved collection problem. Billing Vietnamese clients in VND does not.

**Verdict: KILLED.** C8 as written is a consulting practice with no proven rate card. Saying it plainly, as instructed: nobody has been found to have bought an AI-answer audit, from anyone, at any price, in three research passes and this review.

---

## 3. C6 versus the eight Vietnamese agencies — validation or occupied market?

**2a's claim** (§6): C6's "demand is entirely unsourced." **1d's evidence**: eight agencies sell branded GEO/AEO with four published VND price lists.

**Checked**, 2026-09-17: re-fetch of three of the eight agency pages plus TopOnSeek's tool page (raw above); `../../../../docs/markets/vietnam-sg-access.md`; Google's own `developers.google.com/search/docs/appearance/ai-features` (raw: `../../raw/wave2b-google-ai-features-doc.md`).

**Found.** Three distinct things, pulling in different directions.

*The market is occupied, and by more than a service.* TopOnSeek already ships a free, unauthenticated, Vietnamese-language **AI Visibility Checker** — six GEO pillars, competitor comparison, an industry leaderboard, a saved scan history, and a prospect-report generator wired to its own sales team (`tos_aiv_sales_generate`). That is the tool a two-person team would build for C6, built, in the language, by a staffed HCMC incumbent, given away. "No vendor in the roster claims Vietnamese coverage" was a statement about an English-language roster; it was never a statement about Vietnam.

*But the tool is thin, and the claims around it are weak.* TOS's six pillars — robots.txt, llms.txt, structured data, content, E-E-A-T, technical — are **static-signal checks**, not measured engine behaviour. Nothing in them observes a fetch or reads an answer. And two of the incumbents' central claims are contradicted by the platform owner. Google's own documentation, pulled today: *"There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"* and *"You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add."* Midas's page claims Search Console now has a "báo cáo Generative AI Performance" with dedicated AI Overview filters; Google's page says AI features *"are included in the overall search traffic in Search Console. In particular, they're reported on in the Performance report, within the 'Web' search type."* Both statements are on file, attributed, unreconciled.

*What a two-person team sells that a staffed agency does not.* On this evidence: measurement instead of assertion. Every agency promise checked is a claim about a *cause* — entity building, schema, llms.txt — sold against an outcome ("Cam kết xuất hiện Chat GPT & AI Overview") that none of them measures at the origin, and that the platform owner says needs none of those inputs. SEODO's own page prices the same entry tier at "Từ 18 triệu" and "từ 25 triệu" in two places. This is a market selling an unfalsifiable service.

*Are the agencies customers rather than competitors?* Unresolved, and it is the load-bearing unknown for C6. Evidence both ways: TOS built its own, which argues competitor; Midas's page tells prospects the "in-depth tools all cost quite a lot" (`các công cụ chuyên sâu đều có phí khá cao`), which argues a tool budget exists. No agency was contacted; `unknown — checked agency landing pages only, 2026-09-17`.

**Verdict on 2a's framing: KILLED.** **Verdict on reading 1d's evidence as validation: WEAKENED** — it is supply-side evidence, and the highest-profile supplier has already shipped the free tool.

---

## 4. Does Vietnamese law kill the ad-placement candidates outright?

**2a's claim** (§2, C3a): prohibited already by Google's spam policy and UCPD Annex I item 11; "P5 would add Vietnamese exposure... Neither can rescue it." (§2, C6): "as pure measurement, Vietnam's advertising law is not the gate — **and stating that is itself a claim P5 could overturn**."

**Checked**: `../../raw/vn-luat-quang-cao-2012-full-text.txt` and `../../raw/vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt` (wave 1b's pulls from `vanban.chinhphu.vn` and the signed PDF at `datafiles.chinhphu.vn`), extracting the provisions 1b cited but did not quote. Raw: `../../raw/wave2b-vn-law-duty-bearers.md`.

**Found — the mechanism, not the vibe.** The statute allocates every online-advertising duty across four named roles (Điều 23.3: *người quảng cáo, người kinh doanh dịch vụ quảng cáo, người phát hành quảng cáo, người chuyển tải sản phẩm quảng cáo*), importing Điều 12, 13, 14 and 15a.

Which role the founders occupy is settled by text, not inference. Điều 2.6: *"Người kinh doanh dịch vụ quảng cáo là tổ chức, cá nhân thực hiện **một, một số hoặc tất cả các công đoạn** của quá trình quảng cáo theo hợp đồng cung ứng dịch vụ quảng cáo với người quảng cáo."* A two-person HCMC team paid by a brand to place product-placement text performs one or more stages of the advertising process under a service contract. It is inside the definition, and Điều 23.3 binds it to all of Điều 23.2 from 2026-01-01.

Whether the duty can be discharged is settled by the same text. Điều 23.2(a) requires *"dấu hiệu nhận diện rõ ràng... để phân biệt giữa nội dung quảng cáo với các nội dung khác không phải quảng cáo"* — a sign reaching the *người tiếp nhận quảng cáo*, defined at Điều 2.9 as the person who receives the information through the advertising medium. Điều 23.2(b) additionally requires an easily recognisable control letting that recipient **turn the ad off, report it to the service provider, and refuse unsuitable ad content**. And the publisher role is defined twice over by reference to a medium the duty-bearer manages — Điều 2.7 *"phương tiện quảng cáo thuộc trách nhiệm quản lý của mình"*, Điều 14.1 *"phương tiện của mình"*, Điều 14.4 direct responsibility for what that medium carries — with Điều 14.3 requiring documents be handed over *"khi người tiếp nhận quảng cáo... yêu cầu."*

A placement rendered inside a third party's generated answer gives the founders no surface in the recipient's experience. They cannot place the sign; they cannot place the off-switch; there is no identifiable publisher for the recipient to request documents from. **This is not a disclosure that has been omitted and could be added. It is a disclosure surface that does not exist.** C3a's non-compliance is structural and cannot be engineered away by adding a label.

Reach across the candidate set: C3a is prohibited a third time, now in the founders' own jurisdiction, by a general, platform-neutral instrument that needs no AI-specific provision to bite. C3b is not reached by the law as pure format conversion — but it is exposed the moment a customer adds paid content, which is the same drift risk 2a identified, now with a home-jurisdiction penalty attached. C1, C4, C6, C7 and C8 are not reached: measurement is not *quảng cáo* under Điều 2.1. The single compliance item that does attach to any Vietnamese entity billing for this work is Điều 23.3(a): *"phải đăng ký thuế, kê khai, nộp thuế đối với doanh thu phát sinh từ dịch vụ quảng cáo."*

**Verdict on "C3a is out on evidence": SURVIVES, strengthened.** **Verdict on "a disclosure could satisfy an AI placement": KILLED.** **Verdict on "P5 does not gate C6 as measurement": SURVIVES.**

---

## 5. The measurement premise — does anyone want origin-side crawler data?

**2a's claim** (§2, C1 and §5): the crawl-log half is already free, "only the *join* is unpriced"; and the cross-site record "cannot be bought from Cloudflare, because Cloudflare sells each customer their own view and does not sell the cross-site join. It cannot be rebuilt quickly, because the value is in the elapsed time."

**Checked**, 2026-09-17, direct fetch: `darkvisitors.com` (home, `/pricing`, `/insights`, `/products/ai-chat-referral-tracking`), `knownagents.com/products/{agent-analytics,agent-identification-api}`, `developers.cloudflare.com/ai-crawl-control/` and its `/reference/worker-templates/`. Raw: `../../raw/wave2b-crawler-analytics-competitors.md`.

**Found.** `darkvisitors.com` now serves **Known Agents** (`© 2026 Bit Flip LLC`). It ships, today, with a **$0/month tier** (1 project, 100K events; Startup $29, Growth $299):

- **Agent Analytics** — *"See every crawler, scraper, and AI agent visiting your website in real time"* — with published integration guides for `cloudflare-worker`, `vercel`, `fastly`, `akamai`, `aws`, `wordpress` and a REST API. That is C1's origin half, with the Worker path documented.
- **Agent Identification API** — *"We keep track of 2,000+ agents, so you don't have to. Leave the collection, categorization, and maintenance to us"* — returning `{"agent_token":"Claude-User","operator_name":"Anthropic","result":"verified"}` and *"proves it isn't spoofed."* That is C2 in full, including the refresh-cadence maintenance 2a called C2's "one non-obvious asset."
- **The Agentic Web Index** — schema.org `Dataset`, `"isAccessibleForFree": true`: *"A continuously updating analysis of bot vs. human traffic, AI training, fetching, search indexing, browsing, robots.txt compliance, and AI chat referrals **across 5,000+ websites**."* Sections include AI Fetching, AI Search Indexing, Robots.txt & Compliance, Spoofing & Security. Headline metrics carry 90-day comparisons; the time series runs through **Sep 16** — the day before this pull.
- **AI Chat Referral Tracking**, free, *"in under 5 minutes"*: *"Citations — Which links appear in AI chat responses?"*, click-through, geography, across ChatGPT/Claude/Gemini/Copilot/Perplexity/Meta AI/DeepSeek/Mistral.

Separately confirmed: Cloudflare AI Crawl Control, page stamped **"Last updated Aug 14, 2026"**, *"Available on all plans"*, *"Deploy with zero configuration — Works automatically on all Cloudflare plans"*, with a GraphQL API. Its only published Worker template is an x402 payment gate.

So: the origin instrumentation is a free platform feature **and** a free product from a named vendor with a published cross-site longitudinal index — the exact artifact 2a's §5 says cannot be bought and takes elapsed time to build. It has been built, it is free, and it was current yesterday.

What genuinely survives is narrow: nobody sells *this fetch, at this time, became this sentence*. Known Agents measures citations and clicks, not answer text. But that surviving half is the answer-side half, which is barred on consumer surfaces by documents already read and is gated on P1/P2 — i.e. the half 2a's own fallback argument discards.

**Verdict: KILLED** for C1's asset, C2 entirely, and §5's moat claim. **SURVIVES, narrowly,** for the fetch→answer-text join as an unsold thing — with the caveat that unsold and unbuyable are not the same.

---

## 6. Detection-surface shelf life

**2a's claim** (§2, C2; attack item 5): IP-list matching is the only reliable detection for OpenAI/Anthropic/Perplexity, and tracking range drift is a moat "funded competitors skip."

**Checked**, 2026-09-17: `developers.cloudflare.com/bots/concepts/bot/verified-bots/web-bot-auth/`, `datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/`, `platform.openai.com/docs/bots` (all HTTP 200); `openai.com/gptbot/` 403'd. Raw: `../../raw/wave2b-detection-shelf-life.md`.

**Found**, two directions, both on file.

*Stable today.* OpenAI's own live crawler documentation still tells site owners to allow *"requests from our published IP ranges"* plus the user-agent string. Zero occurrences of `signature`, `Web Bot Auth`, `verify` or `reverse DNS` in that document. Wave 1's rDNS measurement is consistent with the vendor's own docs. The measured range facts also re-checked clean against `../../raw/`: `oai-adsbot.json` really is 2 prefixes, `creationTime 2026-05-12`; `oai-gptbot.json` still `2025-10-30T11:00:00`; `oai-chatgptuser.json` `2026-09-17T05:04:56`. The per-file cadence delta 2a built C2 on is real.

*Named successor already in production.* Cloudflare documents Web Bot Auth as a shipped verification method — *"Web Bot Auth is used as a verification method for verified bots and agents"* — with a live test endpoint (`crawltest.com/cdn-cgi/web-bot-auth`) and an implemented directory draft (`draft-meunier-http-message-signatures-directory-03`). The IETF architecture draft exists with named authors. And a commercial product already classifies agents by *"verified IP **or** HTTP message signature (Web Bot Auth)"* as alternative per-agent methods. No AI operator is named as an adopter in any of the three documents — `unknown — checked cloudflare.com + datatracker.ietf.org + platform.openai.com 2026-09-17`.

The asymmetry that matters: if signatures land, detection gets *cheaper and more certain for everyone*. The maintenance burden 2a framed as a moat becomes a solved, standardised lookup. A moat that a standards process can drain is not a moat.

**Verdict on "IP-list matching is the only method": WEAKENED** — true on today's vendor documentation, with a dated successor shipping elsewhere. **Verdict on "detection drift is a moat": KILLED.**

---

## 7. The C6 contradiction, reconciled explicitly

| Source | Statement | Date |
|---|---|---|
| `../plan/idea-set.md` §6, wave 2a | "It is a fallback and not the primary for one reason: **its demand is entirely unsourced.** No Vietnamese usage figure, no local willingness-to-pay figure, no local agency-market size was pulled by any pass." | 2026-09-17 |
| `../plan/idea-set.md` §2, C6 support | "No vendor in the roster claims Vietnamese coverage." "Absence of a competitor in a market nobody has sized is not a gap, it is an unexamined room." | 2026-09-17 |
| `../explore/cost-and-demand-pulls.md` §3, wave 1d | "8 confirmed [Vietnamese agencies]... selling branded 'GEO'/'AEO' services," four with published VND pricing: SEODO từ 18tr/200tr/350tr; Fast Marketing 32–65tr/tháng; Midas từ 80tr/tháng; TopOnSeek quote-only. | 2026-09-17 |
| This review (`../../raw/wave2b-vn-agency-audit-and-free-tools.md`) | TopOnSeek ships a free Vietnamese self-serve AI Visibility Checker; three of three agencies give the audit away free; SEODO publishes two conflicting entry prices on one page. | 2026-09-17 |

**Which the evidence supports.** 1d's, on the factual question, decisively: local agency-market activity and local pricing were pullable and were pulled, so "entirely unsourced" and "an unexamined room" were both false at the time they were written — 2a wrote them without the pull, not against it. 2a's *caution* nonetheless survives in altered form: what 1d found is vendor-published supply and list prices, not a signed contract, not a brand-side willingness-to-pay figure, and not a single Vietnamese buyer of measurement rather than optimisation. And the room, once examined, has an incumbent standing in it with the free tool already built.

Net: C6's demand moves from *unsourced* to *sourced-but-supply-side*. The blocker moves from "we know nothing" to "we know competitors, we still know no buyer."

---

## 8. Does the pick stand?

**No. C8 as written does not stand.** Its services verdict was imported from a market whose own scorecard scores this market the opposite way; its price band belongs to a different rate card 5x higher than this market's; its single market-specific demand citation describes an activity 2a itself lists as prohibited; and no buyer of an AI-answer audit has been found in any channel by any pass. The instrumentation it runs on is a free feature at Cloudflare and a free product at Known Agents, and the published cross-site research artifact 2a named as C8's compounding asset already exists, free, updated to the day before this review.

**What the evidence now favours: C6**, on three grounds and with one large caveat.

1. It is the only candidate with any sourced spend attached to it — four published VND price lists, one of them 80 triệu/month on a 12-month term.
2. It is the only candidate whose buyer is both reachable (HCMC, no US market access per `../../../../docs/method/scope.md`) and **payable**: domestic VND invoicing sidesteps the Stripe-doesn't-support-Vietnam wall that `vietnam-sg-access.md` shows breaks every other route, and which breaks C8's engagement billing specifically.
3. Its legal position is clean: measurement is not *quảng cáo* under Điều 2.1, so the amended Luật Quảng cáo does not reach it, and no OpenAI or Perplexity document read across two passes governs a non-customer website at all.

**The caveat, stated at full strength:** C6's evidenced demand is for *visibility optimisation*, which is sold by at least eight local agencies, given away as a free audit by three of three checked, and rests on a premise Google's own documentation denies. Promoting C6 promotes the candidate with competitors rather than the candidate with customers. Nothing in this review found a Vietnamese buyer paying for measurement.

One further item, which is 2a's own conditional map applied to a document read this wave rather than a new idea: **P3 resolved, and it resolved the way 2a said would help C7.** OpenAI's Ad policies, stamped 2026-08-10, contain *"These standards apply to all ad assets, including copy, images or video, and landing pages. **Ads must be consistent end-to-end**"*, *"**Destination integrity**: ...Landing pages and destinations must accurately represent the advertiser, product, or service described in the ad"*, and *"Advertisers may not... **attempt to circumvent our policies or enforcement processes**."* `../explore/policy-ceiling-addendum.md` Gap 3 quotes neither and marks the differential-serving column "Silent" — a compiled claim its own raw file does not support (`../../raw/wave2b-openai-ad-policies-destination-clauses.md`). Per §4 of 2a's conditional map, that gives C3a/C3b an advertiser-side contract breach and gives C7 the named rule it needed. C7's own killers are untouched: ChatGPT ads are not live in Vietnam, its buyers sit in markets the team cannot bill, and the rejection reason an advertiser actually wants stays inside OpenAI. Re-scoring C7 is 2c's call, not this file's.

---

## 9. What wave 2c must design around

Constraints, not a design.

1. **Do not design the crawl-log tier as the asset.** It is free twice over — Cloudflare zero-config on all plans, Known Agents free tier with a published Cloudflare Worker guide. Anything 2c builds there must justify itself against a $0 incumbent that already has 5,000+ sites, or be explicitly scoped as scaffolding for something else.
2. **Do not design a cross-site index.** It exists, free, current to 2026-09-16, with 90-day baselines. Elapsed time is no longer available as a moat.
3. **Do not price an audit.** No published price for one exists anywhere this project has looked, and every vendor actually checked gives it away to open a retainer. Any design whose revenue line is "paid audit" needs a named buyer first.
4. **Assume answer-side sampling is unavailable until a document says otherwise.** Consumer surfaces are prohibited by terms already read; the API path is ungoverned rather than permitted; and the "Step 4" gap is not a market opening. Design the origin half to ship and publish standing alone — 2a was right about that structure even though the artifact it produces is no longer novel.
5. **Design detection as a lookup with a swappable backend, not as maintained knowledge.** IP-list matching is correct today per OpenAI's own docs and will be superseded by Web Bot Auth signatures on an unknown timetable. Budget the CIDR matcher as replaceable; do not capitalise range-drift tracking.
6. **If the design is Vietnam-facing, it must be measurement a customer can falsify.** The local field sells causes (entity, schema, llms.txt) against outcomes nobody measures, and Google's own documentation says those inputs are unnecessary for its AI features. Falsifiable measurement is the only differentiation this review found, and it is differentiation against incumbent claims, not against an incumbent product.
7. **Bill in VND or solve payments first.** Merchant-of-record does not cover services billing; Stripe does not cover Vietnam. This constrains revenue shape before it constrains architecture.
8. **The differential-serving branch stays dark, permanently, not provisionally.** Vietnamese law now supplies a third independent prohibition, binding at home, with no satisfiable disclosure path. 2a's instruction to build the branch and leave it unused should become: do not build the branch.

## Caveats

- Every new pull this wave is a vendor's own marketing or documentation page. Known Agents' "5,000+ websites," its metrics, and the Vietnamese agencies' prices are all vendor-stated and unverified by any independent source.
- Three of eight Vietnamese agencies were re-fetched. Hashmeta VN, Nextop, seo.danang.vn and Fast Marketing were not — `unknown — checked 2026-09-17, not pulled`. No agency was contacted, so "agencies as customers for a tool" is unresolved.
- No AI operator was identified as signing Web Bot Auth requests. The migration claim rests on Cloudflare shipping a verifier plus one third-party product's definition sentence.
- The OpenAI ad-policy clauses come from a Wayback snapshot of a page stamped 2026-08-10; `openai.com` 403s every direct method. Live currency on 2026-09-17 is unconfirmed.
- Vietnamese translations are mine and uncertified; the Vietnamese text is operative. Điều 15a is unread, the Điều 23.8 implementing decree is still unlocated, and no penalty provision or enforcement case was pulled.
- Google's AI-features page carries no `Last updated` stamp that was captured; the Search Console help page that would settle the Midas conflict was a JS-thin body.
- This review killed claims. It did not find a buyer for anything, and it did not build or test a prototype. A killed claim is not a decision — the verdict is the user's.
