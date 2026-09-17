# Orchestration log

Main-thread record of who was spawned, on what model, for what. Per `MegaPlan.md`: one agent per project at a time. Main thread spawns only — no planning, no review done here.

## Model policy — set by the user 2026-09-17

| Model | Used for |
|---|---|
| Sonnet | Web and network exploration, pulls, small clear execution tasks |
| Opus | Planning, solution design, code review, plan review |

## Wave plan

| Wave | Model | Phase | Per project |
|---|---|---|---|
| 1 | Sonnet | explore | Terrain + measured pulls into `raw/`, inventory files into `docs/explore/` |
| 2 | Opus | idea → review vs market → solution design → daydream | Reads wave 1 output, writes `docs/plan/`, `docs/design/`, `docs/review/` |
| 3 | Sonnet | vibe-code MVP | Builds `prototype/` from wave 2's design, runs it, logs to `docs/execution/` |
| 4 | Opus | outcome review + end-to-end test read | Reviews code and result, writes `docs/outcome/` |

Waves gate on each other per project. A project may run ahead of the others.

## Task sizing — set by the user 2026-09-17

A wave is not one agent per project by default. A stage too big for one agent gets **split into smaller scoped tasks, each with its own agent, spawned in sequence** as the prior one lands. Quality and efficiency beat agent count.

Split rule: one agent per task that has a single deliverable file (or one tight cluster), a single question, and a clear done condition. When a stage's brief lists five unrelated deliverables, that is five tasks, not one.

Carry-forward rule: each successor agent reads `STATE.md` plus the specific files its predecessor wrote, never a chat handoff. `STATE.md` is the only interface between agents.

Wave 1 ran as one broad explore agent per project — acceptable because explore is fan-out reading with one shared output shape. Wave 2 onward is split by deliverable.

## Runs

### Wave 1 — 2026-09-17, three Sonnet explore agents, parallel

| Project | Brief | Status |
|---|---|---|
| `ai-ads-injection` | Carrier state from pass 2, crawler detection surface per engine, edge controls, policy ceiling, GEO vendor landscape. Measure: fetch published crawler IP ranges, rDNS/ASN sample, find what domain/CDN access exists on this machine | spawned |
| `agent-hermes-dashboard` | Settle what Hermes is (never confirmed — `docs/method/scope.md` flags it), agent control planes shipping today, Claude Code unattended-run limits, small-business blind spots, obtainable task telemetry | spawned |
| `ai-attack-defense` | AISB module inventory with a market column (`D:\ai\aisb`), reusable local code, shipping tool landscape at tool level, Vietnamese/SEA language gap evidence, SEA compliance triggers | spawned |

Standing constraints given to all three: write only inside own project folder; never touch root `docs/`; no git; no spending or account creation; STATE.md written before and after each work chunk, not batched at the end; WebSearch quota may still be exhausted from 2026-09-16, prefer direct fetch.

## Git

Initialized 2026-09-17 as a restore point, not a workflow. `1cb8b00` = scaffold. Main thread commits after each wave. Agents never commit.
