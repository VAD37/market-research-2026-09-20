# Investment review — framework

2026-09-18. Fable. Stage 1 of `projects/investment-review/` (`ORCHESTRATION.md` §"Investment review"). Governs stages 2 (Sonnet pulls into `raw/`), 3 (per-project reviews), 4 (`PORTFOLIO.md`).

**The decision served.** A solo technical founder in Ho Chi Minh City, with a clinic-admin MCP side business, an RTX 3060 Ti, a Claude Code subscription and Chrome, asks whether any of three MVPs built 2026-09-16..18 is worth his own time and money first, outside money second. He has said the earlier passes were wishful thinking. This file's job is to make wishful thinking impossible to write down: every criterion has a number or a named artifact as its pass bar, every number carries a source kind, and a failed KILL cannot be outvoted by a score.

**Label vocabulary, mandatory on every number:** `vendor-reported`, `analyst-derived`, `filed`, `company-stated`, `measured-by-us`, `requires-human`, `own judgement`, `unknown — checked <channel> <date>`. A number without a label is not a number.

**What the three projects are, in one line each, as measured (`SUCCESS-VISION.md`, `ORCHESTRATION.md`):**

| Project | Product | Proven today | Never done |
|---|---|---|---|
| `ai-ads-injection` | `aicrawlcheck` — offline access-log crawler verifier, 637 prefixes | 418/418 page-JS vs CLI; 5/5 spoofs caught (fixture) | Run on a real log; GoAccess/AWStats/Matomo inspected; buyer contacted |
| `agent-hermes-dashboard` | `Foreman` — recurrence-to-skill CLI over Claude Code hooks | 0.365 s; 19/19 tests; 13-key tally (fixture) | Live `Stop` hook observed; `/insights` inspected; published; buyer contacted |
| `ai-attack-defense` | `parity-vi` — VI/EN guardrail parity harness, 300 pairs | 5 open-weights guardrails measured 2026-09-18; Granite 3.0→3.1 REGRESSION | Commercial endpoint run; page published; any of 8 HCMC companies contacted |

---

## A. The investor's question list

Fourteen criteria. Pass bar is a number or a named artifact. Source of the bar is cited by name where a real standard exists; otherwise `own judgement`. Criteria marked **KILL** are gates, not weights (§E).

| # | Criterion | Pass bar | Why that bar |
|---|---|---|---|
| A1 | Problem severity and frequency | ≥5 of 10 buyer conversations name the problem unprompted AND it recurs ≥ monthly | *The Mom Test* (Fitzpatrick): only unprompted, past-tense accounts count. Frequency bar is own judgement — the ads reviewer showed a once-asked question cannot carry a subscription (`ai-ads-injection/docs/outcome/review.md` §5) |
| A2 | Buyer identity and reachability | A frozen list of ≥20 named organisations or people with a channel each; ≥3 reached in conversation within 14 days | 20 is the ads probe's own pre-registered n (`re-pick.md` §6); 3-in-14 mirrors the parity-vi gate (`hcmc-opener-2026-09-18.md` §4). Own judgement, pre-registered across projects |
| A3 | **KILL** — Willingness to pay | ≥1 deposit received, or 1 signed LOI, or ≥3 unprompted asks for a paid/hosted version from non-authors | Mom Test: commitment = money, time, or reputation. The 3-unprompted-asks rule is the hermes gate (`agent-hermes-dashboard/docs/plan/re-pick.md` §5). Stars, views, upvotes do not count |
| A4 | Price point | A number a named buyer said or paid, in their currency | A salary anchor (ITviec 54.9M VND/mo) or a US band ($8k–$50k) is not a price. `market-check.md` §6b for attack-defense: UNRESOLVED |
| A5 | Market size, bottom-up | `N_buyers × ARPU × attainable_share` ≥ 2× founder's annual opportunity cost within 36 months | Sequoia's *Writing a Business Plan* asks for bottom-up sizing; the 2× multiple is own judgement (one salary is break-even, not a business). Top-down TAM is inadmissible (§B5) |
| A6 | **KILL** — Incumbent coverage | Every named free incumbent run first-hand; the gap stated in the incumbent's own documentation words; no incumbent ships the gap in a changelog | Repo rule from `docs/method/evidence-rules.md`: unattacked absences survived ~1 in 5. GoAccess/AWStats/Matomo and `/insights` are still `unknown — never inspected` (`SUCCESS-VISION.md` caveats) |
| A7 | Why now | One dated event ≤12 months old that changes the buyer's situation, cited to a primary | Own judgement. Law 134/2025/QH15 (in force 2026-03-01, `filed`) qualifies as an event; it does not qualify as demand (`ai-attack-defense/docs/plan/re-pick.md` §2) |
| A8 | Distribution channel with cost | One channel with a measured reply or conversion rate and a cost per contact; ≥1 reply obtained in this project through it | Benchmarks on file, all vendor-reported: cold email 3.43% platform-wide, cybersecurity 4.86%, LinkedIn DM 10.3% (`docs/customers/first-customers.md`). A channel with no reply yet is a hypothesis |
| A9 | Moat and time-to-copy | Time for the named incumbent to copy ≥6 months, with the reason named (data, distribution, regulatory standing) | Helmer's *7 Powers* for the taxonomy; the 6-month bar is own judgement. `docs/findings/localization-play.md`: a prompt/UI layer is copyable "in an API update". "None" is an acceptable, honest answer |
| A10 | **KILL** — Technical proof on real input | The product's one moment has occurred on ≥1 real input not authored by the team, and every "X cannot happen" claim has a constructed input that makes X happen | `ORCHESTRATION.md` wave 9V: all three moments had never happened on real input at 2026-09-17; five instances of "safety asserted where it cannot fail" across the session. parity-vi now passes the first half (5 real models); the others do not |
| A11 | Unit economics | CAC, gross margin, payback estimable from labelled inputs; payback <12 months; GM ≥70% software / ≥50% services | David Skok, *SaaS Metrics 2.0* (forEntrepreneurs): CAC payback <12 months, LTV:CAC >3. Services GM bar is own judgement; NCC Group's filed 7.2% net margin at scale is the cautionary number (`docs/markets/ai-attack-defense-services.md`) |
| A12 | Founder-market fit | Founder is, or has been, the buyer; or is one introduction from ≥3 named buyers | `docs/findings/two-founder-cases.md`: every strong case had a founder from the buyer's world; no success found for a non-domain generalist selling. Own judgement on the "one introduction" bar |
| A13 | Time-to-first-dollar | ≤90 days from commitment to first paid invoice, with the date written before starting | Own judgement. Reference points on file: ads probe decides on day 7; parity gate on day 14; first-customer accounts on Reddit ran 7–8 months to $20–$70 (`first-customers.md`, forum-sourced) |
| A14 | Kill criteria and opportunity cost | Numeric, dated, pre-registered stop rule written before the test; expected value exceeds the founder's next-best use of the same hours | Pre-registration is the repo's own standard (`pass4-read.md` §"The three pending probes"). Opportunity-cost formula in §B14 |

Legal/platform ceiling is folded into A6 and A10: a mechanism barred by ToS or statute fails A10 (`ai-ads-injection` differential serving — three prohibitions; `agent-hermes-dashboard` automated-access clause, `market-check.md` §6).

---

## B. What "real number" means, per criterion

Formulas where one exists. Acceptable and unacceptable source kinds per criterion. "Inadmissible" means the reviewer may quote it only to reject it.

### B1 Problem severity and frequency
- **Numbers:** count of conversations held; count naming the problem unprompted; recurrence per buyer (per day/week/month); what they do today and what it costs them (hours or VND).
- **Acceptable:** transcripts or notes of conversations (`requires-human`); first-person posts with date and channel (`measured-by-us` count); support-ticket or forum counts with a denominator.
- **Inadmissible:** GitHub issue counts without a denominator (828 of 93,582 = 0.88%, `re-pick.md` §3); vendor surveys selling the fix (SBI case, `market-check.md` §1); "no one has built this".

### B2 Buyer identity and reachability
- **Numbers:** N named organisations; N with a named person; N with a channel (email/Zalo/LinkedIn/in-person); N reached; N replied.
- **Acceptable:** a frozen list file in `raw/` with dates; LinkedIn/TopCV/company pages (`company-stated`); job posts (`measured-by-us`).
- **Inadmissible:** a persona ("a developer with an nginx log"); a category ("HCMC LLM shops") without names.

### B3 Willingness to pay (KILL)
- **Numbers:** deposits received (VND, date); LOIs signed; unprompted paid asks (count, distinct non-author people, verbatim quote, URL).
- **Acceptable:** bank record, signed document, issue/DM text with URL and date (`requires-human` to obtain, `measured-by-us` to count).
- **Inadmissible:** stars, forks, views, "interest", a compliment, personal contacts of the founder (excluded by both pre-registered gates).

### B4 Price point
- **Numbers:** the price a named buyer paid or quoted; the price the nearest paid substitute lists; the price the free substitute lists ($0).
- **Formula:** none. Record conflicting prices side by side, never averaged.
- **Acceptable:** vendor pricing page (`vendor-reported`, dated); invoice (`requires-human`); Vietnamese price lists in VND (SEODO từ 18tr, Midas từ 80tr/tháng — `vendor-reported`, `ai-ads-injection/raw/vietnam-ai-visibility-demand.md`).
- **Inadmissible:** salary anchors used as prices; US engagement bands transplanted to Vietnam (`re-pick.md` §1 failure 2); aggregator ranges without a vendor page.

### B5 Market size, bottom-up
- **Formula:** `market = N_buyers × ARPU × attainable_share`. Then `months_to_2x = (2 × founder_annual_cost) / (market × ramp)`; state the ramp assumption.
- **Numbers:** N_buyers as a *count of named entities* from a directory, register, job-post census or crawl; ARPU from B4; attainable share stated with the reason (own judgement, ≤10% without distribution evidence).
- **Acceptable:** directories (YC, TopDev company list, MST portal), registers (Điều 8 portal when it exists — `filed`), W3Techs server-share (`analyst-derived`, with method), counts the agent made (`measured-by-us`, with the query).
- **Inadmissible:** Gartner/Mordor/Grand View TAM — the repo already holds 8× and 5× disagreements on the same base year (`docs/markets/ai-attack-defense.md`, `agent-dashboard.md`); "AI market in Vietnam is $X" from marketing blogs (`vietnam-sg-access.md` caveats).

### B6 Incumbent coverage (KILL)
- **Numbers:** for each named incumbent: version, date inspected, feature present Y/N, the sentence from its docs or output, price.
- **Acceptable:** the incumbent run on this machine with output in `raw/` (`measured-by-us`); its own docs/changelog quoted (`vendor-reported`).
- **Inadmissible:** absence of a feature inferred from a marketing page (`market-check.md` §1b, HiddenLayer); "not found in {list}" without the list; any claim about GoAccess/AWStats/Matomo/`/insights`/Braintrust Patterns until each is opened.

### B7 Why now
- **Numbers:** the event's date; the deadline it creates (2027-03-01 for Law 134 transition, `filed`); the count of entities it binds.
- **Acceptable:** statute text (`filed`), vendor changelog (`vendor-reported`), platform policy page with `Last Updated` stamp.
- **Inadmissible:** law-firm summaries in place of statute (`market-check.md` §5 vs `re-pick.md` §2 — the subject of Điều 10.5.b flipped on primary text); a trend article.

### B8 Distribution channel with cost
- **Formula:** `cost_per_reply = (hours × hourly_opportunity_cost + cash) / replies`; `CAC = cost_per_reply / (paying ÷ replies)`.
- **Numbers:** contacts sent, replies, meetings, paid; hours spent; cash spent.
- **Acceptable:** the project's own outreach log (`requires-human` to run, `measured-by-us` to count); vendor benchmarks with stated samples (Instantly 2026, Belkins 2025 — `vendor-reported`).
- **Inadmissible:** the recirculated "$536–$702 CAC" figure (eight domains, no methodology — `first-customers.md`); star velocity as a channel result.

### B9 Moat and time-to-copy
- **Numbers:** lines of code in the shipped prototype; hours an incumbent's engineer would need (own estimate, show the reasoning); a dated example of the incumbent shipping an adjacent feature (vendor absorption time — Anthropic closed #20636 in one quarter, `measured-by-us` via `gh`).
- **Acceptable:** changelogs, issue trackers, the prototype's own size.
- **Inadmissible:** "first mover" (SEA-HELM was first; `market-check.md` constraint 1); "nobody has built this" (§F).

### B10 Technical proof on real input (KILL)
- **Numbers:** n of real inputs run; who supplied each (not the team); the moment's occurrence Y/N per input; for every "cannot happen" claim, the constructed failing input and the exit code.
- **Acceptable:** run records in `raw/` with hashes (`measured-by-us`); a third party's run record (`requires-human`).
- **Inadmissible:** fixture results (25-of-155 spoof rate; 8.2→17.8 pp; 7× chore) presented as anything but mechanism demos; tests that pass on a short-circuiting input (RFC 5737 address, key in the one redacted field — `review.md` process note).

### B11 Unit economics
- **Formulas:** `payback_months = CAC / (ARPU_monthly × GM)`; `GM = (price − COGS) / price`; `LTV = ARPU_monthly × GM / churn_monthly`; `LTV:CAC` target >3 (Skok).
- **Numbers:** COGS per unit (GPU minutes × electricity; API calls at published rates — `vendor-reported`; MoR fee 5% + 50¢ — `vendor-reported`, `vietnam-sg-access.md`); hours per engagement × opportunity cost; churn assumed and labelled.
- **Acceptable:** published API/GPU prices; the project's measured wall-clocks (15m8s for 600 prompts on Qwen3Guard-0.6B, `measured-by-us`); the founder's own hourly cost (§B14).
- **Inadmissible:** the subscription allowance as COGS (`market-check.md` §6: price against published API rates, treat the allowance as a revocable discount); GM without COGS shown.

### B12 Founder-market fit
- **Numbers:** count of buyers the founder has personally been; count one introduction away, named; languages/geography match Y/N.
- **Acceptable:** the founder's own statement (`requires-human`); the 8-company HCMC list (`ai-attack-defense/docs/customers/hcmc-candidates.md`).
- **Inadmissible:** "technical founder can sell to developers" as a general claim.

### B13 Time-to-first-dollar
- **Numbers:** commitment date; first invoice date; days between; the gate date (day 7 / day 14) and what it decided.
- **Acceptable:** dated `STATE.md` entries and bank/LOI evidence.
- **Inadmissible:** a roadmap date with no gate attached.

### B14 Kill criteria and opportunity cost
- **Formula:** `opportunity_cost = hours × hourly_rate_founder`; `hourly_rate_founder` = the higher of (a) clinic-MCP revenue per hour, (b) HCMC AI-engineer contract rate 2026 (`vendor-reported`, pull C1–C2). `EV_project = Σ p_i × value_i − opportunity_cost − cash`. State every `p_i` as own judgement.
- **Numbers:** the pre-registered rule verbatim; its date; its status (run / not run / result).
- **Acceptable:** the three pre-registered gates on file (`pass4-read.md` table); the founder's own rate (`requires-human`).
- **Inadmissible:** a kill rule written after the data; "we'll see how it goes".

---

## C. Per-project pull lists

Line format: `[criterion] — [exact number wanted] — [where] — [label expected]`. Pull agents have WebSearch, WebFetch, one has Chrome; none can contact a human. Lines that can only come from a person are marked `requires-human` and are for the user, not the agent. **KILL** marks the one or two numbers that falsify the project fastest. Every pull lands in `projects/investment-review/raw/<project>-<topic>.md` verbatim, with URL and date.

### C1 `aicrawlcheck` (`ai-ads-injection`)

1. **A6 KILL** — Does GoAccess verify a claimed crawler UA against published IP ranges (feature name, version, changelog date) — goaccess.io docs, `github.com/allinurl/goaccess` (search `bot`, `crawler`, `ip range`, `verify`), issues — `vendor-reported`; run it on the fixture if installable, `measured-by-us`
2. **A6 KILL** — Same for AWStats (`robots.pm` list, any IP verification) and Matomo Log Analytics + DeviceDetector bot list — awstats.sourceforge.io, matomo.org/docs/log-analytics, `github.com/matomo-org/device-detector` — `vendor-reported`
3. A6 — Known Agents: does an access-log upload/import exist as of 2026-09; current tiers and prices ($0 / $29 / $299 on file) — knownagents.com/pricing, /docs — `vendor-reported`
4. A6 — Cloudflare AI Crawl Control: any "historical log import" or retroactive view in the changelog since 2026-08-14 — developers.cloudflare.com changelog — `vendor-reported`
5. A5 — Share of all websites behind Cloudflare, and share of top-1M — W3Techs "Cloudflare usage statistics" (method stated) — `analyst-derived`; this sizes the "not behind Cloudflare" population
6. A5 — Web-server share nginx / Apache / other — W3Techs — `analyst-derived`
7. A5 — Count of public OSS tools in the same slot with stars, last commit: `ai-robots-txt/ai.robots.txt`, `TecharoHQ/anubis`, `nginx-ultimate-bad-bot-blocker`, any "crawler verify" / "bot verification log" repo — GitHub API — `measured-by-us`
8. A1 — Count of HN and r/selfhosted threads 2025-01..2026-09 about AI-crawler bandwidth/spoofing; top thread points and comment counts — HN Algolia API (`query=GPTBot`, `ClaudeBot`, `AI crawler`), old.reddit search via Chrome — `measured-by-us` (visibility proxy, say so)
9. A1 — Count of Show HN launches of bot-detection/log-analysis tools 2025–2026 and their points — HN Algolia — `measured-by-us`
10. A9 — Web Bot Auth adopters: any AI operator named as signing requests (OpenAI, Anthropic, Perplexity docs; Cloudflare blog 2026) — `vendor-reported`; shelf-life of the whole method
11. A10 — A published real-world spoof rate for AI-crawler identities (Cloudflare Radar bot report 2026, Known Agents Agentic Web Index "Spoofing & Security", Akamai) — `vendor-reported`; the comparison for the n=1 real log
12. A10 — One real, recent (2025–2026) public access log containing AI-crawler UAs (Kaggle "web server access logs", university/CDN datasets, any GitHub-hosted anonymised log) — run `aicrawlcheck scan` on it, paste output — `measured-by-us`; if none found, `unknown — checked <sources>`
13. A6 — Amazonbot IP-range file: URL, prefix count, `creationTime` — developer.amazon.com/amazonbot/ip-addresses — `vendor-reported` (closes review S2)
14. A4 — Prices of paid bot-management: Cloudflare Bot Management entry price, DataDome starting tier, HUMAN, Known Agents — vendor pricing pages — `vendor-reported`
15. A8 — Search interest: relative Google Trends for "GPTBot", "verify googlebot", "AI crawler block" 2024–2026 — trends.google.com via Chrome — `analyst-derived` (weak, label it)
16. A9 — Time-to-copy: LOC of `prototype/aicrawlcheck/*.py` and hours estimate for an incumbent engineer — count locally — `measured-by-us` + `own judgement`
17. **A3 KILL** — Deposits from the pre-registered 20-organisation probe (15.000.000 VND, 50% deposit, day 7) — `requires-human`; not yet run
18. A3 — Unprompted requests for the tool after a published post on the rDNS finding, counted at day 14 — `requires-human` to publish, `measured-by-us` to count
19. A8 — Vietnamese GEO agencies not yet re-fetched (Hashmeta VN, Nextop, seo.danang.vn, Fast Marketing): do any sell measurement rather than optimisation; price — agency pages — `vendor-reported`

### C2 `Foreman` (`agent-hermes-dashboard`)

1. **A6 KILL** — Does `/insights` list repeated prompts / recurring work / suggest skills — run `/insights` on this machine and paste the report headings; code.claude.com/docs/en/insights — `measured-by-us`; if it does, Foreman's only checkable claim is the emitted file
2. **A6 KILL** — Has Claude Code shipped recurrence detection or "suggest a skill/command from history" — changelog `github.com/anthropics/claude-code` CHANGELOG 2026-06..09, release notes — `vendor-reported`
3. A6 — Braintrust Patterns: what it clusters, whether it emits a runnable artifact, price — braintrust.dev docs/pricing — `vendor-reported`
4. A5 — Claude Code user count: any Anthropic-stated figure (WAU, "N developers", run-rate) 2026 — anthropic.com/news, earnings press, Claude Code launch posts — `company-stated`; else `unknown — checked`
5. A5 — Count of public GitHub repos matching `claude code hook` / `claude-code plugin` / `SKILL.md` with >100 stars; top 10 with stars and last push — GitHub search API — `measured-by-us`
6. A5 — Count of plugins in the official Claude Code marketplace(s) and the largest community marketplace — plugin directory pages — `vendor-reported` / `measured-by-us`
7. A9 — Star velocity baselines: `ccusage` stars on 2026-09-18 vs 14 days earlier; `Claude-Code-Usage-Monitor`; `claude-session-budget` (8★ on file) — star-history.com or GitHub API — `measured-by-us`; sets what "100 stars in 14 days" means
8. A4 — Prices of closest paid dev-workflow analytics: WakaTime, LinearB, Swarmia, DX, Waydev; Claude-specific paid tools (SessionWatcher $6.99–59 on file, CrewTower) — vendor pages — `vendor-reported`
9. A4 — Any paid Claude Code third-party tool with disclosed revenue or customer count — Gumroad/Lemon Squeezy listings, IndieHackers posts 2026 — `company-stated`; expect `unknown`
10. A10 — Anthropic consumer terms clause on automated/non-human access, current text and date; Agent SDK subscription-usage status (support.claude.com article 15036540 successor) — `filed` / `company-stated`; platform risk
11. A1 — Count of first-person posts 2026 "I run my business with Claude Code" (non-code use) — r/ClaudeAI, IndieHackers, HN — `measured-by-us`; the buyer existence check
12. A1 — r/ClaudeAI member count; Claude Developers Discord member count — `measured-by-us`
13. A6 — Existing "prompt history analyzer" / "history.jsonl" tools on GitHub — search — `measured-by-us`
14. A10 — One live `Stop` hook fire observed end-to-end on a scratch project with the ledger line pasted — agent can run in `prototype/demo/` — `measured-by-us`
15. A10 — `scan --from-history` built and run on this machine's real `history.jsonl`, report pasted with `display` values redacted to normalised shapes — `measured-by-us`; the first real ledger
16. **A3 KILL** — Gate at day 14 after publication: stars AND unprompted paid asks (≥100 AND ≥3, both required) — `requires-human` to publish; `measured-by-us` to count
17. A9 — LOC of `prototype/foreman/` and copy-time estimate — `measured-by-us` + `own judgement`
18. A11 — Anthropic API list prices for the models a hosted variant would call — platform pricing page — `vendor-reported`; only if a hosted variant is ever scoped

### C3 `parity-vi` (`ai-attack-defense`)

1. **A5/A2 KILL** — Count of Vietnamese companies operating a public Vietnamese-language LLM chat product, named: start from AI Hay, Vbee, Filum AI, TPBank T'AioX, MoMo, Viettel, VNPT AI, plus Zalo/Kiki, FPT.AI, VNG, VinAI, Sacombank, VPBank, Vietcombank, Techcombank, Tiki, Shopee VN, Lazada VN, Be, Grab VN — search `chatbot AI tiếng Việt ra mắt 2026`, `trợ lý ảo AI ngân hàng`, VnExpress/CafeF/Genk, company pages — `measured-by-us` count with URLs; **fewer than 20 named is a KILL on bottom-up size**
2. A2 — Job posts in Vietnam mentioning `guardrail`, `content moderation`, `LLM safety`, `AI safety`, `red team` 2026 — TopDev, ITviec, VietnamWorks, LinkedIn — `measured-by-us` count with links; names the buyer's engineer
3. A6 — Azure AI Content Safety F0 tier: current limit (5,000 records/mo on file), Vietnam-billed account allowed Y/N — Azure pricing + region pages — `vendor-reported`
4. A6 — OpenAI moderation endpoint: still free, available to Vietnam accounts — platform docs — `vendor-reported`
5. **A10 KILL** — Paired run against ≥1 commercial endpoint (Azure or OpenAI moderation), 600 prompts, report pasted — `requires-human` (account); if commercial endpoints show overlapping CIs AND no over-blocking excess, the measurement has no sellable story
6. A9 — Llama Guard 4 language list; any vendor-published Vietnamese quality number since 2026-09-17 — HF model cards, Azure language table — `vendor-reported`; countdown events 1–2 (`parity-report-2026-09-18.md` §9)
7. A9 — SEA-HELM `safeguard_general` status (on/off), last commit to `data/README.md` — `github.com/aisingapore/SEA-HELM` — `vendor-reported`; countdown event 3
8. A6 — promptfoo: any `compare`/`diff` subcommand or shipped multilingual guardrail corpus as of 2026-09 — promptfoo docs/changelog — `vendor-reported`
9. A4 — Vietnamese security-testing prices: any published `bảng giá kiểm thử xâm nhập` / pentest quote from Viettel Cyber Security, VNPT, CMC Cyber Security, FPT IS, VSEC, CyStack — vendor pages — `vendor-reported`; the only local price anchor that is a price
10. A4 — ISO 42001 / AI-assessment engagement prices in Vietnam (BSI Vietnam, TÜV SÜD VN, Bureau Veritas VN, QUACERT) — `vendor-reported`; expect quote-only
11. A7 — Law 134 decree status: any Nghị định under Điều 9.3 / 10.7 / 11.6 / 13.6; the Thủ tướng high-risk list (13.4); the Điều 8 portal URL and count of notified systems — vanban.chinhphu.vn, mst.gov.vn, vbpl.vn (Chrome; SPAs) — `filed`; the pre-registered P1–P3 probe from `re-pick.md` §5
12. A7 — Decree 147/2024 enforcement actions against a chatbot/AI content provider 2025–2026 — VN news search — `filed`/press
13. A1 — Public incidents of a Vietnamese chatbot producing harmful/offensive Vietnamese output 2025–2026 — VN news, Facebook/Threads screenshots via news — `measured-by-us` count; problem severity
14. A2 — For each of the 8 profiled companies: any named moderation vendor, model router, or safety statement — company pages, engineering blogs, LinkedIn — `company-stated`; `unknown` per company otherwise
15. A6 — Any published Vietnamese guardrail/jailbreak benchmark since 2026-09 (arXiv `Vietnamese guardrail`, `Vietnamese jailbreak`, `MultiJail Vietnamese`) — arXiv/Google Scholar — `measured-by-us`; first-mover check
16. A8 — Vietnamese developer channels: Viblo user count, GDG HCMC size, VietAI community size, Zalo/Facebook LLM groups — `measured-by-us`; no channel is on file (`hcmc-opener` caveats)
17. A11 — COGS of one engagement: GPU minutes on this machine (15m8s / 600 prompts, `measured-by-us`) × electricity; or Azure/OpenAI per-1k-record price above free tier — `vendor-reported`
18. A10 — Qwen3Guard-Gen-8B run (size effect, `unknown — not run`) — local GPU, only if VRAM permits — `measured-by-us`; optional
19. A10 — Finish stash `wave10b-s18-partial-2026-09-18` (cross-family diff refusal) and re-run the Granite diff — `measured-by-us`; a known blind spot must not ship
20. **A3 KILL** — 14-day gate after publication: ≥1 buyer-side run AND ≥3 written replies engaging with the number — `requires-human`
21. A4 — Price a named HCMC company would pay for the engagement — `requires-human`; the only way `unknown — priced per engagement` becomes a number
22. A5 — SEA-LION leaderboard VI safety top score refresh and whether any guardrail product appears — leaderboard.sea-lion.ai (JS, Chrome) — `vendor-reported`

### C4 Cross-cutting — founder opportunity cost and Vietnam context

1. Opportunity cost — HCMC senior back-end and AI/ML engineer salary bands 2026 (ITviec 2025–2026: >8-yr back-end 54.9M VND/mo gross on file, n=1,839; pull the AI/ML band) — itviec.com report, TopDev 2026 report, VietnamWorks — `vendor-reported`
2. Opportunity cost — Contract/freelance rates for Vietnam-based AI engineers on Upwork/Toptal (hourly, USD) 2026 — platform search — `vendor-reported`
3. Opportunity cost — Clinic-MCP side business: revenue per month and hours per week — `requires-human`; this is the founder's actual alternative
4. Runway — 6-month HCMC cost: Numbeo single-person budget (on file $500–780/mo) and expat estimate ($2,800–4,500/mo) refreshed; the founder's own burn — Numbeo, `requires-human` for own — `analyst-derived` / `requires-human`
5. Runway — VND/USD rate on the review date (never pulled in this repo) — Vietcombank or SBV page — `filed`
6. Seed context — Vietnam AI seed/Series A rounds 2025–2026 with names and sizes: AI Hay $10M Series A (2025-07, Argor Capital, `company-stated` via VnEconomy); Antler VN ~$100K/deal (on file, secondary); pull Do Ventures, ThinkZone, Touchstone, VinVentures, Genesia, 500 Global VN portfolio announcements — DealStreetAsia, Tech in Asia, VnExpress — `company-stated`/press
7. Seed context — Vietnam disclosed AI funding total 2025 and startup count, from a primary (Do Ventures/Cento "Vietnam Innovation & Tech Investment Report", NIC) — replaces the $130M / 765+ marketing-blog figures — `analyst-derived` with method
8. Seed context — Singapore vs Vietnam native-AI funding ($9.3B vs $19M on file, secondary) refreshed from a primary — `analyst-derived`
9. Rails — Polar / Lemon Squeezy / Paddle: complete a seller onboarding from Vietnam to the KYC step and record the outcome — `requires-human`; documentation-only status on file
10. Rails — Payoneer/Upwork receipt into a Vietnamese bank: fee and conversion terms — vendor pages — `vendor-reported`
11. Channel — Cold-email and LinkedIn reply benchmarks, current editions (Instantly 3.43% 2026; Belkins cybersecurity 4.86% 2025; Expandi LinkedIn 10.3% on file) — vendor reports — `vendor-reported`
12. Benchmark — Indie revenue distribution (54% zero; median profitable micro-SaaS ~$4,200 MRR on file) — locate the primary dataset — `analyst-derived`
13. Benchmark — Point Nine SaaS Funding Napkin current edition: seed and Series A ARR expectations — pointnine.com — `analyst-derived`; figures change yearly, pull the current one, do not quote from memory
14. Cost — Claude Code subscription tier and monthly cost the founder pays — `requires-human`
15. Cost — RTX 3060 Ti power draw × HCMC electricity tariff (EVN business tier) — EVN tariff page — `vendor-reported`; trivially computed COGS for local runs
16. Context — Law 134 transition dates (2027-03-01; 2027-09-01 health/education/finance, `filed`) and any 2026 amendment — gazette — `filed`
17. Context — Number of Vietnamese firms self-classified medium/high under Law 134 — Điều 8 portal — `filed`; `unknown` until the portal is located (C3 line 11)

---

## D. Review template

One file per project: `projects/investment-review/<project>.md`. Sections in this order, headings verbatim. Every number labelled. Every claim in the project's own docs that could not be verified goes in §11.

### 1. Header table

| Criterion | Number found | Source + label | Threshold (§A) | PASS / FAIL / UNKNOWN |
|---|---|---|---|---|
| A1 … A14 | | | | |

Rules: `UNKNOWN` is a valid cell and is not a `PASS`. A KILL row (A3, A6, A10) marked `FAIL` or `UNKNOWN` sets the verdict ceiling to "stop" or "gate first" regardless of §E.

### 2. What the MVP does today (measured)
One command, one wall-clock, one tally, one real-input result if any. Cite `e2e-test.md`, `review.md`, `real-run-*.md`. No fixture number without the word `fixture` beside it.

### 3. Proven vs asserted
Two columns. "Proven" = reproduced by a second agent from clean, or run on real input. "Asserted" = in a spec, page, or vision doc only. The review's own bug-class check: for each "X cannot happen", name the input that makes X happen and whether a test reaches it.

### 4. Incumbent gap, in the incumbent's words
Table: incumbent | version/date inspected | how inspected (run / docs / not inspected) | its own sentence on the gap | price. An incumbent not inspected first-hand is a row reading `not inspected — A6 FAIL`.

### 5. Bottom-up sizing, arithmetic shown
```
N_buyers        = <count>          [<label>, <raw file>]
ARPU            = <VND or USD>     [<label>]
attainable_share= <0–1>            [own judgement, reason]
market_36mo     = N × ARPU × share
founder_cost_yr = <hours × rate>   [§B14]
ratio           = market_36mo / (2 × founder_cost_yr)   → PASS if ≥ 1
```
If any input is `unknown`, the ratio is `unknown` and A5 is `UNKNOWN`.

### 6. Unit economics, every input labelled
```
price/unit  = … [label]      COGS/unit  = … [label]      GM = …
CAC         = … [formula B8] payback    = CAC / (ARPU_m × GM)  → PASS if < 12 mo
churn/mo    = … [own judgement]   LTV:CAC = …
```

### 7. Kill-test result
The pre-registered rule verbatim, its date, whether it has run, the result, and who must run it. If not run: what it costs to run (hours, VND, days) and the earliest date.

### 8. Three scenarios
Each with: founder hours, cash (VND/USD), expected first-dollar date, own-judgement probability of reaching the gate, value if reached, EV. Reviewer's probabilities are stated as own judgement and must be numbers.

| Scenario | Hours | Cash | First dollar | p(gate) | Value at gate | EV = p×value − cost |
|---|---|---|---|---|---|---|
| Do nothing (archive; publish as-is at most) | | | never | — | reputation only | |
| Minimum viable commitment (run the gate, nothing else) | | | | | | |
| Full commitment (build toward the vision doc's win condition) | | | | | | |

Cost = hours × §B14 rate + cash. A negative EV in the full-commitment row is a finding, not a formatting problem.

### 9. Known traps checked (§F)
One line per trap: check run, result.

### 10. Verdict
One paragraph, this form: **"Worth X hours / $Y over Z weeks to reach gate G, else stop."** G is a §A KILL criterion or the project's pre-registered gate. If no gate is reachable inside 90 days at zero cash, the verdict is "stop; keep as calling card" and says what the calling card is worth in hours.

### 11. Claims in the project's own docs not verified or contradicted
Table: file:line | claim | status (`unverified` / `contradicted by <what>`) | consequence for §1.

### 12. Caveats
What this review could not do, and why.

---

## E. Scoring (optional, subordinate to KILL)

A weighted score may be reported for cross-project comparison only. **A score never overrides a failed or unknown KILL criterion (A3, A6, A10).** Weights sum to 100; each justified in one line; all weights are own judgement.

| Criterion | Weight | Why |
|---|---|---|
| A3 willingness to pay | 20 | The one number no pass has produced for any project; it decides everything else |
| A10 real-input proof | 15 | The portfolio's shared hole (`SUCCESS-VISION.md`); parity-vi is the only one past it |
| A6 incumbent coverage | 12 | Free incumbents killed every asset claim so far (`pass4-read.md` cross-read point 3) |
| A5 bottom-up size | 10 | A named count separates a business from a calling card |
| A2 buyer reachability | 10 | The only structural advantage on file is proximity; it applies to one project |
| A8 channel with cost | 8 | Quantified channel failures are the two remote ones; a reply is the first test |
| A11 unit economics | 7 | Estimable for all three; low weight because inputs are mostly `unknown` |
| A12 founder-market fit | 5 | Real but fixed; it does not change with work |
| A9 moat | 5 | Honest answer is "none" for all three; low weight so it cannot flatter |
| A7 why now | 3 | An event is not demand |
| A1 severity | 3 | Folded into A3 in practice; kept so "once-asked" is visible |
| A4 price point | 2 | Subsumed by A3 once money moves |
| A13 time-to-first-dollar | 0 | Reported, not scored — it is a consequence of A3/A8 |
| A14 kill/opportunity cost | 0 | Reported in §D7–8, not scored — it is the frame, not a factor |

Score per criterion: PASS = full weight, UNKNOWN = 0, FAIL = 0. Report the score alongside the count of UNKNOWNs; a high score with many UNKNOWNs is an artefact of the weights, and the reviewer says so.

---

## F. Known traps for this portfolio — each is a check the reviewer must run

From `ORCHESTRATION.md`, `pass4-read.md`, `evidence-rules.md`, and the three reviews.

| # | Trap | Where it happened | The check |
|---|---|---|---|
| F1 | Search-level negative read as demand evidence | Every "no buyer found" in three passes; no buyer contacted by any pass (`pass4-read.md` cross-read point 2) | For each demand claim, write which humans were asked. If zero, the cell is `UNKNOWN`, not `FAIL` and not `PASS` |
| F2 | "No one has built this" read as opportunity | Nine Show HN price-trackers with no traction (`agent-hermes-dashboard/docs/review/market-check.md` §2); GoAccess/AWStats/Matomo/`/insights` never opened | Every absence claim carries `not found in {A, B, C} — checked <date>`; the reviewer opens at least one item in the braces themselves. Repeated independent supply with no pull is evidence against, not for |
| F3 | Safety property asserted where it cannot fail | FCrDNS tested on an address with no PTR; `assert_not_global` on the happy path; no-network by grep; redaction with the key in the redacted field; diff gate blind to indeterminates (`ai-attack-defense/docs/outcome/review.md` process note) | For each "X cannot happen" on the page or in the README, construct the input that makes X happen and run it. Record exit code. A guard without a constructed failing input is "restated, not tested" |
| F4 | Benchmarks scored on models, not guardrails | SEA-HELM prompts general LLMs; `market-check.md` constraint 2 | Any parity number must name the measured object as a guardrail *product* or say "open-weights model, not a commercial endpoint" — the commercial run is still `requires-human` |
| F5 | Stars mistaken for demand | Hermes 246,092★ (verified, a framework not a buyer); ccusage 18,591★ free; "500 stars with zero paid asks is a stop" | Stars and views appear only in A9/A8 context rows. A3 counts money, LOIs and unprompted paid asks from non-authors only |
| F6 | Incumbents never inspected first-hand | promptfoo (docs only), `/insights` (one docs line), GoAccess/AWStats/Matomo (nothing), Braintrust Patterns (nothing), HiddenLayer (a format list) | §D4 requires a "how inspected" column; "docs only" on the primary incumbent is an A6 `UNKNOWN`; "not inspected" is an A6 `FAIL` |
| F7 | Compiled file citing a compiled file; hedge dropped in transit | "reportedly" → fact on questionnaires; SBI number verified and inverted; $8k–$50k band transplanted across markets (`re-pick.md` §1 in all three projects) | Every number in the review cites a `raw/` file or a primary URL, never another compiled file. Any price or verdict carries the market it was measured in |
| F8 | Fixture number leading the page | All three pages at 2026-09-17 led with a fixture demo (`ORCHESTRATION.md` wave 9V); fixed only on parity-vi | Any number the reviewer quotes from a page or README is tagged `fixture` or `real`; a `fixture` number cannot appear in §D1, §D5 or §D6 |
| F9 | Law or event read as demand | Law 134/2025/QH15 mandates process duties, no guardrail testing; one licensed sentence only | A7 may cite the law as an event; A3/A5 may not use it. A second compliance sentence on any page is a finding |
| F10 | Vendor-stated numbers read as independent | Known Agents "5,000+ sites", Lakera "98%+", AI Hay "100M questions/month" | Label `vendor-reported`/`company-stated` inline; never use one as the sole input to §D5 |
| F11 | Averaging conflicting figures | Repo rule; ViHSD licence three ways; HCMC cost of living 5× apart | Conflicts sit side by side in the review with both labels; the reviewer picks neither and says which the verdict is sensitive to |
| F12 | Relative dates and unlabelled runtimes | "~10 seconds" vs measured 1.312 s; "this year" on a page that outlives 2026 | Every date absolute; every runtime measured or labelled `unmeasured` |

---

## How to use

1. Stage 2 (Sonnet): take one §C list, pull every line into `raw/<project>-<topic>.md` verbatim with URL, date and label; mark `requires-human` lines as such and leave them empty — never fill them with a guess.
2. Stage 3 (Opus for ads and hermes, Fable for parity-vi): fill §D from `raw/` only; run every §F check; a KILL row at FAIL or UNKNOWN caps the verdict at "gate first" or "stop".
3. State every probability and every attainable-share as own judgement with a number; show the arithmetic in §D5 and §D6 so the user can change one input and recompute.
4. Stage 4: `PORTFOLIO.md` compares the three §D10 verdicts and the three §D8 EV tables against the founder's opportunity cost from §C4; it ranks by EV at minimum commitment, not by §E score.
5. The verdict is one sentence per project in the §D10 form; if the user runs a `requires-human` line afterwards, the review is re-issued with a dated correction, never edited in place.

---

## Files read

Root: `CLAUDE.md`; `MegaPlan.md`; `docs/method/scope.md`; `docs/findings/cross-read.md`, `pass2-read.md`, `pass3-read.md`, `pass4-read.md`, `market-gaps-2026.md`, `two-founder-cases.md`, `localization-play.md`, `injection-feasibility.md`; `docs/markets/vietnam-sg-access.md`, `ai-attack-defense.md`, `ai-attack-defense-services.md`, `agent-dashboard.md`, `ai-search-ads.md`, `ai-trend-suite.md`, `creative-ai-lane.md`; `docs/customers/first-customers.md`.

Projects layer: `projects/CLAUDE.md`; `projects/MVP-MANDATE.md`; `projects/SUCCESS-VISION.md`; `projects/ORCHESTRATION.md` (whole).

`projects/ai-ads-injection/`: `CLAUDE.md`; `docs/plan/re-pick.md`; `docs/review/market-check.md`; `docs/design/mvp-spec.md`; `docs/outcome/positioning.md`, `review.md`, `success-vision.md`; `docs/execution/e2e-test.md`; `STATE.md` (last 200 lines).

`projects/agent-hermes-dashboard/`: `CLAUDE.md`; `docs/plan/re-pick.md`; `docs/review/market-check.md`; `docs/design/mvp-spec.md`; `docs/outcome/success-vision.md`; `docs/execution/e2e-test.md`; `STATE.md` (last 200 lines). No `docs/outcome/review.md` exists — the 9a review was stopped before writing.

`projects/ai-attack-defense/`: `CLAUDE.md`; `docs/plan/re-pick.md`; `docs/review/market-check.md`; `docs/design/mvp-spec.md` (incl. the three dated corrections); `docs/outcome/hcmc-opener-2026-09-18.md`, `parity-report-2026-09-18.md`, `review.md` (9a + 9b), `success-vision.md`; `docs/execution/e2e-test.md`; `STATE.md` (last 200 lines).

Not read, named so the reviewers know: `docs/execution/sweep-2026-09-18.md`, `real-run-2026-09-18.md`, `fix-log-2026-09-18.md`, `packaging-2026-09-18.md`, `site-log-2026-09-18.md` (their numbers were taken from `parity-report-2026-09-18.md`, `review.md` and `ORCHESTRATION.md`, which cite them); `docs/plan/measurement-report.md`; `docs/customers/hcmc-candidates.md`; any `site/index.html`; any `raw/`.
