# Claude Code substrate — what unattended execution can physically do

2026-09-17. Primary source: Anthropic's own docs at code.claude.com/docs, fetched directly (WebFetch), verbatim quotes below. Evidence: `../../raw/claude-code-docs-2026-09-17.md`. This decides what the prototype in `../../prototype/` can build on — read it before designing the task-execution loop.

## The load-bearing finding: OAuth is not one gate, it is three different gates

`MegaPlan.md` §2 states "Autonomous run depend on claude code OAUTH token and usage." That is not one clean fact — it splits three ways depending on which layer runs the loop:

| Layer | OAuth/subscription login usable? | Source |
|---|---|---|
| **`claude -p` CLI, non-bare (default)** | **Yes, by default.** Same subscription login as interactive use | headless.md: "`--bare` mode doesn't use your subscription login" — implies non-bare does |
| **`claude -p --bare`** | No. Requires `ANTHROPIC_API_KEY` | headless.md, verbatim: "In bare mode, Claude Code never reads OAuth credentials or the system keychain" |
| **Claude Agent SDK (Python/TS `query()`)** | **Restricted for third-party products.** Anthropic's own quickstart: **"Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead."** | agent-sdk/quickstart.md |
| **OTel telemetry export** | **Yes, explicitly, both auth methods** | monitoring-usage.md, verbatim: "Claude Code telemetry works with both API key and OAuth/subscription login... All telemetry flows through the same exporters regardless of authentication method" |

**Reading for this project**: a two-person team running Hermes-style agents *for their own business* (not reselling the login to other customers) sits in the first row — plain `claude -p` (non-bare), same subscription OAuth used interactively, is the documented, intended path. The SDK restriction targets a different shape of product: a company that lets *its own customers* log in with claude.ai to get compute the company didn't pay for. If the design phase ever puts multiple end-customers each needing their own Claude login through this product, re-read the SDK quickstart restriction — it applies there, not here. `--bare` mode is Anthropic's stated future default for scripted calls ("will become the default for `-p` in a future release") and requires an API key, so a design that assumes free-standing subscription auth should not assume `--bare` survives long-term; the design phase should pick one lane and note the tradeoff explicitly.

## Headless / print mode — concrete invocation

```
claude -p "prompt" --allowedTools "Read,Edit,Bash"
```

- `-p` / `--print`: non-interactive. Exit code 0 = success, non-zero = failure; auth failures print to **stdout** as the result (not stderr).
- `--output-format`: `text` (default) | `json` (adds `result`, `session_id`, **`total_cost_usd`**, per-model cost breakdown) | `stream-json` (NDJSON events, ends in a `result` message).
- `--json-schema '<schema>'`: forces structured output into a `structured_output` field.
- `--bare`: faster start, skips hooks/skills/commands/subagents/plugins/MCP/CLAUDE.md auto-discovery; requires `ANTHROPIC_API_KEY`.
- `--permission-mode {auto|dontAsk|acceptEdits|...}` + `--permission-prompts none`: for a run with nobody to answer prompts — denies anything that would otherwise prompt (unless a `PermissionRequest` hook allows it), removes `AskUserQuestion` from the toolset, records denials in the final result's `permission_denials` field.
- `--continue` / `--resume <session_id>`: chain follow-up invocations; capture the ID with `jq -r '.session_id'` on the prior JSON output.
- Piped stdin capped at 10MB.
- SIGTERM → exit 143, unfinished turn left unrecorded, `SessionEnd` hooks still run. SIGINT or the SDK's `interrupt()` ends the turn cleanly instead — the one to use for a graceful stop.

## Cost visibility — the concrete field

`--output-format json` on every `claude -p` invocation returns `total_cost_usd` and a per-model cost breakdown, **client-side estimate at list price**, not a bill. Verbatim: *"scripted callers can track spend per invocation without consulting the usage dashboard. Both figures are client-side estimates and can differ from your actual bill."* This is the single field a supervision layer polls per task with zero extra plumbing.

Interactively, `/usage` shows the same figure plus a **`Loops` row** (v2.1.242+) — per scheduled-task breakdown: fire frequency, run count, total/per-run tokens, last-run time. This is the closest built-in feature to "recurring task detection" in the product itself; it does not (per docs fetched) do cross-task pattern detection, only per-defined-task rollup.

For durable, structured telemetry beyond a single invocation's JSON, OTel is the real mechanism — see `task-telemetry.md`.

## Session and context limits

- Context window: reported by a prior research pass as 200,000 tokens; **not independently re-confirmed against a quoted primary-doc line this pull** — flag `unknown, exact figure unconfirmed — checked code.claude.com/docs 2026-09-17` rather than treat 200k as source-verified here.
- Sessions persist as local JSONL transcripts; `--resume`/`--continue` restore them, including scheduled tasks that haven't expired (see below).
- Prompt-cache lifetime: 1 hour on subscription, drops to 5 minutes once drawing on usage credits (choosable TTL), 5 minutes default on API key/cloud provider.

## Rate limits — and what happens when hit

Two separate mechanisms, both documented on the same page (`costs.md`), easy to conflate:

1. **Subscription (Pro/Max/Team/Enterprise) window**: "each member's Claude Code usage draws from a per-seat allowance that resets on a **rolling five-hour window and a weekly window**," shared with Claude chat and Cowork, sized by seat tier. Hit it and you get: `"You've hit your session limit"` or `"You've hit your weekly limit"` (message names the reset time). A **model-specific** variant (`"You've hit your Opus limit"`) lets you switch model family with `/model` to keep working; the session/weekly variant does not. `autoContinueAtUsageLimit` (managed setting, v2.1.234+) controls whether Claude Code auto-waits for reset instead of failing the run.
2. **API/Console org rate limits (TPM/RPM)**: a per-team-size recommendation table exists (1-5 users: 200k-300k TPM, 5-7 RPM per user; scaling down to 500+ users: 10k-15k TPM, 0.25-0.35 RPM) — this is for API-key/Console orgs setting their *own* internal caps, not a hard Anthropic-imposed ceiling on a two-person shop.

For a 2-person team on Pro/Max: the 5-hour + weekly window is the wall to design around, not TPM/RPM. Hitting it degrades to a hard stop with a named reset time, not a queued retry or degraded model (except the Opus→other-family escape hatch).

## Hooks — the per-task capture mechanism

Configured in `~/.claude/settings.json` (user), `.claude/settings.json` (project, shareable), or `.claude/settings.local.json` (project, local). Full event list and per-event fields, source `hooks.md` — flagged in the raw file as a WebFetch-summarized reference page, re-verify exact JSON shape before coding against it:

- **`Stop` / `SubagentStop`** carry `cost: {input_tokens, output_tokens}` and `duration_ms` directly in the hook payload — the concrete mechanism for per-task cost+time without touching OTel.
- **`StopFailure`** carries `error_type` (`rate_limit|overloaded|authentication_failed|billing_error|server_error|unknown`) — the concrete error-class mechanism.
- **`PreToolUse`/`PostToolUse`/`PostToolUseFailure`** carry `tool_name`, `tool_input`, `tool_output`, `error` — per-tool-call detail, retry-adjacent (a retry shows up as repeated `PreToolUse` events for the same logical step, not a dedicated "retry" field).
- **`PermissionRequest`/`PermissionDenied`**: the human-override-adjacent events — a denial is recorded here, not as a separate "override" event type in the docs fetched.
- Exit code 2 from a hook blocks the action; hook output JSON (`hookSpecificOutput.permissionDecision: allow|deny|request`, etc.) can rewrite tool input or add context.

## Scheduled / cron execution

Three mechanisms, compared verbatim (`scheduled-tasks.md`):

| | Cloud (Routines) | Desktop | `/loop` (session-scoped) |
|---|---|---|---|
| Runs on | Cloud, Anthropic-managed | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume`, with exceptions |
| Local file access | No (fresh clone) | Yes | Yes |
| Permission prompts | No (autonomous) | Configurable | Inherits session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

- Underlying tools: `CronCreate` (5-field cron, prompt, recurring/one-shot), `CronList`, `CronDelete`. **Max 50 scheduled tasks per session.**
- **Recurring tasks auto-expire after 7 days**, fire once more, self-delete. Must be recreated for longer-lived recurrence, or moved to Routines/Desktop tasks.
- **Hard gotcha, verbatim**: *"Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit stops them firing."* A backgrounded session keeps `/loop` tasks alive without a terminal; a closed one does not.
- No catch-up for missed fires — a task busy-blocked fires once when idle next, not once per missed interval.
- A fresh conversation clears all session-scoped tasks; self-paced `/loop` specifically is never restored on `--resume` (must reissue the command).
- `CLAUDE_CODE_DISABLE_CRON=1` kills the scheduler entirely.

**For genuinely unattended, restart-surviving execution the docs point away from `/loop`** and toward Routines (cloud) or Desktop scheduled tasks (local) or GitHub Actions — `/loop` is explicitly the "quick polling during a session" tier, not the durable-automation tier.

## MCP in headless mode

`--mcp-config <file-or-json>` (or auto-loaded `.mcp.json` at project root, skipped entirely by `--bare`). Validated at startup; Claude Code waits up to `MCP_TIMEOUT` (default 30s) for pending servers before the first turn (v2.1.221+); a server with a cached tool list skips the wait. Invalid/skipped entries land in the `mcp_server_errors` field of the `system/init` stream event rather than failing the run — a CI/supervision layer can gate on that field being non-empty. No interactive OAuth flow in headless mode for an MCP server that needs one — must pre-authenticate (`claude mcp login <server>`) in an interactive session first.

## Caveats

- Context-window token limit (200k, per a prior subagent pass) is not independently confirmed against a quoted primary-doc line in this pull. Flag as unconfirmed, not wrong.
- `hooks.md` content came back from WebFetch as a pre-structured reference rather than flowing prose (unlike every other page pulled this session) — treat event/field names as reliable but re-verify exact JSON shapes against the live page before coding.
- Rate-limit "what happens when hit" is documented at the message-and-mechanism level (named reset time, model-family escape hatch, `autoContinueAtUsageLimit`); no primary-doc figure found for the exact size of the 5-hour/weekly allowance in tokens or dollars for a given Pro/Max tier — that number lives behind sign-in, not in public docs, as of this pull.
- The OAuth-restriction reading in this file (third-party resale vs. self-use) is this agent's interpretation of the quickstart's wording, not a line Anthropic states explicitly as "self-use is fine." It is the most literal reading of "does not allow third party developers to offer claude.ai login... for their products" — a two-person team running its own agents for its own business is not offering login to third parties — but the design phase should not treat this as a legal green light; it is a research read, not counsel.
