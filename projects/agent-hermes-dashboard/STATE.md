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
