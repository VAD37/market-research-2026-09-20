# Task telemetry — what an agent run can actually emit today

2026-09-17. Evidence: `../../raw/claude-code-docs-2026-09-17.md` (primary Anthropic docs, WebFetch pulled). Cross-reference: `../../../docs/markets/agent-dashboard.md` capability table ("Cost attribution per agent run... Moat is cross-provider rollup, not arithmetic"). Scope: sub-question 4 (observability) and the brief's explicit ask — name the concrete mechanism for each, say what is NOT obtainable.

## Per-task metrics, mechanism named

| Metric | Obtainable? | Concrete mechanism | Granularity |
|---|---|---|---|
| Token cost (per invocation) | **Yes** | `claude -p --output-format json` → `total_cost_usd` field, client-side estimate at list price | Per `claude -p` call |
| Token cost (per task, attributed) | **Yes** | OTel metric `claude_code.cost.usage` (USD), attributes `model`, `query_source` (main/subagent/auxiliary), `agent.name`, `skill.name`, `mcp_server.name`/`mcp_tool.name` | Per subagent/skill/MCP-tool, if OTel enabled |
| Token usage (input/output/cache) | **Yes** | OTel metric `claude_code.token.usage`, attribute `type: input\|output\|cacheRead\|cacheCreation` | Per model, per query_source |
| Wall time | **Yes** | Hook payload: `Stop`/`SubagentStop` events carry `duration_ms` directly. Also `claude -p --output-format json`'s human-readable `Total duration (wall)` in `/usage`, and OTel span `interaction.duration_ms` (beta tracing) | Per turn / per subagent / per session |
| Tool-call counts | **Yes** | `PreToolUse`/`PostToolUse` hook events fire once per call — count them in a hook handler. OTel event `claude_code.tool_result` (one per call) with `success`, `duration_ms`, `tool_input_size_bytes`/`tool_result_size_bytes` | Per tool call |
| Retries | **Partial** | No dedicated "retry" field in hooks. `stream-json` output emits a `system/api_retry` event with `attempt`, `max_retries`, `retry_delay_ms`, `error_status`, `error` (enum) — this is the real retry signal, but only in `--output-format stream-json` mode, not in plain `json` mode or in hooks | Per API-call retry, stream-json only |
| Error classes | **Yes** | Hook `StopFailure` event: `error_type` enum `rate_limit\|overloaded\|authentication_failed\|billing_error\|server_error\|unknown`. Same enum set appears in the `system/api_retry` stream event's `error` field (with two more: `oauth_org_not_allowed`, `invalid_request`, `model_not_found`, `max_output_tokens`, `cloud_credential_error`) | Per turn failure / per retry attempt |
| Human-override events | **Partial** | `PermissionRequest`/`PermissionDenied` hook events fire when a tool call needs or is denied a permission decision — this is the closest primary-doc mechanism to "a human overrode the agent." No dedicated "human edited the output after the fact" event found in what was fetched | Per permission decision only, not per post-hoc edit |
| Recurring-task detection | **No, not built-in** | `/usage`'s `Loops` row (v2.1.242+) rolls up *already-defined* scheduled tasks (fire frequency, run count, tokens) — it does not detect that two *unscheduled*, ad-hoc prompts were "the same task" run twice. That pattern-matching is not a documented Claude Code feature; it would have to be built in the supervision layer, e.g. by hashing/clustering prompt text or task descriptions across `claude_code.user_prompt` OTel events | Not obtainable as a primitive — this is exactly the gap the project brief (sub-question 5) asks the design phase to fill |
| Staleness of a recorded fact | **No** | No mechanism found for "this fact was recorded N days ago and hasn't been re-checked" — this is a supervision-layer concept, not something Claude Code or its telemetry tracks. Would need to be built on top of whatever the agent's memory/state store is (Hermes uses a SQLite `hermes_state_*` split with FTS5 — see `hermes-substrate.md` — which has timestamps to build staleness on, but the runtime itself doesn't surface "staleness" as a metric) | Not obtainable as a primitive |

## The three layers, concretely

1. **Per-invocation JSON** (`claude -p --output-format json`): zero setup, just parse `total_cost_usd`, `session_id`, `result`. Coarsest granularity — one number per whole `claude -p` call, not sub-task.
2. **Hooks** (`.claude/settings.json`): near-zero setup (a shell script + a JSON block), fires synchronously inside the run, can see `cost`/`duration_ms` on `Stop`/`SubagentStop`, can block or rewrite tool calls. Best mechanism for a supervision layer that wants to intercept and log in real time without standing up infrastructure.
3. **OpenTelemetry** (`CLAUDE_CODE_ENABLE_TELEMETRY=1` + `OTEL_METRICS_EXPORTER`/`OTEL_LOGS_EXPORTER`/`OTEL_EXPORTER_OTLP_ENDPOINT`): the only layer with a defined metric+event+span schema (`claude_code.cost.usage`, `claude_code.token.usage`, `claude_code.tool_result`, beta trace spans `claude_code.interaction`→`llm_request`/`tool`/`hook`). Needs an OTel collector to receive it (Langfuse, Helicone, W&B Weave etc. all consume OTel — see `control-planes.md`). **Confirmed to work under OAuth/subscription login, not just API key** — verbatim, "Claude Code telemetry works with both API key and OAuth/subscription login... All telemetry flows through the same exporters regardless of authentication method" (monitoring-usage.md). This directly de-risks the sub-question-6 concern about OAuth-based autonomy losing observability.

## What is NOT obtainable, plainly

- **A native "this is the same task as last week" signal.** Must be built.
- **A native staleness clock on a remembered fact.** Must be built on the agent's own state store's timestamps.
- **Retry counts outside `stream-json` mode.** Plain `json` mode gives you the final result only; you lose the retry trail unless you run in `stream-json` and capture `system/api_retry` events as they stream.
- **Exact dollar billing** — every cost figure surfaced (invocation JSON, `/usage`, OTel `cost.usage`) is explicitly labeled a **client-side estimate at list price**, not the actual bill. Two sources say this in the same words: headless.md ("client-side estimates and can differ from your actual bill") and costs.md ("The figure is an estimate, so for authoritative billing see the Usage page in the Claude Console").
- **A dedicated "human overrode the agent's output after the fact" event.** Only permission-time denial is captured, not a later human edit to something the agent already produced.
- **OTel span-level stability guarantee** — the *industry* semantic conventions for this (OpenTelemetry GenAI semconv) were, per the pass-1 market research, still marked no-Stable-attributes as of 2026-07-17 (`../../../docs/markets/agent-dashboard.md`). Claude Code's own OTel schema (`claude_code.*` namespace) is Anthropic-specific, not the vendor-neutral GenAI semconv — a fleet dashboard spanning multiple model vendors would need to map both.

## Read for the design phase

The record/recurrence/trust layer the brief calls "the claim" (not the dashboard) has real primitives to build on: hooks give synchronous per-task cost+duration+error-class with no infrastructure, and OTel gives a durable, queryable event stream if the design wants a proper store. Recurring-task detection and fact-staleness are both *unbuilt* — confirmed absent from the platform, not just under-documented — which matches the brief's framing that these are the parts worth designing rather than assuming.

## Caveats

- `hooks.md` fetched as a structured reference rather than prose (see `claude-code-substrate.md` caveats) — field names here should be spot-checked against the live page before the prototype codes against them.
- No independent test was run this session confirming these fields actually appear in a live hook/OTel payload — this file reports what the docs claim, not a measured-by-us confirmation. `projects/CLAUDE.md` rates "measured beats argued" — the design/prototype phase should run one real `claude -p` invocation with telemetry on and diff the actual payload against this table before relying on it.
- `agent.name`/`skill.name` OTel attribution depends on the run actually using subagents/skills; a flat single-agent script produces a thinner attribute set.
