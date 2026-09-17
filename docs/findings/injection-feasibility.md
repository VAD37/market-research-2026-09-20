# Technical feasibility — detecting AI crawlers, and measuring answer influence

Pass 2, 2026-09-16. Compiled from `../raw/injection-feasibility-pulls.md` (39 blocks) and `../raw/injection-feasibility-source-index.md`.

Placement note: this is a technical read, not a market sizing, so it does not fit `markets/`. Filed here because it crosses `ai-search-ads` and `ai-attack-defense`. Second stated deviation from `../CLAUDE.md`'s folder scheme, after the rosters.

Scope: authorized testing on infrastructure the tester owns. Detection, measurement and policy. No payloads recorded — technique names and citations only.

## Question 1 — can AI-search crawlers be identified from a domain you control?

**Yes. By IP range or forward-confirmed reverse DNS. Never by user-agent alone.**

Every major operator except ByteDance publishes both a user-agent string and an IP-range file.

| Operator | Bots | IP ranges published |
|---|---|---|
| OpenAI | GPTBot, ChatGPT-User, OAI-SearchBot, **OAI-AdsBot** | Four separate JSON files, one per bot |
| Anthropic | ClaudeBot, Claude-User, Claude-SearchBot | One combined list, no per-bot labels |
| Perplexity | PerplexityBot, Perplexity-User | Two JSON files |
| Amazon | Amazonbot | Yes, verified-IP page |
| Apple | Applebot, Applebot-Extended | Docs page, ranges not confirmed this pass |
| Meta | Meta-ExternalAgent, Meta-ExternalFetcher | **None found** — checked 2026-09-16 |
| Common Crawl | CCBot | Yes, supports rDNS |
| ByteDance | Bytespider | **No documentation found at all** |

Exact URLs are in the raw file. `https://openai.com/gptbot.json` returned 21 IPv4 prefixes, creationTime 2025-10-30, sitting in Azure-registered blocks — consistent with OpenAI crawling from Azure. ASN not confirmed by WHOIS this pass.

**OAI-AdsBot is the find relevant to idea 1.** OpenAI runs a distinct crawler whose stated purpose is "to validate the safety of web pages submitted as ads on ChatGPT," with its own IP file, and whose data "is not used to train generative AI foundation models." The ad pipeline is separately observable from the search pipeline, on a domain you control.

Verification method is vendor-documented. Google publishes the four-step forward-confirmed rDNS procedure with example `host` commands: reverse lookup the IP, check the domain is `googlebot.com` / `google.com` / `googleusercontent.com`, forward lookup that domain, confirm it returns the original IP. IP-range JSON is the automatable alternative for scale.

## The counter-finding that limits all of the above

Declared identity is reliable for compliant operators and **not universally trustworthy.**

Cloudflare, Aug 2025 (vendor-reported): it created test domains with robots.txt prohibiting access, then queried Perplexity about them and got back "detailed information regarding the exact content hosted on each of these restricted domains." The undeclared crawler used "a generic browser intended to impersonate Google Chrome on macOS," ran from "multiple IPs not listed in Perplexity's official IP range," rotated those IPs in response to robots.txt, and used "different ASNs in attempts to further evade website blocks." Volume: **3–6M daily requests** undeclared, against **20–25M** declared.

Control in the same test: "ChatGPT-User fetched the robots file and stopped crawling when it was disallowed."

Anthropic states the limit in its own docs: blocking its IPs "may not work correctly or persistently guarantee an opt-out, as doing so impedes our ability to read your robots.txt file." The vendor-sanctioned control is robots.txt, not IP blocking.

Read for the idea: detection works, and the gap between declared and actual behaviour is itself a measurable product surface. Cloudflare's methodology — controlled domain, robots.txt disallow, then query the engine and see if it knows — is a reusable test, published.

## Crawl volume, for sizing

| Figure | Period | Source |
|---|---|---|
| Training 40.15%, Mixed 36.96%, Search 16.45%, User Action 4.80% | Aug 2026 | Cloudflare Radar, third-party analysis |
| Googlebot 22.90%, Meta-ExternalAgent 14.04%, ClaudeBot 11.88% | Aug 2026 | same |
| Shopping = 31.58% of AI crawler requests, heaviest vertical | Jul 2026 | same |
| 47.9% of AI bot traffic was commerce | Jul–Dec 2025 | Akamai, vendor-reported |
| AI training crawlers = 70%+ of AI bot triggers in commerce | Jul–Dec 2025 | Akamai |
| "OpenAI, ByteDance, and Anthropic rank as the top three AI bots" | Jul–Dec 2025 | Akamai |
| 90%+ of AI bot activity left in "monitor," three-quarters of the rest passed unrestricted | Jul–Dec 2025 | Akamai |
| AI crawlers ~80% of AI bot traffic; Meta over half | Apr–Jul 2025 | Fastly, relayed not fetched |

Akamai's last row is a demand signal: enterprises are watching this traffic and not acting on it.

Cloudflare shipped commercial controls — Pay per crawl (private beta 2025-07-01, revives HTTP 402, requires Web Bot Auth with Ed25519 signatures) and AI Crawl Control (page updated 2026-08-14, zero-config on all plans). The monitoring layer for crawler identity is already free and bundled. That prices the floor for anything built here.

## Question 2 — live retrieval or index?

Mixed, and vendors are vague about it. This decides whether a domain owner can observe an answer being built at all.

| Engine | Behaviour | Confidence |
|---|---|---|
| Claude web search | **Live, per-query.** $10 per 1,000 searches, citations on every response | Confirmed, company-stated |
| Google AI Mode | Query fan-out — "doing a dozen searches for you in the time it takes to do one" | Live sub-searches confirmed; live-fetch vs index **never stated by Google** |
| Google AI Overviews | A page needs only ordinary Search index and snippet eligibility to appear | Confirmed, vendor-reported |
| Perplexity | Third parties describe a six-stage RAG with "fresh web retrieval" per query | **Unverified** — vendor page returned HTTP 403 |
| ChatGPT search, Copilot | No engineering documentation located | unknown — checked 2026-09-16 |

Two consequences. Claude invokes search at model discretion, so absence of a request is not absence of an answer. And Google's controls are split: `Google-Extended` governs training and grounding; Search indexing is governed separately by Googlebot and robots.txt, with `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` controlling what surfaces. Opting out of one is not opting out of the other.

## Question 3 — the measurement methodology

The reusable asset from the literature is the method, not the attacks. Four papers, one consistent pattern.

| Paper | Venue | Reported effect |
|---|---|---|
| GEO: Generative Engine Optimization, Aggarwal et al. | KDD 2024 | Visibility lift ~22% / ~37% by metric, or "approximately 40%" per the abstract — **two renderings, unreconciled** |
| Ranking Manipulation for Conversational Search Engines, Pfrommer et al. | EMNLP 2024 | Reliably promotes low-ranked products; transfers to live perplexity.ai |
| Adversarial SEO for LLMs, Nestaas, Debenedetti, Tramèr | preprint | "Preference Manipulation Attacks." Tested on Bing, Perplexity, GPT-4 and Claude plugin APIs |
| PoisonedRAG, Zou et al. | USENIX Security 2025 | **90% success injecting five texts** into a million-text corpus. Existing defenses "insufficient" |
| LLM Rankers vs Prompt Injection, Yin et al. | preprint / SIGIR 2026 | Encoder-decoder architectures "exhibit strong inherent resilience" |

The shared method, four steps:

1. Build a real-world content and query dataset. Pfrommer released theirs as RAGDOLL, with an open-sourced collection pipeline.
2. Measure **baseline** behaviour with no intervention — which signals drive ranking absent any attack. Pfrommer found LLMs "vary significantly in prioritizing product name, document content, and context position."
3. Apply a controlled intervention and measure the shift.
4. **Test transfer from lab harness to a live production engine.** Pfrommer's target was named: perplexity.ai's Sonar Large Online.

Step 4 is what nobody sells. Steps 1–3 exist in published code.

Two findings cut against a pure-attack framing. Nestaas identifies a prisoner's-dilemma structure — each site is incentivised to manipulate, collective manipulation degrades answers for everyone including the manipulators. And Yin's encoder-decoder resilience result is a defensive finding: architecture choice changes exposure. Both point the same way, toward measurement and defence rather than exploitation.

## Question 4 — the policy boundary

Fetched from Google's own page, `Last Updated: 2026-08-28`:

> "Techniques used to deceive users or manipulate our Search systems into featuring content prominently, such as attempting to manipulate Search systems into ranking content highly or **attempting to manipulate generative AI responses in Google Search**."

AI-response manipulation is listed as spam, on par with classic ranking manipulation. Enforcement: "Sites that violate our policies may rank lower in results or not appear in results at all," via automated systems plus human review and manual actions.

Cloaking, verbatim from the same page:

> "Presenting different content to users and search engines with the intent to manipulate search rankings and mislead users."

Named example: "inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor."

**That is decisive for the idea's design.** Serving different content when you detect OAI-SearchBot or PerplexityBot is the cloaking definition, and intent is the hinge — the policy says "with the intent to manipulate rankings and mislead users." A measurement harness on a domain you own, with no misleading intent toward users, sits on the other side of that line from a production tactic. The line is real, narrow, and needs naming in any offering built here.

**Correction to pass 1:** pass 1 recorded Google classifying AI-answer manipulation as Search spam on **2026-05-15**. The wording is confirmed present on the primary page. **The date is not.** Google's spam-updates changelog carries a last-updated stamp of 2025-12-10 and shows no entry for May 2026. The 2026-05-15 date comes only from secondary press. Treat as `unknown — checked developers.google.com 2026-09-16`.

Other boundaries:

- **Google ToS** (fetched) bars "using automated means to access content from any of our services in violation of the machine-readable instructions on our web pages," bars using Google AI output to develop ML models, and bars reverse engineering its models.
- **OpenAI and Perplexity ToS: read in full on 2026-09-16** via browser, after four HTTP 403s to automated fetch. Raw in `../raw/tos-browser-pulls.md`. The answer splits by surface.

  **Consumer surfaces are closed to a measurement product.** OpenAI's Terms of Use (effective 2026-01-01) bar you outright: "Automatically or programmatically extract data or Output." Perplexity's ToS (last updated 2026-01-23) goes further on three axes — s5.1 licenses the service for "personal, non-commercial use only"; s5.2(e) bars you to "exploit the Services for any commercial purpose"; and s5.2(i) bars any "robot, spider, crawlers, scraper, or other automatic device, process, software or queries that... monitor, extract, copy or collect information or data from or through the Services, **or engage in any manual process to do the same**." That last clause closes the hand-run workaround. Hiring people to type queries and record answers is prohibited on identical terms to a script.

  **The API path is not closed by these documents.** OpenAI's Service Terms (updated 2026-09-10) impose one restriction on API customers: "use APIs in accordance with the applicable documentation." No extraction ban. Perplexity's consumer ToS states in its own scope paragraph that it "do[es] not govern use of the Company's APIs," which are under a separate agreement. Neither API agreement was read — both are the immediate next pull.

  **Perplexity names a third route:** s5.2's restrictions apply "unless applicable laws or regulations prohibit these restrictions or **you have our written permission to do so**." A negotiated agreement is a documented way through, not a loophole.

  **Enforcement is judicial, not arbitral.** Both companies carve unauthorized use and injunctive relief out of otherwise mandatory arbitration. OpenAI's exception covers "injunctive or other equitable relief to stop unauthorized use or abuse of the Services," venued exclusively in San Francisco. Perplexity excepts claims "where the sole form of relief sought is injunctive relief" and IP claims.

  Design consequence: a measurement product that queries consumer ChatGPT or perplexity.ai breaches both ToS regardless of how the querying is done. The same product built on the paid APIs is governed by documents that, as far as these two pages go, do not prohibit it.
- **Perplexity itself states** its user-triggered fetcher "generally ignores robots.txt rules," as does Meta-ExternalFetcher and OpenAI's ChatGPT-User. User-initiated fetches are outside robots.txt across all three.
- **No enforcement action for manipulating an AI answer was found.** The nearest precedent is Amazon v. Perplexity — cease-and-desist Nov 2025, then suit — over Comet's scraping, account logins and "mask[ing] machine actions as human clicks." That is platform-vs-crawler, not answer manipulation.

The sanctioned channel is **llms.txt** — an `/llms.txt` markdown file at site root, modeled on robots.txt and sitemap.xml, proposed by Answer.AI in 2024 — plus schema.org structured data. Publisher-side, declarative, not a substitute for per-engine crawler controls.

## What this means for the two ideas

For `ai-search-ads`: the detection half of the user's hypothesis is confirmed and cheap — published IP files and a documented rDNS procedure. The influence half is measurable by a published four-step method with released datasets. The constraint is not technical. It is that the differential-serving tactic is named in Google's spam policy, two of three engines' ToS could not be read, and Cloudflare already gives crawler visibility away free.

For `ai-attack-defense`: PoisonedRAG's finding that "existing defenses are insufficient" and Yin's architecture-resilience result are both defensible assessment work. Testing a client's own RAG corpus against published poisoning methods is squarely inside the authorized-services lane from `../markets/ai-attack-defense.md`, and needs no third-party engine access at all.

## Caveats

- Anthropic's combined IP list (20 prefixes, no per-bot labels) came via search relay; the JSON was not fetched directly.
- Azure attribution of OpenAI's prefixes is inferred from the ranges, not confirmed by WHOIS or ASN lookup.
- Cloudflare's removal of Perplexity from its verified-bots program is carried from pass 1, not re-quoted verbatim.
- Cloudflare Radar's own pages returned HTTP 403; crawl-share figures come from a third party's reading of Radar.
- Fastly's report was relayed by search summary, never fetched.
- The GEO paper's effect size appears as ~22%/~37% and as "approximately 40%" in the same pull. Both on file.
- Amazon v. Perplexity is entirely secondary-sourced; no filing read.
- Bytespider's lack of documentation is a search-level negative, not proof none exists.
