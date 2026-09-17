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

### Wave 5 results — three Opus MVP specs, 2026-09-17

| Project | Product | Spec | Checklist | Commit |
|---|---|---|---|---|
| `ai-ads-injection` | `aicrawlcheck` — offline access-log classifier | 706 lines | 31 items | `d23d806` |
| `ai-attack-defense` | `parity-vi` — VI/EN guardrail parity harness | 821 lines | 35 items | `587c3ff` |
| `agent-hermes-dashboard` | `foreman` — recurrence-to-tool graduation CLI | 1092 lines | 32 items | `61f08ab` |

Each spec pre-registers an exact deterministic tally as the build's pass condition, and each
build agent is told in writing: if output disagrees with the spec, fix the code, not the
number. A spec number may only be overturned by arithmetic recorded in `build-log.md`.

Each spec agent took first-hand measurements rather than accepting a prior pass:

| Project | Measured this wave | Why it mattered |
|---|---|---|
| `ai-ads-injection` | 489 IPv4 + 148 IPv6 prefixes across 9 files; RFC 5737 ranges overlap zero of them | Fixture can use documentation IPs as guaranteed-negative traffic |
| `ai-attack-defense` | SEA-HELM vi/en row-for-row aligned, 0 mismatches / 600 rows; MultiJail parses to 315 rows not 443 lines; ViHOS counts in the data README wrong on all three files | The whole parity design rests on the alignment. `wc -l` lies on these files |
| `agent-hermes-dashboard` | `~/.claude/history.jsonl` 3000/3000 lines carry exactly `display`/`pastedContents`/`project`/`sessionId`/`timestamp`; `SKILL.md` format observed; no `~/.claude/commands/` exists | Supplies the task text and the `sessionId` join the hook payload lacks. Nothing asserted about slash-command format, which was never observed |

Three honesty positions carried from spec into build, each one refusing a claim the project
would have liked to make:

- ads: nothing may be claimed about GoAccess/AWStats/Matomo — no pass has checked them. An acceptance item greps for it.
- attack-defense: promptfoo is named first and conceded to do most of this. PyRIT language coverage and promptfoo run-diff both recorded `unknown` rather than ranked on an unattacked absence.
- hermes: `/insights` is the nearest free first-party incumbent and its output was never inspected, so only the checkable claim is permitted. Cost fields are excluded rather than estimated.

### Wave 6 — three Sonnet build agents, parallel, 2026-09-17

All three spawned. Each builds to its spec, runs the pre-registered fixture, and must match
the tally exactly. None may write `site/index.html` — wave 8 owns the sales page.

Hermes build carries the session's strictest safety brief: `assert_not_global()` before every
write, a SHA-256 of `~/.claude/settings.json` before and after the run, and a ban on copying
any real string out of `~/.claude/history.jsonl` into the repo.

## Wave 6 — build — landing log

| Project | Product | Commit | Tally vs spec | Tests | Bugs found by running |
|---|---|---|---|---|---|
| ai-ads-injection | `aicrawlcheck` | (wave-6 commit) | matched | offline suite passes | cp1252 stdout; BrokenPipeError on `--out csv \| head` — both fixed |
| agent-hermes-dashboard | `Foreman` | `0e262eb` | 13-key tally matched first run, no fixture edits | 19/19, incl. both voice tone tests | `hookcmd.main` recorded a null-heavy row for malformed-but-valid JSON — now filters on `hook_event_name in ("Stop","SubagentStop")` |
| ai-attack-defense | `parity-vi` | running | — | — | — |

Foreman safety check: SHA-256 of `~/.claude/settings.json` byte-identical before and after
the full e2e run, verified twice. `assert_not_global()` in place. No real ledger content
copied into the repo.

## Wave 7 / 8 — spawned 2026-09-17

| Project | Wave 7 (Sonnet, e2e) | Wave 8 (Fable, sales page) |
|---|---|---|
| ai-ads-injection | running | running |
| agent-hermes-dashboard | running | running |
| ai-attack-defense | waits on build | waits on build |

Waves 7 and 8 run concurrently per project — 7 owns `prototype/` and
`docs/execution/`, 8 owns `site/`. Disjoint file sets, both told the other is live.

Port assignment for local sales-page review: 8801 ads, 8802 hermes, 8803 attack-defense.

---

# MANDATE — concurrency cap (user, 2026-09-17)

**Never more than 3 agents running at once, machine-wide.** Main thread is the scheduler
and does not count toward the 3. Subagents of a subagent count. The cap is a hard ceiling,
not a target — 2 is fine, 4 is a violation.

This file is the mandate. Read it before every spawn decision.

## Scheduler rules

1. Before spawning, count live agents. If the count is already 3, do not spawn — queue.
2. Spawn only on a completion notification, and only up to the free slots.
3. One agent per project at a time is the default. Two agents on one project are allowed
   only when their file sets are provably disjoint AND a slot is free — and each must be
   told in its prompt that the other is live and which paths it may not touch.
4. `infra/` counts as a project for scheduling. It is not free.
5. A stopped agent is not a failed agent. Record the stop in that project's `STATE.md`
   so the next agent does not read an orphaned "starting work" entry as a crash, and
   restore the working tree with `git checkout` if the stop left it half-mutated.
6. Re-queued work goes back at the FRONT of the queue, not the back. Do not let a task
   starve because new waves keep jumping it.

## Queue — live

Live now (3/3):

| Agent | Model | Project | Owns |
|---|---|---|---|
| parity-vi build | Sonnet | ai-attack-defense | `prototype/`, `docs/execution/` |
| Traefik hosting | Sonnet | infra | `infra/` |
| ads sales page | Fable | ai-ads-injection | `site/` |

Queued, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | aicrawlcheck e2e | Sonnet | ai-ads-injection | re-queued, was stopped for the cap |
| 2 | Foreman e2e | Sonnet | agent-hermes-dashboard | re-queued, was stopped for the cap |
| 3 | Foreman sales page | Fable | agent-hermes-dashboard | re-queued, was stopped for the cap |
| 4 | parity-vi e2e | Sonnet | ai-attack-defense | waits on build |
| 5 | parity-vi sales page | Fable | ai-attack-defense | waits on build |
| 6 | review: ads | Opus | ai-ads-injection | wave 9, vision review, needs e2e + site |
| 7 | review: hermes | Opus | agent-hermes-dashboard | wave 9 |
| 8 | review: attack-defense | Opus | ai-attack-defense | wave 9 |
| 9-11 | fix-and-retest ×3 | Sonnet | all | wave 10, one per project |

Wave 11 (publish to `dev1/dev2/dev3.vad37.com`) is main-thread work and is gated on the
Cloudflare token gaining **Zone · DNS · Edit**.

## Why the cap

Six concurrent agents contend on one browser, one Docker daemon, and one set of ports,
and the main thread cannot hold an accurate picture of six moving trees. Three is what
stays reviewable.

## Queue update — 2026-09-17, after parity-vi build landed

All three builds are now in. Commits: ads `aicrawlcheck` (wave 6), hermes `Foreman`
`0e262eb`, attack-defense `parity-vi` `db2ae18`.

parity-vi: all pre-registered spec numbers matched exactly after one bug fix. The bug is
worth carrying forward — Python rounds half-to-even, the spec's numbers use round-half-up,
and it surfaced only at an exact tie (26/32 = 81.25%). The agent fixed the code and left
the spec numbers alone, which is the rule working as intended. It also caught the same
`wc -l` CSV miscount the main thread flagged earlier and corrected `data/README.md` to
csv-parsed 8,844/1,106/1,106.

Two exit-code lessons now confirmed on two separate projects: check `echo $?` on the
command itself, never through a pipe. Piping to `head` masks the real code. This is now
written into every e2e prompt.

Live now (3/3):

| Agent | Model | Project | Owns |
|---|---|---|---|
| Traefik hosting | Sonnet | infra | `infra/` |
| ads sales page | Fable | ai-ads-injection | `site/` |
| aicrawlcheck e2e | Sonnet | ai-ads-injection | `prototype/`, `docs/execution/` |

Two on ai-ads-injection, allowed under scheduler rule 3: file sets disjoint, both prompts
name the other as live and name the paths they may not touch.

Queue, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | Foreman e2e | Sonnet | agent-hermes-dashboard | re-queued from the cap stop |
| 2 | Foreman sales page | Fable | agent-hermes-dashboard | re-queued from the cap stop |
| 3 | parity-vi e2e | Sonnet | ai-attack-defense | build landed, now unblocked |
| 4 | parity-vi sales page | Fable | ai-attack-defense | `site/demo-data.json` already emitted for it |
| 5-7 | review ×3 | Opus | all | wave 9, vision review, needs e2e + site per project |
| 8-10 | fix-and-retest ×3 | Sonnet | all | wave 10 |

## Queue update — 2026-09-17, after the ads sales page landed

Commit `fb561df`. First of the three sales pages in.

The thing worth copying to the other two sales-page agents: this agent did not trust its
own port. The page embeds a JS reimplementation of `verify.py`'s decision table over 637
prefixes, so it extracted that script under Node with a stubbed DOM and diffed it against
`aicrawlcheck scan --out csv` across all 420 fixture lines — 418/418 identical, 2 unparsed
on both sides. A demo that disagrees with the CLI it advertises is worse than no demo.

The honesty rule produced real subtractions, which is the signal it is working:
no comparison to general log analyzers, no real-world spoof rate (the fixture's 25-of-155
is labelled `fixture-measured` and "not a real-world rate" at both mentions), no "detects
undeclared crawlers", no clone URL. The incumbent callout concedes its own size in the
page's own words.

Deviation logged, raw beating brief: the rDNS line reads 6 of 6 sampled OpenAI addresses,
not the brief's 3 of 3, because `raw/rdns-lookups.txt` holds GPTBot 3 + OAI-SearchBot 1 +
OAI-AdsBot 2, all NXDOMAIN. Correct call — the brief was stale, the raw was not.

Browser screenshots were not in that agent's grant and are deferred to the wave 9 vision
review. The agent named three places to look first: the three-column argument cards near
960-1120 px, the results table in card mode at 390 px, and the wrapping `.tag` chips.
Carry those into the ads review prompt.

Live now (3/3):

| Agent | Model | Project | Owns |
|---|---|---|---|
| Traefik hosting | Sonnet | infra | `infra/` |
| aicrawlcheck e2e | Sonnet | ai-ads-injection | `prototype/`, `docs/execution/` |
| Foreman e2e | Sonnet | agent-hermes-dashboard | `prototype/`, `docs/execution/` |

Queue, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | Foreman sales page | Fable | agent-hermes-dashboard | re-queued from the cap stop |
| 2 | parity-vi e2e | Sonnet | ai-attack-defense | |
| 3 | parity-vi sales page | Fable | ai-attack-defense | `site/demo-data.json` already emitted for it |
| 4 | review: ads | Opus | ai-ads-injection | wave 9 — site landed, waits on e2e |
| 5 | review: hermes | Opus | agent-hermes-dashboard | wave 9 |
| 6 | review: attack-defense | Opus | ai-attack-defense | wave 9 |
| 7-9 | fix-and-retest ×3 | Sonnet | all | wave 10 |

## Queue update — 2026-09-17, infra + ads e2e landed

Commits: infra `f2573f0` (root repo), ads e2e `4373c3a`.

**Secret caught in review, worth generalising.** `cf-tunnel.py` masked every credential it
sends to the last 4 characters, correctly. But `infra/README.md` pasted the raw
`/user/tokens/verify` RESPONSE body, which carries the API token's own `id` field — and
our masking never sees Cloudflare's output. Redacted before the commit. A token id is not
the token secret and cannot authenticate, but it is a durable credential identifier and
falls under the same rule.

Standing rule, now in `infra/README.md`: **mask the values you send AND the values that
come back. The response body is the half that gets forgotten.** Apply this to every agent
that pastes live API output into a repo.

**Traefik finding.** The Docker provider cannot reach this machine's Docker daemon —
reproduced on v3.1 and v3.4, isolated to a Traefik-client vs new-engine (moby/moby v2)
incompatibility, not a config error. `docker info`, a raw socket curl and the official
`docker:cli` image all work against the same socket. Worked around with a file provider
carrying identical host rules against network aliases. All three sites return HTTP 200
locally today with zero Docker-socket dependency. Labels stay configured for the upstream fix.

`create --execute` was deliberately NOT run. Creating a real Cloudflare resource is the
user's call. Still gated on **Zone · DNS · Edit** regardless.

**Ads e2e: 24/31 pass, 0 new bugs.** Items 20-28 are browser tests against
`site/index.html` and are marked NOT COVERED rather than passed, because `site/` was a
concurrent agent's scope. That is the correct call and the wave 9 review inherits them.

Browser contention is now a real scheduling constraint: Chrome is one shared resource.
Do not run two browser-driving agents at once. A Fable sales-page agent and an Opus
vision review must not overlap. Prefer a non-browser agent when a browser agent is live.

Live now (3/3):

| Agent | Model | Project | Owns | Browser? |
|---|---|---|---|---|
| Foreman e2e | Sonnet | agent-hermes-dashboard | `prototype/`, `docs/execution/` | no |
| Foreman sales page | Fable | agent-hermes-dashboard | `site/` | YES — port 8802 |
| parity-vi e2e | Sonnet | ai-attack-defense | `prototype/`, `docs/execution/` | no |

Queue, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | parity-vi sales page | Fable | ai-attack-defense | browser, port 8803 |
| 2 | review: ads | Opus | ai-ads-injection | wave 9 — UNBLOCKED, prototype + e2e + site all landed. Inherits acceptance items 20-28. Look first at the three-column cards near 960-1120 px, the results table in card mode at 390 px, the wrapping `.tag` chips |
| 3 | review: hermes | Opus | agent-hermes-dashboard | wave 9 |
| 4 | review: attack-defense | Opus | ai-attack-defense | wave 9 |
| 5-7 | fix-and-retest ×3 | Sonnet | all | wave 10 |

ai-ads-injection is the first project with all four MVP deliverables on disk:
`prototype/` that runs, `docs/execution/e2e-test.md`, `site/index.html`, `docs/outcome/`.

## Queue update — 2026-09-17, Foreman e2e landed

Commit `8aaac10`. The e2e pass earned its cost on this one.

**Safety bug found by running it, not by reading it.** `hookcmd.py`'s `_log_failure()`
wrote a diagnostic log to `dirname(--ledger)/foreman-hook.log` on any exception, with no
`assert_not_global()` call anywhere in the file. If `--ledger` were ever misconfigured to a
path under `~/.claude`, the ledger write would be correctly blocked and the failure-log
write would land inside `~/.claude` unguarded. **The guard protected the happy path and not
the error path.** Reproduced in a sandbox with `expanduser` monkeypatched to scratchpad,
never the real path. Fixed, re-verified, full e2e re-run from clean.

Generalise this: a safety guard is only as good as its least-exercised branch. Every
review from here checks the exception handlers, not just the main write path.
`assert_not_global()` is now confirmed on all 9 write call-sites across 6 write locations.
`~/.claude/settings.json` SHA-256 unchanged.

Foreman timing: 0.365s from `cd prototype` to the full six-section report.

Voice verdict recorded honestly rather than sold: the mocking tone lands, but narrowly.
It is safe precisely because the mechanical tests forbid it from attaching a number to the
mockery — which also makes it toothless by construction. One framing flaw flagged: the
report says "you typed" about tasks an agent executed. Wave 10 candidate.

## Wave 9 is split in two

The vision half of the review needs Chrome, and Chrome is one shared resource. Rather than
idle a slot behind it, wave 9 now runs as two agents per project:

- **9a — code/test/honesty review (Opus, no browser).** Re-runs the headline path from
  clean, audits the decision logic, audits every sales-page claim against the build log and
  e2e doc, cross-checks every number across all five artifacts, gives a buy/no-buy read.
  Writes `docs/outcome/review.md` ending in the mandated `## Is this enough?` heading, with
  a `## Vision review — pending` placeholder naming what the browser pass must look at.
- **9b — vision review (Opus, browser).** Appends its section. Serialized against every
  other browser agent.

9a agents are told to RECORD, not repair. A review that quietly fixes what it found leaves
no record of what was wrong. Wave 10 repairs.

Live now (3/3):

| Agent | Model | Project | Owns | Browser? |
|---|---|---|---|---|
| Foreman sales page | Fable | agent-hermes-dashboard | `site/` | YES — 8802 |
| parity-vi e2e | Sonnet | ai-attack-defense | `prototype/`, `docs/execution/` | no |
| review 9a: ads | Opus | ai-ads-injection | `docs/outcome/review.md` | no |

Queue, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | parity-vi sales page | Fable | ai-attack-defense | browser, 8803 |
| 2 | review 9a: hermes | Opus | agent-hermes-dashboard | needs `site/` to land first |
| 3 | review 9a: attack-defense | Opus | ai-attack-defense | needs e2e + site |
| 4 | review 9b: vision ×3 | Opus | all | browser, strictly serialized |
| 5 | fix-and-retest ×3 | Sonnet | all | wave 10 |

---

# MANDATE CHANGE — success vision precedes planning (user, 2026-09-17)

User caught a real hole in this orchestration:

> "I detect a problem. I think the agent planning wont make a good plan without a final
> vision of outcome docs. so far we dont have these and agents just making blind decision."

Correct, and it is my error. `docs/outcome/` was listed as a required deliverable in
MVP-MANDATE.md, but it was scheduled LAST — after build, after test, after the sales page.
So every agent so far has optimized against a spec and a 31-item acceptance checklist with
no statement of what winning looks like. The specs are locally correct and possibly
globally pointless. The one outcome doc that exists (`ai-ads-injection/docs/outcome/
positioning.md`) was written after the page it justifies, which is backwards.

**New rule: a project's `docs/outcome/success-vision.md` is written BEFORE its sales page
and BEFORE its review, and every downstream agent reads it.** Vision is a Fable job.

A Fable vision agent is now running across all three projects with an explicit
cross-project write grant (one `success-vision.md` per project, plus
`projects/SUCCESS-VISION.md` for the portfolio read). It is told to ground every
present-tense claim in the build and e2e docs, to read the earlier research KILL verdicts
and be honest about them, and that concluding "the honest win here is much smaller than
the original ambition" is the most useful thing it can report.

Its section 7 — the ranked gap between what the e2e docs prove today and the win condition
— becomes the wave 10 fix agents' work list. Wave 10 no longer works only from review
findings; it works from review findings PLUS the vision gap list.

## Queue reordered

`parity-vi sales page` is deliberately held. Writing the last sales page before the
vision doc exists would repeat the mistake the user just caught. It now waits for the
vision agent, not just for a slot.

Live now (3/3):

| Agent | Model | Project | Owns | Browser? |
|---|---|---|---|---|
| Foreman sales page | Fable | agent-hermes-dashboard | `site/` | YES — 8802 |
| review 9a: ads | Opus | ai-ads-injection | `docs/outcome/review.md` | no |
| success vision | Fable | ALL THREE + portfolio | `docs/outcome/success-vision.md` ×3 | no |

Queue, in order:

| # | Agent | Model | Project | Note |
|---|---|---|---|---|
| 1 | parity-vi sales page | Fable | ai-attack-defense | HELD until the vision doc lands; browser 8803 |
| 2 | review 9a: hermes | Opus | agent-hermes-dashboard | reads the vision doc |
| 3 | review 9a: attack-defense | Opus | ai-attack-defense | reads the vision doc |
| 4 | review 9b: vision pass ×3 | Opus | all | browser, strictly serialized |
| 5 | fix-and-retest ×3 | Sonnet | all | works from review findings AND the vision gap list |

## parity-vi e2e landed — commit `589e1ab`

Every pre-registered number reproduced independently from a from-scratch build, including
ViHOS re-counted with the agent's OWN csv parser rather than the harness's. That is what
an independent check is supposed to mean.

Bug found: `parity.py verify` printed licence lines for 2 of 3 corpora — ViHOS missing —
failing acceptance item 4 verbatim. Fixed and re-verified from a clean rebuild; `set_hash`
unchanged.

The no-network claim is now proven DYNAMICALLY: `socket.socket`, `getaddrinfo` and
`create_connection` monkey-patched to raise inside the process actually running `demo`,
with a positive control validating the blocker first. This supersedes the build agent's
static grep, and the agent said so explicitly rather than quietly upgrading the claim.
Carry the pattern: prove a negative by making the forbidden thing fail loudly, not by
grepping for its name.

Honest gap it recorded: the CLI lists misses by id, not prompt text, so the visceral
version of the finding needs the sales page or a manual `bundle.json` read. Two real
examples surfaced that way — "blow up a Mosque", "set someone on fire" — both caught in
EN, missed in VI. That is the product's entire pitch sitting one layer too deep to see.
Wave 10 candidate, and likely a vision-doc gap item.

## Wave 9a — ads review landed, commit `3bdac7e`

The review did its job: it found a counterexample to the product's own thesis.

**S1, CONFIRMED and reproduced end to end.** `--verify-dns` will verify any Google Cloud
tenant as Googlebot. `engines.py:100` keeps `.googleusercontent.com` in the Googlebot
FCrDNS suffix list, which is shared tenant infrastructure any customer can land on.
Demonstrated with `34.162.230.222` — an **Anthropic** crawler IP taken from this
project's own `raw/rdns-lookups.txt` — reported as `verified / fcrdns / Googlebot`.

The product's single claim is that it does not believe a claimed identity. This is the
tool believing one.

**S1b is the deeper lesson.** `e2e-test.md:415` claimed `--verify-dns` does not launder a
false claim, and that test passed — against an RFC 5737 address, which has no PTR record
and fails at step 1 before the suffix list is ever consulted. **The test passed for the
wrong reason and certified the bug.** Bug is spec-origin (`mvp-spec.md:423`) and was built
faithfully, so the chain was: wrong spec → faithful build → test that never reached the
code path → confident claim on the sales page.

Generalise it, and apply to every remaining review: for each claim of the form "X cannot
happen", identify the code path that would have to execute for X to happen, and confirm
the test actually reaches it. A negative proven by a case that short-circuits earlier
proves nothing. This is the same shape as the Foreman finding (guard on the happy path,
absent on the error path) and the parity-vi finding (no-network proven by grep rather than
by making sockets raise). Three projects, three instances, one bug class:
**the safety property was asserted where it was easy to assert, not where it could fail.**

Also confirmed: two unbackable page claims (S2 Amazonbot range file, S3 a block labelled
"Actual terminal output" that was hand-edited), real nginx/Apache logs rejected two ways
with 0 of 2 realistic lines parsed (S4), Applebot classified as `human` (S5), a headline
count wrong at 155 vs an actual 180 (S6), and `refresh --only` disarming the staleness
guard the page sells (S7).

Clean on the honesty rule otherwise — no UA-alone path to verified, no hardcoded allowlist
shortcut, no fake logos/testimonials/counts/urgency/scarcity, no fake clone URL, no
unmeasured competitor, and the 25-of-155 figure correctly labelled a fixture design choice
everywhere it appears. The page's 418/418 self-verification claim was independently
reproduced under Node, matching evidence strings character-for-character across a Python
and a JavaScript implementation.

**Reviewer's verdict, recorded not softened: no-buy as a paid product.** It answers a
once-asked question and produces no action the user can take. Yes as a free credibility
artifact. The success-vision agent now running will have something to say about this, and
the two reads should be compared when it lands.

## Wave 10 started early on ads, scoped to facts only

A fix agent is running on the ads findings. It is explicitly told it is fixing FACTS, not
DIRECTION, because the vision doc is still being written and may change the product's
positioning. It may not touch `docs/outcome/`, may not reposition the product, and may not
add features that change what the tool is for. A second fix pass handles direction once
the vision lands.

It must also append a dated correction to `mvp-spec.md` — the spec is the origin of S1 and
has to stop being a source of that bug — and a dated correction to `e2e-test.md` marking
the insufficiently-tested claim. Append, never rewrite history.

Live now (3/3):

| Agent | Model | Project | Owns | Browser? |
|---|---|---|---|---|
| Foreman sales page | Fable | agent-hermes-dashboard | `site/` | YES — 8802 |
| success vision | Fable | all three + portfolio | `docs/outcome/success-vision.md` ×3 | no |
| wave 10 fix: ads | Sonnet | ai-ads-injection | `prototype/`, `site/`, `docs/execution/` | no |

## Wave 8 complete on hermes — Foreman sales page, commit `b8d17c8`

Two of three sales pages in. This one raised the verification bar again: the ads page
diffed its JS port against the CLI over 420 lines; this one did 421/421 corpus strings,
1,770/1,770 pairwise Jaccard scores to two decimals, 60/60 fixture token sets, 13/13 tally
keys, a byte-identical 2,519 B report, and **200/200 random ledgers** — 4,863 records,
191 graduations, 36 empty — identical on both report text and tally. Python's half-to-even
rounding was reimplemented explicitly and covered by tie cases, which is the same trap
parity-vi hit from the other direction.

The page states the `assert_not_global()` bug and its fix rather than hiding it. That is
the honesty rule producing something better than silence — a security fix disclosed on the
sales page reads as competence, not weakness.

Still open and correctly disclosed: **nobody has ever watched a live `Stop` event fire the
installed hook.** The e2e confirms it. Every claim about hook capture rests on synthetic
payloads and on the 14 keys measured in `docs/explore/telemetry-measured.md`. That is a
real gap between "it works" and "we have seen it work", and it belongs in the vision doc's
gap list.

Browser note for wave 9b: the Chrome window would not resize below 1920, so this agent
measured 390x844 through a same-origin iframe (`scrollWidth` 371 <= 386, no element outside
a `pre`/table container past the viewport) and reviewed by eye at zoom. Chrome screenshot
capture timed out on roughly half the calls. **The 9b agent should expect the same and plan
for it — measurement is the fallback when capture fails, and a timed-out screenshot is not
evidence of a broken page.**

## Wave 9a on hermes spawned

Its priority task is the fourth instance of the bug class. It is given all three prior
instances explicitly and told to hunt for the next one: for every "X cannot happen" claim,
name the code path that must execute for X to happen and confirm a test reaches it. It
re-audits `assert_not_global()` across exception handlers, `finally` blocks, atexit and
signal paths, and anywhere a path is derived from user input, symlinks, `..` segments or
env vars.

It is also told to judge whether the recurrence layer is real or theatre — 60 records ->
41 shapes -> 1 graduated could be genuine clustering or a fixture built so exactly one
thing graduates. The brief's own trap says the dashboard is the worthless half and the
record/recurrence layer is the claim, so that section decides whether this product has a
claim at all.

It reads `success-vision.md` if the Fable agent lands it mid-run, and gives an independent
buy/no-buy read either way. Two independent reads on the same product is worth having —
the ads reviewer said no-buy-as-paid, yes-as-credibility-artifact, and it will be worth
seeing whether the vision agent argues the same from the opposite direction.

Live now (3/3):

| Agent | Model | Project | Owns | Browser? |
|---|---|---|---|---|
| success vision | Fable | all three + portfolio | `docs/outcome/success-vision.md` ×3 | no |
| wave 10 fix: ads | Sonnet | ai-ads-injection | `prototype/`, `site/`, `docs/execution/` | no |
| review 9a: hermes | Opus | agent-hermes-dashboard | `docs/outcome/review.md` | no |

Chrome is free. It is deliberately being held free for the 9b vision passes rather than
spent on a fourth concurrent agent, since the cap is 3 and browser work cannot overlap.

---

# WAVE 9V — success vision landed. It changes the plan.

Commits: `b856b7a` ads, `b7037ed` hermes, `379b792` attack-defense, plus
`projects/SUCCESS-VISION.md` at portfolio level.

The user was right that agents were planning blind. The vision doc's central finding is
one no spec or acceptance checklist could have produced, and all three e2e docs had
independently written down half of it without anyone connecting them:

> **All three products' single moment has never happened on real input.**
> aicrawlcheck has never run on a real log. Foreman's recurrence has never seen a real
> ledger. parity-vi has never been pointed at a real guardrail — both its demo runs use a
> synthetic adapter whose regression the spec itself seeded.

Every page currently leads with the fixture demo. The vision doc names that as the
fake-demo trap in all three files: **the demo that wows and means nothing.** The pages are
more finished than the products.

## Ranked recommendation — remaining effort

| Share | Project | Why |
|---|---|---|
| **70%** | **parity-vi** | The only one with a named, reachable buyer in the team's own city (AI Hay, Vbee, Filum AI), the channel the research rated strongest (1-on-1 proximity), a claim that survived review, a services shape that works at n=1, and a zero-spend path to its own moment — local Qwen3Guard-Gen-0.6B in a `uv` venv, permitted by the mandate. The only honest win that includes money. |
| 20% | Foreman | Buyer broke in review; what it carries is the user's creative intent. Publish and let the pre-registered 14-day gate decide (>=100 stars AND >=3 unprompted paid asks). |
| 10% | aicrawlcheck | One real log, a repo, a post, stop. Check GoAccess/AWStats/Matomo first — one hour, never done. If one already verifies UA claims against ranges, a PR is the whole product. |

No fourth product. The three share no buyer but share a DNA: offline checkers that turn
someone else's claim into evidence, with the source on every row. That is an auditor's
competence — the honest fourth thing is the measurement *service* all three tools are
instruments of, which confirms `cross-read.md` pattern 3 from the build side.

## New wave 10 rule — real input before polish

First task per project, ahead of any cosmetic fix: **one real log / one real ledger via
history mode / one real guardrail via a local adapter.** Then the page leads with a real
`n=1` number and the fixture demo is demoted to "how it works".

Two small high-value CLI items the vision surfaced, both confirmed absent today:
- Foreman `scan --from-history` over `~/.claude/history.jsonl` — every field recurrence
  needs is already there, 3,103/3,103 parsed in the e2e. Moves the "oh" moment from a
  fortnight out to the first run. Confirmed no such subcommand in `foreman/__main__.py`.
- parity-vi `report --show-misses` — the e2e found the visceral half of the moment
  currently requires opening `bundle.json` by hand.

## Honesty lines a "fix" will be tempted to loosen — hold them

No digit in a Foreman voice template. No `keyword` gap charted. One sentence only on
Law 134/2025/QH15. 25-of-155 never quoted as a rate. No "the only tool". No vendor host in
the parity-vi repo.

Caveats the vision doc carries and that must survive into any page: every win-condition
scenario is labelled fiction, **no buyer has been contacted by any pass**, and `/insights`,
GoAccess/AWStats/Matomo and the Qwen3Guard route are all `unknown — not checked/tried`.
No wave 9 review had landed when the vision was written, so the ads review's no-buy verdict
and this document's 10% allocation for ads were reached independently and agree.
