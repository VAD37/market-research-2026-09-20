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

### Wave 1 results

| Project | Landed | Commit |
|---|---|---|
| `agent-hermes-dashboard` | 2026-09-17. Hermes resolved: `NousResearch/hermes-agent`, MIT, a FRAMEWORK, not the model line. Per-task cost/duration obtainable via Claude Code hooks + OTel under OAuth; recurrence detection and fact-staleness are not — those are the build. Dev-facing tracing lane crowded and consolidating; no SMB-targeted supervision product found. Open fork carried: single-tenant OAuth vs API key for resale | `6ea14a3` |
| `ai-ads-injection` | 2026-09-17. Detection measured per engine: rDNS verification is Google/CommonCrawl-only; OpenAI sampled IPs have zero PTR, Anthropic/Perplexity resolve to generic cloud names. Only Cloudflare Workers can vary a response body. Google cloaking policy directly on point; UCPD Annex I item 11 sharpest ad-disclosure hit. Machine has zero infra — no domain, no CDN account. Five policy docs blocked fetch | `b93c743` |
| `ai-attack-defense` | 2026-09-17. 14 of 26 AISB modules show no shipping product. Top gaps: checkpoint integrity (weight-level tamper detection), API extraction-surface auditing, ATLAS tool layer. Vietnamese gap real but narrower than assumed — Thai has a measured guardrail finding, Vietnamese untested. No SEA regime mandates red-teaming | `eb74e75` |

### Wave 2 — `agent-hermes-dashboard`, split into three chained Opus tasks

| # | Task | Deliverable | Status |
|---|---|---|---|
| 2a | Idea + daydream. Candidate product shapes from wave 1 evidence, the pick, and the attack list for 2b | `docs/plan/idea-set.md` | spawned 2026-09-17 |
| 2b | Adversarial review against market. Attacks 2a's load-bearing claims against the incumbent roster and the research layer | `docs/review/market-check.md` | gated on 2a |
| 2c | Solution design. Task record schema, recurrence detection, graduation to tool, trust boundary in UI, metrics panel. Resolves the OAuth fork | `docs/design/` | gated on 2b |

### Live queue — 2026-09-17

| Project | Task | Model | Deliverable | Status |
|---|---|---|---|---|
| `agent-hermes-dashboard` | 2a idea + daydream | Opus | `docs/plan/idea-set.md` | done `bf49c74`. 8 candidates, pick B (single-job blind-spot agent), fallback H. No candidate has direct demand evidence — stated in file |
| `agent-hermes-dashboard` | 1c gap pulls — does a cheap competitor-price tracker already exist (kills pick B), subscription allowance numbers, Vietnam recurring-USD rail, marketplace volume | Sonnet | `docs/explore/gap-pulls.md` | running |
| `agent-hermes-dashboard` | 2b adversarial market review | Opus | `docs/review/market-check.md` | gated on 1c |
| `ai-ads-injection` | 1b policy gap closer — OpenAI Business Terms, Perplexity API ToS, OpenAI ads terms, Bing/Copilot, Vietnam ad law. Browser-equipped | Sonnet | `docs/explore/policy-ceiling-addendum.md` | running |
| `ai-ads-injection` | 2a idea + daydream, candidates conditioned on the five pending policy docs | Opus | `docs/plan/idea-set.md` | running |
| `ai-attack-defense` | 2a niche pick + ranked solution list, incl. the one measurement that settles the Vietnamese wedge | Opus | `docs/plan/niche-and-solutions.md` | running |
| `ai-attack-defense` | 1b compliance primary-source closer (MAS, Vietnam AI law) — needs browser | Sonnet | `docs/explore/compliance-addendum.md` | queued behind the ads browser task |

Browser is single-resource: only one browser-equipped agent runs at a time to avoid two agents fighting over tabs.

## Git

Initialized 2026-09-17 as a restore point, not a workflow. `1cb8b00` = scaffold. Main thread commits after each wave. Agents never commit.

### Wave 2 results — all three, 2026-09-17

| Project | Pick | Review verdict | Standing |
|---|---|---|---|
| `agent-hermes-dashboard` | B single-job blind-spot agent | Killed on three lines; its own statistic pointed the other way | Stop as scoped. Override rule: ship governor free/MIT, ≥100 stars in 14 days AND ≥3 unprompted paid asks |
| `ai-ads-injection` | C8 research → paid audits | Killed on four lines; verdict borrowed from another idea's column, instrumentation already free | Stop as scoped, after one outreach probe. 20 agencies, 15.000.000 VND, 50% deposit, day 7 |
| `ai-attack-defense` | N4 Vietnamese guardrail benchmark | Falsified on four lines; the paired set already exists, built and switched off | Conditional, three days, zero cash. Portal count + decree + assessment register |

Twenty-seven candidates across three projects. Zero with a named buyer.

### Wave 4 — cross-project synthesis

One Opus agent, authorized to write the repo-root research layer, which project agents were not.

| Deliverable | What it holds |
|---|---|
| `..\docs\method\evidence-rules.md` | Eight rules, each with a worked failure from this session. Absence claims survived ~1 in 5 attacks here |
| `..\docs\findings\pass4-read.md` | The decision page: per project, what was established, what was killed, what continuation costs, and which probes need a human |

## Method note — why three picks died

Three independent re-pick agents diagnosed the same class of failure. Compiled claims traced to a real file but not to the right cell, subject, or definition inside it, and hedges were dropped when one compiled file cited another. Three claims were caught only by measurement or by primary text, never by better searching: the Claude Code hook payload, run live; Điều 10.5.b's grammatical subject, read in Vietnamese; the `cross-read.md` column mix-up, found by opening the table.

Every project resolved its hard mechanism question in one day. Not one resolved who pays. No agent contacted a buyer — every negative on file is a search-level negative, which is the same error class as the method failures above.

## Build phase — user directive 2026-09-17

> "run unattended. run until all MVP have end to end testing and ready to sale to people.
> People can look at hosted website instantly know what this product is about... We need a
> MVP that they can run and test even fake test end to end user as well."

The wave-2 stop verdicts stay on file as evidence and are superseded as instructions.
Mandate written to `MVP-MANDATE.md`; every build-phase agent reads it first.

Model split, per the user: **plan / review / imagine → Opus (or Fable for positioning).
Execution → Sonnet.**

| Wave | Model | Task | Per project |
|---|---|---|---|
| 5 | Opus | MVP spec — the buildable contract | `docs/design/mvp-spec.md` |
| 6 | Sonnet | Build the prototype to spec | `prototype/`, `docs/execution/build-log.md` |
| 7 | Sonnet | End-to-end fake-user test | `docs/execution/e2e-test.md` |
| 8 | Fable | Positioning + sales page | `site/index.html` |
| 9 | Opus | Review: code, test, and page — with screenshots | `docs/outcome/review.md` |
| 10 | Sonnet | Fix what review found, re-test | updated `prototype/`, `site/` |
| 11 | main | Publish each sales page as a hosted artifact | URLs back to the user |

Wave 9 review is vision-based: Playwright MCP, 1440x900 and 390x844, `fullPage`.
Chrome extension re-tested 2026-09-17 and still not connected; Playwright MCP works.

Every review deliverable ends with the section `## Is this enough? What else can we do to
improve it?` — the user's standing requirement.

### Wave 5 — three Opus MVP-spec agents, parallel, 2026-09-17

| Project | Framing given | Status |
|---|---|---|
| `ai-ads-injection` | No domain, no CDN, no spend — so build on the one measured asset: per-engine AI-crawler identification verified against published ranges, not UA strings. Candidate shape: a server-log classifier | spawned |
| `agent-hermes-dashboard` | Hook payload carries no cost and no duration — spec only what is obtainable. The supervision layer is the claim: task ledger, recurrence detection, graduation to a tool | spawned |
| `ai-attack-defense` | Three ungated MIT corpora already on disk. Build on them. No paid endpoint in the demo path; local deterministic baseline, commercial adapter optional | spawned |

Each was sent the measured toolchain mid-run so nothing gets specced that cannot run.
