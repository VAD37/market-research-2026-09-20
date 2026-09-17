# Niche shortlist, solution list, and the pick

Wave 2a, 2026-09-17. Inputs: `../explore/{aisb-inventory,shipping-tools,language-gap,sea-compliance-triggers,local-assets}.md` and the raw pulls behind them (`../../raw/`), plus the research layer (`../../../../docs/markets/ai-attack-defense.md`, `ai-attack-defense-services.md`, `vietnam-sg-access.md`, `../../../../docs/competitors/ai-attack-defense-roster.md`, `../../../../docs/customers/first-customers.md`, `../../../../docs/findings/market-gaps-2026.md`, `../../../../docs/method/scope.md`).

Standing constraints this file is scored against, from `scope.md` and `../../CLAUDE.md`: two people, one technical builder, HCMC Vietnam, **no US market access**, no funding, remote-first, no field sales motion, stated preference for a small tool that works over a platform play.

Verdict on the company is the user's. This file produces the evidence and the argument.

## 0. What is excluded before the shortlist, and why

| AISB row | Why it is not a niche here |
|---|---|
| 2.2 monitoring, 2.3 control protocols | Real gap. Buyer is a frontier lab — unreachable from HCMC, no self-serve motion |
| 2.4 safety simulator | Analysis technique, no identified buyer (`../explore/aisb-inventory.md`) |
| 6.3 prefix tuning | Needs embedding-level API access; few production APIs expose it |
| 7.1 RAND report, 7.4 GPU rowhammer | Consulting deliverable / hardware mitigation. Not software a pair ships |
| 7.3 NVIDIA container toolkit | Covered by generic Trivy/Snyk-class CVE scanners |
| 3.2 jailbreaking, 6.1, 6.2, 6.4 | Crowded or covered — see `../explore/aisb-inventory.md` |

---

## 1. Niche shortlist

Five niches, each stated at the width the brief demands: an operational problem one named kind of person has on one named kind of system.

| # | Niche, stated narrow | AISB descent |
|---|---|---|
| **N1** | Detect whether an open-weight checkpoint pulled from a hub had its refusal behavior removed or a trigger backdoor added, versus its claimed base | 5.1, 5.2, 5.3, 5.4 |
| **N2** | Grade a self-hosted LLM serving endpoint's configuration exposure: logprob/top-k leakage, assistant-prefill acceptance, control-token passthrough, extraction economics | 1.1, 1.2, 1.3, 3.5 |
| **N3** | Turn OSS red-team scanner output into an ATLAS-mapped evidence artifact a SOC 2 auditor or vendor security questionnaire accepts | 7.2 (+ services-lane Finding 2) |
| **N4** | Measure whether a shipping guardrail holds on **Vietnamese-language** input for a Vietnamese consumer or support chatbot, and keep it from regressing | 3.3, 1.4 |
| **N5** | Audit what a coding agent's harness actually grants it — file, shell, network scope — against what its policy claims | 2.1 |

### N1 — checkpoint behavioral integrity

Problem: a team deploys a community fine-tune or quant it did not train. Nothing tells it whether the weights were behaviorally edited. `../explore/aisb-inventory.md` row 5.1: HiddenLayer ModelScanner covers file-format threats (pickle, GGUF, safetensors) — **not** weight-level behavioral edits, which is the PoisonGPT threat model exactly.

Who has it: anyone self-hosting a checkpoint from a third-party publisher. In SEA that population is enlarged by local-language fine-tunes, which are community-published rather than vendor-published.

What they do today: read the author name and the download count. Optionally run a file-format scanner, which answers a different question.

### N2 — serving-endpoint exposure grading

Problem: a team runs its own model behind an OpenAI-compatible gateway and does not know whether that gateway returns logprobs, accepts an assistant-role prefill, passes control tokens through, or is configured so the output projection is cheaply recoverable.

Who has it: any team running vLLM/Ollama/LiteLLM behind an API — common in SEA for cost and data-residency reasons. Secondary buyer: the pentest firm asked to test that endpoint and holding no checklist for it.

What they do today: nothing named. `../explore/aisb-inventory.md` rows 1.1/1.2/1.3/3.5 all read NOTHING dedicated; garak probes touch 1.3 incidentally.

### N3 — ATLAS-mapped evidence artifact

Problem: a buyer is asked, by an auditor or a customer's questionnaire, to show **which** attack classes were tested and what the result was. Its scanner output is a log, not an artifact.

Who has it: any company selling software with an LLM feature into a US/EU customer, or through a SOC 2 audit.

What they do today: hand-built spreadsheets. `../explore/shipping-tools.md`: MITRE ATLAS (16 tactics, 84 techniques) has **no maintained interactive tool layer** — no ATT&CK-Navigator equivalent. DeepTeam maps vulns to ATLAS internally but ships no coverage artifact.

### N4 — Vietnamese-language guardrail conformance

Problem: a Vietnamese-language chatbot runs on a guardrail never measured on Vietnamese. Of the three most-cited shipping guardrails checked in `../explore/language-gap.md`, exactly one publishes a language list — Llama Guard 3 — and it stops at Thai. NeMo Guardrails is silent. Lakera's "Observing 100+ languages in real-time" is unverifiable marketing copy.

Who has it, named and sourced from `../../../../docs/markets/vietnam-sg-access.md`: **AI Hay** (HCMC, $10M Series A led by Argor Capital, "hơn 15 triệu lượt tải... hơn 100 triệu câu hỏi được đặt và trả lời mỗi tháng", VnEconomy 2025-07-02, company-stated), **Vbee** (2M+ users), **Filum AI** (HCMC CX platform, Singapore office, Nextrans/VinVentures-backed). Plus the larger, less glamorous population: HCMC software firms building LLM features for foreign clients — Vietnamese outsourcing bills $10–60/hour, Vietnam is a top-5 growth market for Upwork (same file).

What they do today: whatever moderation their model provider ships, or a keyword blocklist. No Vietnamese-specific guardrail number exists anywhere found in wave 1.

### N5 — coding-agent affordance audit

Problem: an agent harness's real grants (filesystem paths, shell, network egress) exceed what the team believes it granted.

Who has it: any team running a coding agent in CI or on a developer machine with repo write access.

What they do today: partial coverage only. `../explore/aisb-inventory.md` row 2.1: Snyk agent-scan / MCP-Scan cover MCP tool-poisoning (v0.6.3, 2026-09-10, active); **no product audits general file/shell/network affordance scope.**

---

## 2. Ranked solution list

Build size is a one-technical-person estimate in person-weeks — **estimated by this agent, not sourced.** "Reachable" answers: does this need a buyer relationship the founders cannot get from HCMC with no field sales motion?

| # | Product | Buyer | Outputs | Build | Defensible because | Killed by | Reachable? |
|---|---|---|---|---|---|---|---|
| **1.1** | `refusal-diff` CLI: behavioral diff of checkpoint vs claimed base | Self-hoster, model-registry owner | Pass/fail plus refusal-rate delta per category | 2–4 wk | Measurement method and its false-positive calibration | Signal may not separate abliteration from benign helpfulness tuning | Yes — pip/GitHub, no sales |
| **1.2** | Trigger-backdoor susceptibility scan (5.2 trigger-specificity eval) | Fine-tune commissioner | Suspect-trigger list, specificity scores | 6–10 wk | Search strategy over a huge trigger space | Search space defeats a small team; academic-only prior art | Yes, but weak result |
| **1.3** | Publisher-side release-integrity report attached to a public checkpoint | Model publisher | Signed, reproducible report | 3–5 wk | Trust artifact; first-mover on the format | Few SEA model publishers; nobody asks for it yet | Yes |
| **2.1** | Endpoint exposure grader — config audit for an LLM gateway | Team running own gateway; pentest firm | Graded report, per-check remediation | 3–5 wk | Check library plus grading rubric, maintained | garak extends probes; a hyperscaler ships it as default | Yes — OSS-led, self-serve |
| **2.2** | Extraction-cost estimator: queries and $ to recover output projection | Company serving its own fine-tune | "Recoverable at ~N queries / $X" | 4–6 wk | A hard number nobody else produces | Buyer population tiny — most SEA AI firms are API wrappers | Yes, market thin |
| **3.1** | ATLAS coverage matrix generated from garak/PyRIT/promptfoo output | AppSec lead, compliance owner | Coverage matrix, gaps named | 2–3 wk | `vendor/atlas-data` already local; report craft | MITRE ships a Navigator; it is a UI over free data | Yes |
| **3.2** | Questionnaire evidence pack: results mapped to questionnaire fields | Vendor answering a customer security review | Answer pack plus linked artifacts | 4–6 wk | Only candidate with a trigger quoted in this repo | Buyer sits in US/EU — the market this team cannot reach | **No** — US/EU buyer |
| **4.1** | Vietnamese guardrail benchmark and picker: published, free, measured | Anyone shipping a VN-language LLM app | Per-guardrail VI vs EN numbers | 1–2 wk | First measured Vietnamese number; language and buyer proximity | Numbers may come back showing no gap — see §4 | Yes — publishing, not selling |
| **4.2** | VI guardrail regression CI: locked corpus, block-rate delta gate | VN chatbot team, VN outsourcing shop | CI pass/fail plus delta report | 3–5 wk | Corpus curation and Vietnamese label quality | promptfoo already does CI red-teaming; VI corpus is the only differentiator | Yes, and in person in HCMC |
| **4.3** | Train a Vietnamese moderation classifier | Same | A model plus an API | 10–16 wk | Labeled VI data plus model weights | ML-engineering build; owner's record is audit, not model training | Yes, wrong skill |
| **5.1** | Agent affordance linter: declared policy vs real grants | Platform/DevEx team running agents in CI | Diff of granted versus declared | 3–4 wk | Harness-specific knowledge, kept current | Snyk extends agent-scan into it; hard to charge for a linter | Yes — OSS-led |

---

## 3. The demand problem, stated head-on

`../explore/sea-compliance-triggers.md`: **nothing in Southeast Asia mandates AI red-teaming or security testing as of 2026-09-17.** AI Verify is voluntary with no enforcer and no penalty. MAS FEAT is 2018 governance principles. Indonesia's UU PDP DPIA is a privacy impact assessment, and nothing in the sourcing says it must include adversarial testing. Vietnam's PDPL (Law 91/2025/QH15) requires transparency and impact assessments on automated decision-making, not third-party testing.

So every candidate has to name a non-regulatory trigger, or admit it has none.

| Product | Named trigger | Evidence grade |
|---|---|---|
| 1.1 / 1.2 / 1.3 checkpoint integrity | **None found.** Closest is an incident (PoisonGPT-class) or an internal model-registry gate | **"They should care."** No trigger sourced |
| 2.1 endpoint grader | Pentest scope item; a customer's vendor security questionnaire | Inferred — the questionnaire quote is about red-teaming generally, not gateway config |
| 2.2 extraction estimator | Protecting a proprietary fine-tune from a competitor | **"They should care."** No purchase evidence |
| 3.1 / 3.2 evidence pack | **Quoted.** SOC 2 auditors "demanding AI-specific evidence in real engagements... red-team suites... prompt-injection test artifacts: a documented adversarial test suite, results, and mitigation evidence" (`../../../../docs/markets/ai-attack-defense-services.md` Finding 2). OWASP published **Vendor Evaluation Criteria for AI Red Teaming Providers & Tooling v1.0, 2026-02-04** — the buyer's checklist | **Strongest in this file.** And the buyer is US/EU |
| 4.1 / 4.2 Vietnamese guardrail | Foreign client's vendor security questionnaire flowing downstream to a Vietnamese supplier; plus reputation and incident avoidance | Partly inferred. The downstream-questionnaire chain is **`unknown — not pulled`** |
| 4.x, if Vietnam content law bites | Vietnam's own content-control regime applied to a public-facing Vietnamese chatbot | **`unknown — not pulled`.** Highest-value open question in this file — see §6 |
| 5.1 agent affordance linter | An incident; a platform team's own hardening pass | **"They should care."** No trigger sourced |

Two honest reads fall out of this table:

- **The only quoted trigger points at a buyer this team cannot reach.** Auditor discretion is a US/EU phenomenon in the evidence available. `../../../../docs/markets/vietnam-sg-access.md`: Stripe does not support Vietnam; AWS Marketplace excludes Vietnam *and* Singapore; a Delaware entity formed from Vietnam does not produce a working Stripe account (Stripe support, confirmed 2026-06-16: "US-based accounts must have a physical presence in the United States").
- **The one trigger this team could reach is the one nobody pulled.** If a Vietnamese-language chatbot's content exposure is regulated in Vietnam, N4 converts from reputation-only to a compliance trigger. Wave 1 never searched it.

---

## 4. The Vietnamese wedge, argued both ways

### The case FOR, at its strongest

1. **No shipping guardrail confirms Vietnamese.** Llama Guard 3's own model card, fetched 2026-09-17: "supports content safety for the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai." NeMo Guardrails: no multilingual claim anywhere in the repo. Lakera: "100+ languages," no list. One list exists and Vietnamese is not on it.
2. **The newest general benchmarks still skip the region.** XSafety (arXiv 2310.00905) language folders, read from the repo itself: `ar bn de en fr hi ja ru sp zh` — zero SEA. ML-Bench (arXiv 2605.00689, 2026-05-01), 14 languages: twelve SEA language-name string searches returned zero matches. The blind spot is current, not historical.
3. **The Thai precedent proves the failure mode is real and measurable.** arXiv 2410.22153, Figure 1 caption: "The guardrails are providing inconsistent predictions for English and Thai inputs with the same semantic meaning. In this case, we are using LLaMa-Guard-3 as the guardrail model **which supports Thai**." A guardrail failed on a SEA language it *claims* to support. Vietnamese is not even claimed.
4. **This is the only candidate where the repo's best-evidenced sales channel is available to this team.** `../../../../docs/customers/first-customers.md` names referral through 1-on-1 pro-bono help inside influential groups as its strongest account, then names its own problem: that channel "assumes physical or social proximity to the buyer," which the team lacks — **for US buyers.** For AI Hay, Vbee, Filum AI and the HCMC outsourcing firms, the team has exactly that proximity. Every other candidate in this file forfeits it.
5. **The raw material exists and is public**: ViHSD (arXiv 2103.10069, 2021-03-18) and ViToSA (arXiv 2506.00636, 2025-05-31), neither integrated into any shipping guardrail checked.

### The case AGAINST, at its strongest

1. **The premise is unmeasured.** `../explore/language-gap.md`, verbatim: "No numeric Vietnamese-specific guardrail ASR or accuracy figure was found or extracted in this pass." The wedge rests on *absence of a claim*, not on a measured failure. Absence of a published language list is not evidence of failure.
2. **Vietnamese is not low-resource, and the famous paper does not cover it.** "Low-Resource Languages Jailbreak GPT-4" (arXiv 2310.02446, 79% ASR) does not mention Vietnamese in full text. Its languages are Zulu/Scots-Gaelic/Hmong-class. Vietnamese has ~85M speakers and a developed NLP base. **That literature is not evidence about Vietnamese**, and a pitch leaning on it leans on the wrong paper.
3. **Vietnamese safety evaluation already exists.** SEA-HELM (arXiv 2502.14301, 2025-02-20, AI Singapore per the listing) "currently supports Filipino, Indonesian, Tamil, Thai, and Vietnamese" with a named Safety pillar. Not virgin ground; a credible institution is already on it and can extend faster.
4. **The price collapses.** ITviec's 2025–2026 report puts senior Vietnamese backend salaries at ~54.9M VND/month (~$27,000/yr). A Vietnamese buyer will not pay the $8k–$50k band in `../../../../docs/markets/ai-attack-defense.md`. Selling locally trades market access for price.
5. **It violates the constraint it appears to satisfy.** Walking into AI Hay's office is a field sales motion. Cheap and local, but still field sales — the thing `scope.md` weighed against.
6. **Closable by an incumbent in one release.** If Meta adds Vietnamese to Llama Guard's list, or OpenAI's moderation endpoint is already fine on Vietnamese, the wedge disappears without anyone deciding anything.

### The single measurement that settles it

Replicate arXiv 2410.22153's Thai design on Vietnamese. Small enough to *be* the prototype, and its outcome decides whether N4 or the fallback is the business.

| Element | Specification |
|---|---|
| Guardrails under test | Llama Guard 3 8B (published list excludes Vietnamese); OpenAI `omni-moderation-latest` (the free default most VN apps land on); Lakera Guard free tier (tests the "100+ languages" claim directly) |
| Dataset | **ViHSD**, arXiv 2103.10069 — human-labeled Vietnamese toxic/constructive social-media comments. Exact label schema `unknown — not pulled`; confirm before sampling. Stratified subset, ~500–1,000 items |
| Paired condition | Each item submitted twice: Vietnamese original, and its English machine translation. Back-translate a sample for fidelity; discard items whose meaning did not survive |
| Metric 1 | **Recall on human-labeled toxic items, VI versus EN**, in percentage points, per guardrail |
| Metric 2 | **Paired verdict disagreement rate**, with direction — VI-pass / EN-flag is the safety-relevant miss |
| Reporting discipline | The 3-part ASR rule from `D:\ai\ai-playground\docs\reference\measurement.md` (2026-06-11): state the evaluator, state k, state binary-vs-averaged. k = 1, single-shot, no amplifiers |
| Boundary | Clean. Public academic dataset, defenses under test, no third-party system targeted, no jailbreak generation, no evasion tooling |

**Pre-registered decision rule — chosen by this agent, not derived from a source:**

| Result | Meaning |
|---|---|
| ≥15 pp VI-below-EN recall gap on at least one shipping guardrail, asymmetric toward VI-misses | **Wedge confirmed.** The team holds the first Vietnamese number of this kind — simultaneously the product's justification and its distribution |
| <5 pp gap on all three | **Wedge dead.** Vietnamese is adequately covered in practice. Fall back |
| Between, or a gap on one guardrail only | **Repoint.** The product is not "Vietnamese safety is broken" but "which guardrail should a Vietnamese app pick" — a published picker. Smaller, honest, weaker business |

Cost: ViHSD is public, the guardrails are free-tier or OpenRouter-routed (AISB already routes through OpenRouter, `../../raw/aisb-module-scan.md`). Days, not weeks, for one person.

---

## 5. The pick

### Primary — N4, product 4.1: the Vietnamese guardrail benchmark, run as the settling measurement

**Case for.** The only candidate where the team's structural position is an advantage rather than a cost — language, buyer proximity in HCMC, and a ~5x cost base against US builders (`../../../../docs/markets/vietnam-sg-access.md`). The only one where the repo's best-evidenced sales channel is reachable. It routes around every access wall in `vietnam-sg-access.md`, because publishing a benchmark needs no Stripe, no US entity, no marketplace listing. It is 1–2 weeks of work and it settles its own premise before further investment. `../../../../docs/findings/market-gaps-2026.md` independently concludes that access-shaped gaps are "the only one where being in Ho Chi Minh City is an advantage rather than a cost."

**Case against, stated as hard.** Its purchase trigger is the weakest of the three that have one at all — reputation, plus an inferred downstream-questionnaire chain **nobody has sourced**. The wedge may measure out flat, leaving a published negative result and no business. If it measures out real, monetizing still means selling to Vietnamese buyers at Vietnamese prices, or to foreign buyers through rails `vietnam-sg-access.md` documents as closed. And a benchmark is not a product: 4.1 is proof and distribution; 4.2 is the thing anyone pays for, and 4.2 competes with promptfoo — free, OSS, 25,180 stars, OpenAI-owned since 2026-03-09.

### Fallback — N1, product 1.1: `refusal-diff`

**Case for.** The cleanest absence claim wave 1 produced, and the one with a named incumbent whose limit is documented rather than assumed: HiddenLayer scans file formats, not behavior. AISB hands over the exact measurement techniques (5.1 efficacy/paraphrase/locality, 5.3 diff-in-means refusal direction). Needs no buyer relationship, no language, no geography — it ships as a pip package and a GitHub Action, the purest form of "small tool that works and scales." Least damaged by the HCMC access constraint.

**Case against, stated as hard.** It has **no purchase trigger at all** — the honest answer is "they should care." Its users are engineers pulling checkpoints, not budget holders; the buyers who would pay (model-registry owners, enterprises) are an enterprise sales motion this team does not have. It needs inference budget against two models, the one place the Vietnamese cost advantage does not reach. And the core technical risk is that the signal does not separate: an abliterated checkpoint and a checkpoint fine-tuned to be more helpful may look identical on a refusal-rate diff. That risk is knowable in about a week, which is the one thing in its favour.

### Third, and why it lost — N2, product 2.1: the endpoint exposure grader

Best fit for the owner's demonstrated skill — configuration auditing and report writing, per `D:\projects\audit-history` and `D:\audits` in `../explore/local-assets.md` — with no ML engineering and no GPU. It lost on two counts. Its absence claim is the **lowest-confidence** in the file: rows 1.1/1.2/1.3 read "NOTHING dedicated found," much weaker than 5.1's documented incumbent limitation, and garak's probe set already touches 1.3. And its trigger is inferred, not quoted. If 2b finds 2.1's absence claim holds and 1.1's does not, the fallback should swap.

### N3, and the platform question

3.2 has the strongest trigger in the file and is disqualified by geography, not merit. It also drifts toward a platform — an evidence-pack generator wants a dashboard, a customer portal and an integration surface — which `scope.md`'s stated preference weighs against. Recorded, not picked. If the team ever acquires US/EU market access, this row changes rank.

### The honest fourth option

"Nothing here clears the bar" is defensible on this evidence. Every candidate is untriggered, unreachable, or unmeasured. What makes N4 the pick is not that it clears the bar — it is that its premise can be tested for under a week of work, and the test is the prototype. That is a cheap way to find out, not a demonstrated business.

---

## 6. What wave 2b must attack

Ordered by how much of this file collapses if the claim is wrong.

**Absence claims — every one is a quota-constrained negative, the easiest kind to get wrong:**

1. **"Nothing detects a behaviorally tampered checkpoint."** The fallback rests entirely on this. Attack HiddenLayer's platform-level detection claim (contact-sales, unverified in wave 1), Protect AI / Palo Alto's post-acquisition line, Cranium, Pillar, and the academic-to-product path for Neural Cleanse / STRIP-class defenses. A single shipping product here kills N1.
2. **"No shipping guardrail supports Vietnamese."** Wave 1 checked three. Attack: OpenAI `omni-moderation-latest` language documentation, Azure AI Content Safety's published language list, Google Perspective API's language list, AWS Bedrock Guardrails, and Alibaba / SEA-region providers. **Perspective API in particular is a known multilingual moderation service and was never checked.** If it covers Vietnamese well, the primary pick weakens before the measurement runs.
3. **"Nothing audits LLM serving-endpoint configuration exposure."** Lowest-confidence absence in the file. Attack garak's probe list directly for prefill / logprob / control-token probes, and search for any LLM-endpoint hardening scanner.
4. **"MITRE ATLAS has no tool layer."** Check for an ATLAS Navigator fork, and whether `vendor/atlas-data`'s upstream ships a viewer.
5. **"Nothing audits general agent affordance scope."** Snyk agent-scan v0.6.3's actual check list was never read.

**Unsourced claims this file depends on, all flagged `unknown — not pulled`:**

6. **Vietnam's content-control regime as applied to a public-facing Vietnamese-language chatbot.** Highest-value single item on this list. If it exists, N4 gains a real compliance trigger and the whole ranking firms up. Wave 1 searched privacy and AI law, not content law.
7. **The downstream-questionnaire chain.** Does a foreign client's vendor security questionnaire actually reach a Vietnamese supplier building an LLM feature? Zero evidence either way. This is the stated trigger for the primary pick.
8. **ViHSD's label schema and licence.** The settling measurement's sampling design depends on it and it was never opened.
9. **SEA-HELM's actual Vietnamese safety score.** Wave 1 budgeted this out twice. If SEA-HELM already publishes a Vietnamese safety number, the settling measurement must be designed against it rather than in ignorance of it — and part of the "first number" claim dies.
10. **MAS primary guidance and Vietnam AI Law primary text.** Wave 1 rates `sea-compliance-triggers.md` its weakest file; MAS returned a maintenance error across two passes and the Vietnam AI Law content is carried forward from `pass3-read.md` unverified. A browser-equipped agent may now close both.

**Reasoning, not sourcing, to attack:**

11. Build-size estimates in §2 are this agent's, unsourced, and systematically optimistic in the direction that flatters the pick.
12. The §4 decision rule's thresholds (15 pp / 5 pp) are chosen, not derived. Argue them.
13. The claim that HCMC proximity restores the referral channel from `first-customers.md`. That account's client base was Y Combinator companies; whether the mechanism transfers to a Vietnamese buyer at a Vietnamese price is asserted here, not evidenced.
14. ML-Bench's SEA exclusion is a **string-search negative** on an ar5iv render, not a confirmed language list. Argument 2 of the case FOR leans on it.

**Boundary marks to verify rather than trust:**

15. Product 2.2 (extraction-cost estimator) is dual-use by construction — a tool that measures extraction cost performs extraction. In scope only if it runs against an endpoint the operator controls and never retains the recovered projection. 2b should decide whether that constraint is enforceable or whether 2.2 must be dropped.
16. Product 1.1 is the defensive half of AISB 5.3. Building the detector does not require shipping the abliteration tool. Confirm that separation holds in the design 2c produces.

---

## Caveats

- No niche in this file has a confirmed paying buyer. Section 3 is the reason, and it is a finding rather than a gap in the research.
- Every market absence traces to `../explore/`, which states its own limit: a "NOTHING" means no shipping product found in the sources checked, not an exhaustive survey. Wave 1 ran on an intermittent WebSearch quota.
- Build sizes, the §4 thresholds, and the ranking order in §2 are this agent's judgement, labeled as such, and are not sourced.
- The whole Vietnamese case rests on an *absence of a published claim* plus a *precedent in a different language*. No Vietnamese guardrail number exists in this repo. That is why the prototype is the measurement.
- `../../../../docs/customers/first-customers.md` carries its own health warning — most accounts date 2013–2021, and its strongest is n=1 from 2015. Argument 4 of the case FOR inherits that weakness.
- Pricing bands quoted from `../../../../docs/markets/ai-attack-defense.md` and `ai-attack-defense-services.md` are US/EU vendor-published or aggregator-derived. No SEA price point for AI security testing exists anywhere in this repo.
