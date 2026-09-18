# C1 `aicrawlcheck` pulls — 2026-09-18

Stage 2 pull against `projects/investment-review/FRAMEWORK.md` §C1 (`ai-ads-injection`). Read first: FRAMEWORK.md §§B, C1, F (whole file); `projects/ai-ads-injection/docs/outcome/review.md`; `projects/ai-ads-injection/docs/plan/re-pick.md`; `projects/ai-ads-injection/docs/explore/detection-surface.md`; and every file under `projects/ai-ads-injection/raw/` referenced below. No Chrome/browser tool used — WebSearch, WebFetch and direct `curl` (network-reachable from this sandbox) only. One H3 per §C1 line, in §C1 order, heading = the line's own text verbatim.

---

### 1. **A6 KILL** — Does GoAccess verify a claimed crawler UA against published IP ranges (feature name, version, changelog date) — goaccess.io docs, `github.com/allinurl/goaccess` (search `bot`, `crawler`, `ip range`, `verify`), issues — `vendor-reported`; run it on the fixture if installable, `measured-by-us`

- **No such feature exists.** — vendor-reported — GoAccess FAQ, goaccess.io, checked 2026-09-18 — `https://goaccess.io/faq`. The FAQ covers performance, log config and report generation; it contains no mention of bot verification, crawler IP verification, or reverse-DNS checks.
- **Zero open/closed issues match the search.** — vendor-reported — GitHub issue search, checked 2026-09-18 — `https://github.com/allinurl/goaccess/issues?q=bot+crawler+verify+ip+range`. Page result: "No results - Try adjusting your search filters."
- **What GoAccess does instead:** ASN mapping and a Hosts panel with reverse-DNS display, plus IP-range *exclusion* (not verification) and heuristic "classify unknown OS/browser as crawler." — vendor-reported — WebSearch summary of goaccess.io/features + goaccess.io/release-notes, checked 2026-09-18.
- **Not installed/run this pull** — no Python/binary install attempted; the FAQ/issue/feature evidence above is unambiguous enough that a local run would not change the answer. `measured-by-us` portion of this line not executed — recorded, not a guess.

Conclusion: GoAccess has no crawler-identity-verification feature, at any version, as of 2026-09-18. `not found in {FAQ, features page, release-notes, issue tracker} — checked goaccess.io + github.com/allinurl/goaccess 2026-09-18`.

---

### 2. **A6 KILL** — Same for AWStats (`robots.pm` list, any IP verification) and Matomo Log Analytics + DeviceDetector bot list — awstats.sourceforge.io, matomo.org/docs/log-analytics, `github.com/matomo-org/device-detector` — `vendor-reported`

- **AWStats `robots.pm` is user-agent regex matching only, no IP or rDNS check.** — vendor-reported — `github.com/eldy/AWStats`, `wwwroot/cgi-bin/lib/robots.pm`, checked 2026-09-18 — `https://raw.githubusercontent.com/eldy/AWStats/develop/wwwroot/cgi-bin/lib/robots.pm`. File's own doc comment: "There are several sorts of bots that AWStats is not able to detect and therefore a considerable amount of bot generated traffic counts as user traffic." The matching arrays (`@RobotsSearchIDOrder_list1/2`, `%RobotsHashIDLib`) are Perl regexes applied to the UA string only.
- **AWStats changelog has no IP/rDNS-verification entry.** — vendor-reported — `awstats_changelog.txt`, checked 2026-09-18 — `https://awstats.sourceforge.io/docs/awstats_changelog.txt`. "None found" for any entry addressing verifying a bot's claimed identity against IP ranges or reverse DNS.
- **Matomo DeviceDetector is UA-string pattern matching only.** — vendor-reported — GitHub README, `matomo-org/device-detector`, checked 2026-09-18 — `https://github.com/matomo-org/device-detector`. README describes it as "The Universal Device Detection library that parses User Agents and Browser Client Hints"; exposes `isBot()`/`getBot()`, no IP-range verification documented.
- **Matomo Log Analytics docs page returned HTTP 404 on this pull** — `unknown — checked https://matomo.org/docs/log-analytics/ 2026-09-18, 404`. The DeviceDetector evidence above stands in for it; both are the same vendor's bot-list mechanism per Matomo's own architecture (Log Analytics uses DeviceDetector for bot classification).

Conclusion: neither AWStats nor Matomo (via DeviceDetector) does IP-range or rDNS verification of a claimed crawler identity — both are UA-pattern matchers, same category as `aicrawlcheck`'s weakest branch, not its strongest. `not found in {AWStats robots.pm source, AWStats changelog, DeviceDetector README} — checked github.com/eldy/AWStats, awstats.sourceforge.io, github.com/matomo-org/device-detector 2026-09-18`.

---

### 3. A6 — Known Agents: does an access-log upload/import exist as of 2026-09; current tiers and prices ($0 / $29 / $299 on file) — knownagents.com/pricing, /docs — `vendor-reported`

- **No log-import/upload feature.** — vendor-reported — `https://knownagents.com/pricing`, re-fetched 2026-09-18 — page's own FAQ: "Every call to the Known Agents API counts toward your event usage. This includes sending visit events, making Agent Identification API requests, and making other API requests." No mention of importing or uploading an existing access-log file; the product is real-time event/API tracking only.
- **Tiers unchanged since the 2026-09-17 pull on file.** — vendor-reported — `https://knownagents.com/pricing`, re-fetched 2026-09-18 (cf. `projects/ai-ads-injection/raw/wave2b-crawler-analytics-competitors.md` §1b, pulled 2026-09-17) — Free **$0/mo, 100K events**; Startup **$29/mo, 1M events**; Growth **$299/mo, 10M events**; Enterprise custom/usage-based. Re-verification found no price or tier change in 24 hours.

This closes the incumbent-coverage question directly: as of 2026-09-18 no free incumbent (Known Agents included) reads a log file the operator already has — every one of them is a forward-looking event sender. Confirms `aicrawlcheck`'s "reads an existing log retroactively" as the one feature gap, still unshipped by the incumbent with the most similar taxonomy.

---

### 4. A6 — Cloudflare AI Crawl Control: any "historical log import" or retroactive view in the changelog since 2026-08-14 — developers.cloudflare.com changelog — `vendor-reported`

- **No historical-log-import entry.** — vendor-reported — `https://developers.cloudflare.com/ai-crawl-control/changelog/`, checked 2026-09-18. The changelog's visible entries run 2024-09-23 → 2026-06-16 (most recent visible entry: "Pay Per Crawl advanced configuration" — disable by URI pattern, dynamic pricing). No entry after 2026-08-14, and none of the entries present mention historical log import, retroactive log upload, or importing existing access logs.
- **Overview page's own "Last Updated" stamp is still Aug 14, 2026** — vendor-reported — `https://developers.cloudflare.com/ai-crawl-control/`, cf. `projects/ai-ads-injection/raw/policy-and-edge-pulls.md:60` (2026-09-17 pull: "page has not moved since" a pass one month earlier). Re-checked 2026-09-18: same stamp, no change.
- **Caveat, stated plainly.** The changelog page and the overview page's "Last Updated" stamp are two different pages; the changelog's own most-recent-entry date (2026-06-16) is *older* than the overview page's stamp (2026-08-14), meaning the overview page changed for a reason not itself listed in the changelog feed captured here — a gap in the changelog's own completeness, not evidence of a hidden feature.

Conclusion: no retroactive/historical-log-import capability has shipped in Cloudflare AI Crawl Control as of 2026-09-18. `not found in {ai-crawl-control changelog page} — checked developers.cloudflare.com 2026-09-18`.

---

### 5. A5 — Share of all websites behind Cloudflare, and share of top-1M — W3Techs "Cloudflare usage statistics" (method stated) — `analyst-derived`; this sizes the "not behind Cloudflare" population

- **25.8% of all websites, 85.1% of websites with a known reverse proxy.** — analyst-derived — W3Techs, live page, fetched 2026-09-18 — `https://w3techs.com/technologies/details/cn-cloudflare` — "Cloudflare is used by 85.1% of all the websites whose reverse proxy service we know. This is 25.8% of all websites."
- **Conflicting, lower, older figures found in search snippets, side by side, not averaged:** "23.4% of all websites" dated June 2026, and "21.3%" dated January 2026 — analyst-derived, secondary (WebSearch snippets of W3Techs pages `technologies/comparison/dn-cloudflare` and `technologies/details/ta-cloudflare`, not independently re-fetched) — these snippets read from different W3Techs technology categories (DNS-provider and web-analytics tabs respectively, not the reverse-proxy tab used for the 25.8% figure above), so the rising trend (21.3% → 23.4% → 25.8%) is directionally consistent but the three numbers are not strictly the same metric.
- **Top-1,000,000-websites share: not stated on the page fetched.** `unknown — checked https://w3techs.com/technologies/details/cn-cloudflare 2026-09-18` — the live page gives only the all-websites and known-reverse-proxy percentages, no separate top-1M breakout.

This sizes the "not behind Cloudflare" population at roughly **74.2% of all websites** (100% − 25.8%), the addressable population for a log-file tool that only matters off Cloudflare's own dashboard.

---

### 6. A5 — Web-server share nginx / Apache / other — W3Techs — `analyst-derived`

- **nginx 30.9%, Cloudflare Server 30.8%, Apache 22.0%, LiteSpeed 14.5%, Node.js 7.2%** — analyst-derived — W3Techs, live page, fetched 2026-09-18 — `https://w3techs.com/technologies/overview/web_server` — "Nginx is used by 30.9% of all the websites whose web server we know." Page notes a website may use more than one web server, so shares can overlap and need not sum to 100%.

---

### 7. A5 — Count of public OSS tools in the same slot with stars, last commit: `ai-robots-txt/ai.robots.txt`, `TecharoHQ/anubis`, `nginx-ultimate-bad-bot-blocker`, any "crawler verify" / "bot verification log" repo — GitHub API — `measured-by-us`

- **`ai-robots-txt/ai.robots.txt`** — 4,126 stars, last commit 2026-09-17, "A list of AI agents and robots to block." — measured-by-us — GitHub API, fetched 2026-09-18 — `https://api.github.com/repos/ai-robots-txt/ai.robots.txt`.
- **`TecharoHQ/anubis`** — 22,512 stars, last commit 2026-09-17, "Weighs the soul of incoming HTTP requests to stop AI crawlers" — measured-by-us — GitHub API, fetched 2026-09-18 — `https://api.github.com/repos/TecharoHQ/anubis`.
- **`mitchellkrogza/nginx-ultimate-bad-bot-blocker`** — 4,794 stars, last push 2026-09-15 — measured-by-us — GitHub search API, fetched 2026-09-18 — `https://api.github.com/search/repositories?q=nginx-ultimate-bad-bot-blocker`.
- **Two direct competitors surfaced by a "crawler verify" / "bot verification log" name+description search, both very low-traction:**
  - `Unsourced-Founder/ai-crawler-intercept` — **1 star**, last push 2026-08-07 — "Detect, verify, and log AI crawlers at the edge — no blocking. A Cloudflare Worker that confirms which AI bots really fetch your site."
  - `evemilano/webserer_log_analyzer` — **0 stars**, last push 2026-09-02 — "Multi-site nginx access-log analyzer: turns rotated log archives into self-contained, interactive HTML reports. Verifies crawler identity."
  - measured-by-us — GitHub search API, fetched 2026-09-18 — `https://api.github.com/search/repositories?q=crawler+verify+bot+verification+log+in:name,description&sort=stars&order=desc` (only 2 results returned).

These two are the closest same-slot competitors found anywhere in this project's research: one is an edge-Worker verifier (0-blocking, like `aicrawlcheck`'s philosophy) at 1 star; the other is explicitly an "access-log analyzer" that "verifies crawler identity" at 0 stars and a push two weeks before this pull. Neither has meaningful traction, but their existence means "nobody has built this" (F2 trap) is false — the idea has been built at least twice, unsuccessfully by star-count.

---

### 8. A1 — Count of HN and r/selfhosted threads 2025-01..2026-09 about AI-crawler bandwidth/spoofing; top thread points and comment counts — HN Algolia API (`query=GPTBot`, `ClaudeBot`, `AI crawler`), old.reddit search via Chrome — `measured-by-us` (visibility proxy, say so)

- **`GPTBot` query: 23 hits total** (HN Algolia, story tag). Top bandwidth/spoofing-relevant results: "GPT Bot Ignoring Robots.txt on my cloudflare worker" (3 pts / 9 comments, 2026-02-25); "57% of sites that block GPTBot leave ChatGPT-User wide open" (2 pts / 1 comment, 2026-09-02). — measured-by-us — HN Algolia API, fetched 2026-09-18 — `https://hn.algolia.com/api/v1/search?query=GPTBot&tags=story`.
- **`ClaudeBot` query: 437 hits total.** Top result by far: **"Someone is running mass vulnerability scans, spoofing AI bots like ClaudeBot" — 305 points, 228 comments, 2026-08-12** — measured-by-us — same API — `https://hn.algolia.com/api/v1/search?query=ClaudeBot&tags=story`. Also: "ClaudeBot is hammering my server with almost a million requests in one day" (5 pts / 1 comment, 2025-09-22).
- **`AI crawler` query: 460 hits total.** Top bandwidth/spoofing threads: "Nepenthes is a tarpit to catch AI web crawlers" (714 pts / 265 comments, 2025-01-16); "Amazon's AI crawler is making my Git server unstable" (607 pts / 246 comments, 2025-01-18); "Devs say AI crawlers dominate traffic, forcing blocks on entire countries" (360 pts / 275 comments, 2025-03-25); "AI crawlers, fetchers are blowing up websites; Meta, OpenAI are worst offenders" (231 pts / 144 comments, 2025-08-21); "It seems like the AI crawlers learned how to solve the Anubis challenges" (177 pts / 148 comments, 2025-08-15) — measured-by-us — `https://hn.algolia.com/api/v1/search?query=AI%20crawler&tags=story&numericFilters=created_at_i%3E1735689600`.
- **r/selfhosted old.reddit search: not run.** This project's Chrome extension is barred to this pull by the task's own instruction (no browser tools this session; the C1 line itself says "via Chrome" for the Reddit half). `unknown — checked, no browser tool available 2026-09-18 (task boundary)`; the HN counts above stand as the visibility-proxy evidence and are explicitly not a demand measurement (F1/F5 — high points on a "my server got hammered" complaint thread is not a willingness-to-pay signal).

---

### 9. A1 — Count of Show HN launches of bot-detection/log-analysis tools 2025–2026 and their points — HN Algolia — `measured-by-us`

- **74 total Show HN hits** for `bot detection` query (`tags=show_hn`) since 2025-01-01. — measured-by-us — HN Algolia API, fetched 2026-09-18 — `https://hn.algolia.com/api/v1/search?query=bot%20detection&tags=show_hn&numericFilters=created_at_i%3E1735689600`.
- **None of the top 10 by relevance is a log-file/access-log analyzer** — the ten returned are anti-detection/evasion tools (Mousecrack, Pydoll, Instagram auto-poster bypass), human-vs-bot games, and a behavioral API (HUMA), plus one unrelated high-scorer (Libretto, 134 pts, AI browser automation determinism — not a bot-detection launch by subject). Highest points among genuine bot-detection Show HNs found here: 7 (Mousecrack, 2026-07-30).
- Cross-referenced against the earlier Wave 2b Cloudflare-analytics pull: **"Show HN: CountermarkAI – Protect your website from AI Bots" — 7 pts, 0 comments, 2025-06-14** — same HN Algolia data source, surfaced under the `GPTBot`/`ClaudeBot` queries above rather than the `bot detection` Show HN query.

Show HN launches in this exact category (bot-detection/log-analysis) score low across the board — no launch found above single-digit points except the one unrelated hit. This is consistent with S9/§5 of `review.md`: low organic traction for tools in this slot even at launch.

---

### 10. A9 — Web Bot Auth adopters: any AI operator named as signing requests (OpenAI, Anthropic, Perplexity docs; Cloudflare blog 2026) — `vendor-reported`; shelf-life of the whole method

- **Cloudflare's own Web Bot Auth spec page names no adopting AI operator** — vendor-reported — already on file, `projects/ai-ads-injection/raw/wave2b-detection-shelf-life.md` §1, pulled 2026-09-17: "Searched and NOT found anywhere in this document: `OpenAI`, `ChatGPT`, `Perplexity`, `Anthropic`." Not re-fetched this pull; the negative finding is a page-content fact unlikely to change day-to-day and the method line (exact strings searched) is already recorded.
- **OpenAI's `ChatGPT agent` product (not GPTBot/OAI-SearchBot the crawlers) is signed and Cloudflare-classified as a "signed agent."** — vendor-reported — Cloudflare Blog, published 2025-08-28 — `https://blog.cloudflare.com/signed-agents/` — direct-fetched 2026-09-18. "...and will be classifying as signed agents: ChatGPT agent, Goose from Block, ..." with a Radar traffic panel "for ChatGPT agent... from August 21, 2025 to August 27, 2025."
- **A 2026-09-03 secondary source restates and updates this:** "OpenAI signs ChatGPT agent and agentic requests using the Web Bot Auth protocol" and "In June 2026, Google started using Web Bot Auth to identify its bots and crawlers using cryptographic signatures," while explicitly stating Anthropic and Perplexity have **not** documented Web Bot Auth support. — vendor-reported (article paraphrasing vendor claims) — CHEQ blog, published 2026-09-03 — `https://cheq.ai/blog/web-bot-auth-solves-identity-but-is-that-enough/`.
- **Unconfirmed claim, not used:** several secondary blogs (search snippets only; not independently fetched to a primary page) assert "GPTBot enabled signed requests by default on May 28, 2026" and that Cloudflare shipped a "Verified AI Agent" bot-management category on 2026-06-02 tied to a "W3C Web Bot Auth specification finalized in May 2026." `unknown — checked blog.cloudflare.com/verified-bots-with-cryptography/ (dated 2025-07-01, no operator-specific text found on direct fetch) 2026-09-18` — this specific date/default-on claim could not be traced to a primary Cloudflare or OpenAI page this pull and is not treated as established.

**Shelf-life read, stated once:** the signed-agent path is live for OpenAI's *agentic* product (ChatGPT agent, since 2025-08-28) and reportedly for Google's crawlers (June 2026, unconfirmed primary), but **not** for the three crawlers `aicrawlcheck` actually classifies against IP ranges — GPTBot/OAI-SearchBot, ClaudeBot, PerplexityBot — as of the most recent primary-sourced check (Cloudflare's own Web Bot Auth doc, 2026-09-17, names none of them). IP-range matching's remaining shelf life looks longer than a naive "Web Bot Auth is shipping" headline would suggest, because it hasn't reached the training/search crawlers this tool targets.

---

### 11. A10 — A published real-world spoof rate for AI-crawler identities (Cloudflare Radar bot report 2026, Known Agents Agentic Web Index "Spoofing & Security", Akamai) — `vendor-reported`; the comparison for the n=1 real log

Three figures found, side by side, **not averaged** — they measure different things, different periods, different methods:

- **"31% of all traffic identifying as GPTBot was actually unrelated scraping infrastructure spoofing the user agent"** — attributed to "Cloudflare's May 2026 Radar report" — vendor-reported, secondary-sourced (multiple blogs cite this figure; the primary Cloudflare Radar report/blog post itself was searched for but not located at a fetchable URL this pull) — checked via WebSearch 2026-09-18, e.g. `pravinkumar.co/blog/cloudflare-ai-crawler-verification-june-2026-webflow-seo-2026`. Treat as `vendor-reported, primary URL not confirmed`.
- **"Spoofed requests make up 5.7% of all traffic labeled as coming from AI crawlers," average spoof ratio 1:17, over a two-week period across 16 named AI crawlers/scrapers** — vendor-reported — HUMAN Security, Satori Threat Intelligence — `https://www.humansecurity.com/learn/blog/ai-crawler-spoofing-chatgpt-mistral-perplexity/` — direct fetch returned **HTTP 403**; figure taken from WebSearch's snippet of the same page, checked 2026-09-18. Not independently verified against the page itself.
- **Already on file, same category:** Known Agents' Agentic Web Index (`projects/ai-ads-injection/raw/wave2b-crawler-analytics-competitors.md` §1e, pulled 2026-09-17) defines spoofing as failing "verified IP or HTTP message signature," and its "Spoofing & Security" section names `Amazonbot — AI Data Scraper — 17.1% — Agents blocked by the most top websites" as the top blocked-agent figure — a *blocked-rate*, not a spoof-rate, and not directly comparable to the two figures above.
- **Comparison for the project's own n=1 real log: not run this pull.** No real log was located (see line 12) so there is nothing to compare the 31%/5.7%/17.1% figures against.

**The three published figures disagree by more than 5x (31% vs 5.7%) and measure different populations (GPTBot-only vs. 16-crawler average vs. one operator's blocked-rate).** This is exactly the F11 trap (averaging conflicting figures) — recorded side by side, neither adopted as "the" rate.

---

### 12. A10 — One real, recent (2025–2026) public access log containing AI-crawler UAs (Kaggle "web server access logs", university/CDN datasets, any GitHub-hosted anonymised log) — run `aicrawlcheck scan` on it, paste output — `measured-by-us`; if none found, `unknown — checked <sources>`

**`unknown — checked the following, 2026-09-18` (no real log with confirmed 2025–2026 AI-crawler UAs found and fetchable without authentication):**

- Kaggle `eliasdabbas/web-server-access-logs` — surfaced by search, described as 3.3 GB of logs from an Iranian e-commerce site (`zanbil.ir`); no date/AI-crawler-UA confirmation found, and Kaggle datasets require an authenticated API/browser download this sandbox does not have. Query: `Kaggle web server access log dataset AI crawler bot 2026`.
- GitHub code/raw-file search for a standalone real access-log sample containing `GPTBot`/`ClaudeBot`/`PerplexityBot` — surfaced only *tooling* repos (log analyzers, cost calculators) that operate on a user's own log, not a published sample log with real AI-crawler hits. Query: `"access.log" OR "access_log" github sample dataset "GPTBot" OR "ClaudeBot" OR "PerplexityBot" raw file real`.
- SecRepo / Awesome-Cybersecurity-Datasets / vizsec.org data catalogs — surfaced only pre-2020 or non-web-log security datasets (CSIC 2010 HTTP dataset, LANL, Charles University SIS log 2018, MIT static log directory) — none post-dates the emergence of GPTBot/ClaudeBot/PerplexityBot (2023+) and none was checked for AI-crawler UAs specifically since the dates alone rule them out. Query: `secrepo public security datasets web server logs 2026`.

**No `aicrawlcheck scan` was run against a real log this pull.** This is the same gap `review.md` calls the single highest-leverage fix ("run it on one real production log... ~3 hours, highest value per hour by a wide margin") and it remains open. A real log requires either a `requires-human`-supplied file from an actual site operator, or continued search beyond this pull's budget.

---

### 13. A6 — Amazonbot IP-range file: URL, prefix count, `creationTime` — developer.amazon.com/amazonbot/ip-addresses — `vendor-reported` (closes review S2)

- **URL:** `https://developer.amazon.com/amazonbot/ip-addresses` — HTTP 200, fetched via direct `curl` 2026-09-18 (not WebFetch, to get an exact count instead of a model-summarized one).
- **`creationTime`: `2026-09-08T05:24:10.610952+00:00`** — quoted verbatim from the JSON.
- **Prefix count: 1,292 `ipv4Prefix` entries, 0 `ipv6Prefix` entries** — measured-by-us, direct `curl` + `grep -c` on the raw response body, 2026-09-18. Each entry is a single IPv4 address (no CIDR suffix present in the field, e.g. `"ipv4Prefix": "3.81.245.78"`), so this is 1,292 individual addresses, not aggregated ranges.
- **This directly resolves review.md finding S2.** `docs/explore/detection-surface.md:19` had this as "vendor states published, not re-fetched this pass"; it is now fetched, with an exact count and date, closing the gap the page's own text ("No published range file for those was located") got wrong.

---

### 14. A4 — Prices of paid bot-management: Cloudflare Bot Management entry price, DataDome starting tier, HUMAN, Known Agents — vendor pricing pages — `vendor-reported`

- **Known Agents** — see line 3 above: $0 / $29 / $299 / custom, vendor's own pricing page, re-verified 2026-09-18.
- **Cloudflare Bot Management: no published self-serve entry price.** — vendor-reported/analyst-derived (mixed) — `https://www.cloudflare.com/plans/bot-management/` returned **HTTP 403** on direct WebFetch 2026-09-18. Secondary sources (not Cloudflare's own page) report it as "a quote-only Enterprise add-on," with one estimate of "$250–500/month" as an add-on to a Business plan ($200–250/mo) and Enterprise API-heavy contracts "typically start around $5,000/month, though Cloudflare does not confirm this publicly" — analyst-derived, secondary, checked via WebSearch `Cloudflare Bot Management pricing entry price 2026` 2026-09-18. Cloudflare itself discloses no number.
- **DataDome: no published self-serve price on DataDome's own site; secondary aggregators report Essentials $3,830/mo, Advanced $8,670/mo, Premium $10,160/mo, Enterprise Plus custom** — analyst-derived, secondary (cside.com blog and similar pricing-aggregator sites, not datadome.com itself, which does not publish prices) — checked via WebSearch `DataDome pricing starting tier 2026` 2026-09-18.
- **HUMAN Security: sales-led, no published price at all** — company-stated (absence) — checked via WebSearch `HUMAN Security bot defense pricing 2026` 2026-09-18: "HUMAN Security uses a sales-led, custom-quote model with no pricing published on its website as of 2026."

Pattern across all three paid incumbents: **none publishes a self-serve entry price.** Only the free tier (Known Agents $0) is an actual, vendor-published number; every other figure in this line is a third party's estimate of an enterprise sales quote, not a price a buyer could act on today.

---

### 15. A8 — Search interest: relative Google Trends for "GPTBot", "verify googlebot", "AI crawler block" 2024–2026 — trends.google.com via Chrome — `analyst-derived` (weak, label it)

**`unknown — checked trends.google.com, no Chrome/browser tool available this session (task boundary; the line itself specifies "via Chrome") 2026-09-18.`** A WebSearch substitute (`Google Trends "GPTBot" "verify googlebot" search interest 2026`) returned no Trends numbers, only unrelated secondary statistics (a HUMAN-Security-sourced "5.7%" figure, already captured under line 11, surfaced again here by the search engine). Google Trends' `trends.google.com/trends/explore` endpoint requires a JS-rendered session and is not fetchable via plain HTTP `curl` or `WebFetch` (confirmed: the tool is excluded by task instruction, not merely untried).

---

### 16. A9 — Time-to-copy: LOC of `prototype/aicrawlcheck/*.py` and hours estimate for an incumbent engineer — count locally — `measured-by-us` + `own judgement`

- **1,640 lines** across the 9 `.py` files in `prototype/aicrawlcheck/` — measured-by-us — local `wc -l`, 2026-09-18, `projects/ai-ads-injection/prototype/aicrawlcheck/*.py`. Breakdown: `report.py` 346, `ranges.py` 285, `logparse.py` 312, `cli.py` 239, `engines.py` 158, `verify.py` 185, `rdns.py` 85, `__main__.py` 25, `__init__.py` 5.
- (For reference, not part of this line: the whole `prototype/` tree, including tests and the browser demo bundle, is 2,009 lines total — local `wc -l`, 2026-09-18.)
- **Hours estimate for an incumbent engineer to copy the differentiating piece (retroactive log-file classification against published IP ranges): own judgement, 1–2 days (8–16 hours).** Reasoning: the core mechanism is (a) a log-format parser [`logparse.py`, 312 lines, itself buggy per `review.md` S4], (b) `ipaddress`-module containment against JSON range files already published by each vendor [`ranges.py`, 285 lines], and (c) a decision table [`verify.py`, 185 lines]. An engineer at Cloudflare or Known Agents already owns the range-file ingestion and the UA-classification registry (both companies publish or consume these already); the only net-new work for them is a "read an existing log file" code path, which `review.md` §5 itself calls "one afternoon of work for either incumbent" — own judgement, consistent with that file's independent estimate, not just copied from it.

---

### 17. **A3 KILL** — Deposits from the pre-registered 20-organisation probe (15.000.000 VND, 50% deposit, day 7) — `requires-human`; not yet run

requires-human — not pulled

---

### 18. A3 — Unprompted requests for the tool after a published post on the rDNS finding, counted at day 14 — `requires-human` to publish, `measured-by-us` to count

**`unknown — checked projects/ai-ads-injection/STATE.md (full), docs/outcome/*.md, docs/execution/*.md, site/ 2026-09-18`.** No entry in `STATE.md` records the rDNS finding ("OpenAI's crawler addresses have no PTR record at all, so Google's documented verification procedure does not transfer") as having been published anywhere. `docs/outcome/review.md`'s closing section explicitly names this as "the cheapest remaining experiment... the one this project has never made," phrased as a recommendation, not a completed action. STATE.md's last entries (2026-09-17 vision agent, 2026-09-18 wave-10 fix agent stopped mid-run) record no publish event. **The precondition (`requires-human` to publish) has not occurred, so the count this line asks for does not exist yet** — this is not the same as a count of zero; it is "not yet measurable."

---

### 19. A8 — Vietnamese GEO agencies not yet re-fetched (Hashmeta VN, Nextop, seo.danang.vn, Fast Marketing): do any sell measurement rather than optimisation; price — agency pages — `vendor-reported`

All four were confirmed as `unknown — checked 2026-09-17, not pulled` in `projects/ai-ads-injection/raw/wave2b-vn-agency-audit-and-free-tools.md:129`. Re-fetched this pull, direct `curl`/WebFetch, 2026-09-18:

- **Hashmeta Vietnam — the one agency selling something branded as measurement, not just optimisation.** — vendor-reported — `https://hashmeta.com/vn` + `https://hashmeta.com/vn/pricing/`, fetched 2026-09-18. "GEO Premium" package: **60.000.000đ+/tháng** (60+ million VND/month, bundles optimisation and measurement). Separately, the page advertises a standalone **"AI Visibility Audit" priced at "trị giá 15.000.000đ"** (valued at 15 million VND) — offered as a free lead-magnet audit ("Đánh giá hiện diện AI" / "assessment of AI presence"), not evidence of anyone having paid 15tr for it. This is the first agency found in this project, across two waves, to name "AI-Visibility" as a distinct line item from SEO/GEO optimisation.
- **Nextop Digital Agency — no distinct price, no distinct measurement product.** — vendor-reported — `https://nextop.agency/cong-ty-geo-agency/`, fetched 2026-09-18. GEO is sold folded into general strategy ("Kết hợp SEO nền tảng và GEO" / "combining foundational SEO and GEO"); "Theo dõi và đánh giá AI visibility" (tracking and evaluating AI visibility) is mentioned only as a feature inside the bundle, not sold separately, and no VND figure is published — quote-only via direct contact.
- **`seo.danang.vn` is not a GEO/AI-visibility agency at all.** — vendor-reported — `https://seo.danang.vn/`, fetched 2026-09-18. The site (branded "SEOViP," title "Dịch Vụ SEO Đà Nẵng #1 UY TÍN") sells general SEO only: "các dự án SEO tổng thể của chúng tôi thường có mức đầu tư khởi điểm từ **80.000.000 VNĐ/dự án** (thực hiện trong 6-12 tháng)" (SEO projects typically start from 80,000,000 VND/project, over 6–12 months). No GEO, AEO, or AI-visibility service found anywhere on the page — `not found in {seo.danang.vn homepage} — checked 2026-09-18`. This may be the wrong URL for whichever "seo.danang.vn"-branded GEO seller the original wave-1 list intended; as fetched, it is a generic Da Nang SEO shop.
- **Fast Marketing — already on file, re-verify not needed for price (see caveat).** `projects/ai-ads-injection/raw/vietnam-ai-visibility-demand.md` (pulled 2026-09-17) has FAST Silver 32.000.000đ/tháng, FAST Gold 45.000.000đ/tháng, FAST Diamond 65.000.000đ/tháng, all optimisation-framed ("Đưa Thương Hiệu Bạn Vào AI Overview, Chat GPT, Gemini" — optimisation language, no measurement/audit line item). Not re-fetched this pull (vendor page unchanged in 24 hours is the working assumption; not independently confirmed — `unknown — not re-fetched 2026-09-18`, flagged per the re-verify-vendor-stated rule rather than silently reused).

**Net finding for this line:** of the four, only **Hashmeta** sells anything nameable as "measurement" (its "AI-Visibility Audit"), and it is a free lead-magnet, not a paid line item with a confirmed buyer — no different in kind from the free incumbents already killing every other asset argument in this project (F2).

---

## Not found

- GoAccess/AWStats/Matomo crawler-IP-verification feature (line 1, 2) — confirmed absent, not merely unsearched.
- Cloudflare AI Crawl Control historical-log-import feature (line 4) — confirmed absent as of 2026-09-18.
- A real 2025–2026 public access log with confirmed AI-crawler UAs, fetchable without authentication (line 12).
- A primary-sourced (not third-party-blog-cited) Cloudflare Radar page stating the "31% of GPTBot traffic is spoofed" figure (line 11).
- Confirmation that GPTBot itself (the crawler, not ChatGPT agent) signs requests via Web Bot Auth, from a primary source (line 10).
- Top-1,000,000-website Cloudflare share, separate from the all-websites figure (line 5).
- Google Trends relative interest for the three named queries (line 15) — tool unavailable this session by task boundary.
- The correct live page for whichever "seo.danang.vn"-branded GEO seller the original list intended (line 19) — the domain as given is a general SEO shop with no GEO/AI-visibility offering.

## Already on file (cited, not re-pulled in full)

- `projects/ai-ads-injection/raw/wave2b-crawler-analytics-competitors.md` → Known Agents full product/pricing/Agentic-Web-Index text (2026-09-17; re-verified pricing only, line 3).
- `projects/ai-ads-injection/raw/wave2b-detection-shelf-life.md` → Web Bot Auth mechanism, IETF draft, OpenAI docs still IP-range-only (2026-09-17; used as-is for line 10's negative finding).
- `projects/ai-ads-injection/raw/vietnam-ai-visibility-demand.md` → Fast Marketing, SEODO, Midas, TopOnSeek VND pricing (2026-09-17; Fast Marketing reused for line 19, flagged not re-verified).
- `projects/ai-ads-injection/raw/wave2b-vn-agency-audit-and-free-tools.md:129` → confirms the four agencies in line 19 were previously unpulled, justifying this pull.
- `projects/ai-ads-injection/docs/explore/detection-surface.md:19` → the Amazonbot "not re-fetched" gap that line 13 closes.
- `projects/ai-ads-injection/docs/outcome/review.md` → S2 (Amazonbot), the "run on a real log" recommendation (line 12), and the "publish the rDNS finding" recommendation (line 18), all cross-referenced above.
- `projects/ai-ads-injection/docs/plan/re-pick.md` → context only (probe design, MoR findings); no C1 line drew a number from it directly.

## Counts

- **Lines pulled (answer found, positive or negative): 15** — lines 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 16, 19, and 11 (11 pulled as three conflicting figures, none confirmed primary — counted as pulled-with-caveat).
- **Lines `unknown`: 3** — line 12 (no real log located), line 15 (Google Trends, tool unavailable), line 18 (precondition — publication — not yet met).
- **Lines `requires-human`: 1** — line 17.
- **Total C1 lines: 19.** 15 + 3 + 1 = 19.

## Caveats

- No Chrome/browser tool was used anywhere in this pull, per task instruction; two lines (8's Reddit half, 15) are explicitly weaker or `unknown` because of it.
- Several WebFetch calls return a small model's *summary* of a fetched page rather than the raw text; where a number mattered (Amazonbot prefix count, line 13) this pull switched to direct `curl` + `grep` for an exact count instead of trusting the summarizer — the two WebFetch attempts at the same page returned 1,072 and 1,040 respectively, both wrong against the `curl`-measured 1,292; that discrepancy is recorded, not hidden, and no other line's WebFetch-derived number was cross-checked this way.
- Cloudflare's own pricing and Radar-report pages 403'd or otherwise resisted direct fetch multiple times this pull (Bot Management pricing, radar.cloudflare.com/reports/bots-2026); every number attributed to Cloudflare on those topics in this file is secondary-sourced and labelled as such.
- "Re-verify vendor-stated" was applied where a C1 line named a specific number to re-check (Known Agents pricing, Cloudflare AI Crawl Control changelog, Cloudflare/W3Techs live pages, Amazonbot file); it was not applied to every vendor-stated number in every already-on-file raw file cited for context (e.g., Fast Marketing's VND prices, reused from the 2026-09-17 pull) — those are flagged individually as not re-verified rather than silently presented as fresh.
- This file produces evidence only. No verdict, no PASS/FAIL judgement against §A thresholds — that is Stage 3's job per `FRAMEWORK.md` §D.
