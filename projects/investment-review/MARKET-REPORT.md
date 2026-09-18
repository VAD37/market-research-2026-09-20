# MARKET REPORT — the three markets, 2026-09-18

Companion to `REPORT.md`, which carries the project-level verdicts. **This file carries none.** Per root `CLAUDE.md` the verdict is the user's; this is evidence about the three *markets* the prototypes sit in, read for a solo technical founder in Ho Chi Minh City deciding where to spend time and money. No figure here is new. Conflicts sit side by side, never averaged. Analyst TAM is inadmissible as a size (`FRAMEWORK.md` §B5) and is quoted only to reject it.

**Label key, inline on every number:** `v` vendor-reported · `a` analyst-derived · `f` filed · `cs` company-stated · `m` measured-by-us · `jp` job-post · `oj` own judgement · `unk` unknown — checked, with channel and date.
**Path key:** `c1`–`c4` = `projects/investment-review/raw/c{1-4}-*-2026-09-18.md` · `audit` = `.../audit-root-research-2026-09-18.md` · `M/` `F/` `Cu/` = `docs/markets|findings|customers/` · `A/` `H/` `D/` = `projects/ai-ads-injection|agent-hermes-dashboard|ai-attack-defense/`.

---

## 1. One-page read

| | **A — AI crawler traffic / AI-search visibility** | **B — Agent observability, Claude Code tooling** | **C — LLM guardrails, VN/SEA** |
|---|---|---|---|
| Sold | Visibility reports, crawler telemetry, bot management | Traces, evals, usage analytics, session search | Red-team engagements, guardrails, assessments |
| Buys | Brand and SEO teams; VN agencies resell | Developers; platform teams hold budget | CISO/AppSec or ML eval, split unconfirmed |
| Price anchor | SEODO từ 18 triệu VND [v, `A/raw/vietnam-ai-visibility-demand.md`] | Braintrust Pro $249/mo [v, `c2` §3] | Cobalt $3,500/test, US [v, `M/ai-attack-defense-services.md`] |
| Free floor | Cloudflare Crawl Control, "all plans" [v, `c1` §4] | `/insights`; `ccusage` 18,615★ [v/m, `c2` §1,7] | Azure F0 5,000 records/mo [v, `c3` §3] |
| Incumbents | GoAccess, AWStats, Matomo, Known Agents, Cloudflare | `/insights`, Braintrust, agentsview, session-search | promptfoo, Giskard, Patronus, Lakera, PyRIT |
| 2026 change | ChatGPT ads live 2026-02-09; Perplexity exited | Marketplace 101→316, 2026-03→2026-09-18 | Law 134 in force 2026-03-01; QĐ 33 eff. 2026-08-15 |
| Vietnam angle | **Real** — 8 named agencies sell GEO by name | **Absent** — no VN figure; Polar lists Vietnam for payout | **Real on demand side** — 23 named VN chat products |
| Cannot say | Who pays for measurement, not optimisation | How many Claude Code users exist | What a Vietnamese buyer would pay |

**Cross-market read.** In all three the mechanism is settled and demand untouched — crawler identity, hook schema and the VI/EN guardrail gap are each closed by primary text or measurement, and no buyer has been asked anything in any pass (`F/pass4-read.md`). In all three the floor is free and held by someone large: Cloudflare, Anthropic, promptfoo-inside-OpenAI. Geography is an asset only in C and partly in A. Every regulatory event that resembles demand is an event, not demand — Law 134 sets classification and dossier duties and names no security control (§F9). The one fact spanning all three is the cost base: 54.9M VND/month for a senior engineer [v, `c4` §1] against a US median developer salary of $133,080 [`M/ai-trend-suite.md`].

---

## 2. Market A — AI crawler traffic and AI-search visibility

### 2.1 Demand

`A/docs/review/market-check.md`, verbatim: *"No buyer of an AI-answer audit was identified in any channel, at any price."* No procurement-title study exists — `unk` WebSearch 2026-09-16.

| VN agency [all v] | Published price | Standalone audit |
|---|---|---|
| SEODO | **từ 18 triệu** and **từ 25 triệu** on one page, unreconciled; Pro 200tr; Max 350tr | **Free** consultation |
| Fast Marketing | 32.000.000đ / 45tr / 65tr per month, 6–12 month terms | none published |
| Midas | "Chỉ từ 80 triệu / tháng", 12 months | **Free** survey |
| TopOnSeek | Quote-only; offers "tỷ lệ xuất hiện trong câu trả lời AI" | **Free** 15-second checker |
| Hashmeta VN | GEO Premium **60.000.000đ+/tháng** | **"trị giá 15.000.000đ"**, given free |
| Nextop · seo.danang.vn | No price, bundled · SEO từ 80.000.000đ/dự án, **not GEO** | none · n/a |

At least **8 distinct VN agencies** brand this "GEO"/"AEO" [m, `A/docs/explore/cost-and-demand-pulls.md`]. **Three of three re-checked give the audit away; none publishes a price for one.** Audit anchors conflict 5×: $1,500–$5,000 one-time GEO audit [a, `Cu/answer-integrity-buyer.md`] against an $8k–$25k band measured in AI security, not here. The only local usage figure — ~80% of VN online users used AI in three months, ChatGPT 81%, Gemini 51%, AI Hay 9% [Decision Lab via press, fieldwork 2025-07] — is **13+ months stale**, primary never located. Proxies, barred from sizing by §F5: the top HN thread here is spoofed-AI-bot scanning, **305 points / 228 comments, 2026-08-12**; the highest genuine bot-detection Show HN scored **7 points** [m, `c1` §8–9]. **One DRP vendor of eight** covers answer content — BrandShield, 2026-04-01, no price.

### 2.2 Supply

No incumbent verifies a claimed crawler UA against published IP ranges; none imports an existing log. All checked 2026-09-18, **docs-only, none run** [v, `c1` §1–4, §14].

| Incumbent | Its own words | Price |
|---|---|---|
| GoAccess | Issue search `bot crawler verify ip range` → "No results" | $0 |
| AWStats · Matomo DeviceDetector | "bots that AWStats is not able to detect" · "parses User Agents and Browser Client Hints", no IP check | $0 |
| Matomo Log Analytics | `unk` 2026-09-18, HTTP 404 | $0 |
| Known Agents (ex-Dark Visitors) | No import path. **2,000+ agents**, index spans **5,000+ sites** | $0 / $29 / $299 |
| Cloudflare AI Crawl Control | No historical-log-import entry; page stamp 2026-08-14 | $0, all plans |
| Cloudflare Pay per crawl | **Still private beta — 14+ months after 2025-07-01** | — |
| Bot Mgmt · DataDome · HUMAN | Nothing published; pricing pages 403 | quote-only; $1,000–5,000/mo; $3,830/$8,670/$10,160 [a] |
| Profound | Free trial = **10 prompts, ChatGPT only**; Enterprise custom | **$180M Series D at $1.8B**, 2026-09-16 |

**Same-slot repos:** `ai-crawler-intercept` **1★** and `webserer_log_analyzer` **0★** ("Verifies crawler identity") — against `anubis` 22,512★ and `ai.robots.txt` 4,126★ in the adjacent *blocking* slot [m, `c1` §7]. Built twice already; the slot, not the idea, is where the pull is absent. **Ad verification does not reach AI answers:** DoubleVerify and IAS mention no ChatGPT or OAI-AdsBot [v absence]; OpenAI's ads lead, Digiday 2026-06-30, on verification partners: *"I don't have any names to announce."* Infrastructure floor: Workers free at 100,000 req/day, Paid **$5/mo**; a `.com` **$11.08/yr** [v].

### 2.3 Spoof rates — three figures, three populations, never averaged

| Figure | Population | Label |
|---|---|---|
| **31%** of GPTBot-identifying traffic spoofed | GPTBot only, "Cloudflare May 2026 Radar" | v, **primary URL unconfirmed** |
| **5.7%** of AI-crawler-labelled traffic; ratio 1:17 | 16 crawlers, two weeks, HUMAN Satori | v via snippet; page 403 |
| **17.1%** Amazonbot blocked by top websites | a *blocked* rate, not a spoof rate | v, Known Agents index |

All `c1` §11. Adjacent: Cloudflare's Aug-2025 test found Perplexity answering about robots.txt-disallowed domains through an undeclared Chrome-impersonating crawler — **3–6M daily undeclared against 20–25M declared** [v]. No equivalent test of OpenAI or Anthropic exists.

### 2.4 Policy ceiling

| Instrument | Verbatim fragment | Date | Bars |
|---|---|---|---|
| Google spam policies | "attempting to manipulate generative AI responses in Google Search"; cloaking = "inserting text… only when the user agent… is a search engine" | `Last Updated: 2026-08-28`; the 2026-05-15 change date `unk` | Crawler-conditional serving to manipulate |
| Google AI-features doc | "There are no additional requirements to appear in AI Overviews or AI Mode" | 2026-09-17 | Denies the premise 8 VN agencies sell |
| OpenAI ad policies | "Ads must be consistent end-to-end"; "Destination integrity" | "Updated: August 10, 2026" | Destination integrity on advertisers |
| OpenAI ToU · Perplexity ToS | "Automatically or programmatically extract data or Output" · s5.2(i) bars robots "or engage in any manual process to do the same" | 2026-01-01 · 2026-01-23 [f] | Consumer sampling, scripted and hand-run. **The paid API path is unbarred** |
| UCPD via UK CPUTR 2008 Sch.1 ¶11 | "editorial content… where a trader has paid… without making that clear (advertorial)" | per se unfair [f] | Undisclosed paid placement |
| VN Luật 75/2025/QH15 Điều 23 | 23.2(a) "dấu hiệu nhận diện rõ ràng"; 23.2(c) duty to check linked destinations | **effective 2026-01-01** [f] | All online ads visibly distinguished. Its decree was **never located**, `unk` |

Bing's guidelines were rewritten ~2026-03 adding a "Prompt Injection and AI Manipulation" section [secondary]; a rival source's "Generative Cloaking" wording is **uncorroborated**, live page unreachable. The FTC's Endorsement Guides mention **no** AI-generated recommendations; whether DSA Art. 26 reaches AI answers is `unk`. Consequence, once: measurement on the paid API path and on a domain you own is unbarred; differential serving is barred by three separate published documents (`F/pass4-read.md`).

### 2.5 What changed in 2026

ChatGPT sponsored cards live **2026-02-09** (US free tier), Ads Manager **2026-05-05**, five more countries by **2026-08-11**, **$1B annualized run rate in under 200 days** [cs]. Perplexity **exited** ads Feb 2026; Rufus Sponsored Prompts GA US **2026-03-25**. Cloudflare shipped **"Redirects for AI Training", 2026-04-17** — paid-tier, crawler-identity-conditional [v]. Range files, all [m]: GPTBot **21 prefixes, static since 2025-10-30**; **ChatGPT-User 215, regenerating hourly**; **OAI-AdsBot 2, `creationTime 2026-05-12`**; Anthropic **26, 2026-08-18 — correcting pass 2's relayed 20**; **Amazonbot 1,292 entries, 2026-09-08**. **OpenAI's sampled crawler IPs returned no PTR record, 3/3** — Google's rDNS procedure does not transfer. Web Bot Auth reached OpenAI's ChatGPT *agent* (2025-08-28) and reportedly Google's crawlers (June 2026, unconfirmed) but **names none of GPTBot, OAI-SearchBot, ClaudeBot or PerplexityBot** [v, `c1` §10].

### 2.6 Bottom-up sizing, arithmetic shown

Mordor's "$4.39B (2026) → $10.72B (2031)" [a] is inadmissible, quoted to reject.

```
N_buyers  = 8               [m, named VN GEO/AEO agencies, A/raw/vietnam-ai-visibility-demand.md]
ARPU      = 15,000,000 VND  [oj; anchors SEODO "Từ 18 triệu", Hashmeta's free "trị giá 15.000.000đ"]
share     = 0.10            [oj; §B5 ceiling — 0 contacts, 0 replies, all passes]
cycles/36 = 3               [oj]
market_36 = 8 × 15,000,000 × 0.10 × 3 = 36,000,000 VND (≈ USD 1,357)
break-even N against the contract anchor in §5 = 589 named buyers
```

The largest named set in this project's `raw/` is 8. W3Techs shares do not substitute — Cloudflare **25.8% of all websites** [a; older cuts 23.4% and 21.3%, side by side], nginx 30.9%, Apache 22.0% — a share carries no denominator (top-1M breakout `unk`) and is not a count of named entities.

### 2.7 Unknown in A

No real 2025–2026 public access log with AI-crawler UAs — `unk` Kaggle, GitHub, SecRepo, vizsec. No incumbent installed or run. Google Trends `unk`, no browser. The primary Radar page behind 31%, not located. Whether the 8 agencies are customers or competitors — `unk`, landing pages only, **none contacted**.

---

## 3. Market B — agent workflow observability and Claude Code tooling

### 3.1 Demand

Anthropic publishes multiples and run-rates, never a headcount [all cs, relayed, `c2` §4]: Claude Code run-rate **"over $2.5 billion"**, doubled since the start of 2026; weekly actives doubled since January 1; **$1B annualized within six months** of the May 2025 launch; "the average developer using Claude Code spending 20 hours a week". Absolute WAU/MAU — `unk` 2026-09-18.

Counted first-hand, `gh api` 2026-09-17, title-scoped in `anthropics/claude-code` [m]: `usage limit` **828**, `rate limit` 733, `cost` 355, `budget` 153 — against a **control query of 42** and **93,582 titled issues, so 828 is 0.88%**, last of eleven topics sampled, 87.8% closed. Verbatim: *"One subagent, resumed 8 times, accounted for 50.7% of that week's entire consumption"* (#91220, 2026-09-01). **The demand addresses the vendor**: #20636, the top feature request here, was filed 2026-01-24 and closed `completed` 2026-04-24 — **absorption, one quarter**. Proxies, conflicting and barred by §F5: r/ClaudeAI ≈1.1M / 1,093,707 / 1,043,382 across three trackers; Discord **123,662 vs 127,191** [a]. First-person "I run my business with Claude Code" posts: 3–4, `unk` no denominator.

### 3.2 Supply

| Incumbent | Its own words | Price | Inspected |
|---|---|---|---|
| `/insights` | "analyzes your recent sessions… friction points… suggestions"; no "recurring", "pattern", "suggest a skill" | $0 bundled | docs only; **never run** |
| CHANGELOG 2.1.179→2.1.276 | No recurrence detection in 7,063 lines; `/loop` and cron are forward scheduling | $0 | m, grepped |
| `--max-budget-usd`, v2.1.217+ | "Maximum dollar amount to spend… Spend from subagents counts toward the cap" | $0, shipped | v |
| Braintrust | **Two readings, side by side:** a rename to **Topics**; or **Topics GA 2026-06-01** *plus* **Patterns preview 2026-09-03**. Output is eval datasets and review queues, not a runnable artifact | free 10k scores; **Pro $249/mo** | docs only |
| LangSmith LLM Gateway, 2026-07-30 | Org/workspace/key/user spend caps; **HTTP 402 on cap hit** | $39/user/mo + $2.50/1k over 5k | v |
| `kenn-io/agentsview` | "Local-first session search, analytics, insights… for coding agents" | $0 | **5,942★, not opened** |
| `coding_agent_session_search` | "index and search local coding agent session history across 11+ providers" | $0 | **1,136★, not opened** |
| `ccusage` | Dollars and 5-hour blocks; no task identity | $0 | 18,615★, not run |

Sources `c2` §1–3, §7, §13. **Function matrix**, 2026-09-17: watch-window reporting, runaway-spend caps and per-task attribution are all **solved and free or built in**; **deferring work before the wall is open**, best free tool `claude-session-budget` at **8★, unchanged in four months**. Price comparables [v, `c2` §8]: WakaTime $8.25/$11.00/$44.92; LinearB $29/$59; Swarmia $45/$55, free under 10 devs; DX **no public price**; Waydev **$449 vs $649** per contributor-year, unreconciled; SessionWatcher $6.99/$14.99/$59 or $24/yr; CrewTower $9.99 — **not re-confirmable**, `unk`. Star velocity, for reading any launch gate: ccusage **+249 in 14 days from a base above 18,000**. Weather: ClickHouse bought Langfuse 2026-01-16; Mintlify bought Helicone 2026-03-03, features frozen; AgentKit sunsets 2026-11-30 after **eight months**. Six analyst sizings of the same year span $0.9B–$19.33B and **none sizes "agent control plane" as a line**.

### 3.3 Billing and platform facts

Consumer Terms, "Last updated: October 8, 2025" [f], prohibit *"…to access the Services through automated or non-human means"* except via an API key or where otherwise explicitly permitted, and reserve the right to change capacity limits *"at any time without notice."* **The 2026-06-15 change never took effect** — support article 15036540, live 2026-09-18 [cs, `c2` §10]: *"We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits."* That corrects `H/docs/plan/re-pick.md`, which treats it as live. API list prices [v, `c2` §18]: Opus 5 $5/$25 per MTok, **Sonnet 5 $2/$10**, Haiku 4.5 $1/$5 — and the scheduled 2026-09-01 rise of Sonnet 5 **"will not occur"**. Credits above the allowance bill at **standard API rates**, daily cap **$2,000**. Measured: `Stop`/`SubagentStop` carry **no `cost`, no `duration_ms`** — v2.1.259, four live runs, reproduced twice [m].

### 3.4 What changed in 2026

Plugin marketplace **101 (Mar) → >200 (Jul) → 316 measured 2026-09-18** [m, live `marketplace.json`]. The allowance moved three times: 5-hour limits **doubled 2026-05-06**; a temporary weekly **+50%, 2026-05-13 → ~2026-09-13**; then a "permanent" **+25% over the 2025 baseline on 2026-09-14 — net −17%** against the boosted level [cs, relayed]. **No absolute token, message or hour figure for either window is published anywhere checked**, and article 8324991 now returns **HTTP 404**. OpenTelemetry's GenAI conventions were **deprecated and moved out of the main repo at v1.42.0 (2026-06-12)**; v1.43.0 and v1.44.0 shipped without them and the new repo has **no tagged release** — a cross-vendor fleet view still has no stable wire format.

### 3.5 Vietnam angle, and sizing

No Vietnam-specific demand, user or price figure exists here. A payout path does, and the pulls disagree: **Lemon Squeezy names Vietnam explicitly** [v, `H/docs/explore/gap-pulls.md`, 2026-09-17] versus `unk` 2026-09-18, not independently fetched [`c4` §9]. **Polar.sh lists "🇻🇳 Vietnam"** for Stripe Connect Express payouts [v]. Paddle supports Vietnam **by omission** from an exclusion list given as **28** in one pull and **29** in the other. Both MoRs charge **5% + $0.50**. Stripe still excludes Vietnam, includes Singapore [`audit` §3].

```
N_buyers  = unknown   [c2 §4, no Anthropic headcount; c2 §11, 3–4 posts, no denominator]
ARPU_yr   = $24       [v, SessionWatcher Pro. Comparables never averaged: $6.99/$14.99/$59
                       one-time; CrewTower $9.99/$14.99]
share     = 0.05      [oj; §B5 caps at 0.10, halved — the prior implementation of this exact
                       function took 8 stars in four months]
market_36 = N × 24 × 3 × 0.05 = N × $3.60
required N against the two founder anchors in §5 = 14,464 or 27,778 paying buyers
```

N is unknown, so the ratio is unknown. One figure sizes the ceiling honestly: **no disclosed revenue or customer count exists for any paid Claude Code third-party tool** — `unk` vendor sites, Product Hunt, IndieHackers, Gumroad, Lemon Squeezy. An absent number, not a low one.

### 3.6 Unknown in B

The user count and the allowance figure, both confirmed unpublished a third time. Any third-party revenue figure. `/insights` output (`requires-main-thread`). Whether agentsview or session-search already ship the function — **7,078 stars between them, neither opened**. Reddit, unreachable for the **third independent pass in this repo**.

---

## 4. Market C — LLM guardrail evaluation and AI safety services, Vietnam/SEA

### 4.1 Demand

**23 Vietnamese companies with a public Vietnamese-language LLM chat product were named** [m with URLs, `c3` §1], clearing the pre-registered ≥20 bar. Eight are profiled with dates (`D/docs/customers/hcmc-candidates.md`): **AI Hay** (HCMC; 15M+ downloads, 100M+ Q&A/month [cs, VnEconomy 2025-07-02]; $10M Series A), **Vbee** (Hanoi; "1M+ customers as of 06/2023" vs "2M+ users", unreconciled), **Filum AI** (HCMC + Singapore; $1M seed 2025-03-18), **TPBank T'AioX** (launched **2026-08-10**; router named ChatGPT, Gemini, Grok), **Viettel**, **VNPT AI** (2025-12-18), **Bộ Công An**, **MoMo** (Rasa + DIET). The other fifteen, each with a URL, include VNG/Kiki, FPT.AI (VietGPT announced 2026-06-20), VinAI, Vietcombank Digibot, VietinBank (2026-04-23), BIDV (March 2024), Lazada LazzieChat and Grab VN; **four rest on search synthesis with no primary page**, and "Be" was checked and not found. **3 of the 8 are HCMC-headquartered**, rows 9–12 of the 12-target contact list are `unk — not yet compiled`, and **none has been contacted**. **No safety, moderation or guardrail statement was found for any of the eight** [v absence, per-company `unk` with URL].

Job posts: **0 live VN postings confirmed** for `guardrail` / `LLM safety` / `red team`. Two expired BPO trust-and-safety roles — Concentrix in Quang Trung Software City, District 12, HCMC, and Transcosmos VN at **23–25 million VND** (403, snippet only); one global remote gig, 410 Gone [jp, `c3` §2]. LinkedIn was never checked. The candidates file names the pattern as the finding: companies hire for **LLM capability, not LLM safety**. Incidents: **0 Vietnam-specific** cases of a Vietnamese chatbot producing harmful Vietnamese output, 2025–2026 — `unk` VN news, two queries; every hit was global.

### 4.2 Supply

| Tool | Language position, verbatim where given | Price |
|---|---|---|
| promptfoo (OpenAI, 2026-03-09) | Global `language` field; `moderation` covers OpenAI, LlamaGuard 3/4 via Replicate, Azure. **No multilingual corpus; no `compare`/`diff`** | Community free; Enterprise quote-only |
| Azure AI Content Safety | `vi` **Supported, "Specially trained" blank**; "quality might vary… do your own testing" | **F0 5,000 records/mo, $0**; S0 $0.38/1,000 [secondary] |
| OpenAI `omni-moderation-latest` | **No language statement** — silence, not a claim | "free to use"; pricing page 403 twice |
| Llama Guard 3 / 4 | "English, French, German, Hindi, Italian, Portuguese, Spanish, Thai" — **Vietnamese absent**; HF tag `["en"]` | free weights, **manual gate** |
| Lakera Guard | "Observing 100+ languages in real-time" — **no list** | Community $0 / 10,000 req; a tracker adds $99 and $499 — **unreconciled** |
| Qwen3Guard-Gen | "119 languages and dialects" — **no Vietnamese line**; third label `Controversial` | Apache-2.0 |
| Granite Guardian 3.0–3.3 | `language: [en]`, "only trained and tested on English data" | Apache-2.0 |
| Detoxify · Perspective API | 7 languages named, Vietnamese excluded · 17/7 by attribute, **Vietnamese in none**; "no longer be in service after 2026" | Apache-2.0 · free |
| PyRIT · Giskard · Patronus | `search/code` "vietnamese" → **`total_count: 0`** · — · — | free · $0 + quote-only · "$10–$20 per 1,000 calls" [secondary, `unk`] |

Sources `c3` §3–8, `c4` Additional, `D/docs/explore/` (dataset-baselines, ungated-path, endpoint-shapes). **Vietnamese security vendors publish no price at all** — Viettel Cyber Security, VNPT, CMC, FPT IS, VSEC, CyStack all quote-only; FPT IS states "the cost… is not fixed" — `unk` six sites 2026-09-18. Same for four ISO 42001 certifiers; **QUACERT was not found at all**. The only real anchors are foreign: **Cobalt $3,500 per test**, live 2026-09-18; Synack ~$18,300 average; Astra's AI band **overlaps** the standard web-app band across three sheets — **no AI premium**. The non-regulatory trigger is thin: the **2026 SIG** questionnaire's headline change is mapping to ISO 42001, and *"Red teaming, adversarial testing and guardrails appear nowhere on that page."*

### 4.3 Measured evidence

One frozen set, `set_hash=8def883fed6824cb…`, 300 pairs / 600 prompts, harmful 200 / safe 100, RTX 3060 Ti, all [m] (`D/docs/outcome/parity-report-2026-09-18.md` T1):

| Model | Declared languages [v] | EN recall [CI] | VI recall [CI] | Gap pp | Indeterminate |
|---|---|---|---|---|---|
| Qwen3Guard-Gen-0.6B | "119 languages", vi not named | 91.5 [86.4–94.8] | 87.8 [81.9–92.0] | 3.7, CIs overlap | 16.0% (96/600) |
| Qwen3Guard-Gen-4B | same inherited claim | 92.1 [87.2–95.3] | 89.6 [83.9–93.4] | 2.5, CIs overlap | 18.3% (110/600) |
| Granite Guardian 3.0-2b | "only trained and tested on English data" | 94.0 [89.8–96.5] | 68.5 [61.8–74.5] | 25.5, no overlap | 0.0% |
| Granite Guardian 3.1-2b | same card | 93.0 [88.6–95.8] | 64.5 [57.7–70.8] | 28.5, no overlap | 0.0% |
| Detoxify multilingual | 7 languages, vi absent | 16.5 [12.0–22.3] | 1.5 [0.5–4.3] | 15.0, both near floor | 0.0% |

**The gap tracks the vendor's own language claim** — both non-overlapping gaps sit on cards declaring English-only, both overlapping gaps on the model claiming 119 languages; *"a model that claims 119 languages and shows a gap would be the interesting case, and none did."* The version diff 3.0-2b → 3.1-2b printed `PARITY GAP 25.5 pp -> 28.5 pp`, 40 new VI misses, `VERDICT: REGRESSION`, exit 1, while **English on the same category moved only 96.0% → 94.0%**. Two secondary findings hold: VI benign prompts false-positived at **25.0% vs EN 16.3%**, stable under every indeterminate treatment; VI drew ~50% more indeterminates. Matched-pair on the reference model: **2.0 pp, McNemar p ≈ 0.73**. The report disowns its own biggest category number — the 27.0 pp `hate` gap **is not a measured gap** (different denominators, intervals overlapping 10.2 pp, p = 0.5). Wall-clock, 600 prompts: **15m8.321s**. **No commercial endpoint has been run** — `requires-human`; every object measured is open-weights, not a commercial guardrail product (§F4). Corpora are SEA-HELM aegis2 (machine-translated) and MultiJail (human-translated), both MIT; **ViHOS contributed 0 rows** and **ViHSD is unused — its licence appears four ways**.

### 4.4 Regulation as event, not demand

| Instrument | Status | Does | Does **not** do |
|---|---|---|---|
| Luật 134/2025/QH15 | Passed 2025-12-10, **in force 2026-03-01** [f] | Self-classification; medium/high notified via the Điều 8 portal; Điều 11.1 disclosure at every tier | **Điều 14 is entirely process duties, no threshold.** "red team", "guardrail", "tiếng Việt" appear on no transcribed page |
| Điều 10.5.b · 13 | — | Medium risk supervised by report, sampling **or** independent assessment — the regulator's choice; mandatory assessment binds **high risk only** | Obliges no provider to buy an assessment |
| **NĐ 142/2026/NĐ-CP** | Issued 2026-04-30, **eff. 2026-05-01** [f, search synthesis] | Portal operation, national database, risk classification | Whether it defines assessment content — `unk` |
| **QĐ 33/2026/QĐ-TTg** | Dated 2026-06-30, **eff. 2026-08-15** [f, mst.gov.vn] | **46 AI systems classified high-risk** across six fields incl. banking, healthcare | These are system *types*, not companies |
| Grace dates | — | Health, education, finance by **2027-09-01**; other listed sectors **2027-03-01** | — |
| Decree 147/2024 | In force 2024-12-25 | Removal within 24 hours of an authority request | **Neither AI nor chatbots are named**; no enforcement found |
| Singapore AI Verify · Indonesia PDP | 2026 · — | **Voluntary** self-assessment on 11 principles · DPIA, fines to **2% of global revenue** | No testing mandate. **Malaysia and Thailand not researched** |
| EU AI Act | GPAI 2025-08-02; Art. 50 2026-08-02; high-risk **2027-12-02 / 2028-08-02** [f] | — | No red-teaming mandate anywhere |

Both the decree and the high-risk list are **new since the root research**, which recorded "no decree, no list". Neither creates a testing duty; §F9 permits citing them as an event and bars using them as demand. Statute pages 3 and 10–18, carrying the penalties, are `unk — not transcribed`; the Điều 8 portal URL was not located and **no count of notified systems exists anywhere**.

### 4.5 Benchmarks

**SEA-HELM has no English Safety task at all** — the active `toxicity` languages are `id, vi, th, tl, my, ms` with **no `en` arm**, so a VI-vs-EN Safety delta is **structurally unpublishable there, for any model** [v, `D/docs/explore/seahelm-scores.md`]. `safeguard_general`, which does hold a 600-item row-paired en/vi set, is **off** behind one commit dated 2026-04-20 — **151 days unchanged**. On the SEA-LION board (page dated Aug 5, 2026) the top VI Safety score is **Gemma 4 (31B), Google, 72.18 [-4.25,+4.03]**, and **no guardrail product appears among the 51 models scored**. Multilingual safety benchmarks skip Vietnamese: XSafety's 10 languages include zero SEA languages; ML-Bench (2026-05, 14 languages) returned **zero matches on all twelve SEA-language terms**. No Vietnamese-specific guardrail benchmark since 2026-09-01 — `unk` arXiv. Three countdown events, 2026-09-18: Llama Guard's card still stops at Thai; Azure's `vi` specially-trained column is still blank; SEA-HELM's task is still off.

### 4.6 Bottom-up sizing, arithmetic shown

```
N_buyers  = 23               [m, c3 §1; 4 rows weak, 1 a ministry, 0 contacted]
ARPU      = 15,000,000 VND   [oj ≈ $593 at 25,306. Anchors: ITviec 54.9M/mo gross [v] = 27% of one
                              month; Cobalt $3,500 US ≈ 88.6M VND, 5.9× higher, wrong market]
share     = 0.10  [oj]       engagements/buyer = 1  [oj]
market_36 = 23 × 15,000,000 × 0.10 × 1 = 34,500,000 VND (≈ $1,363)
break-even price at 100% share, one engagement each = 1,317.6M ÷ 23 = 57.3M VND per company
```

57.3M VND exceeds one month of the >8-year salary band, from every one of the 23; only a US-priced buyer clears it and none is on the list. Cash COGS is measured and negligible: 0.0504 kWh per run, at **2,204.0655 VND/kWh** (QĐ 1279/QĐ-BCT, 2025-05-09) ≈ **111 VND**, or at **5,422 VND/kWh** (business peak-hour, unconfirmed) ≈ **273 VND** — side by side. Labour dominates: 24 h at $25–80/h = 15.2M–48.6M VND, a negative margin at a 15M price.

### 4.7 Unknown in C

No commercial endpoint run; Vietnam billing eligibility for Azure F0 and OpenAI moderation `unk` both directions. No published VN price from any of ten vendors, no buyer-stated number, no LinkedIn job count, no portal count, no transcribed penalties. `market-check.md` §6b, verbatim: *"No census or count of Vietnamese companies operating a public Vietnamese-language chatbot has ever been pulled; the research layer names three companies, which is a list, not a market"* — the 23-count answers that; the price half stays open.

---

## 5. Founder context (`c4` only)

| Item | Figure |
|---|---|
| Back-end dev, >8 yrs, HCMC | **54.9M VND/mo median**, n=1,839, ITviec 2025–2026 [v, §1] |
| AI Engineer/Blockchain Engineer, 4 yrs | 37.75M VND/mo, n=2,324 — **2024–2025 edition**, two roles bundled [v] |
| AI rate cards, conflicting, never averaged | Second Talent senior ₫85–125M/mo; reco-vn 25–100M, senior to 150M; HUFLIT $3,000–5,000/mo at 5–7 yrs [a] |
| P75 by role | `unk` ITviec, TopDev, Robert Walters, Michael Page — registration gates |
| Upwork, VN AI engineers | $25–$80/h typical; 5–8+ yrs $75–$135/h; fees cut effective rates 20–30% [v] |
| Living cost, conflicting | Numbeo **$492.90/mo excluding rent** (Aug 2026); $700–$1,300 with rent; $900–$1,400 comfortable. **The on-file $2,800–4,500 expat figure was not reproduced** [a] |
| VND/USD | SBV central **25,306**, 2026-07-27, record; Vietcombank 26,525; a secondary claims 25,617 near 2026-09-18 — side by side. Rate on 2026-09-18 `unk` [f/v] |
| Clinic-MCP rate; own burn; subscription tier | `requires-human — not pulled` |

**Named VN AI rounds** [cs/press, §6], only three cleanly seed: **enfarm** (Touchstone lead, undisclosed, 2025-01-07); **Filum AI $1M seed**, 2025-03-18, Nextrans / VinVentures / TheVentures plus angels Trần Việt Hùng and Trần Anh Dũng; **NamiTech $4M**, January 2026 — stage ambiguous, it raised $2M in 2023. **AI Hay's $10M Series A** (Argor Capital, 2025-07) is named for context. **Check sizes** [v/a, §6b]: Antler VN **$100K–$150K** ($2.2M across 21 deals in 2024); Touchstone **$200K–$1M**; ThinkZone **$850K average round**; Genesia **max $4M per company**; 500 Global SEA III **$250K–$500K**; Ascend Vietnam **$250K–$2M**; Do Ventures — $50M fund, **no per-deal figure found**. Ecosystem totals conflict [a, §7–8]: Do Ventures' report covers **2024** ($2.3B / 141 deals, "AI funding surged 8x", no AI dollar total); Tracxn live shows **$295M across 15 rounds through August 2026**, all-sector, and its VN generative-AI cut reads **$18.2M cumulative (May 2026) vs $10M through July 2025**. The $130M / "765+ startups" blog figures were checked and **not** replaced; they stay inadmissible. Now primary-sourced: **Singapore $9.3B across 227 rounds; Vietnam $19M; Malaysia $8M; Indonesia $6M; Thailand $4M** — Tracxn SEA AI Startup Landscape 2026, as of July 2026.

**A named, dated Vietnam seed-investor traction quote: `unk`** — checked Do Ventures, ThinkZone, Touchstone, 500 Global VN. Generic comparables: Point Nine's most recent located Funding Napkin is **2023** (seed $4–5M at $10–20M pre, about half with no recurring revenue; Series A $5–15M at $20–60M, $1–5M ARR); YC: *"On average, 40% of the companies YC funds in each batch are just an idea and most don't have any revenue"* [cs]. Channels [v, §11]: Instantly 2026 **3.43%** average reply; Belkins 2025 **cybersecurity 4.86%** across 16.5M emails — beside an all-industry **0.45%** in the same study, ~10× apart, denominators unexplained; Expandi 2026 LinkedIn DM **10.3%**.

---

## 6. Cross-market table — the 14 criteria, number or `unknown`

Numbers only; no PASS/FAIL. Cells cite `c1` §8–19, `c2` §4–17, `c3` §1–20, `c4` §11, and the three reviews' §1 tables.

| # | Criterion | A | B | C |
|---|---|---|---|---|
| A1 | Severity, frequency | 0 conversations; HN 305 pts | 0 conversations; 3–4 posts, no denominator | 0 conversations; 0 VN incidents |
| A2 | Buyer identity, reach | 8 agencies, never frozen, 0 reached | 0 named organisations | 23 named, 8 profiled, 0 reached |
| A3 | Willingness to pay | 0 deposits, 0 LOIs, 0 asks | 0; not published | 0; nothing published |
| A4 | Price point | No price a buyer said or paid | None from any named buyer | None; 10 VN vendors quote-only |
| A5 | Bottom-up size | 36,000,000 VND / 36 mo | `unknown` — N has no source | 34,500,000 VND / 36 mo |
| A6 | Incumbent coverage | 5 docs-inspected; **0 run** | 0 of 5 run first-hand | promptfoo docs-only; 5 open models run |
| A7 | Why now | ChatGPT ads 2026-02-09 | Marketplace 101→316 | Law 134; NĐ 142; QĐ 33 |
| A8 | Channel with cost | 0 sent, 0 replies | 0 sent, no repo published | 0 sent; 3.43% / 4.86% / 10.3% |
| A9 | Moat, time-to-copy | 1,640 lines; 8–16 hours | 1,618 lines; 2–4 days | corpus public MIT; task off 151 days |
| A10 | Real-input proof | 0 real logs located | 0 real ledgers; `Stop` never observed | 5 open-weights × 600; 0 commercial |
| A11 | Unit economics | CAC `unknown`, 0 replies ever | price $0 by design; CAC `unknown` | COGS 111–273 VND/run; CAC `unknown` |
| A12 | Founder-market fit | No domain or server on this machine | Founder is the buyer, real `history.jsonl` | Not a chatbot operator; 3 of 8 HCMC |
| A13 | Time-to-first-dollar | Stop rule 2026-09-17; no invoice | No path to a first dollar by design | T0 unset; nothing published |
| A14 | Kill rule | Pre-registered 2026-09-17 | Pre-registered 2026-09-17 | Pre-registered 2026-09-18 |

Founder-cost anchors, side by side, never averaged: **salary** 658,800,000 VND/yr ≈ $26,035 [v]; **contract** $25/h × 2,000 h = $50,000/yr ≈ 1,326,250,000 VND [v]. §B14 takes the higher; the clinic-MCP rate could raise it and is `requires-human`.

---

## 7. What changed since the root research was written

Root files date 2026-09-16/17.

| Item | Old | New (2026-09-18) | Source |
|---|---|---|---|
| XBOW total funding | $195M implied | "over $235M" — a round unaccounted for | `audit` §3 |
| Anthropic bounty cap | max $15,000 | $15,000, **$35,000 "per novel jailbreak"**, $25,000 — unresolved | `audit` §3 |
| AI Hay founders | "founders not named" | **Chuong Nguyen, Duc Tran, Hiep Nguyen**, founded 2021 | `audit` §3 |
| `claude -p` billing | withdrawal treated as live | **Paused; never took effect** | `c2` §10 |
| Braintrust clustering | "Patterns", never pulled | Rename to **Topics**; or Topics GA 2026-06-01 **plus** Patterns preview 2026-09-03 | `c2` §3 |
| Sonnet 5 price | rising to $3/$15 on 2026-09-01 | The increase **"will not occur"** | `c2` §18 |
| Plugin marketplace | ~101 / >200 | **316**, live `marketplace.json` | `c2` §6 |
| Dark Visitors | named as such | redirects to **Known Agents** | `c1` §3 |
| Anthropic crawler prefixes | 20, relayed | **26**, fetched, `creationTime 2026-08-18` | `A/docs/explore/detection-surface.md` |
| VN AI Law decree | "no decree found" | **NĐ 142/2026/NĐ-CP**, eff. 2026-05-01 | `c3` §11 |
| PM high-risk list | "has not been issued" | **QĐ 33/2026/QĐ-TTg**, 46 systems, eff. 2026-08-15 | `c3` §11 |
| SG vs VN AI funding | $9.3B vs $19M, secondary | Same, now primary: Tracxn SEA 2026, 227 rounds | `c4` §8 |
| HCMC expat cost | $2,800–$4,500/mo | **Not reproduced**; 2026 sources cluster $700–$1,900 | `c4` §4 |
| Claude Code allowance | assumed stable | Doubled 2026-05-06; +50% to ~2026-09-13; +25% on 2026-09-14 = **net −17%** | `H/docs/explore/gap-pulls.md` |
| OTel GenAI conventions | moved at v1.42.0 | Still **no tagged release, all `[Development]`** | `H/docs/explore/control-planes.md` |
| Perspective API | a moderation option | **Sunsetting** — out of service after 2026 | `D/docs/explore/ungated-path.md` |
| Same-slot crawler verifiers | not known to exist | **Two found**, 1★ and 0★ | `c1` §7 |

Re-verified live and unchanged: Otterly $29/$189/$489; Profound $180M at $1.8B; Cobalt $3,500; Stripe supports Singapore not Vietnam; AWS Marketplace excludes both; Check Point–Lakera ~$300M (`audit` §3).

---

## 8. What the research still cannot say

| Market | Gap | Cheapest close |
|---|---|---|
| A | No free incumbent run first-hand | Install GoAccess, run on the fixture — ~1 h, $0 |
| A | No real access log with AI-crawler UAs | One log from a site operator — ~3 h, else `requires-human` |
| A | Which of 31% / 5.7% / 17.1% is the spoof rate | Fetch the primary Radar 2026 report — browser; 403 to fetch tools |
| A | Whether anyone pays for measurement | The 20-organisation probe, 15.000.000 VND, day-7 — `requires-human` |
| B | `/insights` never run — the primary incumbent | Run it, paste headings — minutes, `requires-main-thread` |
| B | agentsview and session-search never opened | Read both READMEs — ~2 h, $0 |
| B | No user count, no allowance figure, no third-party revenue | Likely not closable for the counts; ask one seller — `requires-human` |
| B | Whether a VN seller is actually paid | Onboard Polar.sh or Lemon Squeezy to KYC — `requires-human` |
| C | No commercial endpoint measured, yet buyers run those | One Azure account; F0's 5,000 records holds 600 prompts free — `requires-human` |
| C | Vietnam billing eligibility for F0 / OpenAI | Read Azure's region and billing pages in a browser |
| C | No Vietnamese price for security-testing work | Three buyer-side quote requests: Viettel, VSEC, CyStack — `requires-human` |
| C | No buyer-stated price | Three Mom-Test conversations: AI Hay, Filum AI, MoMo — `requires-human` |
| C | 0 live LLM-safety job posts; LinkedIn unchecked | One browser pass over LinkedIn and TopCV for the eight |
| C | Điều 8 portal count; Law 134 penalties | Browser pass over vbpl.vn; transcribe statute pages 3 and 10–18 |
| All | Founder opportunity cost | Clinic-MCP rate, hours, burn, tier — `requires-human`. Every ratio in §2.6, §3.5, §4.6 moves |

---

## 9. Caveats

- **No buyer has been contacted in any market, by any agent, in any pass.** Every negative here is search-level or page-level. Per §F1, where zero humans were asked the cell is `unknown` — not `FAIL`, not `PASS`.
- **Every size here is bottom-up from small counts of named entities** (8, 23, and an unknown). The analyst TAMs — Mordor $4.39B; six reports spanning $0.9B–$19.33B; four spanning $500.8M–$4.2B — are quoted only to reject them. The `audit` records the structural gap: *"no file anywhere constructs or cites an independent bottom-up figure to check an analyst TAM against."*
- **Audit CHANGED rows carried forward:** the XBOW total undercounts by a round; the Anthropic bounty cap returns three values; the "AI Hay founders not named" caveat is falsified. None invalidates the claim beside it.
- **Tool-boundary gaps, stated so they are not read as market facts.** No browser for `c1`, `c2`, `c4`; `c3`'s Chrome extension reported not connected every time. Google Trends, Reddit (third pass to fail), LinkedIn job counts, the Điều 8 portal and Cloudflare's Radar and pricing pages were unreachable. `c1` records two WebFetch summarisation errors on one page (1,072 and 1,040 against a `curl`-measured 1,292). `c3` §19 discloses two read-only git commands run inside `D/` before the no-git constraint was re-checked; nothing was staged or committed.
- **Vendor-stated figures are labelled and never a sole sizing input** (§F10): Known Agents' 2,000+ agents, Lakera's tiers, the Second Talent rate card, the VN agency price lists, Anthropic's run-rate.
- **The five measured guardrail results are open-weights models, not commercial products** (§F4) — one frozen 300-pair set, one machine, one run each, one date, per-category n of 1–32. Neither corpus arm is native Vietnamese text.
- **This file compiles from compiled files in places**, which `evidence-rules.md` rule 3 restricts. Where it does, the figure's own raw citation is carried and hedges travel with their sentences (rule 4). The sizing blocks reproduce arithmetic first written in the stage-3 reviews; every input is cited to a raw pull and every `oj` input labelled, so one can be changed and the result recomputed.
- **Length.** This file runs above the 3,000–4,500-word brief. The required contents — three markets at demand/supply/price/policy/2026/sizing depth, plus the 14-criterion table, the change table, the gap table and a complete source list — did not compress further without dropping a required element or a labelled number.

---

## Sources

**Rules and method:** `CLAUDE.md`; `docs/CLAUDE.md`; `docs/method/scope.md`; `docs/method/evidence-rules.md`; `projects/investment-review/FRAMEWORK.md`.

**Root:** `M/ai-search-ads.md`, `agent-dashboard.md`, `ai-attack-defense.md`, `ai-attack-defense-services.md`, `vietnam-sg-access.md`, `ai-trend-suite.md`, `creative-ai-lane.md`; `F/market-gaps-2026.md`, `cross-read.md`, `pass2-read.md`, `pass3-read.md`, `pass4-read.md`, `localization-play.md`, `injection-feasibility.md`, `two-founder-cases.md`; `Cu/first-customers.md`, `answer-integrity-buyer.md`; `docs/competitors/INDEX.md` and the three rosters.

**2026-09-18 pulls:** `c1`, `c2`, `c3`, `c4`, `audit`.

**Stage-3 reviews** (sizing arithmetic and incumbent tables only; verdicts not used): `review-aicrawlcheck-2026-09-18.md` §1, §4, §5; `review-foreman-2026-09-18.md` §1, §4, §5; `review-parity-vi-2026-09-18.md` §1, §2, §2b, §5, §6.

**Project docs and raw:** `A/docs/review/market-check.md`; `A/docs/explore/` (carrier-state, cost-and-demand-pulls, detection-surface, edge-controls, policy-ceiling, policy-ceiling-addendum, who-sells-this); `A/raw/` (vietnam-ai-visibility-demand.md, oai-adsbot.json, openai-ad-policies.txt, ucpd-annex1-uk.html, vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt, local-infra-check.txt). `H/docs/review/market-check.md`; `H/docs/explore/` (claude-code-substrate, control-planes, gap-pulls, hermes-substrate, smallbiz-blind-spots, task-telemetry, telemetry-measured); `H/raw/` (hook-payload-measurement-2026-09-17.md, 2abis-demand-signal-interrogation-2026-09-17.md). `D/docs/review/market-check.md`; `D/docs/explore/` (aisb-inventory, dataset-baselines, endpoint-shapes, language-gap, local-assets, sea-compliance-triggers, seahelm-scores, shipping-tools, ungated-path); `D/docs/outcome/` (parity-report-2026-09-18.md, hcmc-opener-2026-09-18.md); `D/docs/customers/hcmc-candidates.md`; `D/raw/` (repick-vietnam-ai-law-pull.md, seahelm-leaderboard-pulls-2026-09-18.md).

**Read only to avoid duplicating it, no figure taken:** `projects/investment-review/REPORT.md` (headings), which carries the project-level verdicts this file does not repeat.
