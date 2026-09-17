# Local reusable-asset scan — raw

Pull date: 2026-09-17. Method: `ls`/directory listing + `cat` of `CLAUDE.md`/`README.md` entry points in each named directory. Skim only, per brief ("scan, do not deep-read").

## D:\ai\security

`CLAUDE.md` verbatim opening: "Interview-prep knowledge base + hands-on lab space for an **Application Red Team engineer** role at **Coinhako** — a MAS-regulated, custodial crypto exchange in Singapore." Focus: app-layer offense (web/API), secure code review, threat modeling + dev collaboration, incident response. Explicitly **not** AI-security content — it is Web3/crypto-exchange interview prep for the repo owner. Structure: `docs/tracks/01..10-*.md` (10 learning tracks), `docs/reference/` (interview cram, tech-stack reference), `labs/` (mostly empty, built on demand).

Relevance: none directly (no AI-security code or tooling). Indirectly: confirms owner's professional background is Web3/crypto AppSec + red-team, not AI safety research — relevant to credibility framing for a services offering, not to prototype code reuse.

## D:\ai\growtrics-llm-engine

`CLAUDE.md` verbatim: "You are an agent that produces STEM explainer animation, and you are an expert in Manim." Chemistry/physics animation generator (Manim Python). No AI-security content. Not reusable.

## D:\ai\ai-playground — the strongest reuse candidate

`CLAUDE.md` verbatim: "A personal **AI red-team / jailbreak practice hub** and reference library... Content grows over time... The active goal is leaderboard placement on the Cinderela Arena wave... using a fingerprint -> cheapest-effective-attack -> log loop. All work here targets **deliberately-vulnerable challenge models under authorized CTF rules** — none of it is aimed at production systems."

Directory contract (`docs/` / `play/` / `vendor/`):

- `docs/attacks/` — 10-file attack-family catalog: `01-reframe.md 02-inject.md 03-indirect.md 04-obfuscation.md 05-leak.md 06-exfil.md 07-tools.md 08-mcp.md 09-multimodal.md 10-model-level.md`.
- `docs/defenses/` — `input-guards.md`, `output-guards.md`, `intrinsic-and-agentic.md`.
- `docs/reference/guard-taxonomy.md` — the **L0-L4 offense ladder <-> A-F defense-stack crossmap**: L0 prompt-only, L1 input filter, L2 output filter, L3 second-model judge, L4 exact-match canary. Maps each rung to which attack family beats it and which vendor mechanism (A intrinsic alignment, B decode-time, C input guard, D output guard, E agentic, F governance) it corresponds to.
- `docs/reference/measurement.md` — ASR (attack success rate) methodology: "ASR is meaningless without an attempt budget" — logs amplifiers (Best-of-N, PAIR, TAP, many-shot, Crescendo) with cited frontier ASR numbers and papers (arxiv-2412.03556, arxiv-2310.08419, arxiv-2312.02119, etc.), a live-frontier-vs-regression-only triage table, and a 3-part ASR reporting discipline (evaluator, k, binary-vs-averaged definition).
- `play/README.md` — describes the `promptfoo` harness (run locally from `play/`) used for templating + ASR measurement, explicit "harness generates payloads and measures — it does not auto-submit" rule, and a Gray Swan Arena recon pipeline (`cinderela/`) with committed `.mjs` scripts and a documented reverse-engineered HTTP API (`cinderela/grayswan/API.md`).
- `vendor/` — **~35 vendored/forked upstream projects**, including exactly the tools this project's `shipping-tools.md` catalogs: `garak`, `PyRIT`, `promptfoo`, `giskard`, `deepeval`, `counterfit`, `FuzzyAI`, `BrokenHill`, `llm-attacks`, `TaskTracker`, `vulnerable-mcp-servers-lab`, `adversarial-robustness-toolbox` (IBM ART), `atlas-data`, `arc_pi_taxonomy`, plus offensive corpora (`L1B3RT4S`, `leaked-system-prompts`, `hackaprompt-dataset`, `UniversalJailbreakDB20XX`, `Pliny_HackAPrompt_Dataset`, `payloads`, `system_prompts_leaks`, `awesome-chatgpt-prompts`, `MisguidedAttention`, `Spiritual-Spell-Red-Teaming`, `Thought-Forgery`, `deck-of-many-prompts`).

Boundary note (load-bearing for this project): the arena-facing parts of this repo (`cinderela/`, `play/solves/`, the offensive corpora in `vendor/`) target a named third party (Gray Swan Arena, `app.grayswan.ai`) and are themselves jailbreak/evasion work product. This project's hard boundary ("no third-party targeting, no evasion tooling") means the arena-harness code and the offensive payload corpora are **not** directly extendable here. What IS reusable without crossing that line: the **taxonomy** (`docs/attacks/`, `docs/defenses/`, `guard-taxonomy.md`) and the **measurement methodology** (`measurement.md`'s ASR/attempt-budget discipline) — both are defensive/analytical documents describing attack classes and how to measure guardrail robustness, not payloads themselves. The vendored OSS libraries (garak, PyRIT, promptfoo, giskard, deepeval, ART) are themselves defensive-purpose testing tools already mirrored locally.

## D:\projects\lv1-auditor

Smart-contract security audit training material. `topics/` (Audit Process, Category, cheatsheet, Solidity), `vulnerabilities/` (~30+ individual vuln-pattern notes: `ERC20 approve(0) first...`, `CREATE2 reinitialize`, `ECDSA replay crosschain`, etc.), `guides/` (address generation, keccak storage, lessons learned). Web3/Solidity-specific, not AI-security. Relevance: none to AI-attack-defense prototype code. Possible indirect relevance: the note-per-vulnerability-pattern format is a reusable *documentation shape* for a future AI-vuln-pattern catalog, not code.

## D:\projects\lv1-wizard

`CLAUDE.md` verbatim: "An Obsidian vault, not a software project. Markdown is the product." Personal knowledge vault with journal/library/character folders and `.agents/` governance docs. Not AI-security tooling. Not reusable.

## D:\projects\smart-contract

`archive`, `comet-helper`, `playground-viem-2025`, `sui-hello`, `template`, `uni-qswap` — Web3 dev/audit playground repos (Solidity/Move/Sui). Not AI-security. Not reusable.

## D:\projects\audit-history

`README.md` verbatim: "VAD37 Security Research & Audit Portfolio — A curated archive of smart contract security research, audits, and CTFs writeup conducted by @VAD37." `audits/` holds ~20+ dated public smart-contract audit engagements (2022-2023 vintage: velodrome, notional, jojo, rubicon, chainlink, dodo, USSD, venus, maia, arcade, ajna, centrifuge, Gitcoin, etc.), each preserved as a repo snapshot. `ctf/` holds CTF writeups.

Relevance: confirms the repo owner (VAD37) has a real, dated professional track record as a Web3 security auditor with public deliverables — this is evidence for the "credibility for enterprise procurement" and "compliance-report paperwork" moats named in `../../../docs/markets/ai-attack-defense.md` (an operator who already knows how to write an audit report an engagement accepts), but it is a portfolio, not reusable code or an AI-security asset.

## D:\audits

Active/recent smart-contract audit engagements (2025-11 through 2026-07: sukukfi, swafe, panoptic, rujira, fluid-dex-v2, currentsui, metric) plus reference material (`_reference`, `cw-plus`, `soroban-examples`, `stellar`, `stellar-core`, `unstoppable`, `aave-v4`, `Ethereal`, `cre-templates`). Confirms VAD37 is a currently-active, professionally engaged smart-contract auditor as of 2026-07. Not AI-security code. Sample audit folder (`2026-01-fluid-dex-v2-VAD37`) contains only `fluid-contracts/` (the audited codebase) and a `README.md` — report format itself was not deep-read (out of scope, would require opening client deliverables).

## D:\hackathon

`greyctf-2026`, `greyctf26-challs-public` (CTF challenges, general infra/crypto, not AI-specific per directory names), `p2p-rwa` (real-world-asset tokenization hackathon project, Solidity/workflow scripts), `TeamPandaBear`. Not AI-security. Not reusable for this project.

## Summary read

Only one directory is a genuine reuse asset for an AI-attack-defense prototype: **`D:\ai\ai-playground`**, specifically its `docs/attacks/`, `docs/defenses/`, `docs/reference/guard-taxonomy.md`, `docs/reference/measurement.md`, and its vendored copies of `garak`, `PyRIT`, `promptfoo`, `giskard`, `deepeval`, `ART`. Everything else on this machine is either non-AI (Web3/Solidity audit work, Manim animation, an Obsidian vault) or AI-security material that is itself AISB (already excluded from re-reading) or Web3-interview prep with no AI content.
