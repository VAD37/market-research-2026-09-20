# agent-dashboard — competitor roster

Pass 1, 2026-09-16. Evidence: `../raw/agent-dashboard-pulls.md`, `../raw/agent-dashboard-source-index.md`. Market read: `../markets/agent-dashboard.md`.

Roster, not profiles. Full profiles only for the idea that survives the cut.

## Observability and eval — funded, and being bought

| Company | Sells | Funding + date | Headcount | Traction | Weak at |
|---|---|---|---|---|---|
| LangChain / LangSmith | Observability + orchestration | $125M B Oct 2025, $1.25B val ($1.3B per one source) | unknown | $16M ARR 2025 (analyst-derived) | Locked to LangChain ecosystem. No self-host below Enterprise |
| Braintrust | Eval and observability | $80M B Feb 2026, $800M val | unknown | Notion, Replit, Cloudflare, Ramp, Dropbox | No self-host below Enterprise. Scores after the fact, does not stop bad output or spend |
| Arize | Observability and eval | $131M total, $70M C Feb 2025, $741.84M val Apr 2026 | ~209–221 (conflicting) | Established enterprise base | Tracker data inconsistent |
| Langfuse | OSS observability | **Acquired by ClickHouse 2026-01-16** (ClickHouse raised $400M at $15B) | 16+ pre-acquisition | 2,000+ paying customers, 19 of Fortune 50 (company-stated) | Self-host needs ClickHouse + Postgres + Redis + S3. Heavy |
| Helicone | OSS observability + gateway | **Acquired by Mintlify 2026-03-03** | unknown | 16,000+ orgs, 33M end users, 14.2T tokens (company-stated) | Feature development ended. Maintenance mode |
| AgentOps | Agent monitoring | $2.6M (645 Ventures, Afore, Plug and Play) | small | — | Agent-specific, weak for non-agentic LLM apps |

## Orchestration and no-code

| Company | Sells | Funding + date | Headcount | Traction | Weak at |
|---|---|---|---|---|---|
| n8n | No-code orchestration | $254M total. $180M C Oct 2025 at $2.5B, then $5.2B May 2026 (SAP investment) | unknown | $40M ARR claim, single-sourced | Visual flows still need technical setup for agentic parts |
| CrewAI | Multi-agent orchestration | $18M, date unclear | unknown | 1.3M monthly PyPI installs. "Most Fortune 500" (company-stated) | Enterprise pricing opaque, est. $60–120k/yr |
| Lindy | No-code AI employees | $53.6M total, $35M B Jan 2023 | unknown | — | $288M valuation is a third-party estimate, not disclosed |

## Control plane and governance — the contested square

| Company | Sells | Funding + date | Headcount | Traction | Weak at |
|---|---|---|---|---|---|
| Nous Research (Hermes Agent) | OSS single-agent runtime + dashboard. Business and Enterprise tiers exist, launch date unconfirmed | ≥$75M in talks Jul 2026 at $1.5B. $70M prior | unknown | **246,092 stars, 51,404 forks, 401 contributors (GitHub API, 2026-09-16)** | Dashboard is single-instance. No multi-user auth, no fleet view, no cost tracking |
| Fiddler AI | Enterprise agent governance control plane | unknown | unknown | Gov, defense, finance, health, insurance verticals | Pricing opaque. Heavyweight enterprise sale |
| Omnara | OSS agent control plane | undisclosed. Claimed broad VC list, unverified | unknown | 2.9k GitHub stars | Small ecosystem vs the Claude Managed Agents it mimics |
| Decawork (YC S26) | **Company-specific models that approve AI actions** across marketing, HR, IT, security, finance, engineering | undisclosed, YC-backed | **2 — Aman Raj (CEO), Sarthak Aggarwal (CTO)** | Active, SF, Product Hunt. No customer or revenue figure disclosed | Pre-traction, no pricing. Broader scope than pass 1 recorded |

Decawork is the closest analog to the proposed team shape: two people, YC-backed, launched 2026. Watch it as a leading indicator.

## Platform vendors — not competitors, weather

Not fundable-to-beat. They set whether the category survives as third-party.

| Vendor | What they shipped | Date |
|---|---|---|
| Anthropic | Claude Agent SDK + Claude Managed Agents, hosted, Console-level multi-subagent auditability | Apr 2026 |
| Google | Gemini Enterprise (was Agentspace), Vertex Agent Builder folded in. Native dashboards, Unified Trace Viewer, governance | Oct 2025, Apr 2026 |
| Microsoft | Agent Framework 1.0, AutoGen + Semantic Kernel merged, enterprise telemetry and state | 2026 |
| OpenAI | AgentKit / Agent Builder **launched 2025-10-06, sunset 2026-11-30**. Folded into Agents SDK + Workspace Agents | 8-month lifespan |
| SailPoint + AWS | Agent identity governance as cloud-native feature | Mar 2026 |

## Open on this roster

- ~~Hermes Agent star count~~ — **resolved: 246,092, confirmed live via GitHub API 2026-09-16.**
- Hermes Business/Enterprise launch date — unknown, checked nousresearch.com/blog 2026-09-16. Tiers exist; no announcement post found.
- Omnara investor list — unconfirmed against primary filing.
- CrewAI round date, Arize headcount, n8n ARR — aggregator-sourced, inconsistent.
- Decawork, Fiddler, Omnara pricing — all undisclosed.
