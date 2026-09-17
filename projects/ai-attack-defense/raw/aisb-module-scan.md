# AISB module scan — raw

Source: `D:\ai\aisb` (local filesystem, read-only per project boundary). Pull date: 2026-09-17. Method: `ls` directory listing of repo root and all 26 module folders, `cat` of `CLAUDE.md`, `AGENTS.md`, top-level `README.md`, and every module `README.md`. Solution/instruction `.py`/`.md` files were NOT deep-read (budgeted per brief) — the README table is the curriculum's own stated contract (per `D:\ai\aisb\CLAUDE.md`: "Every instructional folder has a README.md that records its curriculum contract").

## Repo root listing

```
1.0-readings  1.1-llm-internals  1.2-logprobs  1.3-instruction-hierarchies  1.4-prompt-injection
2.1-coding-agents  2.2-monitoring  2.3-control-protocols  2.4-safety-simulator
3.1-tokenization  3.2-jailbreaking  3.3-guardrails  3.4-knowledge-distillation  3.5-weight-extraction
5.1-model-editing  5.2-backdooring  5.3-undoing-safety-finetuning  5.4-safety-finetuning
6.1-adversarial-vision  6.2-adversarial-language  6.3-prefix-tuning  6.4-watermarking
7.1-rand-report  7.2-threat-modeling  7.3-nvidia-container-toolkit  7.4-gpu-rowhammer
AGENTS.md  aisb_utils  build-instructions.sh  CLAUDE.md  CONTENT_MIGRATION_MAP.md
day0-setup  LICENSE  PREREQUISITES.md  README.md  requirements.txt  requirements-control-arena.txt
requirements-vllm.txt
```

## Per-module directory contents (ls, verbatim file lists)

Every numbered module has the same shape: `README.md`, `sectionN_instructions.md` (generated, participant-facing), `sectionN_solution.py` (source of truth, instructor-only per build system), `sectionN_test.py` (generated). Deviations noted:

- `2.2-monitoring`: adds `conftest.py`, `day2_utils`, `prompts`, `reference_solutions`.
- `2.3-control-protocols`, `3.3-guardrails`: add `conftest.py`.
- `3.3-guardrails`: adds `day3_setup.py`.
- `3.1-tokenization`: adds `setup/`.
- `7.1-rand-report`: adds `optional-iaps-sl5-discussion.md`, `SL5_NOVEL-RECOMMENDATIONS.pdf` (RAND).
- `7.3-nvidia-container-toolkit`: adds `module1/` (lab host material).
- `7.4-gpu-rowhammer`: adds `gpubreach_sim/`, `smoke_test.py`.
- `1.0-readings`: prose only — `llm-training-guide.md`, no exercise files.

## Build system (from `D:\ai\aisb\CLAUDE.md` and `aisb_utils/`)

`*_solution.py` is the single source of truth. `./build-instructions.sh` parses it into `*_instructions.md` (participant-facing, solutions replaced with TODO scaffolds) and `*_test.py` (extracted `test_*` functions). `aisb_utils/` holds `build_instructions.py`, `solution_parsing.py` (libcst-based parser), `test_utils.py` (the `@report` decorator participants import), `env.py` (loads `.env` for OpenRouter API keys — all bootcamp API exercises route through OpenRouter, not direct vendor keys).

## Top-level README curriculum map (verbatim day structure)

```
Day 1 — LLM Internals: What Goes In, What Comes Out
Day 2 — Coding Agents & AI Control
Day 3 — LLM Inference Security
Day 4 — AISF Day (no scheduled content)
Day 5 — Training & Data Security
Day 6 — Adversarial ML
Day 7 — Infrastructure Security & Threat Modeling
```

Audience per `CLAUDE.md`: "experienced cybersecurity experts who need upskilling in the AI-relevant topics." 1-week bootcamp, 1hr lecture + 6hr labs/day, pair programming.

## Per-module README extracts (What to expect + prerequisite/outcome table), verbatim

See full text captured in agent working notes; condensed into `docs/explore/aisb-inventory.md`. Full original READMEs remain at their source paths under `D:\ai\aisb\<module>\README.md` — not reproduced in full here a second time since they are unmodified upstream files (read-only source, not a compiled claim). Per-module one-line "what learner builds by hand" pulled from each README's Engineering/ML "Main learnings going out" column:

- 1.1: build an OpenAI-compatible request + inspect tokenizer chat template
- 1.2: request/parse token-level logprobs, top-k handling
- 1.3: construct/vary an assistant prefill
- 1.4: operate a small RAG app, poison its knowledge base, run a controlled indirect-injection attack
- 2.1: affordance -> exploit -> impact -> mitigation map for a coding agent
- 2.2: build a monitor that flags suspicious agent actions; ROC/AUC evaluation harness (ControlArena)
- 2.3: implement trusted-monitoring / defer-to-trusted / resampling control protocols
- 2.4: Monte Carlo simulator translating monitor AUC into system-level safety
- 3.1: local tokenizer/model harness, template inspection, generation-prompt control
- 3.2: bounded jailbreak log (prompts, model/config, outcomes)
- 3.3: generation wrapper + classifier pipeline + activation-probe pipeline; attack each layer
- 3.4: supervised + temperature-scaled knowledge-distillation training loop
- 3.5: black-box SVD weight-extraction harness (query matrix -> singular values -> projection)
- 5.1: ROME-style model-editing harness, efficacy/paraphrase/locality measurement
- 5.2: poisoned-dataset construction + fine-tune + trigger-specificity eval
- 5.3: refusal-direction extraction (diff-in-means) + weight orthogonalization ("abliteration")
- 5.4 (optional): LoRA adapter training/eval for safety removal
- 6.1: PGD/FGSM-style constrained adversarial image optimization
- 6.2: GCG greedy-coordinate discrete token-search jailbreak optimizer
- 6.3: continuous embedding-space adversarial prefix optimization
- 6.4 (optional): keyed image watermark embed + blind detector + robustness test suite
- 7.1: RAND OC/SL adversary-capability classification exercise (prose)
- 7.2: MITRE ATLAS kill-chain trace + frontier-lab adversary matrix (prose/table)
- 7.3: reproduce CVE-2025-23266 (NVIDIA Container Toolkit `LD_PRELOAD` escape) in a disposable lab
- 7.4: composite GPU RowHammer -> page-table corruption -> DMA overflow simulator

## Caveats

- Solution/instruction files (the actual exercise code) were not opened; the README curriculum-contract table was treated as authoritative per the repo's own stated convention. If a module's README undersells what participants build, this scan would miss it — recorded risk, not fixed.
- `day0-setup`, `CONTENT_MIGRATION_MAP.md`, `PREREQUISITES.md` were listed but not read — orientation/setup material, not curriculum content.
