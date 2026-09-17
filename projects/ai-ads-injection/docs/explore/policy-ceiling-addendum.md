# Policy ceiling addendum — wave 1b, five gaps

2026-09-17. Closes exactly the five documents wave 1 (`policy-ceiling.md`, `carrier-state.md`) could not reach: OpenAI Business Terms/Services Agreement, Perplexity API ToS, OpenAI ads terms, Bing/Copilot webmaster and content policy, Vietnam Law on Advertising + current amendment. Does not duplicate or edit `policy-ceiling.md` — that file is wave 1's and stands as written.

**Tool note.** The Chrome browser extension (`mcp__claude-in-chrome__*`) — the tool this task was built around — never connected this session (`tabs_context_mcp` failed 4 times: "Browser extension is not connected"). Every document below was instead pulled by direct `curl`/`WebFetch`, and where that 403'd or hit a JS shell, by the Wayback Machine (`web.archive.org`) via `curl`, or by locating the primary PDF/HTML the live site's SPA wraps. This is a materially different method than the browser extension the brief specified, recorded per-document below. One page (Bing's live Webmaster Guidelines) was never reached by any method tried — see Gap 4.

---

## Gap 1 — OpenAI Business Terms / Services Agreement (the actual API-governing contract)

**Finding: the four documents that together govern API customers were all located and read. None of them addresses crawler cloaking. This narrows, but does not close, pass 2's "API path is not closed" question — see synthesis below.**

### Document 1: OpenAI Services Agreement (= "Business Terms")
- URL: `https://openai.com/policies/business-terms/` (canonical `https://openai.com/policies/services-agreement/`)
- Dates on page: **"Updated: December 1, 2025" / "Effective: January 1, 2026"**
- Pulled: Wayback snapshot archived 2026-09-12 20:29:46 UTC (direct fetch 403/JS-challenge on every attempt, incl. Googlebot UA). Raw: `raw/openai-services-agreement.txt`

Operative sentences, verbatim:

> "This OpenAI Services Agreement only applies to use of OpenAI's APIs, ChatGPT Enterprise, ChatGPT Business, ChatGPT for Clinicians, and other services for customers who are businesses and developers, and does not apply to OpenAI services used by consumers or individuals unless specified above."

> "'OpenAI Policies' means the Service-Specific Terms, Sharing and Publication Policy, and Usage Policies."

No occurrence of "cloak," "crawl," or "advertis[e]" anywhere in the document.

### Document 2: OpenAI Usage Policies
- URL: `https://openai.com/policies/usage-policies/`
- Date on page: **"Effective: October 29, 2025"**
- Pulled: Wayback snapshot archived 2026-05-31 20:21:05 UTC — the most recent one that returned HTTP 200; snapshots from Dec 2025, Jan 2026, and Sep 2026 for this exact URL all returned 403 **inside the Wayback capture itself**, not just to us. Raw: `raw/openai-usage-policies.txt`

Operative sentences, verbatim:

> "we don't allow our services to be used to manipulate or deceive people, to interfere with their exercise of human rights, to exploit people's vulnerabilities, or to interfere with their ability to get an education or access critical services, including any use for: academic dishonesty, deceit, fraud, scams, spam, or impersonation"

### Document 3: OpenAI Sharing & Publication Policy
- URL: `https://openai.com/policies/sharing-publication-policy/`
- Date on page: **"Updated: November 14, 2022"**
- Pulled: Wayback snapshot archived 2026-09-08 18:25:03 UTC. Raw: `raw/openai-sharing-publication-policy.txt`

Operative sentence, verbatim:

> "The role of AI in formulating the content is clearly disclosed in a way that no reader could possibly miss, and that a typical reader would find sufficiently easy to understand."

### Document 4: OpenAI Service Terms
- URL: `https://openai.com/policies/service-terms/`
- Date on page: **"Updated: September 10, 2026"** (most recently updated of the four)
- Pulled: Wayback snapshot archived 2026-09-11 15:24:25 UTC. Raw: `raw/openai-service-terms.txt`

Operative sentence, verbatim (this is the sentence pass 2 already found and correctly characterized as thin):

> "Customer will only, and will ensure that its End Users only, use APIs in accordance with the applicable documentation at https://platform.openai.com/docs"

### Mapping table

| Quoted provision | Governs whom | (a) differential content to crawlers | (b) paid placement in retrieved content | (c) commercial measurement of retrieval |
|---|---|---|---|---|
| Services Agreement scope clause | OpenAI's business/developer customers only | Silent — not a party to this contract unless you're an API customer | Silent | Silent |
| Usage Policies "manipulate or deceive people" | What a customer may build with the API/ChatGPT | Arguable only if the *customer itself* is doing the cloaking with OpenAI's product; does not reach a non-customer website GPTBot crawls | Same — reaches customer's own downstream deception, not a third party's page | Silent |
| Sharing & Publication "role of AI... clearly disclosed" | Creator who co-authors with the API and publishes | Silent | Governs AI authorship disclosure, not payment disclosure — different duty | Silent |
| Service Terms "use APIs in accordance with... documentation" | API customers generally | Silent | Silent | Silent |

### Read for the plan phase (synthesis, not in policy-ceiling.md)

Pass 2's error was reading the *consumer* Terms of Use and the thin Service Terms page and concluding "the API path isn't closed." This pass reads the actual controlling stack (Services Agreement → incorporates Usage Policies, Sharing & Publication Policy, Service-Specific Terms) in full, and the conclusion is narrower than either "closed" or "open": **none of these four documents contains a cloaking/differential-serving rule, because none of them is written to a website operator's relationship with GPTBot/ChatGPT-User/OAI-SearchBot at all — they are written to OpenAI's own customers.** A company that is simultaneously (1) an OpenAI API customer and (2) the operator of a website that cloaks content for OpenAI's crawlers is bound by the Usage Policies' broad "don't deceive people" clause only insofar as the two facts are the same conduct — a link this pass did not find any OpenAI document draw explicitly. If the site owner is *not* an OpenAI customer at all (the more likely case for the idea's target segment), none of these four documents apply to them by their own terms.

---

## Gap 2 — Perplexity API Terms of Service

**Finding: fetched, along with the two documents it incorporates by reference. Same structural result as Gap 1 — no cloaking-specific language anywhere in the API contract stack.**

### Document 1: Perplexity API Terms of Service
- URL: `https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service`
- Date on page: **"Last updated: January 23, 2026"**
- Pulled: Wayback snapshot archived 2026-08-29 22:43:06 UTC (direct fetch 403). Raw: `raw/perplexity-api-terms-of-service.txt`

Operative sentence, verbatim:

> "2.4 Acceptable Use Policy. Customer has no right or license to, and shall not (nor permit others, including end users of the Customer Applications, to), directly or indirectly use the Services, Outputs or API Platform in a manner that violates Perplexity's Acceptable Use Policy ('AUP')... (which is hereby incorporated into this Agreement by reference)."

### Document 2: Perplexity Acceptable Use Policy (incorporated by reference)
- URL: `https://www.perplexity.ai/hub/legal/aup`
- Date on page: **"Last updated: July 8th, 2025"**
- Pulled: Wayback snapshot archived 2026-08-09 06:40:57 UTC. Raw: `raw/perplexity-aup.txt`

Operative sentences, verbatim:

> "Create content that you subsequently claim was created solely by humans, or otherwise misrepresent the provenance of information or content; or provide chatbot services without disclosing to end users that they are interacting with AI (unless it is obvious from the context);" [listed as a prohibited use]

> "Remove watermarks, metadata or other indicia intended to identify outputs as artificially generated or manipulated, or circumvent abuse protections or safety filters, whether Perplexity's or those of a third party;" [prohibited]

> "Create or make available any products or services competitive with, similar to, or that would otherwise be a substitute for the Services... except with Perplexity's express prior written permission" [prohibited]

### Document 3: Perplexity Search Addendum (governs the raw `/search` API endpoint)
- URL: `https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service-search`
- Date on page: **"Last updated: September 22, 2025"**
- Pulled: Wayback snapshot archived 2025-10-12 21:34:32 UTC — this is the most recent snapshot found; not independently re-verified against a live 2026-09 date. Raw: `raw/perplexity-search-api-addendum.txt`
- Content: this endpoint "retrieves and returns search results (e.g., snippets, URLs, page titles and associated metadata) from an index of public content" and "does not generate Output through the use of artificial intelligence." No cloaking, disclosure, or publisher-facing language of any kind.

### Mapping table

| Quoted provision | Governs whom | (a) differential content to crawlers | (b) paid placement in retrieved content | (c) commercial measurement of retrieval |
|---|---|---|---|---|
| AUP "misrepresent the provenance... or otherwise" | Customer's own use of Output | Silent | Governs claiming AI content is human-made, not a third party's cloaked page | Silent |
| AUP "provide chatbot services without disclosing... AI" | Customer's own downstream chatbot product | Silent | Silent | Silent |
| AUP "competitive with... the Services" | Customer's product vs. Perplexity's own product | Silent | Silent | Only tangential restriction found; a genuine audit/measurement tool is not "competitive with" Perplexity on its face |
| Search Addendum scope | Customers of the raw `/search` endpoint | Silent | Silent | Silent |

**No provision anywhere in the API ToS, AUP, or Search Addendum addresses a website serving different content to PerplexityBot/Perplexity-User than to human visitors.** Same structural gap as OpenAI: these are OpenAI's/Perplexity's contracts with *their* customers, not a code of conduct for the websites their crawlers fetch.

---

## Gap 3 — OpenAI ads terms / ad-product policy

**Finding: CLOSED. Contrary to the brief's fallback instruction ("if no such document is public, record that as a finding"), a full, dated, substantive set of documents exists and was fetched. The correct slugs are `ad-policies` and `advertising-terms` — not `ads-terms`, which both wave 1 and this pass tried first and both got 403.**

### Document 1: OpenAI Ad policies
- URL: `https://openai.com/policies/ad-policies/`
- Date on page: **"Updated: August 10, 2026"**
- Pulled: Wayback snapshot archived 2026-08-18 15:48:37 UTC. Raw: `raw/openai-ad-policies.txt`

Operative sentences, verbatim:

> "Ads must be clearly distinguishable from the ChatGPT product experience. We may remove or require modification of ads that imitate the appearance, functionality, or voice of ChatGPT or other OpenAI interfaces in a way that could reasonably cause users to believe the ad is part of the product."

> "Ads must be truthful and not misleading, including unfounded claims about capabilities, pricing, outcomes, affiliations, or comparisons with other products or companies. Ads that exaggerate results, use false endorsements, or otherwise deceive users are prohibited regardless of category."

### Document 2: OpenAI Advertising Terms
- URL: `https://openai.com/policies/advertising-terms/`
- Date on page: **"Updated: June 12, 2026"**
- Pulled: Wayback snapshot archived 2026-08-18 21:49:26 UTC. Raw: `raw/openai-advertising-terms.txt`

Operative sentence, verbatim:

> "Without limiting your obligations to apply disclosures or disclaimers to your Ads, OpenAI may apply disclosures or disclaimers to Ads as may be required under applicable law, under the OpenAI Policies or in OpenAI's sole discretion."

### Documents 3 & 4: Ad Tools Terms and Ad Tools DPA (fetched, lower relevance)
- `https://openai.com/policies/ad-tools-terms/` and `https://openai.com/policies/ad-tools-dpa/` ("Effective: June 12, 2026"). Raw: `raw/openai-ad-tools-terms.txt`, `raw/openai-ad-tools-dpa.txt`. These govern a separate self-serve "Ad Tools" product and its data processing; no cloaking or paid-placement-disclosure language beyond what's quoted above.

### Mapping table

| Quoted provision | (a) differential content to crawlers | (b) paid placement in retrieved content | (c) commercial measurement of retrieval |
|---|---|---|---|
| "Ads must be clearly distinguishable from the ChatGPT product experience" | Silent — governs OpenAI's own bought-ad surface, not organic retrieval | **Directly answers, for the bought-ads channel only**: an ad that reads as ChatGPT's native answer is expressly barred | Silent |
| "Without limiting your obligations to apply disclosures... to your Ads" | Silent | **Contractually mandates advertiser-side disclosure** for anything purchased through OpenAI's Advertising Services | Silent |

**Caveat — this closes a different channel than the one the idea targets.** These documents govern paid placements *bought from OpenAI* to appear as a labeled ad unit inside ChatGPT. The ai-ads-injection mechanism is about a website's *organic* content being retrieved and paraphrased by ChatGPT with no ad purchased from OpenAI at all — Ad Policies and Advertising Terms do not reach that scenario by their own stated scope (they define "Ads," "Orders," "Destinations" as things submitted to and accepted by OpenAI). The disclosure principle they establish (paid content that could be mistaken for native product output must be distinguishable) is the closest analog found in any OpenAI document to what would need to exist to reach the idea's mechanism — but it does not, on its text, reach it.

---

## Gap 4 — Bing / Copilot webmaster and content policy on cloaking

**Finding: PARTIALLY CLOSED. The live guidelines page itself could not be read by any method available this session — record that failure honestly. A genuine primary source (Bing's own 2018 blog post, not behind the SPA) supplies the baseline cloaking test. A reliable secondary source (Search Engine Journal) corroborates that the live guidelines were substantively rewritten in ~March 2026 for AI/Copilot, but the exact current wording remains unread.**

### Live page: unreachable
- URL: `https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a`
- Tried: direct curl (HTTP 200 but pure JS shell, "You need to enable JavaScript to run this app."); direct curl with Googlebot UA (same); WebFetch (confirms no body text retrievable); Wayback Machine at five different points in time — 2021-02-05, 2022-01-29, 2024-01-01, and two 2026-09 captures — **every single one is the same JS shell**. This is a genuinely client-rendered SPA that no non-JS-executing method reaches; the browser extension this task was built for is exactly the missing tool, and it never connected. Raw (negative-finding record): `raw/bing-webmaster-guidelines-live-attempt.txt`.
- `unknown — checked bing.com direct + Wayback (5 timestamps) + WebFetch, 2026-09-17, browser extension unavailable all 4 connection attempts`

### Primary source found instead: Bing Webmaster Blog, October 31, 2018
- URL: `https://blogs.bing.com/webmaster/october-2018/bingbot-Series-JavaScript,-Dynamic-Rendering,-and-Cloaking-Oh-My`
- Authored by Fabrice Canel and Frédéric Dubut, Program Managers, Microsoft Bing (named, on-the-record)
- This Bing blog subdomain is server-rendered and not behind the SPA wall that blocks the guidelines page itself
- Raw: `raw/bing-blog-cloaking-2018.txt`

Operative sentences, verbatim:

> "Dynamic rendering is about detecting user agent and rendering content differently for humans and search engine crawlers."

> "The good news is that as long as you make a good faith effort to return the same content to all visitors, with the only difference being the content is rendered on the server for bots and on the client for real users, this is acceptable and not considered cloaking."

### Secondary source (reliable): Search Engine Journal, 2026, Matt Southern
- URL: `https://www.searchenginejournal.com/bing-adds-geo-to-official-guidelines-expands-ai-abuse-definitions/568442/`
- Raw: `raw/sej-bing-geo-guidelines-update.txt`

Verbatim quotes SEJ attributes to Bing's live (rewritten) guidelines page:

> Old wording (per SEJ, quoting the pre-rewrite guidelines): "Machine-generated content is information that is generated by an automated computer process, application, or other mechanisms without any active intervention of a human. Content like this is considered malicious and usually contains garbage text only created to garnish a higher ranking. This type of content will result in penalties."

> New wording (per SEJ, quoting the rewrite): "Large-scale content generated without oversight, quality control, or editorial review often lacks usefulness, accuracy, and originality, and may be excluded from indexing."

> SEJ's own reporting, not a Bing quote: "Prompt injection went from a brief mention at the end of the old guidelines to a full section called 'Prompt Injection and AI Manipulation,' covering attempts to interfere with language models used by Bing or Copilot." And: "Microsoft didn't publish a separate announcement about the rewrite. The changes are live on the Bing Webmaster Guidelines page, with the previous version available through the Wayback Machine."

### Secondary source (lower reliability, flagged): AllAboutAI.com, dated March 2, 2026

> "The guidelines now strictly forbid 'Generative Cloaking', showing one version of a page to a traditional crawler (like Bingbot) and a different, AI-optimized version to an LLM crawler."

**This "Generative Cloaking" term and characterization is NOT corroborated by the more careful Search Engine Journal report**, which describes the same guideline rewrite in detail (GEO naming, meta-directive rules, "Prompt Injection and AI Manipulation" abuse category, machine-generated-content language change) and never uses this term or describes a bot-vs-LLM-crawler cloaking ban specifically. Both sources are attributed and left side by side, per instructions, rather than reconciled — this pass could not verify either against Bing's own primary text.

### Mapping table

| Quoted provision | Source reliability | (a) differential content to crawlers | (b) paid placement in retrieved content | (c) commercial measurement of retrieval |
|---|---|---|---|---|
| 2018 Bing blog: dynamic rendering test | Primary, on-the-record, but pre-dates AI/Copilot entirely | **Directly on point**: differential *content* (not just render mechanism) is cloaking; identical content served two ways is not | Silent | Silent |
| SEJ: "Prompt Injection and AI Manipulation" new abuse category | Secondary, reliable, but paraphrased category name not fully quoted | Suggestive — a new abuse category naming AI manipulation exists post-March-2026, exact text unread | Silent | Silent |
| AllAboutAI: "Generative Cloaking" | Secondary, low reliability, uncorroborated | **Would directly answer (a) if verified** — unverified | Silent | Silent |

---

## Gap 5 — Vietnam Law on Advertising (Luật Quảng cáo) + current amendment

**Finding: CLOSED. Wave 1's four failed attempts (404/403/timeout/wrong-document) are resolved — the working source is the official Vietnamese Government Electronic Information Portal, `vanban.chinhphu.vn`, which none of wave 1's four attempts (luatvietnam, vanbanphapluat, thuvienphapluat, WIPOLex) tried. Both the base law and its current amending instrument were fetched as government-published primary text.**

### Document 1: Luật số 16/2012/QH13 (Law on Advertising 2012) — base law, original text
- URL: `https://vanban.chinhphu.vn/?pageid=27160&docid=163008`
- Pulled: direct curl, HTTP 200, official Government Electronic Information Portal. Raw: `raw/vn-luat-quang-cao-2012-full-text.txt`

Article 2.1, definition of "advertising" — Vietnamese, verbatim:

> "Quảng cáo là việc sử dụng các phương tiện nhằm giới thiệu đến công chúng sản phẩm, hàng hóa, dịch vụ có mục đích sinh lợi; sản phẩm, dịch vụ không có mục đích sinh lợi; tổ chức, cá nhân kinh doanh sản phẩm, hàng hoá, dịch vụ được giới thiệu, **trừ tin thời sự**; chính sách xã hội; thông tin cá nhân."

Translation: "Advertising is the use of means to introduce to the public for-profit products, goods and services; non-profit products and services; and organizations or individuals doing business in the products, goods or services introduced, **except news/current-affairs information**; social policy; personal information." — the law defines advertising and editorial ("tin"/news) content as legally distinct, mutually exclusive categories from the outset.

Original Article 23 (superseded by the 2025 amendment below, but shows the law's pre-existing baseline): Article 23.1(a), Vietnamese, verbatim:

> "Không được thiết kế, bố trí phần quảng cáo lẫn vào phần nội dung tin"

Translation: "Advertising must not be designed or arranged so as to be blended into the news content." — but this original clause, by its own placement, bound only "báo điện tử" (licensed electronic press/newspapers) and, per Article 23.2, state-agency "trang thông tin điện tử" (websites) — not ordinary private commercial websites. That gap is closed by the 2025 amendment below.

### Document 2: Luật số 75/2025/QH15 — the current amending instrument
- Landing page: `https://vanban.chinhphu.vn/?pageid=27160&docid=214561&classid=1&typegroupid=3`
- Signed PDF (primary, government-issued): `https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/75qh.signed.pdf` — saved as `raw/vn-luat-75-2025-qh15-sua-doi-signed.pdf`
- **Passed by the National Assembly: 2025-06-16. Effective: 2026-01-01** (Điều 3.1), signed by Trần Thanh Mẫn, Chairman of the National Assembly.
- Full replacement text of Article 23 transcribed at `raw/vn-luat-75-2025-dieu23-quang-cao-tren-mang.txt`

Article 23 (fully replaced), Vietnamese, verbatim:

> "Điều 23. Quảng cáo trên mạng
> 1. Hoạt động quảng cáo trên mạng bao gồm quảng cáo trên báo điện tử, trang thông tin điện tử, mạng xã hội, ứng dụng trực tuyến, nền tảng số có kết nối Internet.
> 2. Hoạt động quảng cáo trên mạng phải tuân thủ các quy định sau đây:
> a) Phải có dấu hiệu nhận diện rõ ràng bằng chữ số, chữ viết, ký hiệu, hình ảnh, âm thanh để phân biệt giữa nội dung quảng cáo với các nội dung khác không phải quảng cáo;"

Translation: "Article 23. Advertising on the network (online advertising). 1. Online advertising activity includes advertising on electronic newspapers, websites, social networks, online applications, and Internet-connected digital platforms. 2. Online advertising activity must comply with the following: a) It must carry a clear identification sign — by number, letter, symbol, image, or sound — to distinguish advertising content from other, non-advertising content."

And, further in the same Article, Vietnamese, verbatim:

> "b) Không đặt sản phẩm quảng cáo vào trong, bên cạnh, liền sau hoặc trước nội dung vi phạm pháp luật; không quảng cáo trên trang thông tin điện tử, mạng xã hội, ứng dụng trực tuyến, nền tảng số vi phạm pháp luật;"

Translation: "b) [The advertiser/publisher] must not place advertising content inside, beside, immediately after, or immediately before content that violates the law; must not advertise on a website, social network, online application, or digital platform that violates the law."

And, on future rulemaking, Vietnamese, verbatim:

> "8. Chính phủ quy định chi tiết Điều này."

Translation: "8. The Government shall issue detailed regulations for this Article [via decree]." **No such decree was located** — WebSearch budget was exhausted (200/200) before this could be confirmed either way. `unknown — checked WebSearch (exhausted mid-search), 2026-09-17`.

### Mapping table

| Quoted provision | (a) differential content to crawlers | (b) paid placement in retrieved content | (c) commercial measurement of retrieval |
|---|---|---|---|
| Điều 2.1, "quảng cáo... trừ tin thời sự" | Silent | Establishes ad/editorial as legally distinct categories — the predicate for (b) | Silent |
| 2012 Điều 23.1(a) (superseded), "không được... lẫn vào phần nội dung tin" | Silent | Bars blending ads into news content, but scope was limited to báo điện tử/state sites before 2026-01-01 | Silent |
| 2025 amendment, new Điều 23.2(a), "dấu hiệu nhận diện rõ ràng... phân biệt" | Silent — no crawler/bot/AI language anywhere in either law | **Squarely answers**: from 2026-01-01, ALL online advertising (websites, social media, apps, digital platforms) must be clearly, visibly distinguished from non-ad content — undisclosed paid placement blended into retrievable page content is out of compliance | Silent |
| 2025 amendment, Điều 23.3(b), ad-adjacency rule | Silent | Governs adjacency to illegal content, not disclosure per se — tangential | Silent |
| Điều 23.8, decree deferred | — | Implementation detail (thresholds, specific format requirements) still pending a decree not yet located | — |

**This is the sharpest, most squarely-on-point primary-source hit found across all five gaps for sub-question (b).** Unlike Google's cloaking policy (bot-vs-human framing) or the UCPD's advertorial rule (media-context framing, EU), Vietnam's 2025 amendment is a general, current (effective in 3.5 months at time of writing), platform-neutral online-advertising disclosure mandate that would apply directly to the founders' own operating jurisdiction (HCMC) regardless of which AI engine is involved.

---

## What is still unknown (channel and date checked)

1. **Bing/Copilot's live Webmaster Guidelines page, exact current text** — `unknown — checked bing.com direct fetch + Googlebot UA + WebFetch + Wayback Machine (5 timestamps: 2021, 2022, 2024, two 2026-09 captures), 2026-09-17`. Every method returns a JS shell; only a JS-executing browser (the unavailable extension) can read it.
2. **Whether Bing's live guidelines actually use the term "cloaking" or "Generative Cloaking" for AI-specific differential serving** — `unknown — checked Search Engine Journal (no corroboration) vs. AllAboutAI.com (uses the term, uncorroborated), 2026-09-17`. Conflicting secondary sources, left side by side per instructions, not reconciled.
3. **The implementing decree for Vietnam's new Điều 23.8** ("Chính phủ quy định chi tiết Điều này") — `unknown — checked WebSearch (budget exhausted at 200/200 mid-search), 2026-09-17`.
4. **Whether OpenAI has any document at all — anywhere in its policy stack — that governs a non-customer website's content as fetched by GPTBot/ChatGPT-User/OAI-SearchBot** (as opposed to governing its own customers) — `unknown — checked openai.com policies index (business-terms, services-agreement, usage-policies, sharing-publication-policy, service-terms, ad-policies, advertising-terms, ad-tools-terms, ad-tools-dpa — 9 documents read in full), 2026-09-17`. None found; this may mean no such document exists, or that it exists at a URL not surfaced by the Wayback CDX search used to find the ad-policy slugs.
5. **Same question for Perplexity** — `unknown — checked perplexity.ai/hub/legal (api-terms-of-service, aup, search addendum — 3 documents read in full), 2026-09-17`.
6. **Current live wording of Perplexity's Search Addendum** (most recent snapshot found is dated 2025-10-12, eleven months old) — `unknown — checked Wayback Machine, 2026-09-17`. Not re-verified against a live 2026-09 capture.

## Read across this addendum

The two closed, decision-relevant findings are: (1) **OpenAI's own Ads Terms exist, are current (updated as recently as August 2026), and contractually require paid content to be "clearly distinguishable"** from ChatGPT's native output — but only for content bought through OpenAI's own ad product, not for organic retrieval; and (2) **Vietnam's advertising law, as amended effective 2026-01-01, requires all online advertising to carry a "clear identification sign... to distinguish advertising content from other, non-advertising content,"** platform-neutral, with no carve-out for AI-mediated retrieval. Neither OpenAI's nor Perplexity's commercial-API contract stack (8 documents read in full across both companies) contains any provision addressing a third-party website's differential serving to their crawlers — that silence is itself the finding: these contracts govern OpenAI's/Perplexity's own customers, not the websites their crawlers fetch, so the "is the API path closed" question from pass 2 is answered not by a prohibition inside these contracts but by whichever *other* body of law reaches the website operator directly — which, for a Vietnam-based operator, is now Điều 23 of the amended Luật Quảng cáo, read squarely against the mechanism.
