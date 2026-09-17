# Policy and edge-control pulls — explore phase

Pull date: 2026-09-17. Method noted per block: WebFetch (Claude's fetch-and-summarize tool, HTML->markdown->small-model read) or curl (raw HTTP, this session's Bash tool). WebFetch summaries are model-generated reads of the fetched page, not our own verbatim transcription — treated as vendor-reported via WebFetch, not as directly-quoted raw text, except where the WebFetch output itself contains a quoted string (kept in quotes below). Where curl pulled raw HTML, grep excerpts are copied verbatim.

---

## Cloudflare — bot score field (cf.client.bot / bot_management.score)

Source: https://developers.cloudflare.com/bots/concepts/bot-score/ — vendor-reported — WebFetch 2026-09-17

Score range 1-99: "a score of 1 means Cloudflare is quite certain the request was automated, while a score of 99 means Cloudflare is quite certain the request came from a human." Groupings: Automated=1, Likely automated=2-29, Likely human=30-99, plus a separate "Verified bot" category described as "non-malicious automated traffic (used to power search engines and other applications)." No cf.client.bot field name found on this page (that name is legacy/deprecated per cross-reference below).

## Cloudflare — bot management variable names (authoritative field list)

Source: https://developers.cloudflare.com/bots/reference/bot-management-variables/ — vendor-reported — WebFetch 2026-09-17

Fields, as reported by the fetch:
- `cf.bot_management.score` — integer 1-99, Cloudflare's certainty a request is a bot.
- `cf.bot_management.verified_bot` — boolean, "whether a request originates from a Cloudflare allowed bot."
- `cf.bot_management.static_resource` — flags static file requests.
- `cf.bot_management.ja3_hash`, `cf.bot_management.ja4` — TLS/client fingerprint hashes.
- `cf.bot_management.detection_ids` — list of heuristic detection IDs that fired.
- `cf.bot_management.tags` — bot tag list.
- `cf.bot_management.signed_agent` — boolean for cryptographically self-identifying agents (i.e. Web Bot Auth signers).
- `cf.bot_management.corporate_proxy` — boolean.

"Cloudflare maintains a large allowlist of good, automated bots (such as Google Search Engine and Pingdom) that perform beneficial tasks." Verification stated as via reverse DNS validation and other undisclosed methods.

Workers access path: `request.cf.botManagement.score` (JS object property, not the WAF-expression dotted name).

Example WAF expression quoted by the fetch:
```
not cf.bot_management.verified_bot
and not cf.bot_management.static_resource
and not cf.bot_management.corporate_proxy
and cf.bot_management.score lt 30
```
This is a block-suspicious-non-verified-traffic rule — it is not, itself, evidence of a serve-different-content rule; that direction (verified_bot == true -> branch content) is the same primitive used inverted, not separately documented on this page.

## Cloudflare — bot solutions overview / plan tiers

Source: https://developers.cloudflare.com/bots/ — vendor-reported — WebFetch 2026-09-17

Three tiers: Bot Fight Mode (Free, domain-wide single toggle, challenge only), Super Bot Fight Mode (Pro/Business/Enterprise, "configurable actions per bot category," no per-request score), Bot Management (Enterprise only, "per-request bot scores, custom rules, per-endpoint handling"). Per-request `cf.bot_management.score` and `verified_bot` used in a Worker or WAF custom rule is an **Enterprise-plan feature**, not free-tier, per this page's tier breakdown — cross-check against AI Crawl Control's "zero-config on all plans" claim (below): the free/zero-config surface is monitoring/allow-block: the fine-grained score-based branching is not confirmed to be on the free plan.

## Cloudflare — WAF custom rules: actions available

Source: https://developers.cloudflare.com/waf/custom-rules/ — vendor-reported — WebFetch 2026-09-17

Action list as reported: Block, Managed Challenge, Skip (bypass other CF security features), Log (Enterprise only). **No "serve alternate content" or "rewrite response body" action is listed for WAF custom rules.** A WAF custom rule alone cannot serve variant page text — it can only allow/block/challenge/log the request.

## Cloudflare — Transform Rules: scope and limits

Source: https://developers.cloudflare.com/rules/transform/ — vendor-reported — WebFetch 2026-09-17

Transform Rules modify "URI path, query string, and HTTP headers of requests and responses" only. "The documentation makes no mention of Transform Rules being able to conditionally modify response bodies." **Response-body branching is out of scope for Transform Rules — Workers is the only primitive found that can vary body content on a signal.**

## Cloudflare — AI Crawl Control status, 2026-09-17 re-check

Source: https://developers.cloudflare.com/ai-crawl-control/ — vendor-reported — WebFetch 2026-09-17, page states "Last Updated: August 14, 2026" (same stamp pass 2 saw one month earlier — page has not moved since)

"Pay Per Crawl remains in private beta" — quoted page label: "(private beta)". Fourteen-plus months after the 2025-07-01 private-beta launch pass 2 found, it is still private beta, not GA — a measured-by-us data point on how far this feature is from being a reliable prototype dependency.

AI Crawl Control (the free/monitoring layer, distinct from Pay per crawl) exposes: "Set allow or block rules for individual crawlers", monitoring of crawler activity/request patterns, robots.txt compliance tracking. **No content-differentiation capability is described on this page** — it is visibility and access control (allow/block/monitor), not a serve-variant-content feature.

## Cloudflare — Workers "Conditional response" example (confirms the branching primitive)

Source: https://developers.cloudflare.com/workers/examples/ — vendor-reported — WebFetch 2026-09-17

Page lists an example titled "Conditional response": "Return a response based on the incoming request's URL, HTTP method, User Agent, IP address, ASN or device type." This is vendor-confirmed evidence that a Worker (not a WAF rule, not a Transform Rule) is the primitive that can branch full response content — including body — on User-Agent/IP/ASN. Full script body was not retrieved in this pass (WebFetch returned only the page's example index, not the linked code) — `unknown — checked developers.cloudflare.com 2026-09-17`, get the actual script next pass.

## Cloudflare — Website Terms of Use, AI/bot and cloaking clauses

Source: https://www.cloudflare.com/website-terms/ — company-stated — WebFetch 2026-09-17, "Effective Date: August 1, 2025"

"You may not use automated bots to access, scan, scrape, data mine, copy, or use the materials or content on this website for developing, training, fine-tuning, or otherwise contributing to or improving a machine learning model" — this is Cloudflare's *own marketing site's* anti-scraping/anti-training clause (i.e. protecting cloudflare.com itself), not a customer-facing prohibition on what a Cloudflare *customer* may configure Workers/rules to do for their own domain. **No explicit "cloaking" clause found in this document** — the fetch could not locate language governing what a Cloudflare customer is permitted to serve differently to crawlers vs humans on their own zone. This is the gap: Cloudflare's own product docs describe the primitive (Workers) but neither this ToS page nor the product pages state a policy on differential serving by a customer.

## Fastly — VCL bot-detection reference

Source: https://developer.fastly.com/learning/vcl/detecting-bots/ redirected (308) to https://www.fastly.com/documentation/guides/vcl/detecting-bots — WebFetch 2026-09-17

Redirect target itself returned HTTP 404 on both WebFetch and curl retry. **No live Fastly page on VCL bot detection was reachable this pass** — `unknown — checked fastly.com 2026-09-17`, URL structure likely changed since whatever indexed it.

Source: https://www.fastly.com/documentation/reference/vcl/subroutines/recv/ — vendor-reported — WebFetch 2026-09-17. Page references conditional logic ("Denying requests based on geolocation or ACLs") in `vcl_recv` but the fetched excerpt contained no literal `req.http.User-Agent` code sample and stated no native bot/AI-crawler classification feature at the VCL-primitive level.

## Fastly — Bot Management product page

Source: https://www.fastly.com/products/bot-management — vendor-reported — WebFetch 2026-09-17

"Fastly Bot Management identifies automated traffic ranging from AI crawlers and fetchers, to headless browsers and malicious bots" — explicit AI-crawler awareness, unlike the bare VCL layer. Actions: "selectively block bots, rate-limit suspicious traffic, or allow known automation"; also lists Block, Allow, Rate-limit, "Dynamic Challenges," "Deception," and "AI monetization capabilities" (unspecified — likely Fastly's answer to Cloudflare's pay-per-crawl, not detailed on this page). No pricing disclosed; "request a demo or contact sales." No stated distinction of OpenAI/Anthropic/Perplexity specifically as "good" vs "bad" in the fetched excerpt — contrast Cloudflare's named verified-bot allowlist.

Read for the idea: Fastly's AI-crawler-aware bot detection is an **Enterprise/sales-gated product**, unlike Cloudflare's free-tier `cf.bot_management.verified_bot`-adjacent Bot Fight Mode. Cloudflare is the cheaper starting point for a two-person prototype.

## FTC — Endorsement Guides, applicability to AI

Source: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking — company/agency-stated — WebFetch 2026-09-17

Core disclosure rule, quoted: "if there's a connection between an endorser and the marketer that a significant minority of consumers wouldn't expect and it would affect how they evaluate the endorsement, that connection should be disclosed clearly and conspicuously." And: "The same is usually true if the endorser has been paid or given something of value to tout the product." **No mention of AI-generated recommendations, AI chatbots, or generative-AI answers anywhere in the fetched document** — the Guides (per the fetch, last substantively updated 2023) predate this fact pattern and do not name it. The FTC has not extended the Endorsement Guides text itself to cover paying to influence a chatbot's answer, as of this pull.

## EU — Digital Services Act, Article 26 (advertising transparency)

Source: https://www.eu-digital-services-act.com/Digital_Services_Act_Article_26.html — third-party legal-explainer mirror of the regulation text, cross-checked against a direct eur-lex.europa.eu fetch that returned no renderable body (JS-gated) — WebFetch 2026-09-17

Para 1 requires platforms let recipients identify an ad "that the information is an advertisement," the advertiser's identity, who paid if different, and "meaningful information directly and easily accessible from the advertisement about the main parameters used to determine the recipient" (i.e. targeting-parameter disclosure). Para 2: platforms must let users flag their own content as commercial and ensure others can identify it "in a clear and unambiguous manner." Para 3: no targeted ads built on special-category (sensitive) personal data profiling.

Applicability read: Article 26 binds "online platforms" (defined elsewhere in the DSA — hosting + dissemination-to-public services) showing ads *on the platform itself*. Whether a page you own that an AI assistant reads and repeats counts as "advertising… on its online platform" is not addressed by this article — the DSA's ad-transparency duty attaches to the platform displaying the ad, and it is genuinely unresolved whether an AI answer that echoes injected page content, without the assistant itself calling it an ad, is "advertising" under this framework at all. Flag as open, not settled by this text — `unknown — no DSA guidance found addressing AI-answer-embedded commercial content, checked 2026-09-17`.

## EU/UK — Unfair Commercial Practices, Annex I item 11 ("advertorial")

Source: https://www.legislation.gov.uk/uksi/2008/1277/schedule/1/made — UK statutory instrument implementing EU Directive 2005/29/EC Annex I into domestic law — company/government-stated — curl (raw HTML) 2026-09-17. Direct eur-lex.europa.eu fetch of the Directive text itself returned no renderable body this pass (JS-gated) — this UK SI is used as a verified verbatim proxy for the Directive's Annex I list, which the SI implements without material alteration per its own heading "Commercial practices which are in all circumstances considered unfair."

Item 11, verbatim: **"Using editorial content in the media to promote a product where a trader has paid for the promotion without making that clear in the content or by images or sounds clearly identifiable by the consumer (advertorial)."**

This is the item on point for the idea: injecting paid product-placement text into a page an AI assistant reads and repeats as if it were the page's own editorial content, without clear disclosure, matches this "in all circumstances unfair" practice's description structurally (paid promotion dressed as ordinary content) even though the enumerated example is print/broadcast media, not an AI-answer pipeline. No EU/UK enforcement action applying item 11 specifically to AI-answer content was found or searched for this pass — untested application, not a settled reading.

## Vietnam — Law on Advertising: not reached

Attempted: https://english.luatvietnam.vn/law-no-16-2012-qh13-... (404, wrong slug), https://vanbanphapluat.co/... (connection timeout), https://thuvienphapluat.vn/... (HTTP 403), https://www.wipo.int/wipolex/en/legislation/details/10145 (wrong document — returned Dominican Republic Law 424-06, not Vietnam). WebSearch attempted once (query: "Vietnam Law on Advertising 16/2012/QH13 English translation prohibited misleading advertising article") and returned "Web search error: unavailable" — 2026-09-17, consistent with the 2026-09-16 200/200 exhaustion possibly not yet reset.

`unknown — checked luatvietnam, vanbanphapluat, thuvienphapluat, WIPOLex, WebSearch (unavailable) 2026-09-17`. Vietnam's Law on Advertising (16/2012/QH13) primary or reliable secondary English text was not reached this pass. Next agent with either a working WebSearch budget or browser access should retry — this is a named brief requirement left open, not skipped by choice.

## Bing/Microsoft — webmaster guidelines: JS shell, no text recovered

Source: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a — attempted WebFetch and curl (2026-09-17). curl returned 125,562 bytes of HTML with zero occurrences of "cloak" (case-insensitive) — page is a client-rendered app shell; the actual guidelines text loads via JS after page load and was not captured by either tool. `unknown — checked bing.com 2026-09-17`, needs browser-rendered fetch (claude-in-chrome) next pass.

## OpenAI — ads-terms and ChatGPT-ads help page: blocked

https://openai.com/en-us/policies/ads-terms/, https://openai.com/policies/ads-terms/, https://help.openai.com/en/articles/12405146-about-ads-in-chatgpt — all returned HTTP 403 to both WebFetch and curl, 2026-09-17. Same 403 pattern pass 2 documented for OpenAI's other policy pages before it fell back to a browser (`../../../docs/raw/tos-browser-pulls.md`). That browser pull did not cover the ads-specific terms. **Open**: whether OpenAI's own Ads Terms require sponsored-content labeling that would apply to a page an advertiser controls being read by OAI-AdsBot vs OAI-SearchBot differently — unresolved, needs browser access.
