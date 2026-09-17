# Google's own documentation on AI features, GEO, and Search Console reporting — raw pull

Pulled: 2026-09-17, wave 2b. Source: `https://developers.google.com/search/docs/appearance/ai-features`, HTTP 200, 179,579 bytes, direct `curl -L` with desktop Chrome UA. Kind: vendor-reported (platform owner). Title on page: "AI features and your website".

Pulled to test two things: (a) the Vietnamese agency claim that Search Console now breaks out AI Overview performance for free (`raw/wave2b-vn-agency-audit-and-free-tools.md` §2), and (b) whether the platform owner endorses the GEO optimisations the agencies sell.

---

## Verbatim, the operative passages

### On whether GEO optimisation is required

> "The best practices for SEO remain relevant for AI features in Google Search (such as AI Overviews and AI Mode). **There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary.** That said, it's always good to review the fundamental SEO best practices."

> "Technical requirements for appearing in AI features. To be eligible to be shown as a supporting link in AI Overviews or AI Mode, a page must be indexed and eligible to be shown in Google Search with a snippet, fulfilling the Search technical requirements. **There are no additional technical requirements.**"

> "**You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add.** To discover and diagnose potential technical issues quickly, verify your site in Search Console."

> "While specific optimization isn't required for AI Overviews and AI Mode, all existing SEO fundamentals continue to be worthwhile, for example: Ensuring that crawling is allowed in robots.txt, and by any CDN or hosting infrastructure; Making your content easily findable through internal links on your website; Providing a great page experience for users; Making sure that important content is available in textual form; Supporting your textual content with high-quality images and videos, when applicable; **Making sure your structured data matches the visible text on the page**; Checking that your Merchant Center and Business Profile information is up-to-date"

### On measurement in Search Console

> "Measuring the performance of your site. Just like the rest of the search results page, sites appearing in AI features (such as AI Overviews and AI Mode) are **included in the overall search traffic in Search Console. In particular, they're reported on in the Performance report, within the 'Web' search type.** Learn more about how AI Overviews and AI Mode are counted towards the overall data in Search Console, how to analyze traffic changes overall, and how to combine Search Console and Analytics data."

> "In addition to Search Console, you could also track conversions and time spent on your site in other tools, such as Google Analytics. We've seen that when people click from search results pages with AI Overviews, these clicks are higher quality (meaning, users are more likely to spend more time on the site)."

### On how the features retrieve

> "Both AI Overviews and AI Mode may use a 'query fan-out' technique — issuing multiple related searches across subtopics and data sources — to develop a response. While responses are being generated, our advanced models identify more supporting web pages, allowing us to display a wider and more diverse set of helpful links associated with the response than with a classic web search... AI Mode and AI Overviews may use different models and techniques, so the set of responses and links they show will vary. AI Overviews are only shown when our systems determine that it is additive to classic Search, and as such, often don't trigger."

### On control

> "AI is built into Search and integral to how Search functions, which is why robots.txt directives for Googlebot is the control for site owners to manage access to how their sites are crawled for Search. To limit the information shown from your pages in Search, use `nosnippet`, `data-nosnippet`, `max-snippet`, or `noindex` controls. To limit AI training and grounding in some of Google's other systems, read more about Google-Extended."

---

## The conflict, stated side by side, not reconciled

| Source | Claim | Date | Kind |
|---|---|---|---|
| Midas Agency (`midas.vn/dich-vu-geo/`) | Google Search Console has a "báo cáo Generative AI Performance" with "bộ lọc chuyên biệt" letting you see exactly which keywords trigger AI Overview display, plus that segment's Clicks and Impressions, free — "xóa bỏ hoàn toàn 'khoảng mù' dữ liệu AI" | pulled 2026-09-17 | vendor-reported (agency) |
| Google (`developers.google.com/search/docs/appearance/ai-features`) | AI Overviews and AI Mode "are included in the overall search traffic in Search Console. In particular, they're reported on in the Performance report, within the 'Web' search type." No separate report, no AI-specific filter named. | pulled 2026-09-17 | vendor-reported (platform owner) |

Both stand as pulled. Google's own page names no AI-specific Search Console report or filter. Whether one exists under a name Google's page does not mention is `unknown — checked developers.google.com/search/docs/appearance/ai-features and support.google.com/webmasters/answer/7576553 (the latter returned a JS-thin 7,158-char body with no occurrence of "AI Mode", "AI Overview", "generative" or "Search Appearance"), 2026-09-17`.

## Caveats

- No page stamp (`Last updated`) was captured from this document. Its currency relative to 2026-09-17 is asserted only by it being the live URL on that date.
- The Search Console help page that would settle the reporting question directly was not readable — it returned a thin, JS-dependent body. This is the same class of failure wave 1b recorded for Bing's guidelines.
- The Google page is about Google's own AI features only. It says nothing about ChatGPT, Claude or Perplexity, where every GEO/AEO vendor in this project also sells, and where no equivalent platform-owner statement has been found by any pass.
