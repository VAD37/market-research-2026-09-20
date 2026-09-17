# Raw — interrogation of the 828 "usage limit" issues

Pull date: **2026-09-17**. Agent: wave 2a-bis (re-pick).
Method: authenticated GitHub CLI, `gh version 2.90.0 (2026-04-16)`, account `VAD37`, token scopes `gist, read:org, repo, workflow`. All counts are `GET /search/issues` `.total_count`; all per-issue rows are `GET /repos/anthropics/claude-code/issues/<n>`. No relay — every figure below was returned to this agent directly.
Purpose: wave 2b established 828 title-scoped issues as the only direct demand evidence in this project. This pull asks what those issues **say**, not how many there are.

Raw is exempt from compression per `../../../CLAUDE.md`.

---

## 1. Counts reproduced

`repo:anthropics/claude-code`, title-scoped:

```
"usage limit" in:title                   828
"usage limit" in:title state:open        101
"usage limit" in:title state:closed      727
"usage limit" in:title is:issue          822
"rate limit"  in:title                   733
"weekly limit" in:title                  234
"budget" in:title                        153
"cost" in:title                          355
"spend" in:title                          98
in:title                              93,582   <- repo total
```

2b's 828 / 733 / 234 / 153 / 355 all reproduce exactly.

**New: the denominator.** 828 / 93,582 = **0.88%** of all titled issues in the repo.

**New: open vs closed.** 727 of 828 (**87.8%**) are closed.

## 2. Is 828 a large number in this repo?

Same repo, same title-scoped method, same pull date:

```
"windows"     in:title   5530
"mcp"         in:title   4806
"context"     in:title   4314
"hook"        in:title   2901
"permission"  in:title   2768
"skill"       in:title   2258
"crash"       in:title   2064
"subagent"    in:title   1797
"memory"      in:title   1424
"vscode"      in:title   1370
"usage limit" in:title    828   <- lowest of the eleven sampled
```

"usage limit" ranks **last of eleven** comparable topics sampled. It is a real, dated, filed signal; it is not an unusually large one for this tracker.

## 3. What the issues are: label tally over the 300 most recently created

`-f sort=created -f order=desc`, pages 1-3, 300 rows.

```
bug              144        stale            143
area:cost        131        duplicate         73
enhancement       57        needs-info        14
platform:macos    78        has repro         11
platform:windows  50        invalid           10
platform:linux    20        needs-repro        6
```

State within the 300: **224 closed / 76 open.**

Engagement within the 300: 40 issues with 0 comments, 65 with 1, 73 with 2, 71 with 3. **Median 2 comments.** Maximum in the sample: 35.

Read: ~48% carry `bug`, ~48% carry `stale`, ~24% carry `duplicate`, ~19% carry `enhancement`.

## 4. The highest-engagement issues in the whole 828

`-f sort=reactions -f order=desc` and `-f sort=comments -f order=desc`, top rows, verbatim titles:

| # | state | created | comments | reactions | title |
|---|---|---|---|---|---|
| 16157 | open | 2026-01-03 | 1495 | 725 | [BUG] Instantly hitting usage limits with Max subscription |
| 38335 | open | 2026-03-24 | 855 | 545 | [BUG] Claude Max plan session limits exhausted abnormally fast since March 23, 2026 (CLI usage) |
| 9424 | closed | 2025-10-12 | 110 | 155 | Weekly Usage Limits Making Claude Subscriptions Unusable |
| 41930 | closed | 2026-04-01 | 108 | 97 | [BUG] Critical: Widespread abnormal usage limit drain across all paid tiers since March 23, 2026 — multiple root causes identified, no formal communication issued |
| 29579 | open | 2026-02-28 | 153 | 94 | [BUG] API Error: Rate limit reached despite Claude Max subscription and only 16% usage |
| 19673 | open | 2026-01-21 | 102 | 77 | You've hit your limit · While usage is still at 84% |
| 16270 | open | 2026-01-04 | 40 | 72 | [BUG] Usage limits bugged after double limits expired on new years. |
| 9094 | closed | 2025-10-07 | 121 | 60 | [Meta] Unexpected change in Claude usage limits as of 2025-09-29. (30+ reports) |
| **20636** | **closed** | 2026-01-24 | 11 | **59** | **Expose rate limit usage (session %, weekly %) to statusLine configuration** |
| 17084 | open | 2026-01-09 | 39 | 56 | [BUG] Opus 4.5 usage limits significantly reduced since January 2026 - most restrictive since Opus 4.5 launch |
| 78610 | open | 2026-07-17 | 14 | 49 | [Bug] Incorrectly Prompts for API Credits Despite Active Subscription Usage Limit |
| 3138 | open | 2025-07-08 | 18 | 45 | [BUG] resume flag fails to maintain conversation context after hitting usage/context limits |

Every one of the top eight by reactions is a **bug report against Anthropic's own metering** — the meter fires early, jumps with no activity, or disagrees with itself across surfaces. None is a request for a third-party tool.

The highest-reaction **feature request** in the 828 is #20636. Its per-issue record:

```
20636  closed  state_reason=completed  created 2026-01-24  closed 2026-04-24  11 comments  59 reactions
       "Expose rate limit usage (session %, weekly %) to statusLine configuration"
```

**Anthropic shipped it, free, three months after it was filed.**

## 5. The 57 `enhancement`-labelled issues in the 300-row sample

Grouped by this agent (grouping is inference; the titles are verbatim).

**Group 1 — "expose the data so external tooling can read it"** (~18 of 57):
`#94424` *"Function hooks: an event when session usage or a rate-limit window changes, so trackers do not have to poll"*; `#91279` *"Expose session/weekly usage-limit percentages via a local CLI command or cache file"*; `#88781` *"[FEATURE] Expose usage-credit state to the session (status line payload)…"*; `#78476` *"expose subscription usage percentages headlessly (stream-json rate_limit_event or `claude usage --json`)"*; `#77453`, `#76791`, `#67797`, `#65672`, `#64476`, `#60764`, `#60674`, `#67748`, `#89993`, `#94686`, `#76007`, `#78362`, `#80261`, `#20636`.
These ask the vendor for a free primitive. #94424's wording, verbatim, *"so trackers do not have to poll"*, presupposes trackers already exist and are free.

**Group 2 — resume / continue / suspend after the wall** (~10): `#85923`, `#79127`, `#78224`, `#62788`, `#74196`, `#68815`, `#91449`, `#94222`, `#69091`, `#67754`. Mostly closed. `autoContinueAtUsageLimit` shipped (per `../docs/review/market-check.md` §5); the open remainder are bug reports against it.

**Group 3 — the limits themselves are too tight / opaque / unfair** (~7): `#93940` *"Max Pro plan: weekly usage limits feel too restrictive for normal single-developer use"*; `#94586`; `#76006`; `#61906`; `#91282`; `#90152` *"Let individual subscribers gift or pool unused usage limits"*; `#91721`. Addressable only by Anthropic changing policy.

**Group 4 — banner / UI nits** (~7): `#79994`, `#76000`, `#65396`, `#72994`, `#62807`, `#69812`, `#71583`. Vendor-only.

**Group 5 — pre-emptive, budget-aware pacing (candidate H's surviving function (b))** (~5-6):
```
#90479  open    2026-08-28  0 comments  0 reactions
        "Surface plan usage limits to the agent for budget-aware planning"
#65524  closed  state_reason=not_planned  created 2026-06-05  closed 2026-07-09  1 comment  0 reactions
        "Expose current usage / limit state to the model (self-pacing for long autonomous runs)"
#67148  closed  "[Feature Request] Usage limits and rate limiting safeguards for agentic operations"   2 comments
#69091  closed  "[FEATURE] durable sub-agent execution log + limit-aware dispatch…"                    3 comments
#76133  closed  state_reason=not_planned  "Max 20x subscriber rate-limited within usage limits during Claude Code subagent orchestration (no early warning / no budget visibility)"  4 comments  1 reaction
#89198  open    "[Feature Request] Per-model usage credit limits configuration"                        0 comments
```
`#65524` — the request for exactly the primitive H(b) would consume — was **closed `not_planned` on 2026-07-09**, with 1 comment and 0 reactions.

## 6. Title-scoped volume for H's surviving function specifically

```
"queue"       in:title   261
"defer"       in:title   170
"pace"        in:title    14
"pacing"      in:title     8
"budget-aware" in:title     4
"self-pacing" in:title     3
"pre-emptive" in:title     1
```

## 7. The "queue" 261 does not mean what H needs

Top `"queue" in:title` by reactions:

```
#50246  closed  state_reason=completed  2026-04-18   71c  242r  "Feature Request: Message queue mode — queue messages instead of interrupting active tasks"
#30677  open                            2026-03-04   22c   60r  "[FEATURE] VS Code Extension: Support queued message sending instead of interrupting current task"
#33323  open                            2026-03-11   19c   49r  "[FEATURE] Task queue for queuing multiple prompts/tasks"
#535    closed  state_reason=not_planned 2025-03-16  15c   30r  "Feature request: The ability to queue up messages"
#34835  closed  state_reason=completed  2026-03-16   21c   28r  "[FEATURE] The ability to queue up messages.via asking the user for further info on user input."
#71726  closed  state_reason=completed  2026-06-27   13c   21r  "[FEATURE] Desktop app: inject queued messages mid-task between tool calls (CLI steering parity)"
#64624  closed  state_reason=completed  2026-06-02   11c   18r  "Feature: Real-time steering — send message mid-generation without queueing"
#63190  open                            2026-05-28    8c   14r  "[FEATURE] Deferred Messages — Queue Input for End of Turn"
```

These are about **typing a second prompt while the first runs** (interactive steering), not about deferring work ahead of a usage-window wall. Four of the eight are `state_reason=completed`, including the 242-reaction top item.

**Correction against `../docs/review/market-check.md` §5, made with a new pull:** 2b records #33323 as *"auto-closed by a stale bot"*. First-hand as of 2026-09-17 its state is **`open`**, 19 comments, 49 reactions, `state_reason` null. Recorded side by side, not averaged; 2b may have read a prior state or a bot comment on an open issue.

## 8. The `"budget" in:title` 153 is contaminated

```
"budget"          in:title   153
"token budget"    in:title    46
"context budget"  in:title    40
"thinking budget" in:title    16
```

Top 20 `"budget"` issues by reactions, read one by one: ~14 concern **thinking-budget or context-window budget**, not dollar spend (e.g. #8756 *"max_tokens must be greater than thinking.budget_tokens"*, 34 reactions; #39465 *"2 PERCENT OF BUDGET USED BY ASKING ABOUT BUDGET USE"*; #56710 *"Skill descriptions truncated due to context budget constraints"*). Dollar-spend budget is a minority of the 153.

## 9. Free-tool ceiling and floor, re-verified first-hand

```
ccusage/ccusage                              18,591 stars   838 forks   pushed 2026-09-17  created 2025-05-29   12 open issues   license NOASSERTION
                                             no .github/FUNDING.yml found (404)
Maciek-roboblog/Claude-Code-Usage-Monitor     8,707 stars   MIT         pushed 2026-07-05
Star001-KR/claude-session-budget                  8 stars     1 fork    pushed 2026-05-15  created 2026-05-09
```

`claude-session-budget` is the only free implementation of H's surviving function (b) per 2b §5. It was **created 2026-05-09 and last pushed 2026-05-15** — six days of work, then untouched for four months as of this pull.

`ccusage` is the category leader at 18,591 stars with **no funding file**. Star counts and funding absence are both facts about visibility and about the author's choices; neither is a revenue measurement. `unknown — no revenue figure found for any tool in this category, checked GitHub 2026-09-17`.

## 10. Wave 1e's file

`docs/explore/telemetry-measured.md` — **absent** as of `2026-09-17T07:58:15Z`. `docs/explore/` contains six files: `claude-code-substrate.md`, `control-planes.md`, `gap-pulls.md`, `hermes-substrate.md`, `smallbiz-blind-spots.md`, `task-telemetry.md`.

## Caveats on this pull

- GitHub `search/issues` `total_count` counts a title substring, not a curated request. 2b's caveat applies unchanged to every count here, including the eleven-topic denominator comparison in §2 — those are substring counts too, and their comparability rests on all eleven being single common words or phrases pulled the same way.
- The eleven comparison topics in §2 were chosen by this agent. They are not a random sample of repo topics and a different eleven would give a different ranking. The defensible claim is the ratio to the repo total (0.88%) and that ten common topics all exceed it, not a precise rank.
- The 300-row label tally is the 300 **most recently created**, not a random sample of 828. Recent issues are more likely to be open and less likely to be stale-closed, so the 87.8% overall closure rate is the better figure for the full set.
- §5's five-group taxonomy is this agent's grouping. Issue titles are verbatim; the groups are inference and should be labelled as such downstream.
- No issue body was fetched by this agent. Titles, labels, states, comment counts and reaction counts only. 2b's relayed body quotes are not re-verified here.
- Reaction and comment counts measure GitHub, on the days people looked. Per `../../../docs/findings/market-gaps-2026.md:93`, engagement counts are visibility proxies, not demand measurements.
</content>
