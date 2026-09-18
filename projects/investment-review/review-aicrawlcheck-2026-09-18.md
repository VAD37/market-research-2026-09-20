# Investment review — `aicrawlcheck` (`projects/ai-ads-injection`)

2026-09-18. Stage 3 of `projects/investment-review/`, per `FRAMEWORK.md` §D. Sections and headings are §D's, verbatim and in order.

Evidence: `raw/c1-aicrawlcheck-pulls-2026-09-18.md` (primary), `raw/c4-cross-cutting-pulls-2026-09-18.md` (founder cost, benchmarks, comparable prices), the project's own `docs/` and `raw/`, and four runs this reviewer made on this machine 2026-09-18 (labelled `measured-by-us 2026-09-18`). No number below is introduced by this review; every one is traced to a file or to one of those four runs.

FX used throughout: **VND 26,525 = USD 1** — vendor-reported, Vietcombank selling rate 2026-07-27 via VnExpress (`c4` line 5). The rate on 2026-09-18 is `unknown — checked vietcombank.com.vn, sbv.gov.vn 2026-09-18, live widget not machine-readable`.

---

## 1. Header table

| Criterion | Number found | Source + label | Threshold (§A) | PASS / FAIL / UNKNOWN |
|---|---|---|---|---|
| A1 severity and frequency | 0 conversations held; HN top thread 305 pts / 228 comments 2026-08-12 | `ORCHESTRATION.md` §8.4 (`measured-by-us`); `c1` line 8 (`measured-by-us`) | ≥5 of 10 name it unprompted, recurs ≥monthly | **UNKNOWN** (§F1: zero humans asked ≠ FAIL) |
| A2 buyer identity and reachability | 8 agencies named; list never frozen; 0 reached | `vietnam-ai-visibility-demand.md` §2 (`measured-by-us` 2026-09-17); `re-pick.md` §6 | frozen list ≥20 named, ≥3 reached in 14 days | **FAIL** |
| **A3 KILL willingness to pay** | 0 deposits, 0 LOIs, 0 unprompted paid asks | `c1` lines 17–18 (`requires-human`; precondition unmet) | ≥1 deposit, or 1 LOI, or ≥3 unprompted asks | **UNKNOWN** — not yet measurable |
| A4 price point | No price any named buyer said or paid | `c1` lines 3, 14, 19; `vietnam-ai-visibility-demand.md` (all `vendor-reported` list prices, wrong SKU) | a number a named buyer said or paid | **FAIL** |
| A5 market size, bottom-up | ratio 0.014 (§5 arithmetic) | `vietnam-ai-visibility-demand.md`, `c4` lines 1–2 | ratio ≥1 | **FAIL** |
| **A6 KILL incumbent coverage** | 5 incumbents docs-inspected 2026-09-18; **0 run first-hand** | `c1` lines 1–4 (`vendor-reported`); `c1` line 1: "Not installed/run this pull" | every free incumbent run first-hand | **UNKNOWN** (§F6: docs-only on primaries) |
| A7 why now | HN 305-pt spoofing thread 2026-08-12; Known Agents "Active Threat" notice | `c1` line 8 (`measured-by-us`); `wave2b-crawler-analytics-competitors.md` §1e (`vendor-reported`) | one dated event ≤12 months, primary-cited | **PASS** (§F9: event, not demand) |
| A8 channel with cost | 0 contacts sent, 0 replies, all channels, all passes | `ORCHESTRATION.md` §8.4 (`measured-by-us`) | ≥1 reply obtained through a costed channel | **FAIL** |
| A9 moat and time-to-copy | 1,640 lines / 9 modules; copy 8–16 hours | `c1` line 16 (`measured-by-us` + `own judgement`); `review.md` §5 | ≥6 months, reason named | **FAIL** — honest answer is none |
| **A10 KILL real-input proof** | 0 real logs; "cannot happen" claim falsified on master today | `c1` line 12 (`unknown — checked`); this review's run (`measured-by-us 2026-09-18`) | moment occurred on ≥1 real non-team input | **FAIL** |
| A11 unit economics | GM 11.6% or 58.4% (rate-dependent); CAC `unknown` | §6 arithmetic | payback <12 mo; GM ≥70% SW / ≥50% services | **UNKNOWN** |
| A12 founder-market fit | No domain, no server, no CDN account on this machine | `raw/local-infra-check.txt` (`measured-by-us` 2026-09-17) | founder is the buyer, or 1 intro from ≥3 named | **FAIL** — founder does not own the input |
| A13 time-to-first-dollar | Stop rule dated 2026-09-17; no commitment date, no invoice | `re-pick.md` §6 | ≤90 days, date written before starting | **UNKNOWN** (weight 0) |
| A14 kill rule and opportunity cost | Rule pre-registered and dated; every EV row negative | `re-pick.md` §6; §8 below | pre-registered rule AND EV > next-best use | **FAIL** on the EV half (weight 0) |

**§E score: 3 / 100, with 5 UNKNOWNs.** Only A7 (weight 3) passes. A high score was never available; a score this low with five UNKNOWNs means the weights are not doing the work — the KILL rows are.

**Which KILL caps the verdict, and why.** Three KILL rows, none clear:

- **A10 = FAIL.** Both halves fail. The tool has never been run on a real access log (`c1` line 12: no fetchable 2025–2026 public log with confirmed AI-crawler UAs; `REPORT-PLAN.md` §8.1: "none for the product's moment"). And the "X cannot happen" claim — `e2e-test.md:415`, "**`--verify-dns` does not launder a false claim**" — has a constructed input that makes X happen, which this reviewer ran on master today (§3). A FAIL, not an UNKNOWN: the counterexample exists and executes.
- **A3 = UNKNOWN.** Not zero. `c1` line 18: the precondition (publishing the rDNS finding) has never occurred, so the count of unprompted paid asks "does not exist yet — this is not the same as a count of zero."
- **A6 = UNKNOWN.** The documentary half closed decisively in the incumbents' favour-of-this-product on 2026-09-18 (§4), but `c1` line 1 states plainly that no incumbent was installed or run. §D4's rule: docs-only on a primary incumbent is UNKNOWN.

Per §D1, a KILL at FAIL sets the ceiling to **stop**; a KILL at UNKNOWN sets it to **gate first**.

**Which of the three drives this verdict, and which is context.** A10's FAIL is a statement about the *prototype* — never run on real input, one falsified safety claim live on master. It is recorded in full (§3) because §D3 requires it, and it is **context, not a verdict driver**: this review's question is whether the project's own research gives a sound, evidenced picture of buyer, problem, price, incumbents and regulation. On that question the binding rows are **A3 (UNKNOWN)** and **A6 (UNKNOWN)**, joined by A2 and A4 at FAIL — all five are research and buyer-evidence rows, and none of them is closed or closeable by writing code. Two KILLs at UNKNOWN set the ceiling at **gate first**, and §2b says which gate. A10 would matter to the verdict only in the world where buyer, price and incumbent were already evidenced; they are not, so the prototype's state changes nothing about what to do next.

---

## 2. What the MVP does today (measured)

| | Value | Label |
|---|---|---|
| One command | `python -m aicrawlcheck scan fixtures/access.log` | — |
| Wall-clock, this reviewer | **0.420 s**, 420-line **fixture** | `measured-by-us 2026-09-18`, Python 3.9.25 |
| Wall-clock, `selftest` | **0.799 s**, exit 0 | `measured-by-us 2026-09-18` |
| Wall-clock on file | 0.936 s cold; 0.391–0.417 s warm, 420 lines, **fixture** | `REPORT-PLAN.md` §8.1, `measured-by-us` |
| Tally | 420 lines / 418 parsed / 2 unparsed; 130 verified / 25 spoofed / 25 unverifiable / 238 n-a — **fixture** | reproduced by this reviewer 2026-09-18; matches `e2e-test.md` §2 and `review.md` §1 |
| Verification bundle | 489 IPv4 + 148 IPv6 = 637 prefixes, 9 vendor files, copied 2026-09-17 | `measured-by-us`, printed by the run above |
| Cross-implementation check | 418/418 Python-CLI vs page-JS agreement, 0 diffs, evidence strings character-identical — **fixture input, real property** | `review.md` §1, reproduced independently under Node v23.11.1 |
| Adversarial fixture | 5 of 5 spoofed claims caught from RFC 5737 addresses, 0 false `verified` — **fixture** | `e2e-test.md` §7a |
| Offline proof | 4 socket entry points stubbed, scan completes — **fixture** | `tests/test_offline.py`, re-run in `review.md` §1 |
| Acceptance | 24 of 31 PASS; 7 NOT COVERED (browser items 20–28) | `e2e-test.md` §13 |
| **Real-input result** | **none.** Never run on a real production access log | `c1` line 12; `success-vision.md` §2 "On their own traffic. Missed." |

No `real-run-*.md` file exists for this project. The one thing this review ran on non-fixture input was the S1 counterexample (§3), which is a constructed adversarial line, not a real log.

**This whole section is context.** Product completeness — the missing unit suite, the unmerged stash, the absent real-log run — is one row of this review, not its spine. What follows in §2b is.

---

## 2b. Research quality — does the project's own `docs/` carry a sound, evidenced picture?

The question this review is actually deciding. For each of the five things the research had to establish: the strongest claim the docs make, its source kind, what the 2026-09-18 C1 pull did to it, and what **research or conversation** — never code — would close it.

| | Strongest claim in the docs | Source kind | C1 pull, 2026-09-18 | What would close it (research only) |
|---|---|---|---|---|
| **Buyer** | `positioning.md`: "a developer or site owner with `/var/log/nginx/access.log` on a box that is not behind Cloudflare" — the doc itself labels it "a hypothesis, not a finding" | `own judgement`; 0 humans asked, any pass | **could not check.** Line 17 `requires-human`; line 18's precondition (publication) unmet, so the count "does not exist yet" | Freeze `re-pick.md` §6's 20-organisation list with a channel each, hold 3 conversations. Nothing else closes it |
| **Buyer population** | `market-check.md` §5: origin instrumentation is free twice over, so the addressable set is whoever is *not* on Cloudflare | `vendor-reported` | **confirmed as a share, not a count** — Cloudflare 25.8% of all websites, so ~74.2% off it (`analyst-derived`, W3Techs); top-1M breakout `unknown — checked 2026-09-18` | A directory, register or crawl yielding named entities. A percentage cannot become an `N_buyers` (§B5) |
| **Problem** | `mvp-spec.md` "The user" — three questions they cannot answer by eye; against `review.md` §5's own counter, "It answers a question people ask once" | `own judgement`, both sides | **confirmed as attention, contradicted as a paid job.** Complaint threads are large — 305 pts / 228 comments on ClaudeBot spoofing 2026-08-12; 714 pts Nepenthes; 607 pts Amazon crawler. But 74 Show HN launches in this exact category since 2025-01-01, best genuine one **7 points** (all `measured-by-us`) | Read the 228 comments and count how many describe the *verification* problem versus the *bandwidth* problem — a thread read, not a build. Then A1's 10 conversations |
| **Price** | `re-pick.md` §4: four published VND price lists — SEODO từ 18tr / 200tr / 350tr; Fast Marketing 32 / 45 / 65tr per tháng; Midas từ 80tr/tháng; TopOnSeek quote-only | `vendor-reported` | **confirmed and extended.** Line 19 closed the four unfetched agencies: Hashmeta GEO Premium 60tr+/tháng plus an "AI Visibility Audit **trị giá 15.000.000đ**" given away **free**; Nextop bundles GEO with no separate price; `seo.danang.vn` is a generic SEO shop, 80tr/dự án, **no GEO offering at all**. Line 14: **no paid bot-management vendor publishes a self-serve entry price** — only Known Agents' $0 is vendor-published | One price a named buyer quoted or paid. Every figure on file prices a *different SKU* (optimisation), and the one thing priced as measurement is a free lead magnet |
| **Incumbent** | `mvp-spec.md` "Why not the free option", last row: GoAccess / AWStats / Matomo `unknown — no pass in this project has checked` — an admitted hole standing since 2026-09-17 | `unknown`, honestly flagged | **confirmed, in the incumbents' own words — the pass's biggest research gain.** GoAccess: no such feature in FAQ, features, release-notes or issues ("No results"). AWStats `robots.pm` is UA-regex only, its own doc comment quoted. Matomo DeviceDetector parses UA strings only. Known Agents has no log import. Cloudflare AI Crawl Control has no historical import in its changelog | One hour: install GoAccess, run it on `fixtures/access.log`, paste the output. That converts A6 UNKNOWN → PASS |
| **Regulation** | `market-check.md` §4: measurement is not *quảng cáo* under Điều 2.1, so Luật Quảng cáo does not reach it; only Điều 23.3(a) tax registration attaches. `policy-ceiling.md`: Google cloaking policy and UCPD Annex I item 11 reach only the killed differential-serving branch | `filed`, from statute text pulled wave 1b/2b; translations uncertified | **not checked** — no C1 line touches law. `c4` line 16 confirms Law 134/2025/QH15 in force 2026-03-01, compliance 2027-03-01 and 2027-09-01 (`filed`), and it does not reach this product either | Điều 15a and the Điều 23.8 implementing decree, both still unread (`market-check.md` caveats). **Low value** — no §1 row rests on regulation, and §F9 bars it from A3/A5 anyway |

**The read, stated once.** Three of the five cells — price, incumbent, regulation — are genuinely well-evidenced in this project's own docs, primary-sourced, and survived a fresh adversarial pull. The incumbent cell in particular went from an admitted `unknown` to a documented capability gap quoted in five vendors' own words, and it is the criterion (`A6`) that had killed every previous asset claim here. **Two cells — who the buyer is, and whether the problem is a paid job — are not evidenced at all, and no amount of further desk research can close them.** Every negative on file about demand is a search-level or landing-page-level negative (§F1), and `c1` added two more: the two same-slot GitHub repos at 1 and 0 stars, which is independent supply with no pull, and the 7-point ceiling on Show HN launches in this category. The research is not thin; it is **complete on the supply side and empty on the demand side**, and it has been that way for four waves. That asymmetry, not the prototype, is what the verdict has to answer.

---

## 3. Proven vs asserted

| Proven — reproduced from clean, or run | Asserted — spec, page or vision doc only |
|---|---|
| Fixture tally 420/418/2, 130/25/25/238 (`measured-by-us 2026-09-18`) | "155 hits claim a known crawler identity" — actual 180 (S6, unrepaired) |
| 418/418 page-JS vs CLI, 0 diffs, evidence strings identical | "Actual terminal output" block — hand-edited 2/+23 vs 10/+15 (S3, unrepaired) |
| 637 prefixes, 9 files, byte-identical to `raw/` (`cmp` 9/9) | "No published range file located" for Amazonbot — 1,292 prefixes exist (S2) |
| Zero network on the default path, 4 sockets stubbed | Meta/Amazonbot/Bytespider "return `unverifiable`, never `verified`" — they return `unknown`; Applebot returns `human` (S5) |
| 5/5 RFC 5737 spoofs caught, 0 false `verified` — fixture | "`--verify-dns` does not launder a false claim" — **falsified, §D3 check below** |
| rDNS: 20 addresses sampled, arithmetic exact against `raw/rdns-lookups.txt` | The buyer — `positioning.md` labels it a hypothesis; 0 humans asked |
| `refresh --dry-run` reached live network, 9/9 unchanged, 5.668 s | `success-vision.md` §1 win condition — every count invented, doc says so |
| 1,640 lines / 9 modules (`c1` line 16, local `wc -l` 2026-09-18) | "18/18 tests" — see below |

**"18/18" is not tests.** Read from code, not docs: `cli.py cmd_selftest` builds 7 top-level counts + 8 by-purpose rows + 2 finding counts + 1 bundle-prefix check = **18 assertions over one fixture**, its own comment saying so. `tests/test_offline.py` contains **0 test functions** (`grep -c '^def test'` = 0; no `unittest`, no `pytest` import) — it is one script with a `main()`. `REPORT-PLAN.md` §8.1 records the same: "**no unit suite below CLI**". Any sentence reading "18/18 tests" overstates the test estate by the whole of it.

**Bug-class check (§F3) — for each "X cannot happen", the input that makes X happen.**

Claim: `e2e-test.md:415` — "**`--verify-dns` does not launder a false claim**."
Input constructed: source IP `34.162.230.222` — an **Anthropic** crawler address taken from this project's own `raw/rdns-lookups.txt` — carrying UA `Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`.
Run on master, `measured-by-us 2026-09-18`:

```
$ python -m aicrawlcheck scan /tmp/fake.log --format combined --verify-dns --out csv
1,...,34.162.230.222,...,google.googlebot,Google,Googlebot,classic-search,verified,fcrdns,
  34.162.230.222 -> 222.230.162.34.bc.googleusercontent.com -> 34.162.230.222 (forward-confirmed reverse DNS)
exit=0
```

Does a test reach it? **No.** The only case `e2e-test.md` §7a tested was an RFC 5737 documentation address, which has no PTR record and short-circuits at step 1 before the suffix list is consulted. The test passed for the wrong reason and certified the bug.

Is it fixed? **No, not on master.** `engines.py` still carries `(".googlebot.com", ".google.com", ".googleusercontent.com")` on the `google.googlebot` rule, and `verify.py` still returns `verified` on an FCrDNS pass. The wave-10 partial fix exists only in the stash: `.git/logs/refs/stash` holds **one** entry, `b63790c5… On master: wave10-fix-partial-2026-09-17` — matching `STATE.md`'s last entry, "12 prototype files modified (388+/67-)… cut by session end… stashed." The product's one sentence is that it does not believe a user-agent string; on master, under the flag it advertises, against an address from its own evidence file, it believes one.

---

## 4. Incumbent gap, in the incumbent's words

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price |
|---|---|---|---|---|
| GoAccess | FAQ, features, release-notes, issues, 2026-09-18 | **docs only — never run** | Zero issue matches for `bot crawler verify ip range`: "No results" | $0 (OSS) |
| AWStats | `robots.pm` source + changelog, 2026-09-18 | **docs only — never run** | "There are several sorts of bots that AWStats is not able to detect" | $0 (OSS) |
| Matomo DeviceDetector | README, 2026-09-18 | **docs only — never run** | "parses User Agents and Browser Client Hints"; no IP verification | $0 (OSS) |
| Matomo Log Analytics | matomo.org/docs/log-analytics, 2026-09-18 | **HTTP 404** | `unknown — checked 2026-09-18, 404` | $0 (OSS) |
| Known Agents (ex-Dark Visitors) | knownagents.com/pricing, re-fetched 2026-09-18 | docs only | "Every call to the Known Agents API counts toward your event usage" — no import | $0 / $29 / $299 / custom |
| Cloudflare AI Crawl Control | changelog to 2026-06-16; overview stamp 2026-08-14 | docs only | No historical-log-import entry in the changelog | $0, "Available on all plans" |
| `Unsourced-Founder/ai-crawler-intercept` | 1 star, last push 2026-08-07 | GitHub API, 2026-09-18 | "Detect, verify, and log AI crawlers at the edge — no blocking" | $0 |
| `evemilano/webserer_log_analyzer` | 0 stars, last push 2026-09-02 | GitHub API, 2026-09-18 | "nginx access-log analyzer… **Verifies crawler identity**" | $0 |
| Cloudflare Bot Management | 2026-09-18 | pricing page HTTP 403 | No self-serve price published by the vendor | quote-only; $1,000–5,000/mo est. (`analyst-derived`, secondary) |
| DataDome | 2026-09-18 | secondary aggregators only | No price on datadome.com | $3,830 / $8,670 / $10,160 per mo (`analyst-derived`, secondary) |
| HUMAN Security | 2026-09-18 | secondary only | "no pricing published on its website as of 2026" | quote-only |

**The gap is real and it is stated in the incumbents' own words.** No incumbent verifies a claimed crawler UA against published IP ranges, and none imports an access log the operator already has — confirmed 2026-09-18 against GoAccess's FAQ and issue tracker, AWStats' own `robots.pm` doc comment, DeviceDetector's README, Known Agents' pricing FAQ and Cloudflare's changelog. That is the criterion which killed every prior asset claim in this project (`market-check.md` §5), and it is the one row that moved in the product's favour this pass.

**It is still A6 UNKNOWN, not PASS**, for one reason: `c1` line 1 says "Not installed/run this pull… `measured-by-us` portion of this line not executed." §D4's rule is a "how inspected" column and §F6 makes docs-only on a primary an UNKNOWN. Converting it costs roughly one hour: install GoAccess, run it on `fixtures/access.log`, paste the output.

**The two same-slot repos are the other half of this table and cut the other way.** Their existence falsifies "nobody has built this" (§F2). Their star counts — **1 and 0**, against 22,512 for `TecharoHQ/anubis` and 4,126 for `ai-robots-txt/ai.robots.txt` in the adjacent blocking slot — say the slot itself, not the idea, is where demand is absent. Repeated independent supply with no pull is evidence against.

---

## 5. Bottom-up sizing, arithmetic shown

Per the instruction: built from `c1`'s counts of sites, agencies and same-slot repos. No TAM appears here; the Mordor "$4.39B (2026)" figure in `docs/markets/ai-search-ads.md` is inadmissible under §B5 and is quoted only to reject it.

```
N_buyers         = 8                     [measured-by-us count of named Vietnamese GEO/AEO agencies,
                                          raw/vietnam-ai-visibility-demand.md §2, 2026-09-17;
                                          7 named in text, "at least 8 distinct" stated by the pull.
                                          The only directory of named entities this project owns.]
ARPU             = 15,000,000 VND        [own judgement — the pre-registered probe price, re-pick.md §6,
                                          2026-09-17. Anchoring comparables, both vendor-reported:
                                          SEODO "GEO Basic — Từ 18 triệu" (2026-09-17), and Hashmeta's
                                          "AI Visibility Audit — trị giá 15.000.000đ" (2026-09-18),
                                          which Hashmeta gives away free as a lead magnet.]
attainable_share = 0.10                  [own judgement. §B5 caps this at ≤10% without distribution
                                          evidence, and there is none: 0 contacts, 0 replies, all passes.
                                          Anchoring comparable: the two same-slot repos at 1 and 0 stars
                                          (measured-by-us, GitHub API 2026-09-18) — the observed pull for
                                          this exact product shape is approximately zero.]
cycles_36mo      = 3                     [own judgement, one report per buyer per year. Generous:
                                          review.md §5 argues the job is asked once, which implies 1.]

market_36mo      = 8 × 15,000,000 × 0.10 × 3 = 36,000,000 VND  ( = USD 1,357 )

founder_cost_yr  — two comparables, side by side, never averaged (§B14 takes the higher):
  (a) salary     = 54.9M VND/mo × 12 = 658,800,000 VND/yr    [ITviec 2025-2026 report, Back-end >8 yrs
                                                              median, n=1,839, vendor-reported, c4 line 1]
  (b) contract   = USD 25/h × 2,000 h/yr = 1,326,250,000 VND [Upwork Vietnam AI band $25–$80/h,
                                                              vendor-reported via Second Talent 2026-08/09,
                                                              c4 line 2; 2,000 h/yr own judgement]
  §B14 → take (b).

ratio            = 36,000,000 / (2 × 1,326,250,000) = 36,000,000 / 2,652,500,000 = **0.014**   → FAIL
ratio, using (a) = 36,000,000 / 1,317,600,000                                    = **0.027**   → FAIL
```

**Off by 74× on the contract comparable, 37× on the salary comparable.** The verdict is insensitive to which is used.

**Break-even N.** `N × 15,000,000 × 0.10 × 3 ≥ 2,652,500,000` → **N ≥ 589 named buyers**. No directory, register, job-post census or crawl anywhere in this project's `raw/` names 589 entities. The largest named set on file is 8.

**The honest shape sizes to zero by construction.** `review.md` §5's recommendation is a free MIT repo: ARPU = 0 → `market_36mo` = 0 → ratio = 0.

**Why the W3Techs rows do not rescue it.** `c1` line 5 gives Cloudflare at 25.8% of all websites (`analyst-derived`, W3Techs 2026-09-18; conflicting older cuts 23.4% June 2026 and 21.3% January 2026, side by side, not averaged), implying ~74.2% not behind Cloudflare, and line 6 gives nginx 30.9% / Apache 22.0%. Those are **percentages with no denominator on file** — W3Techs' top-1M breakout was `unknown — checked 2026-09-18`. A share is not a count of named entities, so under §B5 it cannot be an `N_buyers`. Stated and set aside.

---

## 6. Unit economics, every input labelled

**Shape A — the honest shape on file: free MIT repo plus a published post as a credibility artifact** (`review.md` §5: "Ship it free… treat the question of who pays as still open"; `success-vision.md` §5: "Revenue: none, by design").

```
price/unit  = 0 VND                 [own judgement — the shape review.md §5 recommends]
COGS/unit   ≈ 0 VND marginal        [measured-by-us 2026-09-18: stdlib-only Python, 0 network on the
                                     default path (4 socket entry points stubbed), 0.420 s CPU for 420
                                     fixture lines on this machine. No GPU — so c4 line 15's RTX 3060 Ti
                                     × EVN arithmetic does not apply to this product at all.]
GM          = undefined (price = 0)
CAC         = unknown               [formula B8 = (hours × rate + cash) / replies; replies = 0 in every
                                     channel, every pass — ORCHESTRATION.md §8.4, measured-by-us]
payback     = unknown → A11 UNKNOWN
churn/mo    = n/a                   [own judgement: a one-shot diagnostic has no subscription to churn]
recurring cost = founder time only  [9 range files to keep current; oai-chatgptuser.json regenerates
                                     within hours, stale_after_days 1, measured-by-us; refresh --dry-run
                                     5.668 s live, REPORT-PLAN §8.1]
```

**Shape B — paid variant constructed from the `c1` price anchors: a 10-working-day report on one named domain, 15.000.000 VND, 50% deposit** (`re-pick.md` §6).

```
price/unit  = 15,000,000 VND        [own judgement, pre-registered 2026-09-17; anchor SEODO "Từ 18 triệu",
                                     vendor-reported. Priced deliberately under the anchor.]
hours/unit  = 20 founder-hours      [own judgement; the offer is a 10-working-day report, re-pick.md §6]
COGS/unit, two rates side by side, never averaged:
  at USD 25/h  = 663,125 VND/h × 20 = 13,262,500 VND  →  GM = 11.6%   → FAILS both §A11 bars
  at salary-derived 311,932 VND/h    =  6,238,640 VND  →  GM = 58.4%  → passes services ≥50%, fails SW ≥70%
     [salary-derived = 54.9M VND/mo ÷ 176 h/mo; the 176 is own judgement, 22 days × 8 h]

CAC, arithmetic shown so one input can be changed:
  20 cold contacts × 3.43% reply     = 0.686 expected replies   [Instantly Cold Email Benchmark 2026,
                                                                 vendor-reported, c4 line 11]
  cost of the round = 20 h × USD 25 + USD 11 domain = USD 511    [Porkbun .com $11.08, vendor-reported]
  CAC at 100% reply→paid (generous)  = 511 / 0.686 = **USD 745**
  ARPU per engagement                = 15,000,000 VND = **USD 565**
  → CAC exceeds first-engagement revenue by USD 180 even assuming every reply pays.
payback     = > 12 months on any assumption → the bar fails on arithmetic, but the conversion rate is
              own judgement rather than measured, so A11 is recorded **UNKNOWN**, not FAIL.
LTV:CAC     = undefined — no second purchase is evidenced, and review.md §5 argues the job is asked once.
```

**Shape C — $29/mo self-serve, anchored on Known Agents Startup $29/mo (vendor-reported, re-verified 2026-09-18) — dismissed in one line.** It requires a hosted component, which trades away "nothing leaves your machine", the single structural difference the free incumbents cannot copy (`review.md` §5).

**Which figure the verdict is sensitive to (§F11).** The GM swings 11.6% ↔ 58.4% on the founder-rate choice alone. It does not flip the verdict, because A3, A5 and A10 decide it; recorded so the user can change that one input and see that nothing moves.

---

## 7. Kill-test result

The pre-registered rule, verbatim from `docs/plan/re-pick.md` §6, written **2026-09-17**, before any test:

> **Sample.** 20 named organisations, list frozen in writing before the first message is sent: the 8 agencies named in `vietnam-ai-visibility-demand.md`, plus 12 Vietnamese brands drawn from those agencies' own published case-study pages. No substitutions after the list is frozen.
>
> **Offer.** … Price **15.000.000 VND**, 50% deposit to start.
>
> | Outcome, measured on day 7 after first contact | Rule |
> |---|---|
> | **PASS** | ≥2 of the 20 have paid a 7.500.000 VND deposit. Money received, not promised |
> | **WEAK** | 0 deposits but ≥3 written replies naming a budget line and asking for a scheduled call |
> | **FAIL** | Anything else |
>
> Deposits from personal contacts of either founder do not count toward PASS.

**Has it run? No.** `c1` line 17: `requires-human — not pulled`. The list has never been frozen; no file in `projects/ai-ads-injection/raw/` contains it. Zero of the 20 organisations has been contacted by any pass, any agent, any human (`ORCHESTRATION.md` §8.4: "Human interventions that contacted a buyer, priced anything, or moved money: **0, all projects, all passes**").

**Who must run it:** the founder. No agent in this repo can contact a human.

**What it costs to run:** ≤5 working days of elapsed time and roughly 20 founder-hours (own judgement; anchor `REPORT-PLAN.md` §3.3, "Outreach round: 20 named orgs, one follow-up, decision day 7 — ≤5 working days"), USD 0 infrastructure, USD 11.08 optional domain (Porkbun, vendor-reported). **Earliest date it could produce a result: 2026-10-02** (own judgement: freeze the list and send on 2026-09-21, day-7 decision 2026-09-28, plus the single permitted 5-day WEAK extension).

**A second, cheaper route to the same A3 bar exists and has also never run.** `c1` line 18 / `review.md` closing: publish the rDNS finding — *OpenAI's crawler addresses have no PTR record at all, so Google's documented verification procedure does not transfer* — and count unprompted asks at day 14. The precondition (publication) has never occurred, which is why A3 is UNKNOWN rather than FAIL.

---

## 8. Three scenarios

Cost = hours × §B14 rate + cash. Rate: **USD 25/h**, the low end of the Upwork Vietnam AI band ($25–$80/h, vendor-reported, `c4` line 2), taken per §B14's "higher of" rule over the salary-derived USD 11.76/h (ITviec 54.9M VND/mo ÷ 176 h ÷ 26,525; `vendor-reported` figure, `own judgement` divisor). Both rates carried, never averaged. All probabilities are `own judgement` and are numbers.

Each gate below is a **research or buyer-conversation gate**. None requires a line of code — the `re-pick.md` §6 offer is a hand-delivered report, and A6 closes by installing someone else's tool.

| Scenario | Hours | Cash | First dollar | p(gate) | Value at gate | EV = p×value − cost |
|---|---|---|---|---|---|---|
| Do nothing — archive the docs as the asset, publish nothing | 0 | $0 | never | — | the research itself | **$0** — and negative if the page ships unfixed (S1, S2, S3, S6 live on master) |
| Minimum viable commitment — **research + buyer conversations only, no build** | 23 [14, 23, 45] | $11 | 2026-10-30 earliest | 0.05 | $2,000 | **−$486** |
| Full commitment — build toward `success-vision.md` §1's win condition | 200 [120, 200, 400] | $11 | `unknown` — that doc's win condition has "Revenue: none, by design" | 0.15 | $6,000 | **−$4,111** |

**Minimum commitment, itemised — every hour is research or a conversation.** Run GoAccess and AWStats first-hand on the fixture and paste the output, closing A6 from UNKNOWN to PASS (1 h; §2b's own estimate). Read the 228 comments on the 2026-08-12 ClaudeBot-spoofing thread and count verification-problem versus bandwidth-problem accounts, closing half of A1 (2 h, `own judgement`). Freeze `re-pick.md` §6's 20-organisation list in writing with a named channel each — 8 agencies already named plus 12 brands from their own case-study pages — closing A2's first half (2 h, `own judgement`). Run the outreach round: one message each, one follow-up on day 3, decision on day 7, one permitted 5-day extension (18 h; `REPORT-PLAN.md` §3.3 anchor, "Outreach round: 20 named orgs, one follow-up, decision day 7 — ≤5 working days"). Total **23 h**. Cash **$11.08** for the optional one-page offer domain (Porkbun, `vendor-reported`, wave 1d).

**p(gate) = 0.05, derived, not asserted.** The gate is A3: ≥1 deposit of 7.500.000 VND, or 1 signed LOI, or ≥3 unprompted paid asks from non-authors. Arithmetic, mandatory where a proposal depends on replies: 20 contacts × **3.43%** platform-wide cold-email reply rate (Instantly Cold Email Benchmark 2026, `vendor-reported`) = **0.686 expected replies**; the cybersecurity cut of 4.86% (Belkins 2025, `vendor-reported`) gives 0.97; LinkedIn DM at 10.3% (Expandi 2026, `vendor-reported`) gives 2.06. Fewer than one expected reply on the likeliest channel, before any reply-to-deposit conversion. Demand-side anchors all pointing the same way, all `measured-by-us` 2026-09-18: two same-slot repos at **1** and **0** stars; 74 Show HN launches in this exact category since 2025-01-01 with the best genuine one at **7 points**; the adjacent slot that does get traction is blocking (anubis 22,512★), not verifying. `own judgement`.

**Value at gate = $2,000.** One 15,000,000 VND engagement plus two more inside 90 days at the same price ≈ 45,000,000 VND ≈ $1,700, rounded up. `own judgement`, anchored on the pre-registered price.

**Full commitment, p and value.** p = 0.15 that the vision's win condition lands (a few hundred stars, contributed range files, two citing posts) — `own judgement`, anchored on 4,126★ for `ai.robots.txt` showing the category can carry stars, discounted hard by the 0–1★ same-slot evidence. Value $6,000 = two engagements at $3,000, `own judgement` anchored on the one-time GEO audit band **$1,500–$5,000**, aggregator-sourced, and flagged `transplanted from: English-language GEO-visibility audit` (`answer-integrity-buyer.md` via `market-check.md` §1). The $8k–$50k security-audit band is **not** used here: `market-check.md` §1 killed that transplant, and it is 5× this market's ceiling.

**A fourth row, and the reason it is not the recommendation.** Fix S1/S4, publish the repo, post the rDNS finding, count unprompted asks at day 14: 13 h, $0, p = 0.07, value $2,000 → **EV = −$185**, the least-negative row in this file. It is *cheaper* than the buyer-conversation route and it is *not* the gate, because the question this review is deciding is whether the research establishes a buyer — and a star count or a download count answers a different question (§F5). A publication route measures attention; the 20 conversations measure willingness to pay. Only the second closes A3's bar as §B3 defines it. If the founder wants both, publishing first and converting the post's readers into the conversation list is strictly better than cold contact, and costs 13 h more.

**A negative EV in the full-commitment row is the finding**, per §D8, and it is the largest number in the table.

**Opportunity cost (`c4`).** 23 hours = **$575** forgone at $25/h (vendor-reported band low end), or **$270** at the salary-derived $11.76/h. The clinic-MCP alternative — the founder's actual next-best use — is `requires-human — not pulled` (`c4` line 3) and remains the single missing input that could move this table. On file, the named next-best use of the same hours is `parity-vi`, to which `ORCHESTRATION.md`'s own ranked recommendation allocates **70%** of remaining effort against `aicrawlcheck`'s **10%**.

---

## 9. Known traps checked (§F)

The two the brief flagged are `FRAMEWORK.md`'s **F5** (stars as demand) and **F1** (search-level negative as demand). Both are run below, under their own numbers.

| # | Check run | Result |
|---|---|---|
| F1 | For each demand claim, which humans were asked | **Zero, every claim, every pass** (`ORCHESTRATION.md` §8.4). So A1 and A3 are recorded UNKNOWN, not FAIL and not PASS. The project's own docs are clean here — `positioning.md` labels its buyer "a hypothesis, not a finding" |
| F2 | Every absence claim carries `not found in {…} — checked <date>`; reviewer opens one | The incumbent absences do carry the braces and the date (`c1` lines 1–4). This reviewer opened the product itself, not an incumbent — GoAccess remains unrun, and that is why A6 is UNKNOWN. **The "nobody built this" class of claim is falsified outright**: two same-slot repos, 1★ and 0★, `measured-by-us` 2026-09-18. Repeated independent supply with no pull is evidence against |
| F3 | For each "X cannot happen", construct the input, run it, record exit code | **Run and failed.** `--verify-dns` certified an Anthropic IP as `verified` Googlebot, exit 0, on master, 2026-09-18 (§3). The fix is not on master; it is in the stash `wave10-fix-partial-2026-09-17` |
| F4 | Any measured object named as a product, or labelled otherwise | Not applicable to this project (F4 governs guardrail benchmarks). The analogous check here — is the compared object the real incumbent or a description of it — is F6, and it fails to docs-only |
| F5 | Stars appear only in A9/A8 context; A3 counts money, LOIs, unprompted asks | Held. Stars on file — anubis 22,512★, nginx-ultimate-bad-bot-blocker 4,794★, ai.robots.txt 4,126★, ai-crawler-intercept 1★, webserer_log_analyzer 0★ — appear in §4 and §8 only. A3 records 0/0/0. The useful reading is the trap's inverse: the two repos *nearest* this product have the *lowest* stars, so the star evidence argues **against** demand |
| F6 | §D4 carries a "how inspected" column | Carried. **0 of 11 incumbents run first-hand.** GoAccess, AWStats, Matomo are docs-only as of 2026-09-18 → A6 **UNKNOWN**. This is an improvement on 2026-09-17, when they were `not inspected` → FAIL |
| F7 | Every number cites a `raw/` file or a primary, never a compiled file; prices carry their market | Held. One transplant risk flagged at the point of use: the $1,500–$5,000 audit band is aggregator-sourced for the **English-language GEO-visibility** market. The $8k–$50k security band is quoted only to reject it |
| F8 | No `fixture` number in §1, §5 or §6 | Held. The 25-of-155 ratio (really 25-of-180, S6) appears nowhere in §1, §5 or §6. Every number in §2 carries `fixture` or `real` |
| F9 | A7 may cite an event; A3/A5 may not | Held. A7 cites the HN thread and the Known Agents threat notice. No statute is used anywhere: Law 134/2025/QH15 does not reach this product, and Luật Quảng cáo does not either — measurement is not *quảng cáo* under Điều 2.1 (`market-check.md` §4) |
| F10 | Vendor numbers labelled inline; never the sole input to §5 | Held. "5,000+ websites", "2,000+ agents", the Agentic Web Index percentages, "Available on all plans", the three spoof rates and every VND price are labelled `vendor-reported` or `analyst-derived`. §5's `N_buyers` is a `measured-by-us` count |
| F11 | Conflicts sit side by side; reviewer says which the verdict is sensitive to | Held, four conflicts. **Spoof rates 31% / 5.7% / 17.1%** (§12). Founder rate $25/h vs $11.76/h. W3Techs Cloudflare share 25.8% / 23.4% / 21.3%. AI-engineer band 50–125M vs 25–100M VND/mo. The verdict is sensitive to **none of them**: at the lower founder rate the minimum-commitment EV moves from −$185 to −$100, still negative, and A5's ratio moves from 0.014 to 0.027, still failing by 37× |
| F12 | Every date absolute; every runtime measured or labelled `unmeasured` | Held. Runtimes: 0.420 s scan and 0.799 s selftest, `measured-by-us 2026-09-18`, 420-line fixture, this machine. The on-file 0.936 s / 0.391–0.417 s carried with its own source |

**The three conflicting spoof rates, side by side, neither adopted** (`c1` line 11):

| Figure | Population | Source | Label |
|---|---|---|---|
| **31%** of GPTBot-identifying traffic was spoofing | GPTBot only | "Cloudflare May 2026 Radar report" via secondary blogs | `vendor-reported, primary URL not confirmed` |
| **5.7%** of traffic labelled AI-crawler was spoofed; ratio 1:17 | 16 named crawlers, two weeks | HUMAN Security Satori; page returned HTTP 403, figure from search snippet | `vendor-reported`, not independently verified |
| **17.1%** Amazonbot | blocked-rate, not spoof-rate | Known Agents Agentic Web Index, 2026-09-17 | `vendor-reported`, not comparable |

They disagree by more than **5×** and measure three different things. This matters directly to the verdict: it is exactly the gap a reproducible n=1 real-log measurement with a published instrument would address, and it is the strongest argument this project has for publishing.

---

## 10. Verdict

**Steelman "stop now," at full strength — argued from the research, not the code.** Four waves and three research passes produced an excellent supply-side map and never once tested demand. Every negative on file about a buyer is a search-level or landing-page-level negative (§F1), and this pass added two more that point the same way: two people have already built this exact product and hold 1 and 0 stars between them, and 74 Show HN launches in the category since 2025-01-01 top out at 7 points. The one market with sourced spend sells optimisation, not measurement — and the single agency that does name an "AI Visibility Audit" prices it at 15.000.000đ and **gives it away free** (`c1` line 19), which is the same shape that killed every other asset claim here. Bottom-up sizing fails by 74× and would need 589 named buyers where 8 are named. `market-check.md` §2 already said it plainly: nobody has been found to have bought an AI-answer audit, from anyone, at any price. The founder is measurably not the buyer — `local-infra-check.txt` records no domain, no CDN account, no server — so he cannot even be his own first conversation. Every EV row is negative, and every hour here is an hour not spent on `parity-vi`, which `ORCHESTRATION.md` allocates 70% against this project's 10%.

**Steelman "ship it free," at full strength — also argued from the research.** The research got measurably *better* on 2026-09-18, on the one criterion that had been killing this project. A6 stood as an admitted `unknown` in `mvp-spec.md` since 2026-09-17; `c1` closed it in five incumbents' own words — GoAccess's issue tracker returns "No results", AWStats' own `robots.pm` doc comment concedes the gap, DeviceDetector parses user agents only, Known Agents' FAQ describes event-sending only, Cloudflare's changelog has no historical import. That is a documented capability gap, not an unattacked absence, and it is exactly the artifact `evidence-rules.md` says survives attack roughly 1 time in 5. Alongside it sits a genuine research finding this project owns and nobody has published: the three public spoof rates disagree by more than 5× across three different populations (31% / 5.7% / 17.1%), and the rDNS result — OpenAI's crawler addresses have no PTR record at all, so Google's documented verification procedure does not transfer — is measured, dated and unpublished. `cross-read.md` pattern 5 holds that a published finding buys standing faster than a product does. Publishing costs 13 hours.

**Verdict.** Worth **23 founder-hours / $11 over 3 weeks** to reach gate **A3, run as the pre-registered 20-organisation buyer conversation** — freeze `re-pick.md` §6's list in writing with a channel each (A2), close A6 by running GoAccess and AWStats first-hand for one hour, read the 228-comment thread to separate the verification problem from the bandwidth problem (A1), then send, follow up on day 3 and decide on day 7 — **else stop**. This is a research and conversation gate, and deliberately not a build gate: the offer is a hand-delivered report, nothing in the prototype has to change to run it, and the prototype's own defects (never run on a real log, no unit suite, S1 unmerged in the `wave10-fix-partial-2026-09-17` stash) are context that would only matter in a world where a buyer existed. The ceiling is "gate first" rather than "stop" solely because A3 and A6 stand at UNKNOWN rather than FAIL, and because A6 is one hour from PASS. Against that: the minimum-commitment EV is −$486 on a $575 opportunity cost, the full-commitment EV is −$4,111, and the reply arithmetic predicts **0.686 replies from 20 cold contacts**. **The single number that would flip it: one 7.500.000 VND deposit** — money received, not promised, not from a personal contact of either founder. At one deposit, the four waves of supply-side research finally have a demand-side fact to hang on and this reopens as a service; at zero, it closes on evidence rather than on inference, which is what `re-pick.md` §5 asked for and never got, and the docs stay as the asset they already are.

---

## 11. Claims in the project's own docs not verified or contradicted

| file:line | Claim | Status | Consequence for §1 |
|---|---|---|---|
| `docs/execution/e2e-test.md:415` | "`--verify-dns` does not launder a false claim" | **contradicted by** this reviewer's run on master, 2026-09-18, exit 0 | A10 FAIL — **context row**, not a verdict driver (§1) |
| `prototype/aicrawlcheck/engines.py` (`google.googlebot` rule) | `review.md` S1 fix: drop `.googleusercontent.com` | **not applied on master.** Suffix still present; the partial fix is only in stash `wave10-fix-partial-2026-09-17` (`.git/logs/refs/stash`, one entry, "On master:") | A10 FAIL stands 2026-09-18; context, per §1 |
| `docs/execution/e2e-test.md` §13 item 16; `STATE.md`; `ORCHESTRATION.md` | "18/18" read as tests | **contradicted.** 18 = selftest assertions over one fixture (`cli.py cmd_selftest`: 7+8+2+1). `tests/test_offline.py` has **0** test functions, no `unittest`/`pytest` | §3 Proven column; no §1 row. `REPORT-PLAN.md` §8.1 already records "no unit suite below CLI" |
| `site/index.html:463`; `mvp-spec.md` "does not do" #4 | "No published range file for those was located" (Amazonbot) | **contradicted.** `c1` line 13 fetched `developer.amazon.com/amazonbot/ip-addresses`, HTTP 200: **1,292 `ipv4Prefix`, 0 `ipv6Prefix`, `creationTime 2026-09-08T05:24:10.610952+00:00`** | Closes S2 against the page; the page is wrong and unrepaired |
| `site/index.html:391` | "Actual terminal output of `python -m aicrawlcheck scan fixtures/access.log`" | **contradicted** (S3): page shows 2 spoofed + "+23 more"; the tool prints 10 + "+15 more"; 1 undeclared row vs 3 | Unrepaired. Reputation cost if published as-is |
| `site/index.html:315`; `mvp-spec.md:621`; `positioning.md:15` | "155 hits claim a known crawler identity" | **contradicted** (S6): 180 claim one, 155 are checkable; ratio 13.9%, not 16.1% | Unrepaired, in three files |
| `mvp-spec.md` "does not do" #4 | Meta / Amazonbot / Bytespider "return `unverifiable`, never `verified`" | **contradicted** (S5), confirmed in code 2026-09-18: `BROWSER_RE` wins, so Applebot returns `human`; the others return `unknown` | Unrepaired. The `human 235` row is a residual bucket, not a measurement |
| `prototype/aicrawlcheck/verify.py` `classify()` | Takes a `rules` argument | **contradicted** (S11), confirmed in code today: it calls `engines.match_user_agent(ua)` and ignores the argument | Unrepaired; breaks the documented "add a rule row" extension path |
| `docs/execution/e2e-test.md` §13 items 4, 31 | "no `git` command was run at any point" | **contradicted by its own evidence cell**, "`git status` shows only STATE.md touched" (S12) | Mandate deviation, recorded not repaired |
| `docs/plan/idea-set.md` §2 (C1), §6 | "Step 4 is what nobody sells" as demand evidence | **contradicted by** `market-check.md` §1: Step 4 is live-engine testing, prohibited by OpenAI ToU 2026-01-01 and Perplexity ToS s5.2(i) | Already absorbed; no §1 row rests on it |
| `docs/plan/idea-set.md` §5; `docs/explore/who-sells-this.md` | Absence-of-competitor claims in this slot | **contradicted** by `c1` line 7: `Unsourced-Founder/ai-crawler-intercept` (1★, 2026-08-07) and `evemilano/webserer_log_analyzer` (0★, 2026-09-02) | §F2; hardens A5's `attainable_share` downward |
| `docs/design/mvp-spec.md` "Why not the free option", last row | GoAccess / AWStats / Matomo `unknown — no pass has checked` | **resolved in the product's favour, documentarily**, by `c1` lines 1–2 on 2026-09-18 — but still never run | A6 moves FAIL → **UNKNOWN**, not PASS |
| `docs/outcome/positioning.md` "Who buys this" | The buyer profile | **unverified**, and the doc says so: "a hypothesis, not a finding". 0 humans asked | A1, A2 |
| `docs/outcome/success-vision.md` §1 | 1,900 hits / 1,700 spoofed / 40 fetches / "a few hundred stars" | **unverified by construction**; the doc labels every count invented | Excluded from §1, §5, §6 per §F8 |
| `docs/outcome/success-vision.md` §5 | "no public real-log spoof-rate study exists" | **unverified**: `unknown — not searched this wave`, and `c1` line 11 found three published figures that disagree 5× | Weakens, does not kill, the publish case |

---

## 12. Caveats

- **Weighting, stated so it can be disagreed with.** This review weights the project's own research — buyer, problem, price, incumbents, regulation (§2b) — as the verdict driver, and treats prototype completeness (no unit suite, the unmerged `wave10-fix-partial-2026-09-17` stash, never run on a real log) as one context row. That weighting is the user's instruction of 2026-09-18, not this reviewer's inference. Under `FRAMEWORK.md` §D1 read mechanically, A10's FAIL would cap the verdict at "stop" rather than "gate first"; the §10 gate is 23 hours of research and conversation either way, so the two readings differ in label, not in what to do next.
- **No human was contacted by this review**, and none can be by an agent. A3, A4, A12's positive half, A13 and the clinic-MCP opportunity cost are all `requires-human` and remain open. Every probability in §8 is `own judgement`.
- **No web access this session.** Everything outside this machine comes from `raw/c1-` and `raw/c4-`, pulled 2026-09-18 by another agent. Where `c1` records an `unknown` — no real log located, Google Trends unreachable, the Reddit half of line 8 — this review inherits it and does not fill it.
- **A6 was not converted.** This reviewer did not install GoAccess, AWStats or Matomo. The documentary evidence is strong and the incumbents' own words are quoted, but §F6 is explicit and A6 stays UNKNOWN. Roughly one hour would close it.
- **`c1`'s own WebFetch caveat carries here.** Two WebFetch attempts on the Amazonbot file returned 1,072 and 1,040 prefixes against the `curl`-measured 1,292; only that one number was cross-checked that way. Any other `c1` figure derived from a WebFetch summary carries unquantified summarizer error.
- **Cloudflare's own pages 403'd repeatedly** in `c1` (Bot Management pricing, the Radar bots report), so every Cloudflare *price* and the 31% spoof figure are secondary-sourced and labelled so.
- **The founder's rate is a comparable, not his rate.** §B14 asks for the higher of clinic-MCP revenue per hour and the HCMC contract rate; the first is `requires-human — not pulled` (`c4` line 3). If clinic-MCP pays above $25/h, every EV in §8 gets worse, not better.
- **`site/index.html` was not opened in a browser by this review**, and acceptance items 22–28 remain NOT COVERED from `e2e-test.md` §13 onward. §11's page findings are source-read and inherited from `review.md`, except the Amazonbot row, which `c1` line 13 closed independently.
- **The stash was identified by reading `.git/logs/refs/stash` as a file**, not by running git, per the brief. Its contents were not inspected; that it is a *partial* fix is `STATE.md`'s own word ("12 prototype files modified (388+/67-)… cut by session end"). What it fixes and whether it closes S1 is `unknown — not inspected 2026-09-18`.
- **This review produces evidence and a verdict in §D10's required form. The go/no-go is the user's**, per `CLAUDE.md`.

---

## Files read

`D:\researchs\market-research\CLAUDE.md`
`D:\researchs\market-research\projects\CLAUDE.md`
`D:\researchs\market-research\projects\ORCHESTRATION.md` (§§ on ads/aicrawlcheck: waves 1, 2, 5, 6, 7/8, "Wave 9a — ads review landed", "Wave 10 started early on ads", the vision/ranked-recommendation block, "New wave 10 rule")
`D:\researchs\market-research\projects\investment-review\FRAMEWORK.md` (whole)
`D:\researchs\market-research\projects\investment-review\REPORT-PLAN.md` (§§3.3, 3.4, 3.5, 8, and sections (e)–(i))
`D:\researchs\market-research\projects\investment-review\raw\c1-aicrawlcheck-pulls-2026-09-18.md` (whole, 19 sections)
`D:\researchs\market-research\projects\investment-review\raw\c4-cross-cutting-pulls-2026-09-18.md` (whole)
`D:\researchs\market-research\projects\ai-ads-injection\CLAUDE.md`
`D:\researchs\market-research\projects\ai-ads-injection\STATE.md` (last 300 lines)
`D:\researchs\market-research\projects\ai-ads-injection\docs\plan\idea-set.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\plan\re-pick.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\review\market-check.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\design\mvp-spec.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\execution\build-log.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\execution\e2e-test.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\outcome\review.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\outcome\positioning.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\outcome\success-vision.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\explore\who-sells-this.md`
`D:\researchs\market-research\projects\ai-ads-injection\docs\explore\policy-ceiling.md`
`D:\researchs\market-research\projects\ai-ads-injection\raw\wave2b-crawler-analytics-competitors.md`
`D:\researchs\market-research\projects\ai-ads-injection\raw\vietnam-ai-visibility-demand.md`
`D:\researchs\market-research\projects\ai-ads-injection\prototype\aicrawlcheck\cli.py`
`D:\researchs\market-research\projects\ai-ads-injection\prototype\aicrawlcheck\verify.py`
`D:\researchs\market-research\projects\ai-ads-injection\prototype\aicrawlcheck\engines.py`
`D:\researchs\market-research\projects\ai-ads-injection\prototype\tests\test_offline.py`
`D:\researchs\market-research\projects\ai-ads-injection\prototype\` (directory listing; `wc -l` on all 9 modules and both test files)
`D:\researchs\market-research\projects\ai-ads-injection\.git\logs\refs\stash`, `.git\HEAD`, `.git\logs\HEAD` (read as files; no git command run)
`D:\researchs\market-research\docs\markets\ai-search-ads.md`
`D:\researchs\market-research\docs\findings\injection-feasibility.md`

Runs made by this review on this machine, 2026-09-18 (`measured-by-us`): `python -m aicrawlcheck selftest`; `python -m aicrawlcheck scan fixtures/access.log`; `python -m aicrawlcheck scan /tmp/fake.log --format combined --verify-dns --out csv` (the S1 counterexample); `grep -c '^def test' tests/test_offline.py`.
