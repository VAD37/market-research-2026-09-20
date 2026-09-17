# AI security services — testing pass 1's strongest conclusion

Pass 2, 2026-09-16. Compiled from `../raw/services-lane-pulls.md` (42 blocks) and `../raw/services-lane-source-index.md`. Companion to `ai-attack-defense.md`.

Pass 1 concluded the services lane was the only one of three ideas that pays at n=1: $8k–$50k engagements, free OSS tooling, untouched by nine acquisitions. This agent was told to attack that conclusion. **It found real damage.**

## Finding 1 — the price floor is lower than pass 1 recorded

Pass 1's floor was $8k, from aggregator ranges. Vendor price sheets say otherwise.

| Source | Price | Label |
|---|---|---|
| **Cobalt.io, Autonomous Pentest** | **$3,500 per test** | vendor-published, live price |
| Astra, AI pentest | $5,000–$50,000+ | vendor-published |
| Synack, web app | $5,000–$30,000 | vendor-published |
| deepstrike, web app | $5,000–$30,000+ | vendor-published |
| Synack, market average per engagement | **~$18,300**, typical $10k–$30k | vendor-published |
| Synack, red team / adversary simulation | $30,000–$150,000+ | vendor-published |
| Synack, annual PTaaS | $20,000–$100,000+ | vendor-published |
| Hourly, skilled testers | $100–$300 | vendor-published |

Cobalt publishes $3,500 for an autonomous pentest, below pass 1's entire floor. Its "AI & LLM Pentest" is a named SKU **with no price shown**.

**There is no AI premium.** Astra's AI band ($5k–$50k) overlaps the standard web-app band ($5k–$30k) across three independent vendor price sheets. Pass 1 assumed AI testing commanded more. Three price sheets say it does not.

Autonomous platforms at the enterprise tier: Pentera ~$100k average deal (one source) or ~$50k/yr (another); NodeZero ~EUR 35,000/yr, unlimited testing in scope. Both third-party estimates, conflicting, side by side.

## Finding 2 — nobody is required to buy this. Auditors ask anyway.

Checked every regime named in the brief. **No regulator mandates AI red-teaming.**

| Regime | What it actually says | Date |
|---|---|---|
| NYDFS frontier-AI advisory | "additional testing and validation procedures, including human oversight, for AI-generated code." Code review, **not red-teaming** | 2026-05-21 |
| FCA AI Lab | Voluntary sandbox | 2026 |
| ISO/IEC 42001 | Red-teaming is optional supporting evidence for an AIMS, not a required test | — |
| SOC 2 | **"The AICPA has published no authoritative AI-specific SOC 2 standard"** | 2026 |
| EU AI Act | High-risk obligations deferred — see `ai-attack-defense.md` | 2027-12 / 2028-08 |

And yet, from the same SOC 2 source: *"auditors are now demanding AI-specific evidence in real engagements"* — model registry, prompt logs, **"red-team suites,"** and **"prompt-injection test artifacts: a documented adversarial test suite, results, and mitigation evidence."**

**That is the demand engine.** Not law. Auditor and underwriter discretion running ahead of any written standard. It is softer than a mandate and it is already producing work today, which is the opposite trade-off from the EU AI Act.

Two supporting channels:

- **Cyber insurance.** 81% of carriers now include AI governance questions at renewal. Questionnaires grew from ~30 questions to **200–400**. Seven standard AI questions all ask for *documentation* — written AI use policy, training records, risk assessment on file — **none names third-party red-teaming**. One report of "AI Security Riders" requiring proof of red-teaming could not be tied to a named carrier: `unknown — checked 2026-09-16`. Policies are carrying AI sublimits (example: a $5M policy capped at $500K for AI incidents).
- **Vendor security questionnaires** reportedly ask whether a product "underwent independent AI red teaming, which attack classes were tested, what evidence exists." Could not confirm CSA's CAIQ has such a field: `unknown — checked 2026-09-16`.

OWASP published **Vendor Evaluation Criteria for AI Red Teaming Providers & Tooling v1.0 on 2026-02-04** — a standards body writing the buyer's checklist. That is the document a small firm would need to score well against.

## Finding 3 — the government does not buy this

Strongest negative in the pass, and the strongest label available: **procurement-filed**.

Querying the GovAI Contracts tracker (700 US federal AI/ML awards, drawn from USAspending and SAM.gov APIs, refreshed every 6 hours):

- **"penetration testing" → zero records.**
- **"prompt injection" → zero records.**

What the federal money does buy:

| Vendor | Value | What | Dates |
|---|---|---|---|
| HiddenLayer (USAF) | **$1.80M** | "Machine Learning Security Attack Workbench for Red Teaming of Autonomous Assets" | 2024-02-09 → 2025-08-11 |
| HiddenLayer (USAF) | **$1.25M** | ML detection and response vs adversarial ML | 2023-09-21 → 2025-03-24 |
| AI2 Incorporated (USAF) | $1.35M | Secure LLMs for critical DAF applications | 2024-08-16 → 2025-12-16 |
| Aperio Global (DHS/USCIS) | $1.54M | "Cybersecurity artificial intelligence support" — broad labor | 2024-10-18 → 2025-05-31 |
| CACI NSS (DHS) | $1.29M | AI safety and security steering committee support | — |

Every dollar goes to **tooling R&D or broad advisory labor**. None buys an AI red-team engagement as a named line item. Pass 1 expected procurement to confirm its price band. It did the opposite: it showed the buyer category does not exist in federal contracting yet.

Caveat on scope: this tracker filters on six NAICS codes plus AI keywords. AI testing bought inside a general cybersecurity contract would not appear. UK and EU procurement portals returned 403.

## Finding 4 — automation is actively eating this lane

The counter-evidence pass 1 did not have.

**XBOW** — autonomous AI pentester. Reached **#1 on HackerOne's US leaderboard** in Q2 2025 with ~1,060 reports (54 critical, 242 high, 524 medium in a 90-day window), earning 2,059 points against human researchers who build reputation over years. Raised **$75M (2025-07)** then **$120M (2026-03-18)**.

Its pricing page says the quiet part out loud:

> "Usage-based pricing that scales with your coverage, not a fixed annual engagement."
> **"It's coverage without the headcount."**

That sentence is aimed directly at the lane pass 1 recommended.

**HackerOne cut Internet Bug Bounty payouts by over 75% on 2026-05-22:**

| Severity | Was | Now |
|---|---|---|
| Critical | $9,250 | **$2,257** |
| High | $4,429 | $1,009 |
| Medium | $1,843 | $297 |

Stated reason: *"AI-assisted tooling has made the discovery of plausible security flaws significantly cheaper and faster, and the volume of reports flowing into open-source security programs has grown to the point where maintainers are struggling to process them."* The IBB program is **paused and not accepting submissions.**

The same source names what survives: *"finding a plausible bug is becoming commoditised, but the work of verifying impact, deduplicating reports, making patch decisions, and coordinating disclosure remains an irreducibly human and time-intensive process."*

That is the defensible position, and it is narrower than pass 1's.

## Finding 5 — bounty income is not a living

| Program | Payout | Note |
|---|---|---|
| OpenAI Safety Bug Bounty | up to $100k; standard max $20k | Launched Mar 2026, $1M annual pool |
| OpenAI Security | $200–$100,000 | — |
| Anthropic Model Safety | **max $15,000** per finding | ~$550,835 paid total as of May 2026 |
| Google AI VRP | up to $30,000 base | **Prompt injection and jailbreaks explicitly excluded** |
| Microsoft Copilot | $250–$30,000 | Updated Apr 2026 |
| Cross-program median | **$500–$5,000** | — |
| Median AI/LLM bug, 2026 | **$500–$2,500** | — |

AI vulnerability reports rose 210% and prompt injection 540%; AI features are in scope on 1,100+ HackerOne programs, up 270% YoY. Volume up, price per finding down — which is the commoditization curve, not a market opening.

Anthropic's entire program has paid $550,835 across its lifetime. That is one mid-size consulting year, split among everyone who ever participated.

## Finding 6 — where the incumbents actually landed

| Firm | Revenue | Headcount | Shape |
|---|---|---|---|
| Trail of Bits | $8.7M (2026) | 101 (2026-06-30) | ~$86k/head. Third-party aggregator, not confirmed |
| NCC Group | **£238.9M revenue, £17.1M net income** (FY2025) | 2,140 or 3,130 — sources differ by 46% | **Filed.** Public company |
| Praetorian | not disclosed | not disclosed | Now platform-first |

Trail of Bits at ~$86k revenue per head is the honest ceiling number for a boutique — respectable, not leveraged. NCC's £17.1M net on £238.9M revenue is a **7.2% net margin** at 2,000+ people: services scale into a low-margin business.

Praetorian is the productization case the brief asked for. It started in offensive services and now sells "Praetorian Guard... combining Agentic AI, Workflow Automation, and Offensive Capabilities" under one platform, claiming "25-50% spend reduction," with continuous pentest as one module rather than the headline. Contact-sales only.

Freelance rates: AI/ML specialists $50–$300+/hr by seniority. General cybersecurity consulting on the same platforms was reported **lower**, at $38–$64/hr. If that holds, "AI" is the premium word, not "security."

## What survives of pass 1's conclusion

Damaged, not dead. Revised:

| Pass 1 said | Pass 2 found |
|---|---|
| Floor is $8k | **$3,500 published.** No AI premium over standard pentest |
| Services untouched by consolidation | True of acquirers. **Not true of automation** — XBOW, $195M raised, "coverage without the headcount" |
| Compliance is the future driver | Confirmed deferred. **Auditor discretion is the present driver** and it already works |
| Free OSS makes delivery cheap | Confirmed — and it makes it cheap for everyone, including XBOW |
| Pays at n=1 | Still the only one of three that does. But the defensible work narrowed to **verification, impact, and the report**, not discovery |

The discovery half of security testing is being automated in public, on a leaderboard, by a company that says so on its pricing page. The half that is not: verifying impact, deduplicating, deciding what to patch, coordinating disclosure, and producing an artifact an auditor accepts. Pass 1 named report-writing as the non-technical partner's role. That now looks less like the soft part of the offering and more like the part with a future.

## Caveats

- **WebSearch quota hit 200/200 mid-pass** (shared across five concurrent agents). Themes on buyer-side hiring channels, solo-operator income and boutique firm census were cut short.
- No first-person account of a solo operator's income from AI security work was found.
- UK Contracts Finder and TED returned 403. MAS and FedRAMP AI pages returned server errors. NYDFS's 2024 letter body 404'd on two attempts.
- NetSPI, Bishop Fox, Praetorian and Include Security revenue and headcount: not found.
- Trail of Bits' figures are from a data aggregator, not the company. NCC's headcount differs 46% between two non-primary sources; only its revenue is filed.
- The "AI Security Riders" requiring proof of red-teaming, and the CAIQ AI red-teaming field, are both unconfirmed against any named primary document.
- Pentera and NodeZero prices are third-party estimates. Neither publishes a rate card.
- XBOW's leaderboard position is company-stated from its own blog. The ranking is externally visible; the disposition breakdown is not independently verified.
