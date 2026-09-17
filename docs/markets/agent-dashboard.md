# agent-dashboard — AI assistant manager dashboard, Hermes agent

Pass 1, 2026-09-16. Compiled from `../raw/agent-dashboard-pulls.md` (22 source blocks) and `../raw/agent-dashboard-source-index.md` (85 URLs). Competitors: `../competitors/agent-dashboard-roster.md`.

## Hermes — what it is

Two things from Nous Research, same name, different layers. The ambiguity in the brief resolves to the second.

| Candidate | What | Relevance |
|---|---|---|
| Hermes model line (Hermes 3, Hermes 4) | Open-weight LLMs. Hermes 4 released Aug 2025 in 14B / 70B / 405B. 14B Apache-2.0 on Qwen3-14B base; 70B and 405B inherit Llama 3 license. Hybrid reasoning, Hermes tool-calling format, JSON schema and function calling, 131K context. 405B reasoning-on: 96.2% MATH-500, 78.1% AIME 2025, 61.4% LiveCodeBench. Hosted via OpenRouter, HuggingFace, Nous Portal | The engine you point an agent at, not the dashboard |
| **Hermes Agent** | Open-source (MIT) self-hosted agent runtime **with a built-in web dashboard**. Released Feb 2026. Telegram, Discord, Slack, WhatsApp, Signal, CLI. Persistent memory, self-created skills, cron, subagent delegation, MCP, sandboxed execution (Docker/SSH/Modal). Dashboard on localhost:9119 = session browser, cron manager, API-key governance, log viewer, approval-mode config (`ask` / `yolo` / `deny`) | **This is the match.** It is already a single-agent control plane |

Nous Research: founded 2023 (Quesnelle, Malhotra, Teknium, Mitra). $70M raised; in talks Jul 2026 for ≥$75M at $1.5B (Robot Ventures lead, USV).

As of 2026-09-14 Nous added **Hermes Business** (team tier, shared credit pool, per-member caps) and **Hermes Enterprise** (self-hosted, contract pricing). So the OSS base is already monetizing upward into the tier a two-person entrant would sell.

**The opening inside it**: Hermes Agent's dashboard has no multi-user auth, no multi-agent orchestration, and no cost tracking (Context Studios analysis). It manages *one* Hermes instance, not a fleet of heterogeneous agents.

## Market

Buyer is splitting in two.

- **Technical buyer** — LangChain-native dev teams, ML and AI-ops engineers. The classic observability and eval buyer. Well served.
- **Operational buyer** — the "AI Agent Manager", a role HBR formally named Feb 2026 (Srinivasan, HBS + Wei, Salesforce). Explicitly domain-expertise-over-code. Average salary $103,178, range $55k–$194k. A Salesforce agent manager quoted: "I start and end my day in dashboards." Poorly served — that persona uses developer-first tools today.

| Figure | Value | Label |
|---|---|---|
| Enterprises with a formal AI agent owner / agentic ops lead | 56%, up from 11% in 2024 | analyst-derived, Gartner via secondary blog. Primary not fetched |
| Annual enterprise spend on agent evals + observability | $310k mid-market to $2.4M Fortune 500 | analyst-derived, attribution unclear in source |
| Enterprises raising 2026 eval tooling budget | 71% | Forrester/BCG via secondary source |
| New 2026 AI deployments that are action-based agents | over 70% | article-stated |

Sizing is unusable as a single number. Same year, same rough space, six reports, 5x spread — listed side by side, never averaged:

| Report scope | 2026 | Later | Source |
|---|---|---|---|
| AI Agent Observability | $0.9B | $14.0B (2035), 35.6% CAGR | globemarketresearch |
| Agentic AI Workflow Orchestration | $3.53B | — | Mordor |
| AI Agents (broad) | $10.9B | $182.97B (2033) | Grand View |
| AI Agent Orchestration Platform | $11.0B | $107.34B (2035) | SNS Insider |
| AI Orchestration | $13.99B / $13.96B | $60.34B (2034) | two near-duplicate reports |
| Agentic AI (broadest) | $19.33B | — | — |

**No report sizes "agent control plane / manager dashboard" as its own line.** It is a sub-feature everywhere.

## Available solutions

Four layers. Maturity differs sharply by layer.

**Observability and eval — mature, commoditizing**

| Tool | Does | Price | Free/OSS |
|---|---|---|---|
| Langfuse | Tracing, evals, prompt mgmt | Core $29–59/mo, Pro $199, Enterprise $2,499; 50k free units | MIT core, self-hostable |
| Helicone | Drop-in proxy, logging | ~$20/mo | Free tier + OSS |
| Arize / Phoenix | ML-grade tracing, evals | Phoenix free; Arize custom | Phoenix OSS |
| LangSmith | Traces, evals, playground, HITL annotation | $39/user/mo Plus, 5k free traces, $2.50/1k over | Self-host Enterprise only |
| AgentOps | Session replay for CrewAI, AutoGen, LangGraph | Free 5k events, Pro $40/mo | Partial free |
| W&B Weave | Traces, scorers, guardrails | Free tier, per-seat | Free tier |
| Braintrust | Eval-driven dev, regression scoring | $249/mo+ | Self-host Enterprise only |
| Portkey | Multi-provider gateway routing | $49/mo | — |
| Humanloop | Non-engineer prompt iteration | $750/mo | — |

**Orchestration and runtime — mature but headless. No fleet UI.**

| Tool | Does | Price | Free/OSS |
|---|---|---|---|
| LangGraph Platform | Managed deploy for LangGraph agents | Free dev tier, $39/user/mo Plus + usage | OSS framework MIT, paid platform |
| CrewAI | Multi-agent crews | Free OSS; Enterprise ~$60k–120k/yr | OSS + paid |
| AutoGen / AG2 | Multi-agent conversation | Free | OSS |
| Microsoft Agent Framework 1.0 | Merges AutoGen + Semantic Kernel, enterprise telemetry | Azure-bundled | Partial OSS |
| Temporal Agent Harness | Durable execution, crash-safe agents, tool-call approvals | Usage-based | Core OSS |
| OpenAI AgentKit / Agent Builder | Visual canvas + evals | Free with API usage | **Sunset 2026-11-30** |

**No-code and "AI employee"**

| Tool | Does | Price |
|---|---|---|
| Zapier Agents | Metered activities | Free 400/mo, $33.33/mo+ |
| Relevance AI | Coordinated multi-agent teams | $19–199/mo credit-based |
| n8n | Visual workflow, MCP-triggered agents | ~$20/mo cloud, self-host free |
| Lindy | Email, calendar, CRM agents | ~$20 to low hundreds/mo |
| Gumloop | Node-based data and scraping flows | usage-based |

**Identity, governance, approval gating — nascent. Being formalized in 2026, not solved.**

| Tool | Does | Price |
|---|---|---|
| Omnara | OSS control plane, durable state, RBAC. Markets as the open alternative to Claude Managed Agents | undisclosed, Apache-2.0 |
| Decawork (YC S26) | Agent identity, IT approval gate, audit, kill-switch | undisclosed |
| Fiddler AI Control Plane | Policy enforcement, fleet spend rollup, 100+ risk metrics | contact sales |
| SailPoint + AWS | Non-human-identity governance for agents | enterprise |

**Solved?** Tracing yes. Orchestration yes, but headless. Governance and approval no. A framework-agnostic manager dashboard for a non-technical buyer: not found as a mature product.

## Consolidation — the existential question

Answer: yes, fast, and from two directions.

| Event | Date | Read |
|---|---|---|
| ClickHouse acquires Langfuse | 2026-01-16 | Infra vendor absorbs observability to sell data-platform seats. ClickHouse itself raised $400M at $15B |
| Mintlify acquires Helicone | 2026-03-03 | Devtools vendor absorbs observability + gateway. Feature development already frozen, maintenance mode |
| OpenAI kills Agent Builder + Evals | launched 2025-10-06, wind-down 2026-06-03, sunset 2026-11-30 | **~8-month lifespan.** Folded into Agents SDK (code) and Workspace Agents (ChatGPT-native) |
| Anthropic Claude Managed Agents | Apr 2026 | Hosted, Console-level multi-subagent auditability. Anthropic's own manager dashboard |
| Google Agentspace → Gemini Enterprise | 2025-10-09; Vertex Agent Builder folded in Apr 2026 | Native agent performance dashboards, Unified Trace Viewer, governance built in |
| Microsoft Agent Framework 1.0 | 2026 | Same absorption from the framework side |
| SailPoint + AWS partnership | Mar 2026 | Agent identity governance becomes a cloud-native feature, not a category |

All three frontier vendors now ship their own agent-fleet console. OpenAI killed its own third-party-shaped builder in eight months — that is the clock speed on the middle layer. Independent observability survives by being framework-agnostic and multi-vendor, or by being bought for data-platform lock-in. A single-vendor dashboard play is directly in the blast radius.

## Technical knowhow

| Capability | Public? | Difficulty for one person | Note |
|---|---|---|---|
| Trace ingestion at volume | yes | real infra work | Langfuse's Postgres + ClickHouse + Redis + S3 split is documented. Copyable, not trivial to operate |
| OTel GenAI semantic conventions | yes, but **unstable** | low | As of 2026-07-17 no GenAI span, event, metric or attribute is marked Stable. Content moved repos (v1.42.0, Jun 2026, includes MCP conventions). Pin versions, expect breakage |
| Durable execution and replay | yes | weeks, not months | Temporal is the public pattern. Used by Replit Agent 3, OpenAI Codex web agent, Cursor long-running automation |
| Human-in-the-loop approval gating | yes | concept commodity, UX not | Hermes `ask/yolo/deny`, Temporal tool-call approvals, Fiddler inline enforcement, Decawork IT gate |
| Cost attribution per agent run | yes | easy math, hard aggregation | Sandbox vendors expose per-run primitives. E2B and Daytona ≈$0.0504/vCPU-hr + $0.0162/GiB-hr; Modal ≈3x. Moat is cross-provider rollup, not arithmetic |
| Sandboxed tool execution | yes | buy, don't build | E2B, Modal, Daytona, Cloudflare, Vercel |
| Agent identity and governance | forming | least commodity tooling today | "Agentic IAM" only became a named category in 2026 |

Single-vendor MVP from existing parts (Langfuse OSS core + Temporal + E2B + OTel) is weeks for one strong engineer. The uncommoditized part is the cross-vendor fleet view with non-technical UX.

Moat: thin at infra — all of the above is public and increasingly OSS. Only two defensible grounds found: (a) credibly spanning multiple model vendors and frameworks in one plane, (b) UX for the non-technical AI Agent Manager, a persona the incumbents are architecturally not built for.

## Gaps

- **No cross-vendor fleet manager.** Every native offering is single-vendor (Hermes Agent, Claude Managed Agents, Gemini Enterprise). Every independent one is narrow — Decawork is IT-governance-only, Omnara is single-runtime, Fiddler is enterprise-vertical.
- **Hermes Agent's own dashboard**: no multi-user auth, no multi-agent orchestration, no cost tracking. Stated gap in the most directly relevant product.
- **Cost rollup for non-technical buyers.** Primitives exist at infra level. "What is agent X costing me this week" in plain language exists only behind contact-sales enterprise pricing.
- **Approval gating is config, not workflow.** Hermes `ask/yolo/deny` is a config field, not a review queue. Decawork gates IT provisioning, not manager-level task approval.
- **The HBR-named buyer has no purpose-built tool.** They currently use Agentforce and Copilot dashboards — vendor-locked, developer-shaped.

## Caveats

- ~~Hermes Agent stars unverified~~ — **resolved 2026-09-16 against the GitHub REST API. 246,092 stars is real**: `NousResearch/hermes-agent`, 51,404 forks, 43,490 open issues, 401 contributors, MIT, created 2025-07-22. Latest release v0.21.3 (tag v2026.9.14), published 2026-09-14, rolling up 338 PRs and 1,036 commits since v0.21.2. The highest of pass 1's three figures was the right one.
- Hermes **Business and Enterprise tiers are confirmed to exist** (portal.nousresearch.com/business, "Hermes Pro"), with **no price disclosed** and **no launch announcement found** — the 2026-09-14 date pass 1 recorded matches only the GitHub release, not a tier launch. Consumer tiers are Free / Plus $20 / Super $100 / Ultra $200 per month, all credit-based. Launch date: unknown — checked nousresearch.com/blog 2026-09-16.
- hermes-agent.org and hermesagents.net found in search, not verified as official. Possible unofficial mirrors. Do not cite as authoritative.
- Omnara's claimed investor list (a16z, Founders Fund, General Catalyst) came via startupintros.com, unusually broad for a 2.9k-star repo, not confirmed against a primary filing.
- HBR's "AI Agent Manager" article (Srinivasan/Wei, Feb 2026) not fetched directly. Salary and quote via a secondary blog.
- Market sizes range $3.53B to $19.33B for the same year depending on scope. Directional only.
- The $310k/$2.4M spend figure and the 56% / 71% survey stats trace only to secondary blogs citing Gartner, Forrester, BCG. No primary analyst report fetched.
- CrewAI's $18M round date and Arize headcount (209 vs 178 vs 221) come from aggregators with inconsistent snapshots, not filings.
- n8n's $40M ARR is single-sourced (valueaddvc.com), unconfirmed.
