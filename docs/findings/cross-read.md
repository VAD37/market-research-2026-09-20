# Cross-read — three ideas, pass 1

2026-09-16. Compiled from `../markets/ai-search-ads.md`, `../markets/agent-dashboard.md`, `../markets/ai-attack-defense.md` and the three rosters in `../competitors/`. No new facts here — every number traces back to those files and through them to `../raw/`.

Scope of the pass: `../method/scope.md`. Three ideas, four questions each, one research agent per idea, run in sequence.

## Side by side

| | `ai-search-ads` | `agent-dashboard` | `ai-attack-defense` |
|---|---|---|---|
| Buyer exists | Yes, brand and SEO teams | Yes, and a newly named one — HBR's "AI Agent Manager", Feb 2026 | Yes, CISO/AppSec or ML platform, split |
| Buyer proven to pay | Yes. $29–$828/mo tools, funded vendors | Yes, at developer tier. Non-technical tier unproven | Yes. $8k–$150k engagements, day rates public |
| Problem solved already | Tracking yes. Injection integrity no | Tracing yes. Orchestration yes but headless. Governance no | No. Prompt injection is OWASP #1 and supply is short |
| Competitors funded | Profound $131M, Peec $29M | LangChain $125M B, Braintrust $80M B, Arize $131M | 9 acquisitions 2024–2026, one SEC-filed at $634.5M |
| Consolidation risk | Moderate. Incumbent SEO suites bundling | **Severe.** All three frontier vendors ship it natively | High for product, **nil for services** |
| Tooling cost to start | Build a sampler. Ops-heavy | Assemble OSS. Weeks | **Free.** Garak, PyRIT, DeepTeam, Promptfoo |
| Moat available to two people | Thin | Cross-vendor span, or non-technical UX | Compliance paperwork, original research |
| Revenue shape | Recurring SaaS, needs scale | Recurring SaaS, needs scale | **Per-engagement, works at n=1** |
| Regulatory tailwind | Google spam policy names AI-answer manipulation — a constraint, not demand | None found | EU AI Act high-risk — **deferred to 2027-12 / 2028-08** |

## The one thing two independent passes agreed on

**Answer-engine poisoning has no defender.** Agent 1 found it as a gap in the marketing space. Agent 3, researching a different market with different sources, was asked to confirm or contradict, and confirmed it.

Evidence, combined:

| Fact | Source | Label |
|---|---|---|
| Injection promoted low-ranked products, transferred to live perplexity.ai | arXiv 2406.03589, Pfrommer et al., EMNLP 2024 | peer-reviewed |
| Targeted product became **2.5x more likely to be recommended** | arXiv 2406.18382, Nestaas, Debenedetti, Tramèr | peer-reviewed |
| Corpus poisoning against RAG | PoisonedRAG, USENIX Security 2025 | peer-reviewed |
| Fabricated blog claim repeated as fact by Google AI Overviews and ChatGPT within a day | Schneier, 2026 | named practitioner test |
| Prompt injection ranked #1 for LLM apps, two editions running | OWASP Top 10 for LLM Apps 2025 | standards body |
| Malicious-category detections up 32% relative, Nov 2025 → Feb 2026 | Google, journalist-relayed | platform owner |
| AI-answer manipulation classified as Search spam, enforceable | Google spam policies page, confirmed 2026-09-16. Date of change unconfirmed | platform policy |
| "No mention of any commercial products designed to detect or defend against answer-engine poisoning" | Wraith.sh explainer | secondary, explicit |

It sits precisely between idea 1 and idea 3. The GEO vendors (Profound, Semrush, Peec, Scrunch, Bluefish) measure visibility and are funded to do it. The AI-security vendors (Lakera→Check Point, Protect AI→Palo Alto, HiddenLayer, Mindgard) defend applications and are being acquired. Neither covers the integrity of an answer engine's output.

Counter-reading, which the evidence also supports: a gap two well-funded adjacent industries have both declined to enter may be a gap with no budget behind it. The two literatures do not cite each other. Nobody found a buyer who owns this problem — brand marketing does not buy security, and the SOC does not own brand visibility. **Whose budget line pays for it is unanswered, and that is the question that decides the idea.** It is the first thing pass 2 should attack.

## Cross-cutting patterns

**1. The middle layer is being absorbed, fast.** OpenAI shipped Agent Builder 2025-10-06 and sunsets it 2026-11-30 — eight months. Anthropic shipped Claude Managed Agents Apr 2026. ClickHouse bought Langfuse Jan 2026. Mintlify bought Helicone Mar 2026, features already frozen. In security: nine acquisitions in two years. Any product that sits between a model vendor and its customer is on a clock.

**2. Free OSS sets the floor everywhere.** Garak, PyRIT, DeepTeam, Promptfoo, Langfuse core, NeMo Guardrails. Nothing a two-person team builds competes with free on features. What does not come free: judgment, reporting, and a name a buyer trusts.

**3. Services dodge both problems.** Consolidation cannot absorb a consultancy, and free tooling makes delivery cheaper rather than competing with it. The `ai-attack-defense` services lane is the only one of the three that pays at n=1 customers — $8k–$50k per engagement for a two-person team, with $120–$200/hr senior rates as the floor.

**4. Every compliance deadline that would force demand has slipped.** The EU AI Act's high-risk obligations moved from 2026-08 to **2027-12-02** and **2028-08-02**. NIST AI RMF has no enforcement and no certification. ISO 42001 is a procurement checkbox, not law. Any plan whose demand depends on regulation starts earning late 2027 at the earliest. Demand before then is discretionary.

**5. Original research is a documented entry ticket.** Invariant Labs, an ETH spinout under a year old, was acquired by Snyk in Jun 2025 for finding tool poisoning and MCP rug pulls. Mindgard's Cursor IDE zero-day is its lead marketing asset. In this market a published finding buys reputation faster than a product does.

## Against the team constraints

From `../method/scope.md`: two people, one technical builder, no capital, remote and async, no field sales.

| Constraint | `ai-search-ads` | `agent-dashboard` | `ai-attack-defense` |
|---|---|---|---|
| No capital | Fails. Competes with $131M | Fails. Competes with $125M and three platform vendors | Passes for services. Fails for product |
| No field sales | Fails at enterprise tier | Fails — every governance competitor is contact-sales | Passes. $8k–$50k audits sell without a sales team |
| One builder | Ops-heavy sampling at scale | Weeks to MVP, then a UX problem | Weeks. Tooling is free and public |
| Remote, async | Fine | Fine | Fine. Engagements are deliverable-based |
| Non-technical partner has a role | Content and GEO storytelling | Weak fit | **Strong** — writing the report, running the relationship, the trust-building side of a security sale |

The collaborator's stated strengths — storytelling, charm, business side — map onto a services motion better than onto a SaaS motion. A security audit sells on trust and reads as a document. That is the one place in this research where a non-technical partner is load-bearing rather than decorative.

> **Superseded in part.** Pass 2 ran on 2026-09-16 and answered or corrected much of what follows. Read [`pass2-read.md`](pass2-read.md) after this file. The open-questions list below is kept as the record of what pass 2 was sent to do; each item's outcome is in pass 2's own file.

## Open questions — pass 2

Ranked by how much each would change the decision.

1. **Who pays for answer-engine integrity?** Find one company that has bought anything in this shape, or one budget owner who says they would. Absent that, the gap stays theoretical.
2. **Does the EU AI Act deferral hold?** The "Digital Omnibus" amendments modified provisions beyond what pass 1 captured. Re-check against primary EC text, not summaries.
3. **Verify the Hermes Agent star count.** 100k / 214k / 246k in one week is not credible. Primary GitHub repo.
4. **Fetch primary pricing pages** for Profound, Peec, AthenaHQ, Ahrefs. Pass 1 priced them from comparison blogs, one of which was written by a competitor.
5. **Find real engagement pricing**, not aggregator ranges — a published SOW, a rate card, a procurement doc.
6. **Track Decawork** (YC S26, two founders, agent governance). Same team shape. Whatever happens to it is a cheap experiment run at someone else's expense.
7. **Resolve conflicts on file**: Profound $1B vs $1.8B, Peec's implied post-Series-A raise, PyRIT's real star count from the live repo.

## What this pass does not say

No verdict. Per `../../CLAUDE.md`, the go/no-go is the user's. The fourth idea slot in `../method/scope.md` is still blank, and an unbuilt option is not evidence against the three researched here.
