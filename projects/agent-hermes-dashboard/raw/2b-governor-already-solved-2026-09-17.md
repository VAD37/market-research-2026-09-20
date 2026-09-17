### Source: does candidate H (cost-and-limit governor) already exist, free?

- Pull date: 2026-09-17
- Method: delegated breadth leg across primary Anthropic docs, GitHub search API, raw READMEs, PyPI, npm, Grafana Labs and two commercial vendor sites. Wave 2b then **re-verified first-hand** every kill-grade datapoint: repo stats via the authenticated `gh` CLI (`gh api repos/<owner>/<repo>`), and the `--max-budget-usd` flag via direct fetch of Anthropic's CLI reference.
- Candidate H's four claimed functions, tested separately: (a) watch the rolling 5-hour/weekly window and report headroom; (b) defer/queue/pause work *before* the wall; (c) kill runaway spend / enforce a budget cap; (d) attribute cost and duration per task.

---

## PART 1 — FIRST-HAND VERIFICATION BY WAVE 2b

### (c) is a built-in CLI flag. Primary source, fetched 2026-09-17 from https://code.claude.com/docs/en/cli-reference

> `--max-budget-usd` — "Maximum dollar amount to spend on API calls before stopping (**print mode only**). Spend from subagents counts toward the cap. Once spend reaches the cap, spawning another subagent fails with `Budget limit reached`, and Claude Code stops background subagents that are still running; the cap-enforcement behaviors require Claude Code **v2.1.217 or later**"
>
> Example given in the docs: `claude -p --max-budget-usd 5.00 "query"`

Print mode (`claude -p`) is exactly the mode candidate H targets for unattended runs. The same fetch confirms: "There are no other flags in the provided documentation relating to budget, cost, spend, or usage limits. The only flag addressing session limits is `--max-turns`."

### Repo statistics — verified first-hand via `gh api`, 2026-09-17

| Repo | Stars | Last push | License | Archived |
|---|---|---|---|---|
| ccusage/ccusage | **18,591** | 2026-09-17 (same day) | Other | false |
| Maciek-roboblog/Claude-Code-Usage-Monitor | **8,707** | 2026-07-05 | MIT | false |
| howincodes/claude-code-limiter | 53 | 2026-03-25 | MIT | false |
| Star001-KR/claude-session-budget | 8 | 2026-05-15 | MIT | false |
| outbit/claude-code-tokenbudget | 2 | 2026-05-09 | MIT | false |

`gh api` descriptions, verbatim:
- Maciek-roboblog/Claude-Code-Usage-Monitor: "Real-time Claude Code usage monitor with predictions and warnings"
- howincodes/claude-code-limiter: "Per-user rate limits for Claude Code — share one subscription across your team with enforced quotas, credit budgets, and a real-time dashboard"
- outbit/claude-code-tokenbudget: "Claude code plugin to implement a budget or quota across all backends (Bedrock, Vertex, direct API) and provides guardrails against surprise token costs. No surprise bills, no config beyond a single env var, no external dependencies."

---

## PART 2 — RELAY FROM THE DELEGATED LEG (quotes not re-fetched by wave 2b)

### Function matrix

| Function | Claude Code built-in | Best free OSS | Commercial |
|---|---|---|---|
| (a) watch window, report headroom | YES — `/usage` | YES — Claude-Code-Usage-Monitor, 8,707★ | PARTIAL — SessionWatcher, $6.99-$59 one-time |
| (b) defer/pause *before* the wall | PARTIAL — `autoContinueAtUsageLimit` resumes *after* | YES but tiny — claude-session-budget, 8★ | NO |
| (c) budget cap / kill runaway spend | **YES — `--max-budget-usd`** (print mode, v2.1.217+) | YES — claude-code-limiter 53★; claude-code-tokenbudget 2★ | NO |
| (d) per-task cost + duration attribution | YES — `/usage` Attribution + OTel | YES — free Grafana dashboard #25255 | NO |

### Primary-doc quotes relayed by the delegated leg

From https://code.claude.com/docs/en/costs:
> "each member's Claude Code usage draws from a per-seat allowance that resets on a rolling five-hour window and a weekly window."
> "**Attribution**: recent usage attributed to skills, subagents, plugins, and individual MCP servers, each shown as a percentage of the total."
> "Subscribers see plan usage bars, activity stats, and a usage breakdown on the same screen."

From https://code.claude.com/docs/en/settings-reference:
> `autoContinueAtUsageLimit` — "Wait in the open session and continue the task automatically after a claude.ai usage limit resets"
> `modelPricing` — "Report spend at your organization's contracted rates instead of list price"

From https://code.claude.com/docs/en/monitoring-usage:
> `claude_code.cost.usage` — "Cost of the Claude Code session" (USD), per API request, with attributes `model`, `query_source` ("main"/"subagent"/"auxiliary"), `agent.name`, `skill.name`, `plugin.name`, `mcp_server.name`/`mcp_tool.name`.
> `claude_code.token.usage` — same attribution set, `type`: input/output/cacheRead/cacheCreation.
> `claude_code.active_time.total` — "Total active time" (s).

**A correction the delegated leg surfaced against this project's own explore layer**: neither the `Stop` nor the `SubagentStop` hook input JSON documents a cost or duration field on the current hooks page. Cost for a hook to act on has to be sourced separately (JSONL parsing), not read off the hook payload. This contradicts `docs/explore/task-telemetry.md` and `docs/plan/idea-set.md` fact 1, which cite `raw/claude-code-docs-2026-09-17.md` L130 / L38-39 for `cost: {input_tokens, output_tokens}` and `duration_ms` on `Stop`/`SubagentStop`. **Unresolved — two docs reads of the same page disagree, and neither wave measured it live.** `docs/plan/idea-set.md` attack item #5 (never measured live) remains open and is now actively contested.

### README quotes relayed by the delegated leg

- ccusage: "⏰ **5-Hour Blocks Report**: Track usage within Claude's billing windows with active block monitoring". The leg grepped the README for block/pause/queue/defer/budget/cap/kill — none present, so ccusage is (a)+(d) reporting only.
- Claude-Code-Usage-Monitor: "Official-limit trust layer — `--statusline` captures Claude Code's official `rate_limits`; stale or expired captures fall back to labeled local estimates." / "`--once` exits with automation-friendly codes: `0` ok, `10` near limit, `11` limit hit"
- claude-code-limiter: "Claude Code has zero built-in usage controls. No per-user limits. No quotas... claude-code-limiter gives you a complete usage control layer... Kill switch — instantly revoke access and force logout, remotely."
- claude-session-budget: "Track Claude Code's 5-hour session usage locally — and **automatically pause task queues before hitting the limit**." / "≥ 93% → ⏸ Block dispatch until 5-hour session resets."
- claude-code-tokenbudget: "Claude Code has no built-in spending guardrails. This plugin tracks your token usage and hard stops new prompts once you hit your limit."
- ClaudeBar (1,495★, pushed 2026-09-14): "Each provider displays separate progress bars for multiple quota windows—for example, tracking your 5-hour session quota and 7-day weekly quota simultaneously with dedicated countdown timers."
- ccflare (1,046★) checked and **ruled out**: a multi-account API-key proxy/load-balancer, not a subscription usage governor.

### Commercial

- Grafana Labs community dashboard #25255, "Claude Code Metrics (Prometheus)", built on Anthropic's own OTel export, free: "Leaderboards: top users by cost/tokens, top sessions by cost, cost by model" and "Cost Breakdown: cost by query source, cost by effort". https://grafana.com/grafana/dashboards/25255-claude-code-metrics-prometheus/
- SessionWatcher, https://sessionwatcher.com/claude — $6.99-$59 one-time, tracks "5-hour, weekly & Fable 5 limits", monitoring only.
- CrewTower, https://crewtower.app/ — the delegated leg found no budget-cap or spend-enforcement feature listed on its pricing page. **It did not confirm the $9.99 one-time figure that `docs/plan/idea-set.md` and `docs/explore/control-planes.md` cite as candidate H's price ceiling.** That figure remains `unknown — vendor page checked 2026-09-17, price not re-confirmed`.

## PART 3 — WHAT WAS NOT CHECKED

- CrewTower and SessionWatcher feature depth: marketing pages only, not the binaries. "No budget cap" is absence of a claim, not a tested absence.
- `settings-reference` was not exhaustively re-read row by row; an obscure additional budget-named setting could exist unseen.
- Dubibubii/usage-limit-reducer (193★) and ridelink0/claude-code-usage-limits (0★): READMEs not fetched verbatim, search-snippet only.
