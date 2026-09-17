# Control planes — what ships today, 2026-09-17

Baseline: `../../../docs/competitors/agent-dashboard-roster.md` and `../../../docs/markets/agent-dashboard.md` (pass-1, 2026-09-16) — read those first, this file only adds and updates. Evidence for new material: `../../raw/control-planes-pulls.md`. Per the brief: what each shows, what it records per task, cost/time telemetry, recurring-task detection, pricing, who it's sold to.

## Per-product table (baseline + delta)

| Product | Shows | Records per task | Cost/time telemetry | Recurring-task detection | Pricing | Sold to |
|---|---|---|---|---|---|---|
| **LangSmith** | Traces, evals, playground, HITL annotation | Full trace tree | Yes, native | Not found as a named feature | $39/user/mo Plus, 5k free traces, $2.50/1k over (pass-1) | Dev teams |
| **NEW: LangSmith LLM Gateway** (2026-07-30) | Spend caps at Org/Workspace/API-key/User level | Spend event, HTTP 402 on cap hit | **Yes — this IS a fleet-level cost-rollup feature**, vendor-reported | No | Not disclosed this pull | Dev/platform teams running multiple agents under one org |
| **Langfuse** | Tracing, evals, prompt mgmt | Full trace tree | Yes, native | Not found | Core $29-59/mo, Pro $199, Enterprise $2,499 (pass-1, unconfirmed unchanged — changelog URLs 404'd this pull) | Dev teams. Acquired by ClickHouse 2026-01-16, unchanged per this pull |
| **AgentOps** | Session replay for CrewAI/AutoGen/LangGraph | Session-level | Yes | Not found | Free 5k events, Pro $40/mo (pass-1, no vendor-primary update found this pull) | Agent framework devs |
| **Braintrust** | Eval-driven dev, regression scoring | Trace + eval score | Yes | **NEW, close match: "Topics" (GA 2026-06-01)** — continuously clusters production traces via embedding + LLM naming into Task/Issues/Sentiment dimensions. Vendor quote: "clusters update continuously as new traces arrive, so a topic distribution is always current." **NEW: "Patterns" (public preview, 2026-09-03)** — automatic recurring-behavior identification with recommendations. **NEW: "Loop" (same date)** — scheduled automations with approval workflows | $249/mo+ (pass-1); Patterns/Loop pricing "to follow before GA" per vendor post | Eval-focused dev teams |
| **Helicone** | Drop-in proxy, logging | Request log | Yes | Not found | ~$20/mo (pass-1, unconfirmed — no dated post found in the post-acquisition window this pull) | Dev teams. Acquired by Mintlify 2026-03-03, feature dev frozen per pass-1 |
| **W&B Weave** | Traces, scorers, guardrails | Trace, now with **sessions/turns/steps/sub-agents as first-class objects (NEW, 2026 vendor site)** | Yes | Not found by name; "continuous improvement for production agents" tagline suggests adjacent capability, unconfirmed | Free tier, per-seat (pass-1, no pricing update found) | Dev/ML teams. **NEW: "Weave Guardrails"** (safety/quality scorers), **"Leaderboards"**, autonomous Claude-Code-driven iteration loops |
| **OpenTelemetry GenAI semantic conventions** | N/A — a spec, not a product | N/A | N/A | N/A | Free/open standard | Anyone building observability tooling |
| **Nous Research "Hermes Agent"** | Single-instance dashboard: session browser, cron manager, API-key governance, log viewer, approval config | Per-session | Not found as fleet-level cost tracking (pass-1 finding, unchanged) | Not found | Free (OSS core), Business/Enterprise tiers undisclosed pricing | Self-hosters running one agent instance. See `hermes-substrate.md` |

## OpenTelemetry GenAI semantic conventions — material change since pass-1's 2026-07-17 snapshot

Pass-1 recorded: "as of 2026-07-17 no GenAI span, event, metric, or attribute is marked Stable... v1.42.0, Jun 2026, includes MCP conventions."

**Update, 2026-09-17**: at v1.42.0 (2026-06-12), all `gen_ai.*`, `model/openai/*`, and `model/mcp/*` conventions were **deprecated in the main `semantic-conventions` repo and moved to a new, separate repo** `open-telemetry/semantic-conventions-genai`. The main repo has since released v1.43.0 (2026-07-03) and v1.44.0 (2026-08-04) without them. The new GenAI-specific repo:
- Has **no tagged releases** (`api.github.com/repos/open-telemetry/semantic-conventions-genai/tags` returns empty) — ships from `main` only.
- Every span/attribute/metric/event still carries `Status: [Development]`, confirmed by direct fetch of the raw spec file.
- Its own README schema-URL field is literally "TODO" (third-party-reported, dev.to/azena-ai, 2026-07-16).

**Read**: this is not progress toward stability — it is GenAI conventions leaving the versioned, tagged-release main spec for an unreleased side repo. A fleet dashboard spanning multiple model vendors still has no stable, versioned wire format to build against, 14+ months after GenAI semconv work began appearing in the main repo.

## The SMB gap — searched hard, not found, treat as a real gap with a caveat

Explicit search across HN Algolia (Show HN, 2026 full year, multiple query terms), Product Hunt, and general web search for a product marketed to non-technical 3-10-person business owners for supervising/monitoring agent fleets (as opposed to developer-first observability). **None found.** Everything discoverable is either developer-facing or a generic "AI employee" doer, not a supervisor/monitor:

- **CrewTower** — macOS menu-bar app controlling Claude Code/Codex/Cursor sessions, $9.99 one-time. Developer-targeted.
- **Flowcost** (flowcost.ai) — pre-implementation cost *modeling* for ML engineers, explicitly does not track live production spend.
- **OneManCompany / Agent Universe** — agent marketplace requiring MCP host setup, technical-founder audience.
- Other 2026 Show HN fleet/supervisor launches (OpenLegion, AgentsMesh, Nexroo Supervisor IDE, Batty/tmux, Springdrift) — all CLI/container/IDE-native developer infrastructure.

**Caveat, explicit**: WebSearch was quota-constrained during this check (per the parent brief's known constraint), so this is "hard search, incomplete," not exhaustive. Treat the absence as suggestive of a real gap, matching pass-1's own conclusion ("A framework-agnostic manager dashboard for a non-technical buyer: not found as a mature product"), not as proof nothing exists.

## Consolidation and crowding — unchanged from pass-1, reaffirmed

No new acquisitions or shutdowns found for LangSmith, Langfuse, Braintrust, Helicone, AgentOps, or W&B Weave since pass-1's Jan-Mar 2026 events (ClickHouse/Langfuse, Mintlify/Helicone). The crowded part of the lane is exactly what pass-1 named: **developer-first tracing and eval is mature and consolidating fast** (LangSmith, Langfuse, Braintrust, Helicone, AgentOps, W&B Weave all compete on the same ground, and two of six were already bought within the last research pass's timeframe). The two closest-to-novel features found this pull — Braintrust's "Topics" (recurring-pattern clustering) and LangSmith's Gateway (fleet-level spend caps) — are being built by the *already-funded incumbents*, into their *developer-first* products, not by anyone targeting the non-technical buyer.

## Read for the design phase

Two things pass-1 named as "unsolved" are now partially being solved — but by incumbents, and only for developers:
1. **Cost rollup for non-technical buyers** — pass-1 said this "exists only behind contact-sales enterprise pricing." LangSmith's Gateway (Org/Workspace/API-key/User caps, HTTP 402 on breach) is a real fleet-cost-rollup shipped 2026-07-30 — but it is a developer product, priced and shaped for engineering orgs, not solopreneurs.
2. **Recurring-task / pattern detection** — Braintrust's "Topics" (GA June 2026) and "Patterns" (preview Sept 2026) are the closest thing on the market today to what the brief's sub-question 5 asks the design phase to build — continuous clustering of production traces into recurring task types, with recommendations. **This directly narrows the design space**: if Braintrust already does trace-clustering-for-recurrence at the eval-tooling layer, the design phase's differentiation has to be doing it for the non-technical buyer's *task record*, not re-inventing the clustering itself. Worth reading Braintrust's Topics/Patterns docs directly before designing sub-question 5's graduation path.

Both incumbent moves reinforce pass-1's core read: the developer-tooling layer keeps absorbing every feature the moment it's proven valuable. The SMB-facing UX gap is the one part of the lane that a two-person team's build weeks would not be racing an already-funded competitor into — assuming the SMB search above (quota-constrained) isn't missing something a search-quota reset would find.

## Caveats

- This entire file's new material was produced by a delegated sub-agent, not the parent explore agent's own direct fetches — see `../../raw/control-planes-pulls.md`'s evidence-chain note. Every number here traces to that raw file and, through it, to the primary URLs it lists.
- WebSearch was quota-constrained for the delegated agent's own run (separate quota from the parent thread, which used none). The SMB-gap negative finding and the Langfuse/Helicone/AgentOps "no update found" lines are search-limited, not confirmed absences.
- Langfuse changelog pages returned 404 this pull — pricing/feature currency for Langfuse specifically is **weaker evidence now than pass-1's own snapshot**, not stronger. Flag for re-check when the vendor's changelog URL structure is known.
- Braintrust and LangSmith updates are 100% vendor-reported (vendor blog posts), not independently verified by a third party or by hands-on testing.
