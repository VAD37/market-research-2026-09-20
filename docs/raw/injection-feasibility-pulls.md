# Injection feasibility — raw pulls

Pass 2, fetched 2026-09-16. Research agent 5. Scope: technical feasibility of (1) identifying AI-search crawlers from a domain the tester owns, (2) whether engines do live retrieval, (3) measurement methodology for content influence on AI answers, (4) the policy/legal boundary. No injection payloads reproduced — see CLAUDE.md ethics scope.

---

## OpenAI — OAI-SearchBot

Source: https://developers.openai.com/api/docs/bots — vendor-reported — fetched 2026-09-16 (redirected from https://platform.openai.com/docs/bots, 301)

Purpose: "used to surface websites in search results in ChatGPT's search features"

User agent: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot`

robots.txt guidance: "we recommend allowing OAI-SearchBot in your site's robots.txt file"

IP ranges file: https://openai.com/searchbot.json

---

## OpenAI — GPTBot (training crawler)

Source: https://developers.openai.com/api/docs/bots — vendor-reported — fetched 2026-09-16

Purpose: "used to make our generative AI foundation models more useful and safe"

User agent: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot`

robots.txt guidance: "Disallowing GPTBot indicates a site's content should not be used in training generative AI foundation models"

IP ranges file: https://openai.com/gptbot.json

---

## OpenAI — OAI-AdsBot

Source: https://developers.openai.com/api/docs/bots — vendor-reported — fetched 2026-09-16

Purpose: "used to validate the safety of web pages submitted as ads on ChatGPT"

User agent: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-AdsBot/1.0; +https://openai.com/adsbot`

Note: "data collected by OAI-AdsBot is not used to train generative AI foundation models"

IP ranges file: https://openai.com/adsbot.json

---

## OpenAI — ChatGPT-User (live user-triggered fetch)

Source: https://developers.openai.com/api/docs/bots — vendor-reported — fetched 2026-09-16

Purpose: "used for certain user actions in ChatGPT and Custom GPTs"

User agent: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot`

robots.txt guidance: "robots.txt rules may not apply" since actions are user-initiated

IP ranges file: https://openai.com/chatgpt-user.json

---

## OpenAI — gptbot.json raw content

Source: https://openai.com/gptbot.json — vendor-reported — fetched 2026-09-16

```json
{
  "creationTime": "2025-10-30T11:00:00.000000",
  "prefixes": [
    {"ipv4Prefix": "132.196.86.0/24"},
    {"ipv4Prefix": "172.182.202.0/25"},
    {"ipv4Prefix": "172.182.204.0/24"},
    {"ipv4Prefix": "172.182.207.0/25"},
    {"ipv4Prefix": "172.182.214.0/24"},
    {"ipv4Prefix": "172.182.215.0/24"},
    {"ipv4Prefix": "20.125.66.80/28"},
    {"ipv4Prefix": "20.171.206.0/24"},
    {"ipv4Prefix": "20.171.207.0/24"},
    {"ipv4Prefix": "4.227.36.0/25"},
    {"ipv4Prefix": "52.230.152.0/24"},
    {"ipv4Prefix": "74.7.175.128/25"},
    {"ipv4Prefix": "74.7.227.0/25"},
    {"ipv4Prefix": "74.7.227.128/25"},
    {"ipv4Prefix": "74.7.228.0/25"},
    {"ipv4Prefix": "74.7.230.0/25"},
    {"ipv4Prefix": "74.7.241.0/25"},
    {"ipv4Prefix": "74.7.241.128/25"},
    {"ipv4Prefix": "74.7.242.0/25"},
    {"ipv4Prefix": "74.7.243.128/25"},
    {"ipv4Prefix": "74.7.244.0/25"}
  ]
}
```

21 IPv4 CIDR prefixes as of creationTime 2025-10-30T11:00:00. Geo/ASN read: prefixes fall in Microsoft Azure-registered ranges (20.x, 172.182.x, 4.227.x, 52.230.x are Azure blocks) plus 74.7.x and 132.196.x — consistent with OpenAI running crawl infrastructure on Azure. Not independently confirmed against a WHOIS/ASN lookup in this pass — flagged for pass 3.

---

## Anthropic — ClaudeBot, Claude-User, Claude-SearchBot

Source: https://support.claude.com/en/articles/8896518 — vendor-reported — fetched 2026-09-16

ClaudeBot: "helps enhance the utility and safety of our generative AI models by collecting web content that could potentially contribute to their training."

Claude-User: "supports Claude AI users. When individuals ask questions to Claude, it may access websites using a Claude-User agent."

Claude-SearchBot: "navigates the web to improve search result quality for users. It analyzes online content specifically to enhance the relevance and accuracy of search responses."

IP list: "If a crawler has a source IP address on [this list](https://claude.com/crawling/bots.json), it indicates that the crawler is coming from Anthropic." — one combined list, 20 IPv4 prefixes, no per-bot labels (per WebSearch-relayed count; not independently re-verified by direct JSON fetch in this pass).

IP-blocking caveat, verbatim: "Alternate methods like blocking IP address(es) from which Anthropic Bots operates may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file." Anthropic's own recommended control is robots.txt, not IP blocking.

---

## Perplexity — PerplexityBot

Source: https://docs.perplexity.ai/docs/resources/perplexity-crawlers — vendor-reported — fetched 2026-09-16

User agent: `"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)"`

Purpose: "designed to surface and link websites in search results on Perplexity. It is not used to crawl content for AI foundation models."

IP ranges file: https://www.perplexity.com/perplexitybot.json

---

## Perplexity — Perplexity-User

Source: https://docs.perplexity.ai/docs/resources/perplexity-crawlers — vendor-reported — fetched 2026-09-16

User agent: `"Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)"`

Purpose: "supports user actions within Perplexity. When users ask Perplexity a question, it might visit a web page" to provide accurate answers. Not used for web crawling or model training data collection.

IP ranges file: https://www.perplexity.com/perplexity-user.json

Robots.txt behavior, verbatim: "Since a user requested the fetch, this fetcher generally ignores robots.txt rules."

---

## Cloudflare — Perplexity stealth-crawler report, methodology and findings

Source: https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ — vendor-reported (Cloudflare) — fetched 2026-09-16 — dated August 2025 per prior research pass

Methodology: Cloudflare "created test domains and implemented robots.txt files prohibiting automated access," then "queried Perplexity AI about these restricted sites" and found the service "was still providing detailed information regarding the exact content hosted on each of these restricted domains."

Undeclared user agent: Perplexity used "a generic browser intended to impersonate Google Chrome on macOS when their declared crawler was blocked."

Traffic volume: the stealth crawler generated "3-6m daily requests" versus the declared crawler's "20-25m daily requests," "observed across tens of thousands of domains and millions of requests per day."

IP/ASN evasion: the undeclared crawler "utilized multiple IPs not listed in Perplexity's official IP range, and would rotate through these IPs in response to the restrictive robots.txt policy," with "requests coming from different ASNs in attempts to further evade website blocks."

---

## Cloudflare — Perplexity report, comparison to compliant bot behavior

Source: https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ — vendor-reported — fetched 2026-09-16

Control comparison: when tested identically, "ChatGPT-User fetched the robots file and stopped crawling when it was disallowed" — cited by Cloudflare as the compliant baseline Perplexity's undeclared crawler did not meet.

Consequence: Cloudflare removed Perplexity from its verified-bot program and blocked the observed behavior (per prior pass summary; not independently re-quoted verbatim in this pass — flagged for confirmation in pass 3).

---

## Google — AI features, retrieval relationship to Search index

Source: https://developers.google.com/search/docs/appearance/ai-features — vendor-reported — fetched 2026-09-16

"AI is built into Search and integral to how Search functions."

Eligibility: "a page must be indexed and eligible to be shown in Google Search with a snippet, fulfilling the Search technical requirements." No additional technical requirement beyond ordinary Search indexing/snippet eligibility is stated.

Google-Extended is named as the separate control: site owners can "limit AI training and grounding in some of Google's other systems" via Google-Extended — i.e. training/grounding opt-out is distinct from Search indexing opt-out (robots.txt for Googlebot).

Control surfaces for what shows: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`.

---

## Google — AI Mode announcement (query fan-out, source mix)

Source: https://blog.google/products/search/ai-mode-search/ — company-stated — fetched 2026-09-16

AI Mode described as "an early experiment in Labs" that "expands what AI Overviews can do with more advanced reasoning, thinking and multimodal capabilities."

Query fan-out, verbatim: "issuing multiple related searches concurrently across subtopics and multiple data sources and then brings those results together to provide an easy-to-understand response."

Source mix, verbatim: AI Mode integrates "advanced model capabilities with Google's best-in-class information systems" and accesses "fresh, real-time sources like the Knowledge Graph, info about the real world, and shopping data for billions of products."

Caveat: this Google blog post does not use the phrase "live retrieval" vs "search index" explicitly — the query fan-out description implies live, per-query search dispatch rather than serving a single cached index lookup, but Google does not spell out the live/index distinction in its own words on this page.

---

## Google — query fan-out explained by Search engineering director

Source: https://blog.google/company-news/inside-google/googlers/how-google-ai-visual-search-works/ — company-stated (Dounia Berrada, Search Senior Engineering Director) — fetched 2026-09-16

"AI Mode is basically doing a dozen searches for you in the time it takes to do one."

Mechanism, verbatim: "it uses a 'fan-out' technique which triggers multiple searches at once," and the model "reads through the results and presents a single, cohesive response with helpful links — all in seconds."

Gap: this page does not state whether the underlying searches hit a live web fetch or a pre-built index; Google's own text stops short of that distinction.

---

## Google — verifying Googlebot via forward-confirmed reverse DNS

Source: https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests — vendor-reported — fetched 2026-09-16

Step 1: "Run a reverse DNS lookup on the accessing IP address from your logs, using the `host` command."

Step 2: "Verify that the domain name is either `googlebot.com`, `google.com`, or `googleusercontent.com`."

Step 3: "Run a forward DNS lookup on the domain name retrieved in step 1 using the `host` command on the retrieved domain name."

Step 4: "Verify that it's the same as the original accessing IP address from your logs."

Example commands given: `host 66.249.66.1`, `host 35.247.243.240`, `host 66.249.90.77`.

Google also recommends its published IP-range JSON files for automated, large-scale verification as an alternative to manual rDNS.

---

## Amazon — Amazonbot documentation

Source: https://developer.amazon.com/amazonbot — vendor-reported — fetched 2026-09-16

Purpose: "Amazonbot is used to improve our products and services. This helps us provide more accurate information to customers and may be used to train Amazon AI models."

User agent: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36`

IP verification: Amazon publishes verified IPs at https://developer.amazon.com/amazonbot/ip-addresses/

Note: the fetched page text made no explicit connection to "Rufus" by name — relationship to Amazon's Rufus shopping assistant is asserted by third-party trackers, not stated on this page. Flag as unconfirmed at the primary-source level.

---

## Apple — Applebot and Applebot-Extended

Source: https://support.apple.com/en-us/119829 — vendor-reported — fetched 2026-09-16

Applebot purpose: "The data crawled by Applebot is used to power various features, such as the search technology integrated into many user experiences in Apple's ecosystem including Spotlight, Siri, and Safari."

Applebot-Extended purpose: opt-out control for AI training use. Verbatim: "web publishers can opt-out from having their content used to train generative foundation models by disallowing Applebot-Extended in the robots.txt file."

Example desktop UA: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15 (Applebot/0.1; +http://www.apple.com/go/applebot)"

Opt-out syntax given: `User-agent: Applebot-Extended` / `Disallow: /`

---

## Meta — Meta-ExternalAgent and Meta-ExternalFetcher

Source: https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/ — vendor-reported — fetched 2026-09-16

Meta-ExternalAgent purpose: "crawls the web for use cases such as training foundation AI models or improving products by indexing content directly." UA: `meta-externalagent/1.1 (+/documentation/sharing/webmasters/web-crawlers)`

Meta-ExternalFetcher purpose: "fetches individual links at a user's request and supports product functions such as evaluating and improving agentic AI capabilities—including helping AI navigate websites to complete tasks for users." UA: `meta-externalfetcher/1.1 (+/documentation/sharing/webmasters/web-crawlers)`

robots.txt note, verbatim: Meta-ExternalFetcher "may bypass robots.txt" rules.

No IP-range file found published on this page — negative finding, checked 2026-09-16.

---

## Common Crawl — CCBot

Source: https://commoncrawl.org/ccbot — vendor-reported — fetched 2026-09-16

Purpose: "Common Crawl is a non-profit foundation founded with the goal of democratizing access to web information by producing and maintaining an open repository of web crawl data."

User agent: "CCBot/2.0 (https://commoncrawl.org/faq/)"

IP ranges: published as JSON at https://index.commoncrawl.org/ccbot.json, described as supporting rDNS verification.

---

## ByteDance — Bytespider: negative finding

Not fetched as a primary vendor doc — checked WebSearch 2026-09-16. No ByteDance-published crawler documentation page was located for Bytespider (contrast: OpenAI, Anthropic, Perplexity, Google, Amazon, Apple, Meta and Common Crawl all publish a docs page; ByteDance does not appear to for this crawler). Secondary trackers describe Bytespider as ignoring robots.txt and publishing no user-facing documentation. Unverified at primary-source level — `unknown — checked WebSearch 2026-09-16`.

---

## Cloudflare — Pay per crawl announcement

Source: https://blog.cloudflare.com/introducing-pay-per-crawl/ — vendor-reported — fetched 2026-09-16, post dated 2025-07-01 (private beta launch)

"Pay per crawl is a new feature to allow content creators to charge AI crawlers for access to their content."

Mechanism: Cloudflare revives HTTP response code 402; a `402 Payment Required` response carries pricing information when payment is required.

Authentication requirement: crawlers must implement Web Bot Auth — Ed25519 key pairs, registration with Cloudflare, HTTP Message Signatures with `signature-agent`, `signature-input`, `signature` headers.

Status at fetch time: private beta; no specific price points or adoption numbers stated in the announcement itself.

---

## Cloudflare — AI Crawl Control overview

Source: https://developers.cloudflare.com/ai-crawl-control/ — vendor-reported — fetched 2026-09-16, page states "Last updated August 14, 2026"

Function: "Monitor and control how AI services access your website content." Capabilities listed: see which AI services access content, allow/block policies, monitor robots.txt compliance, explore monetization, "Deploy with zero configuration on all Cloudflare plans."

Gap: this overview page does not itself restate the verified-bots/Web Bot Auth requirement found on the pay-per-crawl page — cross-reference, not contradiction.

---

## Cloudflare Radar data via third-party analysis — AI crawler purpose split

Source: https://technologychecker.io/blog/ai-crawler-statistics — analyst-derived (third party analyzing Cloudflare Radar data, not Cloudflare's own report page directly fetched) — fetched 2026-09-16

August 2026 purpose split of AI crawler requests: Training 40.15% (down from 44.76% in July 2026), Search 16.45% (up from 11.56%), Mixed Purpose 36.96% (down from 39.80%), User Action 4.80% (up from 2.66%).

Year-over-year, July 2025 to July 2026: Training +8.80 points (35.74% to 44.54%), Mixed Purpose −14.62 points (54.61% to 39.99%), Search +3.78 points (7.79% to 11.57%).

Analyst framing, verbatim: "AI crawling has not shifted from training to search so much as it has stopped being ambiguous about which it is doing."

Top AI crawlers, August 2026: Googlebot 22.90%, Meta-ExternalAgent 14.04%, ClaudeBot 11.88%.

Shopping-vertical crawl load: 31.58% of AI crawler requests in July 2026, the heaviest of any industry vertical named.

Caveat: this is a third party's read of Cloudflare Radar, not a direct fetch of a Cloudflare Radar page. Attempted direct fetch of radar.cloudflare.com AI crawl-control report returned HTTP 403 — checked 2026-09-16.

---

## Akamai — 2026 commerce AI-bot report

Source: https://www.akamai.com/newsroom/press-release/akamai-research-commerce-becomes-the-epicenter-for-ai-bot-attacks-and-agentic-fraud-in-2026 — vendor-reported — fetched 2026-09-16

Period: July 2025 to December 2025.

"Nearly half (47.9%) of all AI bot traffic across Akamai's global network from July 2025 to December 2025 was in the commerce vertical."

"AI training crawlers account for more than 70% of AI bot triggers in commerce."

Top three AI bot operators observed, verbatim: "OpenAI, ByteDance, and Anthropic rank as the top three AI bots observed."

Bot-management posture: organizations "placed more than 90% of their AI bot activity in the 'monitor' category but allowed three-quarters of the remaining activity to pass unrestricted."

Regional growth: bot activity "surged by 63% in APAC and 48% in LATAM."

---

## Fastly — bot traffic report (relayed, not directly fetched)

Source: fastly.com blog, via WebSearch summary — vendor-reported, relayed — checked 2026-09-16. Direct WebFetch of the Fastly report page was not attempted in this pass (WebSearch budget exhausted before the URL was captured); flagged for pass 3.

Reported finding: for the period mid-April to mid-July 2025, "AI crawlers made up almost 80% of all AI bot traffic observed, with Meta generating more than half and eclipsing both Google and OpenAI combined." Fetcher-bot (real-time, user-triggered) request volume reported "exceeding 39,000 requests per minute in some cases."

Caveat: numbers not independently confirmed against Fastly's own page text; relayed via search-summary only.

---

## GEO: Generative Engine Optimization (KDD 2024) — abstract and methodology

Source: https://arxiv.org/abs/2311.09735 — peer-reviewed (KDD 2024) — fetched 2026-09-16

Authors: Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande. Submitted 2023-11-16.

Abstract opening, verbatim: "The advent of large language models (LLMs) has ushered in a new paradigm of search engines that use generative models to gather and summarize information to answer user queries."

Method: black-box optimization framework letting a site owner rewrite page content to increase visibility in generative-engine answers, evaluated against a purpose-built benchmark ("GEO-bench") of diverse queries and relevant sources.

Metrics used, per pass-1 carryover and this pass's fetch: "objective and subjective impression metrics — the former measuring word count and citation position in the GE's response, while the latter computes multiple subjective factors, giving an overall impression score." Reported effect size: ~22% improvement on Position-Adjusted Word Count, ~37% on Subjective Impression (best method vs baseline, per search-summary render); the fetched abstract itself states "approximately 40%" visibility improvement, varying significantly by domain. Two renderings of the effect size exist in what was pulled — flagged, not reconciled, per repo rule on conflicting figures.

---

## Ranking Manipulation for Conversational Search Engines (Pfrommer et al., EMNLP 2024)

Source: https://arxiv.org/abs/2406.03589 — peer-reviewed (EMNLP 2024 Main) — fetched 2026-09-16

Authors: Samuel Pfrommer, Yatong Bai, Tanmay Gautam, Somayeh Sojoudi. Submitted 2024-06-05.

Abstract, verbatim: "Major search engine providers are rapidly incorporating Large Language Model (LLM)-generated content in response to user queries. These conversational search engines operate by loading retrieved website text into the LLM context for summarization and interpretation. Recent research demonstrates that LLMs are highly vulnerable to jailbreaking and prompt injection attacks, which disrupt the safety and quality goals of LLMs using adversarial strings. This work investigates the impact of prompt injections on the ranking order of sources referenced by conversational search engines. To this end, we introduce a focused dataset of real-world consumer product websites and formalize conversational search ranking as an adversarial problem. Experimentally, we analyze conversational search rankings in the absence of adversarial injections and show that different LLMs vary significantly in prioritizing product name, document content, and context position. We then present a tree-of-attacks-based jailbreaking technique which reliably promotes low-ranked products. Importantly, these attacks transfer effectively to state-of-the-art conversational search engines such as perplexity.ai. Given the strong financial incentive for website owners to boost their search ranking, we argue that our problem formulation is of critical importance for future robustness work."

Methodology (the reusable measurement asset, no payload reproduced): (1) build a focused real-world product-website dataset (later released as "RAGDOLL"); (2) measure baseline ranking behavior per-LLM with no injection present, isolating which signals (product name, document content, position in context) drive ranking absent attack; (3) apply an automated tree-of-attacks jailbreak search to find adversarial strings that shift ranking, building on the published "Tree of Attacks (TAP)" method; (4) test transfer from a controlled harness to a live production system (perplexity.ai) to see if lab-found manipulations hold outside the lab.

---

## Pfrommer et al. — code repository, methodology detail

Source: https://github.com/spfrommer/cse-ranking-manipulation — peer-reviewed supplementary (author-published code) — fetched 2026-09-16

Dataset: "a real-world e-commerce website dataset" (RAGDOLL), with an open-sourced "dataset collection pipeline."

Attack technique lineage, verbatim: "a tree-of-attacks-based jailbreaking technique which reliably promotes low-ranked products," built "based on the minimal implementation" of "Tree of Attacks (TAP): Jailbreaking Black-Box LLMs Automatically."

Transfer test target named explicitly: "closed-source, online-enabled RAG implementations such as the Sonar Large Online model by perplexity.ai."

---

## Adversarial Search Engine Optimization for Large Language Models (Nestaas, Debenedetti, Tramèr)

Source: https://arxiv.org/abs/2406.18382 — peer-reviewed / preprint — fetched 2026-09-16

Authors: Fredrik Nestaas, Edoardo Debenedetti, Florian Tramèr. Submitted 2024-06-26.

Framing, verbatim: "Large Language Models (LLMs) are increasingly used in applications where the model selects from competing third-party content, such as in LLM-powered search engines or chatbot plugins."

Contribution: "Preference Manipulation Attacks" — a named attack class, using crafted website/plugin-documentation content to shift which source an LLM favors, without reproducing the crafted strings here.

Game-theoretic finding: identifies a prisoner's-dilemma structure — each individual site is incentivized to attack, but collective attacking degrades answer quality for all, including the attackers.

Production systems tested: Bing, Perplexity (search engines), and plugin APIs for GPT-4 and Claude.

---

## PoisonedRAG (Zou, Geng, Wang, Jia — USENIX Security 2025)

Source: https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag and https://arxiv.org/abs/2402.07867 — peer-reviewed — fetched 2026-09-16

Authors: Wei Zou, Runpeng Geng (Penn State), Binghui Wang (Illinois Institute of Technology), Jinyuan Jia (Penn State). Published USENIX Security 25, August 2025, pp. 3827-3844.

Framing, verbatim: "Large language models (LLMs) have achieved remarkable success due to their exceptional generative capabilities. Despite their success, they also have inherent limitations such as a lack of up-to-date knowledge and hallucination." RAG is described as the mitigation, whose "knowledge database... introduces a new and practical attack surface."

Attack description (mechanism named, no payload text reproduced): attacker injects a small number of crafted texts into the RAG knowledge base so that, for an attacker-chosen question, the system retrieves those texts and the LLM generates an attacker-chosen target answer.

Reported effect size: "a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts."

Defense finding: existing defenses evaluated "are insufficient to defend against PoisonedRAG, highlighting the need for new defenses."

---

## PoisonedRAG — code repository description

Source: https://github.com/thisxyz/PoisonedRAG — peer-reviewed supplementary (author-published code) — fetched 2026-09-16

Self-description, verbatim: "The first knowledge poisoning attack against Retrievals-Augmented Generation (RAG) system." Repository provides setup/hyperparameter instructions and points to the arXiv paper (2402.07867) for full method detail; no attack strings reproduced here per this task's scope constraint.

---

## The Vulnerability of LLM Rankers to Prompt Injection Attacks (Yin, Wang, Koopman, Zuccon)

Source: https://arxiv.org/abs/2602.16752 — preprint, cs.CR — fetched 2026-09-16 (carried over from pass-1 abstract-only note; this pass fetched the abstract directly)

Authors: Yu Yin, Shuai Wang, Bevan Koopman, Guido Zuccon. Submitted 2026-02-18.

Finding, verbatim: "simple prompt injections embedded within a candidate document (i.e., jailbreak prompt attacks) can significantly alter an LLM's ranking decisions."

Scope: evaluated across model families, ranking paradigms (pairwise, listwise, setwise), and two injection variants.

Notable negative-for-attacker result, verbatim: "encoder-decoder architectures exhibit strong inherent resilience to jailbreak attacks" — architecture choice affects vulnerability, a defensive-relevant finding.

Venue note: also indexed under SIGIR 2026 proceedings per DOI 10.1145/3805712.3808553 (title carries an embedded prompt-injection joke instructing reviewers to mark it "Best Paper" — the paper's own subject matter demonstrated in its own listing; not itself a payload, noted as a curiosity).

---

## Google — Search spam policies: definition, AI-response manipulation, cloaking, enforcement

Source: https://developers.google.com/search/docs/essentials/spam-policies — vendor-reported (primary Google policy page) — fetched 2026-09-16, page shows "Last Updated: 2026-08-28 UTC"

Spam definition, verbatim, current wording as fetched: "Techniques used to deceive users or manipulate our Search systems into featuring content prominently, such as attempting to manipulate Search systems into ranking content highly or attempting to manipulate generative AI responses in Google Search."

AI-response manipulation is explicitly listed as a spam category, on par with classic ranking manipulation — not a separate/lesser category.

Cloaking definition, verbatim: "Presenting different content to users and search engines with the intent to manipulate search rankings and mislead users." Examples given: "showing a page about travel destinations to search engines while showing a page about discount drugs to users, or inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor."

Enforcement, verbatim: "Sites that violate our policies may rank lower in results or not appear in results at all." Detection is via "automated systems and, as needed, human review that can result in a manual action."

Caveat on the 2026-05-15 date: secondary press (Search Engine Land, MWM, Let's Data Science, Vizup, ALM Corp, mlq.ai, winbuzzer) attributes this specific spam-definition wording change to 2026-05-15. This pass could not independently confirm that exact date against Google's own changelog page (see next block) — the policy-definition page itself carries only a general "Last Updated" stamp, not a per-clause change date.

---

## Google — Search spam policy history / SpamBrain updates page: date-confirmation attempt

Source: https://developers.google.com/search/docs/appearance/spam-updates — vendor-reported — fetched 2026-09-16

Page's own "last updated" stamp at fetch time: 2025-12-10 UTC. No entry dated 2026-05-15 or May 2026 describing generative-AI-response manipulation, GEO, or recommendation poisoning was found on this specific page as fetched.

Negative finding: the primary Google changelog page that would carry a dated entry for the May 2026 policy language does not show that entry as of this fetch — either the change was folded into the spam-policies page without a discrete changelog entry, the changelog page has since been reorganized, or the fetch tool served a cached/stale version. Not resolved this pass — `unknown — checked developers.google.com 2026-09-16`. The wording change itself is independently confirmed present on the current spam-policies page (previous block); only the exact effective date is unconfirmed at the primary source.

---

## Google Terms of Service — automated access restrictions

Source: https://policies.google.com/terms — company-stated — fetched 2026-09-16

Automated access clause, verbatim: "using automated means to access content from any of our services in violation of the machine-readable instructions on our web pages (for example, robots.txt files that disallow crawling, training, or other activities)"

AI-training-use clause, verbatim: "using AI-generated content from our services to develop machine learning models or related AI technology"

Reverse-engineering clause, verbatim: "reverse engineering our services or underlying technology, such as our machine learning models, to extract trade secrets or other proprietary information, except as allowed by applicable law"

Stated consequence: violation "could result in account suspension or termination" (paraphrased by the fetch, not a direct quote of consequence language — flagged).

---

## llms.txt specification

Source: https://llmstxt.org/ — company/community-stated (proposed standard, Jeremy Howard / Answer.AI, 2024) — fetched 2026-09-16

Definition, verbatim: "A proposal to standardise on using an `/llms.txt` file to provide information to help agents use a website."

Problem statement, verbatim: "Web pages are built for people. An HTML page wraps its information in navigation, ads, and JavaScript, and converting it back into clean text is difficult and imprecise."

Required structure, in order: optional byte-order mark; H1 heading with project/site name (the only required section); blockquote with a brief summary; optional markdown sections; optional H2-delimited "file list" sections of markdown links `[name](url)` with optional `:` notes.

Location convention: `/llms.txt` at site root, or any subpath (e.g. `/docs/llms.txt`) covering URLs under that path — modeled explicitly on the robots.txt / sitemap.xml convention.

This is the sanctioned, publisher-side channel for telling an answer engine about a site's own content — distinct from, and not a workaround for, any per-engine crawler opt-in/opt-out (robots.txt) or structured-data (schema.org) mechanism.

---

## Amazon vs. Perplexity — scraping/agent dispute, real-world enforcement-adjacent case

Source: multiple secondary press, relayed via WebSearch — journalist-relayed — checked 2026-09-16 (Engadget, PYMNTS, SDxCentral, Wired-via-Axios; not independently WebFetched due to session search-budget exhaustion)

Timeline as relayed: mid-2024, Amazon Web Services investigated whether a Perplexity-operated virtual machine (identified by Wired, IP 44.221.181.252, hosted on AWS) was bypassing target sites' robots.txt while sourced from Amazon's own cloud — i.e., running afoul of AWS's own acceptable-use terms requiring customers to respect robots.txt when crawling.

Perplexity's own admission, as relayed: "PerplexityBot will ignore robots.txt when a user includes a specific URL in their chatbot inquiry" — i.e. Perplexity itself states the user-triggered fetcher does not honor robots.txt (consistent with the primary Perplexity docs block above).

Escalation, November 2025: Amazon issued a cease-and-desist against Perplexity alleging its "Comet" AI browser scrapes Amazon retail pages, "secretly logs into user accounts," and "masks machine actions as human clicks" — framed by Amazon as violating Amazon's terms of service and potentially federal/California computer-fraud statutes. Amazon subsequently filed suit in California federal court (relayed date: following the cease-and-desist).

Caveat: this is not a Google/OpenAI/Anthropic enforcement action against AI-answer manipulation — it is a platform-vs-crawler-operator scraping/ToS dispute. Relevant here only as the closest found real-world enforcement precedent involving an AI answer engine's crawling conduct. No enforcement action specifically for *manipulating an AI answer* (as opposed to *scraping to build one*) was found in this pass — negative finding, checked WebSearch 2026-09-16 (query terms: "deindexed AI answer manipulation enforcement case ban example 2026").

---

## Perplexity and OpenAI Terms of Service — automated querying: fetch attempts failed

Source: https://www.perplexity.ai/hub/legal/terms-of-service, https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service-search, https://openai.com/policies/usage-policies, https://openai.com/policies/row-terms-of-use/ — attempted fetch 2026-09-16, all four returned HTTP 403 Forbidden to the fetch tool.

Negative finding: could not independently verify exact ToS wording at the primary source in this pass. Secondary-source relay (WebSearch summaries, not independently confirmed verbatim): Perplexity's ToS is reported to prohibit "any robot, spider, crawlers, scraper, or other automatic device, process, software or queries that intercepts, 'mines,' scrapes, extracts, or otherwise accesses the Services to monitor, extract, copy or collect information or data from or through the Services" — outside its own official API. OpenAI's usage policies are reported to prohibit circumventing rate limits and protective measures, and to disallow account pooling/rotation to dodge limits. Both are relayed, not verified verbatim against the primary page in this pass — `unknown — checked WebSearch and WebFetch (403) 2026-09-16`.

---

## Perplexity retrieval pipeline — no vendor engineering blog located

Source: secondary sources only (ziptie.dev, Medium/KazKozDev, frugaltesting.com), relayed via WebSearch — checked 2026-09-16, no primary Perplexity engineering blog located and confirmed reachable in this pass (a direct WebFetch of perplexity.ai/hub/getting-started returned HTTP 403).

Relayed description: Perplexity is described (third-party) as running "a six-stage RAG pipeline: query parsing, embedding-based indexing, hybrid retrieval (BM25 + dense), multi-layer ML ranking, structured prompt assembly with pre-embedded citations, and constrained LLM generation," with "every query" triggering "a fresh web retrieval from Perplexity's live index."

Caveat: none of this is a Perplexity-authored primary source in this pass. Recorded as a negative finding on vendor documentation, with the secondary description flagged as unverified at the primary-source level — `unknown — checked WebFetch (403) and WebSearch 2026-09-16`.

---

## Anthropic — web search tool: pricing, live-retrieval behavior, citations

Source: https://claude.com/blog/web-search-api — company-stated — fetched 2026-09-16

Decision logic, verbatim-derived: Claude "uses its reasoning capabilities to determine whether the web search tool would help provide a more accurate response," and can run "multiple progressive searches, using earlier results to inform subsequent queries."

Live behavior: Claude "generates a targeted search query, retrieves relevant results, analyzes them for key information, and provides a comprehensive answer with citations back to the source material."

Pricing, verbatim: "$10 per 1,000 searches plus standard token costs." Models covered at announcement: Claude 3.7 Sonnet, Claude 3.5 Sonnet, Claude 3.5 Haiku.

Citation behavior: "Every web-sourced response includes citations to source materials."

This confirms Claude's web-search tool is a live, per-query fetch (a request a domain owner's server log would see, tied in time to a live user session), not a pre-built static index lookup — when the tool is invoked. Whether/how often Claude invokes it for a given prompt is model-discretionary per this same text ("determine whether... would help").
