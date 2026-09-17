### Source: delegated general-purpose research agent — control-plane landscape update, 2026-09
- Pull date: 2026-09-17 (agent ran ~555s, 55 tool uses — this agent's own WebSearch/WebFetch quota)
- Method: sub-agent dispatched to check what's new/changed since pass-1 (2026-09-16) for the existing competitor roster, plus fill two specific gaps: OTel GenAI semconv status, and SMB-specific (non-developer) agent-supervision products. This file is the agent's full returned report, relayed verbatim — one level removed from the primary sources it cites (its own tool transcript is not preserved here, only its synthesized report + source list). Primary URLs listed at the bottom for direct re-fetch.

## Agent's full report, verbatim

**Search-quality caveat:** WebSearch returned intermittent "unavailable" errors throughout this session (quota-constrained, as flagged by the parent task). Relied on direct WebFetch of primary sources (GitHub API, vendor blogs, HN Algolia) wherever search failed. Coverage on item 2 (SMB gap) should be read as "hard search, incomplete" not "exhaustive."

### 1. OpenTelemetry GenAI semantic conventions — material change since 2026-07-17

GenAI + MCP conventions were extracted into a separate repo. Confirmed via GitHub API (api.github.com/repos/open-telemetry/semantic-conventions/releases, checked 2026-09-17): main repo releases are v1.44.0 (2026-08-04), v1.43.0 (2026-07-03), v1.42.0 (2026-06-12), v1.41.1 (2026-05-11), v1.41.0 (2026-04-28) — vendor-reported (project-self-reported).

At v1.42.0, all gen_ai.*, model/openai/*, and model/mcp/* conventions were deprecated in the main repo and moved to the new dedicated repo open-telemetry/semantic-conventions-genai. Old docs at opentelemetry.io/docs/specs/semconv/gen-ai/ are now redirect stubs pointing there. Source: GitHub redirect page + corroborating third-party writeup, dev.to/azena-ai (dated 2026-07-16), quote: "all GenAI conventions — model/gen-ai/, the OpenAI-specific ones under model/openai/, and the MCP conventions under model/mcp/ — were deprecated in the main repo and moved to a dedicated repository."

Stability unchanged — still nothing Stable. Direct fetch of the raw spec file raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md (checked 2026-09-17) shows: Status: [Development][DocumentStatus] — vendor-reported. Third-party confirms this is universal: "every single gen_ai.* attribute, span, metric, and event in the official OpenTelemetry registry carries the stability badge 'Development'" (dev.to/azena-ai, 2026-07-16).

The new repo has no tagged releases. api.github.com/repos/open-telemetry/semantic-conventions-genai/tags returned empty; the repo ships from main against schema gen-ai/1.42.0, and its README schema-URL field is literally "TODO" per the dev.to source. Prior note ("v1.42.0, Jun 2026, includes MCP conventions") is correct as a snapshot but should be updated: v1.42.0 is the version where GenAI+MCP conventions left the versioned main repo for an unreleased, still-Development side repo — arguably a regression in formality, not progress toward Stable.

### 2. Small-business-focused agent supervision — no clear hit, this is a real gap

Searched HN Algolia (Show HN, full 2026 date range, multiple query terms: "AI agent fleet dashboard," "AI employee dashboard," "supervise AI agents," "AI workforce," "agent spend small business"), Product Hunt search, and general web search. Found no product marketed specifically to non-technical small-business owners (3-10 person cos.) for supervising/monitoring agent fleets, distinct from the existing dev-tool list. Everything findable is either developer-facing or a generic "AI employee" doer (not a supervisor/monitor):

- CrewTower (macOS menu-bar app, checked 2026-09-17) — controls Claude Code/Codex/Cursor sessions from the notch, $9.99 one-time. Explicitly developer-targeted.
- Flowcost (flowcost.ai, HN 2026-04-08) — pre-implementation cost modeling, not live fleet tracking; targets ML engineers ("directed graphs," "prompt cache" language); explicitly states "does not connect to production, ingest logs, or track live spend."
- OneManCompany / Agent Universe (HN 2026-04-07) — agent marketplace requiring MCP host setup (Claude Code/Cursor/Continue); technical-founder audience.
- Other 2026 Show HN fleet/supervisor tools (OpenLegion "container isolation," AgentsMesh "command center," Nexroo Supervisor IDE, Batty/tmux, Springdrift) are all CLI/container/IDE-native — developer infrastructure, not SMB dashboards.

Could not find anything resembling a "per-task cost dashboard for non-technical operators" or a solopreneur-marketed launch in 2026. Given search-tool quota limits, treat absence as suggestive, not conclusive — worth a follow-up pass when search quota resets, or a targeted Product Hunt category browse.

### 3. Pricing/feature/acquisition checks

No new acquisitions or shutdowns found for LangSmith, Langfuse, Braintrust, Helicone, AgentOps, or W&B Weave beyond the ones already on file.

**Braintrust — closest match to the "rare features" list**, all vendor-reported from braintrust.dev/blog, checked 2026-09-17:
- "Topics," GA 2026-06-01 — near-exact match for recurring task detection: continuously clusters production traces via embedding-based clustering + LLM naming into built-in dimensions (Task/Issues/Sentiment); quote: "clusters update continuously as new traces arrive, so a topic distribution is always current."
- "Behavior specs," 2026-07-29 — open standard for evaluating agent behavior across a full trajectory (process supervision, not outcome-only) — adjacent to but not the same as "task memory."
- "Patterns, Debugger, Loop," 2026-09-03, public preview — Patterns = automatic recurring-behavior identification with recommendations; Loop = scheduled automations with approval workflows. Pricing "to follow before GA," per the post.

**LangSmith** (blog.langchain.com, checked 2026-09-17): "LangSmith LLM Gateway," 2026-07-30 is a close match for fleet-level cost rollup: tracks/caps spend at Organization, Workspace, API-key, and User levels, returns HTTP 402 when a cap is hit. Also shipped: Tuned Evaluators (2026-08-18), "LangSmith Engine >2x better issue detection" (2026-08-25), Preview Builds (2026-08-20) — general eval improvements, not specifically recurring-task detection.

**W&B Weave** (wandb.ai/site/weave, checked 2026-09-17): current tagline "Observability and continuous improvement for production agents." New 2026 features per vendor site: agent-native tracing (sessions/turns/steps/sub-agents as first-class), autonomous Claude-Code-driven iteration loops, Weave Guardrails (safety/quality scorers), Leaderboards. No pricing or acquisition info found.

**Langfuse**: changelog URLs tried (langfuse.com/changelog, /docs/changelog, /change-log) all 404'd — could not verify directly. Third-party aggregator pages (undated precisely, ~Aug 2026) describe pricing as "unchanged" since the ClickHouse acquisition but this is unverified secondhand.

**Helicone**: blog listing (helicone.ai/blog, checked 2026-09-17) showed no dated posts clearly from the March-September 2026 post-acquisition window — could not confirm any new feature/pricing activity either way.

**AgentOps**: no vendor-primary update found this session; only generic third-party aggregator description (open-source self-host, free tier), undated precisely.

### Sources (as given by the agent)

- https://api.github.com/repos/open-telemetry/semantic-conventions/releases
- https://api.github.com/repos/open-telemetry/semantic-conventions-genai/tags
- https://github.com/open-telemetry/semantic-conventions-genai
- https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-spans.md
- https://opentelemetry.io/docs/specs/semconv/gen-ai/
- https://dev.to/azena-ai/opentelemetrys-genai-semantic-conventions-are-not-stable-yet-heres-what-actually-shipped-in-2026-3mke
- https://hn.algolia.com/api/v1/search_by_date (multiple queries, 2026 range)
- https://www.producthunt.com/search (multiple queries)
- https://crewtower.app
- https://www.flowcost.ai/
- https://one-man-company.com/
- https://www.braintrust.dev/blog/topics-ga
- https://www.braintrust.dev/blog/behavior-specs
- https://www.braintrust.dev/blog/active-observability-loop-patterns-debugger
- https://www.langchain.com/blog/langsmith-llm-gateway-runtime-controls-for-production-agents
- https://www.langchain.com/blog/ (post listing)
- https://wandb.ai/site/weave/
- https://www.helicone.ai/blog

## Note on evidence chain

This file relays a sub-agent's report; its own tool transcript is not preserved here. Every number in the compiled `../docs/explore/control-planes.md` traces to this file. A future pass wanting first-hand primary pulls should re-fetch the URLs above directly.
