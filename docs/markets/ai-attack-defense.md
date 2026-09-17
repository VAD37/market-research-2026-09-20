# ai-attack-defense — AI security for tech companies, offense and defense

Pass 1, 2026-09-16. Compiled from `../raw/ai-attack-defense-pulls.md` (35 source blocks) and `../raw/ai-attack-defense-source-index.md` (131 URLs). Competitors: `../competitors/ai-attack-defense-roster.md`.

Scope: authorized testing. Buyer tests its own systems, or a vendor sells that testing. No payloads or exploit steps recorded here — technique names and citations only.

## Market

Buyer is split between CISO/AppSec budget and ML/engineering eval budget. Which one owns it depends on org structure. No dominant buyer confirmed — vendor-comparison framing, no survey.

Budget weather: 69% of CISOs name AI their top investment priority, while overall security budgets are near flat — average 5% growth, 45% flat (analyst-derived, RH-ISAC via Help Net Security). Software rose to 35% of security budget from 29%. So AI security is funded by reallocation, not by new money.

**Services pricing — the number that matters for a small team** (vendor and aggregator-stated):

| Engagement | Price |
|---|---|
| One-time audit | $8k–$25k |
| Single-agent red team | $16k–$50k |
| Multi-agent / comprehensive | $50k–$150k+ |
| Continuous subscription | $5k–$20k/mo |
| Compliance-mapped assessment | $20k–$75k |
| Senior specialist hourly | $120–$200/hr |
| Average contractor hourly | ~$67.60/hr |
| Bug bounty per finding | $200–$100,000 (HackerOne, Bugcrowd) |

Sizing disagrees by 8x on the same base year. Side by side, never averaged. All analyst-derived.

| Source | 2025 base | Forecast | CAGR |
|---|---|---|---|
| Dataintelo | $500.8M | $8.04B (2035) | 32.0% |
| market.us | $1.3B | $18.6B (2035) | 30.5% |
| Research and Markets | $1.75B | $6.17B (2030) | 28.5–28.8% |
| Astute Analytica | $4.2B | $21.8B (2034) | 20.1% |

Gartner puts total AI spend at $2.59T in 2026, +47% YoY (analyst-derived). No AI-security-specific slice of that found.

Demand signal: AI red-teaming demand projected to rise 35% by 2028 "with almost no supply to meet it" (analyst-derived). Getastra: "most traditional pentest firms are not built to test it."

## Available solutions

Problem is **not** solved. Prompt injection is #1 on the OWASP LLM Top 10 while two-thirds of organizations use generative AI routinely.

| Tool | Category | Does | Price | OSS |
|---|---|---|---|---|
| Garak (NVIDIA) | Red-team scanner | 37+ probes: hallucination, injection, jailbreak, toxicity | free | Apache-2.0, **9,268 stars, 129 contributors** |
| PyRIT (Microsoft) | Red-team framework | Multi-turn and multimodal attacks (Crescendo, TAP) | free | MIT, **4,483 stars, 164 contributors** |
| DeepTeam | Red-team framework | 40+ vulns mapped to OWASP, NIST, ATLAS | free | Apache-2.0, **2,822 stars** |
| Promptfoo | Red-team + eval | 50+ vuln types, CI/CD, YAML | free 10k probes/mo, Enterprise custom | **25,180 stars. Acquired by OpenAI 2026-03-09**, stays OSS |
| NeMo Guardrails | Runtime guardrail | Dialog policy control, on-prem | free | OSS |
| Guardrails AI | Output validation | Composable validators | free | OSS |
| Snyk agent-scan | MCP / agent scan | 15+ risks: injection, tool poisoning, shadowing | free | OSS |
| MCP-Scan (ex-Invariant) | MCP security | Tool poisoning, MCP rug pulls | part of Snyk platform | mixed |
| Lakera Guard | AI firewall | Injection, jailbreak, PII detection. Claims 98%+ detection, under 50ms | subscription + free tier | commercial |
| HiddenLayer ModelScanner | Supply-chain scan | 35+ model formats: pickle, GGUF, safetensors | custom quote | commercial |
| HackerOne / Bugcrowd | Bug bounty | Crowdsourced AI vuln discovery | program fee | commercial |
| Gray Swan Arena | Crowdsourced red team | Jailbreak bounties, claims 15,000-hacker network | custom | commercial |

Note the shape: the **tooling is free and good**. Garak, PyRIT, DeepTeam and Promptfoo cover the taxonomy. What is scarce is people who can run them and write a report an auditor accepts.

## Compliance drivers

The decisive finding: **as of 2026-09-16 nothing forces a purchase yet.**

Pass-2 verification: the **Digital Omnibus is enacted law** — Regulation (EU) 2026/1744, published in the Official Journal 2026-07-24, in force 2026-07-27 "as a matter of urgency," six days before the original high-risk deadline. Pass 1's two deferral dates are confirmed exactly. One correction below: pass 1 lumped Art. 50 and GPAI together at 2026-08-02. GPAI has in fact applied since 2025-08-02.

| Regime | Forces | In force | Mandates purchase |
|---|---|---|---|
| EU AI Act — **GPAI, Chapter V (Art. 51–56)** | GPAI model obligations | **2025-08-02 — in force over a year** (Art. 113(b), unamended) | No red-teaming mandate |
| EU AI Act — Art. 50 transparency | Chatbot and synthetic-content disclosure | **2026-08-02** — untouched by the Omnibus | Partial. Transparency, not red-teaming |
| EU AI Act — deepfake and child-safety prohibitions | New prohibited-use categories | 2026-12-02 (filed) | No testing mandate |
| EU AI Act — high-risk, Annex III standalone | Conformity assessment, risk management | **2027-12-02 — confirmed, deferral is now law** | Yes, once in force. Biggest future driver |
| EU AI Act — high-risk embedded, Annex I | Same, embedded systems | **deferred to 2028-08-02** | Yes, once in force |
| NIST AI RMF | Voluntary guidance | no enforcement, no certification exists | No |
| ISO/IEC 42001 | Certifiable AI management system, third-party audit | voluntary | No. Increasingly a procurement checkbox |

The high-risk teeth — the clause that would require third-party AI testing — slipped from Aug 2026 out to Dec 2027 and Aug 2028. A business plan whose demand rests on the EU AI Act is a plan that starts earning in late 2027 at the earliest.

## Consolidation

Every well-funded pure-play got absorbed inside roughly 18 months of a marquee round.

| Acquirer | Target | Value | Date |
|---|---|---|---|
| Cisco | Robust Intelligence | ~$400M (analyst-derived) | Oct 2024 |
| Snyk | Invariant Labs | undisclosed | Jun 2025 |
| Palo Alto Networks | Protect AI | **$634.5M (filed, SEC)** | Jul 2025 |
| CrowdStrike | Pangea | ~$260M (analyst-derived) | Sep 2025 |
| Check Point | Lakera | ~$300M (analyst-derived) | announced 2025-09-16 |
| F5 | CalypsoAI | $180M (**press-reported — absent from F5's 8-K**) | 2025-09-11 (filed) |
| Cato Networks | Aim Security | ~$300–350M (analyst-derived) | 2025 |
| Cranium AI | AIceberg | undisclosed (aggregator-derived) | May 2026 |
| Anaconda | Enkrypt AI | undisclosed (aggregator-derived) | Aug 2026 |

Cisco, Palo Alto, CrowdStrike, Check Point, F5, Cato and Snyk are folding AI security wholesale into existing platforms — Prisma AIRS, Falcon AIDR, AI Trust Platform, SASE.

Frontier model vendors behave differently: they run their own bug-bounty and red-team programs rather than buying vendors, and they partner with independent arenas (Gray Swan works with OpenAI, Anthropic, UK AISI).

Read: the product lane exits by acquisition, not by IPO. That is a viable outcome but it requires venture scale first. The services lane is untouched by this consolidation.

## Services vs product — where a two-person team can play

Product requires enterprise sales. Every named commercial platform is contact-sales — no public pricing found for HiddenLayer, Mindgard, Lakera paid tiers, CalypsoAI, or Cisco AI Defense. A two-person team has no sales motion for that.

Services are open now. Boutiques and solos already win work: AI Red Teamers and Redbot Security market US-based senior engineers and "no outsourcing". Freelancers earn per finding via HackerOne, Bugcrowd, ActiveFence.

Realistic band for two people: **$8k–$50k one-time audits and single-agent engagements.** The $50k–$150k multi-agent enterprise tier needs a brand and an audit-ready report format.

The free OSS tooling is what makes this work — no scanner to build, delivery cost is low.

## Technical knowhow

Public, substantial, and free. OWASP LLM Top 10, OWASP MCP Top 10 (still beta), MITRE ATLAS (16 tactics, 84 techniques), NIST AI RMF — all cross-mapped. Techniques (prompt injection, jailbreak, PoisonedRAG, tool poisoning, MCP rug pulls) are published in arXiv papers and readable in OSS source: Garak's 37+ probes and DeepTeam's 40+ vuln types are literally on GitHub.

One strong engineer can stand up a credible offering in weeks by wrapping Garak + PyRIT + DeepTeam and mapping output to OWASP and ATLAS. The frameworks do the taxonomy work.

Moat is **not** the technique library — that is public. Four candidates, in order of reachability for a small team:

1. **Compliance-report paperwork** mapped to frameworks auditors accept. Boring, learnable, and what buyers actually pay for.
2. **Proprietary attack research** — novel findings generate PR and trust ahead of commoditized OSS coverage. Mindgard's Cursor IDE zero-day is the model.
3. **Reputation for enterprise procurement.** Slow to build, hard to skip.
4. **Maintained adversarial corpus.** Lakera claims 100,000 new adversarial samples analyzed daily. A data and ops moat, not an algorithm moat. Out of reach for two people.

## AI-search overlap — confirms idea 1

Independently confirmed with fresh evidence. No vendor defends against answer-engine poisoning as of 2026-09-16.

- Wraith.sh explainer on answer-engine poisoning states plainly: "The document makes no mention of any commercial products designed to detect or defend against answer-engine poisoning."
- **Schneier, 2026** — a fabricated claim placed on his blog was repeated as fact by Google AI Overviews and ChatGPT within a day.
- **arXiv 2406.18382** (Nestaas, Debenedetti, Tramèr) — a targeted product became **2.5x more likely to be recommended**.
- **PoisonedRAG** — USENIX Security 2025.
- The funded GEO/AEO category (Profound, Semrush, Scrunch, Bluefish) monitors visibility. Marketing tooling, not integrity tooling. One comparison site frames adversarial manipulation as a future "regulatory and ethical question the industry must address proactively" — i.e. not yet addressed.

Two independent passes, different sources, same conclusion. See `../findings/cross-read.md`.

## Gaps

- **Answer-engine poisoning is undefended.** Confirmed twice. Clearest unaddressed niche in this repo.
- **OWASP MCP Top 10 is still beta.** Agent and MCP security standards immature — tooling built against it tracks a moving spec. Also an opening: early and credible in MCP security is a position.
- **No public pricing anywhere in the commercial tier.** Hard for a small buyer to benchmark, and hard for a small competitor to price against. Transparent pricing is itself a differentiator.
- **Supply shortage.** Demand up 35% by 2028 with "almost no supply", and traditional pentest firms are not built for it.
- **No regulator mandate behind ISO 42001 or NIST AI RMF.** Procurement preference, not law.

## Caveats

- Market sizes disagree 8x on the same 2025 base ($500.8M vs $4.2B). Rough analyst estimates, not fact.
- Only Protect AI's $634.5M is SEC-filed. Robust Intelligence, Pangea, Aim Security and Lakera deal values are all reported or analyst-derived, not disclosed.
- Headcounts (HiddenLayer 169, Mindgard ~30) come from third-party people-data aggregators, not company-confirmed.
- Vendor performance claims — Lakera's 98%+ detection and under-50ms latency, Mindgard's 150+ vulnerabilities, Gray Swan's 15,000 hackers — all self-reported, none independently verified.
- ~~PyRIT star count~~ — **resolved: 115 was the archived Azure/PyRIT stub. Live microsoft/PyRIT has 4,483 stars.**
- Enkrypt AI/Anaconda and Cranium/AIceberg deals come only from aggregator profiles, no primary press release.
- ~~Digital Omnibus needs a primary re-check~~ — **done, see the compliance section. It is law, and the deferral dates are confirmed.**
- Deal values: Cisco/Robust Intelligence and CrowdStrike/Pangea are now SEC-confirmed as having happened, **but no filing states a dollar figure**. Check Point/Lakera (6-K, 2025-09-16) and F5/CalypsoAI (8-K, 2025-09-11) likewise contain zero dollar figures. Only Protect AI's $634.5M is a filed number. Cato/Aim and Cranium/AIceberg could not be confirmed against any primary — both sites are JS-rendered and returned empty.
