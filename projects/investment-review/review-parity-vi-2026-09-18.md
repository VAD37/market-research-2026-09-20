# Investment review — `parity-vi` (`projects/ai-attack-defense`)

2026-09-18. Stage 3, Fable. Template: `FRAMEWORK.md` §D; number rules §B; traps §F. Evidence: `raw/c3-parity-vi-pulls-2026-09-18.md` (C3), `raw/c4-cross-cutting-pulls-2026-09-18.md` (C4), the project's own docs, `prototype/` code and `raw/sweep-*.txt` measured output. No web, no git, no GPU this pass. Paths below are relative to `projects/`; C3/C4 are relative to `projects/investment-review/`.

**Prior under test, verbatim:** "I found ai defense product is just bullshit." Tested in §2b, §3, §10 with numbers; not adopted, not rejected, before the numbers.

**Reweight, user, 2026-09-18, verbatim:** "we care the most about our own docs/ and market research. not finished product completion." Applied: the verdict rests on §2b (research quality — buyer, problem, price, incumbent, regulation); product completeness (tests, packaging, S18, S11) is context, one row in §2b, and drives nothing in §10. Gate G in §10 is a buyer-conversation gate.

**Every number carries a label.** `measured-by-us` = produced by the project on this machine, dated 2026-09-17/18; `own judgement` = this reviewer's, with its anchor named. VND↔USD at SBV central rate 25,306 (filed, 2026-07-27, C4 §5); a secondary claims 25,617 near 2026-09-18 (unverified) — side by side, not averaged; nothing below turns on the difference.

---

## 1. Header table

| Criterion | Number found | Source + label | Threshold (§A) | PASS / FAIL / UNKNOWN |
|---|---|---|---|---|
| A1 severity/frequency | 0 conversations; 0 VN chatbot incidents found; 0 live LLM-safety jobs | `hcmc-candidates.md` caveats; C3 §2, §13 — measured-by-us | ≥5 of 10 unprompted, ≥ monthly | UNKNOWN — nobody asked (F1) |
| A2 reachability | 23 named; 8 profiled, CTOs named; 0 channels filled; 0 reached | C3 §1 measured-by-us; `hcmc-opener-2026-09-18.md` §3 | ≥20 named with channel; ≥3 reached in 14 d | UNKNOWN — count passes, reach never run |
| **A3 KILL** willingness to pay | 0 deposits, 0 LOIs, 0 paid asks; nothing published | `ORCHESTRATION.md` "Nothing published"; C3 §20 requires-human | ≥1 deposit/LOI or ≥3 unprompted asks | **UNKNOWN — caps verdict** |
| A4 price | none; 10 VN vendors quote-only; 54.9M VND/mo is salary, inadmissible | C3 §9–10 vendor-reported absence; C4 §1 | a buyer-said or paid number | UNKNOWN |
| A5 bottom-up | 23 × 15M VND × 0.10 = 34.5M VND; ratio 0.026 | §5; ARPU own judgement | ratio ≥ 1 | UNKNOWN — price own judgement; fails at any VN price |
| **A6 KILL** incumbents | promptfoo docs-only; Lakera, PyRIT not inspected; 5 open models run | C3 §8 vendor-reported; §4 below | every free incumbent run first-hand | **UNKNOWN — caps verdict** |
| A7 why now | Law 134 in force 2026-03-01; NĐ 142/2026 eff. 2026-05-01; QĐ 33/2026, 46 systems, eff. 2026-08-15 | C3 §11 filed; C4 §16 filed | dated event ≤12 mo, primary | PASS — event, not demand (F9) |
| A8 channel | 0 sent, 0 replies; benchmarks 3.43% / 4.86% / 10.3% | C4 §11 vendor-reported | ≥1 reply obtained here | UNKNOWN — never run; hypothesis |
| A9 moat | none: `diff.py` 14,147 B; corpus public MIT; SEA-HELM task off 151 d | `ls` measured-by-us; C3 §7 vendor-reported | ≥6 months to copy | FAIL — honest "none" |
| **A10 KILL** real input | 5 open-weights guardrails × 600 prompts; Granite 3.0→3.1 exit 1 | `sweep-2026-09-18.md`, `raw/sweep-diff-granite-3.0-to-3.1.txt` measured-by-us | ≥1 real input; every "cannot happen" attacked | PASS open-weights; UNKNOWN commercial (C3 §5); S11 untested |
| A11 unit economics | cash COGS 111–273 VND/run; labour 15.2–48.6M VND/engagement; CAC unknown | C3 §17 own calc; C4 §2 vendor-reported; §6 | payback <12 mo; GM ≥50% services | UNKNOWN — CAC; GM <50% at 15M VND |
| A12 founder fit | founder not a chatbot operator; 3 of 8 HCMC-HQ; 0 introductions on file | `hcmc-candidates.md`; requires-human | is/was buyer, or 1 intro from ≥3 | UNKNOWN |
| A13 first dollar | no commitment date; T0 unset; nothing published | `hcmc-opener-2026-09-18.md` §4 | ≤90 d, date written first | UNKNOWN — not started |
| **A14 KILL** kill rule | 14-day rule pre-registered 2026-09-18; EV at minimum −$170 to −$610 | `hcmc-opener-2026-09-18.md` §4; §8 own judgement | rule pre-registered; EV > next-best use | PASS rule / FAIL EV on money |

Three KILL rows sit at UNKNOWN (A3, A6, A10-commercial); A14's EV half fails on cash value. Ceiling: **"gate first"**, not "stop" — a gate is reachable inside 90 days at zero cash (§7), which is the §D10 condition that separates the two. A10's PASS is product completeness and, per the reweight, carries no weight in §10.

§E score, subordinate: A7 (3) + A10 (15) = **18/100**, with 10 UNKNOWN rows and 1 FAIL. The score is an artefact of two PASS weights; it must not be read against the other two projects without the UNKNOWN count beside it.

---

## 2. What the MVP does today (measured)

One command, on this machine, 2026-09-18 (`sweep-2026-09-18.md`, all `measured-by-us`):

```
python parity.py diff --baseline runs/20260918T031411Z-local_model-granite-guardian-3.0-2b-e48b7b8acf43-default.json \
                      --candidate runs/20260918T031821Z-local_model-granite-guardian-3.1-2b-81145486e85c-default.json
PARITY GAP (harmful arm)   25.5 pp -> 28.5 pp   (Δ 3.0 pp)
NEW VI MISSES: 40   NEW VI CATCHES: 19   NEW INDETERMINATES: 0
VERDICT: REGRESSION
  category 'aegis2-harmful' (n=100) Vietnamese recall dropped 6.0 pp, threshold 5.0 pp
  net new Vietnamese misses +21, threshold 0
$ echo $?  -> 1
```
(`raw/sweep-diff-granite-3.0-to-3.1.txt`, verbatim; produced by the pre-`b3083bd` `diff.py` — see §11 row 7.)

Wall-clocks, 600 prompts each, RTX 3060 Ti 8 GB, `cuda`, torch 2.6.0+cu124, transformers 5.17.0 (`measured-by-us`): Qwen3Guard-Gen-0.6B **15m8.321s**; Granite Guardian 3.0-2b **4m1s**; 3.1-2b **3m59s**; Detoxify **28s**; Qwen3Guard-Gen-4B **52m6s**. Fixture demo path **1.312 s** (`review.md`, clean-room) — `fixture`, measures no guardrail.

The tally, one frozen set `set_hash=8def883fed6824cb…`, 300 pairs, harmful arm 200 / safe arm 100 (`parity-report-2026-09-18.md` T1, `measured-by-us`):

| Model | Declared languages (vendor-reported) | EN recall [CI] | VI recall [CI] | Gap pp | Indeterminate |
|---|---|---|---|---|---|
| Qwen3Guard-Gen-0.6B | "119 languages", vi not named | 91.5 [86.4–94.8] | 87.8 [81.9–92.0] | 3.7, CIs overlap | 16.0% (96/600) |
| Qwen3Guard-Gen-4B | same inherited claim | 92.1 [87.2–95.3] | 89.6 [83.9–93.4] | 2.5, CIs overlap | 18.3% (110/600) |
| Granite Guardian 3.0-2b | "only trained and tested on English data" | 94.0 [89.8–96.5] | 68.5 [61.8–74.5] | 25.5, no overlap | 0.0% |
| Granite Guardian 3.1-2b | same card | 93.0 [88.6–95.8] | 64.5 [57.7–70.8] | 28.5, no overlap | 0.0% |
| Detoxify multilingual | 7 languages, vi absent | 16.5 [12.0–22.3] | 1.5 [0.5–4.3] | 15.0, both near floor | 0.0% |

Real-input result: the diff above. Matched-pair reading on the reference model: 2.0 pp (155 of 200 items both determinate; 5 VI-only vs 3 EN-only misses; McNemar p ≈ 0.73). Safe arm, 0.6B: VI false-positive 25.0% [17.0–35.2] vs EN 16.3% [9.7–25.8], direction stable under every indeterminate treatment (`review.md` S9). No commercial endpoint run (`parity-report` §0).

---

## 2b. Research quality

The verdict-driving table. For each axis: the strongest claim the project's own `docs/` (explore, plan, review, market-check, customers) plus root `docs/markets` make; its source kind; what the stage-2 pulls (C3, C4) did to it; and the research — not code — that would close it. "Confirmed" means the pull re-found the same primary; "could not check" is recorded with the channel.

| Axis | Strongest claim in the docs | Source kind | Pull result (C3/C4, 2026-09-18) | Research that would close it |
|---|---|---|---|---|
| **Buyer** | An engineer at a Vietnamese company running a public VI chatbot, "findable in person": AI Hay (HCMC, $10M Series A, 100M+ Q&A/month), Vbee, Filum AI; 8 profiled, CTOs named (`success-vision.md` §3; `hcmc-candidates.md`) | company-stated (VnEconomy 2025-07-02, VIR 2025-04-14); 6 of 8 profiles from search snippets | **Confirmed in kind, not in demand**: 23 VI chat products named (C3 §1, ≥20 bar); no safety statement, vendor or guardrail on any of 8 pages reached (C3 §14). **Could not check**: LinkedIn job counts (Chrome down, C3 §2); 0 live LLM-safety posts on TopDev/ITviec/VietnamWorks. **Contradicted in scope**: "in person" holds for 3 of 8 HCMC-HQ (AI Hay, Filum AI, MoMo) | Three Mom-Test conversations (AI Hay, Filum AI, MoMo): what filter runs today, was Vietnamese ever measured, what happened last time a Vietnamese message was wrongly blocked/passed — past tense only. One Chrome pull: LinkedIn/TopCV at the 8 for `guardrail\|content moderation\|LLM safety`. Fill rows 9–12 of the frozen list |
| **Problem** | Guardrails are "chosen for English and never measured on Vietnamese"; Azure's own page: "the quality might vary … do your own testing"; measured: the VI/EN gap tracks the vendor's declared language claim (`mvp-spec.md` §2; `market-check.md` §1a; `sweep-2026-09-18.md`) | vendor-reported (Azure, Llama Guard cards) + measured-by-us (5 open-weights models) + inference ("nobody measures it") | **Confirmed**: Azure `vi` Supported, specially-trained blank (C3 §3, §6); Llama Guard 4 list stops at Thai (§6); no VN benchmark since 2026-09-01 (§15). **Could not check**: any VN chatbot harm incident — 0 found, global stories only (§13); commercial endpoints unrun (§5, requires-human). **Contradicted as a product story**: on the two models claiming Vietnamese the gap is a null (3.7 / 2.5 pp, overlapping CIs); the 25.5–28.5 pp gaps are on cards that say "English only" | The paired run on ≥1 commercial endpoint the 23 actually run (Azure F0 5,000 records $0; OpenAI moderation $0) — a measurement pull, one account, `requires-human`; Vietnam-billing allowed is itself unknown (C3 §3–4). Frequency: ask the 3 buyers for one dated Vietnamese false-positive or miss ticket. Native-text check: any native VI corpus with an EN twin (bundle has none, `parity-report` c.3) |
| **Price** | "priced per engagement — `unknown`"; only anchor ITviec 54.9M VND/mo (>8-yr back-end, gross, n=1,839); US band $8k–$50k inadmissible; Cobalt $3,500/test is the US floor (`hcmc-opener` §2; `market-check` §6b UNRESOLVED; `docs/markets/ai-attack-defense-services.md`) | vendor-reported salary; vendor-published US price; aggregator US band | **Confirmed absent**: 6 VN pentest vendors and 4 ISO-42001 certifiers publish no price — quote-only (C3 §9–10); Upwork VN AI band $25–80/h confirmed (C4 §2). **Could not check**: any buyer-stated number — no buyer asked (§21 requires-human). Nothing contradicted; the docs already say unknown | One quote request each to Viettel Cyber Security, VSEC, CyStack as a buyer for "kiểm thử an toàn chatbot AI tiếng Việt" (`requires-human`, phone/email). Mom-Test past tense to the 3 buyers: what did you pay for your last pentest, who signed it. The sibling ads probe's 15M VND / 50% deposit is the template ask |
| **Incumbent** | "A Vietnamese guardrail regression CI gate is `promptfoo eval` against a Vietnamese test file, in CI, today, free" — what promptfoo lacks: a labelled VI corpus with an EN arm and a run-to-run diff subcommand; SEA-HELM holds the paired corpus switched off (`market-check.md` §2–3; `mvp-spec.md` §3; `parity-report` §6) | vendor-reported via `gh api` docs; SEA-HELM source read; **never run** | **Confirmed**: promptfoo subcommand list has no `compare`/`diff`, no shipped multilingual corpus (C3 §8, re-fetched); SEA-HELM `safeguard_general` off, README unchanged 151 days (§7); no guardrail product on the SEA-LION board (§22). **Could not check**: promptfoo first-hand; PyRIT datasets/languages; Lakera's language list; Giskard/Patronus diff features | Run promptfoo on this machine against the bundle as CSV, twice, and record whether `view`/the GitHub Action surfaces a before/after with a failing exit — an incumbent run, not a build. Read PyRIT's dataset index and Lakera's docs for a language list. Search promptfoo issues for "compare runs" and date the newest |
| **Regulation** | Primary statute: Điều 14 is process duties, no performance threshold; medium-risk "independent assessment" is the regulator's option; high-risk certification only on a PM list that "does not exist"; no decree found (`re-pick.md` §2, 2026-09-17; `market-check.md` §5) | filed — gazette PDF transcribed from page images; pages 3, 10–18 untranscribed | **Confirmed dates** (in force 2026-03-01; 2027-03-01 / 2027-09-01). **Superseded, not contradicted**: Nghị định 142/2026/NĐ-CP issued 2026-04-30, effective 2026-05-01 (search synthesis, primary not fetched) and Quyết định 33/2026/QĐ-TTg, 46 high-risk systems in 6 fields, effective 2026-08-15 (`filed`, mst.gov.vn fetched) now exist — the docs' "no decree, no list" is stale as of 2026-09-18. **Could not check**: Điều 8 portal URL and notified-system count (C3 §11; C4 §17); any enforcement action (§12). Not a demand number under any reading (F9) | Fetch NĐ 142/2026 and QĐ 33/2026 primary text (vbpl.vn, Chrome): does any of the 46 categories cover a public consumer chatbot; does the decree define assessment content or name testing. Count the Điều 8 portal. Transcribe statute pages 10–18 (penalties). Re-run `re-pick.md` P1–P3 to a definite Revive / Hold / Stop |
| Product (context only) | Instrument runs; 5 real models measured; Granite diff exit 1; 43 tests; S18 open on master; S11 untested (§2, §3) | measured-by-us; one agent for the tests | not a pull item; not a verdict input per the reweight | — |

Reading across the rows: the docs are strongest where a primary text or a card could be quoted (regulation, incumbent, problem-as-card) and weakest exactly where money would come from (buyer, price) — both rest on zero conversations. Nothing in the pulls contradicted a factual claim the docs made; two became stale (decree, list) and the product story the problem row implies is contradicted by the project's own measurement. The research picture is honest and incomplete in the same place three passes in a row: nobody has asked a buyer anything.

---

## 3. Proven vs asserted

Context under the reweight — product completeness, not a verdict input.

| Proven — second agent from clean, or real input | Asserted — spec, page, vision only |
|---|---|
| Every pre-registered fixture number reproduced clean-room; 1.312 s (`review.md`) — `fixture` | `local_model` "fully offline at run time" — S11 unenforced, never provoked (`fix-log` deferred) |
| Wilson bounds re-derived independently and by hand, exact (`review.md`; 9b hand check 144/164 → 87.8, [81.9, 92.0]) | `diff` "refuses cross-adapter" — true for adapter *name* only; S18 open (`diff.py:94-104`; C3 §19) |
| Zero socket calls on default path, positive control (`e2e-test.md` §10) — default path only | "The gap tracks the vendor's declared language claim" — post-hoc pattern on 3 families, not a held-out prediction |
| 5 real open-weights guardrails, 600 prompts each; Granite diff exit 1 (`sweep-2026-09-18.md`) | "No paired VI/EN guardrail-product measurement exists" — absence, brace-listed, checked 2026-09-17 |
| S1/S2/S3/S6/S7/S10 fixed failing-first; 43 tests, 0 failures (`fix-log`) — one agent, not reproduced by a second | "About fifteen minutes on one machine" (opener) — true for 0.6B only; 4B is 52m6s |
| Page: 573 fields recomputed, 0 mismatches (`ORCHESTRATION` `bd74ad9`) — not re-run here | "Priced per engagement" — no price exists (A4) |
| `set_hash` unchanged across `bundle.json` rebuilds (`review.md`) | Azure F0 / OpenAI moderation "one sign-up away" — Vietnam-billing allowed: unknown (C3 §3–4) |

Bug-class check — for each "X cannot happen", the input that makes X happen, and whether a test reaches it:

| "X cannot happen" | Constructed input | Exit / result | Reached by a test? |
|---|---|---|---|
| diff refuses mismatched adapters | Granite 3.0-2b vs Detoxify, both `local_model` | exit 1, spurious REGRESSION, +183 misses (`raw/sweep-diff-crossfamily-demo.txt`) | **No** — fix in stash `wave10b-s18-partial-2026-09-18`, off master |
| indeterminate is never a pass | 39 VI misses → `Controversial` | pre-fix exit 0; post-fix exit 1, "rose 19.5 pp" (`fix-log` S1) | Yes, 13 tests |
| report numbers tie to the frozen set | bundle truncated to 150, header stale | pre-fix exit 0, gap −0.9; post-fix exit 2 (S2) | Yes, 9 tests |
| secrets never persist | key in URL query and `body_template` | pre-fix verbatim; post-fix masked to last 4 (S3) | Yes, 6 tests |
| `local_model` runs offline | `HF_HOME=$(mktemp -d)` worker start | **not run** (needs GPU/venv) | **No** — restated, not tested |
| `http_json` failure → indeterminate | `{"flagged": null, "error": …}` 200 body | pre-fix counted PASS; post-fix `None` (S10) | Yes, 11 tests |
| no ViHOS text anywhere | grep + 3 sampled rows incl. a personal name | 0 hits (`e2e-test.md` §12) | Yes |
| licence gate withholds non-permissive text | "Limited", "Unlimited", "CC BY 4.0" | pre-fix wrong both directions; post-fix exact-match (S7) | Yes, 7 tests |

Two of eight guards are open (S18 shipped-unfixed; S11 never attacked). The one that matters for the product's single claim — a gate that ignores indeterminacy — was found, constructed, and closed.

---

## 4. Incumbent gap, in the incumbent's words

| Incumbent | Version / date inspected | How inspected | Its own sentence on the gap | Price | A6 reading |
|---|---|---|---|---|---|
| promptfoo | 0.123.0 (2026-09-10, `mvp-spec` — not re-verified); docs re-fetched 2026-09-18 | docs only, never run | subcommands "`init`, `eval`, `view`, `share`, `auth`, `cache`, `code-scans`, `redteam`, `debug`" — no `compare`/`diff`; guide says "test multilingual prompts" yourself (C3 §8) | Community $0; Enterprise custom (C4 Additional) | **docs-only on the primary incumbent → UNKNOWN** |
| SEA-HELM | `data/README.md` commit 2026-04-20; leaderboard "Aug 5, 2026", pulled 2026-09-18 | source via `gh api`; leaderboard via Chrome; not run | "Omitted from the safeguard category pending further checks/data cleanup for the dataset (e.g. aegis2)" (C3 §7) | free, MIT | inspected at source; the paired task exists, switched off 151 days |
| Azure AI Content Safety | pricing + language pages, 2026-09-18 | docs only; not run | `\| Vietnamese \| vi \| \| ✔️ \|`; "the quality might vary. In all cases, you should do your own testing" (`market-check` §1a) | F0 5,000 records/mo $0; S0 $0.38/1,000 (secondary) | not run — requires-human account |
| OpenAI moderation | guide, 2026-09-18 | docs only | "The moderation endpoint is free to use." No language statement (C3 §4) | $0 | not run — requires-human account |
| Llama Guard 4 | PurpleLlama `MODEL_CARD.md`, 2026-09-18 | docs only | "French, German, Hindi, Italian, Portuguese, Spanish, and Thai" — Vietnamese absent (C3 §6) | open weights; Replicate metered, unknown | not run; Llama Guard 3 8B gated manual approval |
| Lakera Guard | secondary snapshots 2025-10-01 / 2026-08 | **not inspected** — marketing only | "Observing 100+ languages in real-time" (`language-gap.md`) | Community $0, 10k req/mo; Enterprise custom | **not inspected — A6 FAIL row** |
| garak | 0.17.0 (2026-09-09); probe listing 2026-09-17 | source listing, not run | 43 probe modules, none a Vietnamese or paired corpus — inference from names (`mvp-spec` §3.2) | free | not run |
| PyRIT | 1.1.0 (2026-09-04) | **not inspected** | unknown — no language or dataset fact on file (`mvp-spec` §3.3) | free | **not inspected — A6 FAIL row** |
| Giskard | pricing page 2026-09-18 | docs only | free OSS tier; Enterprise custom (C4 Additional) | $0 / custom | diff feature not checked |
| Qwen3Guard, Granite Guardian, Detoxify | HF revisions pinned, 2026-09-18 | **run first-hand, 600 prompts each** | cards quoted in §2 | Apache-2.0 | these are measured objects, not instrument incumbents |

The instrument's claimed gap — a stored-run, `set_hash`-gated, per-category, per-language diff with exit codes — is stated in promptfoo's own subcommand list (absent) and bounded to channels checked 2026-09-18. It is not confirmed by running promptfoo. Independent supply with no pull (F2): SEA-HELM holds both halves of the paired corpus switched off; promptfoo ships `language` + `moderation` + CSV ingestion. That is evidence against a market, not for one.

---

## 5. Bottom-up sizing, arithmetic shown

```
N_buyers        = 23                    [measured-by-us, C3 §1: 8 profiled (hcmc-candidates.md) + 15 from WebSearch;
                                         4 rows weak (Tiki, ACB, MB Bank, VNPT); 1 is a ministry; 0 contacted]
ARPU            = 15,000,000 VND/engagement  (≈ $593 at 25,306)
                                        [own judgement. Anchors: the sibling ads probe's pre-registered
                                         15.000.000 VND engagement (FRAMEWORK §C1 line 17, own judgement there);
                                         ITviec >8-yr back-end 54.9M VND/mo gross, n=1,839 (vendor-reported, C4 §1)
                                         → 15M ≈ 27% of one month; Cobalt $3,500/test, US (vendor-published,
                                         docs/markets/ai-attack-defense-services.md) ≈ 88.6M VND — the US floor,
                                         5.9× higher; Upwork VN AI engineer $25–80/h (vendor-reported, C4 §2).
                                         Market: Vietnam. No buyer has said any number (A4).]
attainable_share= 0.10                  [own judgement; §B5 ceiling without distribution evidence; 0 contacted]
engagements/buyer over 36 mo = 1        [own judgement; a re-run per vendor release is unpriced]
market_36mo     = 23 × 15,000,000 × 0.10 × 1 = 34,500,000 VND   (≈ $1,363)
founder_cost_yr = 658,800,000 VND       [ITviec 54.9M × 12, salary basis (market-check §6); ≈ $26,033;
                                         clinic-MCP revenue/hour requires-human (C4 §3) — not pulled]
ratio           = 34.5M / (2 × 658.8M = 1,317.6M) = 0.026   → FAIL at these inputs
ramp            = 1.0 (revenue spread evenly over 36 months) [own judgement]
months_to_2x    = 1,317.6M / (34.5M ÷ 36 = 0.958M/mo) = 1,375 months
```

Sensitivity, same N: at 100% share and 3 engagements per buyer, 23 × 15M × 3 = 1,035M VND → ratio 0.79, still < 1. Break-even price at 100% share, one engagement per buyer over 36 months: 1,317.6M ÷ 23 = **57.3M VND per company** — above one month of the >8-year salary band, from every one of the 23. On the named Vietnamese list the 2× bar is unreachable at any price a Vietnamese buyer has been anchored to; only a US-priced buyer ($3,500 ≈ 88.6M VND) clears 57.3M, and no US buyer is on the list. A5 stays UNKNOWN because ARPU is own judgement, not a buyer number — but no admissible price on file flips it.

---

## 6. Unit economics, every input labelled

Honest shape: free instrument (MIT) + published measurement + paid measurement-and-CI-gate engagement.

```
price/unit   = 15,000,000 VND          [own judgement, §5 anchors]
COGS/unit, cash:
  GPU electricity per 600-prompt run = 0.0504 kWh × 2,204.0655 VND/kWh ≈ 111 VND
                                       … × 5,422 VND/kWh ≈ 273 VND
                                       [own calc on vendor-reported inputs: RTX 3060 Ti 200 W; 15m8.321s
                                        measured-by-us; QĐ 1279/QĐ-BCT 2025-05-09 average retail (filed via
                                        kingteksolar) vs business peak-hour 5,422 (search synthesis, unconfirmed)
                                        — side by side, C3 §17]
  buyer's guardrail is Azure: 600 records inside F0 5,000/mo = $0 [vendor-reported]; S0 $0.38/1,000 → $0.23 [secondary]
  MoR fee, if paid cross-border: 5% + 50¢ [vendor-reported, vietnam-sg-access.md] → 0.75M VND + 12,650 VND
COGS/unit, founder labour:
  hours/engagement = 24 h               [own judgement: run 28 s–52m6s measured; report + CI wiring unmeasured;
                                         the sweep agent did 4 runs + doc in 86 min (STATE.md 09:54→11:20 +07)]
  hourly rate      = $25–80             [vendor-reported, Upwork VN AI engineer band, C4 §2; clinic-MCP requires-human]
  labour           = 24 × $25–80 = $600–1,920 ≈ 15.2M–48.6M VND
GM (cash only)   = (15M − 273) / 15M ≈ 99.998%
GM (labour-loaded) = (15M − 15.2M) / 15M ≈ −1%  at $25/h;  (15M − 48.6M)/15M ≈ −224% at $80/h
  → price for 50% services GM at 24 h: ≥ 30.4M VND ($25/h) … ≥ 97.2M VND ($80/h)
CAC = (hours × rate + cash) / replies ÷ (paying ÷ replies)
  outreach hours = 4 h [own judgement: 7 messages + day-3 follow-ups, hcmc-opener §3]; cash 0
  expected replies from 7 targets = 7 × 3.43% = 0.24 … 7 × 10.3% = 0.72 … 7 × 16.86% = 1.18
                                       [vendor-reported: Instantly 2026; Expandi 2026 DM; Expandi warm-trigger, C4 §11]
  paying ÷ replies = unknown            → CAC = unknown
payback = CAC / (ARPU_m × GM)          → unknown (CAC unknown; ARPU_m for a one-off is undefined)
churn/mo = n/a (one-off engagement)    [own judgement]      LTV:CAC = unknown
```

A11 UNKNOWN on CAC. The computable half is the finding: at the only Vietnamese-anchored price, the engagement does not cover the founder's own hours at the Upwork floor. The services GM bar (≥50%) needs a price of 30.4M–97.2M VND, i.e. 0.55–1.8 months of the >8-year salary band per engagement, before any CAC.

---

## 7. Kill-test result

**Pre-registered rule, verbatim** (`docs/outcome/hcmc-opener-2026-09-18.md` §4, written 2026-09-18, before any outreach; mirrors `docs/plan/measurement-report.md` §5e):

> **PASS** — ≥1 run of `parity-vi` against a guardrail a contact operates, run by or with them, evidenced by **their** run record — AND ≥3 written replies from distinct organisations engaging with the number. **WEAK** — 0 buyer-side runs but ≥3 such written replies. Buys one 7-day extension, once. **FAIL** — Anything else.

Binding conditions there: list frozen before the first message (8 rows; rows 9–12 `unknown — not yet compiled`); Ministry of Public Security excluded, so denominator 7; "engaging with the number" = quotes a figure, asks for own number, or asks for a run; personal contacts excluded; stars/views excluded; one message + day-3 follow-up.

**Status: not run.** T0 = publication date, unset; page and repo unpublished (`ORCHESTRATION.md` "Nothing published"); mailto is `hello@example.invalid`; "Source on request" has no URL (`review.md` V9). 0 of 8 contacted (`hcmc-candidates.md` caveats). **Who must run it:** the user — publishing, the account sign-up and the messages are all `requires-human` (C3 §5, §20, §21).

**Cost to run** (own judgement, hours; cash 0 VND; no code step counted, per the reweight): publish repo + page, replace two placeholders — 2 h ("minutes once a URL exists", `review.md` 9b); read the unwritten report review or accept the report unreviewed — 1 h; 7 messages + day-3 follow-ups — 4 h; gate bookkeeping — 1 h. **8 h, $0, 14 days (+7 WEAK).** Earliest: publish 2026-09-19 → gate 2026-10-03, WEAK extension 2026-10-10. Not part of the gate, listed for the §2b problem row: one commercial-endpoint run on the user's Azure F0 or OpenAI account, +1 h ("a user sign-up plus an hour", `review.md` item 4; Vietnam-billing allowed unknown, C3 §3–4). Not counted at all: finishing stash `wave10b-s18-partial-2026-09-18` (code; context only).

**Second pre-registered rule on file**, `docs/plan/re-pick.md` §5 (2026-09-17): P1 Điều 8 portal count ≥50 medium/high systems AND P2 decree specifies assessment content → Revive; P1 <50 or no decree → Hold; none of P1–P3 → Stop. C3 §11 partly ran it: P2 — Nghị định 142/2026/NĐ-CP exists (issued 2026-04-30, effective 2026-05-01; scope: portal, national database, risk classification — search synthesis, primary not fetched); high-risk list exists (QĐ 33/2026/QĐ-TTg, 46 systems, 6 fields, `filed`, mst.gov.vn fetched); P1 — portal URL and count `unknown — checked vanban.chinhphu.vn, mst.gov.vn, thuvienphapluat.vn (403) 2026-09-18`; P3 — not checked. Result: **indeterminate** — not Stop (a decree exists), not Revive (no count). Its own text: a Hold "is explicitly not a licence to build 2.1 or publish 4.1 as a consolation."

---

## 8. Three scenarios

Rate = §B14: higher of clinic-MCP revenue/hour (`requires-human`, not pulled) and the HCMC AI-engineer contract band **$25–80/h** (vendor-reported, Second Talent citing Upwork, 2026-08/09, C4 §2). Both ends shown; the clinic rate, if higher, raises every cost. Context: Numbeo HCMC single person $492.90/mo excl. rent (analyst-derived, Aug 2026, C4 §4). All p and value cells are **own judgement**.

| Scenario | Hours | Cash | First dollar | p(gate) | Value at gate | EV = p×value − cost |
|---|---|---|---|---|---|---|
| Do nothing (archive; publish as-is at most) | 2 | $0 | never | — | reputation only | **−$50 to −$160** |
| Minimum viable commitment (run the gate, nothing else) | 8 (§7 breakdown) | $0 | 2026-10-17 (gate + invoice, if PASS) | 0.05 | $593 — one 15M VND engagement | 0.05×593 − (200 to 640) = **−$170 to −$610** |
| Full commitment (vision §1: instrument + published commercial measurement + paid service; 2027-09 win) | 240 over 12 weeks | $100 | 2026-11-30 | 0.15 | $13,633 — 23 × 15M VND, every named buyer once (ceiling) | 0.15×13,633 − (6,000 to 19,200) − 100 = **−$4,055 to −$17,255** |

How p(gate) = 0.05 was set: 7 targets; P(≥3 replies) by binomial at the Expandi warm-trigger 16.86% ≈ 0.10, at the DM platform rate 10.3% ≈ 0.03; a buyer-side run given replies ≈ 0.5 → 0.015–0.05. Proximity (3 of 8 HCMC-HQ, named CTOs) is credited by taking the top of that range. p = 0.15 for full commitment assumes twelve weeks of in-person follow-up triples the chance of one paying engagement; no evidence for that multiplier exists.

Full-commitment hours (own judgement): 4 commercial-endpoint runs 8 h; S18/S11 fixes 8 h; native-Vietnamese corpus question (ViHOS excluded, nothing native in the bundle — `parity-report` caveat 3) 40 h; 12-org outreach 24 h; 3 engagements × 24 h = 72 h; report/page upkeep 40 h; slack 48 h. Cash: Claude Code Pro $20/mo (secondary aggregation, C4 Additional; tier the founder pays `requires-human`) × 3 = $60; Azure S0 overage ≤ $1; MoR fees only on receipt.

**A negative EV in every row on cash value is the finding.** The minimum commitment buys information — a definite stop or a definite buyer for 8 hours — not expected revenue. The full commitment loses $4k–$17k of founder time against a ceiling of $13.6k if all 23 named companies bought once at a price none has stated.

---

## 9. Known traps checked (§F)

| # | Check run | Result |
|---|---|---|
| F1 | For each demand claim, which humans were asked | Zero. `hcmc-candidates.md` reads "companies hiring for LLM capability, not for LLM safety evaluation … is evidence for the project's thesis" — a search-level negative read as evidence; **rejected**. A1, A3, A8 set UNKNOWN, not FAIL, not PASS |
| F2 | Absence claims carry `{A, B, C} — checked <date>` | Yes: promptfoo diff `{caching, command-line, GitHub Action docs, 2 WebSearches} 2026-09-18`; paired measurement `{SEA-HELM, promptfoo, garak, PyRIT, Azure, OpenAI, Perspective, AWS} 2026-09-17`. Reviewer could open none (no web) — **partial**. Independent supply with no pull found twice (SEA-HELM paired task off; promptfoo `language`+`moderation`) — counted against |
| F3 | Constructed failing input per "cannot happen" | §3 table: 6 of 8 tested with exit codes; S18 constructed, exit 1, unfixed on master; S11 restated, not tested |
| F4 | Measured object is a guardrail product, not a prompted LLM | All five are guardrail models (Qwen3Guard, Granite Guardian, Detoxify), open-weights, run locally — not commercial endpoints; stated in every doc; commercial run `requires-human` (C3 §5) |
| F5 | Stars/views used as demand | None. promptfoo 25,180 stars appears only as incumbent context; no star count for `parity-vi` exists (unpublished) |
| F6 | "How inspected" column | §4: promptfoo docs-only → A6 UNKNOWN; Lakera, PyRIT not inspected → FAIL rows |
| F7 | Every number cites raw or primary; prices carry their market | C3/C4 and measured docs cited inline; 15M VND and 54.9M VND labelled Vietnam, $3,500 labelled US. One compiled→compiled cite: the 8 profiles via `hcmc-candidates.md`, whose `raw/buyer-profile-pulls-2026-09-18.md` was not read — flagged |
| F8 | Fixture numbers tagged; none in §1/§5/§6 | 8.2→17.8 pp, 76.0→0.0, 88.5/80.3, 1.312 s appear only in §2/§3 tagged `fixture`; §1, §5, §6 carry real or own-judgement numbers only |
| F9 | Law as demand | A7 cites Law 134 / NĐ 142/2026 / QĐ 33/2026 as events only; A3/A5 use none. The 46 are system *types*, not registered companies (C4 §17); no enforcement action (C3 §12). The page carries **two** law sentences (`review.md` V8) — a standing finding, a disclaimer not a claim |
| F10 | Vendor-stated read as independent | AI Hay "100M+ Q&A/month" company-stated, not used; Qwen "119 languages" vendor-reported, not used as evidence of Vietnamese; N=23 is measured-by-us, though 4 rows rest on secondary press |
| F11 | Conflicts side by side, none averaged | Electricity 2,204 vs 5,422 VND/kWh; FX 25,306 vs 25,617; Belkins 4.86% vs 0.45%; ViHSD licence four ways; Vbee 1M+ vs 2M+; salary bands ITviec vs Second Talent vs reco-vn. Verdict sensitive to the reply rate (3.43% vs 16.86% moves p(gate) 0.01→0.05) and to nothing else |
| F12 | Absolute dates; runtimes measured or `unmeasured` | All dates absolute; runtimes 15m8.321s, 4m1s, 3m59s, 28s, 52m6s, 1.312 s measured; hours per engagement `own judgement, unmeasured`; opener's "fifteen minutes" is 0.6B-only (§11) |

---

## 10. Verdict

**The three threads, separated, before any verdict.**

(i) *The "Vietnamese gap" thesis.* Two models that claim broad language coverage show 3.7 pp [86.4–94.8 vs 81.9–92.0] and 2.5 pp [87.2–95.3 vs 83.9–93.4] — overlapping intervals, matched-pair 2.0 pp, McNemar p ≈ 0.73. That is a null. Two models whose card says "only trained and tested on English data" show 25.5 and 28.5 pp with no overlap. That is the card, measured. Detoxify's 15.0 pp sits on 16.5% English recall — a label mismatch. **A measurement that confirms the vendor's own language claim is not a product.** It is a free, one-time confirmation that the card is honest; a buyer running an English-only guardrail on Vietnamese traffic has a procurement error the card already discloses, and `python parity.py run` settles it once, for nothing. What the cards do *not* predict — 16.0%/18.3% `Controversial`, VI benign over-blocking 25.0% vs 16.3% — is real, is about one model family, and is not the product the page sells. On the thesis, the user's prior holds: 0 of 5 measured models produced the "your multilingual guardrail is worse in Vietnamese" story.

(ii) *The instrument.* `diff.py` refuses `set_hash`, `set_id` and adapter-name mismatches (exit 2), regresses on a >5 pp Vietnamese recall drop in any n ≥ 5 category, net new misses > 0, a >5 pp rise in Vietnamese indeterminates, or an effective-n collapse (exit 1), else 0 — read from code, exercised on two real IBM releases. promptfoo's published subcommand list has no `compare`/`diff` (C3 §8). This is not bullshit; it is 14,147 bytes of stdlib Python with 43 tests, an open blind spot (S18, family not checked), and one unattacked claim (S11). Its moat is the time it takes promptfoo's maintainers to add a subcommand and SEA-HELM to delete one README line (151 days unchanged): own judgement, weeks to months, below the 6-month bar.

(iii) *The services wedge.* 8 candidates, 3 HCMC-headquartered, named CTOs, 0 contacted; 23 named nationwide. Law 134 (2026-03-01), Decree 142/2026 (2026-05-01) and the 46-system high-risk list (2026-08-15, deadlines 2027-03-01 / 2027-09-01) are dated events with primary sources; none mentions guardrail testing; no enforcement action, no VN chatbot incident, no live LLM-safety job posting, no price from any of 10 vendors. On demand, the user's prior is **UNKNOWN, not confirmed** — nobody has asked a buyer, and on the named list the bottom-up cannot reach 2× salary at any Vietnamese-anchored price (§5).

**Steelman "stop now."** Five measured models, zero that show the sold story; the only defensible findings are properties of one open model family that no buyer runs; N=23 named buyers cannot fund one founder at any price a Vietnamese buyer has been anchored to; the instrument's unique feature is a subcommand away from a free, OpenAI-owned incumbent with 25,180 stars; every gate EV is negative on cash; and the pattern of this project — three passes of research substituting for one conversation — is the one `re-pick.md` §5 already diagnosed. Eight more hours is the same substitution with a smaller number.

**Steelman "this is the one."** It is the only project of three past the real-input hole, with a real vendor regression printed and exit 1 read directly; it is the only one whose buyer is one district away with a named CTO; the two robust findings (1-in-6 no-verdict, Vietnamese over-blocking) are support-ticket-shaped and unpublished by anyone; the commercial-endpoint measurement is one account sign-up from existing; the honesty discipline survived two adversarial reviews with 0 numeric discrepancies; and the gate is 14 days, $0, pre-registered, with a FAIL that retires the project cleanly. Nothing else in the portfolio can be killed or confirmed that cheaply.

**Verdict.** Worth **8 hours / $0 over 3 weeks** to reach gate **G** = the pre-registered 14-day buyer-conversation signal (≥1 buyer-side run record AND ≥3 written replies from 7 named organisations engaging with the number, `hcmc-opener-2026-09-18.md` §4) — **else stop; keep as calling card.** G is a conversation gate, not a build gate: it closes the two empty §2b rows (buyer, price) that no pull can close and that the docs have left empty for three passes. Ceiling "gate first" because A3 and A6 are UNKNOWN, not FAIL: nobody has been asked and the primary incumbent has not been run, and the gate that answers the first is reachable inside 90 days at zero cash. No build hour is licensed by this verdict — not S18, not the vision — because the full-commitment row is EV-negative at every own-judgement input and stays negative even if all 23 named companies buy once. The single number that flips "gate first" to "build" is **one buyer-stated price ≥ 30.4M VND** (the 50% services-GM floor at 24 h × $25/h, §6) on or before 2026-10-10; the single number that flips it to "stop now" is **0 written replies by 2026-10-03**. The calling card — instrument, 5-model measurement, report — is worth the 2 hours it costs to publish and no more.

---

## 11. Claims in the project's own docs not verified or contradicted

| file:line | Claim | Status | Consequence for §1 |
|---|---|---|---|
| `parity-report-2026-09-18.md` §8, §10 c.11 | S18 family-aware refusal "scoped … not yet applied" | unverified as fixed — still open on master; stash `wave10b-s18-partial-2026-09-18` (C3 §19, `diff.py:94-104` read) | A10 second half incomplete |
| `hcmc-opener-2026-09-18.md` §1 | "about fifteen minutes on one machine" | contradicted by `sweep-2026-09-18.md`: 52m6s (4B), 28 s (Detoxify); true for 0.6B only | opener overstates; A8/A12 pitch |
| `hcmc-candidates.md` caveats | vocabulary gap in job posts "is evidence for the project's thesis" | contradicted by F1 — search-level negative | A1 UNKNOWN, not PASS |
| `hcmc-candidates.md`, `success-vision.md` §3 | Vbee "1M+ customers (06/2023)" vs "2M+ users" | unverified — unreconciled conflict | none; N count unaffected |
| `hcmc-candidates.md` (6 of 8), C3 §1 (Tiki, ACB, MB, VNPT) | profiles rest on WebSearch snippets | unverified live pages | A2 count carries 4 weak rows |
| `raw/sweep-diff-granite-3.0-to-3.1.txt` | current gate output | artifact produced by pre-`b3083bd` `diff.py`: no `max-new-indeterminate-pp` in header, no Δ suffix on the INDETERMINATES line; not re-run after the S1 fix | none for verdict (0 new indeterminates); A10 artifact stale |
| `parity-report-2026-09-18.md` §6, footer | "61 open-weight and 9 closed-weight models" | partly contradicted by `seahelm-scores.md`: 51 open-weight rendered on VI page; closed-weight rows never surfaced — unresolved | none; published-report error |
| `parity-report-2026-09-18.md` §0, c.6 | free tiers "both require creating an account" — one sign-up away | unverified for a Vietnam-billed account: Azure F0 and OpenAI VN availability `unknown` (C3 §3–4) | A10 commercial line may cost more than 1 h |
| `mvp-spec.md` §3.1 | promptfoo 0.123.0 (2026-09-10) | unverified — C3 §8 re-checked docs, not the version | A6 date column |
| `parity-report` §6, `mvp-spec` §3.1 | promptfoo "25,180 stars" | unverified currency — from `docs/markets/ai-attack-defense.md`, pass 1, 2026-09-16 | A9 context only |
| `fix-log-2026-09-18.md` | "43 tests, 0 failures" | unverified — one agent; no second-agent run; not re-run here | A10 "proven" column caveat |
| `ORCHESTRATION.md` `bd74ad9` | page "573 fields cross-checked, 0 mismatches" | unverified — not re-run here | none |
| `sweep-2026-09-18.md` cross-model | "four out of five … consistent with 'the gap tracks the vendor's language claim'" | unverified as a prediction — post-hoc on 3 families; Detoxify uninterpretable by its own caveat | §10(i) treats it as a card confirmation |
| `language-gap.md` | ViHSD cited as arXiv 2103.10069 | contradicted — 2103.11528 (`market-check.md` §2 iv) | none |
| `measurement-report.md` §1b (original) | `hate` 27.0 pp "intervals do not overlap" | contradicted, corrected in place (S4): overlap 10.2 pp, 2 discordant of 32 | none — correction on file |
| `e2e-test.md:10, :725` | `demo-data.json` sha256 `581a4320…` unchanged | contradicted — `42f17888…` after wave 10 (S16); dated correction on file | none |
| `hcmc-opener` §3 | 12-organisation target | unmet: 8 rows, 1 excluded → denominator 7; rows 9–12 `unknown — not yet compiled` | A2 |
| C3 §2 | LinkedIn job counts | unknown — Chrome never connected; TopDev/ITviec/VietnamWorks: 0 live LLM-safety posts | A2 buyer's-engineer evidence absent |
| C3 §11, C4 §17 | Điều 8 portal URL and notified-system count | unknown — checked vanban.chinhphu.vn, mst.gov.vn, thuvienphapluat.vn (403) 2026-09-18 | `re-pick.md` P1 indeterminate |
| `review.md` S11 | `local_model` "fully offline at run time" (`prototype/README.md:113`) | unverified — PLAUSIBLE, never provoked; patch written, not applied (`fix-log`) | A10 "every cannot-happen attacked": no |

---

## 12. Caveats

- No web access: no incumbent was opened by this reviewer (F2/F6 partial); every vendor sentence in §4 is as C3 or the project's raw pulls transcribed it, re-verified by the C3 agent 2026-09-18 without Chrome.
- No git and no GPU: the 43 tests, the 573-field page cross-check, the five model runs and the Granite diff were not re-executed; run records were not re-parsed. §2 rests on `raw/sweep-*.txt` and the execution docs, not on a second run.
- The founder's clinic-MCP revenue per hour, HCMC burn, Claude Code tier and any bank/KYC outcome are `requires-human` and absent; §6 and §8 use the Upwork band at both ends instead. If the clinic rate exceeds $80/h every EV in §8 is worse than shown.
- Every price, share, hours-per-engagement and probability in §5, §6, §8 is own judgement with its anchor named; no buyer has stated a price, and the arithmetic is laid out so one input can be changed and the ratio recomputed.
- The 23-company count includes a ministry, four rows resting on secondary press, and "VNG" and "Zalo/Kiki" collapsed to one; it counts public Vietnamese-language chat products, not guardrail buyers — no company on it is known to run any guardrail (C3 §14: no safety statement on any page reached).
- `hcmc-candidates.md` was cited as a compiled file; its raw source `raw/buyer-profile-pulls-2026-09-18.md` was not in this review's read list.
- FX is the 2026-07-27 SBV rate, not the review-date rate (unknown, C4 §5); at 25,617 every USD figure moves by ~1%.
- Electricity uses the average retail tariff and an unconfirmed business peak rate; the standard household/small-business tier was not located (C4 §15). COGS is negligible under any of them.
- The commercial-endpoint run that C3 §5 marks as the A10 KILL has not happened; whether a Vietnam-billed Azure or OpenAI account can be opened at all is unknown. If it cannot, the "one sign-up" route in §7 is not $0 and not 1 h.
- The verdict is the user's call; this file produced the numbers, the two steelmen and the §D10 sentence it was asked for.

---

## Files read

Root and governing: `CLAUDE.md`; `projects/CLAUDE.md`; `projects/investment-review/FRAMEWORK.md` (whole); `projects/investment-review/raw/c3-parity-vi-pulls-2026-09-18.md`; `projects/investment-review/raw/c4-cross-cutting-pulls-2026-09-18.md`; `projects/ORCHESTRATION.md` (lines 716–924, "SESSION 2026-09-18" onward); `docs/markets/ai-attack-defense.md`; `docs/markets/ai-attack-defense-services.md`.

Project `projects/ai-attack-defense/`: `CLAUDE.md`; `docs/plan/niche-and-solutions.md`; `docs/plan/re-pick.md`; `docs/plan/measurement-report.md`; `docs/review/market-check.md`; `docs/design/mvp-spec.md` (with its three dated corrections); `docs/execution/real-run-2026-09-18.md`; `docs/execution/sweep-2026-09-18.md`; `docs/execution/fix-log-2026-09-18.md`; `docs/execution/e2e-test.md`; `docs/outcome/review.md` (9a + 9b + buy/no-buy); `docs/outcome/success-vision.md`; `docs/outcome/parity-report-2026-09-18.md`; `docs/outcome/hcmc-opener-2026-09-18.md`; `docs/customers/hcmc-candidates.md`; `docs/explore/seahelm-scores.md`; `docs/explore/language-gap.md`; `STATE.md` (last 300 of 707 lines).

Prototype and measured output: `prototype/harness/` and `prototype/harness/adapters/` directory listings (`ls -la`); `prototype/parity.py`; `prototype/harness/diff.py`; `prototype/harness/scoring.py`; `prototype/harness/adapters/local_model.py`; `raw/sweep-diff-granite-3.0-to-3.1.txt`; `raw/sweep-report-qwen3guard-4b.txt`.

Not read, named: `raw/buyer-profile-pulls-2026-09-18.md`, `raw/sweep-diff-crossfamily-demo.txt`, `raw/endpoint-shape-pulls-2026-09-18.md`, `raw/seahelm-leaderboard-pulls-2026-09-18.md`, `site/index.html`, `prototype/tests/`, `prototype/harness/adapters/local_model_worker.py`, `docs/execution/build-log.md` — cited only through the files above.
