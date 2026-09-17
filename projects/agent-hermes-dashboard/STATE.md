# STATE — agent-hermes-dashboard

Append-only running log. Newest entry at the bottom. Write the plan BEFORE the work, the result AFTER it. An agent that dies mid-run must leave its successor enough to continue.

Entry format:

```
## <UTC+7 timestamp> — <agent role> — <phase>
PLAN: what is about to happen
DID: what happened
FILES: paths written
OPEN: what is unfinished, and what the next agent should pick up first
```

---

## 2026-09-17 — main thread — scaffold
PLAN: create project folder, brief, state log.
DID: folder skeleton + `CLAUDE.md` written from `MegaPlan.md` and the three research passes in `../../docs/`.
FILES: `CLAUDE.md`, `STATE.md`, `docs/{explore,plan,design,review,execution,outcome}/`, `raw/`, `prototype/`.
OPEN: explore phase not started.

## 2026-09-17 — explore agent — phase 1 start
PLAN: Read parent CLAUDE.md chain + existing research (docs/markets/agent-dashboard.md, competitors/agent-dashboard-roster.md, raw/agent-dashboard-pulls.md, findings/cross-read.md, findings/market-gaps-2026.md, method/scope.md). Search D:\ai, D:\projects, D:\researchs, home dir for a local Hermes clone. Then produce 5 explore files: hermes-substrate.md, control-planes.md, claude-code-substrate.md, smallbiz-blind-spots.md, task-telemetry.md, each backed by raw/ pulls. Budget WebSearch (may be exhausted); prefer gh CLI / direct fetch for GitHub, WebFetch for docs pages.
DID: Read parent chain + existing docs. Searched D:\ai, D:\projects, D:\researchs, ~ for Hermes — no local clone found (only unrelated D:\hackathon\...\hermes_bridge, ruled out). Fresh-pulled GitHub API for NousResearch/hermes-agent (repo meta, latest release, releases list, root tree, LICENSE, README) confirming pass-1's resolution and adding directory layout + MODEL-vs-FRAMEWORK confirmation. Wrote hermes-substrate.md. WebFetched Anthropic primary docs directly (quickstart, headless, costs, scheduled-tasks, hooks, monitoring-usage/OTel) — got concrete flags/fields including a load-bearing nuance: Agent SDK quickstart restricts OAuth/claude.ai-login use for THIRD-PARTY-PRODUCT resale, but non-bare `claude -p` uses subscription OAuth by default, and OTel telemetry explicitly supports OAuth/subscription login too. Launched 3 background agents in parallel: claude-code-guide (unattended substrate — completed, findings folded in + independently verified against primary docs), general-purpose (control-planes landscape update — pending), general-purpose (smallbiz blind spots — pending). WebSearch not used at all so far (budget preserved).
FILES: raw/hermes-agent-github-2026-09-17.md, raw/claude-code-docs-2026-09-17.md, docs/explore/hermes-substrate.md
OPEN: Write claude-code-substrate.md + task-telemetry.md from raw/claude-code-docs pull (in progress). Wait on 2 pending background agents (control-planes, smallbiz-blind-spots) then write those explore files. Not yet fetched: AGENTS.md/SOUL.md bodies from hermes-agent repo (flagged optional for design phase).

## 2026-09-17 — explore agent — claude-code-substrate + task-telemetry written
PLAN: Turn the raw Anthropic-docs pull into docs/explore/claude-code-substrate.md and docs/explore/task-telemetry.md.
DID: Wrote both files. Key finding surfaced and documented: OAuth/subscription auth splits three ways — plain `claude -p` (non-bare) uses subscription OAuth by default; `--bare` and the Agent SDK require API key (SDK quickstart explicitly restricts OAuth for "third party developers" reselling login, read as not applying to self-use); OTel telemetry explicitly supports OAuth/subscription login per primary docs. This de-risks sub-question 6. Also confirmed concrete per-task telemetry mechanisms (hooks' Stop/SubagentStop cost+duration_ms, StopFailure error_type, OTel claude_code.* metrics/events/beta spans) and confirmed recurring-task detection and fact-staleness are NOT built-in anywhere in the platform — must be designed.
FILES: docs/explore/claude-code-substrate.md, docs/explore/task-telemetry.md
OPEN: Still waiting on 2 background agents (control-planes landscape update, smallbiz-blind-spots). Will write docs/explore/control-planes.md and docs/explore/smallbiz-blind-spots.md once they return. WebSearch quota untouched so far — all research done via WebFetch/gh-API/curl direct fetch.

## 2026-09-17 — explore agent — smallbiz-blind-spots done, hermes AGENTS.md attempted
PLAN: While waiting on control-planes agent, pull Hermes's AGENTS.md/SOUL.md (optional, for design phase persona reference), then write smallbiz-blind-spots.md from the completed smallbiz research agent's report.
DID: AGENTS.md fetch hit GitHub's raw-content rate limit (429) — not retrieved. SOUL.md fetched successfully: Hermes's own persona spec is a direct/no-filler communication style doc, not a "mocking" tone — noted as a data point for the design phase's persona work, not equivalent to the meme "dabs at you" tone the brief wants. Wrote docs/explore/smallbiz-blind-spots.md and raw/smallbiz-blind-spots-pulls.md from the completed sub-agent's report. Strongest sourced finding: SBI 2024 B2B SaaS pricing survey (760 respondents, revenue-stratified) — smallest firms (<$1M ARR) use competitor-pricing 54% vs value-based 20%, inverted at $500M+ firms; explicitly resource-cost-attributed by the source.
FILES: docs/explore/smallbiz-blind-spots.md, raw/smallbiz-blind-spots-pulls.md
OPEN: Still waiting on control-planes-landscape background agent. AGENTS.md body still unfetched (rate-limited, low priority). Once control-planes agent returns: write docs/explore/control-planes.md + its raw pull file, then do a final STATE.md close-out entry and compressed final report.

## 2026-09-17 — explore agent — phase 1 COMPLETE
PLAN: Write docs/explore/control-planes.md + raw/control-planes-pulls.md from the completed landscape agent, then close out.
DID: All 5 required explore/ files written, each backed by a raw/ pull. Explore phase done. Key handoffs for the design (Opus) agent, phase 2:
  1. Hermes = NousResearch/hermes-agent, MIT, FRAMEWORK not model, confirmed fresh 2026-09-17 (was already resolved pass-1, re-confirmed + added directory layout). No local clone exists on this machine — design phase should clone it if it wants to mimic structure. SOUL.md (Hermes's own persona spec) fetched: direct/no-filler style, NOT a mocking tone — different from the brief's "dabs at you" meme framing, worth reading before designing persona.
  2. OAuth/subscription auth for unattended runs is NOT one gate — plain `claude -p` (non-bare) uses subscription OAuth by default; `--bare`/Agent SDK want API key; OTel telemetry explicitly supports OAuth. This significantly de-risks sub-question 6 IF the design stays single-tenant (team's own account, not reselling login to customers).
  3. Concrete telemetry primitives exist (hooks' Stop/SubagentStop cost+duration_ms, StopFailure error_type, OTel claude_code.* schema) but recurring-task detection and fact-staleness are confirmed NOT built into the platform anywhere — must be designed, per brief's own framing.
  4. Sharpest sourced small-business blind spot: SBI 2024 B2B SaaS pricing survey (n=760, revenue-stratified) — sub-$1M-ARR firms use competitor-pricing 54% vs value-based-pricing 20%, inverted at $500M+; resource-cost-attributed by the source itself. Cleanest wedge argument found.
  5. Crowded-lane update: Braintrust shipped "Topics"/"Patterns" (trace clustering for recurring behavior, GA Jun/preview Sep 2026) and LangSmith shipped a fleet-cost-rollup Gateway (Jul 2026) — both incumbent, both developer-facing only. No SMB-targeted agent-supervision product found despite a real search (quota-constrained, flagged as not fully conclusive). OTel GenAI semconv got LESS stable/versioned since pass-1 (moved to an untagged side repo), not more.
  6. WebSearch quota was never touched by this agent directly; two delegated sub-agents used their own WebSearch allocations and both hit intermittent quota/availability issues, noted in their raw files.
FILES (all under projects/agent-hermes-dashboard/): raw/hermes-agent-github-2026-09-17.md, raw/claude-code-docs-2026-09-17.md, raw/smallbiz-blind-spots-pulls.md, raw/control-planes-pulls.md, docs/explore/hermes-substrate.md, docs/explore/claude-code-substrate.md, docs/explore/task-telemetry.md, docs/explore/smallbiz-blind-spots.md, docs/explore/control-planes.md.
OPEN: Explore phase done. Not yet fetched: Hermes's AGENTS.md body (rate-limited by GitHub, low-value, optional). No file written to docs/plan/ or docs/design/ — that's phase 2 (Opus design agent), per the brief's 3-phase structure. Next agent should start there, reading this STATE.md plus all 5 explore files.

## 2026-09-17 — wave 2a (idea + daydream) — phase 2 start
PLAN: Read the CLAUDE.md chain, STATE.md, all 5 files in docs/explore/, spot-check raw/ (smallbiz pricing survey provenance, claude-code telemetry fields), and the read-only research layer (markets/agent-dashboard.md, competitors/agent-dashboard-roster.md, findings/market-gaps-2026.md, customers/first-customers.md, method/scope.md). Then write ONE deliverable: docs/plan/idea-set.md — 5-8 genuinely different product shapes, each with payer / evidence / build size / kill condition / single-tenant-OAuth survival; a clearly fenced speculative daydream section; a pick + fallback argued both ways; and an explicit attack list for wave 2b. No architecture (2c's job), no fact-checking of my own claims (2b's job). Write only inside projects/agent-hermes-dashboard/. No git.
DID: see closing entry below.
FILES: docs/plan/idea-set.md
OPEN: see closing entry below.

## 2026-09-17 — wave 2a (idea + daydream) — phase 2 COMPLETE
PLAN: close out after writing docs/plan/idea-set.md.
DID: Wrote the single deliverable. Eight candidates (A fleet supervision dashboard, B single-job blind-spot agent, C standalone graduation engine, D mocking morning report, E agent-ops as a service, F provenance/staleness layer, G marketplace-shipped narrow agent, H cost-and-limit governor), each with payer / build size / kill condition / single-tenant-OAuth verdict. Spot-checked raw/ before leaning on anything: `raw/smallbiz-blind-spots-pulls.md` (confirmed the SBI n=760 figures are a relayed sub-agent chart read, NOT a first-hand fetch — represented honestly in docs/explore/smallbiz-blind-spots.md, and re-flagged here) and `raw/claude-code-docs-2026-09-17.md` L19-21/L33-39/L52-58/L76-78/L130/L148-158 (OAuth three-way split, total_cost_usd, Stop/SubagentStop cost+duration_ms, 5-hour+weekly window, 7x agent-teams cost, /usage Loops row).
  PICK, argued both ways: **primary B**, scoped to the recorded fact and explicitly NOT the repricing recommendation — the recommendation version violates the brief's own sub-question-3 trust line, which is named in the file as an internal contradiction. **Fallback H**, on near-zero expected cost (it is the tool needed to run anything else unattended), not on market size. **C flagged watch-not-start**, contingent on attack item #6.
  HONEST HEADLINE, stated in the file before the pick: no candidate has direct demand evidence. Every argument rests on absence-of-supply (quota-constrained search) or a practice gap. That is stated as a limit on the pick, not smuggled past it.
  DIED ON SINGLE-TENANT: A as a product (a non-technical buyer can neither supply an API key nor be offered a claude.ai login) — it survives only as an internal tool, which is candidate E. Second-order: per-customer compute lands on the team's own bill for B/D/E/G, and the subscription allowance size is unknown, so unit economics are unresolvable.
  DAYDREAM fenced between horizontal rules and labelled fiction-by-construction at both ends.
FILES: docs/plan/idea-set.md
OPEN:
  **WAVE 2b — attack these, in this order.** Full table is the last section of docs/plan/idea-set.md (12 items). The three that decide whether the pick stands:
    #1 The OAuth self-use reading — is running one subscription unattended to produce output sold to paying customers permitted? Wave 1 flagged its own reading as interpretation, not counsel. If this fails, B and E need a different compute model and the set narrows to C/F/H.
    #2 The SBI/Price Intelligently ~54% / ~20% figures — re-fetch the PDF p.11 first-hand. Vendor sells the exact service the finding says is missing; figures were chart-read by a delegated sub-agent; population is B2B SaaS companies, not 3-10-person SMBs. If this fails, B loses its only evidential leg and "no candidate clears the bar" becomes the honest output.
    #3 Is there already a cheap incumbent competitor-price tracker (Prisync, Competera, Visualping)? Never pulled at all. If yes, B is a commodity.
  Then: #4 re-run the SMB-supervision-product search on a fresh quota; #5 MEASURE one live `claude -p` run and diff the actual hook payload against docs/explore/task-telemetry.md's table (projects/CLAUDE.md: measured beats argued); #6 hands-on Braintrust Patterns; #7 payment rail out of Vietnam; #8 subscription allowance size; #10 CrewTower n=1; #11 zero demand evidence for the mocking persona; #12 marketplace volume.
  **WAVE 2c — the shape you are designing**, if the pick survives 2b: a single-tenant, output-shipping, recurring watcher. Unit of work = a *watched fact* — a dated observation with a source artifact, a re-check cadence, and a staleness clock. Not a dashboard. Required pieces, in dependency order: (1) task record schema carrying cost/duration from the Stop/SubagentStop hook payload; (2) the fact store with timestamps, since staleness is confirmed unobtainable from the platform and must be built; (3) recurrence detection over the task record — the only genuinely uninvented piece; (4) the graduation path from repeated task to dedicated tool; (5) the trust boundary rendered in the output: recorded fact is shown, agent-authored recommendation is fenced or omitted. Design H alongside it, not after it — the subscription window governor is a prerequisite for any unattended run, and it is the fallback product.
  Not done, deliberately: no architecture (2c's), no fact-checking of my own claims (2b's), no go/no-go (the user's).

