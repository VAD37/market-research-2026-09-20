# Investment review — `Foreman` (`projects/agent-hermes-dashboard`)

2026-09-18. Stage 3 of `projects/investment-review/`, per `FRAMEWORK.md` §D. Opus.

Primary evidence: `raw/c2-foreman-pulls-2026-09-18.md`. Cross-cutting evidence: `raw/c4-cross-cutting-pulls-2026-09-18.md` — **absent when this review began, landed mid-pass and was read in full before §D6 and §D8 were written. No `pending-c4` cell remains in this file.**

Every number below already exists in a `raw/` file or a project doc, cited inline by path and label kind. No figure is introduced by this review. Arithmetic in §5, §6 and §8 is shown so one input can be changed and the result recomputed.

**Three KILL rows are down: A3 `UNKNOWN`, A6 `FAIL`, A10 `FAIL`. Verdict ceiling is "gate first" (§10), not "stop" — every one of the three is closable inside 11 founder-hours at $0 cash. If those hours are not spent, the answer is "stop".**

---

## 1. Header table

| Criterion | Number found | Source + label | Threshold (§A) | PASS / FAIL / UNKNOWN |
|---|---|---|---|---|
| A1 Problem severity | 0 buyer conversations held; 3–4 first-person posts, no denominator | `c2` item 11, `measured-by-us`; `success-vision.md` caveats | ≥5 of 10 name it unprompted | **UNKNOWN** (§9 F1) |
| A2 Buyer reachability | 0 named organisations or people on any frozen list | project has no `docs/customers/`; `ORCHESTRATION.md` L708 | ≥20 named, ≥3 reached in 14 days | **FAIL** |
| A3 **KILL** Willingness to pay | 0 deposits, 0 LOIs, 0 paid asks; not published, clock not started | `c2` item 16, `requires-human` | ≥1 deposit / LOI / ≥3 unprompted asks | **UNKNOWN** |
| A4 Price point | No price from any named buyer | no buyer contacted by any pass | a number a named buyer said or paid | **UNKNOWN** |
| A5 Bottom-up size | `N_buyers` unknown; no Claude Code headcount published | `c2` item 4, `unknown — checked WebSearch 2026-09-18` | ratio ≥ 1 (§5) | **UNKNOWN** |
| A6 **KILL** Incumbent coverage | 0 of 5 free incumbents run first-hand | §4 table; `c2` items 1, 3, 13 | every named free incumbent run | **FAIL** |
| A7 Why now | Official plugin marketplace 101 → 316 entries, 2026-03 → 2026-09-18 | `c2` item 6, `measured-by-us` from live `marketplace.json` | one dated event ≤12 months, primary | **PASS** |
| A8 Channel with cost | 0 contacts, 0 replies, no published repo | `c2` item 16, `measured-by-us` negative | ≥1 reply obtained in this project | **FAIL** |
| A9 Moat / time-to-copy | 1,618 lines in `foreman/`; copy estimate 2–4 days + 0.5–1 day | `c2` item 17, `measured-by-us` + `own judgement` | ≥6 months to copy | **FAIL** |
| A10 **KILL** Real-input proof | The moment has occurred on 0 real ledgers; 1 real hook record → `task_text: null` | `e2e-test.md` step 10, `measured-by-us` | ≥1 real input not authored by team | **FAIL** |
| A11 Unit economics | CAC unknown (0 replies ever); price $0 by pre-registration | §6 | payback <12 mo, GM ≥70% | **UNKNOWN** |
| A12 Founder-market fit | Founder is the buyer: 3,103-line real `history.jsonl`, clinic-MCP business on this stack | `e2e-test.md` "Extra", `measured-by-us`; `FRAMEWORK.md` §"decision served" | founder is, or has been, the buyer | **PASS** |
| A13 Time-to-first-dollar | No path to a first dollar exists in the pre-registered design | `re-pick.md` §5 "no paywall"; `success-vision.md` §1 "never paid anything" | ≤90 days to first paid invoice | **FAIL** |
| A14 Kill rule / opportunity cost | Rule verbatim, numeric, dated 2026-09-17, pre-registered; EV negative in all three scenarios | `re-pick.md` §5; §8 | rule exists AND EV > next-best use | **FAIL** (second conjunct) |

§E score, reported for stage 4 only and subordinate to the KILLs: **8 of 100** (A7 = 3, A12 = 5), with **6 UNKNOWNs and 6 FAILs**. A score this low with this many UNKNOWNs carries no information beyond "nothing has been tested against a person"; it must not be read as a ranking input on its own.

---

## 2. What the MVP does today (measured)

One command: `cd prototype && python -m foreman`. No install, no key, no network, no signup (`e2e-test.md`, `measured-by-us` 2026-09-17).

| Fact | Value | Source, label |
|---|---|---|
| Wall-clock, `cd` to full six-section report | **0.365 s**, `time`-measured — **fixture** | `e2e-test.md` "Timing", `measured-by-us` |
| Tally, 13 keys, matched spec first run | 60 records, 52 eligible, 41 clusters, 3 repeats, 1 graduated — **fixture** | `e2e-test.md` step 3, `measured-by-us` |
| Graduated artifact | one `SKILL.md`, slug `chore-csv-pull-refund-sale`, 7 dated records, steps `TODO` — **fixture** | `e2e-test.md` step 4 |
| Unit tests | **19/19 OK**, 0.033 s | `e2e-test.md` step 5, `measured-by-us` |
| Global-config safety | SHA-256 `56edc1a2…a660` byte-identical before and after the whole session | `e2e-test.md` "Final safety proof", `measured-by-us` |
| Real-input fact 1 | `~/.claude/history.jsonl`: **3,103/3,103** lines parsed, one 5-key schema, `timestamp` 13-digit int | `e2e-test.md` "Extra", `measured-by-us` |
| Real-input fact 2 | one real-shaped hook payload → exactly 1 record, **`task_text: null`, `task_text_source: "unavailable"`** | `e2e-test.md` step 10, `measured-by-us` |
| Shipped code size | **1,618 lines** across 12 `.py` in `foreman/`; 1,887 total incl. hook + tests | `c2` item 17, `measured-by-us` |

**Real-input result for the product's own moment: none.** Every number that demonstrates recurrence is from the 60-record fixture that `fixtures.py` generates to the spec.

Mechanism, read from the code and not from the docs (`prototype/foreman/cluster.py`, `normalize.py`, `config.py`, `__main__.py`): NFKC-normalise, drop anything starting with `/`, substitute `<str>/<url>/<path>/<date>/<num>`, fold punctuation, drop a 130-word stopword list, six-branch stemmer, sort-unique → token set. Two records are the same task iff **Jaccard ≥ 0.70** (`MATCH_THRESHOLD`) with ≥ **3** tokens (`MIN_TOKENS`). Clustering is a deterministic single pass over `(recorded_at, record_id)`; each record joins the first cluster whose **representative** matches — never the full membership, which is an explicit guard against single-link chaining. A cluster graduates at **≥5 members across ≥2 distinct UTC days** (`GRADUATE_MIN_COUNT`, `GRADUATE_MIN_DISTINCT_DAYS`, the anti-burst rule). Subcommands present: `demo, scan, report, hook, install, build-fixture`. **No `--from-history` mode exists**, confirmed against `__main__.py`'s parser directly.

---

## 3. Proven vs asserted

"Proven" = run on real input, or reproduced from clean by a second agent. The e2e agent qualifies as the second agent: it deleted `out/` and `demo/`, regenerated the fixture byte-identically, and re-ran the whole script post-bug-fix.

| Proven | Asserted |
|---|---|
| The pipeline is deterministic: identical 13-key tally across build agent, e2e agent, and a JS port — **fixture input** | That a real fortnight of one person's work contains a chore repeating ≥5 times across ≥2 days |
| `assert_not_global` raises on a `~/.claude` path, exit 1, constructed input | That the clustering is *better* than `/insights` or Braintrust Topics — correctly claimed nowhere |
| 9 guard call-sites cover 6 write locations, grep-verified after the fix | That `history.jsonl` is written **before** the `Stop` hook fires — `mvp-spec.md`: *"Not measured"* |
| `history.jsonl` parses 3,103/3,103; the join falls back to `unavailable` on a miss, no crash | That the join's **positive** path recovers a real prompt — never once demonstrated |
| 0.365 s, 19/19 tests, byte-identical global config | That a live `Stop` hook fires Foreman's handler end-to-end — never watched (`e2e-test.md` caveats) |
| Stop/SubagentStop payloads carry no `cost`, no `duration_ms`, 3 live runs, v2.1.259 | That the graduated `SKILL.md` changes what anyone does — `success-vision.md` §4: today, **nothing** |

**Bug-class check (the review's own obligation).** For each "X cannot happen", the input that makes X happen:

- *"`assert_not_global()` is called before every write path"* (`mvp-spec.md`) — **constructed input found, claim was false.** `hookcmd.py`'s `_log_failure()` wrote a diagnostic log to `dirname(--ledger)/foreman-hook.log` on any exception with **zero** guard calls in the file. Reproduced in a sandbox, fixed, re-verified (`e2e-test.md` "Bugs found by running it"). This is the portfolio's fourth instance of the class and the only one caught by construction rather than by review. Credit where due.
- *"No `cost` field is ever emitted"* — reachable only through the excluded-fields table; no constructed input needed, and the report's own text points at `ccusage` instead. Held.
- *"Voice templates carry no numbers and no claims"* — two mechanical tests enforce it (`test_voice_templates_carry_no_numbers`, `_carry_no_claims`), 19/19. Tested, not merely restated.
- *"`task_text` is the user's own words, never fabricated"* — **no constructed failing input exists.** The join is a heuristic on an assumption the spec itself labels `Not measured`. If history lands after the hook, the record silently carries **the previous prompt's** text. Restated, not tested.

---

## 4. Incumbent gap, in the incumbent's words

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price |
|---|---|---|---|---|
| `/insights` (first-party, the primary) | docs live 2026-09-18 | **docs only** — run is `requires-main-thread` | *"analyzes your recent sessions on this machine … friction points such as misunderstood requests or buggy code, and suggestions for using Claude Code more effectively"* — no "recurring", "repeated", "pattern" or "suggest a skill" anywhere | $0, bundled |
| Claude Code CHANGELOG | 2.1.179 → 2.1.276, fetched 2026-09-18 | **full raw file grepped, 7,063 lines** | No recurrence-detection or history-suggestion entry. Nearest: `/loop` and cron — forward scheduling, the opposite mechanism | $0 |
| Braintrust Topics (was "Patterns") | GA, docs 2026-09-18 | **docs only** | *"continuously clusters production traces … to surface recurring patterns automatically"*; output is *"evaluation datasets, scorers, and review queues"* — not a runnable artifact | free 10k scores/1 GB; **Pro $249/mo** |
| `kenn-io/agentsview` (5,942★) | 2026-09-18 | **not inspected — A6 FAIL** | *"Local-first session search, analytics, insights, and token use statistics for coding agents"* | $0 |
| `Dicklesworthstone/coding_agent_session_search` (1,136★) | 2026-09-18 | **not inspected — A6 FAIL** | *"Unified TUI and CLI to index and search local coding agent session history across 11+ providers"* | $0 |
| `ccusage` (18,615★, 2026-09-18) | star count measured; tool not run | **not run** | Dollars and 5-hour blocks; no task identity | $0 |
| `/usage` `Loops` row | docs 2026-09-17 | docs only | Rolls up *already-defined* scheduled tasks | $0 |

All sources `vendor-reported` except the star counts and the changelog grep (`measured-by-us`, `c2` items 2, 5, 7, 13).

**A6 = FAIL, not UNKNOWN.** The changelog half passes cleanly — the feature is not shipped by the vendor as of 2026-09-18. But the bar is *every named free incumbent run first-hand*, and two free incumbents in exactly Foreman's shape surfaced on 2026-09-18 with 7,078 stars between them and neither was opened. `/insights` alone would be `UNKNOWN` (docs-only on the primary, F6); the two uninspected repos are what make it `FAIL`. Closing cost: ~2 hours, $0.

---

## 5. Bottom-up sizing, arithmetic shown

```
N_buyers         = unknown           [c2 item 4: no Anthropic-stated WAU/MAU/headcount,
                                      unknown — checked WebSearch 2026-09-18;
                                      c2 item 11: 3-4 first-person posts, no denominator]
ARPU_yr          = $24               [vendor-reported — SessionWatcher Pro $24/year, c2 item 8.
                                      NOT Foreman's price; Foreman is $0 by pre-registration.
                                      Conflicting comparables side by side, never averaged:
                                      SessionWatcher Solo $6.99 one-time, Bundle $14.99,
                                      Pro $59 one-time; CrewTower $9.99 / $14.99 one-time]
attainable_share = 0.05              [own judgement. B5 caps at 0.10 without distribution
                                      evidence; halved again because the channel count is
                                      zero, no repo is published, and the one prior
                                      implementation of this exact function took 8 stars
                                      in four months (c2 item 7, measured-by-us)]
market_36mo      = N x 24 x 3 x 0.05 = N x $3.60

founder_cost_yr, two anchors, side by side, never averaged:
  rate_A  = 54.9M VND/mo / 176 h = 311,932 VND/h = $12.33/h
            [vendor-reported ITviec 2025-2026, n=1,839, back-end >8yr, c4 item 1;
             176 h/mo own judgement; VND 25,306/USD filed SBV 2026-07-27, c4 item 5]
  cost_A  = 54.9M x 12 = 658.8M VND = $26,035/yr
  rate_B  = $25/h, the floor of the Vietnam AI-engineer Upwork band $25-80/h
            [vendor-reported via Second Talent rate card, c4 item 2]
  cost_B  = 25 x 2,000 = $50,000/yr

ratio    = market_36mo / (2 x founder_cost_yr)   -> PASS if >= 1
  anchor A: N x 3.60 >= 52,070   ->  N >= 14,464 paying-eligible buyers
  anchor B: N x 3.60 >= 100,000  ->  N >= 27,778 paying-eligible buyers

N_buyers is unknown -> ratio is unknown -> A5 = UNKNOWN.
```

The clinic-MCP revenue per hour, which `B14` says to take if higher, is `requires-human — not pulled` (`c4` item 3). Both anchors above are therefore **floors**; the true rate can only move the required `N` up.

What is on file instead of `N`, and why none of it substitutes: r/ClaudeAI ≈1.1M members (2026-09-13) / 1,093,707 (2026-08-23) / 1,043,382 (late Aug) — three `analyst-derived` trackers, conflicting, none Reddit's own; Claude Discord 123,662 vs 127,191, genuinely conflicting, no date resolution (`c2` item 12). These are visibility proxies and are barred from A5 by F5 and F10. The relevant denominator — how many of them run a *business* rather than a codebase through Claude Code — is `unknown — no denominator; checked WebSearch 2026-09-18`.

One number sizes the ceiling honestly: **no disclosed revenue or customer count exists for any paid Claude Code third-party tool**, checked 2026-09-18 (`c2` item 9). Not a low number — an absent one, for the whole category.

---

## 6. Unit economics, every input labelled

```
price/unit   = $0          [re-pick.md §5, pre-registered: "Ship it free and MIT...
                            no paywall, no waitlist gate on the download"]
COGS/unit    = $0          [measured-by-us: stdlib only, no install, no key, no network
                            (e2e-test.md); marginal cost of one more download is zero]
GM           = (0 - 0)/0   = undefined at the shipped price.

Hypothetical paid variant, at the nearest comparable price:
  price      = $24/yr      [vendor-reported, c2 item 8]        ARPU_m = $2.00
  COGS       = $0          [local CLI; no hosted variant is scoped -
                            success-vision.md §7 "what is not on this list"]
  GM         = 100%        -> clears the >=70% software bar, and means nothing at price $0.
  (A hosted variant would call Sonnet 5 at $2/$10 per MTok or Opus 5 at $5/$25
   [vendor-reported, c2 item 18]. Not scoped, so not costed.)

CAC          = cost_per_reply / (paying / replies)   [B8]
  cost_per_reply = (hours x rate + cash) / replies
  replies      = 0        [measured-by-us negative: not published, no repo, c2 item 16]
  -> cost_per_reply = undefined, CAC = unknown.

payback_mo   = CAC / (ARPU_m x GM) = unknown / (2.00 x 1.00) = unknown
churn_mo     = 0.05       [own judgement; no retention data exists for any tool in this category]
LTV          = 2.00 x 1.00 / 0.05 = $40
LTV:CAC      = 40 / unknown = unknown

Solved backwards, so the user can test it: LTV:CAC > 3 (Skok) requires CAC < $13.33.
At rate_A ($12.33/h) that is under 65 minutes of founder time per paying customer,
outreach included. Own judgement: not reachable through any channel on file -
cold email replies at 3.43% and LinkedIn DMs at 10.3% [vendor-reported, c4 item 11]
put 10-30 contacts behind each reply before anyone pays.
```

A11 = **UNKNOWN**: GM is computable and passes; CAC and payback are not, and never will be until one message is sent to one person.

---

## 7. Kill-test result

**The rule, verbatim** (`docs/plan/re-pick.md` §5, written **2026-09-17, before any test runs, and not adjustable afterwards**):

> **Test**: build H function (b) only — a local governor that, before dispatching a queued job, projects its cost against remaining window headroom and defers it past the reset instead of letting it die mid-run. Ship it free and MIT on GitHub. One release post. No paywall, no waitlist gate on the download.
>
> **Pre-registered rule, both conditions required to proceed:**
> - **≥ 100 GitHub stars within 14 days of release**, AND
> - **≥ 3 distinct people who are not the authors, unprompted, asking for a paid, hosted or supported version.**
>
> **Miss either → stop, and this project closes for good.** … **500 stars with zero paid asks is a stop**, not a proceed, and that is written down now so it cannot be renegotiated later.

**Has it run: no.** The project is unpublished — no public repo and no release post found on 2026-09-18 (`c2` item 16, `measured-by-us` negative). The 14-day clock has not started.

**Who must run it:** the user. Publishing, licensing, the release post and any reply to a stranger are `requires-human` (`pass4-read.md` "Which need a human"; `success-vision.md` §7 item 7).

**Cost to run:** ~4 hours of hygiene (repo, licence, release post) plus 1 hour to count at day 14 — `own judgement`, extending `success-vision.md` §7 item 7's "an hour of hygiene plus 14 days of waiting". **$0 cash.** Earliest read date if published 2026-09-18: **2026-10-02**.

**One flag on the rule itself, and it is not a technicality.** The gate was pre-registered for the **deferral governor**, which was never built. `success-vision.md` §5 transfers it to Foreman *"unchanged because it measures the same thing — whether this team can reach developers at all."* The thresholds were not moved, which is the thing B14 actually forbids, so the transfer is legitimate. But the consequence is stated in the re-pick's own words: a pass would mean *"this team can reach developers"*, **not** *"the supervision layer is a business"*. **Passing this gate cannot validate Foreman's premise.** It buys an answer to a question about the team that is worth knowing for the sibling projects, and nothing about A5, A6 or A10.

---

## 8. Three scenarios

Rate anchors from §5, reported side by side, never averaged. Cash is $0 in every row — the tool is stdlib-only, local, and needs no hosting.

| Scenario | Hours | Cash | First dollar | p(gate) | Value at gate | EV = p×value − cost |
|---|---|---|---|---|---|---|
| Do nothing (archive; publish as-is at most) | 0 | $0 | never | — | reputation only | **$0** |
| Minimum viable commitment (run the gate, nothing else) | 5 | $0 | never — no paywall by pre-registration | **0.012** | **$440** | **−$56** (rate_A) / **−$120** (rate_B) |
| Full commitment (build toward the vision doc's win condition) | 132 | $0 | never — the win condition has the user paying nothing | **0.05** | **$440** | **−$1,606** (rate_A) / **−$3,278** (rate_B) |
| *Pre-gate, not in the template: close A6 + A10 first* | *11* | *$0* | *n/a* | *n/a* | *decision information* | *−$136 (rate_A) / −$275 (rate_B)* |

Every input, labelled:

- **Hours, min commitment = 5** — 4 h publish hygiene + 1 h counting at day 14 (`own judgement`, from `success-vision.md` §7 item 7).
- **Hours, full commitment = 132** — `own judgement` over `success-vision.md` §7's ranked list: item 1 `scan --from-history` 8 h, item 2 runnable command from the user's own prompt 10 h, items 3–4 wording + caveat 1 h, item 5 live hook fire 4 h, item 6 real-ledger run with redaction 2 h, item 7 publish 4 h, item 8 `--plain` 3 h = 32 h; plus the win condition's twelve months of a maintained 700-star repo at 2 h/week × 50 weeks = 100 h.
- **Hours, pre-gate = 11** — 2 h to run `/insights` and open the two uninspected repos (closes A6); 8 h to build `scan --from-history` (the parser, join, normalizer and clusterer all exist — `success-vision.md` §7 item 1); 1 h to run it on the real 3,103-line history and redact to normalised shapes (closes A10). `own judgement`.
- **p(≥100 stars in 14 days from a cold start) = 0.12**, `own judgement`, from the cold-start comparables on file: `claude-session-budget` **8★**, unchanged across four months (`c2` item 7); `claude-meter` 48★, `hydra` 18★, `claumon` 16★ (`raw/2b-demand-evidence-2026-09-17.md`). The category leader's +249 stars in 14 days compounds on an 18,000-star base and is not a cold-start comparable.
- **p(≥3 unprompted paid asks | 100 stars) = 0.10**, `own judgement`, from `c2` item 9: zero disclosed revenue or customer count for **any** paid Claude Code third-party tool, checked 2026-09-18.
- **p(gate) = 0.12 × 0.10 = 0.012** — both conditions are required by the rule.
- **Value at gate = $440**, `own judgement`, constructed: 100 stars × 2% ever paying × $24/yr × 3 yr = $144, plus $296 of information value for the sibling projects (24 h of a channel test not re-run elsewhere, at rate_A).
- **p(full-commitment win condition) = 0.05**, `own judgement` — it requires the gate to pass *and* 700 stars at twelve months, against a vision the file itself labels fiction.

**The full-commitment row is negative by construction, not by pessimism.** `success-vision.md` §1's own win condition reads *"She has never paid anything"*, and §5 states the shape outright: *"A free MIT tool that passes or fails a pre-registered gate… Not a product with a price."* There is no revenue term to put in the EV. Raising p to 1.00 leaves EV at −$1,187 (rate_A). **No probability makes this row positive; only a price would, and the pre-registration forbids one.**

---

## 9. Known traps checked (§F)

| # | Check run | Result |
|---|---|---|
| F1 | For each demand claim, which humans were asked | **Zero, for every one.** A1, A3, A4 recorded `UNKNOWN`, not `FAIL` and not `PASS`. `ORCHESTRATION.md` L708: *"no buyer has been contacted by any pass"* |
| F2 | Absence claim carries `not found in {…}`; reviewer opens one item in the braces | Claim: no platform feature detects that two ad-hoc prompts were one task — `not found in {CHANGELOG 2.1.179–2.1.276, /insights docs, /usage Loops, Braintrust Topics} — checked 2026-09-18`. **The reviewer opened none of them** (no web access this pass; `/insights` is `requires-main-thread`); opened `foreman/__main__.py` and `cluster.py` first-hand instead. That failure is precisely why A6 is FAIL. Counter-evidence found: `agentsview` 5,942★ and `coding_agent_session_search` 1,136★ are repeated independent supply with no disclosed pull |
| F3 | For each "X cannot happen", construct the input that makes X happen | **Run, one claim broke.** `assert_not_global` bypass via the hook failure-log path: constructed, reproduced, fixed, re-verified across 9 call sites. Held: no-cost-field, voice-template tests. **Restated, not tested:** the join's *"assumes history is written before the `Stop` hook fires — Not measured"* |
| F4 | Any parity number names the measured object | n/a — Foreman publishes no benchmark. The analogue check: no clustering-quality comparison against `/insights` or Braintrust exists anywhere in the project, and the page correctly asserts none |
| F5 | Stars appear only in A9/A8 context; A3 counts money only | **Held.** The project's own gate pre-registers stars as insufficient — *"500 stars with zero paid asks is a stop."* Star counts appear in §4, §5, §8 as context and in no A3 cell |
| F6 | "How inspected" column present; docs-only on the primary is UNKNOWN, not inspected is FAIL | **Run — §4.** 0 of 5 free incumbents run first-hand. `/insights` docs-only (would be UNKNOWN alone); two repos not inspected → A6 **FAIL** |
| F7 | Every number cites a `raw/` file or a primary, never another compiled file | **Held.** One correction applied: 18,591★ circulates through `re-pick.md` (compiled); this review cites the `c2` measured **18,615**, 2026-09-18. Prices carry their market — the $24/yr comparable is a US-billed vendor price, not a Vietnam price |
| F8 | Any quoted page/README number tagged `fixture` or `real`; no fixture number in §1, §5, §6 | **Held.** 0.365 s, the 13-key tally, 41 clusters, 1 graduated, `chore-csv-pull-refund-sale` are tagged `fixture` and confined to §2 and §3 |
| F9 | A law or event may not feed A3/A5 | No law is cited by this project. The analogue: the **828 GitHub issues** are demand for the *cost governor*, not Foreman, and `re-pick.md` §3 establishes they are demand directed at the vendor to fix its own meter. **That signal does not transfer**; it is used in no A3 or A5 cell here |
| F10 | Vendor-stated labelled inline; never sole input to §5 | **Held.** Anthropic's *"WAU doubled since January 1, 2026"* and *"$2.5B run-rate"* are `company-stated` and relayed (primary URL not located, `c2` item 4 / `c4` Additional); §5's `N_buyers` is `unknown`, so neither is an input |
| F11 | Conflicts side by side; say which the verdict is sensitive to | **Held.** Discord 123,662 vs 127,191; Waydev $449 vs $649; ITviec 54.9M vs Second Talent 85–125M vs reco-vn 25–100M VND/mo; SBV 25,306 (2026-07-27) vs 25,617 (secondary, ~2026-09-18); plugin marketplace 101 → >200 → 316. **The verdict is sensitive only to the founder-rate conflict, and it does not flip on it**: min-commitment EV is −$56 at the lowest anchor and −$120 at the highest. Both negative |
| F12 | Every date absolute; every runtime measured or labelled | **Held.** 0.365 s measured with `time`. The report's `median self-timed duration 142.5 s` is **Foreman's own submit-to-stop arithmetic, not Claude Code's `duration_ms`**, which is absent from the payload — and `success-vision.md` §6 already flags that the caveat prints two screens after the number |

---

## 10. Verdict

**Steelman for stopping now, at full strength, before the verdict.** The buyer was killed by the project's own adversarial review and nothing since has revived him: `re-pick.md` §4 closes all three shapes — sell supervision to developers (floored at free), to non-technical buyers (unreachable without field sales), or sell a service instead (a different brief). Nine months of this repo's research put the whole category on a clock: OpenAI killed its own third-party-shaped agent builder in eight months, ClickHouse bought Langfuse, Mintlify bought Helicone, and all three frontier vendors now ship their own console (`docs/markets/agent-dashboard.md`, `docs/competitors/agent-dashboard-roster.md`). The one demand signal the project ever found — 828 issues — belongs to a different product and is aimed at the vendor. The moat is 1,618 lines that copy in 2–4 days. Time-to-first-dollar is not long, it is **absent**: the pre-registered design forbids a paywall and the success vision's own happy user *"has never paid anything"*, so the full-commitment EV is negative at **every** probability including 1.00. A6 and A10 are both FAIL, A2, A8, A9, A13 and A14 are FAIL, and the honest §E score is 8 of 100. Stopping costs nothing and loses nothing that is not already written down.

**What survives that, and it is one thing.** All three KILL rows are cheap to close, the two cheapest are decisive, and neither has been attempted. Two hours opens `/insights` and the two uninspected competitors — and if any of them already reports repeated prompts, the project ends that afternoon on evidence rather than on argument, which is worth more to the portfolio than an unresolved stop. Nine more hours puts the product's own moment on real input for the first time: every part of `scan --from-history` already exists, and this machine holds a 3,103-line real ledger that parses 3,103/3,103. That is `ORCHESTRATION.md`'s own wave-10 rule — real input before polish — and it is the only way the portfolio's shared hole gets closed for this project at $0.

**Worth 11 hours / $0 over 2 weeks to reach gate G — G = A6 closed (run `/insights`; open `kenn-io/agentsview` and `Dicklesworthstone/coding_agent_session_search`) and A10 closed (`scan --from-history`, run on this machine's real 3,103-line `history.jsonl`, report redacted to normalised shapes) — else stop.** Publication and the pre-registered 14-day gate are worth starting **only if G passes**; at p = 0.012 its expected value is −$56 and it cannot validate the premise in any case. **The numbers that flip this:** if `/insights` or `agentsview` already lists repeated work, stop that day — Foreman's only surviving claim is the emitted file, which is not a business. If the real-ledger run produces **zero** clusters of ≥5 members across ≥2 days, stop — the mechanism is correct and the world does not contain its input. If it produces one and the user recognises the chore, the 5-hour publication gate becomes the cheapest remaining question, and the answer to it is still about the *team's* distribution, not about Foreman.

---

## 11. Claims in the project's own docs not verified or contradicted

| file:line | Claim | Status | Consequence for §1 |
|---|---|---|---|
| `docs/plan/re-pick.md:158` | Revival condition *"Anthropic removes `claude -p` from subscription limits — the 2026-06-15 withdrawal says this is live"* | **Ambiguous, not contradicted on the plain reading.** `c2` item 10 reads it as treating the change as shipped; the support banner says it was **paused before taking effect and is still paused 2026-09-18**. But `market-check.md:163` — the binding input `re-pick` cites — quotes that same pause banner verbatim and correctly on 2026-09-17, and reads "live" as *the risk* being live. **Checked all three named files:** `success-vision.md` and `mvp-spec.md` never mention `claude -p` billing at all | **None.** No downstream claim depends on the change having taken effect. The revival condition remains untriggered, which is the correct state |
| `docs/plan/re-pick.md:122` | *"the 2026-06-15 billing withdrawal"* listed as a first-hand evidence asset | **Verified.** A withdrawal did occur — the change was announced, scheduled, and pulled | None |
| `docs/explore/claude-code-substrate.md`, `docs/explore/task-telemetry.md` | `Stop`/`SubagentStop` carry `cost` and `duration_ms` | **Contradicted by measurement** — `raw/hook-payload-measurement-2026-09-17.md`, 3 live runs, v2.1.259; re-confirmed 2026-09-18 (`c2` conflict table). Both files remain uncorrected on disk | **None for Foreman.** `mvp-spec.md` §"Fields that do NOT exist" already excludes every affected field and cites the measurement. The stale files are a hazard only to a future agent reading `explore/` first |
| `docs/design/mvp-spec.md` §"The join…" | *"It assumes history is written before the `Stop` hook fires. Not measured."* | **Unverified, and load-bearing** | **A10.** The mechanism that supplies the user's own words has never produced a non-null `task_text` on a real record; on a real hook payload it produced `null` |
| `docs/design/mvp-spec.md` §"Why not the free option" | `/insights` *"Emits no runnable artifact; no scriptable/headless form found"* | **Unverified** — sourced to one docs line; output never inspected | **A6 FAIL.** The project's own file already labels this `unknown — checked …L61 only` |
| `docs/design/mvp-spec.md`, `docs/outcome/success-vision.md` §3, §5, §6, §7 | *"Braintrust Patterns remains `unknown — not pulled`"* | **Superseded 2026-09-18.** Now pulled (`c2` item 3): renamed **Topics**, GA, clusters traces to *"surface recurring patterns automatically"*, emits eval datasets/scorers/review queues — **not** a runnable artifact. Free tier + **$249/mo** Pro | Gap claim survives on the vendor's own words, still `vendor-reported` docs-only. Does **not** lift A6 |
| `docs/outcome/success-vision.md` §5 | *"the gate transfers unchanged because it measures the same thing"* | **Unverified transfer.** The gate was pre-registered for the deferral governor, never built; the transfer decision was made after Foreman existed. Thresholds unmoved, so not a renegotiation | **A3.** Passing the gate cannot validate Foreman's premise — §7 |
| `docs/outcome/success-vision.md` §2 | JS port agrees with Python on 421/421, 1,770/1,770, 200/200 | **Self-reported** by the agent that wrote the page (`STATE.md`, sales-page COMPLETE). Not independently reproduced | Low. Parity of a demo, not of the product |
| `docs/design/mvp-spec.md` | No `~/.claude/commands/` on this machine; slash-command format *"unknown — never observed"* | **Unverified** | Blocks `success-vision.md` §7 item 2, the one change that would make a user stop retyping (§D3 "what they stop doing: nothing") |
| `docs/plan/idea-set.md` fact 1 | *"Per-task cost and duration are free"* | **False as written**, already declared so by `re-pick.md` §2 | None; superseded upstream |
| `docs/plan/re-pick.md` §2/§5, `success-vision.md` | `ccusage` 18,591★ | **Superseded, not contradicted** — 18,615★ measured 2026-09-18. A trend on a steady ~18/day line | None |
| `docs/execution/e2e-test.md` "Acceptance checklist" | 20/20 items pass | **Verified for items 1–20; items 21–31 never independently checked.** The wave-9a review agent was **STOPPED before writing** `docs/outcome/review.md` (`STATE.md`, 2026-09-18) — **this project has never had an outcome review** | Every "Proven" cell in §3 rests on the build agent plus one e2e agent. The e2e agent does satisfy the framework's "second agent from clean" test for the fixture pipeline; nothing else has a second reader |

---

## 12. Caveats

- This review had **no web access and could not run `/insights`**. Every incumbent statement is second-hand from `raw/c2-foreman-pulls-2026-09-18.md`. The F2 check therefore **failed to run as specified** — the reviewer opened no item in its own absence-claim braces, and §4's A6 FAIL is partly a verdict on this review's own reach as well as on the project's.
- `requires-main-thread` items (`c2` 1 and 14: `/insights` output; one live `Stop` hook fire) and `requires-human` items (`c2` 16: publication and the gate; `c4` 3, 14: clinic-MCP revenue per hour, the founder's actual subscription cost) are held at `UNKNOWN`. No inference was made around any of them.
- `founder_cost_yr` uses the higher of two **published** anchors because the third input B14 actually prefers — clinic-MCP revenue per hour — is `requires-human — not pulled`. Both figures used are floors.
- The VND/USD rate is **VND 25,306, filed SBV 2026-07-27** — not the review-date rate, which is `unknown — checked vietcombank.com.vn and sbv.gov.vn 2026-09-18, live widget not machine-readable` (`c4` item 5). A secondary claims 25,617 around 2026-09-18. Every USD figure in §5, §6 and §8 moves ~1% between the two and no verdict turns on it.
- Every probability and every attainable share in §5 and §8 is `own judgement` with its reasoning shown, so the user can replace one and recompute. None is sourced, and §8's EVs are the weakest numbers in this file.
- The 828-issue demand signal, the strongest evidence this project ever produced, belongs to a **different candidate** (the cost governor, H(b)) that was never built. It is cited here only to say it does not transfer.
- Reddit was unreachable for every pass in this project's history (three independent failures on file). Every demand negative for Foreman inherits that weakness, and A1 is `UNKNOWN` partly for that reason.
- The verdict is the user's. This file produces the evidence and the arithmetic, not the decision.

---

## Files read

Root and framework:
- `CLAUDE.md`
- `projects/CLAUDE.md`
- `projects/investment-review/FRAMEWORK.md` (whole, 354 lines, incl. §A, §B1–B14, §C1–C4, §D1–D12, §E, §F1–F12)
- `projects/investment-review/raw/c2-foreman-pulls-2026-09-18.md` (whole, 222 lines)
- `projects/investment-review/raw/c4-cross-cutting-pulls-2026-09-18.md` (whole, 212 lines)
- `projects/ORCHESTRATION.md` (sections naming hermes/Foreman: L40, 49, 53, 65–67, 83, 137, 148, 160, 167, 174, 183, 186, 195, 201, 242–247, 262, 291–292, 329–339, 380–381, 390, 397–414, 441–450, 495–504, 555, 594–598, 625, 651, 660–710, 735, 906, 920–923)
- `docs/markets/agent-dashboard.md`
- `docs/competitors/agent-dashboard-roster.md`

Project `projects/agent-hermes-dashboard/`:
- `CLAUDE.md`
- `docs/plan/idea-set.md`
- `docs/plan/re-pick.md`
- `docs/review/market-check.md`
- `docs/design/mvp-spec.md`
- `docs/execution/build-log.md`
- `docs/execution/e2e-test.md`
- `docs/outcome/success-vision.md`
- `docs/explore/telemetry-measured.md`
- `raw/hook-payload-measurement-2026-09-17.md`
- `raw/2b-demand-evidence-2026-09-17.md`
- `STATE.md` (last 300 lines)

Prototype code, read first-hand for §2 and §3:
- `prototype/foreman/__main__.py`
- `prototype/foreman/cluster.py`
- `prototype/foreman/normalize.py`
- `prototype/foreman/config.py`
- file listing and `wc -l` of `prototype/foreman/*.py`, `prototype/foreman_hook.py`, `prototype/test_foreman.py`
