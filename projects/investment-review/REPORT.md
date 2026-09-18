# REPORT — three prototypes, investment review, 2026-09-18

Stage 3.5 of `projects/investment-review/`, per `REPORT-PLAN.md` §2–§8 and its 2026-09-18 addendum: (b), (b2), (c), (e) carry the verdict; (d) is context. Inputs: `review-aicrawlcheck-`, `review-foreman-`, `review-parity-vi-2026-09-18.md`; `raw/c1..c4-*`; `raw/audit-root-research-2026-09-18.md`; `raw/audit-project-docs-2026-09-18.md`. No figure here is new; arithmetic over cited figures is shown inline.

Labels: `[m]` measured-by-us · `[v]` vendor-reported · `[a]` analyst-derived · `[f]` filed · `[c]` company-stated · `[oj]` own judgement · `[rh]` requires-human · `[fx]` fixture. FX, side by side, never averaged: SBV central VND 25,306/USD (`[f]` 2026-07-27, c4 §5; Foreman and parity-vi reviews) vs Vietcombank selling 26,525 (`[v]`, same date; ads review); 2026-09-18 rate `unknown — checked vietcombank.com.vn, sbv.gov.vn 2026-09-18`. USD figures keep their review's rate; the 4.8% spread moves nothing.

## (a) Executive verdict

| Project | KILL A3 / A6 / A10 | Verdict (§D10 form) | Number that flips it | Gate expires |
|---|---|---|---|---|
| `aicrawlcheck` | UNKNOWN / UNKNOWN / FAIL (context) | 23 h / $11 / 3 weeks to A3 via the pre-registered 20-org probe, else stop | one 7.500.000 VND deposit, not a personal contact | 2026-10-02 (day 7 = 2026-09-28, +5-day WEAK) |
| `Foreman` | UNKNOWN / FAIL / FAIL | 11 h / $0 / 2 weeks to close A6 (`/insights`, two repos) and A10 (real-ledger count), else stop | any incumbent lists repeated work → stop; 0 real clusters ≥5 across ≥2 days → stop | 2026-10-02 |
| `parity-vi` | UNKNOWN / UNKNOWN / PASS open-weights, UNKNOWN commercial | 8 h / $0 / 3 weeks to the 14-day buyer gate (≥1 buyer-side run AND ≥3 replies from 7 orgs), else stop, keep as calling card | buyer-stated price ≥30.4M VND by 2026-10-10 → build; 0 written replies by 2026-10-03 → stop | 2026-10-03; WEAK to 2026-10-10 |

All three read "gate first" — compared, not flattened. The gates differ in channel and what they buy: `aicrawlcheck`'s is 20 cold contacts at 0.686 expected replies (20 × 3.43% `[v]`); `Foreman`'s is two hours of reading that can end the project the same afternoon, then one count on a real ledger, before any buyer; `parity-vi`'s is seven organisations reachable in person, the only gate whose pass value is money. No verdict exceeds its KILL ceiling. Every minimum-commitment EV is negative on cash (h); the gates buy information. The user's prior — "I found ai defense product is just bullshit" — as the parity-vi review tested it (§10):

| Thread | Result | Number |
|---|---|---|
| Vietnamese-gap thesis | Prior holds | 0 of 5 models show it: 3.7 / 2.5 pp, CIs overlap, on cards claiming many languages; 25.5 / 28.5 pp on cards saying "English only" `[m]` |
| Instrument | Prior does not hold | Granite 3.0→3.1 diff exit 1, +21 net VI misses `[m]`; 43 tests `[m]`; promptfoo has no `diff` `[v]`; moat weeks–months `[oj]` |
| Services wedge | UNKNOWN | 23 named, 8 profiled, 0 contacted `[m]`; 0 VN incidents, 0 live safety jobs, 10 vendors quote-only `[m]` |

## (b) Market understanding

```
aicrawlcheck (review §5)
N_buyers  = 8                 [m: named VN GEO agencies, raw/vietnam-ai-visibility-demand.md 2026-09-17]
ARPU      = 15,000,000 VND    [oj; anchors: SEODO "từ 18 triệu" [v]; Hashmeta audit "trị giá 15.000.000đ", given free [v, c1 §19]]
share     = 0.10   cycles_36mo = 3          [oj; §B5 cap; same-slot repos 1★ / 0★ [m, c1 §7]]
market_36 = 8 × 15M × 0.10 × 3 = 36,000,000 VND  (USD 1,357 at 26,525)
ratio     = 36M / (2 × 1,326.25M) = 0.014   |  salary basis 36M / 1,317.6M = 0.027   → FAIL either way
break-even N = 589 named buyers; largest named set on file = 8
```
```
Foreman (review §5)
N_buyers  = unknown           [c2 §4: no Anthropic headcount; c2 §11: 3–4 first-person posts, no denominator]
ARPU_yr   = $24               [v, SessionWatcher Pro $24/yr, c2 §8 — a comparable; Foreman is $0 by pre-registration]
share     = 0.05              [oj; claude-session-budget 8★ over four months, c2 §7]
market_36 = N × 24 × 3 × 0.05 = N × $3.60;  ratio ≥1 needs N ≥ 14,464 (salary) / 27,778 (contract)
N unknown → ratio unknown → A5 UNKNOWN
```
```
parity-vi (review §5)
N_buyers  = 23                [m, c3 §1: 8 profiled + 15 found; 4 rows weak; 1 ministry; 0 contacted]
ARPU      = 15,000,000 VND (≈ $593 at 25,306)   [oj; anchors: ads probe price; Cobalt $3,500/test, US [v]]
share     = 0.10   engagements/buyer = 1        [oj]
market_36 = 23 × 15M × 0.10 = 34,500,000 VND (≈ $1,363);  ratio = 34.5M / 1,317.6M = 0.026 → FAIL
sensitivity: 100% share × 3 engagements = 1,035M → 0.79, still <1; break-even price at 100% share = 57.3M VND/company
```
```
Founder opportunity cost (§B14) — stated once
(a) salary   = 54.9M VND/mo [v, ITviec 2025–26, back-end >8 yr, n=1,839, c4 §1] ÷ 176 h [oj] = 311,932 VND/h = $11.76 (26,525) / $12.33 (25,306)
(b) contract = $25–80/h [v, Upwork VN AI band via Second Talent 2026-08/09, c4 §2]; §B14 takes the higher → $25/h floor
(c) clinic-MCP = requires-human — not pulled [c4 §3]; if above $25/h every EV below worsens
founder_cost_yr = (a) 658.8M VND ≈ $26,033  |  (b) $25 × 2,000 h [oj] = $50,000 ≈ 1,326.25M VND
side by side, not averaged: Second Talent senior 85–125M VND/mo [a]; reco-vn 25–100M [a]; ITviec AI+Blockchain 4-yr 37.75M [v, 2024–25 edition]
```

Who buys, by name: eight Vietnamese agencies selling optimisation, not measurement (ads); nobody named (Foreman); 23 companies operating Vietnamese chat products, none of whose eight reached pages carries a safety statement, vendor or guardrail (c3 §14 `[c]`). What they pay today for the nearest thing — ads: SEODO từ 18tr, Fast Marketing 32/45/65tr per tháng, Midas từ 80tr/tháng, Hashmeta GEO 60tr+/tháng `[v]`; Known Agents $0 / $29 / $299 `[v]`; Cloudflare Bot Management, DataDome, HUMAN publish no self-serve price (c1 §14). Foreman: SessionWatcher $6.99 / $14.99 / $59 or $24/yr, CrewTower $9.99 / $14.99 `[v]`; Braintrust Topics Pro $249/mo `[v]`; `/insights` $0; no disclosed revenue for any paid Claude Code tool (c2 §9). parity-vi: Azure F0 $0 for 5,000 records/mo, S0 $0.38/1,000 (secondary) `[v]`; OpenAI moderation $0 `[v]`; six VN pentest vendors and four ISO-42001 certifiers quote-only (c3 §9–10); Cobalt $3,500/test is a US price; the $8k–$50k US band appears only to be rejected (`evidence-rules.md` rule 2).

None clears the founder's opportunity cost: ratios 0.014 / 0.027, unknown, 0.026. Inadmissible and set aside: Mordor $4.39B (`ai-search-ads.md`); W3Techs 25.8% of websites on Cloudflare (a share, not a count, c1 §5); r/ClaudeAI ≈1.1M (`[a]`, three trackers conflicting); the "$130M Vietnam AI funding 2025" blog figure (c4 §7). Sensitivity: the ads ratio is insensitive to the rate choice (74× vs 37× short); parity-vi to share and cycles (0.79 at the ceiling); Foreman's is unknown at any rate.

## (b2) Research quality

Can the founder trust his own research? Counts from the two audits (`[m]`, 2026-09-18):

| Scope | Files | TRACED | DRIFT | UNTRACED | MEMORY | STILL-TRUE / CHANGED / GONE | Contradictions | Worst finding |
|---|---|---|---|---|---|---|---|---|
| Root `docs/` | 21 | 40/40 | 0 | 0 | 0 | 13 / 2 / 0 (§5; §3 lists three CHANGED rows — XBOW raise >$235M vs $195M; Anthropic bounty $15k vs $35k; AI Hay founders findable) | — | no bottom-up figure anywhere; labels 4/61 `first-customers.md`, 6/53 `two-founder-cases.md`; claim #35 cites the wrong raw file |
| `ai-ads-injection/docs/` | 16 | 20/20 | 0 | 0 | 0 | 3 / 1 / 1 | 3, 1 unreconciled | 155-vs-180 denominator still in `mvp-spec.md:621`, `positioning.md:15`; 5 files use non-canonical labels |
| `agent-hermes-dashboard/docs/` | 14 | 17/20 | 3 | 0 | 0 | 5 / 0 / 0 | 3, all reconciled | `claude-code-substrate.md:60`, `task-telemetry.md:12` still assert cost/duration_ms — false by 3 live runs; ≈0 label tokens in 9 files |
| `ai-attack-defense/docs/` | 26 | 15/20 | 4 | 0 | 1 | 4 / 1 / 0 (SEA-HELM 72.18 → 72.42) | 3, 1 unreconciled | MEMORY claim `aisb-inventory.md:23` (HiddenLayer); ViHSD arXiv ID wrong in two files; 6 execution files with 0 labels |

Pipeline 6/6 for all three; every `market-check.md` cites root `docs/markets` or `docs/findings` by filename with quotes. The reviews' §D2b tables, one cell per axis:

| Axis | `aicrawlcheck` | `Foreman` | `parity-vi` |
|---|---|---|---|
| Buyer | self-labelled "a hypothesis"; 0 asked; pull could not check | persona; 3–4 posts, no denominator; 0 asked | 23 named, 8 profiled; 0 asked; "in person" true for 3 of 8 |
| Problem | attention confirmed (305 pts / 228 comments `[m]`); paid job contradicted (74 Show HN, best 7 pts; audit given free) | 828 / 93,582 = 0.88%, cost-governor demand; no Foreman count exists | card-confirmed on "English only" models; null on multilingual; 0 VN incidents `[m]` |
| Price | four VN lists, all optimisation SKUs `[v]`; no measurement price | $24/yr comparable `[v]`; category has no disclosed revenue | 10 vendors quote-only `[v]`; no buyer number |
| Incumbent | gap confirmed in five vendors' own words `[v]`; 0 run | vendor has not shipped it (7,063-line changelog `[v]`); two repos, 7,078★, unopened | promptfoo no `diff` (docs `[v]`); Lakera, PyRIT unopened; 5 models run `[m]` |
| Regulation | not checked; no §1 row rests on it | consumer-terms clause confirmed `[f]`; Agent SDK change paused `[c]` | stale: NĐ 142/2026 (eff. 2026-05-01), QĐ 33/2026 (46 systems, eff. 2026-08-15) exist `[f]`; not demand (F9) |

The read: 92 of 100 sampled claims resolve to a raw file verbatim, 0 untraced, 1 from memory, and the docs are honest about their holes. The research is supply-complete and demand-empty in all three projects — price, incumbent and regulation rows are primary-sourced and survived a fresh adversarial pull; buyer and problem rows have been `unknown` since wave 1 because nobody was asked. The pulls contradicted no factual claim in the ads or parity-vi docs, corrected one in Foreman (the 2026-06-15 billing change was paused, not shipped — c2 §10) and found two Foreman explore files uncorrected on disk. The root layer's sharpest gap is the one (b) fills: no bottom-up figure existed anywhere.

## (c) Problems

| Project | Problem as the doc states it | Evidence it is real, with denominator | Frequency per sufferer | Who suffers, named | What they do today |
|---|---|---|---|---|---|
| `aicrawlcheck` | "which hits were real AI fetches, which forged, evidence shown, logs never leave" (`positioning.md`) | HN 305 pts / 228 comments 2026-08-12 `[m]`, visibility only; 74 Show HN, best 7 pts `[m]` | asked once (`review.md` §5) `[oj]` | nobody; "a hypothesis, not a finding"; 0 asked | UA-regex tools (GoAccess, AWStats `[v]`) or nothing |
| `Foreman` | operator "has never looked at what they keep re-typing" (`mvp-spec.md`); supervision layer is the product (`CLAUDE.md`) | 828 of 93,582 issues = 0.88%, last of 11 topics, aimed at the vendor (`re-pick.md` §3) `[m]` | `unknown — never counted on a real ledger` | persona; 3–4 Indie Hackers posts `[m]`; 0 named | re-type; `/insights` $0 `[v]`; `agentsview` 5,942★ `[m]` |
| `parity-vi` | guardrails "chosen for English and never measured on Vietnamese" (`mvp-spec.md` §2); Azure: "do your own testing" `[v]` | 5 models × 600 `[m]`: 25.5 / 28.5 pp on English-only cards; 3.7 / 2.5 pp, overlapping, on multilingual; 0 VN incidents, 0 live safety jobs (c3 §2, §13) | `unknown`; no false-positive ticket on file | 8 profiled, CTOs named; 23 nationwide; 0 asked | nothing — "an absence, not a workflow" (`success-vision.md` §4); TPBank routes ChatGPT/Gemini/Grok `[c]` |

Severity is an observation about humans, and none was observed: zero buyer conversations in any project, any pass (`pass4-read.md` point 2; `ORCHESTRATION.md` §8.4). The desk research cuts against each problem being a paid job. The ads threads are about bandwidth, not verification, and the 228-comment read that would separate them has not been done. Foreman's one demand number belongs to a product never built and asks the vendor for a free fix. parity-vi's measured gap is the vendor's card restated: the two models claiming broad coverage produce a null; the two saying "English only" produce the gap, and a buyer running one of those on Vietnamese traffic has a procurement error the card discloses (review §10 i). "Nobody has built this" is falsified for `aicrawlcheck` (same-slot repos at 1★ and 0★) and Foreman (session-history tools at 5,942★ and 1,136★); for parity-vi the paired corpus sits upstream in SEA-HELM, switched off 151 days `[v]`. Repeated independent supply with no pull is evidence against.

## (d) Solutions

| Project | One command | Wall-clock | Tally | Real-input result |
|---|---|---|---|---|
| `aicrawlcheck` | `python -m aicrawlcheck scan fixtures/access.log` | 0.420 s `[m]` `[fx]` 420 lines | 420 / 418 parsed / 2 unparsed; 130 verified / 25 spoofed / 25 unverifiable / 238 n-a `[fx]` | never run on a real log; none located (c1 §12) |
| `Foreman` | `python -m foreman` | 0.365 s `[m]` `[fx]` | 60 records / 52 eligible / 41 clusters / 3 repeats / 1 graduated `[fx]` | `history.jsonl` 3,103/3,103 parsed `[m]`; 1 real hook payload → `task_text: null`; moment never occurred |
| `parity-vi` | `python parity.py diff --baseline … --candidate …` | 28 s – 52 m 06 s per 600-prompt run `[m]`; 1.312 s demo `[fx]` | 5 guardrails × 600; Granite 3.0→3.1 gap 25.5 → 28.5 pp, +21 net VI misses, exit 1 `[m]` | 5 open-weights guardrails 2026-09-18; 0 commercial endpoints |

| Project | Proven — reproduced from clean or run on real input | Asserted — spec, page or vision only |
|---|---|---|
| `aicrawlcheck` | fixture tally; 418/418 page-JS vs CLI; 637 prefixes byte-identical; 0 sockets on default path; 5/5 RFC 5737 spoofs caught `[fx]`; rDNS 20 addresses `[m]` | "155 hits claim an identity" (180); Amazonbot "no range file" (1,292 `[v]`); "`--verify-dns` does not launder a false claim" — falsified; "18/18 tests" = 18 assertions, 0 test functions |
| `Foreman` | deterministic 13-key tally across three implementations `[fx]`; `assert_not_global` exit 1 on constructed input; 19/19 tests; `settings.json` SHA-256 unchanged | a real fortnight holds a chore ≥5× across ≥2 days; history written before `Stop` fires ("Not measured"); a live `Stop` hook fires end-to-end; the join recovers a real prompt |
| `parity-vi` | every pre-registered fixture number clean-room `[fx]`; Wilson bounds re-derived by hand; 5 real models; Granite diff exit 1 `[m]`; S1/S2/S3/S6/S7/S10 fixed failing-first, 43 tests (one agent) | `local_model` "fully offline" (S11, never provoked); `diff` "refuses cross-adapter" (name only; S18 open); "gap tracks the vendor's language claim" (post-hoc, 3 families); "about fifteen minutes" (0.6B only) |

The bug class — "X cannot happen" asserted where no test reaches the input that makes X happen — with the input named: ads `--verify-dns` certified Anthropic address `34.162.230.222` as `verified` Googlebot, exit 0, on master 2026-09-18 (the test used an RFC 5737 address that short-circuits); Foreman `_log_failure()` wrote outside the guard — constructed, fixed, 9 call sites re-verified; Foreman `task_text` "never fabricated" — no failing input constructed; parity-vi S1 indeterminacy gate — 39 misses → `Controversial` passed pre-fix, now exit 1, 13 tests; parity-vi S11 no-network — restated, `HF_HOME=$(mktemp -d)` never run; parity-vi S18 cross-family diff — Granite vs Detoxify exit 1 with +183 spurious misses, fix in stash only. The sixth the plan expected to go unnamed: ads "18/18 tests" — `tests/test_offline.py` has 0 test functions (`grep -c '^def test'` = 0 `[m]`). Product completeness is one row: no unit suite below the ads CLI; S1 unmerged (`wave10-fix-partial-2026-09-17`); no `scan --from-history`; S18 unmerged (`wave10b-s18-partial-2026-09-18`). Under the reweight none drives a verdict.

## (e) Competitors

### `aicrawlcheck`

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price |
|---|---|---|---|---|
| GoAccess | FAQ, features, release notes, issues 2026-09-18 | docs only — never run | issue search `bot crawler verify ip range`: "No results" | $0 |
| AWStats | `robots.pm` + changelog 2026-09-18 | docs only — never run | "several sorts of bots that AWStats is not able to detect" | $0 |
| Matomo DeviceDetector / Log Analytics | README 2026-09-18 / HTTP 404 | docs only / `unknown — 404` | "parses User Agents and Browser Client Hints" | $0 |
| Known Agents | pricing re-fetched 2026-09-18 | docs only | "Every call to the Known Agents API counts toward your event usage" — no import | $0 100K events / $29 1M / $299 10M |
| Cloudflare AI Crawl Control | changelog to 2026-06-16 | docs only | no historical-import entry | $0, all plans |
| `ai-crawler-intercept` / `webserer_log_analyzer` | GitHub API 2026-09-18 | not inspected | "Detect, verify, and log AI crawlers" / "Verifies crawler identity" | $0; 1★ / 0★ |
| Cloudflare Bot Management / DataDome / HUMAN | 2026-09-18 | pricing 403 / secondary only | no self-serve price published | quote-only; $1,000–5,000/mo; $3,830+/mo `[a]` |

### `Foreman`

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price |
|---|---|---|---|---|
| `/insights` (primary) | docs 2026-09-18 | docs only — `requires-main-thread` | "friction points … suggestions for using Claude Code more effectively"; no "recurring", "repeated", "suggest a skill" | $0 bundled |
| Claude Code CHANGELOG | 2.1.179 → 2.1.276, 2026-09-18 | full raw file grepped, 7,063 lines | no recurrence entry; `/loop` and cron are forward scheduling | $0 |
| Braintrust Topics (was Patterns) | GA docs 2026-09-18 | docs only | "clusters production traces … surface recurring patterns"; emits "evaluation datasets, scorers, and review queues" | free 10k scores; Pro $249/mo |
| `kenn-io/agentsview` | 2026-09-18 | not inspected — A6 FAIL | "Local-first session search, analytics, insights … for coding agents" | $0; 5,942★ |
| `coding_agent_session_search` | 2026-09-18 | not inspected — A6 FAIL | "index and search local coding agent session history across 11+ providers" | $0; 1,136★ |
| `ccusage` | stars only 2026-09-18 | not run | dollars and 5-hour blocks; no task identity | $0; 18,615★ |

### `parity-vi`

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price |
|---|---|---|---|---|
| promptfoo (primary) | 0.123.0 (2026-09-10); docs 2026-09-18 | docs only — never run | subcommands `init eval view share auth cache code-scans redteam debug` — no `compare`/`diff` | Community $0; Enterprise custom |
| SEA-HELM | `data/README.md` commit 2026-04-20 | source via `gh api`; not run | "Omitted from the safeguard category pending further checks/data cleanup" — 151 days | free, MIT |
| Azure AI Content Safety | pricing + language pages 2026-09-18 | docs only; not run | `vi` Supported, specially-trained blank; "do your own testing" | F0 $0 5,000/mo; S0 $0.38/1,000 `[a]` |
| OpenAI moderation | guide 2026-09-18 | docs only; not run | "The moderation endpoint is free to use"; no language statement | $0 |
| Llama Guard 4 | `MODEL_CARD.md` 2026-09-18 | docs only | "French, German, Hindi, Italian, Portuguese, Spanish, and Thai" | open weights |
| Lakera Guard / PyRIT | secondary 2025-10 / 1.1.0 | not inspected — A6 FAIL rows | "100+ languages" / no language fact on file | $0 10k req/mo; free |
| Qwen3Guard, Granite Guardian, Detoxify | HF revisions pinned 2026-09-18 | run first-hand, 600 prompts each | measured objects, not instrument incumbents | Apache-2.0 |

Stage-2 pulls closed the documentary half for every named free incumbent and ran none. Still not run as of 2026-09-18: GoAccess, AWStats, Matomo (docs only, up from `not inspected` on 2026-09-17); `/insights` (`requires-main-thread`); `agentsview` and `coding_agent_session_search` (not inspected — the rows that make Foreman's A6 a FAIL); promptfoo docs only; Lakera and PyRIT not inspected. Every gap above is the incumbent's own sentence or a quoted absence with braces; none is confirmed by a run. The free tier sets the floor in all three lanes (`pass4-read.md` point 3); the nearest-shaped free competitors have the lowest traction where `aicrawlcheck` sits (1★, 0★) and the highest where Foreman sits (5,942★).

## (f) Open proposals

Block form: source · pros · cons (failure mode — earliest signal) · prerequisites · kill · believe. Stop blocks match their gate block's length.

### `aicrawlcheck`

**A1 Stop and archive** — review §10. Pros: 23 h back ≈ $575 `[v]`; supply map kept (five vendors' words `[v]`, rDNS 20 `[m]`); 1★/0★ same-slot repos, 7-pt Show HN ceiling `[m]` already answer demand. Cons: closes on search-level negatives (F1) — signal it was wrong: a third party sells a paid crawler-verification audit by 2026-12-31. Prerequisites: none. Kill: n/a. Believe: 1. 0.686 replies is the true reach `[v]` 2. the map is worth more as document than probe `[oj]`.

**A2 Publish, post the rDNS finding, count asks at day 14** — `review.md`; c1 §18; absorbs open-source-and-walk. Pros: 13 h, $0, EV −$185 `[oj]`; spoof rates disagree 5× (31 / 5.7 / 17.1% `[v]`); rDNS result unpublished by anyone. Cons: attention is not pay (F5) — signal: stars, 0 paid asks by 2026-10-16; S1/S3/S6 live — signal: a reader reproduces the counterexample. Prerequisites: merge stash `wave10-fix-partial-2026-09-17` (build); fix 155→180, Amazonbot 1,292. Kill: <3 paid asks from non-authors at day 14. Believe: 1. p = 0.07 `[oj]` 2. no real log `[m]`.

**A3 Run GoAccess and AWStats; PR upstream if the gap holds** — `success-vision` §7 item 2. Pros: 1 h moves A6 UNKNOWN → PASS; "No results" (c1 §1). Cons: PR unwanted — signal: unanswered 30 days. Prerequisites: install; fixture. Kill: either tool verifies UA against IP → A6 FAIL, stop. Believe: 1. c1's negative survives a run `[oj]` 2. a PR is the whole product `[oj]`.

**A4 Pre-registered 20-org probe, 15.000.000 VND, 50% deposit** — `re-pick.md` §6; the gate. Pros: the only route closing A3 per §B3; 8 of 20 named `[m]`; under SEODO "từ 18 triệu" `[v]`; A1/A2 close en route. Cons: 20 × 3.43% = 0.686 replies `[v]` — signal: 0 at the day-3 follow-up; Hashmeta gives its "15.000.000đ" audit free `[v]` — signal: "we get this free"; founder has never sold `[m]`. Prerequisites: frozen list with channels; $11.08 domain optional. Kill: day 7 (2026-09-28) <2 deposits and <3 budget-naming replies; WEAK +5 days to 2026-10-02. Believe: 1. reply band 3.43–10.3% `[v]` 2. reply→deposit conversion `[oj]` 3. an agency pays for measurement `[oj]` 4. clinic-MCP ≤ $25/h `[rh]`.

Dismissed: **A5** free instrument + paid audit — GM 11.6%, CAC $745 > $565 ARPU (review §6). **A6** C6 answer-visibility pivot — live-engine testing barred (`market-check.md` §1); measurement priced free. **A7** open-source and walk — inside A2.

### `Foreman`

**F1 Stop, close for good** — `re-pick.md` §5 wording; review §10. Pros: 11 h back ≈ $275 `[v]`; no revenue term at any p — vision §1 "never paid anything", EV −$1,187 at p = 1.00 `[oj]`; 1,618 lines copy in 2–4 days `[oj]`; the 828 issues belong to an unbuilt product. Cons: stops before the two cheapest decisive reads — signal it was wrong: a third party ships and charges for recurrence-to-skill before 2027-03-01. Prerequisites: none. Kill: n/a. Believe: 1. free floors the lane (`cross-read.md`:46) `[oj]` 2. the vendor ships top requests within a quarter (#20636 `[m]`).

**F2 Inspect `/insights` and the two repos; let it decide** — C2 line 1; review §10. Pros: 2 h, $0; closes A6; `agentsview` 5,942★, `coding_agent_session_search` 1,136★ `[m]`. Cons: `/insights` is `requires-main-thread` — signal: not run by 2026-09-25; READMEs silent → still docs-only (F6). Prerequisites: an interactive session. Kill: any lists repeated prompts or suggests a skill → stop that day. Believe: 1. the changelog negative (7,063 lines `[v]`) holds for the report's output `[oj]`.

**F3 Count recurrence on the founder's real ledger** — build `scan --from-history` first (`success-vision` §7 item 1; c2 §15). Pros: the first denominator this project would hold; 3,103/3,103 parse `[m]`; components exist, 19/19 `[m]`. Cons: 8 build hours first `[oj]`; `display` may be pastes — signal: most records under 3 tokens; validates mechanism, not buyer (F1). Prerequisites: F2 negative; redaction reviewed. Kill: 0 clusters ≥5 across ≥2 days → stop. Believe: 1. the founder's work stands in for the persona `[oj]` 2. history-only needs no hook ordering `[oj]`.

**F4 Publish MIT, run the 14-day gate** — `re-pick.md` §5, thresholds unmoved; absorbs open-source-and-walk. Pros: 5 h, $0; stars pre-declared insufficient; cold-start comparable 8★ over four months `[m]`. Cons: p = 0.12 × 0.10 = 0.012 `[oj]`; a pass measures reach, not premise (review §7) — signal: 100 stars, 0 paid asks; no paywall (A13 FAIL). Prerequisites: F2, F3 not fatal; repo, licence, post. Kill: <100 stars OR <3 paid asks at day 14 (2026-10-02). Believe: 1. reach without Reddit `[oj]` 2. three strangers ask to pay where no tool has disclosed revenue (c2 §9) `[oj]`.

Dismissed: **F5** instrument + services — candidate E, "a different brief" (`re-pick.md` §4). **F6** voice asset only — never tested on a stranger; no research gate. **F7** open-source and walk — inside F4.

### `parity-vi`

**P1 Stop; publish once, keep as calling card** — review §10; absorbs open-source-and-walk. Pros: 8 h back ≈ $200–640 `[v]`; 0 of 5 models show the sold story `[m]`; 57.3M VND/company break-even at 100% share `[oj]`; one subcommand from promptfoo (25,180★ `[v]`); every EV negative. Cons: buyer and price rows stay empty — signal it was wrong: a VN chatbot incident or NĐ 142/2026 enforcement before 2027-03-01 (none found, c3 §12–13). Prerequisites: replace two placeholders (0.5 h). Kill: n/a. Believe: 1. the robust findings (1-in-6 no-verdict; 25.0% vs 16.3% over-blocking `[m]`) belong to one family no buyer runs `[oj]`.

**P2 One commercial-endpoint paired run, then publish** — c3 §5; `success-vision` §7 item 1(b). Pros: unpublished by anyone — no VN benchmark since 2026-09-01 `[m]`; Azure F0 / OpenAI moderation $0 `[v]`; `http_json` proven (`12811f1`). Cons: C3's rule — overlapping CIs AND no over-blocking → "no sellable story" — signal: the first commercial gap inside its CI; Vietnam-billed account `unknown` — signal: sign-up refused. Prerequisites: one account `[rh]`. Kill: gap inside CI on the endpoint the 23 run. Believe: 1. account accepted `[oj]` 2. 600 records fit F0 `[v]`.

**P3 Pre-registered HCMC 14-day gate** — `hcmc-opener-2026-09-18.md` §4; the gate. Pros: buyer one district away — 3 of 8 HCMC-HQ, CTOs named `[m]`; proximity is the parent research's strongest channel; $0; FAIL retires cleanly. Cons: 7 × 10.3% = 0.72 replies `[v]` against a bar of 3 — signal: 0 at day 3; needs a published number — signal: unpublished by 2026-09-19; field sales, which `scope.md` weighed against. Prerequisites: publish (2 h); rows 9–12 uncompiled. Kill: day 14 (2026-10-03) <1 buyer-side run or <3 written replies; WEAK +7 days to 2026-10-10. Believe: 1. warm-trigger 16.86% `[v]` in person → P(≥3 of 7) ≈ 0.10 `[oj]` 2. replies engage a number without a commercial run `[oj]` 3. clinic-MCP ≤ $80/h `[rh]`.

**P4 Free instrument + paid engagement (vision §1)** — the full commitment. Pros: the only vision whose win includes money; ceiling $13,633 = 23 × 15M VND `[oj]`. Cons: EV −$4,055 to −$17,255 at 240 h `[oj]` — signal: no price ≥30.4M VND by 2026-10-10; GM under 50% at 15M VND, 24 h (review §6); invoicing from Vietnam `unknown — not attempted`. Prerequisites: P3 PASS; buyer-stated price; MoR/KYC `[rh]`. Kill: first engagement under 30.4M VND or over 24 h. Believe: 1. a HCMC company pays ≥30.4M VND `[oj]` 2. re-runs billable `[oj]` 3. twelve weeks in person triples p `[oj]`.

Dismissed: **P5** finish stash S18 — build, context only. **P6** Vietnamese classifier — wrong skill, 10–16 weeks (`success-vision.md` §7). **P7** open-source and walk — inside P1.

### Cross-project

**X1 Stop all three; return to clinic-MCP** — review-foreman §10. Pros: 42 h back ≈ $1,050 `[v]`; 0 buyer contacts in ~55 runs `[m]`; every gate EV negative. Cons: clinic rate unmeasured — signal: no figure by 2026-10-01 (`[rh]`). Kill: n/a. Believe: 1. clinic-MCP ≥ $25/h `[rh]`.

**X2 One honest-measurement service, three tools as instruments** — `SUCCESS-VISION.md`; `cross-read.md` pattern 3. Pros: competence shown three times (5 models, 637 prefixes, 3,103 lines `[m]`); services pay at n=1 (US/EU evidence). Cons: $8k–$50k inadmissible in Vietnam (F7) — signal: first quote under 30.4M VND; selling never exercised. Prerequisites: P3's conversations as first sales calls. Kill: 0 paid engagements by 2026-12-17. Believe: 1. report-shaped work sells in HCMC at a Vietnamese price `[oj]` 2. MoR/KYC works `[rh]`.

**X3 Publish the method as reputation asset** — `SUCCESS-VISION.md`. Pros: 40/40 and 52/60 traced `[m]`; five bug-class finds. Cons: pattern 5 rests on acquired security firms, not method posts (F7) — signal: 0 inbound in 30 days. Prerequisites: 2–4 h. Kill: 0 inbound by day 30. Believe: 1. reputation converts to contracts `[oj]`.

**X4 Sequence the gates** — 70/10/20 `[oj]` as research order; specified in (h). **X5 Calling cards + contract work** — review-parity-vi §10. Pros: Upwork band $25–80/h `[v]`; ~6 h to publish `[oj]`. Cons: no client contacted; platform fees 20–30% `[a]`; SBV FX control `[a]` — signal: no contract in 30 days. Prerequisites: profile, Payoneer `[rh]`. Kill: 0 contracts by 2026-11-17. Believe: 1. calling cards convert `[oj]`.

## (g) Time estimate and difficulty

Reference class: `REPORT-PLAN.md` §8 only. Founder hours `[oj]` (§8.5). Agent-run bands carry the 8-of-55 stopped-run rate. Wall-clock is elapsed, agents concurrent; calendar days where waiting dominates.

| Proposal | Tasks | Agent-runs | Wall-clock | Founder research / conversation h | Founder build h | Cash | Difficulty | What makes it that number |
|---|---|---|---|---|---|---|---|---|
| A1 stop | 1 | [0, 0, 1] | [0, 0, 0.5] h | [0, 0, 1] | 0 | $0 | 1 | done: stop commit `f9f9a98` |
| A2 publish + post + count | 4 | [2, 4, 8] | [1, 4, 12] h + 14 d | [2, 4, 8] | [1, 3, 6] | $0–11 | 3 | publishing never done, any project; anchor "hour of hygiene" [1, 2, 6] |
| A3 GoAccess/AWStats run; PR | 2 | [1, 1, 2] | [0.5, 1, 3] h | [0.5, 1, 2] | PR [0, 0, 16] | $0 | 2 / 4 | run = class of `a241740`, new tool; no external PR ever filed |
| A4 20-org probe | 4 | [1, 2, 3] | [7, 12, 17] d | [14, 23, 45] | 0 | $11.08 | 4 | buyer conversation: none held by any pass |
| F1 stop | 1 | [0, 0, 1] | [0, 0, 0.5] h | [0, 0, 1] | 0 | $0 | 1 | done: stop commit `44156ab` |
| F2 `/insights` + two READMEs | 2 | [0, 1, 2] | [0.5, 1, 3] h | [1, 2, 4] | 0 | $0 | 2 | class of the 7,063-line changelog grep; `/insights` never run |
| F3 real-ledger count (build first) | 3 | [1, 2, 4] | [0.5, 1.5, 3] h | [1, 1, 3] | [4, 8, 16] | $0 | 1 | offline CLI subcommand with tests: 19/19 precedent |
| F4 publish + 14-day gate | 3 | [0, 1, 2] | 14 d | [2, 5, 9] | 0 | $0 | 3 | known script (`success-vision` §7 item 7); never done |
| P1 stop, publish once | 2 | [0, 1, 2] | [0.5, 1, 3] h | [1, 2, 6] | 0 | $0 | 3 | publish never done; placeholders [0.25, 0.5, 1] |
| P2 commercial endpoint run | 4 | [1, 2, 4] | [1, 3, 6] h | [1.5, 3, 7] | [0, 1, 2] | $0 (F0) | 3 | first commercial endpoint; `http_json` proven `12811f1` |
| P3 HCMC 14-day gate | 4 | [0, 1, 2] | 14 (+7) d | [5, 8, 16] | 0 | $0 | 4 | buyer conversation; 0 of 8 contacted; [2, 3, 6] each |
| P4 full commitment | ~8 | [13, 27, 54] | [6, 12, 20] wk | [100, 144, 240] | [24, 48, 96] | $60–100 | 4 | invoicing from Vietnam `unknown — not attempted` |
| X1 stop all | 0 | 0 | 0 | 0 | 0 | $0 | 1 | done: "stop all task and agents" 2026-09-18 |
| X2 measurement service | 4 | [2, 4, 8] | [2, 6, 20] h + gates | [20, 42, 80] | 0 | $0–11 | 4 | no sale, quote or invoice in any pass |
| X3 publish the method | 2 | [1, 2, 4] | [1, 3, 8] h | [2, 4, 8] | 0 | $0 | 3 | publish never done; content exists |
| X4 sequence | sum | [3, 6, 12] | 5 wk | [24, 42, 80] | [4, 8, 16] | $0–11 | 4 | max of components |
| X5 calling cards + contracts | 3 | [1, 3, 6] | [2, 6, 18] h | [3, 6, 18] | 0 | $0 | 4 | no client contacted; Upwork onboarding unattempted |

Widest bands. **P4 [100, 144, 240]**: the high case carries a native-Vietnamese corpus question (40 h) and unmeasured delivery hours (24); the sweep agent did four runs plus a doc in 86 minutes, but a report a buyer signs off has no reference row. **A4 [14, 23, 45]**: the high case is the WEAK path, three conversations at [2, 3, 6] h, the anchor the plan marks "no precedent in this repo". **F3 build [4, 8, 16]**: components exist, but two cap-stops hit this project's 14 runs and the redaction review is a new judgement. GPU rows (P2, P4) carry §8.3's 112× spread (28 s to 52 m per 600 prompts) in their run count. Blocked, excluded, floors: a real access log for A2 (`unknown — c1 §12`); a Vietnam-billed account for P2; contract and invoicing for P4, X2, X5 (`unknown — not attempted`).

## (h) Recommendation

Rank by EV at minimum commitment (`FRAMEWORK.md` "How to use" step 4), at $25/h `[v]`, cash included, `[oj]` probabilities from each review §8:

| Project | Min. commitment | p(gate) | Value at gate | EV | Founder rate at EV = 0 |
|---|---|---|---|---|---|
| `Foreman` | 5 h publish gate (−$120) or 11 h verdict gate (−$275, information) | 0.012 | $440 | −$120 / −$275 | $1.06/h |
| `parity-vi` | 8 h | 0.05 | $593 | −$170 (−$610 at $80/h) | $3.71/h |
| `aicrawlcheck` | 23 h + $11 | 0.05 | $2,000 | −$486 | $3.87/h |

The order turns on one choice — Foreman's minimum commitment (5-h publish gate ranks first; the 11-h gate its review names ranks second) — and on nothing else: every EV is negative above $3.87/h, below the salary-derived $11.76–12.33/h. The 90 days buy information, not revenue.

Next 90 days, in order: P3 (8 h, $0, reads 2026-10-03) first — the only in-person channel and the only gate with a money term; F2 (2 h) in parallel — it can kill Foreman in an afternoon; A3 (1 h) the same week; F3 (11 h) only if F2 is negative; A4 (23 h, $11) only if, after P3 has read, a cold-outreach answer is still wanted. Total ≤42 founder-hours, ≤$11, by 2026-10-23. No build hour beyond F3's prerequisite. Stop signals: parity-vi 0 written replies by 2026-10-03; Foreman any incumbent listing repeated work, or 0 real clusters; ads FAIL at day 7.

Assumptions: 1. reply rates 3.43 / 4.86 / 10.3 / 16.86% — `sourced` `[v]`. 2. founder rate $25/h floor — `sourced`; clinic-MCP — `requires-human`. 3. p(gate) 0.05 / 0.012 / 0.05 — `own judgement`. 4. gate values $593 / $440 / $2,000 — `own judgement`, anchored on 15M VND. 5. five-model measurement, Granite regression — `measured`. 6. 23 named, 8 profiled, 3 HCMC-HQ — `measured`. 7. incumbents lack the feature — `sourced`, docs only. 8. 42 founder-hours exist — `own judgement`.

Flips. `parity-vi`: buyer-stated price ≥30.4M VND by 2026-10-10 → build P4; 0 replies by 2026-10-03 → stop. `Foreman`: incumbent lists repeated work → stop; ≥1 real cluster the founder recognises → F4. `aicrawlcheck`: one 7.500.000 VND deposit → reopen as a service; 0 → close. Portfolio: clinic-MCP above $80/h → X1.

Anti-bias checks. 1. Sunk cost, as amended — from `raw/` alone: P3, F2, A3 stand; A2 and F4 do not (their value is the code); A4 does not (c1 alone argues against demand). 2. Narrative fit — the "three audit instruments" story: its refutation would be a buyer saying no; nobody looked; X2 listed, not recommended. 3. §F: F1 zero humans asked, demand cells UNKNOWN; F2 braces present, none opened by this writer; F3 six instances in (d); F4 open-weights only; F5 stars only in (e); F6 0 incumbents run; F7 $8k–$50k and $1,500–$5,000 flagged as transplants; F8 no `[fx]` in (a), (b), (g); F9 laws as events only; F10 `[v]`/`[c]` inline, none sole input to (b); F11 five conflict pairs side by side; F12 dates absolute, runtimes measured or `unknown`. 4. Steelman stop — A1, F1, P1 at the length of A4, F4, P3. 5. Opportunity cost — one block in (b), applied to every EV; break-even rates given where the clinic rate is missing. Closest to failing: check 1 — A4 is last because the raw evidence alone would not propose it.

## (i) Caveats and unverified claims

| file:line | Claim | Status | Affects |
|---|---|---|---|
| `ai-ads-injection/docs/execution/e2e-test.md:415` | "`--verify-dns` does not launder a false claim" | contradicted by run on master 2026-09-18, exit 0 | (d); A10 |
| `ai-ads-injection/site/index.html:315`, `mvp-spec.md:621`, `positioning.md:15` | "155 hits claim a known crawler identity" | contradicted (180; 13.9% not 16.1%), unrepaired | (d); A2 |
| `ai-ads-injection/site/index.html:463` | Amazonbot "no published range file located" | contradicted: 1,292 prefixes, `creationTime` 2026-09-08 `[v]` | (d), (e) |
| `ai-ads-injection/docs/outcome/positioning.md` | the buyer profile | unverified, self-labelled hypothesis | (b), (c) |
| `agent-hermes-dashboard/docs/explore/claude-code-substrate.md:60`, `task-telemetry.md:12` | `Stop` hooks carry `cost`, `duration_ms` | contradicted by 3 live runs v2.1.259; uncorrected on disk | (b2) |
| `agent-hermes-dashboard/docs/design/mvp-spec.md` §"The join" | history written before `Stop` fires — "Not measured" | unverified, load-bearing | (d); A10 |
| `agent-hermes-dashboard/docs/design/mvp-spec.md` | `/insights` "emits no runnable artifact" | unverified — one docs line | (e); A6 |
| `agent-hermes-dashboard/docs/outcome/success-vision.md` §5 | gate "transfers unchanged" | unverified; a pass measures reach, not premise | (f) F4 |
| `ai-attack-defense/docs/outcome/hcmc-opener-2026-09-18.md` §1 | "about fifteen minutes on one machine" | contradicted: 52 m 06 s for 4B `[m]` | (f) P3 |
| `ai-attack-defense/docs/customers/hcmc-candidates.md` caveats | job-post vocabulary gap "is evidence for the thesis" | contradicted by F1 | (c); A1 |
| `ai-attack-defense/docs/plan/re-pick.md` §2; `market-check.md` §5 | "no decree, no high-risk list" | stale: NĐ 142/2026 eff. 2026-05-01; QĐ 33/2026 eff. 2026-08-15 `[f]` | (b2) |
| `ai-attack-defense/docs/explore/aisb-inventory.md:23` | HiddenLayer covers formats, not behaviour | MEMORY — no raw source | (b2) |
| `ai-attack-defense/docs/explore/language-gap.md:27`, `niche-and-solutions.md:127` | ViHSD = arXiv 2103.10069 | contradicted: 2103.11528; uncorrected | (b2) |
| `ai-attack-defense/docs/execution/fix-log-2026-09-18.md` | 43 tests, 0 failures | unverified — one agent, never re-run | (d) |
| `ai-attack-defense/docs/outcome/parity-report-2026-09-18.md` §0 | commercial free tiers "one sign-up away" | unverified for a Vietnam-billed account (c3 §3–4) | (f) P2 |
| `docs/findings/cross-read.md:48` | services $8k–$50k per engagement | US/EU market; inadmissible in Vietnam | (b), (f) X2 |
| `docs/markets/ai-attack-defense-services.md` | XBOW total raise $195M | CHANGED: live total >$235M | (b2) |
| `docs/markets/vietnam-sg-access.md:107` | AI Hay "founders not named" | CHANGED: names surfaced 2026-09-18 | (b2) |
| c4 §3, §14 | clinic-MCP revenue/hour; subscription tier | `requires-human`, unfilled | (b), (h) |

Standing portfolio facts, unsoftened. No buyer has been contacted by any pass in any project (`ORCHESTRATION.md` §8.4: human interventions that contacted a buyer, priced anything or moved money — 0). No commercial guardrail endpoint has been run. `/insights`, GoAccess, AWStats and Matomo have never been opened; two Foreman-shaped repos with 7,078 stars between them were found on 2026-09-18 and not opened either. The Foreman 9a review was stopped before writing, so that project has never had an outcome review; every Foreman "proven" cell rests on the build agent plus one e2e agent. Twelve agents' `STATE.md` appends were lost on 2026-09-18; `ORCHESTRATION.md` is authoritative for that span. Nothing has been published for any project; every gate's clock is unstarted.

What this report could not do. It had no web, no git, no GPU and no browser; every incumbent sentence is as C1–C3 transcribed it, and this writer opened none. It did not re-run the ads counterexample, the Foreman tests, the five model runs or the 573-field page check. The audits' trace samples are hand-picked (40 root, 20 per project), weighted toward buyer, price and incumbent claims; their contradiction counts are lower bounds; the root audit's §3 and §5 disagree on the CHANGED count (3 rows vs 2). Every probability, attainable share, delivery-hour figure and founder-hour band is `own judgement` with its anchor named — all the money assumptions are of that kind, as the plan's §4 predicts. The FX rate is 2026-07-27, not 2026-09-18. The clinic-MCP rate, the input §B14 prefers, is unfilled; every EV in (h) is conditional on it sitting at or below the Upwork floor. Two `requires-main-thread` items (`/insights`, a live `Stop` hook) and three `requires-human` KILL lines (20-org deposits, the 14-day gates, a buyer-stated price) remain unrun; nothing above infers around them. C3 ran two read-only git commands against its brief and disclosed it. This section is longer than (h).

## (j) Sources

| Path | What it supplied | Date | Label kind |
|---|---|---|---|
| `projects/investment-review/raw/c1-aicrawlcheck-pulls-2026-09-18.md` | incumbent absences (GoAccess, AWStats, Matomo, Known Agents, Cloudflare); W3Techs 25.8%; repo stars; HN 305/228, 74 Show HN, 7 pts; spoof rates 31 / 5.7 / 17.1%; Amazonbot 1,292; VN agency prices; 1,640 lines | 2026-09-18 | `[v]` `[a]` `[m]` `[oj]` |
| `projects/investment-review/raw/c2-foreman-pulls-2026-09-18.md` | `/insights` docs; changelog 2.1.179–2.1.276; Braintrust Topics $249; ccusage 18,615, session-budget 8★; SessionWatcher/CrewTower prices; consumer terms; Agent SDK pause; agentsview 5,942★, session_search 1,136★; 1,618 lines | 2026-09-18 | `[v]` `[c]` `[f]` `[m]` `[oj]` |
| `projects/investment-review/raw/c3-parity-vi-pulls-2026-09-18.md` | 23 named companies; 0 live safety jobs; Azure F0, OpenAI $0; Llama Guard 4 languages; SEA-HELM 151 days; promptfoo subcommands; 10 vendors quote-only; NĐ 142/2026, QĐ 33/2026; 0 incidents; GPU COGS; S18 open | 2026-09-18 | `[v]` `[f]` `[m]` `[c]` `[oj]` |
| `projects/investment-review/raw/c4-cross-cutting-pulls-2026-09-18.md` | ITviec 54.9M, 37.75M; Second Talent, reco-vn bands; Upwork $25–80/h; FX 25,306 / 26,525 / 25,617; reply benchmarks; Payoneer, Polar; Law 134 dates; Claude Code Pro $20 | 2026-09-18 | `[v]` `[a]` `[f]` `[c]` `[rh]` |
| `projects/investment-review/raw/audit-root-research-2026-09-18.md` | 21 files; 40/40 TRACED; 13/2/0; label densities; no bottom-up figure; XBOW, AI Hay CHANGED | 2026-09-18 | `[m]` |
| `projects/investment-review/raw/audit-project-docs-2026-09-18.md` | 60 claims: 20/17/15 TRACED, 0/3/4 DRIFT, 0/0/1 MEMORY; re-verify 3-1-1 / 5-0-0 / 4-1-0; contradictions 3/3/3; pipeline 6/6 | 2026-09-18 | `[m]` |
| `projects/investment-review/review-aicrawlcheck-2026-09-18.md` | §1 KILL rows; §3 counterexample run; §5 ratio 0.014 / 0.027, N ≥ 589; §6 GM 11.6 / 58.4%, CAC $745; §8 EVs −$486, −$4,111, −$185; §10 | 2026-09-18 | `[m]` `[oj]` |
| `projects/investment-review/review-foreman-2026-09-18.md` | §1 KILL rows; §5 N ≥ 14,464 / 27,778; §6 CAC < $13.33; §8 p = 0.012, $440, EVs; §10 verdict 11 h | 2026-09-18 | `[m]` `[oj]` |
| `projects/investment-review/review-parity-vi-2026-09-18.md` | §1 KILL rows; §2 five-model table; §5 ratio 0.026, 57.3M break-even; §6 30.4M–97.2M GM floor; §8 EVs; §10 three-thread test, verdict 8 h | 2026-09-18 | `[m]` `[oj]` |
| `projects/investment-review/REPORT-PLAN.md` §3.3, §8 | human-task anchors; agent-runs 14 / 14 / 27; stopped 8 of 55; lane wall-clocks; GPU spread 112×; commits | 2026-09-18 | `[m]` `[oj]` |
| `projects/SUCCESS-VISION.md` | ranked recommendation; 70/10/20; "fourth product"; win conditions | 2026-09-17 | `[oj]` |
| `projects/ORCHESTRATION.md` §"Investment review" onward | stage status; review commits; reweight text | 2026-09-18 | `[m]` |
| `projects/*/docs/outcome/success-vision.md` §1, §4, §7 | gap lists; win-condition fiction; "an absence, not a workflow" | 2026-09-17/18 | `[oj]` |
| `projects/ai-ads-injection/docs/outcome/positioning.md`; `docs/plan/re-pick.md` §6 | problem statement; buyer hypothesis; pre-registered probe rule | 2026-09-17 | `[oj]` `[m]` |
| `projects/agent-hermes-dashboard/CLAUDE.md`; `docs/plan/re-pick.md` §3–5 | problem statement; 828 / 93,582; gate rule; "different brief" | 2026-09-17 | `[m]` `[oj]` |
| `projects/ai-attack-defense/docs/plan/niche-and-solutions.md` §3–4; `docs/outcome/hcmc-opener-2026-09-18.md` §4 | problem statement; wedge argued both ways; 14-day gate rule | 2026-09-17/18 | `[oj]` `[f]` |
| `docs/findings/cross-read.md:48,52`; `docs/findings/pass4-read.md:73,75` | services at n=1 (US/EU); published finding as reputation; no buyer contacted; free floors all lanes | 2026-09-16/17 | `[a]` `[oj]` |
| `docs/method/evidence-rules.md` rules 2–3 | transplanted price bands; compiled-citing-compiled | 2026-09-17 | — |
