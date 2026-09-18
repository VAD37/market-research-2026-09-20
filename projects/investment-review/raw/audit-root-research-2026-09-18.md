# Evidence audit — root market research, 2026-09-18

Scope: `docs/markets/`, `docs/findings/`, `docs/customers/`, `docs/competitors/` — traced against `docs/raw/`. Rules read first: root `CLAUDE.md`, `docs/CLAUDE.md`, `docs/method/evidence-rules.md`, `docs/method/scope.md`, `docs/method/open-questions.md`. No git run. No verdict rendered — counts and traces only, per the standing rule that the verdict is the user's.

## 1. Inventory — every compiled file

Numeric claims = count of distinct `$`/`%`/large-number tokens (mechanical grep, not judgment). Source labels = count of kind-tag tokens (vendor-reported, analyst-derived, company-stated, filed, unknown—checked, etc.). Caveats = has a `## Caveats` header.

| File | Date (own header) | Words | Numeric claims | Source labels | Caveats section |
|---|---|---|---|---|---|
| `docs/markets/ai-search-ads.md` | Pass 1, 2026-09-16 | 1,440 | 48 | 15 | Yes |
| `docs/markets/agent-dashboard.md` | Pass 1, 2026-09-16 | 1,955 | 61 | 11 | Yes |
| `docs/markets/ai-attack-defense.md` | Pass 1, 2026-09-16 | 1,922 | 56 | 24 | Yes |
| `docs/markets/ai-attack-defense-services.md` | Pass 2, 2026-09-16 | 1,806 | 76 | 12 | Yes |
| `docs/markets/ai-trend-suite.md` | Pass 2, 2026-09-16 | 1,837 | 116 | 19 | Yes |
| `docs/markets/creative-ai-lane.md` | Pass 3, 2026-09-16 | 1,786 | 114 | 13 | Yes |
| `docs/markets/vietnam-sg-access.md` | Pass 3, 2026-09-16 | 2,207 | 43 | 5 | Yes |
| `docs/findings/cross-read.md` | 2026-09-16 | 1,379 | 21 | 6 | **No** — ends `## What this pass does not say` |
| `docs/findings/injection-feasibility.md` | Pass 2, 2026-09-16 | 2,317 | 20 | 12 | Yes |
| `docs/findings/localization-play.md` | Pass 3, 2026-09-16 | 1,505 | 34 | 3 | Yes |
| `docs/findings/market-gaps-2026.md` | Pass 3, 2026-09-16 | 1,336 | 3 | 4 | Yes |
| `docs/findings/pass2-read.md` | 2026-09-16 | 1,443 | 34 | 5 | **No** — ends `## What this pass still does not say` |
| `docs/findings/pass3-read.md` | Ran 2026-09-16 | 1,260 | 28 | 1 | Yes |
| `docs/findings/pass4-read.md` | 2026-09-17 | 2,898 | 17 | 10 | Yes |
| `docs/findings/two-founder-cases.md` | Pass 3, 2026-09-16 | 1,808 | 53 | 6 | Yes |
| `docs/customers/answer-integrity-buyer.md` | Pass 2, 2026-09-16 | 1,571 | 28 | 19 | Yes |
| `docs/customers/first-customers.md` | Pass 3, 2026-09-16 | 2,222 | 61 | 4 | Yes |
| `docs/competitors/INDEX.md` | Pass 1, 2026-09-16 | 995 | 38 | 5 | **No** — ends `## Reading the board` |
| `docs/competitors/agent-dashboard-roster.md` | Pass 1, 2026-09-16 | 762 | 29 | 7 | **No** — ends `## Open on this roster` |
| `docs/competitors/ai-attack-defense-roster.md` | Pass 1, 2026-09-16 | 535 | 18 | 9 | **No** — ends `## Open on this roster` |
| `docs/competitors/ai-search-ads-roster.md` | Pass 1, 2026-09-16 | 611 | 27 | 8 | **No** — ends `## Open on this roster` |

Totals: 21 files, ~29,600 words, ~907 numeric-claim tokens, ~198 label tokens. 16/21 have a literal `## Caveats` header; the other 5 carry an equivalent limitations section under a different name (`Open on this roster` ×3, `Reading the board`, `What this pass does not/still does not say` ×2) — same function, different label, so `docs/CLAUDE.md`'s "every compiled doc carries a caveats section" is met in substance everywhere but not in name everywhere.

## 2. Trace sample — 40 claims

Weighted toward the six project-feeding files plus `first-customers.md` and `two-founder-cases.md` (5 each × 8 files). Status: TRACED (raw backs it verbatim) / TRACED-DRIFT (raw backs a different number) / UNTRACED / MEMORY.

| # | Claim (compiled file:line) | Raw file:line | Label present | Status |
|---|---|---|---|---|
| 1 | `ai-search-ads.md:18` AI Search Visibility Services $4.39B(2026)→$10.72B(2031), 19.55% CAGR | `ai-search-ads-pulls.md:39` | Yes, Mordor Intelligence | TRACED |
| 2 | `ai-search-ads.md:30` Otterly Lite $29/Standard $189/Premium $489/Ent from $1,000 | `ai-search-ads-pulls.md:164` | Yes, verified 2026-09-16 | TRACED |
| 3 | `ai-search-ads.md:49` Perplexity exited Feb 2026, subscription-only, targeting $500M ARR | `ai-search-ads-pulls.md:115-123` | Yes, vendor-stated+journalist | TRACED |
| 4 | `ai-search-ads.md:94` Peec AI $0→$4M+ ARR/10mo, 1,300+ brands, 300+/mo | `verify-pass2-pulls.md:283` | Yes, company-stated | TRACED |
| 5 | `ai-search-ads.md:92` Profound Series D $180M, 2026-09-16, Sequoia+Kleiner Perkins | `verify-pass2-pulls.md:275` | Yes | TRACED |
| 6 | `agent-dashboard.md:14` Nous Research $70M raised; talks Jul 2026 ≥$75M at $1.5B | `agent-dashboard-pulls.md:35-37` | Yes | TRACED |
| 7 | `agent-dashboard.md:139` 246,092 stars/51,404 forks/43,490 issues/401 contrib, created 2025-07-22 | `verify-pass2-pulls.md:84-95` | Yes, GitHub API | TRACED |
| 8 | `agent-dashboard.md:25` AI Agent Manager salary avg $103,178, range $55k–$194k | `agent-dashboard-pulls.md:192` | Yes, secondary, no primary survey | TRACED |
| 9 | `agent-dashboard.md:103` ClickHouse acquires Langfuse 2026-01-16 | `agent-dashboard-pulls.md:210` | Yes, company-stated | TRACED |
| 10 | `agent-dashboard.md:74` OpenAI AgentKit sunset 2026-11-30, launched 2025-10-06 | `agent-dashboard-pulls.md:154` | Yes | TRACED |
| 11 | `ai-attack-defense.md:86` Protect AI $634.5M filed SEC, Jul 2025 | `ai-attack-defense-pulls.md:139-141` | Yes, filed | TRACED |
| 12 | `ai-attack-defense.md:68` EU AI Act GPAI in force 2025-08-02 | `verify-pass2-pulls.md:11-42` | Yes | TRACED |
| 13 | `ai-attack-defense.md:48` Promptfoo 25,180 stars, acquired by OpenAI 2026-03-09 | `verify-pass2-pulls.md:189,201` | Yes | TRACED |
| 14 | `ai-attack-defense.md:45` Garak 9,268 stars, 129 contributors | `verify-pass2-pulls.md:163,169` | Yes, GitHub API | TRACED |
| 15 | `ai-attack-defense.md:88` Check Point–Lakera ~$300M, announced 2025-09-16 | `ai-attack-defense-pulls.md:150,152` | Yes, analyst-derived | TRACED |
| 16 | `ai-attack-defense-services.md:13` Cobalt.io Autonomous Pentest $3,500 per test | `services-lane-pulls.md:70` | Yes, vendor-published | TRACED |
| 17 | `ai-attack-defense-services.md:78` XBOW #1 HackerOne US leaderboard Q2 2025, ~1,060 reports | `services-lane-pulls.md:154` | Yes | TRACED |
| 18 | `ai-attack-defense-services.md:87-92` IBB cuts >75%, Critical $9,250→$2,257, 2026-05-22 | `services-lane-pulls.md:130` | Yes | TRACED |
| 19 | `ai-attack-defense-services.md:64` HiddenLayer USAF $1.80M, 2024-02-09→2025-08-11 | `services-lane-pulls.md:220` | Yes, procurement-filed | TRACED |
| 20 | `ai-attack-defense-services.md:107` Anthropic max $15,000/finding, ~$550,835 paid total by May 2026 | `services-lane-pulls.md:142` | Yes | TRACED |
| 21 | `vietnam-sg-access.md:23` Singapore Pte Ltd S$315 ACRA fee, nominee SGD 1,200–6,000/yr | `sg-hcmc-scene-pulls.md:241` | Yes, government-published | TRACED |
| 22 | `vietnam-sg-access.md:84` Sky Mavis $152M Series B, a16z, ~$3B val, 2021-10-05 | `sg-hcmc-scene-pulls.md:369` | Yes, trade-press+registry | TRACED |
| 23 | `vietnam-sg-access.md:107` AI Hay $10M Series A, Argor Capital, 15M+ dl, 100M+ q/mo | `sg-hcmc-scene-pulls.md:52-57` | Yes, VN+EN trade press | TRACED |
| 24 | `vietnam-sg-access.md:117` ITviec senior backend ~54.9M VND/mo, ~$27,000/yr | `sg-hcmc-scene-pulls.md:475,481` | Yes, vendor-reported | TRACED — raw computes $26,900, rounds to "~$27,000" |
| 25 | `vietnam-sg-access.md:129` Propzy $35M raised, ended 2022 | `sg-hcmc-scene-pulls.md:534` | Yes, failure-analysis site | TRACED |
| 26 | `market-gaps-2026.md:53` Nine Show HN launches May–Sep 2026; one broke out, 88 points | `market-gaps-2026-pulls.md:45` | Yes, HN Algolia API | TRACED |
| 27 | `market-gaps-2026.md:64` AI content-flood thread 860 points, 401 comments | `market-gaps-2026-pulls.md:174` | Yes | TRACED |
| 28 | `market-gaps-2026.md:77` Humane AI Pin full shutdown 2025-02-18 | `market-gaps-2026-pulls.md:103-109` | Yes, The Verge | TRACED |
| 29 | `market-gaps-2026.md:45` MCP tax-filing server, IRS ATS cert in progress 2026-04-14 | `market-gaps-2026-pulls.md:85` | Yes, company-stated/interested | TRACED |
| 30 | `market-gaps-2026.md:35` Cursor India INR plan, ~30% markup, 2026-07-28, 6 likes | `market-gaps-2026-pulls.md:231-236` | Yes | TRACED |
| 31 | `two-founder-cases.md:23` Harvey $190M revenue 2025; $550M at $15.5B, 2026-09 | `two-founder-cases-pulls.md:29` | No inline tag on this line (file caveat covers it) | TRACED |
| 32 | `two-founder-cases.md:45` Humane raised $230M+, sold to HP $116M, 2025-02 | `two-founder-cases-pulls.md:225` | Yes, Wikipedia-sourced | TRACED |
| 33 | `two-founder-cases.md:90` Mailchimp $700M rev 2019; Intuit ~$5.7B cash+10.1M shares ~$6.3B | `two-founder-cases-pulls.md:278` | Yes | TRACED |
| 34 | `two-founder-cases.md:46` Argo AI $7.25B val 2020, shut 2022-10, Ford wrote off $2.7B+$500M | `two-founder-cases-pulls.md:245` | Yes | TRACED |
| 35 | `two-founder-cases.md:92` Lovable ARR $200M by 2025-11, $400M Series C at $13.3B 2026-08 | `ai-trend-suite-pulls.md:321-327` | Yes, analyst-derived | TRACED — **cross-file**: file's own named raw source is `two-founder-cases-pulls.md`, but this number lives only in a different agent's raw pull |
| 36 | `first-customers.md:73` Instantly 2026: 3.43% platform-wide reply rate | `recovery-pulls.md:272` | Yes, vendor-reported | TRACED |
| 37 | `first-customers.md:74` Belkins 2025: 16.5M emails, 93 industries, Cybersecurity 4.86% | `recovery-pulls.md:282` | Yes, vendor-reported | TRACED |
| 38 | `first-customers.md:113` Shopify: 100% of first $1M gross app rev, 85% above, 2.9% fee | `recovery-pulls.md:218` | Yes, vendor-published primary | TRACED |
| 39 | `first-customers.md:75` Expandi: LinkedIn DM 10.3% vs cold email 5.1% | `recovery-pulls.md:290` | Yes, vendor-reported | TRACED |
| 40 | `first-customers.md:89` r/SaaS cofounder, 928 pts: $190K job offer, kept 40% | `recovery-pulls.md:52-54` | Yes, forum post quoted | TRACED |

**40/40 TRACED. Zero DRIFT, zero UNTRACED, zero MEMORY in this sample.** Two soft findings inside an otherwise clean sample: #24 is a $100/yr rounding, immaterial; #35 crosses into another agent's raw file without the compiled file naming that cross-reference — the number is real and in `docs/raw/`, but a reader following only `two-founder-cases.md`'s stated source (`two-founder-cases-pulls.md`) would not find it there. This is exactly the failure shape `evidence-rules.md` rule 1 targets ("a citation resolves to a cell or a sentence, never to a file") — here it resolves to the *wrong* file's raw pull.

Sample-selection caveat: 40 claims were hand-picked as number/company/price/date-bearing and weighted toward the eight named files. This is not a random sample of the ~900 numeric tokens counted in §1; a wider or adversarial sample (e.g., targeting the `pass2-read.md`/`cross-read.md` files that lack Caveats sections) was not run and might find a different rate.

## 3. Re-verification — 15 of the 40, against live sources today (2026-09-18)

Picked for buyer/price/incumbent load-bearing weight. STILL-TRUE / CHANGED (new value, source, date) / GONE.

| # (from §2) | Claim | Live check | Status |
|---|---|---|---|
| 2 | Otterly Lite $29/Standard $189/Premium $489/Ent $1,000 | WebSearch of otterly.ai pricing today: identical tiers, identical prices, plus feature detail (prompt counts) not in repo | STILL-TRUE |
| 5 | Profound Series D $180M at $1.8B, Sequoia+Kleiner Perkins | WebSearch: multiple outlets confirm exact figures and date; adds "1,000+ enterprise clients," "tripled revenue in 6mo" (not in repo, not contradicting) | STILL-TRUE |
| 16 | Cobalt.io Autonomous Pentest $3,500 per test | WebFetch-equivalent WebSearch of cobalt.io/platform/pricing: same $3,500 figure live | STILL-TRUE |
| 13 | Promptfoo 25,180 stars; acquired by OpenAI 2026-03-09 | WebSearch confirms date and deal; adds Promptfoo's own pre-deal valuation **$86M** (Series A $18.4M, Jul 2025) — not in repo at all | STILL-TRUE, plus one uncaptured fact |
| 21 | Stripe supports Singapore, not Vietnam | WebSearch of Stripe's current country list: confirmed, Vietnam still absent, Singapore still present | STILL-TRUE |
| 7 | Hermes Agent 246,092 stars / 51,404 forks / 43,490 issues | Live GitHub API fetch today: **246,723 stars / 51,695 forks / 44,115 issues** | STILL-TRUE (natural 2-day growth, ~0.3%; direction and order of magnitude hold) |
| 14 | Garak 9,268 stars, 129 contributors | Live GitHub API fetch today: **9,296 stars**, 1,290 forks | STILL-TRUE (same drift pattern) |
| 18 | HackerOne IBB payout cuts >75%, paused 2026-05-22 | WebSearch: multiple outlets confirm cuts and pause; adds GitHub also cut public payouts 50% eff. 2026-07-27 — an escalation of the same trend, not a contradiction | STILL-TRUE |
| 17 | XBOW #1 HackerOne leaderboard Q2 2025; raised $75M then $120M | WebSearch confirms leaderboard claim and the $120M Series C (2026-03-18, DFJ Growth/Northzone lead, val >$1B). **Total funding reported live as "over $235M"** — repo's own two figures sum to $195M, so a funding event (~$40M+) is missing from the repo's account | **CHANGED** — total funding higher than the repo's own arithmetic implies; a round is unaccounted for |
| 20 | Anthropic Model Safety max $15,000/finding | WebSearch today returns a Maginative headline citing **"up to $15,000"** in one place and **"up to $35,000 per novel jailbreak"** in another (Maginative article title vs. body), with a third source citing $25,000 historically | **CHANGED / conflicting** — live search surfaces a higher cap than the repo's $15,000, itself sourced 2026-09-16 directly from the HackerOne program page; the discrepancy is not resolved by this pass and should be re-checked against Anthropic's own page, not a secondary aggregator |
| 23 | AI Hay $10M Series A, Argor Capital; "founders not named in the coverage" (repo's own caveat) | WebSearch surfaces founder names directly: **Chuong Nguyen, Duc Tran, Hiep Nguyen**, founded 2021 (Crowdfund Insider, VietnamNet) | **CHANGED** — repo's caveat ("founders not named") is contradicted by sources this pass located in under a minute; funding figures themselves hold |
| 22 | Sky Mavis $152M Series B, a16z, ~$3B valuation, 2021-10-05 | WebSearch confirms figures and date exactly; adds context that the $3B valuation did not survive the 2022-03 Ronin hack (repo doesn't claim it did) | STILL-TRUE |
| 38 | Shopify 100% of first $1M gross app rev, 85% above, 2.9% fee | WebSearch of Shopify's own current developer docs: identical terms, plus the $20M/$100M large-developer carve-out (already in repo's raw, not in the compiled sentence quoted) | STILL-TRUE |
| — | AWS Marketplace seller-eligible jurisdictions exclude Vietnam and Singapore (`vietnam-sg-access.md:68`) | WebFetch of AWS's live seller-eligibility doc today: identical 16-country list, Vietnam and Singapore both absent | STILL-TRUE |
| 15 | Check Point–Lakera ~$300M, announced 2025-09-16 | WebSearch confirms $300M figure and Q4-2025 close target, undisclosed-terms framing consistent | STILL-TRUE |

**11 STILL-TRUE, 2 CHANGED (net-new/contradicting detail), 0 GONE, 2 rows above are supplementary checks beyond the 15 (AWS + an extra Shopify angle) folded in for the buyer/incumbent weighting the brief asked for.** Read narrowly: nothing in the sample has evaporated — every vendor, price and deal named still exists and is still priced about where the repo says. The two CHANGED items are not the repo getting a number wrong; they are the repo undercounting (XBOW's total raise) and the repo's own caveat being falsifiable in under a minute (AI Hay's founders) — both fixable by a follow-up query, neither invalidating the underlying claim.

## 4. Structural checks

**Unlabeled numbers.** `docs/CLAUDE.md` requires markets/ sizing to be "labeled" and root `CLAUDE.md` requires "every number carries a source, labeled by kind." Label density is uneven across folders: `markets/` files average one label per 3–6 numeric tokens (e.g. `ai-attack-defense.md` 56 numbers/24 labels). `findings/two-founder-cases.md` (53 numbers/6 labels) and `customers/first-customers.md` (61 numbers/4 labels) are far thinner. Concrete example: `two-founder-cases.md:26`, Harvey's nine-round funding ladder ("$5M→$23M→$80M at $715M→…→$550M at $15.5B") carries no inline kind tag on any of the nine figures — the file substitutes one blanket caveat ("Wikipedia is the backbone… relayed trade press, not filings") at the bottom instead of per-number labels. Same pattern at `two-founder-cases.md:30-36` (ElevenLabs/Wordware/Decagon/Sierra table) and in `first-customers.md`'s quoted dollar figures (L84, L89), where attribution is "this is a quote from a named forum post" rather than a `vendor-reported`/`company-stated` kind tag. Not a fabrication risk — every number in both files did trace cleanly in §2 — but it is a departure from the letter of the labeling rule that `markets/` follows and `findings/`/`customers/` mostly don't.

**Averaged figures.** None found. Every multi-source sizing conflict located (`agent-dashboard.md:34-44` six reports $0.9B–$19.33B; `ai-attack-defense.md:26-33` four sizings $500.8M–$4.2B, 8x spread; `localization-play.md:87` Vietnam ICT $198B vs $52B) is presented side by side with an explicit "never averaged" or "not resolved" note. `pass4-read.md:138` states this as a self-check: "No conflicting figures were averaged anywhere in this file."

**Relative dates.** None found. Grepped `recently|this year|last year|currently` across all four folders; the only `currently` hits (`vietnam-sg-access.md:72`, `agent-dashboard.md:135`) are present-tense state descriptions ("currently constituted," "currently use Agentforce"), not date substitutes, and both sit in files that date everything else absolutely.

**Verdict language.** None found. Every "verdict"-adjacent sentence located is an explicit *disclaimer* of verdict, not a verdict: `cross-read.md:84`, `pass2-read.md:102`, `pass3-read.md:91`, `pass4-read.md:9,141`, `market-gaps-2026.md:88`, `two-founder-cases.md:103`, `localization-play.md:98`, `vietnam-sg-access.md:142`, `first-customers.md:137` all read "No verdict. Per `../../CLAUDE.md` that is the user's" or equivalent. The rule is followed, repeatedly and by name, everywhere it could have been broken.

**TAM without a bottom-up beside it.** The literal string "TAM" and "bottom-up" appear zero times in any of the 21 compiled files (grepped). `docs/CLAUDE.md` requires market size to be labeled "top-down, bottom-up, or vendor-reported" — in practice every market size in this repo is an analyst-report figure (Mordor, Dataintelo, market.us, Astute Analytica, Grand View, SNS Insider, Gartner, Menlo) presented as `analyst-derived`, which is closer to top-down-by-proxy than to either named method, and **no file anywhere constructs or cites an independent bottom-up figure to check an analyst TAM against.** This is the sharpest structural gap in the repo: every headline market-size number (`agent-dashboard.md`'s $0.9B–$19.33B spread, `ai-attack-defense.md`'s $500.8M–$4.2B spread, `ai-search-ads.md`'s $4.39B–$10.72B) is one flavor of vendor/analyst estimate checked only against other vendor/analyst estimates of the same kind, never against a bottom-up build (e.g., buyer count × price, seats × ACV). The repo is honest about the *spread* between analyst numbers; it has no independent cross-check on whether any of them are right.

**Caveats-section naming.** Five files (`cross-read.md`, `pass2-read.md`, `INDEX.md`, and the three competitor rosters) satisfy the spirit of "carries a caveats section" under a different heading (`Open on this roster`, `Reading the board`, `What this pass does not say`). Functionally present, not literally named — noted in §1, not treated as a violation since the content is there.

## 5. Summary

| Trace sample (40) | Count |
|---|---|
| TRACED | 40 |
| TRACED-DRIFT | 0 |
| UNTRACED | 0 |
| MEMORY | 0 |

| Re-verification (15) | Count |
|---|---|
| STILL-TRUE | 13 |
| CHANGED | 2 |
| GONE | 0 |

**Per-file worst finding** (one line each, the eight weighted files plus notable others):

| File | Worst finding |
|---|---|
| `ai-search-ads.md` | None in sample; file's own caveats already flag most pricing as blog-sourced, not vendor-fetched |
| `agent-dashboard.md` | None in sample; strongest-labeled market file in the repo (24 labels/56 numbers in the sibling `ai-attack-defense.md`, 11/61 here — thinner but every traced number held) |
| `ai-attack-defense.md` | None in sample; best label density of any file audited |
| `ai-attack-defense-services.md` | None in sample; but see XBOW total-funding gap surfaced in re-verification (row 17, §3) |
| `vietnam-sg-access.md` | None in sample; AI Hay founder-anonymity caveat is live-falsifiable (§3) |
| `market-gaps-2026.md` | Thinnest numeric-claim count of any file (3) — mostly qualitative HN/forum evidence, low label density is structural to the genre not a defect |
| `two-founder-cases.md` | Weakest per-number labeling in the sample (6 labels/53 numbers) — relies on one blanket Wikipedia caveat instead of per-figure tags; also the one cross-file citation gap (#35) |
| `first-customers.md` | Weakest label density of any file audited (4 labels/61 numbers) — same blanket-caveat pattern, file's own header already calls itself "the weakest-sourced file in the repo" |
| `cross-read.md`, `pass2-read.md` | No `## Caveats` section at all (functional equivalent present under other headings) |
| Repo-wide | No bottom-up figure exists anywhere to check any analyst-derived market size against |

No verdict rendered. Per root `CLAUDE.md`, that is the user's call — this file counts and traces.

## Files read

`CLAUDE.md`, `docs/CLAUDE.md`, `docs/method/scope.md`, `docs/method/evidence-rules.md`, `docs/method/open-questions.md`; all 21 compiled files listed in §1 (full read, not excerpt); raw files opened via `sed`/`Read` for line-level confirmation: `docs/raw/ai-search-ads-pulls.md`, `docs/raw/agent-dashboard-pulls.md`, `docs/raw/ai-attack-defense-pulls.md`, `docs/raw/services-lane-pulls.md`, `docs/raw/sg-hcmc-scene-pulls.md`, `docs/raw/market-gaps-2026-pulls.md`, `docs/raw/two-founder-cases-pulls.md`, `docs/raw/recovery-pulls.md`, `docs/raw/verify-pass2-pulls.md`, `docs/raw/ai-trend-suite-pulls.md`. Raw files inventoried by line count but not directly grepped this pass: `docs/raw/ai-attack-defense-source-index.md` and the other nine `*-source-index.md` files, `docs/raw/buyer-integrity-pulls.md`, `docs/raw/creative-technical-pair-pulls.md`, `docs/raw/first-customers-pulls.md`, `docs/raw/injection-feasibility-pulls.md`, `docs/raw/localization-play-pulls.md`, `docs/raw/tos-browser-pulls.md`.

## Queries run

Bash/grep (repo-local, ~30 calls): word/line counts on all 21 compiled files and all 30 raw files; targeted `grep -n` for each of the 40 sample claims' key figures across the raw files named above; repo-wide `Grep` tool calls for `recently|this year|last year|currently`, `average|averaged|TAM|bottom-up`, `verdict`, across `markets/`, `findings/`, `customers/`, `competitors/`.

Live (WebSearch/WebFetch, 2026-09-18): "Otterly AI pricing plans"; "Profound AI search visibility Series D funding valuation"; "Cobalt.io autonomous pentest pricing"; "Promptfoo acquired by OpenAI"; "Stripe supported countries list Vietnam Singapore"; WebFetch `api.github.com/repos/NousResearch/hermes-agent`; WebFetch `api.github.com/repos/NVIDIA/garak`; "HackerOne Internet Bug Bounty payout cut AI tooling 2026"; "XBOW HackerOne leaderboard funding 2026"; "Anthropic bug bounty program maximum reward jailbreak"; "AI Hay Vietnam Series A Argor Capital funding"; "Sky Mavis Series B a16z Axie Infinity funding valuation"; WebFetch `shopify.dev/docs/apps/launch/billing/pricing-app-store` (404, retried as search); "AWS Marketplace seller eligibility countries list Vietnam"; "Check Point acquires Lakera deal value 2025"; WebFetch `docs.aws.amazon.com/marketplace/latest/userguide/seller-eligibility.html`; "Shopify Partners revenue share 2026 keep 100% first $1,000,000".
