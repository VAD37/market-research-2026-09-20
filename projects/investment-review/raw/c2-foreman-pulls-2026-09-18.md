# §C2 pulls — `Foreman` (`agent-hermes-dashboard`) — 2026-09-18

Stage 2 pull per `projects/investment-review/FRAMEWORK.md` §C2. Read first: `FRAMEWORK.md` (whole, incl. §B, C2, F), `projects/agent-hermes-dashboard/docs/outcome/success-vision.md`, `docs/plan/re-pick.md`, `docs/execution/e2e-test.md`, and `projects/agent-hermes-dashboard/raw/` (listed below). One H3 per §C2 line, in §C2 order, heading = the line's own text verbatim. No git run. No browser/Chrome tools used — WebSearch and WebFetch only, per instructions. Today: 2026-09-18.

Already-on-file raw checked before pulling (per project's own `raw/`): `2abis-demand-signal-interrogation-2026-09-17.md`, `claude-code-docs-2026-09-17.md`, `hook-payload-measurement-2026-09-17.md`, `hermes-agent-github-2026-09-17.md`, `control-planes-pulls.md`, `gap1..4-*-2026-09-17.md`, `smallbiz-blind-spots-pulls.md`, `2b-*-2026-09-17.md`. All dated 2026-09-17 — one day old, but every vendor-stated or docs-derived number in them was re-verified live per instructions (vendor-stated numbers are re-checked regardless of age); measured-by-us numbers from live runs on this machine were cited by path, not re-run.

---

### 1. **A6 KILL** — Does `/insights` list repeated prompts / recurring work / suggest skills — run `/insights` on this machine and paste the report headings; code.claude.com/docs/en/insights — `measured-by-us`; if it does, Foreman's only checkable claim is the emitted file

**requires-main-thread** — running `/insights` requires an interactive Claude Code session on this machine; this pull agent cannot start one (same category as the framework's own `/insights`-inspection caveat). Not pulled as a live run.

What the live docs say instead, fetched fresh 2026-09-18 (the exact URL in the C2 line, `code.claude.com/docs/en/insights`, 404s — the command is documented inside `commands.md` and `costs.md`):

- **"Generate an HTML report analyzing your recent sessions on this machine: which projects you work in, how you use Claude Code, where things go wrong, and features to try."** — vendor-reported, `code.claude.com/docs/en/commands.md`, fetched 2026-09-18.
- **"Run `/insights` for a report on how you work rather than how many tokens you've used. It analyzes your recent sessions on this machine and writes an HTML report covering what you work on, friction points such as misunderstood requests or buggy code, and suggestions for using Claude Code more effectively. A single run analyzes up to 200 sessions it hasn't seen before and skips very short ones."** — vendor-reported, `code.claude.com/docs/en/costs.md` §"Analyze your usage patterns", fetched 2026-09-18. Report written to `~/.claude/usage-data/report.html`, timestamped copies kept, deleted after `cleanupPeriodDays` (default 30 days).
- Neither doc page uses the words "recurring", "repeated", "pattern", or "suggest a skill/command" — the described output is friction points and general effectiveness suggestions, not a recurrence-detection report. This is a docs-only reading, not an inspection of real output; the report's actual section headings remain unknown until someone runs it.
- Already on file, consistent: `projects/agent-hermes-dashboard/raw/claude-code-docs-2026-09-17.md` L61 pulled the same `costs.md` passage one day earlier with identical wording — the docs did not change between 2026-09-17 and 2026-09-18.

### 2. **A6 KILL** — Has Claude Code shipped recurrence detection or "suggest a skill/command from history" — changelog `github.com/anthropics/claude-code` CHANGELOG 2026-06..09, release notes — `vendor-reported`; if it does, Foreman's only checkable claim is the emitted file

- **No matching entry found** — vendor-reported, `github.com/anthropics/claude-code/blob/main/CHANGELOG.md` (raw file fetched in full, 7,063 lines, versions 2.1.179 through 2.1.276 — current top-of-file version as of 2026-09-18), fetched via `curl` to the raw file and grepped for `recur|pattern|history\.jsonl|suggest.*(skill|command)|/insights`. Every `/insights`-tagged entry across the whole file is a bug fix (crash on Bedrock/Vertex/Foundry accounts, literal `<message>` tag leak, crash on malformed tool-call fields, `EBUSY` crash on Windows, missing report-file link) — none adds recurrence detection or history-based suggestion.
- Closest near-misses, both unrelated to the claim: **"Added CLI tool usage detection to plugin tips, in addition to file pattern matching"** (plugin-discovery tips based on which CLI tools you run, not a recurring-task ledger) and **"Added `/loop` command to run a prompt or slash command on a recurring interval"** plus **"Added cron scheduling tools for recurring prompts within a session"** — both are forward scheduling (you tell it what to repeat), the opposite mechanism from Foreman's backward detection (it tells you what you already repeated).
- **Verdict on this line: not shipped, as of 2026-09-18.** Confirms and extends the already-on-file finding (`docs/plan/re-pick.md` §2b/1e) that Anthropic ships top-requested features in about a quarter but this specific feature has not appeared in the visible changelog window.

### 3. A6 — Braintrust Patterns: what it clusters, whether it emits a runnable artifact, price — braintrust.dev docs/pricing — `vendor-reported`

- **Braintrust's clustering feature is now named "Topics" (GA), not "Patterns"** — vendor-reported, `braintrust.dev/blog/topics-ga` / `braintrust.dev/docs/observe/topics`, via WebSearch 2026-09-18. This closes the project's own standing `unknown — not pulled` on this line (`success-vision.md` §3, §5, §6, §7 all cite Patterns as unpulled).
- **"Topics continuously clusters production traces by custom facets (use case, sentiment, etc.) to surface recurring patterns automatically"; "uses embedding-based clustering followed by an LLM-assisted naming pass that turns each cluster into a human-readable label"** — vendor-reported, Braintrust blog, 2026 (exact post date not shown in the search snippet).
- **Does it emit a runnable artifact?** Docs describe it as turning patterns into **"evaluation datasets, scorers, and review queues"** — vendor-reported, `braintrust.dev/docs/observe/topics`. That is an eval/observability artifact, not a runnable tool/skill/command comparable to Foreman's `SKILL.md`. No mention of generating an executable script or slash command.
- **Price**: free tier — 10,000 scores + 1 GB processed data/month, unlimited users/projects/datasets; **Pro plan $249/month**, model credits included for AI features including Topics — vendor-reported, `braintrust.dev/pricing`, via WebSearch 2026-09-18.

### 4. A5 — Claude Code user count: any Anthropic-stated figure (WAU, "N developers", run-rate) 2026 — anthropic.com/news, earnings press, Claude Code launch posts — `company-stated`; else `unknown — checked`

No single absolute headcount found. Growth-rate and revenue figures found, all company-stated, via WebSearch 2026-09-18:

- **"Claude Code's weekly active users had doubled since January 1, 2026, while business subscriptions had quadrupled since the start of 2026"** — company-stated, Anthropic announcement, February 2026 (relayed via secondary coverage, not the primary press release itself — primary URL not independently located this pull).
- **"80x annualized growth in Q1 2026, with API volume up nearly 70x year over year, and the average developer using Claude Code spending 20 hours a week with the tool"** — company-stated, Dario Amodei, Code with Claude conference, May 2026 (relayed).
- **"Claude Code's annualized revenue run rate surpassed $2.5 billion in early 2026"**; **"$1 billion in annualized revenue... six months after Claude Code's public launch in May 2025"** (i.e., November 2025) — company-stated, relayed via secondary coverage.
- `unknown — checked WebSearch "Anthropic Claude Code weekly active users OR N developers 2026 announcement" 2026-09-18` for an absolute WAU/MAU count or total-developer figure — none of the returned sources states one; all figures are growth multiples or dollar run-rates.

### 5. A5 — Count of public GitHub repos matching `claude code hook` / `claude-code plugin` / `SKILL.md` with >100 stars; top 10 with stars and last push — GitHub search API — `measured-by-us`

All three pulled directly from `api.github.com/search/repositories`, 2026-09-18. Caveat per F7/framework note: `total_count` counts a title/readme/description substring match, not a curated request — the defensible number is that all of it clears >100 stars easily, not a precise ranking.

**`"claude code hook" in:readme,description`** — total_count **19,593**. Top 10 (repo — stars — last push):
| Repo | Stars | Last push |
|---|---|---|
| affaan-m/ECC | 261,478 | 2026-09-17 |
| JuliusBrussee/caveman | 106,436 | 2026-09-18 |
| code-yeongyu/oh-my-openagent | 69,180 | 2026-09-18 |
| pbakaus/impeccable | 68,870 | 2026-09-18 |
| shanraisshan/claude-code-best-practice | 66,075 | 2026-09-18 |
| hesreallyhim/awesome-claude-code | 54,245 | 2026-09-18 |
| abhigyanpatwari/GitNexus | 47,419 | 2026-09-18 |
| sickn33/agentic-awesome-skills | 46,552 | 2026-09-18 |
| rohitg00/agentmemory | 28,574 | 2026-09-14 |
| OthmanAdi/planning-with-files | 26,974 | 2026-09-17 |

**`"claude-code plugin" in:readme,description`** — total_count **69,712**. Top 10 include mattpocock/skills (264,900★), affaan-m/ECC (261,479★), multica-ai/andrej-karpathy-skills (213,842★), anthropics/skills (176,965★), f/prompts.chat (170,631★), **anthropics/claude-code itself (146,020★, pushed 2026-09-18)**, DietrichGebert/ponytail (141,683★), punkpeye/awesome-mcp-servers (95,194★), ruvnet/RuView (94,357★), thedotmack/claude-mem (94,160★).

**`"SKILL.md" in:readme`** — total_count **364,399**. Top 10 include obra/superpowers (288,306★), affaan-m/ECC (261,475★), firecrawl/firecrawl (181,824★), anthropics/skills (176,964★), msitarzewski/agency-agents (153,248★), garrytan/gstack (133,522★), harry0703/MoneyPrinterTurbo (124,514★), Graphify-Labs/graphify (119,185★), nexu-io/open-design (96,868★), addyosmani/agent-skills (96,109★).

All three queries return counts and lists dominated by generic AI-coding-tool repos (skill packs, harnesses, awesome-lists), not recurrence/history tools specifically — none of the top-10 rows in any of the three lists is a Foreman-shaped competitor. That specific search is line 13 below.

### 6. A5 — Count of plugins in the official Claude Code marketplace(s) and the largest community marketplace — plugin directory pages — `vendor-reported` / `measured-by-us`

- **Official marketplace (`anthropics/claude-plugins-official`): 316 plugin entries**, counted directly from the live `marketplace.json` file — measured-by-us, `raw.githubusercontent.com/anthropics/claude-plugins-official/main/.claude-plugin/marketplace.json`, fetched 2026-09-18. First 10 alphabetically: `42crunch-api-security-testing`, `adobe-for-creativity`, `agent-sdk-dev`, `agentforce-adlc`, `ai-plugins`, `aikido`, `airtable`, `airwallex-agentos`, `airwallex-dev`, `aiven`.
- **Conflicting secondary figure**: "more than 200 plugins as of July 2026" and, separately, "101 plugins total (33 Anthropic-built, 68 partner) as of March 2026" — vendor-reported/press, via WebSearch, exact source pages not independently re-fetched this pull. Sitting side by side, never averaged: March 2026 ≈101 → July 2026 >200 → **measured today, 2026-09-18: 316**. Consistent growth trend, three different snapshot methods.
- **Largest community marketplace: no single authoritative number.** Press description: **"over 9,000 third-party entries by mid-2026"** spread **across** ClaudePluginHub, Claude-Plugins.dev and the official marketplace combined — vendor-adjacent press, via WebSearch 2026-09-18, not attributable to one named marketplace. Named community directories: `aitmpl.com` (davila7/claude-code-templates, "indexing thousands of agents, commands, skills, and MCP servers" — no exact count found), `buildwithclaude.com`, `claudepluginhub.com` (all self-described directories, none publishing a live total-count page this pull could fetch). `unknown — checked WebSearch "largest community Claude Code plugin marketplace number of plugins 2026" 2026-09-18; no single-marketplace count found`.

### 7. A9 — Star velocity baselines: `ccusage` stars on 2026-09-18 vs 14 days earlier; `Claude-Code-Usage-Monitor`; `claude-session-budget` (8★ on file) — star-history.com or GitHub API — `measured-by-us`; sets what "100 stars in 14 days" means

- **`ccusage/ccusage`: 18,615 stars, 2026-09-18** — measured-by-us, `api.github.com/repos/ryoppippi/ccusage`, fetched 2026-09-18 (created 2025-05-29, last push 2026-09-17). Note: repo migrated org (`ryoppippi/ccusage` → `ccusage/ccusage`); language field now reports Rust.
- **vs 18,366 stars, 2026-09-04** — analyst-derived (third-party star-tracking snapshot, exact site not independently re-fetchable; relayed via WebSearch), giving **+249 stars in 14 days** for the category leader.
- Already on file: `projects/agent-hermes-dashboard/docs/plan/re-pick.md` §3/§5 cites **18,591 stars, 2026-09-17** (vendor-reported at the time) — sits between the two points above and confirms a steady, un-viral growth rate (~18/day), not a launch spike.
- **`Maciek-roboblog/Claude-Code-Usage-Monitor`: 8,713 stars**, created 2025-06-19, last push 2026-07-05 (no commits in ~2.5 months) — measured-by-us, `api.github.com/repos/Maciek-roboblog/Claude-Code-Usage-Monitor`, fetched 2026-09-18. A third-party star-history page shows a slightly stale **8.7k (8,706)**, consistent within rounding.
- **`Star001-KR/claude-session-budget`: still 8 stars**, created 2025-05-09, last push 2026-05-15 — measured-by-us, `api.github.com/repos/Star001-KR/claude-session-budget`, fetched 2026-09-18. **Unchanged from the 8★ already on file** (`re-pick.md` §3/§5) — four-plus months with zero star growth on the exact abandoned reference implementation the pre-registered gate (`success-vision.md` §5) uses as its floor.
- **What "100 in 14 days" means, restated with fresher numbers:** the category leader gained 249 in 14 days from a base of 18,000+; the one prior attempt at this exact function gained 0 in over four months from a base of 8. 100 stars in 14 days for a brand-new, zero-history repo is a materially harder bar than the leader's organic growth rate suggests, because the leader's growth compounds on an existing installed base — a cold-start repo has no such base.

### 8. A4 — Prices of closest paid dev-workflow analytics: WakaTime, LinearB, Swarmia, DX, Waydev; Claude-specific paid tools (SessionWatcher $6.99–59 on file, CrewTower) — vendor pages — `vendor-reported`

All fetched/searched live 2026-09-18, superseding/confirming the "on file" figures named in the C2 line itself:

| Vendor | Tier | Price | Source |
|---|---|---|---|
| WakaTime | Premium | $8.25/mo | SaaSworthy pricing aggregator, via WebSearch |
| WakaTime | Team | $11.00/user/mo | same |
| WakaTime | Business | $44.92/user/mo | same |
| LinearB | Essentials | $29/user/mo, billed annually | `linearb.io/pricing`, WebFetch |
| LinearB | Enterprise | $59/user/mo, billed annually | same |
| Swarmia | Standard | $45/developer/mo, billed annually | `swarmia.com/pricing`, WebFetch |
| Swarmia | Enterprise | $55/developer/mo, billed annually | same |
| Swarmia | free tier | $0 for <10 developers | same |
| Swarmia | à la carte "AI adoption & cost" | $5/developer/mo | same |
| DX (getdx.com) | — | **no public price** — page has no pricing content, "contact for demo" | `getdx.com/pricing`, WebFetch |
| Waydev | Pro | $449–$649/active contributor/year (range from two aggregator pages, not averaged) | WebSearch, waydev.co/pricing referenced but not independently WebFetched |
| Waydev | Enterprise | custom | same |
| SessionWatcher | Solo | $6.99 (one tool tracked) | `sessionwatcher.com`, WebSearch — **confirms the $6.99 floor already on file** |
| SessionWatcher | Bundle | $14.99 (Claude+Codex+Cursor) | same |
| SessionWatcher | Pro | $59 one-time or $24/year | same — **note: "$59" not "$59 max" as the on-file range implied; it is one specific one-time price, alongside a separate $24/yr option, not a ceiling** |
| CrewTower | Early-bird, 1 Mac | $9.99 one-time, lifetime | `producthunt.com`/`crewtower.app`, WebSearch |
| CrewTower | Regular, 1 Mac | $14.99 one-time | same |

Waydev's own pricing page (`waydev.co/pricing`) was found by search but not independently WebFetched this pull; the $449/$649 figures are aggregator-relayed, side by side because they may reflect two different billing cycles or tiers, not verified as the same SKU.

### 9. A4 — Any paid Claude Code third-party tool with disclosed revenue or customer count — Gumroad/Lemon Squeezy listings, IndieHackers posts 2026 — `company-stated`; expect `unknown`

`unknown — checked WebSearch "Claude Code third-party tool disclosed revenue MRR Gumroad Lemon Squeezy 2026" and "SessionWatcher OR CrewTower founder disclosed revenue customers indiehackers", 2026-09-18`. Found: several Claude-integrated **revenue-tracking MCP servers** (e.g. `warfare-hub/revenue-mcp`, an "Indie Founder Revenue MCP" aggregating Stripe/Gumroad/Lemon Squeezy/Polar) — these are tools that let you query *your own* revenue from inside Claude, not Claude-Code-analytics tools with their *own* disclosed revenue. No disclosed revenue or customer count found for SessionWatcher, CrewTower, or any other Claude-Code-specific paid analytics/tracking tool named in this project. Expected `unknown` per the C2 line itself, confirmed.

### 10. A10 — Anthropic consumer terms clause on automated/non-human access, current text and date; Agent SDK subscription-usage status (support.claude.com article 15036540 successor) — `filed` / `company-stated`; platform risk

- **Consumer Terms clause, verbatim**: **"Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through automated or non-human means, whether through a bot, script, or otherwise"** [is prohibited] — filed, `anthropic.com/legal/consumer-terms`, WebFetch 2026-09-18, page's own **"Last updated: October 8, 2025"**. Section numbering not independently confirmed in the fetched excerpt (a secondary source calls it "Section 3.7"; not verified against the primary document's own section numbers this pull).
- **Claude Code CLI's own automated use is the explicitly-permitted exception** — company-stated, relayed via WebSearch (`theregister.com` Feb 2026 coverage, `daimonlegal.com`): Claude Code CLI is Anthropic's official product built for scripted/automated use and is treated as within the "explicitly permit it" carve-out; third-party automation tools and the Agent SDK under OAuth are not.
- **Agent SDK / OAuth**: "As of February 2026, the Agent SDK now explicitly requires API key authentication — OAuth tokens from Free/Pro/Max accounts cannot be used with the Agent SDK" — company-stated, relayed via WebSearch, primary Anthropic post not independently re-fetched this pull.
- **Support article 15036540, current status, verbatim update banner**: **"We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits."** — company-stated, `support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan`, WebFetch 2026-09-18. The article's original body (no longer in effect) had described a June 15, 2026 change letting Agent SDK and `claude -p` usage draw from separate monthly credits instead of the subscription window; **that change was paused before it took effect and is still paused as of 2026-09-18.**
- **This corrects an assumption on file**: `docs/plan/re-pick.md` (2026-09-17) treats "the 2026-06-15 billing withdrawal" and "Anthropic removes `claude -p` from subscription limits" as a **live, already-happened** event (§4 case-against, §5 revival table: "the 2026-06-15 withdrawal says this is live"). The support article's own banner says the opposite — the change was **paused**, not shipped, and subscription-drawn `claude -p`/Agent SDK usage is unchanged from before June 15. This is a direct correction, not a nuance: any downstream reasoning in `re-pick.md` that depends on `claude -p` having been freed from subscription limits is currently false.

### 11. A1 — Count of first-person posts 2026 "I run my business with Claude Code" (non-code use) — r/ClaudeAI, IndieHackers, HN — `measured-by-us`; the buyer existence check

No systematic count obtainable within this pull's tooling (WebSearch returns a handful of matching snippets, not an exhaustive corpus with a denominator — the same "no denominator" trap `re-pick.md` §1 already flags for the 828-issue count). Individual first-person examples found, via WebSearch 2026-09-18, queries `"I run my business with Claude Code" reddit OR indiehackers 2026`:

- Indie Hackers post: a founder describing building a "13-step SEO pipeline directly from their IDE" via an MCP server after noticing they context-switched between Claude Code and a dashboard to write blog posts.
- Indie Hackers post: "I let Claude Code run my entire SEO pipeline. Here's how."
- Indie Hackers post: a founder using Claude Code for "live analysis of subreddits and social media data" for marketing.
- A blog aphorism, not a first-person account: "2026 founder mode... just a Claude Code subscription and a Mac Mini... AI as the first employee" (Substack, not a verified individual's own post).

These are **non-code business tasks run through Claude Code** (marketing pipelines, analytics), matching the delighted-user persona in `success-vision.md` §3 — but this is 3-4 anecdotes found by a handful of search queries, not a count with a denominator. `unknown — no denominator; checked WebSearch, exact query above, 2026-09-18` for how common this is relative to all Claude Code users.

### 12. A1 — r/ClaudeAI member count; Claude Developers Discord member count — `measured-by-us`

- **r/ClaudeAI**, conflicting snapshots, side by side, never averaged: **≈1.1M members as of 2026-09-13** (GummySearch); **1,093,707 as of 2026-08-23** (Prowlo); **1,043,382 "as of late August 2026"** (RedditList) — all analyst-derived third-party subreddit trackers, via WebSearch 2026-09-18, none of them Reddit's own official count (this pull could not query Reddit's API directly). Trend is consistent (growing through August into September), the exact figure is not.
- **Claude Discord** (the general `discord.gg/anthropic` community server — no separately-named "Claude Developers" server was found distinct from this one): two conflicting live-widget-style snapshots relayed via WebSearch, **123,662** and **127,191** members, neither independently timestamped by this pull; both via WebSearch 2026-09-18, no direct widget API access succeeded (`discord.com/api/guilds/.../widget.json` returned HTTP 400 — the invite code is not the numeric guild ID needed for that endpoint). `unknown — exact current count; checked discord.com/api/guilds/<code>/widget.json (400, wrong id format) and WebSearch, 2026-09-18` for a single authoritative figure. No evidence found of a Discord server specifically branded "Claude Developers" as distinct from the general Claude community server named in the C2 line.

### 13. A6 — Existing "prompt history analyzer" / "history.jsonl" tools on GitHub — search — `measured-by-us`

`"history.jsonl" claude in:readme` — total_count **4,548** — measured-by-us, `api.github.com/search/repositories`, fetched 2026-09-18. Top 10 by stars:

| Repo | Stars | Description | Last push |
|---|---|---|---|
| wonderwhy-er/DesktopCommanderMCP | 9,635 | MCP server: terminal control, filesystem search/diff | 2026-09-17 |
| kenn-io/agentsview | 5,942 | "Local-first session search, analytics, insights, and token use statistics for coding agents" | 2026-09-18 |
| parcadei/Continuous-Claude-v3 | 3,943 | Context management via hooks, ledgers, handoffs | 2026-01-26 |
| Dicklesworthstone/coding_agent_session_search | 1,136 | "Unified TUI and CLI to index and search local coding agent session history across 11+ providers" | 2026-09-18 |
| doccker/cc-use-exp | 1,054 | Config templates | 2026-08-26 |
| Pantheon-Security/medusa | 988 | Security scanner, Claude Code compromise detection | 2026-08-10 |
| iAmCorey/kooky | 651 | Terminal for AI coding, sidebar workspaces | 2026-09-05 |
| scanaislop/aislop | 632 | Catches AI-agent code-quality issues | 2026-09-18 |
| Arindam200/cc-lens | 600 | "Local analytics dashboard for Claude Code without cloud or telemetry" | 2026-06-27 |
| uppinote20/claude-dashboard | 568 | Status-line plugin: context/rate-limit/cost tracking | 2026-09-12 |

**Two direct competitors surfaced, closer to Foreman's shape than anything found for C1/C3-equivalent searches**: `kenn-io/agentsview` (5,942★, "session search, analytics, insights... for coding agents") and `Dicklesworthstone/coding_agent_session_search` (1,136★, cross-provider session-history search/index). Neither description mentions recurrence-to-skill graduation specifically — both read as search/analytics over history, not "detect a repeated task and emit a runnable artifact." Not independently inspected beyond the description text this pull (would need a repo-level read to confirm feature parity or absence).

### 14. A10 — One live `Stop` hook fire observed end-to-end on a scratch project with the ledger line pasted — agent can run in `prototype/demo/` — `measured-by-us`

**requires-main-thread** — not pulled. Firing a real `Stop` hook end-to-end requires an actual interactive (or `-p`) Claude Code session terminating inside `prototype/demo/`; this research-pull agent's own turn is not that session and starting a nested Claude Code invocation from within this pull to manufacture the event is the same circularity `e2e-test.md`'s own caveats already declined ("would require running a live Claude Code session from inside this test session, which is circular and was judged out of scope"). Left for the user or a main-thread session to run directly.

### 15. A10 — `scan --from-history` built and run on this machine's real `history.jsonl`, report pasted with `display` values redacted to normalised shapes — `measured-by-us`; the first real ledger

**Not built as of 2026-09-18** — this is a design recommendation (`success-vision.md` §7 item 1), not shipped code. Confirmed by inspecting `projects/agent-hermes-dashboard/prototype/foreman/__main__.py`'s own subcommand list, cited already in `success-vision.md` §7 item 1: **"Check the CLI first: no such mode exists today (`foreman/__main__.py` subcommands: demo, scan, report, hook, install, build-fixture)."** Building this feature is out of scope for a stage-2 research pull (§C2's own framing is "pull," not "build"; `projects/CLAUDE.md`'s pipeline puts new code under the MVP/build step, not the investment-review pull). `unknown — not run; feature does not exist in the current prototype, per success-vision.md §7 item 1, verified 2026-09-18 against the file list actually present`.

### 16. **A3 KILL** — Gate at day 14 after publication: stars AND unprompted paid asks (≥100 AND ≥3, both required) — `requires-human` to publish; `measured-by-us` to count

**requires-human — not pulled.** The project has not been published (no public repo, no release post as of 2026-09-18 per this pull's own web search turning up no `Foreman`/`agent-hermes-dashboard` GitHub repo, and per the project's own docs treating publication as a still-pending human decision, `success-vision.md` §7 item 7: "Publish and run the gate... Human decision"). The 14-day clock has not started.

### 17. A9 — LOC of `prototype/foreman/` and copy-time estimate — `measured-by-us` + `own judgement`

- **`foreman/` package: 1,618 lines across 12 `.py` files** — measured-by-us, `wc -l` on `projects/agent-hermes-dashboard/prototype/foreman/*.py`, run 2026-09-18: `cluster.py` 129, `config.py` 62, `fixtures.py` 205, `graduate.py` 140, `hookcmd.py` 187, `install.py` 122, `ledger.py` 121, `normalize.py` 129, `report.py` 180, `voice.py` 135, `__init__.py` 10, `__main__.py` 198.
- **Plus `foreman_hook.py`: 25 lines** and **`test_foreman.py`: 244 lines** (test code, not shipped logic) — measured-by-us, same method. **Total `.py` under `prototype/`: 1,887 lines** (`foreman/` + `foreman_hook.py` + `test_foreman.py`).
- **Copy-time estimate — own judgement**: the shipped logic (excluding tests) is 1,643 lines of dependency-free Python 3.9 (`grep` for `requests`/`numpy`/`pandas`/`pydantic`/`rich`/`click` returns 0 hits per `e2e-test.md` item 1), covering: JSONL parsing, a Jaccard-based normalizer/clusterer with a hand-tuned stopword/placeholder scheme, a graduation-threshold rule, a hook payload handler with an `assert_not_global` safety guard repeated at 9 call sites, and template-based report/voice generation with two mechanical no-numbers/no-claims tests. An incumbent engineer who already knows the target behavior (because the report and this file describe it) could plausibly reproduce the clustering + graduation + report core in **2-4 days**; reproducing the safety-guard discipline and the exact tone-template mechanical tests (`test_voice_templates_carry_no_numbers`, `_carry_no_claims`) adds **0.5-1 day** if they choose to bother, which a fast-follow competitor optimizing only for a demo would likely skip. No externally-verifiable "vendor absorption time" data point exists for this exact shape (unlike C2 line 2's changelog-negative, which is a different question); this is an estimate from the code's own measured size, not a measured incumbent build.

### 18. A11 — Anthropic API list prices for the models a hosted variant would call — platform pricing page — `vendor-reported`; only if a hosted variant is ever scoped

Pulled live, `platform.claude.com/docs/en/about-claude/pricing`, WebFetch 2026-09-18 (current page, reflects a pricing change dated for **2026-09-01** — see note below):

| Model | Base input | Output | 1h cache write | Cache read |
|---|---|---|---|---|
| Claude Opus 5 | $5/MTok | $25/MTok | $10/MTok | $0.50/MTok |
| Claude Sonnet 5 | $2/MTok | $10/MTok | $4/MTok | $0.20/MTok |
| Claude Sonnet 4.6 | $3/MTok | $15/MTok | $6/MTok | $0.30/MTok |
| Claude Haiku 4.5 | $1/MTok | $5/MTok | $2/MTok | $0.10/MTok |

**Note, load-bearing for any COGS calc using Sonnet**: the live page states, verbatim: **"The $2/$10 per million input/output token pricing for Claude Sonnet 5, announced at launch as introductory pricing through August 31, 2026, is now the standard price. The previously scheduled increase to $3/$15 per million input/output tokens on September 1, 2026 will not occur."** Any prior project file assuming Sonnet 5 reverts to $3/$15 after 2026-09-01 is now stale as of this pull; $2/$10 is the standing price. Web search: $10/1,000 searches; web fetch: no additional charge beyond token cost.

---

## Conflicting figures, side by side (never averaged) — summary of what appears above

| Topic | Value A | Value B | Where |
|---|---|---|---|
| `Stop`/`SubagentStop` payload cost/duration fields | 2026-09-17 raw pull (`claude-code-docs-2026-09-17.md`) claimed: **carries `cost` and `duration_ms`** | Live re-fetch 2026-09-18 (`hooks.md`) + measured-by-us live runs (`hook-payload-measurement-2026-09-17.md`): **neither field present** | Item 2 context; resolved in favor of B — B is a live measurement, A was WebFetch's own flagged-as-risky summarization pass over the same page |
| `claude -p`/Agent SDK subscription-limit status | `docs/plan/re-pick.md` (2026-09-17): treats the 2026-06-15 change as **live** | Support article 15036540, live 2026-09-18: change **paused**, never took effect | Item 10 — B is current and corrects A |
| ccusage stars | 18,366 (2026-09-04, analyst-derived) | 18,591 (2026-09-17, on file) | 18,615 (2026-09-18, measured-by-us) | Item 7 — a trend, not a conflict; all three plausible on a steady growth line |
| Official plugin marketplace count | ~101 (March 2026) | >200 (July 2026) | 316 (2026-09-18, measured-by-us) | Item 6 — trend, not a conflict |
| r/ClaudeAI members | 1,043,382 (late Aug) | 1,093,707 (Aug 23) | ~1.1M (Sep 13) | Item 12 — trend |
| Claude Discord members | 123,662 | 127,191 | Item 12 — genuinely conflicting, no date resolution possible this pull |
| Waydev Pro price | $449/contributor/yr | $649/contributor/yr | Item 8 — possibly two different billing terms, not resolved |

## Not found

- An absolute Claude Code WAU/MAU/total-developer headcount (only growth multiples and revenue run-rates are company-stated).
- A single authoritative "largest community marketplace" plugin count.
- Any disclosed revenue or customer count for a paid Claude Code third-party analytics/tracking tool.
- A verified "Claude Developers"-branded Discord distinct from the general Claude community Discord.
- A systematic (denominator-bearing) count of first-person "I run my business with Claude Code" posts.
- Waydev's own pricing page content, independently WebFetched (relied on aggregator relay only).

## Already on file (cited, not re-pulled in full)

- `projects/agent-hermes-dashboard/raw/hook-payload-measurement-2026-09-17.md` — live measured Stop/SubagentStop payloads, no `cost`/`duration_ms` field, 3 runs, v2.1.259, 2026-09-17 → used to resolve the item-2/item-10 conflict above.
- `projects/agent-hermes-dashboard/raw/claude-code-docs-2026-09-17.md` — `/insights`, `costs.md`, `hooks.md`, `scheduled-tasks.md`, `monitoring-usage.md` pulls one day prior → used as the baseline that today's live re-fetches confirmed or corrected.
- `projects/agent-hermes-dashboard/docs/plan/re-pick.md` §3, §5 — ccusage 18,591★ (2026-09-17), claude-session-budget 8★, 828-issue demand-signal interrogation, the "2026-06-15 withdrawal" claim now corrected by item 10 above.
- `projects/agent-hermes-dashboard/docs/outcome/success-vision.md` §7 item 1 — confirms `scan --from-history` does not exist in `foreman/__main__.py`'s subcommand list (used for item 15).
- `projects/agent-hermes-dashboard/prototype/foreman/*.py`, `foreman_hook.py`, `test_foreman.py` — LOC counted directly (item 17).

## Counts

- **Pulled (live source obtained, dated, labeled)**: 13 of 18 lines (1 partial-docs-only, 2, 3, 4 partial, 5, 6, 7, 8, 9 negative-result, 11 partial, 12, 13, 17, 18).
- **`unknown`** (checked, not found): items nested inside 4, 6, 9, 11, 12 (5 distinct sub-claims marked `unknown` with the exact query/endpoint attempted).
- **`requires-human`**: 1 (item 16).
- **`requires-main-thread`**: 2 (items 1, 14).
- **Not built / not applicable to a pull**: 1 (item 15).
