# Evidence audit — three projects' own docs/, 2026-09-18

Scope, per user's stated priority verbatim: *"we care the most about our own docs/ and market research. not finished product completion."* Answers: for each project, how much of its compiled `docs/` (explore, plan/idea, review-against-market, design, execution, outcome, and — where present — customers) is backed by its own `raw/` or by root `docs/raw/`, and how much still holds as of today.

Method: read root `CLAUDE.md` and `projects/CLAUDE.md` first (rules below). Then, per project, ran an isolated audit pass covering inventory, a 20-claim trace sample, 5 live re-verifications, in-project contradiction search, and pipeline-completeness check. No git run. No Chrome. WebSearch/WebFetch used only for step 3 (re-verification). `prototype/` ignored except where a doc cites a measured-by-us number, in which case the cited raw/prototype output was checked to exist.

Rules applied (from root `CLAUDE.md` / `projects/CLAUDE.md`):
- Compiled claims trace to a file in the project's own `raw/` or root `docs/raw/` — never memory.
- Every number carries a source label: vendor-reported / analyst-derived / filed / company-stated / measured-by-us.
- Dates absolute. Conflicting figures sit side by side, attributed, never averaged. Every compiled doc carries a caveats section.
- Pipeline (per `projects/CLAUDE.md`): explore → idea → review-against-market → technical solution (design) → execution → outcome. Folder mapping: `docs/explore/`, `docs/plan/` (idea + re-pick), `docs/review/`, `docs/design/`, `docs/execution/`, `docs/outcome/`; `docs/customers/` (where present) treated as demand-side, explore/idea stage.
- Review-against-market must cite root `docs/markets/` / `docs/findings/` **by name**, not assert generically.

Root `docs/raw/` (32 files) and `docs/markets/` (7) / `docs/findings/` (8) / `docs/customers/` (2) / `docs/competitors/` (4) enumerated and used as the citation-check universe; see file list at end.

---

## ai-ads-injection

### 1. Inventory table

| Path | Date (source) | Words | Numeric claims (rough) | Labels present | Caveats §? | Pipeline step |
|---|---|---|---|---|---|---|
| docs/explore/carrier-state.md | 2026-09-17 | 1,696 | ~25 | 1 (company-stated) | Yes | explore |
| docs/explore/cost-and-demand-pulls.md | 2026-09-17 | 1,593 | ~35 | 7 (1 company-stated, 6 vendor-reported) | Yes | explore |
| docs/explore/detection-surface.md | 2026-09-17 | 1,247 | ~30 | 23 (2 company-stated, 18 measured-by-us, 3 vendor-reported) | Yes | explore |
| docs/explore/edge-controls.md | 2026-09-17 | 1,176 | ~15 | 0 (uses "Source:" not canonical labels) | Yes | explore |
| docs/explore/policy-ceiling.md | 2026-09-17 | 1,222 | ~10 | 0 (uses "Source:") | Yes | explore |
| docs/explore/policy-ceiling-addendum.md | 2026-09-17 | 4,165 | ~40 | 0 (uses "Pulled:") | Yes | explore |
| docs/explore/who-sells-this.md | 2026-09-17 | 720 | ~8 | 0 | Yes | explore |
| docs/plan/idea-set.md | 2026-09-17 | 4,451 | ~45 | 7 (5 company-stated, 2 filed) | Yes | idea |
| docs/plan/re-pick.md | 2026-09-17 | 3,584 | ~35 | 6 (1 analyst-derived, 2 company-stated, 1 filed, 2 vendor-reported) | Yes | idea |
| docs/review/market-check.md | 2026-09-17 | 4,501 | ~45 | 0 (non-canonical "vendor-stated"/"aggregator-stated") | Yes | review-against-market |
| docs/design/mvp-spec.md | 2026-09-17 | 8,264 | ~70 | 21 (1 company-stated, 12 measured-by-us, 8 vendor-reported) | Yes | design |
| docs/execution/build-log.md | 2026-09-17 | 3,343 | ~40 | 10 (9 measured-by-us, 1 vendor-reported) | Yes | execution |
| docs/execution/e2e-test.md | 2026-09-17 | 5,595 | ~50 | 9 (4 measured-by-us, 5 vendor-reported) | Yes | execution |
| docs/outcome/positioning.md | 2026-09-17 | 1,291 | ~15 | 3 (1 measured-by-us, 2 vendor-reported) | Yes | outcome |
| docs/outcome/review.md | 2026-09-17 | 5,969 | ~55 | 4 (1 measured-by-us, 3 vendor-reported) | Yes | outcome |
| docs/outcome/success-vision.md | 2026-09-17 | 2,345 | ~20 | 5 (1 measured-by-us, 4 vendor-reported) | Yes | outcome |

All 16 files carry `## Caveats`; all dates self-declared 2026-09-17, matching mtimes. Label-vocabulary gap: `edge-controls.md`, `policy-ceiling.md`, `policy-ceiling-addendum.md`, `who-sells-this.md`, `market-check.md` source rigorously (URLs, dates, quotes) but skip the 5 canonical kind-words.

### 2. Trace sample — 20 claims

| # | Claim (≤25 words) | File:line | Backing raw file:line | Label | Verdict |
|---|---|---|---|---|---|
| 1 | OAI-AdsBot IP-range file has 2 prefixes only, smallest range found | explore/detection-surface.md:12 | raw/oai-adsbot.json:5,8 | absent | TRACED |
| 2 | Anthropic combined bots.json: 26 prefixes, creationTime 2026-08-18T23:56:36Z | explore/carrier-state.md:23 | raw/anthropic-bots.json:2-3 | absent | TRACED |
| 3 | Cloudflare/Perplexity: undeclared crawler 3-6M daily req vs 20-25M declared | explore/detection-surface.md:36 | root docs/raw/injection-feasibility-pulls.md:150 | absent | TRACED |
| 4 | One-time GEO audit priced $1,500-$5,000 | plan/idea-set.md:54 | root docs/raw/buyer-integrity-pulls.md:268 | aggregator (via docs/customers/answer-integrity-buyer.md:85) | TRACED |
| 5 | SEODO GEO Basic priced "từ 18 triệu" VND | explore/cost-and-demand-pulls.md:60 | raw/vietnam-ai-visibility-demand.md:44 | vendor-reported | TRACED |
| 6 | Fast Marketing priced 32-65 triệu/tháng, 6-12mo terms | explore/cost-and-demand-pulls.md:60 | raw/vietnam-ai-visibility-demand.md:49-52 | vendor-reported | TRACED |
| 7 | Midas priced "từ 80 triệu/tháng," 12-month package | explore/cost-and-demand-pulls.md:60 | raw/vietnam-ai-visibility-demand.md:56 | vendor-reported | TRACED |
| 8 | Cloudflare Workers free tier: 100,000 requests/day | explore/cost-and-demand-pulls.md:11 | raw/cloudflare-workers-limits-and-pricing.md:12,34 | vendor-reported | TRACED |
| 9 | Cheapest domain `.click`: first-year $1.54, renews $10.81 | explore/cost-and-demand-pulls.md:26 | raw/cloudflare-workers-limits-and-pricing.md:122 | vendor-reported | TRACED |
| 10 | OpenAI Services Agreement "Updated: Dec 1 2025 / Effective: Jan 1 2026" | explore/policy-ceiling-addendum.md:15 | raw/openai-services-agreement.txt:1 | absent | TRACED |
| 11 | VN Luật 75/2025/QH15 passed 2025-06-16, effective 2026-01-01 | explore/policy-ceiling-addendum.md:223 | raw/vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt:4 | absent | TRACED, re-verified §3 |
| 12 | Google spam policy cloaking def., "Last Updated: 2026-08-28" | explore/policy-ceiling.md:9 | root docs/raw/injection-feasibility-pulls.md:450 | vendor-reported | TRACED, re-verified §3 |
| 13 | OpenAI Ad policies page "Updated: August 10, 2026" | plan/re-pick.md:60 | raw/openai-ad-policies.txt:1 | absent | TRACED at write-time; CHANGED now (§3) |
| 14 | Perplexity API ToS "Last updated: January 23, 2026" | explore/policy-ceiling-addendum.md:74 | raw/perplexity-api-terms-of-service.txt:1 | absent | TRACED |
| 15 | Profound $96M Series C 2026-02-24 @$1B; $180M Series D 2026-09-16 @$1.8B | plan/idea-set.md:99 | root docs/raw/verify-pass2-pulls.md:269-277 (via docs/competitors/ai-search-ads-roster.md:11) | absent at idea-set.md:99 | TRACED, one hop |
| 16 | ChatGPT ads "$1B annualized run rate in under 200 days" | plan/idea-set.md:131 | root docs/raw/ai-search-ads-pulls.md:132 (labeled at docs/markets/ai-search-ads.md:50) | company-stated (upstream only) | TRACED |
| 17 | BrandShield AI Platforms Protection launched 2026-04-01, price undisclosed | plan/idea-set.md:101 | root docs/raw/buyer-integrity-pulls.md:15-20 | absent | TRACED |
| 18 | Known Agents free tier: $0/mo, 1 project, 100K events | design/mvp-spec.md:44 | raw/wave2b-crawler-analytics-competitors.md:40 | vendor-reported | TRACED |
| 19 | TopOnSeek ships free self-serve VN AI Visibility Checker, 6 pillars | review/market-check.md:80 | raw/wave2b-vn-agency-audit-and-free-tools.md:13,27,51 | absent | TRACED |
| 20 | Polar/Lemon Squeezy list Vietnam as eligible payout country (MoR route) | plan/re-pick.md:98 | raw/wave2abis-mor-seller-eligibility-vietnam.md:17,19,33 | absent | TRACED |

19/20 TRACED, 1/20 CHANGED-since-write (#13). 0 UNTRACED, 0 MEMORY.

### 3. Re-verify 5 (checked 2026-09-18)

| Claim | Source | Result |
|---|---|---|
| Google spam policy cloaking def. + AI-answer-manipulation clause | developers.google.com/search/docs/essentials/spam-policies | STILL-TRUE, "Last Updated: 2026-08-28" unchanged |
| VN Luật 75/2025/QH15: passed 2025-06-16, effective 2026-01-01 | WebSearch, thuvienphapluat.vn, luatvietnam.vn | STILL-TRUE |
| OpenAI Ad policies "Updated: August 10, 2026" | openai.com/policies/ad-policies (403 direct); WebSearch corroboration | CHANGED — live page now v1.6 (Sept 2026), was v1.5 (Aug 2026) |
| Perplexity API ToS "Last updated: January 23, 2026" | perplexity.ai (403 direct); WebSearch corroboration | STILL-TRUE, low confidence — could not directly re-fetch |
| Bing Webmaster Guidelines page unreadable (JS shell, no cloaking text) | bing.com/webmasters/help/webmaster-guidelines-30fba23a | STILL-TRUE / unchanged failure |

3 STILL-TRUE / 1 CHANGED / 1 GONE(unreachable, unchanged).

### 4. Contradictions

1. **rDNS sample 3-of-3 vs 6-of-6.** design/mvp-spec.md:623 says 3 of 3 OpenAI addrs no-PTR. outcome/positioning.md:35 corrects: raw/rdns-lookups.txt shows 6 sampled, all NXDOMAIN. **Reconciled** — positioning.md is the dated correction.
2. **C6 Vietnam demand "entirely unsourced" vs sourced same day.** plan/idea-set.md:195 claims no VN pricing pulled; explore/cost-and-demand-pulls.md:59-64 (same day) lists 8 VN agencies with prices. **Reconciled** — review/market-check.md:157-165 lays both quotes side by side, dated, rules idea-set.md's claim false at time of writing.
3. **Spoof-claim denominator 155 vs 180.** design/mvp-spec.md:621 and outcome/positioning.md:15 both say "155 hits claim a known identity, 25 outside." outcome/review.md:245-260 (finding S6) measures actual fixture at 180 matching records, only 155 with bundled range files — changes the ratio (16.1% vs 13.9%). **Not reconciled** — review.md flags it same-day but mvp-spec.md/positioning.md text unedited.

### 5. Pipeline completeness

All 6/6 present: explore (7 files), idea (idea-set, re-pick), review-against-market (market-check.md), design (mvp-spec.md), execution (build-log, e2e-test), outcome (positioning, review, success-vision).

Review-against-market cites root docs by name with quotes, not generic assertion. E.g. market-check.md:40 — *"cross-read.md's side-by-side gives ai-search-ads 'Revenue shape: Recurring SaaS, needs scale' and ai-attack-defense 'Per-engagement, works at n=1.'"* Also names/quotes docs/findings/injection-feasibility.md, docs/customers/answer-integrity-buyer.md, docs/markets/ai-attack-defense.md, docs/markets/vietnam-sg-access.md, docs/method/scope.md.

### 6. Summary

| TRACED /20 | DRIFT /20 | UNTRACED /20 | MEMORY /20 | STILL-TRUE/CHANGED/GONE /5 | Contradictions | Pipeline /6 |
|---|---|---|---|---|---|---|
| 20 | 0 | 0 | 0 | 3/1/1 | 3 (2 reconciled, 1 not) | 6 |

---

## agent-hermes-dashboard

### 1. Inventory table

| Path | Date (source) | Words | Numeric claims (rough) | Labels present | Caveats §? | Pipeline step |
|---|---|---|---|---|---|---|
| docs/explore/hermes-substrate.md | 2026-09-17 | 1,005 | 107 | 0 | Yes | explore |
| docs/explore/claude-code-substrate.md | 2026-09-17 | 1,740 | 47 | 0 | Yes | explore |
| docs/explore/control-planes.md | 2026-09-17 | 1,332 | 100 | 2 | Yes | explore |
| docs/explore/gap-pulls.md | 2026-09-17 | 1,650 | 173 | 9 | No | explore |
| docs/explore/smallbiz-blind-spots.md | 2026-09-17 | 1,146 | 78 | 2 | Yes | explore |
| docs/explore/task-telemetry.md | 2026-09-17 | 1,123 | 19 | 1 | Yes | explore |
| docs/explore/telemetry-measured.md | 2026-09-17 | 1,870 | 43 | 0 | Yes | explore |
| docs/plan/idea-set.md | 2026-09-17 | 3,739 | 173 | 1 | Yes | idea |
| docs/plan/re-pick.md | 2026-09-17 | 3,816 | 266 | 2 | Yes | idea |
| docs/review/market-check.md | 2026-09-17 | 4,590 | 464 | 1 | Yes | review-against-market |
| docs/design/mvp-spec.md | 2026-09-17 | 8,662 | 812 | 2 | Yes | design |
| docs/execution/build-log.md | 2026-09-17 | 3,367 | 542 | 0 | No | execution |
| docs/execution/e2e-test.md | 2026-09-17 | 5,324 | 650 | 0 | Yes | execution |
| docs/outcome/success-vision.md | 2026-09-17 | 2,766 | 131 | 5 | Yes | outcome |

Label count undercounts real sourcing discipline: gap-pulls.md and control-planes.md make real evidence-kind distinctions in prose without the exact canonical tokens.

### 2. Trace sample — 20 claims

| # | Claim (≤25 words) | File:line | Backing raw file:line | Label | Verdict |
|---|---|---|---|---|---|
| 1 | Hermes = NousResearch/hermes-agent, model-agnostic agent runtime, MIT license | explore/hermes-substrate.md:7,12 | raw/hermes-agent-github-2026-09-17.md:23 | absent | TRACED |
| 2 | Stars/forks/open-issues 246,296/51,513/43,690 (2026-09-17) | explore/hermes-substrate.md:17 | raw/hermes-agent-github-2026-09-17.md:16-19 | absent | TRACED |
| 3 | Latest release v0.21.3, tag v2026.9.14, published 2026-09-14 | explore/hermes-substrate.md:15 | raw/hermes-agent-github-2026-09-17.md:31-32 | absent | TRACED |
| 4 | Anthropic bars 3rd-party devs offering claude.ai login for their products | explore/claude-code-substrate.md:13 | raw/claude-code-docs-2026-09-17.md:19 | absent | TRACED |
| 5 | Context window 200,000 tokens, "not independently re-confirmed against primary-doc line" | explore/claude-code-substrate.md:43 | raw/claude-code-docs-2026-09-17.md:168 | absent | TRACED (honest unknown) |
| 6 | Stop/SubagentStop hooks carry cost/duration_ms in payload | explore/claude-code-substrate.md:60 | raw/claude-code-docs-2026-09-17.md (hooks.md ref) | absent | TRACED-DRIFT, later measured false |
| 7 | Measured: Stop/SubagentStop carry NO cost, NO duration_ms; 3 live runs, v2.1.259 | explore/telemetry-measured.md:19-22 | raw/hook-payload-measurement-2026-09-17.md:54,77,106 | absent (no "measured-by-us" token) | TRACED |
| 8 | SBI 2024: $0-1m band 54% competitor / 24% cost-plus / 21% value-based | review/market-check.md:35 | raw/2b-sbi-pricing-report-firsthand-2026-09-17.md:24 | absent | TRACED |
| 9 | SBI survey "n=760" cited as basis for the above | plan/idea-set.md:36 | corrected in market-check.md:37 → raw file:83 (true subgroup n≈82) | absent | TRACED-DRIFT, contradiction reconciled §4 |
| 10 | CrewTower governor priced $9.99 one-time — price ceiling for candidate H | plan/idea-set.md:60,78; explore/control-planes.md:34 | raw/2b-governor-already-solved-2026-09-17.md:79 ("not confirmed... unknown") | absent | TRACED-DRIFT, contradiction reconciled §4 |
| 11 | ccusage/ccusage: 18,591 stars, pushed 2026-09-17 | design/mvp-spec.md:28,62; review/market-check.md:90 | raw/2b-governor-already-solved-2026-09-17.md:23 | absent | TRACED |
| 12 | `--max-budget-usd` flag, print-mode only, needs v2.1.217+ | review/market-check.md:140 | raw/2b-governor-already-solved-2026-09-17.md:13 | absent | TRACED |
| 13 | Paddle: Vietnam absent from 28-country exclusion list — supported by omission | explore/gap-pulls.md:54 | raw/gap3-vietnam-payment-rails-2026-09-17.md:16-18 | absent | TRACED |
| 14 | Lemon Squeezy names Vietnam explicitly in bank-payout country list | explore/gap-pulls.md:55 | raw/gap3-vietnam-payment-rails-2026-09-17.md:28 | absent | TRACED, re-verified §3 |
| 15 | Wise Business VN eligibility unresolved; page 404'd | explore/gap-pulls.md:57 | raw/gap3-vietnam-payment-rails-2026-09-17.md:38 | absent | TRACED |
| 16 | Pro weekly Sonnet 4 allowance 40-80 hrs/week (2025-08-28 baseline) | explore/gap-pulls.md:36 | raw/gap2-claude-subscription-limits-2026-09-17.md:41 | present (company-stated) | TRACED |
| 17 | "usage limit" in:title = 828 of 93,582 titled issues = 0.88% | plan/re-pick.md:73; review/market-check.md:90 | raw/2abis-demand-signal-interrogation-2026-09-17.md:16,25,30 | absent | TRACED |
| 18 | Anthropic scheduled removing `claude -p` from limits 2026-06-15, then paused | review/market-check.md:163 | raw/2b-allowance-architectural-risk-2026-09-17.md:29,35,37 | absent | TRACED |
| 19 | Shopify keeps-100%-of-first-$1M rule; AWS Marketplace excludes Vietnam | plan/idea-set.md:56 | root docs/customers/first-customers.md:109,113 | absent | TRACED, one hop to compiled doc |
| 20 | Hermes contributor count 401 (2026-09-16, pass-1) | explore/hermes-substrate.md:67 | root docs/raw/agent-dashboard-pulls.md (not project's own raw/) | absent | TRACED, outside own raw/ |

### 3. Re-verify 5 (checked 2026-09-18)

| Claim | Source | Result |
|---|---|---|
| Hermes GitHub: MIT, ~246K★/~51K forks/~44K issues | api.github.com/repos/NousResearch/hermes-agent | STILL-TRUE (246,723★/51,695/44,115) |
| ccusage/ccusage 18,591 stars | api.github.com/repos/ccusage/ccusage | STILL-TRUE (18,615) |
| Claude Code weekly/5hr limits doubled May 2026, +50% weekly, no absolute figure published | WebSearch multiple 2026 sources | STILL-TRUE |
| Lemon Squeezy names Vietnam in bank-payout list | docs.lemonsqueezy.com/help/getting-started/supported-countries | STILL-TRUE |
| Shopify keeps-100%-of-first-$1M | shopify.dev docs, BetaKit | STILL-TRUE — note it's a lifetime, not annual, threshold from 2025-05-01; root doc already carries that qualifier |

5 STILL-TRUE / 0 CHANGED / 0 GONE.

### 4. Contradictions

1. **Stop/SubagentStop cost/duration_ms.** claude-code-substrate.md:60 and task-telemetry.md:12 assert fields present; telemetry-measured.md:19-22 (3 live runs, v2.1.259) finds neither field on either hook. **Reconciled** — plan/re-pick.md:7,55 says "both wrong"; review/market-check.md had flagged it contested pre-measurement.
2. **CrewTower price ceiling $9.99.** idea-set.md:60,78 and control-planes.md:34 cite it; raw/2b-governor-already-solved-2026-09-17.md:79 says "not re-confirmed... unknown," substitutes SessionWatcher comparable. **Reconciled** at review/market-check.md:148.
3. **SBI survey n=760 vs n≈82.** idea-set.md:36,72 treats 54%/21% figures as resting on n=760; market-check.md:37 shows the load-bearing subgroup is n≈82 (10.8% of 760). **Reconciled** — market-check.md §1 "1b WEAKENED," and §1c kills the underlying thesis.

### 5. Pipeline completeness

All 6/6 present and substantive — including execution (build-log.md, e2e-test.md carry real pasted terminal output, a real bug found and fixed, hash-verified proof) and outcome (success-vision.md, ranked gap list).

Review-against-market citation: market-check.md cites root docs/findings/market-gaps-2026.md by name twice with quotes (line 98: *"this is the third independent pass in this repo to fail there"*; line 224 quoting `/search.json` finding) and docs/customers/first-customers.md by name twice. It does **not** cite docs/markets/*.md directly — that grounding is carried one doc earlier, in plan/idea-set.md:32 (quoting `../../../../docs/markets/agent-dashboard.md`) and explore/gap-pulls.md:50 / task-telemetry.md:3 (`vietnam-sg-access.md`, `agent-dashboard.md`).

### 6. Summary

| TRACED /20 | DRIFT /20 | UNTRACED /20 | MEMORY /20 | STILL-TRUE/CHANGED/GONE /5 | Contradictions | Pipeline /6 |
|---|---|---|---|---|---|---|
| 17 | 3 | 0 | 0 | 5/0/0 | 3 (all reconciled) | 6 |

---

## ai-attack-defense

### 1. Inventory table

| Path | Date (source) | Words | Numeric claims (rough) | Labels present | Caveats §? | Pipeline step |
|---|---|---|---|---|---|---|
| docs/customers/hcmc-candidates.md | 2026-09-18 | 2,332 | 85 | 9 | Yes | explore/idea (demand-side) |
| docs/design/mvp-spec.md | 2026-09-17 | 10,363 | 1,009 | 14 | Yes | design |
| docs/execution/build-log.md | 2026-09-17 | 4,407 | 650 | 0 | No (mentions "caveats" in prose only) | execution |
| docs/execution/e2e-test.md | 2026-09-17 | 6,263 | 1,141 | 0 | Yes | execution |
| docs/execution/fix-log-2026-09-18.md | 2026-09-18 | 3,764 | 389 | 0 | No | execution |
| docs/execution/packaging-2026-09-18.md | 2026-09-18 | 1,925 | 77 | 0 | Yes | execution |
| docs/execution/real-run-2026-09-18.md | 2026-09-18 | 3,302 | 735 | 5 | Yes | execution |
| docs/execution/site-log-2026-09-18.md | 2026-09-18 | 4,303 | 499 | 2 | Yes | execution |
| docs/execution/sweep-2026-09-18.md | 2026-09-18 | 6,489 | 1,628 | 1 (blanket, file-level) | Yes | execution |
| docs/explore/aisb-inventory.md | 2026-09-17 | 1,495 | 66 | 0 | Yes | explore |
| docs/explore/dataset-baselines.md | 2026-09-17 | 1,997 | 126 | 0 | Yes | explore |
| docs/explore/endpoint-shapes.md | 2026-09-18 | 1,221 | 59 | 3 | Yes | explore |
| docs/explore/language-gap.md | 2026-09-17 | 930 | 48 | 0 | Yes | explore |
| docs/explore/local-assets.md | 2026-09-17 | 813 | 33 | 0 | Yes | explore |
| docs/explore/sea-compliance-triggers.md | 2026-09-17 | 1,045 | 13 | 1 | Yes | explore |
| docs/explore/seahelm-scores.md | 2026-09-18 | 926 | 113 | 3 | Yes | explore |
| docs/explore/shipping-tools.md | 2026-09-17 | 1,042 | 57 | 1 | Yes | explore |
| docs/explore/ungated-path.md | 2026-09-17 | 1,770 | 103 | 1 | Yes | explore |
| docs/outcome/hcmc-opener-2026-09-18.md | 2026-09-18 | 1,486 | 72 | 4 | Yes | outcome |
| docs/outcome/parity-report-2026-09-18.md | 2026-09-18 | 3,994 | 705 | 4 | Yes | outcome |
| docs/outcome/review.md | 2026-09-18 | 13,951 | 1,827 | 3 | No explicit heading (caveats embedded per-finding) | outcome |
| docs/outcome/success-vision.md | 2026-09-17 | 3,141 | 193 | 4 | Yes | outcome |
| docs/plan/measurement-report.md | 2026-09-18 | 6,199 | 641 | 30 | Yes | plan/idea |
| docs/plan/niche-and-solutions.md | 2026-09-17 | 4,239 | 258 | 1 | Yes | plan/idea |
| docs/plan/re-pick.md | 2026-09-17 | 3,882 | 206 | 2 | Yes | plan/idea |
| docs/review/market-check.md | 2026-09-17 | 6,026 | 442 | 5 | Yes | review-against-market |

Largest, most execution-heavy project of the three (26 docs vs 16 and 14).

### 2. Trace sample — 20 claims

| # | Claim (≤25 words) | File:line | Backing raw file:line | Label | Verdict |
|---|---|---|---|---|---|
| 1 | AI Hay: "hơn 15 triệu lượt tải... hơn 100 triệu câu hỏi/tháng", $10M Series A (Argor Capital) | customers/hcmc-candidates.md:19 | root docs/raw/sg-hcmc-scene-pulls.md:57,53 | company-stated | TRACED |
| 2 | Llama Guard 3 supports EN/FR/DE/HI/IT/PT/ES/Thai only | explore/language-gap.md:19 | raw/language-gap-pulls.md:52 | source col only | TRACED |
| 3 | ViHSD cited as arXiv 2103.10069 | plan/niche-and-solutions.md:127,145 | raw/vihsd-vitosa-pull.md via explore/dataset-baselines.md:7 shows correct ID 2103.11528 | none | TRACED-DRIFT, uncorrected |
| 4 | Nothing in SEA mandates AI red-teaming/security testing as of 2026-09-17 | plan/niche-and-solutions.md:98 | raw/sea-compliance-pulls.md (AI Verify block) | analyst-derived, implicit | TRACED, later reversed by VN Law 134/2025 (§4) |
| 5 | HiddenLayer ModelScanner covers file-format threats, not weight-level behavioral edits | explore/aisb-inventory.md:23 | none — root docs/raw/ai-attack-defense-pulls.md:338 lists formats only, says nothing about behavior | none | MEMORY — confirmed unsourced by review/market-check.md:53-59 |
| 6 | Granite Guardian 3.0-2b: EN recall 94.0%, VI recall 68.5%, gap 25.5pp | execution/sweep-2026-09-18.md:29,298-300 | raw/sweep-report-granite-3.0-2b.txt:5-7 | measured — this machine — 2026-09-18 | TRACED |
| 7 | Qwen3Guard-Gen-4B smoketest wall-clock 18.7s, 6.3-7.5GB free VRAM | execution/sweep-2026-09-18.md:635-636 | raw/sweep-smoketest-qwen3guard-4b-bf16-2026-09-18.txt:4 | measured | TRACED |
| 8 | SEA-HELM top VI Safety: Gemma 4 (31B), 72.18 [-4.25,+4.03] | outcome/parity-report-2026-09-18.md:211 | raw/seahelm-leaderboard-pulls-2026-09-18.md:70 | vendor-reported | TRACED, live re-check shows 72.42 (§3) |
| 9 | Senior VN backend dev ≈54.9M VND/mo (~$27,000/yr) | plan/niche-and-solutions.md:134 | via review/market-check.md:197 (ITviec, n=1,839) | none at source | TRACED-DRIFT — market-check corrects: >8yr band, gross, no USD rate pulled |
| 10 | fixture:v1 totals: VI-miss 39, EN-miss 24 | design/mvp-spec.md:622,778 | execution/fix-log-2026-09-18.md:136-141,249-252 shows correct EN-miss is 22 | none | TRACED-DRIFT, dated correction exists (§4) |
| 11 | VN Law on AI No.134/2025/QH15, adopted 2025-12-10, in force 2026-03-01 | review/market-check.md:171 | raw/review-buyer-trigger-pulls.md:131,161 | filed (secondary, flagged) | TRACED, re-verified §3 |
| 12 | Azure AI Content Safety `vi` row — Supported | review/market-check.md:37 | raw/review-guardrail-coverage-pulls.md:28 | vendor-reported | TRACED |
| 13 | promptfoo: 25,180 stars, MIT, acquired by OpenAI 2026-03-09 | plan/niche-and-solutions.md:170; review/market-check.md:219 | raw/shipping-tools-github-pulls.md:33; raw/review-guardrail-coverage-pulls.md:356 | none | TRACED |
| 14 | Snyk agent-scan v0.6.3, 2026-09-10, active, covers MCP tool-poisoning | plan/niche-and-solutions.md:72 | raw/shipping-tools-github-pulls.md:37 | none | TRACED |
| 15 | TPBank T'AioX runs multi-LLM router: ChatGPT, Gemini, Grok | customers/hcmc-candidates.md:22,36 | raw/buyer-profile-pulls-2026-09-18.md:252,263 | company-stated | TRACED |
| 16 | Qwen3Guard-Gen-0.6B: EN recall 91.5%, VI recall 87.8% | execution/real-run-2026-09-18.md:36 | raw/local-model-run-backup/...json:289 (cached totals, not verbatim report) | measured — this machine | TRACED, weaker backing than sibling claims |
| 17 | Detoxify multilingual: EN recall 16.5%, VI recall 1.5%, vi unsupported | execution/sweep-2026-09-18.md:31,525-526 | raw/sweep-report-detoxify.txt | measured | TRACED |
| 18 | MITRE ATLAS has no maintained interactive tool layer, no Navigator equivalent | plan/niche-and-solutions.md:56 | contradicted 31 lines later, same file (niche-and-solutions.md:87: "MITRE ships a Navigator") | none | TRACED-DRIFT, self-contradiction (§4) |
| 19 | Singapore AI Verify voluntary, no enforcement, no penalty | explore/sea-compliance-triggers.md:9 | raw/sea-compliance-pulls.md:7 | channel-labeled | TRACED |
| 20 | p-e-w/heretic (abliteration tool): 31,632 stars, pushed 2026-09-05 | review/market-check.md:65 | raw/review-checkpoint-tamper-pulls.md:69 | none | TRACED |

### 3. Re-verify 5 (checked 2026-09-18)

| Claim | Source | Result |
|---|---|---|
| Llama Guard 3 supports only EN/FR/DE/HI/IT/PT/ES/Thai | huggingface.co/meta-llama/Llama-Guard-3-8B | STILL-TRUE |
| Granite Guardian 3.1-2b "only trained/tested on English data" | huggingface.co/ibm-granite/granite-guardian-3.1-2b | STILL-TRUE |
| SEA-HELM top VI Safety: Gemma 4 (31B) at 72.18 | leaderboard.sea-lion.ai/detailed/VI | CHANGED — now 72.42, same model/source |
| VN AI Law 134/2025/QH15: adopted 2025-12-10, in force 2026-03-01 | WebSearch (Lexology, VILAF, Duane Morris) | STILL-TRUE, deadlines 2027-03-01/2027-09-01 confirmed |
| Perspective API pages never render (JS shell), VN support unknown | developers.perspectiveapi.com/s/about-the-api-faqs, .../model-cards | STILL-TRUE, still unrendered |

4 STILL-TRUE / 1 CHANGED / 0 GONE.

### 4. Contradictions

1. **fixture:v1 EN-miss 24 vs 22.** mvp-spec.md:622,778 and e2e-test.md:139,240 say 24; fix-log-2026-09-18.md:136-141,249-252 (finding S6) shows correct value 22 (2 safe-arm items miscounted). **Reconciled** — mvp-spec.md:883-885 and e2e-test.md:821-824 both carry dated correction notes, 2026-09-18.
2. **MITRE ATLAS tool-layer self-contradiction.** niche-and-solutions.md:56 ("no maintained interactive tool layer") vs :87 ("MITRE ships a Navigator") — same file. **Reconciled** — review/market-check.md:81-90 flags it explicitly, resolves WEAKENED (Navigator exists but 27 months stale).
3. **ViHSD arXiv ID 2103.10069 vs 2103.11528.** language-gap.md:27 and niche-and-solutions.md:127,145 cite wrong ID (that of UIT-ViCTSD); dataset-baselines.md:7 finds correct ID. **Not reconciled** — dataset-baselines.md:7-8,108 states both source files "still carry the wrong ID and were not edited (out of boundary)."
4. **Vbee user count 1M+ vs 2M+**, flagged in-file at customers/hcmc-candidates.md:20,52 — self-disclosed side-by-side per convention, not an independent finding.

### 5. Pipeline completeness

All 6/6 present: explore (9 files), idea (niche-and-solutions.md, re-pick.md), review-against-market (market-check.md), design (mvp-spec.md), execution (6 files), outcome (4 files).

Review-against-market cites root docs by name with quotes. market-check.md:159 — *"`../../../../docs/markets/ai-attack-defense-services.md` line 47 says vendor security questionnaires 'reportedly' ask about independent AI red teaming, and flags 'Could not confirm CSA's CAIQ has such a field: unknown — checked 2026-09-16.'"* Also names `docs/findings/pass2-read.md` and `docs/competitors/ai-attack-defense-roster.md` by path with quoted content — citation-by-name-with-quote, not generic assertion.

### 6. Summary

| TRACED /20 | DRIFT /20 | UNTRACED /20 | MEMORY /20 | STILL-TRUE/CHANGED/GONE /5 | Contradictions | Pipeline /6 |
|---|---|---|---|---|---|---|
| 15 | 4 | 0 | 1 | 4/1/0 | 3 (1 reconciled, 1 reconciled elsewhere, 1 not) | 6 |

---

## Cross-project summary

| Project | TRACED /20 | DRIFT /20 | UNTRACED /20 | MEMORY /20 | STILL-TRUE/CHANGED/GONE /5 | Contradictions | Pipeline /6 |
|---|---|---|---|---|---|---|---|
| ai-ads-injection | 20 | 0 | 0 | 0 | 3/1/1 | 3 (2 reconciled) | 6 |
| agent-hermes-dashboard | 17 | 3 | 0 | 0 | 5/0/0 | 3 (all reconciled) | 6 |
| ai-attack-defense | 15 | 4 | 0 | 1 | 4/1/0 | 3 (1 reconciled, 1 elsewhere, 1 not) | 6 |
| **Total** | **52/60** | **7/60** | **0/60** | **1/60** | **12/15, 2/15, 1/15** | 9 (7 reconciled, 1 elsewhere, 1 not) | 18/18 |

No prose verdict per instructions — numbers only. Zero UNTRACED across all 60 sampled claims; one MEMORY claim, in ai-attack-defense (explore/aisb-inventory.md:23, HiddenLayer ModelScanner behavioral-coverage claim), itself already flagged unsourced by that project's own review/market-check.md:53-59.

## Caveats

- Trace samples are 20/project, hand-picked toward buyer/problem/price/incumbent/regulation per instructions — not exhaustive; each project has hundreds of numeric claims total (see inventory word/claim counts).
- "Numeric-claim count" is a rough digit-token grep per project agent, over-counts (includes line-citation numbers like "L19"); directional only, not comparable claim-for-claim across projects since each agent used its own counting pass.
- Re-verification for 2 of 15 claims (Perplexity API ToS date, ai-ads-injection; ChatGPT Ads run-rate not independently re-checked) could not be directly re-fetched (403s on openai.com/policies and perplexity.ai) — corroborated via WebSearch secondary sources only, flagged lower-confidence in the per-project sections.
- Label-presence undercounts real sourcing discipline in agent-hermes-dashboard and parts of ai-ads-injection: several files use non-canonical but still-attributed forms ("Source:", "Pulled:", "vendor-stated") instead of the five canonical CLAUDE.md kind-words — this is a vocabulary-compliance gap, not an evidentiary one, and is called out per-file in each inventory table.
- Contradiction search was manual/grep-driven per project agent within a time budget, not exhaustive over every cross-file number pair; three found per project (9 total) is a lower bound.
- This audit itself is compiled by three isolated subagent passes (one per project) synthesized by the orchestrating agent; each subagent's queries and files read are logged below in full per the task's transparency requirement.

## Every file read

### Shared / root (read by orchestrator)
- D:\researchs\market-research\CLAUDE.md
- D:\researchs\market-research\projects\CLAUDE.md
- D:\researchs\market-research\docs\CLAUDE.md
- D:\researchs\market-research\projects\ai-ads-injection\CLAUDE.md
- D:\researchs\market-research\projects\agent-hermes-dashboard\CLAUDE.md
- D:\researchs\market-research\projects\ai-attack-defense\CLAUDE.md
- Directory listings (`find`) of: docs/raw, docs/markets, docs/findings, docs/competitors, docs/customers, docs/sources, docs/method, and each project's docs/ and raw/ trees.
- D:\researchs\market-research\projects\investment-review\raw\c1-aicrawlcheck-pulls-2026-09-18.md (header only, context check, unrelated prior work)

### ai-ads-injection (subagent)
All 16 files under `projects/ai-ads-injection/docs/` (design/mvp-spec.md, execution/{build-log,e2e-test}.md, explore/{carrier-state,cost-and-demand-pulls,detection-surface,edge-controls,policy-ceiling,policy-ceiling-addendum,who-sells-this}.md, outcome/{positioning,review,success-vision}.md, plan/{idea-set,re-pick}.md, review/market-check.md).
Raw: oai-adsbot.json, anthropic-bots.json, rdns-lookups.txt, vietnam-ai-visibility-demand.md, cloudflare-workers-limits-and-pricing.md, openai-services-agreement.txt, vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt, policy-and-edge-pulls.md, openai-ad-policies.txt, perplexity-api-terms-of-service.txt, wave2b-crawler-analytics-competitors.md, wave2b-vn-agency-audit-and-free-tools.md, wave2abis-mor-seller-eligibility-vietnam.md, ad-verification-oai-adsbot-check.md, ucpd-annex1-uk.html.
Also: prototype/aicrawlcheck/engines.py; site/index.html (existence only).
Root: docs/raw/{injection-feasibility-pulls,buyer-integrity-pulls,verify-pass2-pulls,ai-search-ads-pulls}.md; docs/customers/answer-integrity-buyer.md; docs/markets/ai-search-ads.md; docs/competitors/ai-search-ads-roster.md.

### agent-hermes-dashboard (subagent)
All 14 files under `projects/agent-hermes-dashboard/docs/` (explore/{hermes-substrate,claude-code-substrate,control-planes,gap-pulls,smallbiz-blind-spots,task-telemetry,telemetry-measured}.md, plan/{idea-set,re-pick}.md, review/market-check.md, design/mvp-spec.md, execution/{build-log,e2e-test}.md, outcome/success-vision.md).
Raw: hermes-agent-github-2026-09-17.md, 2b-price-tracker-longtail-2026-09-17.md, 2b-demand-evidence-2026-09-17.md, 2abis-demand-interrogation-2026-09-17.raw.txt, 2abis-demand-signal-interrogation-2026-09-17.md, 2b-governor-already-solved-2026-09-17.md, control-planes-pulls.md, gap3-vietnam-payment-rails-2026-09-17.md, hook-payload-measurement-2026-09-17.md, gap2-claude-subscription-limits-2026-09-17.md, 2b-allowance-architectural-risk-2026-09-17.md, claude-code-docs-2026-09-17.md, 2b-sbi-pricing-report-firsthand-2026-09-17.md.
Root: docs/customers/first-customers.md (partial).

### ai-attack-defense (subagent)
`projects/ai-attack-defense/docs/`: customers/hcmc-candidates.md; design/mvp-spec.md (partial); execution/{build-log(partial),e2e-test(partial),fix-log-2026-09-18(full),packaging-2026-09-18(partial),real-run-2026-09-18(partial),site-log-2026-09-18(partial),sweep-2026-09-18(full)}.md; explore/{aisb-inventory,dataset-baselines,language-gap,sea-compliance-triggers}.md (full), {endpoint-shapes,local-assets,seahelm-scores,shipping-tools,ungated-path}.md (partial); outcome/{hcmc-opener-2026-09-18(partial),parity-report-2026-09-18(full),review.md(grep),success-vision.md(grep)}; plan/{measurement-report.md(grep),niche-and-solutions.md(full),re-pick.md(partial)}; review/market-check.md (full).
Raw (partial/grep): language-gap-pulls.md, buyer-profile-pulls-2026-09-18.md, sweep-report-granite-3.0-2b.txt, sweep-diff-granite-3.0-to-3.1.txt, sweep-run-granite-3.0-2b-stdout.txt, sweep-smoketest-qwen3guard-4b-bf16-2026-09-18.txt, seahelm-leaderboard-pulls-2026-09-18.md, sea-compliance-pulls.md, review-buyer-trigger-pulls.md, review-guardrail-coverage-pulls.md, shipping-tools-github-pulls.md, review-checkpoint-tamper-pulls.md, local-model-run-2026-09-18-stdout.txt (full, 2 lines), local-model-run-backup/20260918T023722Z-*.json (grep).
Root: docs/raw/sg-hcmc-scene-pulls.md (partial); docs/markets/ai-attack-defense.md (grep).

## Every query run

### ai-ads-injection (subagent)
Grep: label-word counts, caveat-header counts, date-pattern counts, numeric-token counts per file; targeted greps for IP prefixes, creationTime, 3-6M/20-25M, $1,500-$5,000, VND price strings, Cloudflare Workers limits, OpenAI Services Agreement dates, VN Luật dates, Google spam-policy date, OpenAI ad-policy date, Perplexity ToS date, Profound funding figures, ChatGPT ads run-rate, BrandShield launch, rDNS NXDOMAIN counts, MoR eligibility, ad-verification quotes, UCPD Annex I text, VN AI Visibility Checker tool. engines.py:95-105 inspection.
WebFetch: openai.com/policies/ad-policies/ (403), developers.google.com/search/docs/essentials/spam-policies (200), perplexity.ai/hub/legal/perplexity-api-terms-of-service (403), bing.com/webmasters/help/webmaster-guidelines-30fba23a (no body).
WebSearch: "Vietnam Luật số 75/2025/QH15... Điều 23 hiệu lực 2026"; OpenAI ad-policies update-date search; Perplexity API ToS last-updated search; "openai.com/policies/ad-policies updated August 2026 OR September 2026".

### agent-hermes-dashboard (subagent)
Bash: `find docs raw -type f`; word/label/caveats-section counts per file; mtime per file; numeric-token counts per file; greps for Hermes stars/forks/issues, MIT license, release tags, JABB/39, 828/93582, max-budget-usd, ccusage stars, CrewTower/$9.99, Paddle/Lemon Squeezy/Vietnam, cost/duration_ms fields, subscription-hour figures, June-15 pause date, Wise, context-window figure, "third party developers" clause, SBI 760/82/10.8, docs/markets & docs/findings & docs/customers citations, evidence-label tokens. Root grep: "$1,000,000\|AWS Marketplace" in docs/customers/first-customers.md.
WebFetch: api.github.com/repos/NousResearch/hermes-agent; api.github.com/repos/ccusage/ccusage; docs.lemonsqueezy.com/help/getting-started/supported-countries; shopify.com/partners/blog/app-revenue-share (404); betakit.com Shopify revenue-share article.
WebSearch: "Claude Code subscription weekly rate limit hours 2026"; "Lemon Squeezy Vietnam supported countries payout"; Shopify $1M revenue-share search.

### ai-attack-defense (subagent)
Bash: `find docs -type f`, `find raw -type f`; per-file wc/mtime/date/numeric-token loops; caveat-heading grep; evidence-label-token grep (canonical + expanded pattern); targeted greps for Llama Guard languages, ViHSD arXiv ID, AI Hay download/revenue figures, HiddenLayer ModelScanner claim, Granite Guardian recall numbers, SEA-HELM Gemma-4 score, AI Verify voluntary status, VN AI Law dates, Azure Content Safety `vi` support, promptfoo stars/acquisition date, Snyk agent-scan version, TPBank router vendors, Qwen3Guard recall numbers, Detoxify recall numbers, MITRE ATLAS Navigator contradiction, heretic stars, fixture EN-miss 24-vs-22, ITviec salary figures.
WebFetch: huggingface.co/meta-llama/Llama-Guard-3-8B; huggingface.co/ibm-granite/granite-guardian-3.1-2b; leaderboard.sea-lion.ai/detailed/VI; developers.perspectiveapi.com/s/about-the-api-faqs; developers.perspectiveapi.com/s/about-the-api-model-cards.
WebSearch: "Vietnam Law on Artificial Intelligence 134/2025/QH15 effective date March 2026".
