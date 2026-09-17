# Injection feasibility — source index

Pass 2, fetched 2026-09-16. Every URL touched during this research pass, grouped by theme. One line each. Full quotes are in `injection-feasibility-pulls.md`.

## Crawler identity — OpenAI

- https://developers.openai.com/api/docs/bots — primary bot docs, fetched (redirected from platform.openai.com/docs/bots)
- https://openai.com/gptbot.json — IP range file, fetched, raw JSON quoted
- https://openai.com/searchbot.json — IP range file, URL confirmed, not fetched (content not pulled this pass)
- https://openai.com/chatgpt-user.json — IP range file, URL confirmed, not fetched
- https://openai.com/adsbot.json — IP range file, URL confirmed, not fetched
- https://github.com/FabrizioCafolla/openai-crawlers-ip-ranges — third-party IP range mirror, found via WebSearch, not fetched

## Crawler identity — Anthropic

- https://support.claude.com/en/articles/8896518 — primary crawler docs, fetched
- https://claude.com/crawling/bots.json — IP range file, URL confirmed via fetched page, not independently re-fetched as raw JSON

## Crawler identity — Perplexity

- https://docs.perplexity.ai/docs/resources/perplexity-crawlers — primary crawler docs, fetched
- https://www.perplexity.com/perplexitybot.json — IP range file, URL confirmed, not fetched
- https://www.perplexity.com/perplexity-user.json — IP range file, URL confirmed, not fetched
- https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ — Cloudflare's Aug 2025 report, fetched, methodology and findings quoted
- https://tech.slashdot.org/story/25/08/04/1459240/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives-cloudflare-says — press relay, found via WebSearch, not fetched
- https://cybersecuritynews.com/cloudflare-accuses-perplexity-ai-for-evading-firewalls/ — press relay, not fetched
- https://winbuzzer.com/2025/08/04/cloudflare-accuses-perplexity-of-using-stealth-crawlers-to-evade-web-standards-xcxwbn/ — press relay, not fetched
- https://www.searchenginejournal.com/cloudflare-delists-and-blocks-perplexity-from-crawling-websites/552899/ — press relay re: Cloudflare delisting Perplexity from verified-bot program, not fetched

## Crawler identity — Google

- https://developers.google.com/search/docs/appearance/ai-features — primary AI-features doc, fetched
- https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests — primary rDNS verification instructions, fetched
- https://www.muratulusoy.de/en/glossary/google-extended.html — third-party glossary entry on Google-Extended, found via WebSearch, not fetched

## Crawler identity — Amazon, Apple, Meta, ByteDance, Common Crawl

- https://developer.amazon.com/amazonbot — primary Amazonbot docs, fetched
- https://developer.amazon.com/amazonbot/ip-addresses/ — Amazon IP range page, URL confirmed via fetched page, not independently fetched
- https://support.apple.com/en-us/119829 — primary Applebot / Applebot-Extended docs, fetched
- https://developers.facebook.com/docs/sharing/webmasters/web-crawlers/ — primary Meta-ExternalAgent / Meta-ExternalFetcher docs, fetched
- https://commoncrawl.org/ccbot — primary CCBot docs, fetched
- https://index.commoncrawl.org/ccbot.json — CCBot IP range file, URL confirmed via fetched page, not independently fetched
- Bytespider — no ByteDance-published documentation page located; negative finding, checked WebSearch 2026-09-16

## Verification method (rDNS / IP / geo)

- https://gist.github.com/NovCog/1733e3c161a9faa7de674addfe878ebd — third-party FCrDNS explainer, found via WebSearch, not fetched
- https://searchengineland.com/guide/what-is-googlebot-fraud — third-party guide, found via WebSearch, not fetched
- https://geoiphub.com/blog/verify-ai-crawler-bot-by-ip-rdns-cidr-web-bot-auth — third-party guide on verifying AI bots via rDNS/CIDR/Web Bot Auth, found via WebSearch, not fetched

## Cloudflare / Fastly / Akamai infrastructure and traffic-share reporting

- https://blog.cloudflare.com/introducing-pay-per-crawl/ — primary announcement, fetched
- https://developers.cloudflare.com/ai-crawl-control/ — primary product overview, fetched
- https://developers.cloudflare.com/ai-crawl-control/features/pay-per-crawl/use-pay-per-crawl-as-ai-owner/verify-ai-crawler/ — Web Bot Auth verification doc, found via WebSearch, not fetched
- https://developers.cloudflare.com/changelog/2025-12-10-pay-per-crawl-enhancements/ — changelog entry, found via WebSearch, not fetched
- https://techcrunch.com/2025/07/01/cloudflare-launches-a-marketplace-that-lets-websites-charge-ai-bots-for-scraping/ — press coverage, not fetched
- https://stackoverflow.blog/2026/02/19/stack-overflow-cloudflare-pay-per-crawl/ — case study, not fetched
- https://radar.cloudflare.com/reports/ai-crawl-control-2026 — attempted direct fetch of Cloudflare Radar report, returned HTTP 403, not obtained
- https://technologychecker.io/blog/ai-crawler-statistics — third-party analysis of Cloudflare Radar data, fetched, percentages quoted
- https://technologychecker.io/blog/robots-txt-ai-crawlers-blocking-report — related third-party analysis, found via WebSearch, not fetched
- https://technologychecker.io/blog/bot-traffic-statistics — related third-party analysis, found via WebSearch, not fetched
- https://technologychecker.io/blog/web-traffic-statistics — related third-party analysis, found via WebSearch, not fetched
- https://www.digitalapplied.com/blog/ai-crawler-bot-traffic-statistics-2026-data-reference — third-party stats compilation, found via WebSearch, not fetched
- https://nobori.ai/blog/crawl-to-refer-ratio-ai-crawler-traffic-b2b-2026 — third-party crawl-to-referral-ratio analysis, found via WebSearch, not fetched
- https://www.alphamatch.ai/blog/ai-crawlers-drain-web-economy-on-premise-ai-2026 — third-party analysis, found via WebSearch, not fetched
- https://workos.com/blog/ai-agent-web-traffic-what-developers-need-to-change — third-party analysis, found via WebSearch, not fetched
- https://www.akamai.com/newsroom/press-release/akamai-research-commerce-becomes-the-epicenter-for-ai-bot-attacks-and-agentic-fraud-in-2026 — primary Akamai press release, fetched, stats quoted
- https://www.akamai.com/resources/infographic/fraud-and-abuse-report-2025 — related Akamai infographic, found via WebSearch, not fetched
- https://www.akamai.com/blog/security/ai-pulse-how-ai-bots-agents-will-shape-2026 — related Akamai blog post, found via WebSearch, not fetched
- Fastly bot-traffic report — exact primary blog URL not captured before WebSearch budget was exhausted; relayed statistics only, checked 2026-09-16, flagged for pass 3 to fetch directly

## Live retrieval vs index — architecture

- https://blog.google/products/search/ai-mode-search/ — primary Google AI Mode announcement, fetched
- https://blog.google/company-news/inside-google/googlers/how-google-ai-visual-search-works/ — primary Google explainer (query fan-out), fetched
- https://claude.com/blog/web-search-api — primary Anthropic web-search-tool announcement, fetched
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool — Claude platform docs, found via WebSearch, not independently fetched
- https://www.perplexity.ai/hub/getting-started — attempted fetch for Perplexity's own retrieval description, returned HTTP 403, not obtained
- https://ziptie.dev/blog/how-perplexity-ai-answers-work/ — third-party description of Perplexity's RAG pipeline, found via WebSearch, not fetched
- https://medium.com/@kazkozdev/how-perplexity-actually-searches-the-internet-ae4b50dd9837 — third-party description, found via WebSearch, not fetched
- https://rankly.substack.com/p/how-microsoft-copilot-search-works — third-party description of Bing Copilot / Prometheus grounding, found via WebSearch, not fetched
- Microsoft's own engineering blog on Copilot/Prometheus grounding — not located within this pass's search budget; negative finding, checked WebSearch 2026-09-16

## Measurement literature — Part 3

- https://arxiv.org/abs/2406.03589 — Pfrommer et al., EMNLP 2024, fetched, abstract quoted
- https://github.com/spfrommer/cse-ranking-manipulation — companion code repo, fetched, methodology quoted
- https://arxiv.org/abs/2406.18382 — Nestaas, Debenedetti, Tramèr, fetched, abstract quoted
- https://edoardo.science/ — author homepage, found via WebSearch, not fetched
- https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag — primary USENIX listing, fetched
- https://github.com/thisxyz/PoisonedRAG — companion code repo, fetched
- https://arxiv.org/abs/2402.07867 — PoisonedRAG arXiv preprint, referenced, not independently re-fetched (abstract obtained via the USENIX listing fetch instead)
- https://pure.psu.edu/en/publications/poisonedrag-knowledge-corruption-attacks-to-retrieval-augmented-g/ — Penn State repository record, found via WebSearch, not fetched
- https://arxiv.org/abs/2311.09735 — GEO: Generative Engine Optimization, KDD 2024, fetched, abstract quoted
- https://dl.acm.org/doi/10.1145/3637528.3671900 — KDD ACM DL record for GEO paper, found via WebSearch, not fetched
- https://arxiv.org/abs/2602.16752 — LLM Rankers Vulnerability paper, fetched, abstract quoted
- https://doi.org/10.1145/3805712.3808553 — SIGIR 2026 proceedings DOI for the same paper (embedded prompt-injection joke in title), found via WebSearch, not fetched
- https://arxiv.org/html/2605.29107 — GEO-Bench: Benchmarking Ranking Manipulation in GEO, found via WebSearch, not fetched — candidate for pass 3
- https://arxiv.org/pdf/2605.28017 — "Can It Reach the Generator?" prompt-injection survival in RAG, found via WebSearch, not fetched — candidate for pass 3
- https://arxiv.org/pdf/2509.18575 — "The Ranking Blind Spot: Decision Hijacking in LLM-based Text Ranking," found via WebSearch, not fetched — candidate for pass 3
- https://arxiv.org/html/2509.23519 — ReliabilityRAG defense paper, found via WebSearch, not fetched — candidate for pass 3
- https://arxiv.org/pdf/2508.18652 — UniC-RAG universal knowledge-corruption attacks, found via WebSearch, not fetched — candidate for pass 3
- https://arxiv.org/pdf/2411.18948 — RevPRAG poisoning-detection via activation analysis, found via WebSearch, not fetched — candidate for pass 3

## Policy and legal boundary — Part 4

- https://developers.google.com/search/docs/essentials/spam-policies — primary Google spam policy, fetched, spam/cloaking/enforcement definitions quoted
- https://developers.google.com/search/docs/appearance/spam-updates — primary Google spam-policy changelog, fetched, date-confirmation attempt (inconclusive — see raw pulls)
- https://developers.google.com/search/blog/2011/11/was-ist-cloaking — Google Search Central blog cloaking post, fetch attempted, returned only navigation/archive shell, not article text
- https://developers.google.com/search/blog/2026/04/back-button-hijacking — related spam-policy blog post, found via WebSearch, not fetched
- https://developers.google.com/search/blog/2024/11/site-reputation-abuse — related spam-policy blog post, found via WebSearch, not fetched
- https://searchengineland.com/google-updates-search-spam-policies-to-clarify-it-applies-to-generative-ai-responses-477657 — press coverage of the May 2026 policy change, not fetched
- https://mwm.ai/articles/google-updates-spam-policy-to-counter-ai-search-manipulation-in-may-2026 — press coverage, not fetched
- https://winbuzzer.com/2026/05/17/google-search-spam-policy-ai-overviews-ai-mode-manipulation-xcxwbn/ — press coverage naming 2026-05-15, not fetched
- https://mlq.ai/news/googles-revised-spam-rules-draw-industry-focus-to-ai-answer-manipulation-risks/ — press coverage, not fetched
- https://policies.google.com/terms — primary Google ToS, fetched, automated-access clause quoted
- https://openai.com/policies/usage-policies/ — attempted fetch, HTTP 403, not obtained
- https://openai.com/policies/usage-policies — attempted fetch (no trailing slash), HTTP 403, not obtained
- https://openai.com/policies/row-terms-of-use/ — attempted fetch, HTTP 403, not obtained
- https://openai.com/policies/service-terms/ — found via WebSearch, not fetched
- https://openai.com/policies/using-chatgpt-agent-in-line-with-our-policies/ — found via WebSearch, not fetched
- https://developers.openai.com/api/docs/guides/rate-limits — found via WebSearch, not fetched
- https://www.perplexity.ai/hub/legal/terms-of-service — attempted fetch, HTTP 403, not obtained
- https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service-search — attempted fetch, HTTP 403, not obtained
- https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service — found via WebSearch, not fetched
- https://link.axios.com/click/... (Wired, "Amazon Is Investigating Perplexity Over Claims of Scraping Abuse") — press relay, tracking-link URL, not fetched directly
- https://www.engadget.com/amazon-investigating-perplexity-ai-after-accusations-it-scrapes-websites-without-consent-133003374.html — press coverage, not fetched
- https://www.pymnts.com/artificial-intelligence-2/2025/perplexitys-agents-crash-amazons-gate-and-spark-a-legal-showdown/ — press coverage, not fetched
- https://www.sdxcentral.com/news/perplexity-insists-ai-agents-are-not-scrapers-in-amazon-spat/ — press coverage, not fetched
- https://www.yahoo.com/news/articles/amazon-sues-perplexity-ai-covert-102252600.html — press coverage of the lawsuit, not fetched
- https://llmstxt.org/ — primary llms.txt specification, fetched
- https://searchengineland.com/llms-txt-proposed-standard-453676 — press coverage of llms.txt, not fetched
- https://www.pravinkumar.co/blog/w3c-llms-txt-standard-proposal-june-2026-webflow-2026 — coverage of a reported W3C llms.txt standardization proposal (June 2026), found via WebSearch, not fetched — worth primary-source confirmation in pass 3
- schema.org itself (https://schema.org/) — not fetched directly; treated via secondary SEO-industry summaries only

## Not fetched — open for pass 3

- OpenAI, Perplexity ToS/usage-policy pages: all four attempted URLs returned HTTP 403 to the fetch tool. Needs either a different fetch method (authenticated browser tool, or `curl` from an environment not blocked) or accepting secondary-source relay as the ceiling of verification.
- Fastly's own bot-traffic report page: exact URL never captured before WebSearch budget (200/200) was exhausted this session. Statistics currently rest on a WebSearch summary only.
- Cloudflare Radar's own report/dashboard pages (radar.cloudflare.com): direct fetch returned HTTP 403; all Radar-sourced numbers in this pass are third-party re-reporting (technologychecker.io), not Cloudflare's own page text.
- ByteDance Bytespider: confirmed as having no located vendor documentation page — worth one more explicit check (ByteDance developer portal, if one exists) before calling this permanently unconfirmed.
- W3C llms.txt standardization: one WebSearch snippet claims a June 2026 W3C working draft. Not verified against w3.org directly.
- The exact 2026-05-15 effective date for Google's generative-AI-response spam-policy wording: confirmed only via secondary press; Google's own spam-updates changelog page did not show a matching entry as fetched.
- W3C/IETF Web Bot Auth spec itself (the mechanism underlying Cloudflare pay-per-crawl and verified bots) — not fetched as a primary IETF/W3C draft in this pass.
- Six candidate 2025-2026 arXiv papers on RAG poisoning/ranking-manipulation defenses and benchmarks, listed above under "Measurement literature," found by title/URL only via WebSearch and not yet fetched or read.
- Amazon Rufus's own technical documentation on how it selects/cites sources (as distinct from Amazonbot crawler docs) — not located or fetched this pass.
- Microsoft's own (not third-party) engineering documentation of Bing Copilot / Prometheus grounding architecture — not located within this pass's search budget.
