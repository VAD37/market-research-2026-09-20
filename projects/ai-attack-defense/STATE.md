# STATE — ai-attack-defense

Append-only running log. Newest entry at the bottom. Write the plan BEFORE the work, the result AFTER it. An agent that dies mid-run must leave its successor enough to continue.

Entry format:

```
## <UTC+7 timestamp> — <agent role> — <phase>
PLAN: what is about to happen
DID: what happened
FILES: paths written
OPEN: what is unfinished, and what the next agent should pick up first
```

---

## 2026-09-17 — main thread — scaffold
PLAN: create project folder, brief, state log.
DID: folder skeleton + `CLAUDE.md` written from `MegaPlan.md` and the three research passes in `../../docs/`.
FILES: `CLAUDE.md`, `STATE.md`, `docs/{explore,plan,design,review,execution,outcome}/`, `raw/`, `prototype/`.
OPEN: explore phase not started.

## 2026-09-17 — explore agent — phase 1 (inventory)
PLAN: read AISB module tree (D:\ai\aisb), scan local reuse candidates (D:\ai\security, D:\ai\growtrics-llm-engine, D:\ai\ai-playground, D:\projects\lv1-auditor, D:\projects\lv1-wizard, D:\projects\smart-contract, D:\projects\audit-history, D:\audits, D:\hackathon). Write raw/ pulls, then docs/explore/{aisb-inventory,local-assets,shipping-tools,language-gap,sea-compliance-triggers}.md. Budget WebSearch — prefer direct fetch, note if quota still exhausted.
DID: (in progress)
FILES: (pending)
OPEN: starting now.

## 2026-09-17 — explore agent — raw pulls complete
DID: Read all 26 AISB module READMEs + top-level CLAUDE.md/AGENTS.md/README.md (D:\ai\aisb). Scanned 9 local reuse dirs (D:\ai\security, ai-playground, growtrics-llm-engine; D:\projects\lv1-auditor, lv1-wizard, smart-contract, audit-history; D:\audits; D:\hackathon) — strongest find: D:\ai\ai-playground (attack taxonomy, guard-layer L0-L4/A-F crossmap, ASR measurement methodology, ~35 vendored tools incl. garak/PyRIT/promptfoo/giskard/deepeval/ART). Pulled live GitHub repo+release metadata via `gh api` for 12 shipping tools (no WebSearch spent). Pulled arXiv abstracts + full-text language-name searches for 7 multilingual-safety papers plus 2 Vietnamese-specific toxicity datasets, and checked 3 shipping guardrails' own language-support claims (Llama Guard 3: Thai only, no Vietnamese; NeMo: silent; Lakera: vague "100+ languages"). Pulled SEA compliance-trigger evidence (Singapore AI Verify = voluntary; MAS FEAT = principles, not testing mandate; Vietnam PDPL Law 91/2025/QH15 eff. 2026-01-01; Indonesia UU PDP 2% revenue fine) — this file is weaker-sourced (WebSearch synthesis, primary MAS/Vietnam-law text not reached).
FILES: raw/aisb-module-scan.md, raw/local-assets-scan.md, raw/shipping-tools-github-pulls.md, raw/language-gap-pulls.md, raw/sea-compliance-pulls.md.
OPEN: WebSearch quota flaky (2 of ~10 calls failed mid-session, rest succeeded) — noted, not blocking. Next: write the 5 docs/explore/*.md compiled deliverables from these pulls.

## 2026-09-17 — explore agent — phase 1 complete
DID: Wrote all 5 required docs/explore/*.md deliverables from the raw pulls: aisb-inventory.md (26-row module table, 14 NOTHING/thin rows, strongest candidates flagged as checkpoint-integrity [5.1/5.2/5.3], API-extraction-surface auditing [1.2/3.4/3.5], and ATLAS tooling [7.2]), local-assets.md (D:\ai\ai-playground is the one real reuse asset — taxonomy + ASR measurement methodology + ~14 vendored OSS tools; everything else scanned is Web3/unrelated), shipping-tools.md (12 tools re-verified via live GitHub API, 2 net-new additions beyond the roster: Llama Guard 3's language list, MITRE ATLAS's missing tool layer; Rebuff confirmed dead, LLM Guard ambiguously archived), language-gap.md (real but narrower gap than assumed: major benchmarks XSafety/ML-Bench exclude all SEA languages; Thai has a measured guardrail-inconsistency finding, Vietnamese does not; SEA-HELM is the one benchmark naming Vietnamese safety; Llama Guard 3 supports Thai not Vietnamese; the "low-resource jailbreak" literature does NOT test Vietnamese, which is medium-resource), sea-compliance-triggers.md (weakest-sourced file — no SEA regime mandates AI red-teaming; Indonesia's DPIA requirement is the closest thing to a trigger; MAS/Vietnam-AI-Law primary text not reached, WebSearch quota intermittent).
FILES: docs/explore/{aisb-inventory,local-assets,shipping-tools,language-gap,sea-compliance-triggers}.md, raw/{aisb-module-scan,local-assets-scan,shipping-tools-github-pulls,language-gap-pulls,sea-compliance-pulls}.md.
OPEN: Explore phase done. Nothing selected, no niche picked, no plan written — per boundary, that is phase 2 (planner/Opus agent). Follow-ups a future pass could pick up: extract SEA-HELM's actual Vietnamese safety score (not done, budgeted out); confirm ML-Bench's 14-language list beyond a negative text search; re-verify Vietnam's AI Law/Digital Technology Industry Law against primary text (two attempts failed — 404 and reliance on a prior pass's finding); re-check MAS's primary guidance page (returned maintenance error both times touched across passes). Phase 2 should start at docs/plan/ per projects/CLAUDE.md's pipeline.

## 2026-09-17 — wave 2a (niche pick + solution list) — phase 2 start
PLAN: read global/projects/project CLAUDE.md, STATE, all 5 docs/explore/*.md, spot-check raw/ behind load-bearing claims, read research layer (markets/ai-attack-defense{,-services}.md, competitors/ai-attack-defense-roster.md, markets/vietnam-sg-access.md, customers/first-customers.md, findings/market-gaps-2026.md, method/scope.md). Then write ONE deliverable `docs/plan/niche-and-solutions.md`: 4-6 narrow niches from the NOTHING/thin rows, ranked solution table per niche, purchase trigger named per candidate (wave 1 found no SEA compliance mandate), the Vietnamese wedge argued both directions plus one settling measurement small enough to be the prototype, the pick + fallback with the case against stated as hard as the case for, and a 2b attack list weighted toward every ABSENCE claim. No tool design (2c), no self-fact-check (2b). No git, no writes outside projects/ai-attack-defense/, no edits to docs/explore/ or raw/.
DID: (in progress)
FILES: (pending)
OPEN: reading done, drafting next.

## 2026-09-17 — wave 2a (niche pick + solution list) — phase 2 complete
DID: Read all 5 docs/explore/*.md, spot-checked raw/language-gap-pulls.md and raw/aisb-module-scan.md behind load-bearing claims, read the research layer (markets/ai-attack-defense{,-services}.md, competitors roster, vietnam-sg-access.md, customers/first-customers.md, findings/market-gaps-2026.md, method/scope.md). Wrote docs/plan/niche-and-solutions.md: 5 narrow niches (N1 checkpoint behavioral integrity 5.1-5.4; N2 serving-endpoint exposure grading 1.1/1.2/1.3/3.5; N3 ATLAS-mapped evidence artifact 7.2; N4 Vietnamese-language guardrail conformance 3.3/1.4; N5 coding-agent affordance audit 2.1), 11 ranked products with build size / defensibility / killer / HCMC-reachability, a per-candidate purchase-trigger table that says "they should care" out loud where that is the truth, the Vietnamese wedge argued both ways with a pre-registered settling measurement, the pick plus fallback plus third with the case against stated as hard as the case for, and a 16-item 2b attack list weighted toward absence claims.
FILES: docs/plan/niche-and-solutions.md (only file written).
OPEN — FOR WAVE 2B (attack these, in order):
  1. ABSENCE: "nothing detects a behaviorally tampered checkpoint" — the fallback dies if one shipping product exists. Attack HiddenLayer platform claims, Protect AI/Palo Alto post-acquisition line, Cranium, Pillar, Neural Cleanse/STRIP productization.
  2. ABSENCE: "no shipping guardrail supports Vietnamese" — wave 1 checked only Llama Guard 3 / NeMo / Lakera. NOT CHECKED and high-risk: Google Perspective API, OpenAI omni-moderation-latest language docs, Azure AI Content Safety, AWS Bedrock Guardrails, Alibaba/SEA providers. This can weaken the primary pick before the prototype runs.
  3. ABSENCE: "nothing audits LLM serving-endpoint config exposure" — lowest-confidence absence in the file; check garak probe list for prefill/logprob/control-token probes.
  4. ABSENCE: ATLAS has no tool layer; Snyk agent-scan v0.6.3 check list never read.
  5. UNSOURCED, HIGHEST VALUE: Vietnam content-control regime applied to a public-facing Vietnamese chatbot. Wave 1 searched privacy and AI law, never content law. If it exists, N4 gains a real compliance trigger and the ranking firms up.
  6. UNSOURCED: the downstream vendor-security-questionnaire chain reaching a Vietnamese supplier — the stated trigger for the primary pick, zero evidence either way.
  7. UNSOURCED: ViHSD label schema + licence; SEA-HELM's actual Vietnamese safety score (if it publishes one, part of the "first number" claim dies).
  8. REASONING: build-size estimates, the 15pp/5pp thresholds, the HCMC-proximity-restores-the-referral-channel argument, and the ML-Bench string-search negative.
OPEN — FOR WAVE 2C (the tool you are designing):
  PRIMARY: product 4.1 — the Vietnamese guardrail benchmark, built so that running it IS the settling measurement. Spec, verbatim from docs/plan/niche-and-solutions.md §4: guardrails under test = Llama Guard 3 8B, OpenAI omni-moderation-latest, Lakera Guard free tier. Dataset = ViHSD (arXiv 2103.10069), stratified subset ~500-1000 items, label schema unknown-not-pulled, confirm before sampling. Paired condition = each item submitted twice, Vietnamese original and English machine translation, back-translate a sample for fidelity and discard items whose meaning did not survive. Metric 1 = recall on human-labeled toxic items, VI vs EN, in percentage points, per guardrail. Metric 2 = paired verdict disagreement rate with direction (VI-pass/EN-flag is the safety-relevant miss). Reporting discipline = the 3-part ASR rule from D:\ai\ai-playground\docs\reference\measurement.md — state evaluator, state k, state binary-vs-averaged; k=1, single-shot, no amplifiers. Decision rule (pre-registered, chosen not derived): >=15pp VI-below-EN gap on >=1 guardrail asymmetric toward VI-misses = wedge confirmed; <5pp on all three = wedge dead, fall back; in between or one-guardrail-only = repoint to a published guardrail picker.
  FALLBACK if 2b kills the Vietnamese wedge: product 1.1 `refusal-diff` — behavioral diff of a checkpoint against its claimed base, pass/fail plus refusal-rate delta per category, ships as pip package + GitHub Action. Technique from AISB 5.1 (efficacy/paraphrase/locality) and 5.3 (diff-in-means refusal direction). Known technical risk: the signal may not separate abliteration from benign helpfulness tuning.
  THIRD, swap fallback to it if 2b confirms 2.1 absence and kills 1.1 absence: product 2.1 endpoint exposure grader.
  BOUNDARY CARRIED FORWARD: product 2.2 (extraction-cost estimator) is dual-use and in scope only against an operator-controlled endpoint with no retention of the recovered projection — 2b decides whether to drop it. Product 1.1 is the defensive half of 5.3; the design must not require shipping the abliteration tool. ai-playground's arena harness, worked solves and offensive corpora stay out of bounds; only its taxonomy and measurement docs are reusable.
