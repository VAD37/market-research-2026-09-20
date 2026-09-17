# Shipping-tools GitHub metadata — raw

Pull date: 2026-09-17. Method: `gh api repos/<org>/<repo>` and `gh api repos/<org>/<repo>/releases/latest` (authenticated GitHub REST API via the `gh` CLI, not WebSearch — quota-safe). Fields extracted via `--jq`. Verbatim JSON fragments below.

## Repo metadata (`archived`, `pushed_at`, `stargazers_count`, `license`, `description`)

```
protectai/rebuff: archived=true, created=2023-04-24, pushed_at=2024-08-07T23:35:48Z, stars=1522, license=Apache-2.0, desc="LLM Prompt Injection Detector"
protectai/llm-guard: archived=true, created=2023-07-27, pushed_at=2026-07-08T23:58:40Z, stars=3207, license=MIT, desc="The Security Toolkit for LLM Interactions"
NVIDIA-NeMo/Guardrails: archived=false, created=2023-04-18, pushed_at=2026-09-17T03:01:13Z, stars=7151, license=NOASSERTION, desc="NeMo Guardrails is an open-source toolkit for easily adding programmable guardrails to LLM-based conversational systems." (repo moved from NVIDIA/NeMo-Guardrails to NVIDIA-NeMo/Guardrails; old slug redirects)
guardrails-ai/guardrails: archived=false, created=2023-01-29, pushed_at=2026-09-13T01:35:49Z, stars=7424, license=Apache-2.0, desc="Adding guardrails to large language models."
meta-llama/PurpleLlama: archived=false, created=2023-12-06, pushed_at=2026-08-18T01:15:09Z, stars=4398, license=NOASSERTION, desc="Set of tools to assess and improve LLM security." (Llama Guard ships inside this repo; meta-llama/llama-guard as standalone repo returns 404 — not a separate repo)
OWASP/www-project-top-10-for-large-language-model-applications: archived=false, created=2023-05-16, pushed_at=2026-08-05T19:19:48Z, stars=1394, license=NOASSERTION, desc="OWASP Top 10 for Large Language Model Apps (Part of the GenAI Security Project)"
Giskard-AI/giskard (canonical name giskard-oss): archived=false, created=2022-03-06, pushed_at=2026-09-16T09:32:30Z, stars=5821, license=Apache-2.0, desc="Open-Source Evaluation & Testing library for LLM Agents"
confident-ai/deepteam: archived=false, created=2025-03-05, pushed_at=2026-08-21T03:45:15Z, stars=2825, license=Apache-2.0, desc="DeepTeam is a framework to red team LLMs and AI agents."
promptfoo/promptfoo: archived=false, created=2023-04-28, pushed_at=2026-09-17T04:02:20Z, stars=25205, license=MIT, desc="Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI..."
NVIDIA/garak: archived=false, created=2023-05-10, pushed_at=2026-09-16T21:54:58Z, stars=9277, license=Apache-2.0, desc="the LLM vulnerability scanner"
Azure/PyRIT (archived stub): archived=true, created=2026-03-25, pushed_at=2026-03-25T01:18:52Z, stars=115 — this is a redirect/renamed-org artifact, NOT the live project.
microsoft/PyRIT (live): archived=false, pushed_at=2026-09-16T23:48:54Z, stars=4486
snyk/agent-scan (formerly invariantlabs-ai/mcp-scan; the mcp-scan slug now redirects here post-acquisition): archived=false, created=2025-04-07, pushed_at=2026-09-17T06:53:05Z, stars=3058, license=Apache-2.0, desc="Security scanner for AI agents, MCP servers and agent skills."
mitre-atlas/atlas-website: archived=false, created=2021-12-30, pushed_at=2026-09-16T04:05:47Z, stars=20 (this is the website source repo, not a scanning tool — ATLAS itself is a knowledge base/matrix, not a shipping scanner)
```

## Latest release tag + date (`gh api repos/<repo>/releases/latest`)

```
protectai/llm-guard: 404 Not Found (no GitHub Releases published — versions ship via PyPI only, not visible via this endpoint)
NVIDIA-NeMo/Guardrails: v0.24.1, published 2026-09-16T17:15:59Z
guardrails-ai/guardrails: v0.11.0, published 2026-08-14T14:22:32Z
meta-llama/PurpleLlama: 404 Not Found (no GitHub Releases; ships as a monorepo, no tagged release channel found via this endpoint)
Giskard-AI/giskard-oss: giskard-checks/v1.0.4, published 2026-09-14T09:49:47Z
confident-ai/deepteam: v1.0.9, published 2025-11-12T14:18:25Z (no newer GitHub Release tag found as of 2026-09-17 despite commits continuing — PyPI may be ahead of GitHub Releases, not independently checked)
promptfoo/promptfoo: 0.123.0, published 2026-09-10T02:34:32Z
NVIDIA/garak: v0.17.0, published 2026-09-09T18:56:03Z
microsoft/PyRIT: v1.1.0, published 2026-09-04T22:19:28Z
protectai/rebuff: v0.1.1, published 2024-01-20T01:11:48Z (last release; repo archived 2024, matches)
snyk/agent-scan: v0.6.3, published 2026-09-10T08:23:04Z
```

## Notes on ambiguous/redirect cases

- `NVIDIA/NeMo-Guardrails` and `NVIDIA-NeMo/Guardrails` return the identical repo object (org rename/transfer) — treated as one project.
- `Azure/PyRIT` (115 stars, archived) vs `microsoft/PyRIT` (4486 stars, active) is the exact discrepancy already flagged and resolved in `../../../docs/markets/ai-attack-defense.md` caveats ("115 was the archived Azure/PyRIT stub"). Confirmed again independently this pull, same conclusion, via direct API rather than search synthesis.
- `invariantlabs-ai/mcp-scan` resolves to `snyk/agent-scan` — confirms the Snyk/Invariant Labs acquisition already recorded in `../../../docs/competitors/ai-attack-defense-roster.md` at the repo level, not just the press-release level.
- `meta-llama/llama-guard` as a standalone repo does not exist (404) — Llama Guard model weights and eval harness live inside `meta-llama/PurpleLlama`, confirmed by the redirect-free 404.
