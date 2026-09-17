# ai-search-ads — AI search visibility, ads, injection testing

Pass 1, 2026-09-16. Compiled from `../raw/ai-search-ads-pulls.md` (23 source blocks) and `../raw/ai-search-ads-source-index.md` (64 URLs). Competitors: `../competitors/ai-search-ads-roster.md`.

The idea splits in two. Research covered both because they share a mechanism and share nothing else.

- **(A) Marketing read** — GEO / AI search visibility. Does my brand appear in AI answers, can I buy ads there. Buyer: brand and SEO teams.
- **(B) Adversarial read** — injection testing. Can an answer be manipulated, who audits that. Buyer: SOC / security, or the engine itself.

## Market

Buyer, read A: brand and SEO teams. Vendor and blog framing only — no procurement-title study found (unknown — checked WebSearch 2026-09-16).

Buyer, read B: SOC teams. ZeroFox, CrowdStrike and Vectra frame AI-answer poisoning as malware and phishing distribution, not brand visibility. **No buyer found bridging A and B.** The two literatures do not cite each other in anything pulled.

| Figure | Value | Label |
|---|---|---|
| AI Search Visibility Services market | $4.39B (2026) to $10.72B (2031), 19.55% CAGR | analyst-derived, Mordor Intelligence |
| Marketing leaders raising GEO spend in 2026 | 94% | vendor/survey-derived, primary survey unidentified |
| Enterprise digital marketing budget on AI search optimization | 12% average | vendor/survey-derived, primary unidentified |
| Leaders who cannot measure AI-answer visibility | 45%; only 9% have full-metric tools | vendor/survey-derived |
| Semrush AI Visibility Index base | 126M US prompts, Jan–Apr 2026, 22 industries | company-stated, Semrush is itself a vendor |

## Available solutions

Read A is served. Ten-plus near-identical tools, price spread $29/mo to $828/mo all-in.

| Tool | Does | Price | Free tier |
|---|---|---|---|
| Otterly AI | Mentions and citations, 4 engines, GEO URL audits | Lite $29 / Standard $189 / Premium $489 / Ent. from $1,000 | **verified 2026-09-16** |
| Rankscale AI | LLM visibility for solo SEOs, schema audits | from ~€20/mo | not confirmed |
| Peec AI | Brand visibility across AI engines | Starter / Pro / Advanced / Enterprise — **no figures render** | unknown — checked peec.ai/pricing 2026-09-16 |
| Profound | Enterprise visibility and optimization | **Free trial and Enterprise/custom only** — no self-serve tier | **verified 2026-09-16** |
| SE Ranking | Prompt-based LLM rank tracking | $129–$279/mo | unknown |
| Writesonic | Content gen + visibility tracking | $79–$399/mo annual | unknown |
| Goodie AI | High-volume prompt testing, 11+ models, Amazon Rufus | $495/mo | unknown |
| AthenaHQ | GEO visibility platform | Free ($25 credit) / **Starter $295** / Enterprise custom | **verified 2026-09-16** |
| Ahrefs Brand Radar | Visibility add-on | Custom Prompts from $50; AI Visibility Index $199; **$699 all models** | **verified 2026-09-16** |
| Garak, Promptfoo, PyRIT, DeepTeam | Open-source LLM red-teaming | free | yes |

Read B is not served by a product. Open-source red-team frameworks can be pointed at it; none is marketed for AI-search-answer integrity.

## Ad formats in AI answers, as of 2026-09

Not a stable market. One major platform exited while four expanded.

| Platform | Format | Status | Money |
|---|---|---|---|
| Perplexity | Sponsored follow-up questions | **Exited Feb 2026**, subscription-only, targeting $500M ARR | was CPM over $50, 15-sector exclusivity |
| OpenAI ChatGPT | Sponsored card under response, labeled | Live Feb 9 2026 US free tier; self-serve Ads Manager May 5 2026; UK, Mexico, Brazil, Japan, South Korea by Aug 11 2026 | $1B annualized run rate in under 200 days (company-stated, not filed) |
| Google | AI Overviews uses existing Search/Shopping/PMax. AI Mode adds Conversational Discovery + Highlighted Answers (announced May 20 2026) | Live, staged rollout | standard Google Ads auction |
| Microsoft Copilot | Sponsored responses, Copilot Checkout in-chat purchase | GA since 2025, expanding | 15–25% higher CTR vs traditional search ads (partner-stated) |
| Amazon Rufus | Sponsored Products Prompts, Sponsored Brands Prompts | GA US Mar 25 2026 | CPC per leaked pitch deck, unconfirmed by Amazon; 250M users claimed |

## Injection and manipulation

Works, published, and now policed.

- **Demonstrated**: arXiv 2406.03589 (Pfrommer et al., EMNLP 2024) — tree-of-attacks prompt injection reliably promoted low-ranked products and **transferred to live perplexity.ai**. Peer-reviewed.
- **Active research**: arXiv 2602.16752 on LLM ranker vulnerability to prompt injection (abstract only, not fetched directly).
- **Standardized**: OWASP Top 10 for LLM Apps 2025 ranks prompt injection #1 (LLM01) for the second edition running; RAG and vector poisoning is LLM08, data and model poisoning LLM04.
- **Confirmed in the wild by the platform owner**: Google reported 32% relative rise in malicious-category detections Nov 2025 to Feb 2026 (journalist-relayed). Google's spam policy names "attempting to manipulate generative AI responses in Google Search" as spam, enforceable by demotion or removal — wording confirmed on the primary page 2026-09-16, `Last Updated: 2026-08-28`. The **2026-05-15** effective date is secondary-press only and unconfirmed against Google's changelog. See `../findings/injection-feasibility.md`.
- **Adjacent but different control point**: Cloudflare AI Crawl Control, TollBit ($24M Series A) gate *whether* crawlers get the content. Neither addresses manipulation of content already crawled.

Consequence for a build: the offensive technique is public and now against platform policy. The defensible product is the audit and the defense, not the injection.

## Technical knowhow

| Capability | Public? | Difficulty | Note |
|---|---|---|---|
| Sampling AI answers at scale | yes | moderate, ops-heavy | Answers vary run to run. Thousands of prompts needed. Must hit UI and API — UI-only elements (tables, maps) missed by API alone |
| Multi-engine coverage | yes | scope problem, not research | ChatGPT, Gemini, AI Mode, AI Overviews, Perplexity, Claude, Copilot, Rufus. Table stakes |
| Statistical attribution to traffic and revenue | unsolved industry-wide | hard | 45% of leaders say they cannot measure it. No tool found convincingly claiming it is closed |
| Injection payload research | yes, academic + OWASP | moderate | Documented, not a moat |

Build-vs-buy for a would-be customer reportedly flips around 50,000 queries/month or 10+ clients (third-party estimate, not vendor-benchmarked) — that number is also the wall a new tracking entrant hits.

Moat candidates: proprietary prompt and response corpus at scale (Semrush claims 126M prompts), enterprise distribution and trust (Profound's Fortune 500 logos), or depth in injection defense (nobody productizing it — candidate whitespace, not a demonstrated moat).

## Gaps

- **No productized injection audit for AI-search answers.** Neither brand-side ("can a competitor inject content to outrank us") nor engine-side ("can our RAG pipeline be steered by page content"). Closest substitutes are general-purpose red-team frameworks. Clearest gap found.
- **The two literatures are disconnected.** Marketing GEO and security threat-intel treat the same mechanism and do not cite each other. Adversarial angle under-served from the marketing side.
- **Attribution unsolved.** The industry's own stated pain point, no credible closer found.
- **Tracking is commoditizing.** Overlapping features, visible price competition. Differentiation thin — persona-based prompts (Gumshoe.AI) is a rare exception.
- **Ad inventory unstable.** Perplexity exited while OpenAI, Google, Microsoft and Amazon expanded. Not yet a comparable market across platforms.

## Caveats

- Most pricing came from third-party comparison blogs, not vendor pricing pages. peec.ai, tryprofound.com/pricing, athenahq.ai, ahrefs.com not fetched directly. One comparison source (tryprofound.com) reviews its own competitors.
- **Pass 2 correction:** Profound's own page as of 2026-09-16 shows no public self-serve tier — free trial and Enterprise only. Pass 1's $99/$399/$499 figures came from aggregators and do not appear on the vendor page. Whether the tiers were withdrawn or never existed is undetermined. Semrush's AI-visibility product is now "Semrush One" with no separate public price — unknown, checked 2026-09-16.
- **Resolved, both correct:** $1B was the Series C valuation ($96M, 2026-02-24, Lightspeed). **$1.8B is the Series D — $180M, announced 2026-09-16, led by Sequoia and Kleiner Perkins** (company blog). Sequential rounds, never a conflict.
- **Resolved:** Peec AI's own blog names Daniel Drabo, Tobias Siwonia and Marius Meiners. TechCrunch was right; Tracxn's "Gorbacheva" is an error.
- **Peec AI ARR corrected:** the company's own post (2025-11-18) states **"$0 to $4M+ ARR in 10 months"**, 1,300+ brands, 300+ customers/month. The $10M ARR figure has no traceable source — do not use. $29M total funding confirmed as €7M seed (20VC, Jul 2025) plus $21M Series A (2025-11-18, Singular).
- Google spam-policy wording is journalist-paraphrased. Not checked against Google's own policy page.
- ChatGPT Ads run rate and Amazon Rufus figures are press and pitch-deck sourced. Claimed, not filed.
- Several survey stats (94%, 12%, 65%, 45%, 9%) could not be traced to a named primary survey.
- Headcount unknown for most vendors except Profound (~62, 2025).
