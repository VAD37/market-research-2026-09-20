# Telemetry, measured — resolving the Stop/SubagentStop cost+duration dispute

2026-09-17. Wave 1e. Evidence: `../../raw/hook-payload-measurement-2026-09-17.md` (measured by
us — live `claude -p` runs, Claude Code v2.1.259, interactive OAuth/subscription login, this
machine, 2026-09-17). This is a measurement, not a docs re-read. Scope: settle the claim flagged
CONTESTED in `../review/market-check.md` ("(i) Stop/SubagentStop cost + duration_ms is
CONTESTED... Load-bearing for C, F and H(d)") per `../../STATE.md`'s 1e assignment.

## The contradiction, both sides, attributed

| Source | Claim |
|---|---|
| `claude-code-substrate.md` (this project, wave 1) | Verbatim: "**`Stop` / `SubagentStop`** carry `cost: {input_tokens, output_tokens}` and `duration_ms` directly in the hook payload — the concrete mechanism for per-task cost+time without touching OTel." |
| `task-telemetry.md` (this project, wave 1) | Table row: "Wall time... Hook payload: `Stop`/`SubagentStop` events carry `duration_ms` directly." Same file's own caveats section already flagged this as unverified: "No independent test was run this session confirming these fields actually appear in a live hook/OTel payload." |
| `market-check.md` (wave 2b) | "This wave's docs read found no cost or duration field documented on either hook's input JSON, against docs/explore/task-telemetry.md and idea-set.md fact 1. Two reads of the same page disagree and neither wave measured it live." |

## Measured answer

**Neither `Stop` nor `SubagentStop` carries a `cost` field or a `duration_ms` field, on this
machine, this Claude Code version, across 3 independent live runs (2 `Stop`, 1 `SubagentStop`,
one of which spawned a real subagent).** `claude-code-substrate.md`'s specific claim does not
hold. `task-telemetry.md`'s own caveat calling for a live test was correct to ask for one.

## Field table — every key actually observed

| Field | Type | Unit | In `Stop`? | In `SubagentStop`? | Good for |
|---|---|---|---|---|---|
| `session_id` | string (UUID) | — | Yes | Yes | Correlating hook fire to a session/transcript |
| `transcript_path` | string (path) | — | Yes | Yes | Locating the main session's JSONL for later parsing |
| `agent_transcript_path` | string (path) | — | No | Yes | Locating the SPECIFIC subagent's own JSONL |
| `agent_id` | string (hex id) | — | No | Yes | Per-subagent identity — needed for attribution, present |
| `agent_type` | string | — | No | Yes | Which subagent definition ran (e.g. `general-purpose`) |
| `cwd` | string (path) | — | Yes | Yes | Working directory context |
| `prompt_id` | string (UUID) | — | Yes | Yes | Correlating to a specific user turn |
| `permission_mode` | string enum | — | Yes | Yes | e.g. `auto`, `acceptEdits`, `bypassPermissions` |
| `effort` | object `{level}` | — | Yes | Yes | Effort tier used (`high` observed) — not a model id |
| `hook_event_name` | string | — | Yes | Yes | `"Stop"` / `"SubagentStop"` — confirms which fired |
| `stop_hook_active` | boolean | — | Yes | Yes | Loop-guard flag; `false` in every run observed |
| `last_assistant_message` | string | — | Yes | Yes | Final text output of the turn/subagent |
| `background_tasks` | array | — | Yes | Yes | Empty in every run observed; not exercised |
| `session_crons` | array | — | Yes | Yes | Empty in every run observed; not exercised |
| `cost` | — | — | **not observed — tested 2026-09-17** | **not observed — tested 2026-09-17** | n/a — claimed by substrate doc, absent in 3 live runs |
| `duration_ms` (hook-level) | — | — | **not observed — tested 2026-09-17** | **not observed — tested 2026-09-17** | n/a — claimed by both docs, absent in 3 live runs |
| token counts | — | — | not observed | not observed | Absent from the hook payload itself |
| model id | — | — | not observed | not observed | Absent from the hook payload itself (only `effort.level`) |
| tool-call counts | — | — | not observed | not observed | Absent from the hook payload itself |
| turn counts | — | — | not observed | not observed | Absent from the hook payload itself |

Fields observed instead in `claude -p --output-format json` stdout (per-whole-invocation, NOT a
hook payload — see raw file for full verbatim capture):

| Field | Type | Unit | Granularity | Good for |
|---|---|---|---|---|
| `total_cost_usd` | float | USD, client-side list-price estimate | Per `claude -p` invocation | The only directly-handed dollar figure that exists in this measurement |
| `duration_ms` | int | milliseconds, wall time | Per invocation | Wall time — but only for the WHOLE run, not per subagent/turn |
| `duration_api_ms` | int | milliseconds | Per invocation | Time actually spent in API calls |
| `usage.{input,output,cache_read,cache_creation}_tokens` | int | tokens | Per invocation | Token accounting |
| `modelUsage.<model>.costUSD` | float | USD | Per model, within one invocation | Cost split when a run used more than one model |
| `subagent_stats.{spawned,completed,failed,killed,refused}` | int counts | count | Per invocation, aggregated across ALL subagents | Counts only — no per-subagent dollar breakdown |
| `permission_denials` | array | — | Per invocation | Closest observed field to a "human override" signal; empty in every run here (nothing was actually denied) |
| `num_turns` | int | count | Per invocation | Turn count |

Fields observed in the per-subagent transcript JSONL (reached via `agent_transcript_path`, not
part of the hook payload itself — requires an extra file-read step):

| Field | Type | Unit | Good for |
|---|---|---|---|
| `message.usage.{input,output,cache_read,cache_creation}_tokens` | int | tokens | Per-message token counts — the raw ingredient for computing a subagent's own cost yourself |
| `message.model` | string | — | e.g. `claude-opus-5` — needed to look up a price per token externally |
| `attributionAgent` | string | — | Which subagent type produced this message |
| `timestamp` | ISO 8601 string | — | Per-message time — can derive subagent wall time as (last ts − first ts); no `duration_ms` field exists to read directly |

Confirmed by exhaustive grep of the actual JSONL files: **zero occurrences of `costUSD` or
`duration_ms`** in the transcript files themselves. No dollar figure is ever written into a
transcript by Claude Code — an external reader (ccusage-style) must compute it from tokens +
model + its own pricing table.

## Verdict on the contested claim

**Per-task cost and duration_ms do NOT arrive in the `Stop`/`SubagentStop` hook payload, under
either auth mode reachable from this measurement (measured: interactive OAuth/subscription
login; not measured: API key / `--bare`, but nothing in the hook schema shown here is
auth-mode-conditional — the hook fields are a fixed JSON shape independent of how the session
authenticated).** `task-telemetry.md` and `claude-code-substrate.md` were both wrong on this one
specific field claim; `market-check.md`'s "docs read found no cost/duration field" reading is the
one that survives contact with a live run.

What DOES arrive, and where:
- **Per-invocation** dollar cost and wall time: yes, in `claude -p --output-format json` stdout —
  `total_cost_usd` and `duration_ms`. One number per whole `claude -p` call.
- **Per-subagent** cost: only indirectly. `SubagentStop` hands you `agent_id`, `agent_type`, and
  `agent_transcript_path` — real attribution keys — but you must open that file yourself, sum its
  `usage` token fields, and multiply by a price table you supply. Claude Code does not do this
  arithmetic and does not expose a subagent-level dollar or `duration_ms` field anywhere observed.
- **Per-subagent wall time**: not directly available anywhere observed; derivable only by
  subtracting the first and last `timestamp` in that subagent's own transcript file.

### What this means for candidates C, F, H

- **Candidate C** (needs per-subagent cost attribution): the hook alone does not deliver it. It IS
  buildable — `agent_id` + `agent_transcript_path` from `SubagentStop` are real, present,
  reliable keys — but it requires a supervisor process that reads the pointed-to transcript file
  and does the token→dollar math itself, keyed off `message.model` per line. This is real
  engineering work, not "read a field," and it needs an externally maintained price table that
  Claude Code does not supply anywhere in this measurement.
- **Candidate F and H(d)** (assumed hook-level cost/duration as a zero-plumbing mechanism): that
  specific mechanism does not exist. The zero-plumbing mechanism that DOES exist is
  `--output-format json`'s `total_cost_usd`/`duration_ms`, but only at the granularity of one
  whole `claude -p` call — fine for "cost of this task" if one task = one `claude -p` invocation
  with no subagents, not fine for splitting cost across a fan-out of subagents within one call.

## What remains genuinely unobtainable (measured, not assumed)

- **A per-subagent dollar figure handed to you directly** — must be computed from tokens + a
  self-maintained price table; not a native field anywhere checked (hooks, CLI JSON, transcripts,
  `stats-cache.json`).
- **A per-subagent `duration_ms`** — not present anywhere checked; derivable only from transcript
  timestamps, not handed to you.
- **`/usage` from a headless/scripted context** — confirmed absent from `claude --help` (v2.1.259):
  no `usage` subcommand, no `--usage` flag exists. It is interactive-session-only; untestable
  headlessly by definition, not just unattempted.
- **A local, Claude-Code-maintained cost ledger** — `stats-cache.json` is the closest thing that
  exists under `~/.claude/`, and its own `costUSD` fields are hard-coded `0` for every model on
  this machine; it tracks cumulative lifetime TOKEN counts and daily message/session/tool-call
  counts, never a dollar figure, and never at per-task granularity (only "today" rollups and one
  all-time "longest session" record).
- **Retry counts, outside stream-json mode** — not retested this pass (would require forcing an
  actual API retry, out of scope for "trivial, few" runs); `task-telemetry.md`'s existing finding
  that only `--output-format stream-json`'s `system/api_retry` event carries this is unchallenged
  by anything measured here.
- **Human-override events distinct from permission denial** — `permission_denials` is a real,
  present field (confirmed structurally, empty in every run here because nothing was actually
  denied); a genuine denial event was not exercised this pass (see raw file, run 4 note) —
  disallowing a tool outright removes it from the toolset rather than triggering a denial. Still
  unconfirmed whether a true mid-call `PermissionDenied` produces a richer payload than what's
  shown here; flagged as **not observed — tested 2026-09-17, inconclusive**, not as confirmed absent.
- **Exact billed dollar amount vs. the client-side estimate** — not re-tested here (would require
  comparing against actual Anthropic billing, outside this measurement's reach); carried forward
  from `claude-code-substrate.md`/`task-telemetry.md` as an unchallenged prior finding.
- **API-key / `--bare` auth mode's hook payload shape** — not tested this pass; everything above
  was measured under interactive OAuth/subscription login only.

## Caveats

- Single machine, single version (2.1.259), single auth mode, 4 total `claude -p` invocations —
  enough to settle the specific yes/no on cost/duration-in-hooks (reproduced twice, plus the
  subagent case), not enough to characterize every hook event type or every failure path.
- OTel export was not stood up for this measurement (would need a running collector) — nothing
  here contradicts or confirms `task-telemetry.md`'s OTel-schema claims (`claude_code.cost.usage`
  etc.); those remain doc-sourced, not measured, and are a distinct mechanism from hooks.
- `StopFailure`, `PreToolUse`/`PostToolUse`, and `PermissionRequest`/`PermissionDenied` payload
  shapes were not captured this pass (only `Stop` and `SubagentStop`, per the assignment) — do not
  read this file as confirming or denying anything about those other hook events.
