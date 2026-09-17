# Hook payload measurement — measured by us, 2026-09-17

Wave 1e. This is NOT a docs pull. Every payload below was produced by running Claude Code on this
machine and capturing what its `Stop`/`SubagentStop` hooks actually received on stdin, and what
`claude -p --output-format json` actually printed on stdout. Settles the CONTESTED claim flagged
in `../STATE.md` (2b closing entry) and `../docs/review/market-check.md` §"TWO CORRECTIONS...(i)".

**Claude Code version measured**: `claude --version` → `2.1.259 (Claude Code)`
**Date**: 2026-09-17 (UTC timestamps in captures ~07:54–07:56Z)
**Auth mode**: interactive OAuth/subscription login (the machine's normal `claude` login) — not
`--bare`, not `ANTHROPIC_API_KEY`. This is the "plain `claude -p`, non-bare" row from
`claude-code-substrate.md`'s OAuth table.
**Test harness location**: throwaway dir
`C:\Users\vad\AppData\Local\Temp\claude\D--researchs-market-research\6015ae55-967c-483c-a913-ac90724ab1d4\scratchpad\hook-test-1e`,
project-local `.claude\settings.json` only (never `C:\Users\vad\.claude\settings.json`, never this
repo). Removed at the end of this wave (see closing note).

Redaction applied: all session/agent/prompt UUIDs and hex ids → `<redacted-uuid>` / `<redacted-id>`;
any email → `<redacted-email>`; request/message ids → `<redacted-request-id>` / `<redacted-message-id>`.
No token, key, or OAuth value appeared in any captured payload (checked).

## Harness config (`.claude\settings.json`, throwaway dir only)

```json
{
  "hooks": {
    "Stop": [
      { "matcher": "", "hooks": [ { "type": "command", "command": "cat > ./hook-captures/stop_payload.json" } ] }
    ],
    "SubagentStop": [
      { "matcher": "", "hooks": [ { "type": "command", "command": "cat >> ./hook-captures/subagentstop_payload.jsonl" } ] }
    ]
  }
}
```

## Run 1 — trivial Stop hook, no tools, no subagent

Command:
```
claude -p "Print exactly the string HOOK_TEST_STOP_1E and nothing else." --output-format json
```

`Stop` hook payload (verbatim stdin, redacted):
```json
{"session_id":"<redacted-uuid>","transcript_path":"C:\\Users\\vad\\.claude\\projects\\C--Users-vad-AppData-Local-Temp-claude-D--researchs-market-research-<redacted-uuid>-scratchpad-hook-test-1e\\<redacted-uuid>.jsonl","cwd":"C:\\Users\\vad\\AppData\\Local\\Temp\\claude\\D--researchs-market-research\\<redacted-uuid>\\scratchpad\\hook-test-1e","prompt_id":"<redacted-uuid>","permission_mode":"auto","effort":{"level":"high"},"hook_event_name":"Stop","stop_hook_active":false,"last_assistant_message":"HOOK_TEST_STOP_1E","background_tasks":[],"session_crons":[]}
```

`claude -p --output-format json` stdout (verbatim, redacted):
```json
{"duration_api_ms":1624,"stop_reason":"end_turn","session_id":"<redacted-uuid>","total_cost_usd":0.270235,"usage":{"input_tokens":2,"cache_creation_input_tokens":26980,"cache_read_input_tokens":0,"output_tokens":17,"output_tokens_details":{"thinking_tokens":0},"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":26980,"ephemeral_5m_input_tokens":0},"inference_geo":"not_available","iterations":[{"input_tokens":2,"output_tokens":17,"cache_read_input_tokens":0,"cache_creation_input_tokens":26980,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":26980},"type":"message"}],"speed":"standard"},"modelUsage":{"claude-opus-5[1m]":{"inputTokens":2,"outputTokens":17,"cacheReadInputTokens":0,"cacheCreationInputTokens":26980,"webSearchRequests":0,"costUSD":0.270235,"contextWindow":1000000,"maxOutputTokens":64000,"thinkingTokens":0,"canonicalModel":"claude-opus-5","provider":"firstParty","costBasis":"list"}},"permission_denials":[],"terminal_reason":"completed","fast_mode_state":"off","fast_mode_disabled_reason":"sdk_opt_in_required","subagent_stats":{"spawned":0,"requested":{"background":0,"foreground":0,"unset":0},"started_in_background":0,"max_depth":0,"spawned_by_subagents":0,"completed":0,"failed":0,"killed":{"parent":0,"user":0,"system":0},"refused":{"depth_limit":0,"concurrency_limit":0,"budget":0},"by_type":{}},"is_error":false,"num_turns":1,"subtype":"success","api_error_status":null,"result":"HOOK_TEST_STOP_1E","ttft_ms":1904,"type":"result","duration_ms":2105,"uuid":"<redacted-uuid>","ttft_stream_ms":1348,"time_to_request_ms":310,"queued_turn_count":0}
```

**Observation**: the `Stop` hook payload has NO `cost` field and NO `duration_ms` field. The
`total_cost_usd`, `usage`, and `duration_ms` fields that DO exist for this run live only in the
CLI's own stdout JSON (`--output-format json`), not in what the hook receives on stdin.

## Run 2 — repeat, confirm reproducibility

Command:
```
claude -p "Print exactly the string HOOK_TEST_STOP_1E_RUN2 and nothing else." --output-format json
```

`Stop` hook payload (verbatim, redacted) — same shape, same missing fields:
```json
{"session_id":"<redacted-uuid>","transcript_path":"C:\\Users\\vad\\.claude\\projects\\C--Users-vad-AppData-Local-Temp-claude-D--researchs-market-research-<redacted-uuid>-scratchpad-hook-test-1e\\<redacted-uuid>.jsonl","cwd":"C:\\Users\\vad\\AppData\\Local\\Temp\\claude\\D--researchs-market-research\\<redacted-uuid>\\scratchpad\\hook-test-1e","prompt_id":"<redacted-uuid>","permission_mode":"auto","effort":{"level":"high"},"hook_event_name":"Stop","stop_hook_active":false,"last_assistant_message":"HOOK_TEST_STOP_1E_RUN2","background_tasks":[],"session_crons":[]}
```

CLI stdout (verbatim, redacted) — `total_cost_usd` differs (0.0991635) from run 1, driven by cache-read
vs cache-creation mix (`cache_read_input_tokens: 18027` here vs `0` in run 1: run 1 paid to create a
1-hour prompt cache, run 2 read from it):
```json
{"duration_api_ms":1558,"stop_reason":"end_turn","session_id":"<redacted-uuid>","total_cost_usd":0.0991635,"usage":{"input_tokens":2,"cache_creation_input_tokens":8959,"cache_read_input_tokens":18027,"output_tokens":22,"output_tokens_details":{"thinking_tokens":0},"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":8959,"ephemeral_5m_input_tokens":0},"inference_geo":"not_available","iterations":[{"input_tokens":2,"output_tokens":22,"cache_read_input_tokens":18027,"cache_creation_input_tokens":8959,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":8959},"type":"message"}],"speed":"standard"},"modelUsage":{"claude-opus-5[1m]":{"inputTokens":2,"outputTokens":22,"cacheReadInputTokens":18027,"cacheCreationInputTokens":8959,"webSearchRequests":0,"costUSD":0.0991635,"contextWindow":1000000,"maxOutputTokens":64000,"thinkingTokens":0,"canonicalModel":"claude-opus-5","provider":"firstParty","costBasis":"list"}},"permission_denials":[],"terminal_reason":"completed","fast_mode_state":"off","fast_mode_disabled_reason":"sdk_opt_in_required","subagent_stats":{"spawned":0,"requested":{"background":0,"foreground":0,"unset":0},"started_in_background":0,"max_depth":0,"spawned_by_subagents":0,"completed":0,"failed":0,"killed":{"parent":0,"user":0,"system":0},"refused":{"depth_limit":0,"concurrency_limit":0,"budget":0},"by_type":{}},"is_error":false,"num_turns":1,"subtype":"success","api_error_status":null,"result":"HOOK_TEST_STOP_1E_RUN2","ttft_ms":1840,"type":"result","duration_ms":2018,"uuid":"<redacted-uuid>","ttft_stream_ms":1279,"time_to_request_ms":309,"queued_turn_count":0}
```

**Observation**: reproducible. Two independent runs, same `Stop` payload shape, cost/duration absent both times. Not a fluke.

## Run 3 — SubagentStop, one spawned subagent

Command:
```
claude -p "Use the Task tool to launch one general-purpose subagent with the instruction: print exactly SUBAGENT_TEST_1E and nothing else. Wait for it to finish, then report back exactly what it printed." --output-format json --permission-mode bypassPermissions --allowedTools "Task"
```

`Stop` hook payload for the parent turn (verbatim, redacted):
```json
{"session_id":"<redacted-uuid>","transcript_path":"...<redacted-uuid>...","cwd":"...","prompt_id":"<redacted-uuid>","permission_mode":"bypassPermissions","effort":{"level":"high"},"hook_event_name":"Stop","stop_hook_active":false,"last_assistant_message":"Subagent printed:\n\n```\nSUBAGENT_TEST_1E\n```\n\nExact match. No tool uses, 1.7s.\n\nAlso — caveman statusline badge not configured. Want me add it to `C:\\Users\\vad\\.claude\\settings.json`?","background_tasks":[],"session_crons":[]}
```
(Note: the trailing "caveman statusline badge" line is an unrelated stray suggestion generated by
this machine's global plugin config bleeding into the model's own reply text — not acted on, not
part of the hook schema; included here only because the capture is verbatim.)

`SubagentStop` hook payload for the spawned subagent (verbatim, redacted):
```json
{"session_id":"<redacted-uuid>","transcript_path":"C:\\Users\\vad\\.claude\\projects\\C--Users-vad-AppData-Local-Temp-claude-D--researchs-market-research-<redacted-uuid>-scratchpad-hook-test-1e\\<redacted-uuid>.jsonl","cwd":"C:\\Users\\vad\\AppData\\Local\\Temp\\claude\\D--researchs-market-research\\<redacted-uuid>\\scratchpad\\hook-test-1e","prompt_id":"<redacted-uuid>","permission_mode":"bypassPermissions","agent_id":"<redacted-id>","agent_type":"general-purpose","effort":{"level":"high"},"hook_event_name":"SubagentStop","stop_hook_active":false,"agent_transcript_path":"C:\\Users\\vad\\.claude\\projects\\C--Users-vad-AppData-Local-Temp-claude-D--researchs-market-research-<redacted-uuid>-scratchpad-hook-test-1e\\<redacted-uuid>\\subagents\\agent-<redacted-id>.jsonl","last_assistant_message":"SUBAGENT_TEST_1E","background_tasks":[],"session_crons":[]}
```

CLI stdout for the whole invocation (verbatim, redacted) — note `subagent_stats` block:
```json
{"duration_api_ms":7700,"stop_reason":"end_turn","session_id":"<redacted-uuid>","total_cost_usd":0.259276,"usage":{"input_tokens":4,"cache_creation_input_tokens":10972,"cache_read_input_tokens":45052,"output_tokens":344,"output_tokens_details":{"thinking_tokens":104},"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":10972,"ephemeral_5m_input_tokens":0},"inference_geo":"not_available","iterations":[{"input_tokens":2,"output_tokens":88,"cache_read_input_tokens":27025,"cache_creation_input_tokens":1974,"cache_creation":{"ephemeral_5m_input_tokens":0,"ephemeral_1h_input_tokens":1974},"type":"message"}],"speed":"standard"},"modelUsage":{"claude-opus-5[1m]":{"inputTokens":6,"outputTokens":360,"cacheReadInputTokens":45052,"cacheCreationInputTokens":29852,"webSearchRequests":0,"costUSD":0.259276,"contextWindow":1000000,"maxOutputTokens":64000,"thinkingTokens":104,"canonicalModel":"claude-opus-5","provider":"firstParty","costBasis":"list"}},"permission_denials":[],"terminal_reason":"completed","fast_mode_state":"off","fast_mode_disabled_reason":"sdk_opt_in_required","subagent_stats":{"spawned":1,"requested":{"background":0,"foreground":1,"unset":0},"started_in_background":0,"max_depth":1,"spawned_by_subagents":0,"completed":1,"failed":0,"killed":{"parent":0,"user":0,"system":0},"refused":{"depth_limit":0,"concurrency_limit":0,"budget":0},"by_type":{"general-purpose":1}},"is_error":false,"num_turns":2,"subtype":"success","api_error_status":null,"result":"Subagent printed:\n\n```\nSUBAGENT_TEST_1E\n```\n\nExact match. No tool uses, 1.7s.\n\nAlso — caveman statusline badge not configured. Want me add it to `...`?","ttft_ms":3030,"type":"result","duration_ms":8324,"uuid":"<redacted-uuid>","ttft_stream_ms":1298,"time_to_request_ms":321,"queued_turn_count":0}
```

**Observation — critical for candidate C**: `SubagentStop` carries `agent_id` and `agent_type`
(useful identifiers) and `agent_transcript_path` (a pointer to a per-subagent JSONL file), but
**no cost field and no duration_ms field**, same as `Stop`. The top-level CLI JSON's
`subagent_stats` block gives `spawned`/`completed`/`failed`/`killed`/`refused` COUNTS and a
`by_type` breakdown, but no per-subagent dollar figure — it is an aggregate count block, not a
per-agent cost ledger.

### Following `agent_transcript_path` — does the pointed-to file carry cost?

Read directly (redacted excerpt, one assistant-message line from the subagent's own transcript
JSONL):
```json
{"parentUuid":"<redacted-uuid>","isSidechain":true,"agentId":"<redacted-id>","message":{"model":"claude-opus-5","id":"<redacted-message-id>","type":"message","role":"assistant","content":[{"type":"text","text":"SUBAGENT_TEST_1E"}],"container":null,"stop_reason":"end_turn","stop_sequence":null,"stop_details":null,"usage":{"input_tokens":2,"cache_creation_input_tokens":18880,"cache_read_input_tokens":0,"output_tokens":16,"output_tokens_details":{"thinking_tokens":0},"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":0,"ephemeral_5m_input_tokens":18880},"inference_geo":"not_available","iterations":[{"input_tokens":2,"output_tokens":16,"cache_read_input_tokens":0,"cache_creation_input_tokens":18880,"cache_creation":{"ephemeral_5m_input_tokens":18880,"ephemeral_1h_input_tokens":0},"type":"message"}],"speed":"standard"},"diagnostics":null,"context_management":null},"apiBlockIndex":0,"requestId":"<redacted-request-id>","attributionAgent":"general-purpose","type":"assistant","uuid":"<redacted-uuid>","timestamp":"2026-09-17T07:55:32.823Z","effort":"high","userType":"external","entrypoint":"sdk-cli","cwd":"...","sessionId":"<redacted-uuid>","version":"2.1.259","gitBranch":"HEAD"}
```

**Observation**: the per-subagent transcript file DOES carry per-message token `usage`
(input/output/cache-read/cache-creation) plus `model` (`claude-opus-5`) and `attributionAgent`
(`general-purpose`). It does NOT carry a dollar cost field or a `duration_ms` field anywhere —
confirmed by exhaustive grep of both the main session transcript (31 lines) and this subagent
transcript (6 lines): `grep -c "costUSD"` = 0, `grep -o '"duration_ms"'` = 0 matches, in both files.
So per-subagent dollar-cost attribution is possible **only** as a build-it-yourself step: hook
gives you `agent_transcript_path`, you parse its `usage` objects, you multiply by an externally-known
per-model price table. Claude Code does not do this arithmetic for you at the subagent level, and
does not hand you a subagent-level `duration_ms` at all — you would have to derive wall time from
the transcript's own `timestamp` fields (first vs. last line) if you need it.

## Run 4 — permission-denial shape (secondary check)

Command:
```
claude -p "Run the shell command 'echo denied_test' using the Bash tool." --output-format json --disallowedTools "Bash" --permission-mode acceptEdits
```

Result: `Bash` was removed from the tool list entirely (not "denied at call time") — the model
just reported it had no Bash tool and never attempted the call. `permission_denials` stayed `[]`
in the CLI JSON, and the `Stop` payload was the same shape as runs 1-2 (no cost/duration). This
is a negative result, not a positive one: disallowing a tool via `--disallowedTools` does not
exercise the `PermissionRequest`/`PermissionDenied` hook path — that requires a tool that IS
offered but whose call is denied at request time, which needs an interactive-style denial this
harness did not attempt (out of scope: constraint says no interactive prompts, and the two
existing docs already agree on `PermissionRequest`/`PermissionDenied` as the mechanism — this run
only confirms `permission_denials` is a real, populated-when-relevant field, empty here because
nothing was denied).

## Alternative paths — tested, not read

### `--output-format json` (see runs 1-4 above)

Confirmed working. Fields present in every run: `total_cost_usd` (float, USD), `usage` (object:
`input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`,
`output_tokens_details.thinking_tokens`, `server_tool_use.{web_search_requests,web_fetch_requests}`),
`modelUsage` (per-model breakdown incl. `costUSD`, `contextWindow`, `maxOutputTokens`,
`canonicalModel`, `provider`, `costBasis":"list"`), `duration_ms` (int, wall time for the whole
invocation), `duration_api_ms` (int, time spent in API calls specifically), `session_id`,
`num_turns`, `subagent_stats` (spawn/complete/fail/kill/refuse counts + `by_type`),
`permission_denials` (array), `terminal_reason`, `stop_reason`, `result` (the final text),
`uuid`, `ttft_ms`/`ttft_stream_ms`/`time_to_request_ms`, `queued_turn_count`,
`fast_mode_state`/`fast_mode_disabled_reason`. **Granularity: one JSON blob per whole `claude -p`
invocation** — not per turn, not per subagent, not per tool call.

### `/usage` CLI equivalent

`claude --help` (full text captured, v2.1.259) lists these top-level commands: `agents`, `attach`,
`auth`, `auto-mode`, `doctor`, `gateway`, `import`, `install`, `logs`, `mcp`, `plugin|plugins`,
`project`, `respawn`, `rm`, `setup-token`, `stop|kill`, `ultrareview`, `update|upgrade`. **No
`usage` subcommand and no `--usage` flag exist.** `/usage` is a session-scoped interactive slash
command; no headless/CLI equivalent was found in this version. Not tested further — constraint
bars triggering interactive prompts, and an interactive-only feature cannot be exercised headlessly
by definition. Recorded as **untestable in headless mode, confirmed absent from `--help`**, not
"not found because we didn't look."

### Local files under `C:\Users\vad\.claude\` (the ccusage-equivalent question)

Checked live on this machine (redacted where needed):

- **`stats-cache.json`** (26KB) — a lifetime rolling-aggregate cache, NOT per-task or per-session.
  Top-level keys: `version`, `lastComputedDate`, `dailyActivity` (per-calendar-day
  `messageCount`/`sessionCount`/`toolCallCount` — no cost), `dailyModelTokens`,
  `dailyModelTokensVersion`, `modelUsage` (per-model **lifetime cumulative** token counts —
  `inputTokens`, `outputTokens`, `cacheReadInputTokens`, `cacheCreationInputTokens`,
  `webSearchRequests`, and a `costUSD` field that was **`0` for every model** on this machine,
  plus `contextWindow: 0` and `maxOutputTokens: 0` — i.e. this cache does not compute cost at
  all, the field exists but is unpopulated), `totalSessions` (894), `totalMessages` (118856),
  `longestSession` (a single record: `sessionId`, `timestamp`, `duration` in ms, `messageCount` —
  only the ONE longest session, not a per-session log), `firstSessionDate`, `hourCounts`.
- **`history.jsonl`** (1.1MB) — command-line input history only: `display` (the typed text),
  `pastedContents`, `timestamp`, `project`, `sessionId`. No cost, no duration, no token counts.
- **`cache/`** directory — a changelog markdown cache and a small GitHub-issues cache file,
  unrelated to cost/usage.
- Session transcripts live at `C:\Users\vad\.claude\projects\<slug>\<session-id>.jsonl` (main) and
  `...\<session-id>\subagents\agent-<agent-id>.jsonl` (per-subagent). Confirmed above: these carry
  per-message `usage` token objects and `model`, but **zero occurrences of `costUSD` or
  `duration_ms`** anywhere in either file type (grepped both transcript files from run 3
  exhaustively — 0 matches each). This is almost certainly the exact file an external tool like
  `ccusage` reads: it must reconstruct dollar cost itself from `usage` + `model` + its own
  hard-coded pricing table, because Claude Code does not write a cost figure into the transcript.

**Conclusion on this item**: there is no local Claude Code-maintained file that already contains
a per-task dollar-cost ledger. The transcripts contain the raw ingredients (tokens + model id);
everything past that (pricing, aggregation, dollarization) is the reading tool's own logic, not
something Claude Code computed and persisted.

## Caveats specific to this measurement

- Single machine, single Claude Code version (2.1.259), single auth mode (interactive OAuth). Not
  tested: `--bare` mode, `ANTHROPIC_API_KEY` mode, OTel export (would require standing up a
  collector — out of scope for "trivial, few" runs), a genuinely denied permission request (see
  run 4 note), `StopFailure` (would require forcing an actual API failure), stream-json mode's
  `system/api_retry` event.
- `total_cost_usd` / `costUSD` are, per the CLI's own labeling elsewhere (already documented in
  `claude-code-substrate.md`), client-side list-price estimates — this pull did not independently
  re-verify that specific caveat, only confirmed the field's presence/absence pattern.
- The stray "caveman statusline badge" suggestion appearing inside `last_assistant_message` in
  runs 3-4 is this machine's own global plugin config leaking into the model's free-text reply —
  not a Claude Code telemetry field, not acted on, kept in the capture only because the brief asks
  for stdin/stdout verbatim.

## Housekeeping

Throwaway dir and its `.claude\settings.json` were used only for this measurement and are
confined to the scratchpad path named above; nothing was written to
`C:\Users\vad\.claude\settings.json` or any other global/user config at any point.
