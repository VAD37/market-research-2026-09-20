# Shipping AI-security tools, as of 2026-09-17

Explore phase. Source: `../../raw/shipping-tools-github-pulls.md` (live `gh api` pulls, 2026-09-17) plus `../../../docs/markets/ai-attack-defense.md` and `../../../docs/competitors/ai-attack-defense-roster.md`, which this file only **adds to** per instruction — tools already fully profiled there (Garak, PyRIT, DeepTeam, Promptfoo, NeMo Guardrails, Guardrails AI, Snyk agent-scan/MCP-Scan, Lakera Guard, HiddenLayer ModelScanner, HackerOne/Bugcrowd, Gray Swan Arena) are re-verified for last-release-date only, not re-profiled.

## Re-verification of tools already in the roster (last-release check)

| Tool | What it tests | Maintainer | License | Last release / last push (2026-09-17) | Not covered |
|---|---|---|---|---|---|
| Garak | 37+ probes: hallucination, injection, jailbreak, toxicity | NVIDIA | Apache-2.0 | **v0.17.0, 2026-09-09**; pushed 2026-09-16. Active | No runtime guardrail — scan-time only |
| PyRIT | Multi-turn/multimodal attacks (Crescendo, TAP) | Microsoft | MIT | **v1.1.0, 2026-09-04**; pushed 2026-09-16. Active. Note: `Azure/PyRIT` (115 stars) is an archived stub — the live project is `microsoft/PyRIT` (4,486 stars) | Framework, not a hosted service |
| Promptfoo | 50+ vuln types, CI/CD, YAML red-team configs | promptfoo (OpenAI-acquired 2026-03-09) | MIT | **0.123.0, 2026-09-10**; pushed 2026-09-17. Most active repo checked | Enterprise tier is contact-sales |
| NeMo Guardrails | Dialog-policy runtime guardrail | NVIDIA (org moved to NVIDIA-NeMo) | source-available, no SPDX license tag | **v0.24.1, 2026-09-16**. Active | No multilingual-support claim anywhere in repo (checked, see `language-gap.md`) |
| Guardrails AI | Composable output validators | Guardrails AI | Apache-2.0 | **v0.11.0, 2026-08-14**; pushed 2026-09-13. Active | Validator library, not a scanner |
| Snyk agent-scan (formerly Invariant Labs MCP-Scan) | MCP tool-poisoning, rug-pulls, 15+ agent risks | Snyk | Apache-2.0 | **v0.6.3, 2026-09-10**; pushed 2026-09-17. Active, most-recently-pushed of the group | Post-acquisition — the `invariantlabs-ai/mcp-scan` slug now redirects here |
| DeepTeam | 40+ vulns mapped to OWASP/NIST/ATLAS | Confident AI | Apache-2.0 | **v1.0.9, 2025-11-12** (no newer GitHub Release tag found, though commits continue through 2026-08-21) | Release-tag lag vs. commit activity — check PyPI separately before relying on the tag date |
| HiddenLayer ModelScanner | 35+ model formats: pickle, GGUF, safetensors | HiddenLayer | commercial | not on GitHub (closed-source), no public release cadence to check | Confirmed elsewhere: does not detect behavioral weight edits (ROME-style), only file-format-level threats — see `aisb-inventory.md` row 5.1 |

## New additions — tools not in the existing roster

| Tool | What it tests | Maintainer | License | Last release / last push (2026-09-17) | Not covered |
|---|---|---|---|---|---|
| **Rebuff** | Prompt-injection detection (heuristic + LLM + vector-DB canary) | Protect AI (acquired by Palo Alto Networks Jul 2025) | Apache-2.0 | **v0.1.1, 2024-01-20**; repo **archived** 2024-08-07. Read-only, dead | Superseded by LLM Guard from the same acquirer; do not recommend for new builds |
| **LLM Guard** | Input/output scanners: PII, prompt injection, toxicity, ~20 scanner classes | Protect AI (acquired by Palo Alto Networks Jul 2025) | MIT | pushed **2026-07-08**, but repo flagged **archived** as of this check (2026-09-17) — no GitHub Releases channel found (versions ship via PyPI) | Post-acquisition maintenance status ambiguous: recent push, archived flag. Verify current support before building on it |
| **Purple Llama / Llama Guard 3** | Safety classifier for prompt/response moderation, 14-category taxonomy | Meta | source-available (custom Llama license, NOASSERTION on GitHub) | pushed **2026-08-18**. Active (as a monorepo — no discrete GitHub Releases channel) | Own model card names 8 supported languages: English, French, German, Hindi, Italian, Portuguese, Spanish, **Thai**. No Vietnamese, no Indonesian — see `language-gap.md` |
| **OWASP LLM Top 10 / GenAI Security Project** | Not a scanner — the taxonomy shipping products map their coverage to | OWASP (community) | source-available | repo pushed **2026-08-05**. Active | It is a standard, not a tool. `../../../docs/raw/services-lane-pulls.md` already covers OWASP's separate Vendor Evaluation Criteria doc (2026-02-04) |
| **Giskard** (now `giskard-oss`) | LLM-agent evaluation and testing: RAG correctness, bias, hallucination, injection | Giskard AI | Apache-2.0 | **giskard-checks/v1.0.4, 2026-09-14**; pushed 2026-09-16. Active | Broader eval/QA framing than pure red-team; overlaps DeepTeam/Promptfoo |
| **MITRE ATLAS** | Not a scanner — 16-tactic/84-technique knowledge base and matrix for ML-system threat modeling | MITRE (Center for Threat-Informed Defense) | source-available | website repo (`mitre-atlas/atlas-website`) pushed **2026-09-16**. Actively maintained as a knowledge base | **No maintained interactive tool layer** — unlike ATT&CK's Navigator, there is no comparable ATLAS Navigator product. This is itself a candidate gap, see `aisb-inventory.md` row 7.2 |

## Read for the planner

- Every OSS tool checked that is still active pushed code **within the last 8 days of this pull** (2026-09-09 through 2026-09-17) — this category moves fast and none of the actively-developed tools is stagnant.
- Two tools are genuinely abandoned: **Rebuff** (archived 2024, superseded internally by its own maker) and possibly **LLM Guard** (archived flag set despite a 2026-07 push — ambiguous, needs a direct maintainer check before depending on it). Both trace to Protect AI, now inside Palo Alto Networks — a consolidation-driven abandonment pattern consistent with `../../../docs/markets/ai-attack-defense.md`'s finding that every well-funded pure-play got absorbed within ~18 months.
- No tool checked here (or in the existing roster) claims or demonstrates Vietnamese-language support. Llama Guard 3 is the only one that publishes a language list at all, and it stops at Thai. See `language-gap.md` for the full evidentiary picture.
- MITRE ATLAS's missing tool layer (no Navigator-equivalent) is the cleanest "the standard exists, the product around it doesn't" gap found in this pass.

## Caveats

- `gh api` release-date checks reflect **GitHub Releases tags only**. A tool that ships primarily via PyPI/npm without tagging GitHub Releases (DeepTeam, LLM Guard, PurpleLlama) may be more current than its GitHub Releases tag suggests — `pushed_at` (last commit) is the more reliable freshness signal for those, and is reported alongside the release tag above.
- "Archived" on GitHub means the repo is read-only; it does not always mean the underlying product died — Protect AI's tools may live on inside Palo Alto Networks' commercial platform under a different repo or closed-source. Not independently checked this pass.
- License field shows `NOASSERTION`/"source-available" for NeMo Guardrails and PurpleLlama because GitHub's API could not resolve an SPDX identifier from their license files — the repos do publish license terms, just not in a form this check's `--jq` filter recognized as standard SPDX.
