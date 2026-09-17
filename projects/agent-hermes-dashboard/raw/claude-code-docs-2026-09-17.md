# Claude Code / Agent SDK primary docs — pulled 2026-09-17

Method: WebFetch direct to code.claude.com/docs pages (Anthropic's own docs, primary source). Each block is the fetched content, condensed by WebFetch's summarization pass (noted per-block); URLs given. No WebSearch used for this file.

---

## https://code.claude.com/docs/en/agent-sdk/quickstart.md

Fetched in full (WebFetch returned near-complete page text). Key verbatim passage on auth:

> Get an API key from the Claude Console, then set it as an environment variable... The SDK reads the key from the environment of the process that runs your agent; it doesn't load `.env` files automatically.
>
> The SDK also supports authentication via third-party API providers:
> - **Amazon Bedrock**: set `CLAUDE_CODE_USE_BEDROCK=1` and configure AWS credentials
> - **Claude Platform on AWS**: set `CLAUDE_CODE_USE_ANTHROPIC_AWS=1` and `ANTHROPIC_AWS_WORKSPACE_ID`
> - **Google Cloud's Agent Platform**: set `CLAUDE_CODE_USE_VERTEX=1`
> - **Microsoft Foundry**: set `CLAUDE_CODE_USE_FOUNDRY=1`
>
> **Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.**

Read carefully: this restricts *offering claude.ai login to your own product's end users / customers* (i.e., building a multi-tenant SaaS that piggybacks on other people's claude.ai logins for compute). It is a policy statement in the SDK quickstart, not a blanket ban on a single operator running their own Claude Code subscription unattended for their own use — see headless.md below, which describes non-bare `-p` mode using subscription login by default.

Agent loop: Python `claude_agent_sdk.query()` / TypeScript `@anthropic-ai/claude-agent-sdk` `query()`, async iterator, `ClaudeAgentOptions` (allowed_tools, permission_mode, system_prompt, mcp_servers, etc). SDK "handles the orchestration, tool execution, context management, and retries."

---

## https://code.claude.com/docs/en/headless.md ("Run Claude Code programmatically")

Fetched near-verbatim. Key facts:

- **Invocation**: `claude -p "prompt" --allowedTools "Read,Edit,Bash"`. `-p`/`--print` = non-interactive.
- **Exit codes**: 0 = success, non-zero = failure. Auth failures print to stdout as the result, not stderr.
- **`--bare` mode**: skips auto-discovery of hooks, skills, custom commands, subagents, plugins, MCP servers, auto memory, CLAUDE.md. Verbatim: **"bare mode doesn't use your subscription login"** — you must set `ANTHROPIC_API_KEY` in bare mode. **"In bare mode, Claude Code never reads OAuth credentials or the system keychain."**
  - **Implication, load-bearing**: non-bare `-p` (the default) DOES read OAuth credentials / subscription login by default, same as an interactive session. `--bare` is recommended for CI/scripted/SDK calls going forward ("will become the default for `-p` in a future release") but is not yet the default.
- **No workspace-trust dialog in `-p`**: "A `-p` session shows no workspace trust dialog and no per-server approval prompt" — hooks in `.claude/settings.json` and MCP servers in `.mcp.json` run even in an untrusted folder, unless `--bare`.
- **Background tasks at exit**: a background Bash task (dev server, watch build) is killed ~5s after Claude returns its final result. A background subagent/workflow keeps `-p` open until done, capped at 10 minutes idle wait (`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` to change, `0` = unlimited).
- **SIGTERM**: exits 143, leaves in-progress turn unfinished, records no result for it, runs `SessionEnd` hooks, kills any running Bash process tree. SIGINT (or SDK `interrupt()`) ends the turn cleanly instead.
- **Output formats** (`--output-format`): `text` (default), `json` (structured, includes `result`, `session_id`, `total_cost_usd`, per-model cost breakdown), `stream-json` (NDJSON events).
  - Verbatim: **"With `--output-format json`, the response payload includes `total_cost_usd` and a per-model cost breakdown, so scripted callers can track spend per invocation without consulting the usage dashboard. Both figures are client-side estimates and can differ from your actual bill."**
  - `--json-schema` forces structured output into a `structured_output` field.
- **Piped stdin**: capped at 10MB.
- **`system/api_retry` event** (stream-json): fields `attempt`, `max_retries`, `retry_delay_ms`, `error_status`, `error` (enum: `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `rate_limit`, `overloaded`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown`), `session_id`.
- **`system/init` event**: reports model, tools, MCP servers, plugins loaded; optional `capabilities` array; `plugin_errors` / `mcp_server_errors` fields for catching load failures (e.g. CI gating).
- **Subagent messages in stream**: carry `parent_tool_use_id`; `--forward-subagent-text` / `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` forwards subagent text/thinking blocks too (full transcript reconstruction).
- **`--permission-prompts none`**: for unattended runs with nobody to answer prompts. Denies anything that would otherwise prompt (unless a `PermissionRequest` hook allows it), removes `AskUserQuestion` from Claude's toolset, cancels unanswered MCP elicitations. Denials appear as `permission_denied` system messages; final result lists them in `permission_denials`.
- **`--permission-mode`**: `auto` (classifier reviews most actions), `dontAsk` (denies everything that would prompt, but allow-rules/allowedTools still work), `acceptEdits` (auto-approves file writes + common fs commands like mkdir/touch/mv/cp).
- **`--continue` / `--resume <session_id>`**: continue prior conversation; session ID capturable via `jq -r '.session_id'` from JSON output.
- **MCP in `-p`**: `--mcp-config <file-or-json>`, validated at startup; waits up to `MCP_TIMEOUT` (default 30s) for pending servers before first turn (v2.1.221+); skipped/invalid entries reported in `mcp_server_errors`, run continues.

---

## https://code.claude.com/docs/en/costs.md ("Manage costs effectively")

Fetched near-verbatim.

- **Billing model**: "Claude Code charges by API token consumption." Enterprise average ~$13/developer/active-day, $150-250/developer/month, <$30/active-day for 90% of users (vendor-reported, Anthropic's own doc).
- **`/usage` command**: Session block shows `Total cost`, `Total duration (API)`, `Total duration (wall)`, code changes, per-model token breakdown. Verbatim: **"Claude Max and Pro subscribers have usage included in their subscription, so the session cost figure isn't relevant for billing purposes."** The dollar figure is computed **locally, from token counts, at list price** — an estimate, not a bill. Resets on `/clear` (before v2.1.211 it accumulated for the process lifetime — a versioned behavior change).
- **`Loops` row in `/usage`** (v2.1.242+): per scheduled-task/`/loop` breakdown — fire frequency, run count, total and per-run tokens, last-run time. This is the closest built-in feature to "recurring task detection / telemetry" found in the primary docs.
- **Attribution row**: usage attributed to skills, subagents, plugins, individual MCP servers, as % of total.
- **Plan usage-credits row** (Pro/Max): monthly usage-credit spend vs monthly spend limit (if set); `Unlimited` if no limit set.
- **`/insights`**: analyzes up to 200 recent local sessions, writes an HTML report to `~/.claude/usage-data/report.html` (timestamped copies kept, auto-deleted after `cleanupPeriodDays`, default 30 days) — covers "what you work on, friction points... suggestions."
- **Rate-limit hit messages** (verbatim): `"You've hit your session limit"` / `"You've hit your weekly limit"` — seat-based usage window on subscription plans, shared across all models, resets shown in message. Model-specific variants (`"You've hit your Opus limit"`) let you switch model family to keep working. `autoContinueAtUsageLimit` managed setting controls whether Claude Code auto-waits for reset (v2.1.234+).
- **Teams/Enterprise**: per-seat allowance resets on **rolling 5-hour window + weekly window**, shared with Claude chat and Cowork; size depends on seat tier (Standard/Premium).
- **Rate-limit recommendation table (API/Console orgs, TPM/RPM per user)**:
  | Team size | TPM/user | RPM/user |
  |---|---|---|
  | 1-5 | 200k-300k | 5-7 |
  | 5-20 | 100k-150k | 2.5-3.5 |
  | 20-50 | 50k-75k | 1.25-1.75 |
  | 50-100 | 25k-35k | 0.62-0.87 |
  | 100-500 | 15k-20k | 0.37-0.47 |
  | 500+ | 10k-15k | 0.25-0.35 |
  This table is for API/Console org-level rate limits, NOT the Pro/Max subscription window model — the two are separate mechanisms documented on the same page.
- **Cache lifetime**: 1 hour on subscription, drops to 5 min once drawing on usage credits (choosable via TTL setting); 5 min default on API key/cloud provider.
- **Background token usage**: conversation summarization for `--resume`, some command processing — "typically under $0.04 per session" even idle.
- **Why usage climbs**: long context resent every turn, cache misses after >1hr idle, **scheduled tasks fire on interval even while session idle, sending full context each time**, cross-session messages, goal check-ins (max 3 idle check-ins per goal, `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` to disable), agent teammates (each keeps consuming until it exits), compaction cost.
- **Agent teams**: ~7x token cost vs standard session when teammates run in plan mode (each teammate = own context window, own Claude instance). Disabled by default; `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` to enable.
- **Per-user cost attribution options** (cloud-provider billing, e.g. Bedrock/Vertex/Foundry): OpenTelemetry export (`/docs/en/monitoring-usage`) — "the only option that streams per-user token and cost metrics into your own observability stack in near real time" — or a self-hosted "Claude apps gateway," or a third-party LLM gateway (LiteLLM named, "unaffiliated with Anthropic, not audited for security").

---

## https://code.claude.com/docs/en/scheduled-tasks.md ("Run prompts on a schedule")

Fetched in full (WebFetch returned complete page text, including the comparison table verbatim).

**Three scheduling mechanisms, compared (verbatim table)**:

| | Cloud (Routines) | Desktop | `/loop` |
|---|---|---|---|
| Runs on | Cloud, Anthropic-managed by default | Your machine | Your machine |
| Requires machine on | No | Yes | Yes |
| Requires open session | No | No | Yes |
| Persistent across restarts | Yes | Yes | Restored on `--resume`, with exceptions |
| Access to local files | No (fresh clone) | Yes | Yes |
| MCP servers | Connectors configured per task | Config files + connectors | Inherits from session |
| Permission prompts | No (runs autonomously) | Configurable per task | Inherits from session |
| Customizable schedule | Via `/schedule` in CLI | Yes | Yes |
| Minimum interval | 1 hour | 1 minute | 1 minute |

- **`/loop`**: bundled skill. `/loop 5m check the deploy` = fixed cron interval (Claude converts to a cron expr); `/loop check the deploy` (no interval) = Claude dynamically picks a 1-min-to-1-hour delay each iteration based on observed state; bare `/loop` = built-in maintenance prompt (continue unfinished work → tend open PR → cleanup pass) or a custom `.claude/loop.md` / `~/.claude/loop.md` (max 25,000 bytes, project file wins).
- **Underlying tools**: `CronCreate` (5-field cron expr, prompt, recurring or one-shot), `CronList`, `CronDelete` (8-char task ID). **Max 50 scheduled tasks per session.**
- **Scheduler mechanics**: checks every second for due tasks, enqueues at low priority, fires between turns (not mid-response). Local timezone. **Jitter**: recurring tasks fire up to 30 min after scheduled time (or up to half the interval if sub-hourly) to avoid thundering-herd; deterministic per task ID.
- **Seven-day expiry**: recurring tasks auto-expire 7 days after creation, fire once more, then self-delete. For longer-lived recurrence, must recreate before expiry, or use Routines/Desktop tasks.
- **`CLAUDE_CODE_DISABLE_CRON=1`**: disables the scheduler entirely.
- **Hard limitations (verbatim), load-bearing for "runs unattended"**:
  > "Tasks only fire while Claude Code is running and idle. Closing the terminal or letting the session exit stops them firing." (Backgrounding the session carries `/loop` tasks to a background session that keeps running without a terminal.)
  > "No catch-up for missed fires. If a task's scheduled time passes while Claude is busy on a long-running request, it fires once when Claude becomes idle, not once per missed interval."
  > "Starting a fresh conversation clears all session-scoped tasks." Self-paced `/loop` is not restored on `--resume` (must re-issue `/loop`). Background Bash/monitor tasks never restored on resume.
- **For durable unattended cron**, the doc explicitly points to: **Routines** (cloud, runs on schedule / API call / GitHub event, min interval 1 hour, "runs autonomously" with no permission prompts, no local file access — fresh clone each run), **GitHub Actions** (`schedule` trigger), **Desktop scheduled tasks** (runs locally, min interval 1 minute, configurable permission prompts per task).

---

## https://code.claude.com/docs/en/hooks.md — hook events reference

**Caveat: WebFetch returned this as a pre-structured reference (tables/lists), not flowing prose — flag as WebFetch's summarization pass over the source page, not a verbatim quote block like the sections above. Treat event names and field names as reliable (structured reference content is low-risk to compress) but re-verify against the live page before citing exact JSON schemas in a build.**

**Full event list, by phase**:
- Session: `SessionStart`, `Setup` (fires on `--init-only`/`--init`/`--maintenance`), `SessionEnd`
- Per-turn: `UserPromptSubmit`, `UserPromptExpansion`, `Stop`, `StopFailure`
- Tool execution: `PreToolUse` (can block), `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `PermissionRequest`, `PermissionDenied`
- Agent/team: `SubagentStart`, `SubagentStop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`
- File/dir: `FileChanged`, `CwdChanged`, `DirectoryAdded`, `WorktreeCreate`, `WorktreeRemove`
- Context/config: `InstructionsLoaded`, `ConfigChange`, `PreCompact`, `PostCompact`
- Model: `PreModelSwitch` (can block), `PostModelSwitch`
- MCP/user input: `Elicitation`, `ElicitationResult`
- Display: `Notification`, `MessageDisplay`

**Common fields on every hook invocation**: `session_id`, `prompt_id`, `transcript_path`, `cwd`, `scratchpad_dir`, `permission_mode`, `effort.level`, `hook_event_name`, `agent_id`, `agent_type`.

**Cost/duration-bearing fields, specifically**: `Stop` / `SubagentStop` events carry `cost: {input_tokens, output_tokens}` and `duration_ms` directly in the hook payload — **this is the concrete per-task cost+time mechanism**, available without touching OTel. `StopFailure` carries `error_type` (`rate_limit|overloaded|authentication_failed|billing_error|server_error|unknown`) — the concrete error-class mechanism.

**Config locations**: `~/.claude/settings.json` (user, all projects), `.claude/settings.json` (project, git-shareable), `.claude/settings.local.json` (project, gitignored), managed/org policy settings, plugin `hooks/hooks.json`, skill/subagent frontmatter (scoped to that skill/subagent's run).

**Handler types**: `command` (shell script, gets JSON on stdin, timeout field, `async`/`asyncRewake`), `http` (POST to a URL), `mcp_tool` (call an MCP tool), `prompt` (ask a model yes/no), `agent` (spawn a full agent to verify).

**Exit code semantics**: `0` = success (stdout JSON still parsed if present), `2` = blocks the action, other = non-blocking but stdout JSON still honored if valid.

**Output schema**: `hookSpecificOutput.{hookEventName, permissionDecision: allow|deny|request, permissionDecisionReason, additionalContext, updatedInput, systemMessage, terminalSequence}`.

---

## https://code.claude.com/docs/en/monitoring-usage.md ("Claude Code OpenTelemetry Monitoring")

Fetched in full (WebFetch returned complete, well-structured page — reads as a genuine reference page, not a summarization artifact).

**Enable**: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `OTEL_METRICS_EXPORTER={otlp|prometheus|console|none}`, `OTEL_LOGS_EXPORTER={otlp|console|none}`, `OTEL_EXPORTER_OTLP_PROTOCOL`, `OTEL_EXPORTER_OTLP_ENDPOINT`.

**Metrics** (time series): `claude_code.session.count`, `claude_code.lines_of_code.count`, `claude_code.pull_request.count`, `claude_code.commit.count`, `claude_code.cost.usage` (USD), `claude_code.token.usage` (tokens, with `type: input|output|cacheRead|cacheCreation` and `query_source: main|subagent|auxiliary` attributes), `claude_code.code_edit_tool.decision`, `claude_code.active_time.total` (s).

**Cost counter attributes**: `model`, `query_source`, `speed`, `effort`, `agent.name` (subagent type), `skill.name`, `mcp_server.name`/`mcp_tool.name` — i.e. cost is attributable down to which subagent/skill/MCP tool incurred it.

**Standard attributes on every metric**: `session.id`, `app.version`, `user.account_uuid` (when authenticated), `user.id` (anon install ID), `organization.id` (when authenticated), `terminal.type`.

**Events (OTel logs protocol)**: `claude_code.user_prompt` (`prompt_length`, `command_name`), `claude_code.assistant_response` (`response_length`, `model`, `request_id`), `claude_code.tool_result` (`success`, `duration_ms`, `error_type`, `tool_input_size_bytes`/`tool_result_size_bytes`), `claude_code.tool_decision`. All events carry `prompt.id` (correlates every event from one prompt), `event.sequence`, `event.timestamp`.

**Distributed tracing (beta)**: `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` + `OTEL_TRACES_EXPORTER=otlp`. Span tree: `claude_code.interaction` (root, per prompt) → `claude_code.llm_request`, `claude_code.hook`, `claude_code.tool` (→ `.blocked_on_user`, `.execution`, nested subagent spans). Span attributes: `llm_request` gets `model`, `input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_creation_tokens`, `duration_ms`, `ttft_ms`, `request_id`, `success`; `tool` gets `tool_name`, `duration_ms`, `success`, `error`, `result_tokens`; `interaction` gets `user_prompt`, `user_prompt_length`, `interaction.duration_ms`.

**Authentication — directly answers the OAuth question for telemetry, load-bearing**: verbatim, **"Claude Code telemetry works with both API key and OAuth/subscription login... All telemetry flows through the same exporters regardless of authentication method."** This is a materially different (more permissive) answer than the Agent SDK quickstart's "third party developers" restriction — OTel export is not gated the way SDK-based resale is. Via a Claude apps gateway, `user.id` becomes the IdP subject and `user.email`/`user.groups` are added.

**Content redaction gates (opt-in, off by default)**: `OTEL_LOG_USER_PROMPTS`, `OTEL_LOG_ASSISTANT_RESPONSES`, `OTEL_LOG_TOOL_DETAILS`, `OTEL_LOG_TOOL_CONTENT`, `OTEL_LOG_RAW_API_BODIES`. Default: prompts, responses, and tool details redacted.

---

## Not fetched this pass (bounded effort)

- `/docs/en/monitoring-usage` (OpenTelemetry export detail — span/metric names) — needed for `task-telemetry.md`'s OTel column; flagged open below.
- `/docs/en/mcp.md` full page (only the headless-mode `--mcp-config` behavior came via headless.md).
- `/docs/en/sessions.md` (exact context-window token limit not independently re-confirmed this pull; a prior subagent pass reported 200,000 tokens but that number came from the subagent's own knowledge, not a quoted primary-doc line in this pull — flag as unconfirmed-this-session).
