# Pass 4 — three projects executed, three picks killed, three probes pending

2026-09-17. Compiled from `../../projects/ai-ads-injection/docs/plan/re-pick.md`, `../../projects/agent-hermes-dashboard/docs/plan/re-pick.md`, `../../projects/ai-attack-defense/docs/plan/re-pick.md`, and the raw pulls each cites. Method amendments from the same three files are in `../method/evidence-rules.md`.

Reads on top of `pass3-read.md`. Where they disagree, this file is later.

Passes 1–3 tested ideas and then tested the team. **Pass 4 executed.** Three project folders ran the same pipeline on the same day — explore, idea set, adversarial review against this repo's research, re-pick. Each review killed its project's primary candidate. Each re-pick recommends stopping and pre-registers one cheap probe that could reverse it.

Verdict is the user's, per `../../CLAUDE.md`. This file is evidence and options.

---

## 1. `ai-ads-injection`

**Set out to test.** Can a site you control detect an AI assistant's retrieval fetch and serve it different text — and does the changed text move the model's answer (`../../projects/ai-ads-injection/CLAUDE.md`).

**Established as fact.** The detection half works and is cheap. AI-assistant fetches are identifiable from the origin by published IP range or forward-confirmed rDNS, never by user-agent (`pass2-read.md`). `OAI-AdsBot` publishes two prefixes, `130.131.229.128/25` and `20.168.90.128/25` — 256 addresses, `creationTime 2026-05-12T03:00:00` (`../../projects/ai-ads-injection/raw/oai-adsbot.json`). OpenAI's ad policies, page stamped "Updated: August 10, 2026", do carry a destination-integrity duty: *"Ads must be consistent end-to-end"*, *"Landing pages and destinations must accurately represent the advertiser, product, or service described in the ad"* (`../../projects/ai-ads-injection/raw/openai-ad-policies.txt`). Vietnamese AI-visibility spend is published and real — SEODO từ 18tr / 200tr / 350tr, Fast Marketing 32–65tr/tháng, Midas từ 80tr/tháng on 12 months, TopOnSeek quote-only (`../../projects/ai-ads-injection/raw/vietnam-ai-visibility-demand.md`). And a Vietnam-resident seller can be paid out for a digital product: Polar via Stripe Connect Express and Lemon Squeezy both list Vietnam (`../../projects/ai-ads-injection/raw/wave2abis-mor-seller-eligibility-vietnam.md`) — never tested by onboarding.

**Killed, and by what.** The delivery half is out of scope permanently, not merely hard: OpenAI's ToU effective 2026-01-01 bars programmatic extraction of Output, Perplexity ToS s5.2(i) bars it *"or engage in any manual process to do the same"*, and Google's spam policy defines crawler-conditional text as cloaking verbatim. Seven of eight candidates are dead or unreachable (`re-pick.md` §2). The origin-telemetry asset is free at Cloudflare ("Available on all plans") and Known Agents ($0 tier, 2,000+ agents). A better visibility checker competes with TopOnSeek's free, Vietnamese, self-serve AI Visibility Checker, which already ships six pillars, competitor comparison and a prospect-report generator (`../../projects/ai-ads-injection/raw/wave2b-vn-agency-audit-and-free-tools.md`). And Google's own documentation denies the premise the eight Vietnamese agencies sell: *"There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"*, *"You don't need to create new machine readable files, AI text files, or markup"* (`../../projects/ai-ads-injection/raw/wave2b-google-ai-features-doc.md`).

**Where it stands.** One candidate alive and changed: C6, Vietnamese answer-visibility measurement, narrowed to falsification — telling a brand whether its 32–80 triệu/month retainer changed anything an engine does. No buyer has ever been contacted, in any channel, by any pass. C7 (OAI-AdsBot landing-page observability) is the one candidate with a named, dated, published rule to measure against — and it is unbuildable from Vietnam, because AdsBot visits only submitted ad destinations and ChatGPT ads are not sold in Vietnam.

**Cost to continue.** ≤5 working days of human outreach. $0 infrastructure (Cloudflare free tier, 100,000 req/day), optional $11.08 domain. API sampling spend only after a deposit clears.

---

## 2. `agent-hermes-dashboard`

**Set out to test.** Whether the supervision layer, not the agents, is the product for a small business (`../../projects/agent-hermes-dashboard/CLAUDE.md`).

**Established as fact, by measurement.** `Stop` and `SubagentStop` carry **no `cost` field and no `duration_ms` field** — Claude Code v2.1.259, interactive OAuth, four live `claude -p` runs, reproduced twice including one real subagent spawn (`../../projects/agent-hermes-dashboard/raw/hook-payload-measurement-2026-09-17.md`). What does exist: `total_cost_usd` and `duration_ms` per whole `claude -p` invocation, which do not split across a subagent fan-out; and `agent_id`, `agent_type`, `agent_transcript_path` on `SubagentStop`, which are real attribution keys. Zero occurrences of `costUSD` or `duration_ms` in the transcripts; `~/.claude/stats-cache.json`'s `costUSD` is hard-coded 0; no headless `/usage`. Demand, counted first-hand: 828 title-scoped `usage limit` issues in `anthropics/claude-code` — 0.88% of 93,582 titled issues, last of eleven topics sampled, 87.8% closed (`../../projects/agent-hermes-dashboard/raw/2abis-demand-signal-interrogation-2026-09-17.md`).

**Killed, and by what.** Candidate B, the competitor-price watcher, on three independent lines in `../../projects/agent-hermes-dashboard/docs/review/market-check.md` §7 — including a size-stratified statistic that verified correctly and pointed the opposite way from the thesis built on it. Candidate A was already dead in this repo before the project opened (`pass3-read.md`: the only idea column with no positive row). The cost mechanism under C, F and H(d) died to the measurement above. And the demand signal, interrogated, is demand **directed at the vendor**: all eight highest-reaction issues are bug reports against Anthropic's own metering; the top feature request in the area, #20636, was filed 2026-01-24 and closed `completed` 2026-04-24 — observed vendor absorption time, one quarter; the enabling primitive for the surviving function, #65524, was closed `not_planned` 2026-07-09 with 0 reactions. The category leader, `ccusage`, is free at 18,591 stars.

**Where it stands.** One candidate alive and twice narrowed: H(b), a local governor that defers a queued job past a window reset instead of letting it die mid-run. Three candidates (C, D, G) were never tested; two of them are not supervision-layer products and belong to a different question. Nothing in the 828 is a person asking to buy something.

**Cost to continue.** ~3 days of the one builder, $0 cash — and a design decision that must be named before starting, since headroom is not readable headlessly.

---

## 3. `ai-attack-defense`

**Set out to test.** Find one narrow niche in AI attack/defense with a Southeast Asian buyer reachable without field sales, and build one small thing (`../../projects/ai-attack-defense/CLAUDE.md`).

**Established as fact, from primary text.** Vietnam's Law 134/2025/QH15 is in force **2026-03-01**, with transitions to 2027-03-01, or 2027-09-01 for health, education and finance (Điều 34–35). Providers self-classify into high/medium/low and notify medium and high to Bộ KH&CN through a one-stop portal before deployment (Điều 10.1, 10.3). Mandatory conformity assessment binds **high risk only** (Điều 13.1); third-party certification applies only to a Prime-Minister list that has not been issued (13.4). Điều 13.2 defines assessment as conformity with Điều 14 — and Điều 14 is **entirely process duties**, with no performance, accuracy or safety threshold anywhere in it. Nothing in the transcribed text mentions adversarial testing, red teaming, guardrails, jailbreaks or language coverage. All from `../../projects/ai-attack-defense/raw/repick-vietnam-ai-law-pull.md`, transcribed visually from rendered gazette pages; pages 3 and 10–18 are `unknown — not transcribed 2026-09-17`, so penalties are unknown.

**Killed, and by what.** The reading that medium-risk providers must buy an independent assessment: Điều 10.5.b's grammatical subject is the supervising authority, and independent assessment is one of three alternatives the **regulator** may choose. The endpoint exposure grader, the only absence that survived the review wave, lost three of five sub-claims to one wider sweep — `JailbrokenAI/wallbreaker` (1,459 stars) ships `tools/prefill.py`; promptfoo ships a `special-token-injection` plugin; nuclei ships `http/exposures/apis/vllm-openai-api-exposed.yaml`, `verified: true` (`../../projects/ai-attack-defense/raw/repick-endpoint-absence-pulls.md`). Of eleven products: five dead, three alive-but-changed, three never tested. **No survivor has a buyer.**

**Where it stands.** The regulatory trigger this repo hunted across three passes exists, in the founders' own jurisdiction — and it demands classification, disclosure, labelling, dossiers and explanation, none of which is this team's competence. The decree that would specify any of it is unissued: `unknown — checked vanban.chinhphu.vn 2026-09-17`, where list pages return HTTP 500. One correction runs the other way and is recorded rather than acted on: selling a digital product to a US/EU buyer from HCMC is priced, not blocked — a merchant of record costs 5% + 50¢, $0 fixed, no entity (`../markets/vietnam-sg-access.md`), and `../method/scope.md` calls the US-buyer question "a business call, not a research finding".

**Cost to continue.** 2–3 days of one person, zero cash — plus a browser and a WebSearch budget, both of which this session lacked.

---

## The cross-read

**All three converged on the same shape of answer.** In each project the mechanism was tractable and the demand was never evidenced.

| | `ai-ads-injection` | `agent-hermes-dashboard` | `ai-attack-defense` |
|---|---|---|---|
| Mechanism established | Yes — detection by published IP range | Yes — hook schema measured live | Yes — statute read in primary text |
| Mechanism is the asset | No. Free at Cloudflare, Known Agents | No. Free at `ccusage`, 18,591 stars | No. Free at nuclei, promptfoo, wallbreaker |
| Buyer named | None, any channel, any pass | None. 828 issues ask the vendor | None in any pulled source |
| Price point in this market | Published VND lists; no buyer asked | `unknown — no revenue figure found` | No SEA price point exists in repo |
| Primary candidate | Killed by review | Killed by review | Killed by review |
| Blocking constraint | Engine ToS, then demand | Vendor absorbs top request in a quarter | Decree unissued; trigger is not security |
| Survivors with a buyer | Zero | Zero | Zero |

Four things they share, stated once.

**1. Every mechanism question got answered; no demand question did.** Crawler identification, hook payloads, statute scope — all three teams resolved their hard technical or legal question inside one day, correctly, with primary evidence. Not one resolved who pays.

**2. Nobody spoke to a potential buyer.** No agency, brand, advertiser, developer or Vietnamese company was contacted by any agent in any project this session. Every negative on file is a search-level or landing-page-level negative. The ads re-pick names this against itself: *"an absence of published prices, not an absence of transactions"*, and closing on it is the same class of error as the method failures in `../method/evidence-rules.md`.

**3. Free incumbents set the floor in all three lanes.** This is `cross-read.md` pattern 2 — *"Nothing a two-person team builds competes with free on features"* — confirmed three more times independently, against three unrelated free tool sets.

**4. All three diagnosed the same method failure, separately.** A compiled claim its own evidence did not support. That is a repo-level defect, not three agents' bad luck, and it is why `../method/evidence-rules.md` exists.

**What is not true.** This was not a wasted session. Three facts established today are load-bearing, durable and were not in this repo yesterday: the measured Claude Code hook schema, the actual subject and scope of Vietnam's AI Law, and a documented Vietnam payout path for a digital product. Two of the three were found only by running or reading the thing directly, against files that said otherwise.

---

## The three pending probes

Each was pre-registered by its own author before the test runs, and is **not adjustable after the fact**. Rules quoted as written.

| Project | Pre-registered rule, verbatim | Cost | Who runs it |
|---|---|---|---|
| `ai-ads-injection` | PASS: "≥2 of the 20 have paid a 7.500.000 VND deposit. Money received, not promised". WEAK: "0 deposits but ≥3 written replies naming a budget line and asking for a scheduled call". FAIL: "Anything else" | ≤5 days, $0 infra, $11.08 optional domain | **Human only** |
| `agent-hermes-dashboard` | "≥ 100 GitHub stars within 14 days of release, AND ≥ 3 distinct people who are not the authors, unprompted, asking for a paid, hosted or supported version." Miss either → stop | ~3 days one builder, $0 cash | **Mixed** |
| `ai-attack-defense` | Revive: "P1 portal live, ≥50 medium/high systems published, and P2 decree specifies assessment content". Hold: "P1 live but <50 entries, or P2 decree absent". Stop: "P1 not locatable and P2 no decree and P3 no register" | 2–3 days, $0 cash, needs browser + search budget | **Agent** |

Attached conditions the authors wrote alongside the rules, which bind equally:

- **Ads.** 20 named organisations, list frozen in writing before the first message. One offer, one price: 15.000.000 VND, 50% deposit, a 10-working-day report on one named domain. Answer sampling by paid API only. Email plus Zalo or LinkedIn, one message each, one follow-up on day 3, no discounting, no re-scoping mid-probe. Deposits from personal contacts of either founder do not count. WEAK buys exactly one 5-day extension, once. The author states the asymmetry in advance: a deposit is strong positive evidence, a FAIL is weak negative evidence, and FAIL closes the project only because it sits on top of three research passes and four waves that also found nobody.
- **Hermes.** Stars alone are pre-registered as insufficient: *"500 stars with zero paid asks is a stop, not a proceed."* Free and MIT, one release post, no paywall, no waitlist, no cold outreach to issue filers. If neither of the two workable headroom mechanisms can be built in three days, the test does not run and the answer is stop.
- **Attack-defense.** Three desk probes against Vietnamese primary sources: P1 locate the Điều 8 one-stop portal and count published medium/high notifications since 2026-03-01; P2 find any decree under Điều 9.3 / 10.7 / 11.6 / 13.6 and the Thủ tướng's high-risk list under 13.4; P3 find the Điều 13.5 register of assessment bodies. A "Hold" is explicitly not a licence to build anything as a consolation.

### Which need a human

**`ai-ads-injection` — human, entirely.** Every element is contact with a real company: messages sent under a real identity, a real offer at a real price, a real deposit received. No agent runs any part of it.

**`agent-hermes-dashboard` — split.** An agent can build the governor and can count stars and asks afterwards. Publishing it under the user's name — the repo, the license, the release post, and any reply to a stranger asking for a paid version — is human. The build is worthless without the publication, so the probe cannot start without human time.

**`ai-attack-defense` — agent, fully.** Reading published government registers and gazette pages, contacting nobody. It needs a browser (`vbpl.vn` and `phapluat.gov.vn` return a loading shell to `curl`) and a WebSearch budget; this session had neither, and its shallow probe found nothing: `unknown — checked 2026-09-17, portal not located`.

**A fourth option, named by the attack-defense author and not in any probe.** Three conversations with AI Hay, Vbee or Filum AI — named in `../markets/vietnam-sg-access.md`, all reachable from HCMC — answer the business half of P1–P3 in a way no portal count can. That author's own words: *"A human should probably run it in parallel; on information per day it dominates my test."* It is outside an agent's remit and is the only route in this whole session that tests demand by asking someone.

---

## What pass 4 killed

- **Crawler-conditional serving as a product.** Not hard — barred, by three separate published documents, permanently.
- **"Per-task cost and duration are free" on Claude Code.** Measured false on v2.1.259. Any cost-shaped agent-supervision product now carries a self-maintained price table.
- **"SEA has a compliance trigger for AI security testing."** The trigger is real and belongs to a compliance-documentation business. The statute names no security control.
- **Ranking a candidate on an unattacked absence.** Observed survival roughly one in five (`../method/evidence-rules.md` rule 6).
- **The assumption that a correctly-sourced number supports the thesis citing it.** The SBI case verified perfectly and inverted.

## What pass 4 strengthened

- **`cross-read.md` pattern 2, three more times.** Free OSS set the floor in three unrelated lanes.
- **`pass3-read.md`'s access finding, in both directions.** A digital product has a documented Vietnam payout path (two MoR vendors, untested by onboarding); a services sale and an advertiser account still do not.
- **`projects/CLAUDE.md`'s "measured beats argued".** Two of this session's three durable facts came from running or reading the thing, against files that said otherwise.

## Open

1. **Does any of the three probes get run, and by whom.** Two of three need human days.
2. **Whether the fourth idea slot in `../method/scope.md`, still blank, is opened before or after the probes.**
3. **Whether the survivors that were never tested — hermes C, D, E, G; attack-defense 1.2, 1.3, 4.3, 5.1 — are re-asked as their own questions or closed with their projects.** Their authors recommend the former for the non-supervision ones and are silent on the rest.

## Caveats

- Every project's re-pick recommends stopping while arguing the case against stopping at full strength. Two of the three explicitly state a reader weighting unexamined optionality differently would reach the opposite conclusion from the same evidence. This file does not resolve that; it reports it.
- **WebSearch was exhausted at 200/200 before pass 4's synthesis ran**, session-wide. Every absence in this file inherits the channel limits recorded in its source project's caveats.
- The Vietnam statute reading rests on a visual transcription by one agent of a PDF with no text layer. Pages 3 and 10–18 were not transcribed; penalties, the high-risk list and any decree are `unknown`.
- The hook measurement is one machine, one version (v2.1.259), one auth mode, four invocations. It settles the yes/no asked; it does not characterise every hook event.
- The probe thresholds — 20 organisations, 15.000.000 VND, 100 stars, 3 paid asks, 50 notified systems, three days — are their authors' engineering and commercial judgement, labelled as such by each of them, not sourced. They are recorded before the tests so they cannot be moved after.
- No conflicting figures were averaged anywhere in this file. Where two sources disagree they sit in their own project's file, attributed.
- This file compiles from three re-pick documents and the raw pulls they cite. The intermediate compiled files those re-picks correct were not independently re-verified here.

No verdict. Per `../../CLAUDE.md`, that is the user's.
