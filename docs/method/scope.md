# Scope

Standing brief. Set 2026-09-16. Everything in `docs/` serves this.

## Decision served

Pick which of three AI product ideas, if any, is worth building. Two people: the user (technical, builds) and a collaborator (animator, storyteller, business and front-of-house). Neither has committed capital or time yet. Output of this repo is evidence for a go / no-go / narrow-it, not the decision.

## Questions, every idea, in order

1. **Market** — does a buyer exist, who is it, what do they pay today, how big is the spend.
2. **Available solution** — what can a buyer use right now, free or paid. Is the problem already solved well enough.
3. **Competitors** — who is already trying to solve it. Funding, headcount, traction, and what they are bad at.
4. **Technical knowhow** — what is the base capability needed, is it public, how hard is the build, what is the moat if any.

## Ideas under review

| ID | Idea | Read |
|---|---|---|
| `ai-search-ads` | AI search engine / ads injection testing | Visibility and manipulation of AI-generated answers. Covers both the marketing read (GEO / AI search visibility) and the adversarial read (injection into answer pipelines) |
| `agent-dashboard` | AI assistant manager dashboard, Hermes agent | Control plane for running and supervising AI assistants. Hermes = the open-weight agent model line assumed as the substrate; confirm before building on it |
| `ai-attack-defense` | AI research + defense for tech companies, offense too | Red-teaming and guardrails for AI systems. Preference stated: small tool that works and scales, not a platform play |

Fourth idea left blank by the user. Open slot.

## Constraints

- Team of two. No funding assumed. Build effort is one technical person.
- Collaborator travels; remote-first, async. Weighs toward a product that sells without a field sales motion.
- User's own stated preference: work on what they are good at — the technical side.
- Geography of the buyer is open. The collaborator has signalled against a US-based life; whether that rules out a US-buyer product is a business call, not a research finding. Note it, do not assume it.

## Out of scope

Pricing strategy, brand, and the partnership terms. Not researched here.

## Pass 2 — opened 2026-09-16

Pass 1 answered the four questions for all three ideas and produced a cross-read with no verdict. Pass 2 narrows to what pass 1 could not settle, plus two additions the user named.

Five agents, parallel. The user lifted pass 1's one-at-a-time constraint on 2026-09-16, cap of five.

| # | Agent | Question |
|---|---|---|
| 1 | `buyer-integrity` | Who pays for answer-engine integrity and AI-ad integrity. Pass 1's #1 open question |
| 2 | `injection-feasibility` | Can AI-search crawlers be identified from a domain you control (published IP ranges, rDNS, user-agent, ASN), which engines retrieve live, and what the policy boundary is |
| 3 | `ai-trend-suite` | Wide-angle read on AI product and solution-suite trends as of 2026-09 — categories forming, what is bundling, what works at two people |
| 4 | `verify-pass2` | Fact-check. Settles pass 1's unverified and conflicting numbers against primary sources |
| 5 | `services-lane` | Tests pass 1's services conclusion against real procurement pricing, and looks for evidence that kills it |

Agent 2 scope is authorized testing on infrastructure the tester controls. Detection, measurement and policy only. No payloads, no third-party targeting.

Agent 4 is adversarial toward this repo's own contents: a pass-1 number proved wrong is a success. Agent 5 is adversarial toward pass 1's strongest conclusion, by instruction.

Pass 1's open questions are all now assigned — 1 to agent 1, 2/3/4/7 to agent 4, 5 to agent 5, 6 to agent 4.

## Pass 3 — opened 2026-09-16

Question set changed shape. Passes 1–2 tested three product ideas. Pass 3 tests **the team**: what two-founder AI companies actually look like, where the gaps are, and whether a US product can be re-pointed at a local market.

Team shape on the table: one technical founder (the user), one business/creative founder (animator, storyteller). Pass 3 is scoped to that pair, not to a generic startup.

**Geography CONFIRMED by the user on 2026-09-16.** Ho Chi Minh City, Vietnam. Strong local developer talent, and **no US market access** — that last one is the stated constraint and it reframes the whole question. Singapore enters scope as the access layer. Agent 4 was re-briefed mid-run: Layer A unchanged, Layer B rescoped to named local success stories, the Singapore holding-company route, and how a Vietnamese team sells to a US buyer with no US entity.

**Browser access granted 2026-09-16.** The user enabled the Chrome extension for reading pages that block automated fetch. Pass 2 lost material to HTTP 403 on OpenAI, Perplexity, Gartner, Cloudflare Radar, EUR-Lex, peec.ai, Semrush, Cato and Cranium. Those are now reachable. Future agents may be granted browser tools; the main thread used them on 2026-09-16 to close question E2.

Five agents, parallel, sonnet.

| # | Agent | Question |
|---|---|---|
| 1 | `two-founder-cases` | Named AI companies with exactly two founders. Backgrounds, product, revenue, time to first money |
| 2 | `creative-technical-pair` | The technical + storyteller pairing specifically. Where creative AI companies make money, and who runs the business half |
| 3 | `market-gaps-2026` | What is unbuilt or badly built as of 2026-09. Whitespace, not categories |
| 4 | `localization-play` | Does re-pointing a proven US product at a local market work. Evidence both ways |
| 5 | `first-customers` | How two-person AI companies get the first ten paying customers. Channel, not product |

Standing constraint carried forward: agents write raw pulls only. No agent writes into `markets/`, `competitors/`, `customers/` or `findings/`. The main thread compiles.

**Quota note.** Pass 2 exhausted WebSearch at 200/200. Pass 3 agents are told to prefer direct fetch and API calls, and to budget search.
