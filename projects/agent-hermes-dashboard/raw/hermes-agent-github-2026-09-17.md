### Source: GitHub REST API — NousResearch/hermes-agent
- URL: https://api.github.com/repos/NousResearch/hermes-agent
- Pull date: 2026-09-17
- Method: `curl` direct fetch of GitHub REST API (repo metadata, latest release, releases list, root contents listing, LICENSE raw file, README.md raw file). No WebSearch used.

## Repo metadata (`GET /repos/NousResearch/hermes-agent`)

```
full_name: NousResearch/hermes-agent
description: "The agent that grows with you"
html_url: https://github.com/NousResearch/hermes-agent
homepage: https://hermes-agent.nousresearch.com
created_at: 2025-07-22T22:22:28Z
updated_at: 2026-09-17T07:02:28Z
pushed_at: 2026-09-17T07:03:28Z
stargazers_count: 246296
watchers_count: 246296
forks_count: 51513
open_issues_count: 43690
subscribers_count: 958
language: Python
default_branch: main
license: {key: mit, name: "MIT License", spdx_id: MIT}
```

Compare to pass-1 figure (`../../docs/competitors/agent-dashboard-roster.md`, pulled 2026-09-16): 246,092 stars / 51,404 forks / 43,490 open issues / 401 contributors. Three days later: 246,296 stars (+204), 51,513 forks (+109), 43,690 open issues (+200). Contributor count not re-pulled (see below — pagination-only method, expensive to re-derive exactly; growth direction only).

## Latest release (`GET /repos/.../releases/latest`)

```
tag_name: v2026.9.14
name: "Hermes Agent v0.21.3 (v2026.9.14)"
published_at: 2026-09-14T16:04:14Z
html_url: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.9.14
```

Full release body (verbatim):

> # Hermes Agent v0.21.3 (v2026.9.14)
>
> **Release Date:** September 14, 2026
>
> > Patch release. This tag rolls up the ~338 PRs merged since v0.21.2 into a stable tagged release for downstream consumers (Docker images, Hermes Cloud, hosted deployments). It exists so the remote-gateway sign-in fixes below reach Cloud agents, which auto-update to the newest release tag.
>
> ## What this patch ships for remote Desktop / Cloud users
>
> - **Remote dashboard sessions no longer expire on refresh bursts** (#110061, fixes #55712; salvage #71548 @Doud-FR, #55717 @liuhao1024). Both refresh paths on the gateway (cookie gate and the desktop's native bearer route) now coalesce concurrent requests carrying the same rotating refresh token, so a Desktop wake burst can no longer replay an already-rotated token into the Portal's reuse detection and revoke the whole session. Refresh also runs off the event loop, so a slow identity provider no longer freezes `/api/status`. Pairs with Portal-side NousResearch/hermes-portal#1209 (sliding 30-day idle horizon, 5-minute rotated-token grace).
>
> ## Also requested for this tag
>
> - **Long-lived processes stop leaking duplicate state.db writer handles** (#110934, fixes #100896 #103339; salvage #107974 @kshitijk4poor, mapping @Rroven): gateway, dashboard/Desktop backend, ACP and CLI readers attach read-only and in-process writers share the registry handle, so the `N live SessionDB handles` precursor stops firing on a healthy topology.
>
> ## About this release
>
> Measured at commit `9b419a2d3c2657c192008e732149d61170b32c01`, the window since v0.21.2 contains **1,036 non-merge commits** across **2,642 changed files** (+131,690 / −37,096) and **338 merged PRs**.
>
> Also in the window, undocumented here on purpose: server→client JSON-RPC requests and a Pydantic wire-contract registry with generated TS/OpenRPC for the TUI/Desktop gateway (#110521, #110522); reasoning-effort selection on every model picker, a composer pill and per-auxiliary control in Desktop; OpenRouter OAuth PKCE login; HEIF/HEIC/AVIF image decoding; the Honcho peer-model setup rework; MCP OAuth refresh tokens bound to their issuer; a daily MCP re-auth nudge in Desktop; Wan 3.0, Kling 3.0 / Kling Image v3, MiniMax H3 Max Turbo, Gemini Omni Flash 1.1 and Meta Muse in the FAL catalogs; Slack pasted tables and the Agent Sessions API; multiplexed-profile isolation and gateway-liveness fixes; and the state.db WAL refusal on cross-VM filesystems.
>
> **Full curated release notes for this window ship with v0.22.0**, which will document everything from v0.21.0 onward — highlights, feature areas, and complete contributor credits. Nothing in this window is skipped.
>
> ## Updating
>
> - `hermes update` (git installs), or re-run the installer one-liner.
> - Docker / Hermes Cloud: images build from this tag (`nousresearch/hermes-agent:v2026.9.14`).
>
> **Full changelog:** https://github.com/NousResearch/hermes-agent/compare/v2026.9.11...v2026.9.14

## Recent release cadence (`GET /repos/.../releases?per_page=5`)

```
v2026.9.14  — Hermes Agent v0.21.3 — published 2026-09-14T16:04:14Z
v2026.9.11  — Hermes Agent v0.21.2 — published 2026-09-11T19:20:31Z
v2026.9.7   — Hermes Agent v0.21.1 — published 2026-09-07T22:17:01Z
v2026.8.31  — Hermes Agent v0.21.0 — published 2026-08-31T19:29:49Z
v2026.8.27  — Hermes Agent v0.20.6 — published 2026-08-27T12:06:53Z
```

Release cadence: roughly every 3-7 days as of Aug-Sep 2026. Pass-1's "Herald" release (Aug 3, 2026, "3,650 commits, 1,400 PRs, 650 contributors" — `../../docs/raw/agent-dashboard-pulls.md` line 83, sourced from a secondary blog) does not appear as a tagged GitHub release name in this list; it may be an internal/marketing codename for a release in the v0.19–v0.20 range, not verified against the primary tag list this pull. Flag as unresolved, do not treat "Herald" as authoritative.

## LICENSE (raw file, `main` branch)

```
MIT License

Copyright (c) 2025 Nous Research

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: ...
```
Full MIT text, no additional restriction clauses. Confirms GitHub API `license.key: mit` against the actual file.

## Root directory listing (`GET /repos/.../contents/`, 2026-09-17)

Top-level entries (files and dirs), alphabetical as returned:

```
.coderabbit.yaml   .dockerignore   .env.example   .envrc   .gitattributes
.github/           .gitignore   .hadolint.yaml   .mailmap   .npmrc   .nvmrc
.prettierignore   .prettierrc   .python-version
AGENTS.md   COMPAT_MANIFEST.md   CONTRIBUTING.md (+ .es)   Dockerfile   LICENSE
README.md (+ .es, .ur-pk, .zh-CN)   SECURITY.md (+ .es)   SOUL.md
acp_adapter/   agent/   apps/   assets/   batch_runner.py
cli-config.yaml.example   cli.py   compat_manifest.json   constraints-termux.txt
contributors/   cron/   docker/   docker-compose.yml   docker-compose.windows.yml
eslint.config.shared.mjs   evals/   flake.lock   flake.nix   gateway/
hermes (no ext, likely launcher script)   hermes_bootstrap.py   hermes_cli/
hermes_constants.py   hermes_logging.py   hermes_startup_watchdog.py
hermes_state*.py (18 files — sessions, schema, search, usage, telegram, rewind,
  repair, portability, maintenance, lockguard, holders, guard, gateway,
  fts, errors, dbfile, compression, common, wal, titles, user_copy)
hermes_time.py   locales/   mcp_serve.py   mini_swe_runner.py   model_tools.py
native/   nix/   optional-mcps/   optional-skills/   package.json / package-lock.json
plugin-catalog/   plugins/   providers/   pyproject.toml   registration_lifecycle.py
run_agent.py   scripts/   setup-hermes.sh   setup.py   skills/
tests/   tests-js/   tools/   toolset_distributions.py   toolsets.py
trajectory_compressor.py   tui_gateway/   ui-tui/   utils.py   uv.lock
web/   website/
```

Read from names, not fetched: `agent/` = core agent loop; `gateway/` + `tui_gateway/` = the multi-platform (Telegram/Discord/Slack/WhatsApp/Signal/CLI) message routing layer and its terminal-UI counterpart; `acp_adapter/` = Agent Client Protocol adapter (editor/IDE integration, matches the roster note re: JetBrains/PyCharm ACP); `providers/` = model backends; `hermes_state*.py` = SQLite-backed session/state persistence, split into ~18 focused modules (schema, WAL, FTS full-text search, usage tracking, rewind/repair, portability); `cron/` = the built-in scheduler; `plugins/` + `plugin-catalog/` + `optional-mcps/` + `optional-skills/` + `skills/` = the extensibility surface; `evals/` = eval harness; `native/` = compiled/native components; `web/` + `website/` = dashboard frontend + marketing site source, both in-repo; `contributors/` = per-contributor metadata directory (unusual — not fetched further).

## README.md (raw, `main` branch, first ~40 lines, verbatim excerpt)

> **The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.
>
> Use any model you want — Nous Portal, OpenRouter, OpenAI, your own endpoint, and many others. Switch with `hermes model` — no code changes, no lock-in.

Feature table (verbatim row labels): "A real terminal interface" (TUI, slash commands, streaming tool output); "Lives where you do" (Telegram, Discord, Slack, WhatsApp, Signal, CLI — single gateway process, voice memo transcription, cross-platform conversation continuity); "A closed learning loop" (agent-curated memory, autonomous skill creation, FTS5 session search + LLM summarization, Honcho dialectic user modeling, agentskills.io standard compatible); "Scheduled automations" (built-in cron scheduler, delivery to any platform, natural-language schedules, "running unattended"); "Delegates and parallelizes" (isolated subagents, Python-RPC tool calls); "Runs anywhere" (7 terminal backends: local, Docker, SSH, Singularity, Modal, Daytona, Vercel Sandbox; Daytona/Modal offer hibernate-on-idle serverless persistence); "Research-ready" (batch trajectory generation, trajectory compression for training tool-calling models).

**Model-agnostic, confirmed from primary source**: README explicitly states "Use any model you want" and lists Nous Portal, OpenRouter, OpenAI, and custom endpoints as interchangeable backends switchable with a CLI command. This is a runtime/framework, not a model — it does not bundle or require the Hermes model line (Hermes 3/4).

## Not fetched this pull (bounded effort, flag for a later pass if needed)

- Exact contributor count (pass-1's 401 was current as of 2026-09-16; this pull did not re-paginate the full contributor list, only confirmed the API endpoint still works and returns >1 page at `per_page=1`, i.e. count has grown past 1 — no exact number re-derived).
- `AGENTS.md`, `SOUL.md`, `COMPAT_MANIFEST.md` bodies — named but not fetched. Worth a follow-up if the design phase needs Hermes's own internal agent-authoring conventions.
- v0.22.0 "curated release notes" — not yet published as of pull date (release notes say they ship later, will cover v0.21.0 onward).
