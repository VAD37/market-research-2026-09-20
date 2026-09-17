# Carrier state — what pass 2 settled, what it left open, what this pass changed

2026-09-17. Reads `../../../../docs/findings/injection-feasibility.md` and its raw file `../../../../docs/raw/injection-feasibility-pulls.md` (pass 2, 2026-09-16), plus `../../../../docs/raw/tos-browser-pulls.md` and the market/roster files. Do not re-read those files for the plan step — this is the digest. New measurement from this pass is in `raw/` and cross-referenced below.

## Settled by pass 2 — do not re-litigate

**Sub-question 1, Detection: yes.** "Yes. By IP range or forward-confirmed reverse DNS. Never by user-agent alone." Every operator except ByteDance publishes a user-agent string; OpenAI, Anthropic, Perplexity, Amazon and Common Crawl publish IP-range files. OAI-AdsBot exists as a distinct, separately observable ads-verification crawler whose data "is not used to train generative AI foundation models."

**The declared/actual gap is real and documented, not theoretical.** Cloudflare's Aug-2025 test: Perplexity answered questions about robots.txt-disallowed domains using an undeclared crawler impersonating Chrome on macOS, from IPs outside its published range, rotating IPs and ASNs to evade blocks — 3-6M daily undeclared requests vs 20-25M declared. Control: "ChatGPT-User fetched the robots file and stopped crawling when it was disallowed."

**Sub-question 2 (this project's "Delivery"), edge/CDN capability: pass 2 did not cover this at all.** Pass 2's four questions were detection, live-vs-index, measurement methodology, and policy — the CDN/edge-control mechanics (what a Worker vs a WAF rule vs a Transform Rule actually exposes) are new ground, covered for the first time in `docs/explore/edge-controls.md` this pass. Not a gap in pass 2 — outside its scope.

**Live retrieval vs index (part of sub-question 1): mixed, engine by engine.** Claude web search is confirmed live per-query, company-stated, $10/1,000 searches, citations on every response. Google AI Mode does confirmed live sub-searches via query fan-out but Google's own text "does not spell out the live/index distinction." Google AI Overviews needs only ordinary Search index/snippet eligibility — no separate technical bar. Perplexity and ChatGPT search/Copilot pipeline mechanics were **not settled** (see Open, below).

**Policy ceiling, partially settled.** Google's spam policy (fetched, `Last Updated: 2026-08-28`) names "attempting to manipulate generative AI responses in Google Search" as spam, on par with ranking manipulation, and defines cloaking as "presenting different content to users and search engines with the intent to manipulate search rankings and mislead users" — naming as an example "inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor." Consumer ToS for OpenAI and Perplexity were read via browser (`tos-browser-pulls.md`): OpenAI bars "automatically or programmatically extract data or Output"; Perplexity bars both automated and manual "monitor, extract, copy or collect information," restricts use to "personal, non-commercial" purposes, and bars commercial exploitation outright. Both engines carve unauthorized-use/injunctive relief out of arbitration, meaning enforcement runs through court.

**The reusable measurement method exists and is published**, independent of any specific attack payload: build a real content/query dataset, measure baseline model behavior with no intervention, apply a controlled intervention, test transfer from lab harness to a live production engine. Pfrommer et al. (EMNLP 2024) named their transfer target explicitly: "perplexity.ai's Sonar Large Online."

## Left open by pass 2 — quoted verbatim

These are pass 2's own words, not paraphrase, pulled from its caveats section and inline "unknown" markers in `injection-feasibility.md` and `tos-browser-pulls.md`:

1. **"Anthropic's combined IP list (20 prefixes, no per-bot labels) came via search relay; the JSON was not fetched directly."** — **Resolved this pass.** Direct fetch of `https://claude.com/crawling/bots.json` (2026-09-17) returns **26 prefixes**, `creationTime: 2026-08-18T23:56:36Z`. Pass 2's 20 was a relayed, unverified count. Use 26 going forward; see `raw/crawler-ip-ranges-2026-09-17.md`.

2. **"Azure attribution of OpenAI's prefixes is inferred from the ranges, not confirmed by WHOIS or ASN lookup."** — **Resolved this pass.** ASN lookup (ip-api.com) on sampled GPTBot/SearchBot/AdsBot IPs returns `AS8075 Microsoft Corporation / MICROSOFT-CORP-MSN-AS-BLOCK` on every sample, org field reading `Microsoft Azure Cloud (<region>)`. See `raw/asn-lookups.txt`.

3. **"Cloudflare's removal of Perplexity from its verified-bots program is carried from pass 1, not re-quoted verbatim."** — **Still open.** Not re-verified this pass either; would need a fresh Cloudflare verified-bots-list fetch, not attempted (list membership, not a policy page — low priority, cheap to close later).

4. **"Cloudflare Radar's own pages returned HTTP 403; crawl-share figures come from a third party's reading of Radar."** — **Still open.** Not reattempted this pass.

5. **"Fastly's report was relayed by search summary, never fetched."** — **Still open** for the specific bot-traffic report pass 2 cited (mid-Apr to mid-Jul 2025, "AI crawlers ~80% of AI bot traffic; Meta over half"). This pass fetched *different* Fastly pages (bot-management product, VCL docs) for the edge-controls question, not this traffic report.

6. **"The GEO paper's effect size appears as ~22%/~37% and as 'approximately 40%' in the same pull. Both on file."** — **Still open, unreconciled.** Not re-examined this pass; not directly relevant to detection/delivery/policy terrain.

7. **"Amazon v. Perplexity is entirely secondary-sourced; no filing read."** — **Still open.** Not pursued this pass — it is platform-vs-crawler scraping litigation, not answer-manipulation precedent, and stays a lower-priority thread per pass 2's own read.

8. **"Bytespider's lack of documentation is a search-level negative, not proof none exists."** — **Still open.** Not re-checked this pass (would need WebSearch, which returned "unavailable" when tried for an unrelated query today — see below).

9. From `tos-browser-pulls.md`: **"`unknown — checked 2026-09-16`: the OpenAI Services Agreement / Business Terms were not fetched this pass. Section 1 points to them and they control for API customers. Fetch before relying on this block."** — **Still open. This is the single highest-value open item for the plan phase.** The whole "API path is not closed" conclusion in pass 2 rests on OpenAI's *Service Terms* page (fetched, only says "use APIs in accordance with the applicable documentation"), not on the Business Terms/Services Agreement that Section 1 itself says "will control" in a conflict. Not fetched by pass 2, not fetched this pass either (attempted `openai.com/policies/ads-terms/` for a different reason and got 403 — the Business/Services Agreement URL itself was never even attempted).

10. From `tos-browser-pulls.md`: **"`unknown — checked 2026-09-16`: the Perplexity API Terms of Service at https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service was not fetched. It controls the API path, which is the route that matters. Next pull."** — **Still open, second-highest-value item.** Same structural gap: pass 2's "API path is not closed by these documents" reads Perplexity's *consumer* ToS explicitly disclaiming API coverage, then stops. The document that actually governs API use was never read, by pass 2 or by this pass.

11. From `tos-browser-pulls.md`: **"`unknown — checked 2026-09-16`: the page truncated at 50,000 of 56,200 characters. Sections after 'Shopping with Perplexity Pro' were not read."** on Perplexity's consumer ToS. — **Still open.**

12. From `injection-feasibility.md`: **"Correction to pass 1... The date is not [confirmed]... Treat as `unknown — checked developers.google.com 2026-09-16`."** on the 2026-05-15 effective date for Google's AI-answer-manipulation spam wording. — **Still open**, not re-checked this pass.

13. From `injection-feasibility.md` Question 2 table: **"ChatGPT search, Copilot — No engineering documentation located — unknown — checked 2026-09-16."** — **Still open.** Not pursued this pass.

14. From `injection-feasibility.md` Question 2: **"Perplexity — Third parties describe a six-stage RAG with 'fresh web retrieval' per query — Unverified — vendor page returned HTTP 403."** — **Still open.** Consistent with this pass's own experience: Perplexity/OpenAI documentation and ToS pages 403 to automated fetch across the board; only a browser (used once by the main thread in pass 2, not available to this agent by default) got through.

## What this pass adds beyond resolving pass 2's own list

- **rDNS convention, tested, not just documented.** Pass 2 recorded Google's forward-confirmed-rDNS *procedure* as vendor-documented but never tested whether OpenAI/Anthropic/Perplexity IPs actually resolve to anything. They mostly do not: sampled OpenAI IPs (GPTBot, SearchBot, AdsBot ranges) returned **zero PTR records** against 8.8.8.8; sampled Anthropic and Perplexity IPs resolved to **generic cloud-vendor hostnames** (`*.bc.googleusercontent.com`, `ec2-*.compute-1.amazonaws.com`) with no bot-specific or company-branded string. Only Google (`crawl-*.googlebot.com`) and Common Crawl (`*.crawl.commoncrawl.org`) have a vanity rDNS convention that supports forward-confirmation. **Practical read: for OpenAI, Anthropic and Perplexity, IP-range-list matching is the only detection method — rDNS is a Google/Common-Crawl-only technique, not general.** See `docs/explore/detection-surface.md` and `raw/rdns-lookups.txt`.
- **Edge-control mechanics, previously untouched.** See `docs/explore/edge-controls.md` — Workers can branch full response body on UA/IP/ASN/bot-score; WAF custom rules cannot (block/challenge/skip/log only); Transform Rules cannot touch the body at all. Cloudflare's Pay per crawl is still private beta as of the 2026-08-14 page stamp, 14+ months after its 2025-07-01 launch.
- **Ad-disclosure law, previously absent.** Pass 2 had only Google's own cloaking definition. This pass adds the FTC Endorsement Guides (no AI mention as of the current text), EU DSA Article 26 (advertising-transparency duty attaches to the platform showing the ad — unclear it reaches an AI answer echoing page content), and UCPD Annex I item 11, the EU's "advertorial" per-se-unfair practice, quoted verbatim via a UK statutory instrument. See `docs/explore/policy-ceiling.md`.

## What is newly open, introduced by this pass's own gaps

- Vietnam's Law on Advertising (16/2012/QH13) — not reached. Four URL attempts (404/403/timeout/wrong-document) plus one WebSearch call returning "Web search error: unavailable." `unknown — checked luatvietnam, vanbanphapluat, thuvienphapluat, WIPOLex, WebSearch 2026-09-17.`
- Bing/Microsoft Copilot cloaking policy and OpenAI's Ads Terms (sponsored-content disclosure rule) — both pages are either JS-rendered shells (Bing) or 403 to automated fetch (OpenAI), same pattern pass 2 hit before falling back to a browser. Not resolved this pass; this agent did not use browser tooling.
- WebSearch: one test query today ("Vietnam Law on Advertising 16/2012/QH13...") returned "Web search error: unavailable," not a quota-remaining message — consistent with the 2026-09-16 200/200 exhaustion not having reset by 2026-09-17. Budget accordingly; direct fetch worked for the large majority of this pass's pulls.

## Read for the plan phase

The technical answer to "can you detect it" (yes, mostly by IP list, not rDNS, for the three engines that matter) and "can you branch on it at the edge" (yes, but only with a Worker, not a WAF/Transform rule) are both now closed enough to design against. The two open items that actually gate a real build are contractual, not technical: **OpenAI's Business Terms/Services Agreement and Perplexity's API Terms of Service have never been read, by any pass.** Everything pass 2 concluded about "the API path is not closed" is provisional on documents nobody has opened yet.
