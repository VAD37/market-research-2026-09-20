# Hermes substrate — settled

Confirmed 2026-09-17 against primary source. Evidence: `../../raw/hermes-agent-github-2026-09-17.md` (fresh pull, today) and `../../../docs/raw/agent-dashboard-pulls.md` (pass-1 pull, 2026-09-16 — already did most of this work; this file re-confirms and adds the directory layout `MegaPlan.md` §2 asks for).

## The answer

**Hermes = `NousResearch/hermes-agent`, a FRAMEWORK (self-hosted agent runtime), not the model line.** `docs/method/scope.md`'s description — "the open-weight agent model line assumed as the substrate" — is factually wrong about which Hermes; the repo the user means to clone the structure from is the agent runtime, and it is explicitly model-agnostic.

| Fact | Value | Source |
|---|---|---|
| Repo | github.com/NousResearch/hermes-agent | GitHub API, pulled 2026-09-17 |
| License | MIT, no extra clauses. Copyright (c) 2025 Nous Research | LICENSE raw file, pulled 2026-09-17 |
| Created | 2025-07-22 | GitHub API |
| Last push | 2026-09-17T07:03:28Z (active same day as this pull) | GitHub API |
| Latest tagged release | v0.21.3, tag `v2026.9.14`, published 2026-09-14T16:04:14Z | GitHub API, releases/latest |
| Release cadence | Every 3-7 days (5 releases in 18 days, Aug 27 - Sep 14 2026) | GitHub API, releases list |
| Stars / forks / open issues | 246,296 / 51,513 / 43,690 (2026-09-17) vs 246,092 / 51,404 / 43,490 (2026-09-16, pass-1) | GitHub API, both dates |
| Primary language | Python (frontend under `web/` and `website/` also present, not language-tagged by GitHub's top field) | GitHub API |
| Homepage / docs | hermes-agent.nousresearch.com, /docs/ | README, GitHub API |
| MODEL or FRAMEWORK | **FRAMEWORK.** "Use any model you want — Nous Portal, OpenRouter, OpenAI, your own endpoint... Switch with `hermes model` — no code changes, no lock-in." | README.md, verbatim, pulled 2026-09-17 |

## Disambiguation table (candidates, ranked)

| Rank | Candidate | What | Verdict |
|---|---|---|---|
| 1 | **NousResearch/hermes-agent** | Self-hosted, MIT, model-agnostic agent runtime: TUI, multi-platform gateway (Telegram/Discord/Slack/WhatsApp/Signal/CLI), built-in cron, subagent delegation, memory (SQLite + FTS5), skill self-authoring, MCP, ACP adapter, 7 sandboxed execution backends, web dashboard | **The match.** Confirmed by both passes, both dates. Matches "control plane" framing in `scope.md` and the "structure layout" `MegaPlan.md` asks to clone |
| 2 | Hermes model line (Hermes 3, Hermes 4) | Open-weight LLMs from the same org, Nous Research. Hermes 4: Aug 2025, 14B (Apache-2.0, Qwen3-14B base) / 70B / 405B (Llama-3 license). 131K context, hybrid reasoning, Hermes tool-calling format | A model you could point the runtime at — one of several interchangeable backends per hermes-agent's own README ("Use any model you want ... OpenRouter"). Not itself a thing to clone a repo structure from |
| 3 | Any other agent framework named "Hermes" | Searched: no independent open-source "Hermes" agent framework outside Nous Research found in this pass or pass-1 | Ruled out |
| 4 | Local clone on this machine | Searched `D:\ai`, `D:\projects`, `D:\researchs`, home dir (`~`) for `*hermes*` | **None found.** Only hit: `D:\hackathon\TeamPandaBear\server\hermes_bridge` — a 3-file Python ZeroMQ-style bridge script (bridge.py, requirements.txt, a systemd unit file), unrelated to Nous Research, no reference to Nous, agents, or LLMs in its filenames. Not a candidate |

**No local copy exists.** The user has not yet cloned `NousResearch/hermes-agent` onto this machine. `MegaPlan.md` §2's "clone technical from hermes and same structure layout" is an instruction for a future step (design or prototype phase), not something already done — flag this for the design agent so it doesn't assume a local reference copy exists.

## Directory layout (from GitHub API root listing, 2026-09-17 — no local clone to inspect, so this is the closest available)

```
agent/              core agent loop
gateway/            multi-platform message routing (Telegram/Discord/Slack/WhatsApp/Signal/CLI)
tui_gateway/         terminal-UI counterpart to gateway/
acp_adapter/         Agent Client Protocol adapter (IDE/editor integration)
providers/           model backends (Nous Portal, OpenRouter, OpenAI, custom endpoint)
hermes_state*.py     ~18 focused modules: schema, WAL, FTS5 search, usage, rewind/repair,
                     portability, telegram, titles, gateway, guard, lockguard, holders,
                     maintenance, compression, dbfile, errors, common — SQLite-backed
                     session/state persistence, split by concern rather than one file
cron/                built-in scheduler (natural-language schedules, "running unattended")
plugins/, plugin-catalog/, optional-mcps/, optional-skills/, skills/
                     extensibility surface — plugins, MCP servers, agent-authored skills
evals/               eval harness
native/              compiled/native components
web/, website/       dashboard frontend + marketing site, both in-repo
contributors/        per-contributor metadata directory (unusual, not further inspected)
docker/, Dockerfile, docker-compose.yml(+.windows), flake.nix, nix/
                     containerized + Nix deployment paths
tests/, tests-js/    Python + JS test suites
AGENTS.md, SOUL.md, COMPAT_MANIFEST.md, CONTRIBUTING.md, SECURITY.md
                     top-level docs (not fetched this pass — AGENTS.md and SOUL.md are
                     candidates worth reading in the design phase: likely the repo's own
                     internal agent-authoring / persona conventions)
```

The concern-split pattern in `hermes_state_*.py` (schema separate from WAL separate from FTS separate from usage tracking) and the `gateway/` + `tui_gateway/` + `acp_adapter/` split (one core, three presentation/integration surfaces) are the two structural patterns most directly reusable for "same structure layout" per `MegaPlan.md` §2.

## What's still open

- `AGENTS.md` and `SOUL.md` bodies not fetched — read them before the design phase claims to mimic Hermes's "structure and layout," since they may state the repo's own authoring conventions directly.
- Pass-1's "Herald" release (Aug 3, 2026, secondary-blog-sourced: "~3,650 commits, ~1,400 PRs, 650+ contributors") does not match any tag name in the primary releases list pulled today (`v2026.8.27` through `v2026.9.14`). Unresolved — likely a marketing codename for an earlier tag, not verified. Treat "Herald" as unconfirmed.
- Exact current contributor count not re-derived (pass-1: 401, 2026-09-16). Confirmed only that it has grown past 1 page.
- Hermes Business/Enterprise tier pricing and launch date: still undisclosed, per pass-1 (`../../../docs/markets/agent-dashboard.md` caveats).

## Caveats

- This file adds no new uncertainty pass-1 didn't already flag; it re-confirms pass-1's resolution with a same-week fresh pull and answers the one thing pass-1 didn't need to answer (local presence, directory layout).
- Root directory listing is file/dir names only — no file contents fetched except LICENSE and the first ~40 lines of README.md. Internal structure within `agent/`, `gateway/`, etc. is unknown until someone actually clones it.
- WebSearch was not used for this file; all facts trace to direct GitHub REST API / raw-file fetches, dated 2026-09-17.
