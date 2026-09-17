# Re-pick — wave 2a-bis

2026-09-17. Binding input: `../review/market-check.md` (wave 2b). Target of the re-pick: `idea-set.md` (wave 2a), whose primary candidate B is dead and whose fallback H is narrowed to one function.

New first-hand evidence added by this wave: `../../raw/2abis-demand-signal-interrogation-2026-09-17.md` — authenticated `gh` CLI, 2026-09-17, interrogating the 828-issue signal 2b established.

**`../explore/telemetry-measured.md` landed during this wave and is used as measured fact.** Wave 1e, Claude Code v2.1.259, interactive OAuth, 4 live `claude -p` runs, reproduced twice including one real subagent spawn: `Stop` and `SubagentStop` carry **no `cost` field and no `duration_ms` field**. `../explore/claude-code-substrate.md` and `../explore/task-telemetry.md` were both wrong; `../review/market-check.md`'s correction (ii) is confirmed. Nothing below is conditional any more — the contested claim broke in the direction that costs C, F and H(d) the most, and §2 is re-scored accordingly.

---

## 1. Post-mortem: which belief broke

**The belief**: that a verified, dated, size-stratified statistic is evidence for the thesis built on it.

The SBI figures were real. 2b re-fetched the PDF, rasterised p.11, and the numbers matched the relay exactly (`../review/market-check.md` §1). Every rule in `../../../CLAUDE.md` was obeyed — sourced, dated, kind-labelled, traced to `raw/`. And the statistic pointed the **opposite way from the thesis**: the $0-1M cohort uses competitor pricing at ~54%, the highest of any band, and the source calls that the error to correct.

How it got through, four mechanisms, in order of how much each contributed:

| # | Mechanism | Evidence |
|---|---|---|
| 1 | Verification effort went to the number, never the direction | 2a's attack item #2 asks "are the figures right", not "do they support B" |
| 2 | The thesis preceded the search | 2a needed a size-stratified source; SBI was the only qualifier found |
| 3 | A sub-agent's causal synthesis entered `raw/` wearing quote marks | 2b §1: the "expensive to implement" mechanism is the relay's, unstratified in source |
| 4 | No rule in this repo catches a correctly-sourced wrong-direction number | All existing rules are provenance rules |

**The general lesson, stated as a rule this repo does not yet have.** For any statistic that is load-bearing for a thesis, record verbatim what the source's own author concludes from it, next to the number. If the author's conclusion contradicts the thesis, that is the finding — not a nuance to caveat. Provenance rules catch fabrication and staleness. They do not catch inversion.

**Second lesson, from this wave's own pull.** A count with no denominator is not a measurement. 2b reported 828 issues; 828 is 0.88% of the repo's 93,582 titled issues and ranks last of eleven comparable topics sampled (§3). The number is true and the scale was never stated. Same failure family as the SBI inversion, different dress.

**Third lesson, from 1e, and the repo already had the rule.** Two of this project's own explore files asserted that `Stop`/`SubagentStop` carry `cost` and `duration_ms`. Neither had been run. `../explore/task-telemetry.md`'s own caveats section asked for a live test and was ignored for two waves; `../../../projects/CLAUDE.md` states *"Measured beats argued"* as a standing rule. A docs read was carried as a mechanism through an idea set, a pick and a review before anyone executed it. The rule existed and was not applied — which is a different failure from the SBI one, and cheaper to fix: when a claim names a field, run the thing.

**Why this threatens the sibling projects.** Both remaining ideas will want a "the market is blind to X" statistic, and the cheapest such statistic is always published by a vendor selling the fix for X. `../../../docs/findings/pass3-read.md:56-59` already records three prior over-reads in this repo (the two-founders survey, the recirculated CAC figure, the animation-jobs data). The SBI case is the fourth and the first where the number survived verification and the inference still died. That is the one the existing rules do not catch.

---

## 2. Survivor audit, A through H

Verdicts against 2b's findings plus this wave's pull. **Untested is not alive.**

| ID | Shape | Status | Reason, one line |
|---|---|---|---|
| **A** | Fleet supervision dashboard | **Dead** | Killed pre-project by `pass3-read.md`; no positive scorecard row |
| **B** | Competitor-price watch, memo | **Dead** | 2b, three independent lines; §7 of `market-check.md` |
| **C** | Recurrence-to-tool graduation | **Untested, and now more expensive** | Braintrust Patterns unrun; its free cost primitive measured absent |
| **D** | Mocking morning report | **Untested** | Zero demand evidence; no wave has attacked it |
| **E** | Agent-ops as a service | **Untested** | No wave attacked it; also not a supervision-layer product |
| **F** | Provenance and staleness layer | **Dead as a product** | 2b §4: a property of the record, not a purchase reason |
| **G** | Narrow agent into a marketplace | **Untested, and empty** | Rails confirmed; the product half is every other dead candidate |
| **H** | Cost-and-limit governor | **Alive, narrowed twice** | 2b cut it to function (b); §3 below cuts (b) further |

Notes where the one-liner is not the whole story:

**A** was never 2b's to kill because the repo had already killed it. `../../../docs/findings/pass3-read.md:44-49` scores `agent-dashboard` as the only idea column with no positive row — no price floor found, does not work at n=1, not reachable without US presence, team not domain expert, storyteller has no real job in it. `../../../docs/findings/cross-read.md:60-64`: *"No capital | Fails. Competes with $125M and three platform vendors"*, *"No field sales | Fails — every governance competitor is contact-sales"*, non-technical partner fit *"Weak fit."* And `cross-read.md:44`: *"Any product that sits between a model vendor and its customer is on a clock."* A supervision layer is that middle layer by definition.

**C** has two gates. Gate 1, Braintrust Patterns: 2a's attack item #6, not run by 2b, still `unknown — not pulled`. Gate 2, the telemetry dependency, is now **measured and failed**. `../explore/telemetry-measured.md`: no `cost` and no `duration_ms` on `Stop` or `SubagentStop`, across three live runs on v2.1.259. C is still buildable — `SubagentStop` does hand over `agent_id`, `agent_type` and `agent_transcript_path`, which are real attribution keys — but per-subagent cost now requires a supervisor process that opens the pointed-to transcript, sums `message.usage` tokens per line, reads `message.model`, and multiplies by **a price table the team maintains itself**. Verbatim, 1e: *"This is real engineering work, not 'read a field'."* Grep confirms zero occurrences of `costUSD` or `duration_ms` in any transcript.

Three consequences for C. **Build size**: `idea-set.md`'s 3-5 weeks was priced on reading a field; re-score upward, and add a standing maintenance cost — an external price table goes stale every time Anthropic reprices a model. **Differentiation**: the arithmetic C would now own is exactly what `ccusage` already does for free at 18,591 stars. **Fact 1 of `idea-set.md`** — *"Per-task cost and duration are free"* — is false as written; the free mechanism is `claude -p --output-format json`'s `total_cost_usd` and `duration_ms`, one number per whole invocation, which does not split across a subagent fan-out.

**D** is the only candidate whose asset is the collaborator rather than the builder, and `../../../docs/method/scope.md:7` puts the collaborator at half the team. It is also the only candidate with `unknown — not pulled` in every evidence column, and `../explore/hermes-substrate.md`'s `SOUL.md` fetch is the one adjacent data point, cutting against. Untested in both directions.

**E** is misfiled. It is a services business that happens to use a supervision tool; the tool never ships. The repo's own research is the most favourable it has for anything here — `cross-read.md:18` rates services revenue *"Per-engagement, works at n=1"* against the dashboard's *"Recurring SaaS, needs scale"*, and `market-gaps-2026.md:84`: *"The access gap is the only one where being in Ho Chi Minh City is an advantage rather than a cost."* Against it, from the same layer: `first-customers.md:133`, *"The strongest channel is the least portable"*, and `scope.md:30`, the user's stated preference for the technical side.

**F** dies on 2b's §4 reasoning, which this wave does not re-argue: nobody buys provenance before being burned by its absence, and the trace vendors bolt it on in a sprint. 1e makes it worse in the same direction as C — the zero-plumbing per-task cost mechanism F assumed does not exist, leaving only whole-invocation granularity. Note one thing 1e found that F would have wanted and that is genuinely absent: `~/.claude/stats-cache.json`'s own `costUSD` field is **hard-coded 0**, and there is no headless `/usage`. A staleness-and-provenance layer is still the only thing in this project confirmed unbuilt by the platform; it is still not a reason to buy.

**G** is a channel, not a product. `first-customers.md:111-115` confirms the rail — Shopify, *"You keep 100% of your first $1,000,000 USD in gross app revenue"*, one-time $19 registration, Hyperwallet payout, Vietnam eligibility unconfirmed. A confirmed rail with nothing to put on it is not a candidate.

---

## 3. The one real demand signal, interrogated

2b: 828 title-scoped issues in `anthropics/claude-code`, *"the only direct demand evidence anywhere in this project"*. This wave reproduced every count first-hand and then asked what they say. Full pull: `../../raw/2abis-demand-signal-interrogation-2026-09-17.md`.

**Scale.** 828 of **93,582** titled issues = 0.88%. Against ten other single-phrase title searches in the same repo on the same day: `windows` 5,530, `mcp` 4,806, `context` 4,314, `hook` 2,901, `permission` 2,768, `skill` 2,258, `crash` 2,064, `subagent` 1,797, `memory` 1,424, `vscode` 1,370. `usage limit` is **last of the eleven**. 727 of the 828 (87.8%) are closed.

**Composition**, 300 most recently created: 144 `bug`, 143 `stale`, 73 `duplicate`, 57 `enhancement`. Median comment count 2; 40 of 300 have zero comments.

**What the loudest ones ask for.** All eight highest-reaction issues are bug reports against Anthropic's own metering — #16157 *"Instantly hitting usage limits with Max subscription"* (725 reactions, 1,495 comments), #19673 *"You've hit your limit · While usage is still at 84%"*, #29579 *"Rate limit reached despite Claude Max subscription and only 16% usage"*. Nobody in that set wants a tool. They want the meter to be right.

This matters beyond framing: **a third-party tracker reads the same numbers the bug reports say are wrong.** Building on a contested meter produces a confident wrong figure, which is the first of the four tone-liability lines `idea-set.md` names — *"when the number is wrong."*

**What the feature requests ask for.** Of 57 `enhancement` issues sampled, ~18 ask Anthropic to expose usage data so external tools can read it — #94424, verbatim, *"an event when session usage or a rate-limit window changes, so trackers do not have to poll."* The wording presupposes free trackers already exist. ~10 ask for resume-after-the-wall, which shipped as `autoContinueAtUsageLimit`. ~7 ask Anthropic to loosen the limits. ~7 are banner nits.

**Is the need met already?** Two dated facts answer it.

- The highest-reaction feature request in the whole 828 — **#20636**, *"Expose rate limit usage (session %, weekly %) to statusLine configuration"*, 59 reactions — was filed 2026-01-24 and **closed `completed` 2026-04-24**. Anthropic shipped it free in three months.
- The highest-reaction request in the adjacent queue cluster — **#50246**, 242 reactions — is likewise `state_reason=completed`, 2026-04-18.

The observed vendor absorption time for a top-voted request in exactly this area is **one quarter**. That is `idea-set.md`'s own stated kill condition for H, now measured rather than asserted.

**What survives for H specifically.** 2b narrowed H to function (b), pre-emptive deferral before the window wall. Title-scoped volume for that function: `pacing` 8, `budget-aware` 4, `self-pacing` 3, `pre-emptive` 1. The request for the enabling primitive — #65524, *"Expose current usage / limit state to the model (self-pacing for long autonomous runs)"* — was **closed `not_planned` on 2026-07-09** with 1 comment and 0 reactions. The only free implementation, `Star001-KR/claude-session-budget`, was created 2026-05-09, last pushed 2026-05-15, and has 8 stars: six days of work, abandoned four months.

**And 1e hardens the feasibility problem under it.** H(b) needs remaining-window headroom, and `../explore/telemetry-measured.md` confirms by measurement that **`/usage` has no headless equivalent** — no `usage` subcommand and no `--usage` flag in `claude --help` on v2.1.259, interactive-session-only. `~/.claude/stats-cache.json` holds lifetime cumulative token counts with `costUSD` hard-coded 0 and no per-task granularity. So a headless governor cannot read headroom; it must infer it by accumulating tokens against an allowance whose size Anthropic does not publish (`../explore/gap-pulls.md` gap 2, confirmed absent three times). That is why #65524 mattered, and #65524 is the request Anthropic declined. H(b) is a deferral decision computed against an unknown denominator.

**Two corrections against `../review/market-check.md`, both from a new pull, not from reasoning.**

| 2b's statement | First-hand, 2026-09-17 |
|---|---|
| #33323 *"auto-closed by a stale bot"* | State **`open`**, `state_reason` null, 19 comments, 49 reactions |
| `"budget" in:title` 153, cited as spend demand | 46 are `token budget`, 40 `context budget`, 16 `thinking budget` |

The 261 `queue` issues are about typing a second prompt while the first runs — interactive steering — not about deferring work ahead of a quota wall. They are not H(b) demand.

**Verdict on the signal.** The demand is **real, large in absolute terms, and unmonetizable by this team.** It is demand directed at the vendor, for the vendor to fix its own meter and to expose its own numbers for free; the vendor answers top-voted requests in this area in about a quarter; the category leader is free at 18,591 stars with no funding file; and the one function the vendor has declined has single-digit title-scoped volume and an abandoned reference implementation. Nothing in the 828 is a person asking to buy something. `unknown — no revenue figure found for any tool in this category, checked GitHub 2026-09-17`.

---

## 4. Recommendation

**Stop this project as scoped.** The premise — *the supervision layer, not the agents, is the product* — did not survive contact. Name the part that broke: not the technology, which wave 1 confirmed in detail and correctly; the **buyer**. Every candidate resolves to one of three shapes, and all three are closed:

1. Sell supervision to developers — floored at free. `cross-read.md:46`: *"Nothing a two-person team builds competes with free on features."* Confirmed here: 18,591 stars, no funding file, and the vendor shipping the top request in a quarter.
2. Sell supervision to non-technical buyers — unreachable. `pass3-read.md:44-49`, no positive row; no field sales motion; `first-customers.md:133`, the one channel that works is the one that does not travel.
3. Sell something else that uses supervision internally — that is candidate E, a services business, and it is a different question with a different brief.

Two of the eight candidates (D, E) were never tested and are not supervision-layer products. They should be re-asked as their own questions rather than kept alive here to justify a project whose premise is gone. One (C) is a genuine supervision-layer candidate that was never tested; see the gate in §5.

**The case against stopping, at full strength.**

- **Three of eight were never tested.** Stopping on C, D and G is stopping on ignorance, not on evidence. C in particular has a specific, cheap, unrun test that 2a named and 2b skipped: one hands-on session with Braintrust Patterns, roughly a day, to see whether it closes cluster→generated-tool. That is the most defensible technical claim in the set if it comes back negative, because C's mechanism is the only one confirmed absent from the platform rather than merely absent from a search.
- **E is the one shape the repo's own research favours** — works at n=1, geography an asset, no scale requirement — and no wave has laid a glove on it. Killing the project buries it unexamined.
- **The tone hypothesis has never been tested at all**, and it is the only place the non-technical half of a two-person team has a job. `unknown — not pulled` is not a refutation.
- **The evidence base is an asset.** Subscription economics, the 2026-06-15 billing withdrawal, the Vietnam payment rails, and now a measured hook-payload schema are first-hand and transfer to the sibling projects. Stated against itself: the telemetry half of that base was **wrong for two waves** until 1e ran it, so the asset is smaller than it looked on 2026-09-17 morning. It argues the waves were not wasted; it does not argue for continuing.

**Why I still recommend stopping despite that.** C, D and G do not fail for lack of testing; they fail the same way B did before anyone tested it, and the tests would confirm rather than change that. Suppose Patterns comes back negative: C is then a technically defensible tool — now carrying a self-maintained price table it did not have this morning (§2) — for developers, competing with free, in a lane where the vendor ships the top request in a quarter. The competitive test is not the binding gate. The demand gate is, and it is shut for every candidate in the set — including H, whose 828 turned out to be 828 people asking Anthropic for a free fix.

---

## 5. The pre-registered revival gate

Written **2026-09-17, before any test runs, and not adjustable afterwards.**

This is a revival condition, not a recommendation to run it. If the user overrules the stop, this is the cheapest thing that proves or kills the premise in under a week.

**Test**: build H function (b) only — a local governor that, before dispatching a queued job, projects its cost against remaining window headroom and defers it past the reset instead of letting it die mid-run. Ship it free and MIT on GitHub. One release post. No paywall, no waitlist gate on the download.

**Cost**: ~3 days of the one builder was 2b's estimate and it was priced before 1e. Re-scored: the headroom number is not readable headlessly (§3), so the build must either accumulate `total_cost_usd` per invocation against a user-supplied ceiling, or parse the interactive session's own state. **Say which of the two before starting, and if neither is workable in three days the test does not run and the answer is stop.** $0 cash. No third-party targeting: public release, no cold outreach to issue filers.

**Pre-registered rule, both conditions required to proceed:**

- **≥ 100 GitHub stars within 14 days of release**, AND
- **≥ 3 distinct people who are not the authors, unprompted, asking for a paid, hosted or supported version.**

**Miss either → stop, and this project closes for good.**

**Why 100.** Base rates from `../../raw/2abis-demand-signal-interrogation-2026-09-17.md` §9: the existing implementation of this exact function got **8 stars**; the category leader got **18,591**. 100 is ~12× the observed floor and ~0.5% of the observed ceiling — reachable if there is a user base, not reachable by accident.

**Pre-registered as insufficient on its own: stars.** Per `../../../docs/findings/market-gaps-2026.md:93`, engagement counts are visibility proxies, not demand measurements. The unprompted-paid-ask count is the binding half. 500 stars with zero paid asks is a **stop**, not a proceed, and that is written down now so it cannot be renegotiated later.

**What the test does not test, stated now.** It measures whether this team can get distribution and whether free users convert to askers. It does not test whether the supervision-layer premise is right; §§2-4 already answered that. A pass would mean *this team can reach developers*, which is worth knowing for the sibling projects, not *the supervision layer is a business*.

**The tone hypothesis does not die with the project.** It was never tested, it is the user's stated intent, and it is a property of the collaborator's craft rather than of this product. It travels to whichever project ships an output with a voice, and it is still owed the cheapest possible test: one artifact, published, in the register, measured on whether a stranger shares it. That test was never designed here and is not designed here.

**Revival conditions independent of the test above.** Any one of these re-opens the question:

| Condition | Why it would change the verdict |
|---|---|
| A dated, disclosed-traction, recurring-revenue agent-supervision tool appears | The repo has zero such data points today |
| Anthropic removes `claude -p` from subscription limits | Repriced substrate; the 2026-06-15 withdrawal says this is live |
| A non-technical buyer channel opens that needs no field sales | Closes `pass3-read.md`'s empty column |
| Braintrust Patterns is confirmed to close cluster→generated-tool | Would settle C negatively for good; a day's work, still unrun |

---

## 6. What wave 2c would design

**There is nothing for 2c to design.** 2b's §8 constraints rule out the competitor-price watcher and reduce H to one function. This wave reduces the same function to single-digit demand, a `not_planned` closure on its enabling primitive, and a one-quarter observed vendor absorption time. 1e removes the last reason to design anything cost-shaped: the free per-task primitive C, F and H(d) were built on does not exist.

If the user overrules the stop, 2c's scope is exactly §5 — the deferral governor, alone, free — and its single design decision is now answerable rather than blocked: headroom is not readable headlessly, so the governor accumulates `total_cost_usd` per invocation against a ceiling the user sets, and never claims to know the subscription window. That is one afternoon of design, not a wave.

---

## Caveats

- `../explore/telemetry-measured.md` is one machine, one version (v2.1.259), one auth mode (interactive OAuth), four invocations. It settles the yes/no it was asked (reproduced twice, plus the subagent case); it does not characterise every hook event, and API-key/`--bare` payload shape was not tested. Its OTel claims are untested — no collector was stood up — so `../explore/task-telemetry.md`'s OTel schema remains doc-sourced and is a distinct mechanism from hooks.
- Nothing in §4's recommendation turns on the telemetry result. It made C and F worse; the binding gate was and remains demand, not feasibility. A reader should not read the stop as caused by a missing field.
- GitHub `total_count` counts a title substring, not a curated request. This applies to the eleven-topic comparison in §3 as much as to 2b's 828. The defensible claim is the 0.88% ratio and the direction, not a precise rank.
- The eleven comparison topics were chosen by this agent, not sampled randomly. A different eleven gives a different ordering.
- The five-group taxonomy of the 57 `enhancement` issues is this agent's grouping; the titles quoted are verbatim, the groups are inference.
- No issue body was fetched by this wave. 2b's relayed body quotes are not re-verified here and are not relied on.
- Reddit was not attempted by this wave. Three prior passes in this repo failed on it (`../review/market-check.md` §3). Every demand negative here inherits that weakness; H's positive signal does not, having been reached at full volume on GitHub.
- §4's case-against is argued at full strength on purpose and is not defeated by the recommendation; a reader who weights unexamined optionality higher than I do should reach the opposite conclusion from the same evidence.
- Per `../../../CLAUDE.md`, the verdict is the user's. This file recommends; it does not decide.
