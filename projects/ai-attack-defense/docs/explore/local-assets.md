# Local reusable assets

Explore phase, 2026-09-17. Source: `../../raw/local-assets-scan.md`. Scope: what already exists on this machine that a prototype could reuse — code, harnesses, datasets, eval rigs, prior audit tooling. Nine directories scanned per brief; one is a genuine asset.

## The asset: `D:\ai\ai-playground`

| Path | What it does | Language | State |
|---|---|---|---|
| `docs/attacks/01..10-*.md` | Attack-family catalog (reframe, inject, indirect, obfuscation, leak, exfil, tools, MCP, multimodal, model-level) | Markdown | Working, actively maintained by repo owner |
| `docs/defenses/{input-guards,output-guards,intrinsic-and-agentic}.md` | Defense-mechanism catalog matching the attack families | Markdown | Working |
| `docs/reference/guard-taxonomy.md` | L0-L4 offense ladder <-> A-F defense-stack crossmap; which attack family beats which guard layer | Markdown | Working, cites primary papers per rung |
| `docs/reference/measurement.md` | ASR/attempt-budget measurement discipline: amplifiers (Best-of-N, PAIR, TAP, Crescendo) with cited frontier ASR numbers, 3-part ASR reporting rule (evaluator/k/binary-vs-averaged), live-frontier-vs-regression-only triage table | Markdown | Working, dated 2026-06-11 source report |
| `play/` (promptfoo harness) | Local `promptfoo` install for templating + ASR measurement, manual-chat + one-account discipline, no auto-submit | promptfoo YAML/JS | Working, used against Gray Swan Arena |
| `vendor/garak`, `vendor/PyRIT`, `vendor/promptfoo`, `vendor/giskard`, `vendor/deepeval`, `vendor/adversarial-robustness-toolbox` (IBM ART), `vendor/counterfit`, `vendor/FuzzyAI`, `vendor/BrokenHill`, `vendor/llm-attacks`, `vendor/TaskTracker`, `vendor/vulnerable-mcp-servers-lab`, `vendor/atlas-data`, `vendor/arc_pi_taxonomy` | Local mirrors/forks of the exact OSS tools named in `../../../docs/markets/ai-attack-defense.md`'s tool table, plus several not yet in that table (ART, Counterfit, FuzzyAI, BrokenHill, TaskTracker) | Mixed (Python/JS/Go) | Vendored, not hand-modified per repo convention ("Never hand-edit submodule contents") |
| `vendor/{L1B3RT4S,leaked-system-prompts,hackaprompt-dataset,UniversalJailbreakDB20XX,Pliny_HackAPrompt_Dataset,payloads,system_prompts_leaks}` | Offensive jailbreak/payload corpora | Text/JSON | Working, but offensive — see boundary note below |
| `play/cinderela/`, `play/solves/` | Gray Swan Arena (`app.grayswan.ai`) recon harness + worked jailbreak solutions, incl. a reverse-engineered HTTP API doc (`cinderela/grayswan/API.md`) | Node.js (`.mjs`) + Markdown | Working, actively used |

**Boundary note, load-bearing.** The arena harness (`cinderela/`), the worked solves (`play/solves/`), and the offensive corpora in `vendor/` target a named third party (Gray Swan Arena) and are themselves jailbreak/evasion work product. This project's hard boundary — "no third-party targeting, no evasion tooling built for misuse" — means those parts are **not** extendable here. What crosses the line cleanly into reusable: the taxonomy documents (`docs/attacks/`, `docs/defenses/`, `guard-taxonomy.md`, `measurement.md`) and the vendored defensive-purpose OSS libraries (garak, PyRIT, promptfoo, giskard, deepeval, ART, Counterfit) — these are analytical/methodological references and already-public tools, not payloads aimed at anyone's production system.

**Direct relevance to the AISB gaps.** `guard-taxonomy.md`'s L0-L4 ladder is functionally the same threat model as AISB `3.3-guardrails`; `measurement.md`'s ASR/attempt-budget discipline is exactly the rigor a prototype red-team or guardrail-regression tool would need to report results honestly. A prototype in the guardrail-testing space does not need to build this methodology from scratch — it exists locally, dated and cited.

## Everything else scanned: not reusable for this project

| Path | What it is | Why it doesn't apply |
|---|---|---|
| `D:\ai\security` | Web3/crypto-exchange AppSec interview-prep vault for the repo owner (Coinhako role prep) | No AI-security content — confirms owner's professional background (Web3 AppSec + red-team), not code to reuse |
| `D:\ai\growtrics-llm-engine` | Manim-based STEM animation generator | Unrelated domain (chemistry/physics explainer video) |
| `D:\projects\lv1-auditor` | Solidity/smart-contract vulnerability-pattern notes (~30+ files) | Web3-specific; the per-vulnerability-note *format* is a reusable documentation shape, not code |
| `D:\projects\lv1-wizard` | Personal Obsidian vault (journal, library) | Not a software project |
| `D:\projects\smart-contract` | Solidity/Move/Sui dev playgrounds | Web3-specific, no AI-security overlap |
| `D:\projects\audit-history` | VAD37's public smart-contract audit + CTF portfolio (~20+ dated engagements, 2022-2023) | Confirms the owner's real, dated professional audit-report track record (relevant to the "compliance-report paperwork" and "enterprise-procurement credibility" moats named in `../../../docs/markets/ai-attack-defense.md`) but contributes no code |
| `D:\audits` | VAD37's active 2025-2026 smart-contract audit engagements | Same read as above — active professional credibility, not AI-security code |
| `D:\hackathon` | CTF challenges (greyctf 2026) and a RWA-tokenization hackathon project | Not AI-security |

## Read for the planner

- The one asset worth building on is methodological (taxonomy + measurement discipline), not a runnable product. A prototype still has to be built; what exists locally shortens the "how do we measure this credibly" step, not the "what do we ship" step.
- The repo owner's demonstrated track record is Web3/smart-contract security auditing (dated, public, ongoing) plus personal AI red-team/jailbreak practice (Gray Swan Arena). Neither is AI-defense product engineering — the planner should weigh this against any solution requiring deep ML engineering (e.g., training a custom guardrail classifier) versus one that primarily orchestrates existing OSS scanners and writes the report (which matches both the owner's audit-report experience and the vendored tool inventory).

## Caveats

- Skim-level scan only, per brief. `D:\ai\ai-playground`'s `docs/models/`, `docs/papers/`, `docs/research/` subfolders and the full `vendor/` tree (35 projects) were listed by name, not individually opened — some may hold further reusable reference material not captured here.
- Sample audit report format in `D:\audits\2026-01-fluid-dex-v2-VAD37` was not opened (client deliverable, out of scope for this scan).
