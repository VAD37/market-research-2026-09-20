# REPORT-PLAN — what `REPORT.md` must contain and how it must be built

2026-09-18. Stage 3.5 of `projects/investment-review/` (`ORCHESTRATION.md` §"Investment review, stage 2"). Governs the final `REPORT.md`, written AFTER the per-project reviews (`<project>.md` per `FRAMEWORK.md` §D) and before or alongside `PORTFOLIO.md`.

This file plans. It reaches no verdict on any project; that is the reviews' job and the report's.

It answers the user's ask verbatim: *"make a plan on what is a good report on proposal and market understanding, problems, solution, competitor, and then what are our open proposal and its pro/cons, time estimate and difficulty — then write that report."* Sections (b)–(e) are market, problems, solution, competitor. Sections (f)–(g) are open proposals with pro/cons, time and difficulty.

---

## 1. Purpose and reader

`REPORT.md` is a decision document for the founder first and an investor second. The founder is a solo technical builder in Ho Chi Minh City with a clinic-admin MCP side business, an RTX 3060 Ti, a Claude Code subscription and Chrome; he has said the earlier research passes were wishful thinking and has asked for real numbers. The investor reader is hypothetical and secondary: the report must survive being handed to one, which is why every figure carries a source kind and every estimate carries a band — but it is not written to raise money, and nothing in it may be shaped to be fundable. **The one decision it must enable: for each of the three prototypes, and for the portfolio as a whole, decide how many of the founder's own hours and how much of his own cash to commit in the next 90 days, and at what dated, pre-registered signal to stop.** It is not asked whether any of these is a good business in the abstract; it is asked what the next 90 days are worth against the founder's next-best use of the same hours.

---

## 2. Section skeleton for `REPORT.md`

Ten sections, this order, headings verbatim. Sections may be added; none removed. Length caps are hard — a section over cap is compressed, not extended.

### (a) Executive verdict

**Question.** Per project: commit, gate, or stop — and at what number does that flip?

**Evidence.** The three review files' §10 verdict paragraphs and §1 header tables (`projects/investment-review/<project>.md`). Every KILL row (A3 willingness to pay, A6 incumbent coverage, A10 real-input proof) carried forward with the PASS/FAIL/UNKNOWN the review set. No number appears here that is not already in a review's §1.

**Length.** Three-row table plus ≤120 words. Columns: project | KILL status A3/A6/A10 | verdict in the §D10 form | the one number that flips it | date the gate expires.

**Wishful-thinking test.** A row reading "commit" while any of its three KILL cells reads FAIL or UNKNOWN is wrong — §D1 caps that verdict at "gate first" or "stop", and §E forbids a score outvoting it. If all three rows say the same thing, check whether the writer compared the projects or flattened them.

### (b) Market understanding

**Question.** Who buys, how many by name, what do they pay today for the nearest thing, and does the bottom-up arithmetic clear the founder's opportunity cost?

**Evidence.** `raw/c1-pulls-2026-09-18.md`, `c2-`, `c3-`, `c4-` (buyer counts, vendor prices, salary and contract bands); `FRAMEWORK.md` §A2, §A4, §A5, §B5; each review's §5 arithmetic block; `../ai-attack-defense/docs/customers/hcmc-candidates.md` for the 8 named HCMC companies; `../../docs/customers/first-customers.md` for channel reply rates. Opportunity cost from `raw/c4-*` per §B14: the higher of clinic-MCP revenue per hour or the HCMC AI-engineer band.

**Length.** Three arithmetic blocks in the §D5 code-block form, one per project, plus ≤400 words. One shared opportunity-cost block, stated once.

**Wishful-thinking test.** Gartner / Mordor / Grand View TAM is inadmissible (§B5) — the repo already holds 8× and 5× disagreements on the same base year. `N_buyers` must be a count of named entities from a directory, register or crawl, not a persona or a category. If any input is `unknown`, the ratio is `unknown` and the section says so rather than substituting a placeholder. A US price band transplanted to Vietnam (the $8k–$50k figure, `evidence-rules.md` rule 2) appears only to be rejected.

### (c) Problems

**Question.** What problem does each project claim, what evidence exists that it is real, how severe and how frequent, who suffers it, and what do they do instead today?

**Evidence.** Each problem statement cited to its own file: `ai-ads-injection/docs/outcome/positioning.md`; `agent-hermes-dashboard/CLAUDE.md` plus `docs/plan/re-pick.md`; `ai-attack-defense/docs/plan/niche-and-solutions.md` plus `docs/outcome/success-vision.md`. Severity and frequency from `raw/c*-pulls` thread, forum and job-post counts, each with its denominator. `FRAMEWORK.md` §A1, §B1. `../../docs/findings/pass4-read.md` cross-read point 2 for the standing fact that no buyer has been contacted by any pass.

**Length.** One table, three rows, six columns: project | problem as the doc states it | evidence it is real, with denominator | frequency per sufferer | who suffers, named | what they do today. Plus ≤300 words. Cells 12 words.

**Wishful-thinking test.** A GitHub issue count without a denominator is inadmissible — 828 of 93,582 is 0.88%, last of 11 topics sampled (`agent-hermes-dashboard/docs/plan/re-pick.md`). A vendor survey selling the fix is inadmissible. "Nobody has built this" is not a problem statement (§F2). If a "what they do today" cell reads "nothing", check whether the real answer is "the problem is not felt" — `ai-attack-defense/docs/outcome/success-vision.md` §4 already says the Vietnamese check has no manual process to automate, which is an absence, not a workflow. The severity column is an observation about humans, not about software.

### (d) Solutions

**Question.** What does each MVP do today, measured, and which claims are proven versus asserted?

**Evidence.** `FRAMEWORK.md` §D2 and §D3. Per project: `docs/execution/e2e-test.md`; `docs/outcome/review.md` — exists for ads and attack-defense, **absent for hermes, whose 9a review was stopped before writing**, and the report says so rather than filling the hole; `ai-attack-defense/docs/outcome/parity-report-2026-09-18.md` for the five-guardrail table; §8 of this plan for code size and test counts.

**Length.** Two tables. Table 1, three rows: project | one command | measured wall-clock | tally | real-input result or `never run on real input`. Table 2, two columns per project: Proven (reproduced from clean, or run on real input) versus Asserted (in a spec, page or vision doc only). Plus ≤350 words.

**Wishful-thinking test.** Every number carries `fixture` or `real` beside it (§F8), and a `fixture` number may not appear in sections (a), (b) or (g). Barred from appearing as real: the ads 25-of-155 spoof rate, the parity-vi 8.2→17.8 pp fixture gap, the Foreman 7× chore. For every "X cannot happen" claim on a page or in a README, name the input that makes X happen and whether a test reaches it — this session produced five instances of that bug class (ads S1/S1b; Foreman `_log_failure`; parity-vi no-network-by-grep; parity-vi S1 indeterminacy gate), and a sixth going unnamed is the expected failure.

### (e) Competitors

**Question.** Per project: who already ships this, what do they say they cover in their own words, what do they charge, and what is left over?

**Evidence.** `FRAMEWORK.md` §A6 (KILL), §B6, §D4. `raw/c1-`, `c2-`, `c3-pulls-2026-09-18.md` for first-hand inspections. Each project's `docs/review/market-check.md` for the incumbent roster and the kill lines already run.

**Length.** One table per project, ≤8 rows, five columns: incumbent | version and date inspected | how inspected (run / docs only / not inspected) | its own sentence on the gap | price. Plus ≤250 words across all three.

**Wishful-thinking test.** The "how inspected" column is the point (§F6). `not inspected` is an A6 FAIL; `docs only` on a primary incumbent is an A6 UNKNOWN. As of 2026-09-18 the never-inspected primaries are GoAccess, AWStats, Matomo (ads) and Claude Code `/insights`, Braintrust Patterns (Foreman); promptfoo is docs-only for parity-vi. If the stage-2 pulls closed any of these, the row says so with a date; if not, the row says `not inspected` and the KILL stands. A gap stated in the report's words rather than the incumbent's is not evidence. "Free" is a price: write `$0` with the tier and its limit (Azure F0 5,000 records/month; OpenAI moderation; Known Agents $0).

### (f) Open proposals

**Question.** What are all the paths forward, per project and across the portfolio, and what does each cost and kill?

**Evidence.** Every candidate traces to a document that already proposes it, or is marked `new — proposed by this report` and justified. Floor set — each must appear, or be dismissed in one line with a reason:

| Project | Proposals that must be listed |
|---|---|
| `aicrawlcheck` | stop and archive; publish repo plus one real-log run and a post; check GoAccess/AWStats/Matomo then upstream PR; run the 20-org probe at 15.000.000 VND; free instrument plus paid audit service; pivot to Vietnamese answer-visibility measurement (C6); open-source and walk |
| `Foreman` | stop, close for good per the gate wording; build `scan --from-history` then publish; publish MIT and run the 14-day gate; inspect `/insights` first and let it decide; free instrument plus services; keep the voice asset only; open-source and walk |
| `parity-vi` | stop, keep as calling card; finish the `wave10b-s18` stash, publish repo and report; run one commercial endpoint then publish; run the HCMC 14-day gate on the 8 named companies; free instrument plus paid engagement; train a Vietnamese moderation classifier; open-source and walk |
| Cross-project | stop all three, return to clinic-MCP; merge into one honest-measurement service with the three tools as instruments; publish the method itself (`MVP-MANDATE.md` plus `evidence-rules.md`) as the reputation asset; sequence at the 70/20/10 split; hold all three as calling cards and take contract work |

Sources: `projects/SUCCESS-VISION.md` (ranked recommendation, the fourth-thing question, the 70/10/20 split); each `docs/outcome/success-vision.md` §7 gap list; each review's "Is this enough?" ranked list; `../../docs/findings/cross-read.md` pattern 3 (services at n=1).

**Five required fields per proposal.** Pros (§4), cons (§4), prerequisites (what must be true or bought before the first hour), kill signal (dated, numeric, pre-registered — §A14, §B14; a rule written after the data is inadmissible), and "what we would have to believe" (§4).

**Length.** One block per proposal, ≤60 words plus its assumption list. ≤900 words total. If the count pushes past the cap, merge the weakest — never drop the stop option.

**Wishful-thinking test.** "Stop" appears as a real option for every project with its own pros filled in, not as a strawman (§6 check 4). A proposal whose kill signal is "we'll see how it goes", or whose prerequisite list is empty, is not a proposal. A proposal requiring the founder to do something no document shows him doing — selling, invoicing internationally, hiring — says so in its prerequisites and scores 4 or 5 in section (g).

### (g) Time estimate and difficulty

**Question.** Per proposal: how many agent-runs, how many wall-clock hours, how many founder hours, how much cash, and how hard — with the reference class named?

**Evidence.** §3 of this plan (method) and §8 (reference class). No other source of throughput figures is permitted.

**Length.** One table, one row per proposal from section (f), eight columns: proposal | task count | agent-runs [band] | wall-clock hours [band] | founder hours [band] | cash | difficulty 1–5 | what makes it that number. Plus ≤400 words on the two or three widest bands and why.

**Wishful-thinking test.** A point estimate anywhere in this table is a defect — every number is a band (§3.4). A difficulty score without a cited precedent or cited absence is a defect. A row whose founder-hours figure equals its wall-clock figure has confused agent time with human time; §8 separates them. Any human sales task estimated under two hours is checked against the §3.3 anchors.

### (h) Recommendation

**Question.** Given the above, what should the founder do in the next 90 days, on what assumptions, and what single number flips it?

**Evidence.** Sections (a)–(g) only. The §D8 three-scenario EV tables from each review (do nothing / minimum viable commitment / full commitment), the founder opportunity cost from §B14, and the ranking rule from `FRAMEWORK.md` "How to use" step 4: **rank by EV at minimum commitment, not by §E score.**

**Length.** ≤450 words. Must contain a numbered assumption list, each marked `measured` / `sourced` / `own judgement`, and a named flip number per project: "if X is below or above N, this changes to Y".

**Wishful-thinking test.** If no assumption is marked `own judgement`, judgement has been disguised as evidence. If the recommendation is insensitive to every input, it was not derived from the arithmetic. A negative EV in a full-commitment row is a finding to state, not a formatting problem to fix (§D8). The recommendation survives the §6 checks, and the report names which check it came closest to failing.

### (i) Caveats and unverified claims

**Question.** What could this report not do, and which claims in the projects' own docs are unverified or contradicted?

**Evidence.** Each review's §11 and §12, merged and deduplicated. Every `requires-human` line from `FRAMEWORK.md` §C still unrun. Every `unknown — checked <channel> <date>` that a section above depends on.

**Length.** One table: file:line | claim | status (`unverified` / `contradicted by <what>`) | which section it affects. Plus ≤350 words of narrative caveats.

**Wishful-thinking test.** The standing portfolio-level facts appear here unsoftened: no buyer has been contacted by any pass in any project; no commercial guardrail endpoint has been run; `/insights`, GoAccess, AWStats and Matomo have never been opened; the Foreman 9a review was stopped before writing, so no review verdict exists for that project; twelve agents' `STATE.md` appends were lost on 2026-09-18 and `ORCHESTRATION.md` is authoritative for that span. If this section is shorter than section (h), the report is selling.

### (j) Sources

**Question.** Where did every number come from?

**Evidence.** One row per source actually cited in (a)–(i): path | what it supplied | pull or write date | label kind. `raw/` files and primary URLs for numbers; project docs for claims about the projects themselves.

**Length.** Table only. No prose.

**Wishful-thinking test.** Every number in the report resolves to a row here. A compiled file citing another compiled file's conclusion breaks `evidence-rules.md` rule 3 and §F7 — the row names the `raw/` file or primary URL underneath. A section citing a source absent from this table means one of the two is wrong.

---

## 3. Time-estimate method

The report does not guess hours. It derives them.

### 3.1 Procedure, per proposal

1. **Decompose** into tasks. One task = one deliverable file or one tight cluster, one question, one done condition (`ORCHESTRATION.md` §"Task sizing"). The task count is a reported column.
2. **Classify** each task: `agent-executable`, `human-only`, or `blocked` (needs something that does not exist yet — a repo URL, an account, a reply).
3. **Match** each agent-executable task to a reference row in §8 and state the multiplier and the reason. Form: `1.5× the parity-vi packaging lane — new config files over an existing CLI, one more adapter`.
4. **Price** human-only tasks from the §3.3 anchors, each labelled `own judgement` with its anchor named.
5. **Report three quantities separately, never summed into one:** agent-runs, wall-clock hours, founder hours. Wall-clock is not founder time — the founder's cost is scheduling, review and commits.
6. **Band** every quantity (§3.4).
7. **Blocked** tasks get `unknown — blocked on <what>, checked 2026-09-18` and are excluded from the total, which is then stated as a floor.

### 3.2 Units

`agent-runs` = discrete agent spawns, counted as in §8. `wall-clock hours` = elapsed from first spawn to last landing for that proposal's tasks, agents concurrent where the cap allows (10 Sonnet / 2 Opus / 1 Fable, `ORCHESTRATION.md` 2026-09-18; browser and GPU remain single resources and serialize). `founder hours` = the founder's own attention — prompt-writing, reading landings, committing, plus every human-only task. `cash` = VND or USD with the vendor named.

### 3.3 Human-only task anchors — all `own judgement`, anchor named

| Task | Duration [low, likely, high] | Anchor |
|---|---|---|
| Create one vendor account, first API call | 1 h [0.5, 1, 3] | `ai-attack-defense/docs/outcome/review.md` item 4: "a user sign-up plus an hour" |
| Publish a public repo: licence, README, release post | 2 h [1, 2, 6] | `agent-hermes-dashboard/docs/outcome/success-vision.md` §7 item 7: "an hour of hygiene" |
| Replace page placeholders (mailto, repo URL) | 0.5 h [0.25, 0.5, 1] | parity-vi 9b addendum: "Minutes, once a URL exists" |
| One scheduled buyer conversation: prep, meeting, follow-up | 3 h [2, 3, 6] | no precedent in this repo; pure own judgement — say so |
| Outreach round: 20 named orgs, one follow-up, decision day 7 | ≤5 working days | `../../docs/findings/pass4-read.md`, ads probe continuation cost |
| Outreach round: 8 named orgs, HCMC, 14-day gate | 14 calendar days; founder hours counted separately | `ai-attack-defense/docs/outcome/hcmc-opener-2026-09-18.md` §4 |
| Waiting out a pre-registered gate | 14 calendar days, 0 founder hours | both gates, as written |
| Contract, invoicing, receiving money from Vietnam | `unknown — not attempted` | `FRAMEWORK.md` §C4 line 9 — MoR onboarding is documentation-only status; do not guess |

**Reply-rate arithmetic is mandatory wherever a proposal depends on replies.** Benchmarks, all `vendor-reported`: cold email 3.43% platform-wide (Instantly 2026, billions of emails); cybersecurity 4.86% (Belkins 2025, 16.5M emails, 93 industries); LinkedIn DM 10.3% (Expandi, H1 2025, 70,130+ campaigns). At a frozen list of 8 names and 10.3%, expected replies is under 1 — so any proposal needing ≥3 replies from that list must either widen the list or name in-person or warm-intro as the channel, and show that arithmetic rather than asserting reachability.

### 3.4 Confidence bands, not points

Every estimate is `[low, likely, high]`. Two rules:

- The band's width is at least the observed spread of its reference class. §8.3 shows same-class GPU lanes spanning 28 s to 52 m on identical input — 112×. A band narrower than its reference class's spread is a defect.
- `high` includes at least one named failure mode from that proposal's con list. A high estimate that assumes nothing goes wrong is not a high estimate.

Stopped-run overhead is a measured input, not a hedge: 8 of roughly 55 runs this session were stopped mid-work or by the concurrency cap, and 3 never produced their deliverable (§8.5). Any plan running more than four agents carries that rate explicitly.

### 3.5 Difficulty — 1 to 5, rubric

| Score | Meaning | What must be cited |
|---|---|---|
| 1 | Done before in this repo, more than once, with an artifact to point at | The artifact, and its commit or §8 row |
| 2 | Same class as done work; new substrate or new tool, documented | The nearest done artifact, and the one thing that differs |
| 3 | Uses a resource this repo has but never at this scale, or a human step with a known script | The resource, and why the scale or the human step is new |
| 4 | Needs a capability demonstrated once and unreliably, or a human skill the founder has not exercised in this repo | The one demonstration and why it is not repeatable, or the named absence |
| 5 | Needs a capability neither the founder nor the agents have demonstrated at all | The named absence, and what evidence would move it to 4 |

Every score cites what makes it that number, in the section (g) cell. Worked anchors the writer may reuse: another offline CLI subcommand with tests = **1** (43 tests, 27 lanes precedent); a new HTTP adapter against a documented moderation API = **2** (`http_json` adapter exists, worked examples landed `12811f1`); running a commercial endpoint for the first time = **3** (account creation is a new human step; the run path is proven); one buyer conversation = **4** (no buyer contacted by any pass, any project, ever); training a Vietnamese moderation classifier = **5** (excluded by `ai-attack-defense/docs/outcome/success-vision.md` §7 as wrong skill, 10–16 weeks); a hosted multi-tenant product with billing from Vietnam = **5** (no rail onboarded; Stripe does not support Vietnam, confirmed 2026-06-16, `pass3-read.md`).

---

## 4. Pro/con discipline

**A pro cites a number or an artifact.** Form: `<claim> — <number or artifact> [<label>, <file>]`. A pro with no citation is deleted, not softened. "Strong", "compelling", "significant", "large", "fast", "cheap", "unique" are banned without a referent — replace the adjective with the number, or cut the line. A `fixture`-derived number may not be used as a pro.

**A con names the failure mode and the earliest signal of it.** Form: `<failure mode> — earliest signal: <observable>, by <date or event>`. "Risk" and "might not work" are not failure modes. A con is complete only when someone could notice it happening.

**Every proposal carries "What we would have to believe".** A numbered assumption list, each marked:

- `measured` — a number this repo produced by running something, with the run record in `raw/` or `docs/execution/`.
- `sourced` — a number from outside, with vendor, URL and date, labelled by kind.
- `own judgement` — neither. Probabilities, attainable shares and every duration in §3.3 are `own judgement`, stated as numbers, not adjectives.

A proposal whose assumption list is entirely `measured` is mislabelled: every money assumption in this portfolio is `own judgement` as of 2026-09-18, and hiding that is the failure this report exists to prevent.

---

## 5. Numbers policy

Repo rules, in force unchanged:

- Every number carries a source kind: `vendor-reported`, `analyst-derived`, `filed`, `company-stated`, `measured-by-us`, `requires-human`, `own judgement`, or `unknown — checked <channel> <date>`. A number without a label is not a number (`FRAMEWORK.md` preamble).
- Absolute dates. "As of 2026-09-18", never "recently" or "this year".
- `unknown — checked <channel> <date>` beats a guess.
- Conflicting figures sit side by side, attributed, never averaged — and the report names which conclusion is sensitive to which of the two (§F11).
- Table cell: 12 words. A cell wanting a paragraph means the paragraph belongs in `raw/` and the cell carries the number.
- Every compiled section carries its caveats; section (i) is where they collect.

Added for this report:

- **The report introduces no figures.** Any number in `REPORT.md` must already appear in a `projects/investment-review/raw/` file, a per-project review, or a project document — and the citation names which. A number appearing for the first time in the report is a missing pull; the fix is to pull it, or to write `unknown — checked <channel> 2026-09-18`. Never to estimate it.
- The one exception is arithmetic *over* cited numbers — a ratio, a sum, an EV — which shows its inputs inline so the reader can change one and recompute (`FRAMEWORK.md` "How to use" step 3).
- Throughput and effort figures come only from §8 of this plan.

---

## 6. Anti-bias checks — run before finishing, recorded in the report

The writer runs all five and records each result in one line at the end of section (h).

1. **Sunk cost.** Three days of agent work is not evidence. Re-read every pro in section (f): if its force comes from work already done rather than from a buyer, a price or a measurement, cut it. Test: would this proposal be attractive if the prototype did not exist and had to be built from zero? If no, the proposal's value is the code, and the report says so.
2. **Narrative fit.** The session has a good story in it — the bug class found five times, the DNA of three audit instruments, the honest-measurement-service idea arriving from a fourth direction. A good story is not a market. Test: for each claim that fits the story, name the evidence that would have contradicted it, and whether anyone looked.
3. **`FRAMEWORK.md` §F traps, all twelve.** One line each: check run, result. F1 search-level negative read as demand; F2 "no one has built this"; F3 safety asserted where it cannot fail; F4 benchmarks scored on models not guardrails; F5 stars mistaken for demand; F6 incumbents never inspected first-hand; F7 compiled citing compiled, hedge dropped in transit; F8 fixture number leading; F9 law read as demand; F10 vendor numbers read as independent; F11 averaging conflicts; F12 relative dates and unlabelled runtimes.
4. **Steelman the stop option, per project.** For each of the three, write the strongest honest case for stopping — in its own voice, with its own numbers, at the same length as the strongest case for continuing. The stop case includes what the founder gets back (hours, at the §B14 rate) and what he keeps (the code, the method, the calling card, and what that is worth in hours). A stop case shorter or weaker than its continue case is a failed check, and the writer redoes it.
5. **Opportunity cost, stated once, applied everywhere.** Every EV in section (h) nets out the founder's next-best use of the same hours. If the clinic-MCP revenue-per-hour figure is `requires-human` and unfilled, the report states the EV as `unknown` and gives the break-even hourly rate instead — the rate at which the recommendation flips.

---

## 7. Writer brief

Give the writing agent this block verbatim.

> **Task.** Write `projects/investment-review/REPORT.md` per `projects/investment-review/REPORT-PLAN.md`. Follow that plan's section skeleton exactly: ten sections, the order given, headings verbatim, every length cap hard.
>
> **Read first, in this order.**
> 1. `CLAUDE.md` (repo root), `projects/CLAUDE.md`, `projects/MVP-MANDATE.md`
> 2. `projects/investment-review/REPORT-PLAN.md` — §2 skeleton, §3 time method, §4 pro/con, §5 numbers, §6 checks, §8 reference class
> 3. `projects/investment-review/FRAMEWORK.md` — criteria A1–A14, §B definitions, §D template, §E scoring, §F traps
> 4. The three per-project reviews: `projects/investment-review/ai-ads-injection.md`, `agent-hermes-dashboard.md`, `ai-attack-defense.md`
> 5. `projects/investment-review/raw/` — every file, for the numbers
> 6. `projects/SUCCESS-VISION.md`, then each project's `docs/outcome/success-vision.md`
> 7. `projects/ORCHESTRATION.md` from §"Investment review" onward, for what stands today
> 8. Only as needed for a specific claim: each project's `docs/review/market-check.md`, `docs/plan/re-pick.md`, `docs/outcome/review.md`, `docs/execution/e2e-test.md`
>
> **Output.** `projects/investment-review/REPORT.md`. One file. Write nothing else. Do not run git.
>
> **Length.** 3,500–4,000 words including tables. Over cap, compress; do not extend.
>
> **Formatting.** Tables for anything parallel across the three projects or across proposals. Table cells 12 words maximum. No heading deeper than `###`. Absolute dates only. Every number labelled by kind. Code blocks for arithmetic in the `FRAMEWORK.md` §D5 form, inputs shown so one can be changed and recomputed. No emoji.
>
> **Hard rules.**
> - Introduce no figure that is not already in `raw/`, a review file, or a project doc. Cite which, per number.
> - Never average conflicting figures; place them side by side and say which conclusion is sensitive to which.
> - `unknown — checked <channel> 2026-09-18` beats a guess, everywhere, including in the estimate tables.
> - Every time estimate is a band `[low, likely, high]`, never a point, and names its reference row from `REPORT-PLAN.md` §8.
> - Every difficulty score is 1–5 per the §3.5 rubric and cites what makes it that number.
> - Every pro cites a number or artifact; every con names a failure mode and its earliest signal; no adjective without a referent.
> - Every proposal lists "what we would have to believe", each assumption marked `measured` / `sourced` / `own judgement`.
> - Throughput figures come only from `REPORT-PLAN.md` §8. Nowhere else.
> - A `fixture` number may not appear in sections (a), (b) or (g).
> - A KILL row (A3, A6, A10) at FAIL or UNKNOWN caps that project's verdict at "gate first" or "stop", regardless of any score.
> - The decision is the founder's. The report states the evidence, the arithmetic and the flip number, and may recommend — it may not decide.
>
> **Self-check before returning. Answer each in one line at the end of your final message, not in the file.**
> 1. Does every number in the file resolve to a row in section (j)? Name any that does not.
> 2. Is there a point estimate anywhere in section (g)? If yes, fix it.
> 3. Does every difficulty score cite a precedent artifact or a named absence?
> 4. Does every proposal in section (f) have all five fields — pros, cons, prerequisites, kill signal, what-we-would-have-to-believe?
> 5. Is "stop" present for all three projects with real pros, at the same length as its continue case?
> 6. Are all twelve §F traps checked and recorded?
> 7. Does any verdict in section (a) exceed what its KILL rows allow?
> 8. Is section (i) longer than section (h)? If not, what did you leave out?
> 9. Any adjective without a referent? Any relative date? Any unlabelled number?
> 10. Word count, and which section you compressed to hit it.

---

## 8. Reference-class table — extracted 2026-09-18

**This is the only place `REPORT.md` may take throughput figures from.** All rows `measured-by-us`, from `projects/ORCHESTRATION.md` sections named per row, each project's `STATE.md` entry headings, and file counts run on this machine 2026-09-18. `STATE.md` appends from twelve agents were lost on 2026-09-18 and partially recovered; `ORCHESTRATION.md` is authoritative for that span.

### 8.1 Per project

| | `aicrawlcheck` (ai-ads-injection) | `Foreman` (agent-hermes-dashboard) | `parity-vi` (ai-attack-defense) |
|---|---|---|---|
| Agent runs, total | 14 | 14 | 27 |
| Of those, stopped incomplete | 2 — e2e cap-stop; wave 10 fix mid-run | 3 — e2e cap-stop; sales page cap-stop; 9a review never written | 3 — wave 10 real-input setup only; 10b code fix; report review never written |
| Wall-clock span | 2026-09-17 scaffold → 2026-09-18 stop | 2026-09-17 scaffold → 2026-09-18 stop | 2026-09-17 scaffold → 2026-09-18 11:42+07:00 |
| Explore → page → vision, elapsed | one calendar day, 2026-09-17 | one calendar day, 2026-09-17 | two calendar days, 2026-09-17..18 |
| Prototype Python, modules | 1,640 lines, 9 modules | 1,618 lines, 12 modules | 3,921 lines — `harness/` 3,244 plus `parity.py` 677 |
| Prototype Python, other | fixtures 296; offline harness 73 | `foreman_hook.py` 25 | tests 828; total non-venv 4,864 |
| Sales page | `site/index.html` 855 lines | 1,175 lines | 923 lines |
| Tests | `selftest` 18/18 assertions; **no unit suite below CLI** | 19 test functions, 19/19 in 0.033 s | 43 test functions across 7 files |
| e2e acceptance | 24/31 PASS, 7 NOT COVERED | 20/20 in scope, 11 NOT COVERED | every pre-registered number reproduced from clean |
| Measured on REAL input | **none for the product's moment** — never run on a real access log | partial — `~/.claude/history.jsonl` 3,103/3,103 parsed, 5 keys; recurrence never saw a real ledger; live `Stop` hook never observed | **yes** — 5 open-weights guardrails, 600 prompts each, CUDA, 2026-09-18 |
| Other real measurements | rDNS 20 addresses sampled; `refresh --dry-run` 5.668 s live network | SHA-256 of `settings.json` byte-identical before and after | Granite 3.0→3.1 `diff`: REGRESSION, exit 1, +21 new VI misses |
| Headline fixture wall-clock | 0.936 s cold; 0.391–0.417 s warm, 420 lines | 0.365 s, full six-section report | 1.312 s demo path, restated 1.4 s post-fix |
| Commits named | spec `d23d806`; e2e `4373c3a`; page `fb561df`; 9a review `3bdac7e`; stop `f9f9a98` | spec `61f08ab`; build `0e262eb`; e2e `8aaac10`; page `b8d17c8`; vision `b7037ed`; stop `44156ab` | spec `587c3ff`; build `db2ae18`; e2e `589e1ab`; real run `a241740`; 9a `f25f274`; code fix `b3083bd`; page `1baacca`; sweep `39d4454`; 9b `572a211`; page fix `bd74ad9`; report `de8f467` |
| `ORCHESTRATION.md` sections | Waves 1, 2, 5, 6, 7/8; §"Wave 9a — ads review landed"; §"Wave 10 started early on ads" | Waves 1, 2, 5, 6; §"Wave 8 complete on hermes"; §"Wave 9a on hermes spawned" | Waves 1, 2, 5, 6, 9V; §"SESSION 2026-09-18"; stages 1–2; §"Sweep landed"; §"Page fixed, report drafted" |

### 8.2 Single-lane wall-clocks, measured 2026-09-18 (`ai-attack-defense/STATE.md`, timestamped entries)

| Lane | Elapsed | Note |
|---|---|---|
| Real-input agent — adapter, 600-prompt run, clean re-verify | 00:00Z PLAN → 02:56Z ALL TASKS DONE ≈ 2 h 56 m | contains a 15m08s GPU run |
| Guardrail sweep — 4 more models plus version diff | 09:54 → 11:20 +07:00 = 1 h 26 m | GPU serialized, single resource |
| Sales page (Fable), recovered entry | 11:30Z → 11:50Z = 20 m | data-driven from `site/*.json` |

### 8.3 GPU task spread — same task class, identical input, 600 prompts, 2026-09-18

| Model | Wall-clock |
|---|---|
| Detoxify multilingual | 28 s |
| Granite Guardian 3.1-2b | 3 m 59 s |
| Granite Guardian 3.0-2b | 4 m 01 s |
| Qwen3Guard-Gen-0.6B | 15 m 08.321 s |
| Qwen3Guard-Gen-4B | 52 m 06 s |

Spread within one task class: 112×. This is the floor for band width on any GPU-bound estimate (§3.4).

### 8.4 Human interventions in the session — 12 recorded, all `ORCHESTRATION.md`

Model policy (2026-09-17); task sizing (2026-09-17); build-phase directive "run unattended" (2026-09-17); concurrency cap 3 (2026-09-17); browser and container grant (2026-09-17); hosting grant (2026-09-17); mandate change, success vision precedes planning (2026-09-17); Chrome extension enabled mid-run (2026-09-17); single-project directive, parity-vi (2026-09-18); cap change to 10 Sonnet / 2 Opus / 1 Fable (2026-09-18); "stop all task and agents" (2026-09-18); investment-review directive and the report ask (2026-09-18).

Project-specific human interventions: ads 0, hermes 0, parity-vi 1 — the single-project directive that made it the only project worked on 2026-09-18. **Human interventions that contacted a buyer, priced anything, or moved money: 0, all projects, all passes.**

### 8.5 Rates the report may derive from this table

- Prototype Python per project, built and tested in one to two calendar days: 1,618–3,921 lines.
- Agent-runs to reach prototype plus e2e plus sales page plus vision doc: 14 per project.
- Additional agent-runs to reach one real-input measurement, a publishable report and a fixed page: +13 (parity-vi, 2026-09-18).
- Observed stopped-run rate: 8 of roughly 55 runs stopped mid-work or by the cap; 3 never produced their deliverable.
- **Founder hours are not in this table and cannot be derived from it** — no `STATE.md` or `ORCHESTRATION.md` entry records founder attention time. Any founder-hour figure in `REPORT.md` is `own judgement` and says so.

---

## Files read

Root: `CLAUDE.md`; `docs/CLAUDE.md`; `docs/findings/cross-read.md`, `pass2-read.md`, `pass3-read.md`, `pass4-read.md`, `market-gaps-2026.md`, `two-founder-cases.md`, `localization-play.md`, `injection-feasibility.md`; `docs/customers/first-customers.md`; `docs/method/evidence-rules.md`, `scope.md`; directory listings of `docs/markets/` and `docs/method/`.

Projects layer: `projects/CLAUDE.md`; `projects/MVP-MANDATE.md`; `projects/SUCCESS-VISION.md`; `projects/ORCHESTRATION.md` (whole, 924 lines); `projects/investment-review/FRAMEWORK.md` (whole, 354 lines).

`projects/ai-ads-injection/`: `CLAUDE.md`; `docs/plan/idea-set.md`, `re-pick.md`; `docs/review/market-check.md`; `docs/outcome/positioning.md`, `review.md`, `success-vision.md`; `docs/execution/e2e-test.md`; `STATE.md`; `prototype/` file and line counts; `site/index.html` line count.

`projects/agent-hermes-dashboard/`: `CLAUDE.md`; `docs/plan/idea-set.md`, `re-pick.md`; `docs/review/market-check.md`; `docs/outcome/success-vision.md`; `docs/execution/e2e-test.md`; `STATE.md`; `prototype/` file and line counts; `site/index.html` line count. **`docs/outcome/review.md` confirmed absent** — the 9a review was stopped before writing.

`projects/ai-attack-defense/`: `CLAUDE.md`; `docs/plan/re-pick.md`, `niche-and-solutions.md`; `docs/review/market-check.md`; `docs/outcome/review.md`, `success-vision.md`, `parity-report-2026-09-18.md`, `hcmc-opener-2026-09-18.md`; `docs/customers/hcmc-candidates.md`; `STATE.md`; `prototype/` file, line and test counts; `site/index.html` line count.

Not read, named so the writer knows: `projects/investment-review/raw/` — the stage-2 pulls were still running when this plan was written; the report reads them, this plan could not. Also unread: each project's `docs/design/mvp-spec.md` and `docs/execution/build-log.md`; `ai-attack-defense/docs/execution/sweep-2026-09-18.md`, `real-run-2026-09-18.md`, `fix-log-2026-09-18.md`, `packaging-2026-09-18.md`, `site-log-2026-09-18.md`, `docs/plan/measurement-report.md`; `MegaPlan.md`; `infra/`; any `site/index.html` source.
