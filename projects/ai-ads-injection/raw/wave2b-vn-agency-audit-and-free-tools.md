# Vietnamese GEO agencies — what the audit actually costs, and what they already ship — raw pull

Pulled: 2026-09-17, wave 2b. Method: direct `curl -L` with a desktop Chrome UA against the three agency pages `raw/vietnam-ai-visibility-demand.md` (wave 1d) already priced, re-fetched to answer a different question: **is the audit a paid SKU, and has any of them already built the tool?** Vietnamese quoted verbatim first, translation mine, marked. Kind: vendor-reported throughout.

---

## 1. TopOnSeek (TOS) — `https://www.toponseek.com/dich-vu-aeo/` (HTTP 200) and `https://www.toponseek.com/ai-visibility-check/` (HTTP 200)

Wave 1d recorded TOS as "quote-only, contact required" with no published price. That is still true of the retainer. What wave 1d did not record is that **TOS already ships a free self-serve AI-visibility measurement tool in Vietnamese.**

From the service page, verbatim:

> "KIỂM TRA AI VISIBILITY MIỄN PHÍ — Website của bạn có được ChatGPT, Gemini & Perplexity trích dẫn? Chấm điểm AI Visibility trên 6 trụ tín hiệu GEO — miễn phí, chỉ 15 giây."

Translation (mine): "FREE AI VISIBILITY CHECK — Is your website cited by ChatGPT, Gemini & Perplexity? Score your AI Visibility on 6 GEO signal pillars — free, only 15 seconds."

> "Chi phí linh hoạt theo nhu cầu, mục tiêu và độ cạnh tranh dự án. Chúng tôi có nhiều gói dịch vụ. Vui lòng liên hệ TOS để nhận báo giá chính xác và tư vấn miễn phí."

Translation (mine): "Cost is flexible according to need, goal and project competitiveness. We have several service packages. Please contact TOS for an accurate quote and free consultation."

Service-page items, verbatim: "Audit khả năng hiển thị trong Chat GPT"; "Audit khả năng hiển thị trong Gemini AI — Đánh giá website có đang được Gemini sử dụng làm nguồn tham chiếu, trích dẫn hoặc tổng hợp câu trả lời hay không. Audit AI visibility & answer eligibility". Nav also carries "GEO Audit" pointing at `toponseek.com/blogs/geo-audit/` — a blog URL, i.e. content marketing, not a product page.

### The tool itself — `/ai-visibility-check/`, verbatim

Schema.org block on the page:

> "@type":"WebPage", "name":"AI Visibility Checker", "description":"Công cụ miễn phí chấm điểm AI Visibility (GEO) cho website của bạn & đối thủ: llms.txt, schema, khả năng được ChatGPT/Gemini/Perplexity trích dẫn. Bởi TOS.", "inLanguage":"vi"

Translation (mine): "Free tool scoring AI Visibility (GEO) for your website & competitors: llms.txt, schema, ability to be cited by ChatGPT/Gemini/Perplexity. By TOS."

Page body, verbatim:

> "Website của bạn có được ChatGPT, Gemini, Perplexity & Google AI Overviews trích dẫn? Chấm điểm miễn phí + so sánh 3 đối thủ cùng ngành."

> "⚡ Kiểm tra AI Visibility miễn phí — Không cần đăng ký · Kết quả tức thì · Chấm trên 6 trụ tín hiệu GEO"

Translation (mine): "Free AI Visibility check — No registration needed · Instant results · Scored on 6 GEO signal pillars"

> "Đang chấm điểm site của bạn + tự tìm & so sánh 3 đối thủ" ["Scoring your site + automatically finding & comparing 3 competitors"]

The six pillars named on the page, with the quick-test tabs, verbatim: `AI Crawler Access` — "robots.txt có cho GPTBot, PerplexityBot, Google-Extended, ClaudeBot"; `llms.txt`; `Structured Data`; `Nội dung` [Content]; `E-E-A-T`; `Kỹ thuật` [Technical] — "6. Technical /15 Meta, canonical, mobile, tốc độ tải."

> "Kiểm tra riêng từng tín hiệu AI Visibility cho website bất kỳ — không cần đăng nhập."
Translation (mine): "Check each AI Visibility signal individually for any website — no login needed."

Other shipped surfaces visible in the page source:
- An industry leaderboard: "Chọn ngành để xem top website & điểm AI Visibility (**đo thật**)." — "Choose an industry to see top websites & AI Visibility scores (**really measured**)."
- A self-referential claim: "100/100 điểm AI Visibility — cao nhất trong các SEO agency VN" ("100/100 AI Visibility score — highest among Vietnamese SEO agencies"), with the gloss "Thợ giày đi giày đẹp" ("the cobbler wears good shoes").
- A scanned-domain history: "Hồ sơ website đã quét — Mọi domain đã kiểm tra trên tool, kèm lịch sử điểm AI Visibility — theo dõi & chăm sóc dần." ("Every domain checked on the tool, with its AI Visibility score history — track and nurture over time.")
- A free-account upsell: "Tạo tài khoản miễn phí" / "Create a free account" — "Đăng ký để kiểm tra thêm & lưu lịch sử." ("Register to check more & save history.")
- A sales-report generator, JS handler name verbatim `tos_aiv_sales_generate`, with prompts `'Enter a prospect domain.'` and `'Đang tạo báo cáo…'` / `'Generating…'` → `'Mở báo cáo'` / `'Open report'`.
- Elsewhere on the page: "Nhận audit GEO miễn phí →" ("Get a free GEO audit →").

[Note, mine: the tool is bilingual (`VI` flag in the JS), self-serve, unauthenticated, and wired to a prospect-report generator for the agency's own sales team. The audit is the lead magnet; the retainer is the product.]

---

## 2. Midas Agency — `https://midas.vn/dich-vu-geo/` (HTTP 200)

Verbatim:

> "Ngân sách đầu tư ước tính chỉ từ 80 triệu/tháng với gói triển khai tiêu chuẩn 12 tháng. Chi phí thực tế sẽ được chuẩn hóa theo quy mô doanh nghiệp, độ phủ thương hiệu hiện tại và mục tiêu cụ thể **sau buổi khảo sát miễn phí**."

Translation (mine): "Estimated investment budget from only 80 million VND/month with a standard 12-month deployment package. Actual cost will be normalised to company size, current brand coverage and specific goals **after the free survey**."

> "Tư vấn miễn phí 100%" ["100% free consultation"] · "Nhận tư vấn chiến lược miễn phí" ["Get a free strategy consultation"]

Audit's position in the offer, verbatim: it is line item **3** inside the retainer — "3. Audit & Content Optimization" — and:

> "Midas sẽ audit toàn bộ nền tảng SEO hiện có, giữ lại và tối ưu bổ sung những phần đang hoạt động tốt, đồng thời bổ sung các lớp còn thiếu như Entity Map, Schema chuẩn AI, và nội dung theo chuẩn Answer Engine để chuyển đổi sang mô hình Trusted Source."

> "...không thay thế các hạng mục Technical SEO, Content, Entity vốn có, mà bổ sung thêm khâu **AI Audit** và các chỉ số theo dõi hiện diện thương hiệu trên nền tảng AI."

Translation (mine): "...does not replace the existing Technical SEO, Content, Entity items, but adds an **AI Audit** step and metrics tracking brand presence on AI platforms."

### Midas's own answer to "are there free GEO tools?" — verbatim

> "Có công cụ nào miễn phí để làm GEO không? Hiện tại các công cụ chuyên sâu đều có phí khá cao. Tuy nhiên, bạn có thể dùng miễn phí các công cụ sau để hỗ trợ: Miễn phí: Google Search Console (báo cáo Generative AI Performance), AnswerThePublic/AlsoAsked, bản free của ChatGPT/Perplexity để tự kiểm tra mức độ được trích dẫn."

Translation (mine): "Is there any free tool for doing GEO? Currently the in-depth tools all cost quite a lot. However, you can use these free: Google Search Console (**Generative AI Performance report**), AnswerThePublic/AlsoAsked, the free version of ChatGPT/Perplexity to check your citation level yourself."

And, twice on the page:

> "...độc lập ngay bên trong Google Search Console. Bạn hiện tại có thể sử dụng các bộ lọc chuyên biệt để xem chính xác những từ khóa nào của mình đang được kích hoạt hiển thị trong khung AI Overview, cũng như theo dõi số lượt nhấp chuột (Clicks) và lượt hiển thị (Impressions) thực tế từ phân đoạn này hoàn toàn miễn phí. Điều này giúp xóa bỏ hoàn toàn 'khoảng mù' dữ liệu AI trước đây."

Translation (mine): "...independently right inside Google Search Console. You can currently use dedicated filters to see exactly which of your keywords are triggering display in the AI Overview box, as well as track actual Clicks and Impressions from that segment completely free. This completely eliminates the former AI data 'blind spot'."

**This specific claim conflicts with Google's own documentation — see `raw/wave2b-google-ai-features-doc.md`. Both are recorded, side by side, not reconciled.**

---

## 3. SEODO — `https://seodo.vn/dich-vu-geo/` (HTTP 200)

Wave 1d's three tier prices re-confirmed verbatim on the live page: "Từ 18 triệu", "Từ 200 triệu / Trọn gói", "Từ 350 triệu / Trọn gói". Every tier's CTA is the same three words: "Tư vấn miễn phí" ("free consultation").

**A fourth, conflicting entry price appears in the same page's FAQ**, verbatim:

> "Chúng tôi có các gói dịch vụ linh hoạt **từ 25 triệu** cho các doanh nghiệp nhỏ muốn xây dựng nền tảng vững chắc, đến các gói chiến lược cho những thương hiệu lớn muốn thống lĩnh thị trường."

Translation (mine): "We have flexible service packages **from 25 million** for small businesses wanting to build a solid foundation, up to strategic packages for large brands wanting to dominate the market."

`Từ 18 triệu` (pricing table) vs `từ 25 triệu` (FAQ) — same page, same pull, same day. Recorded side by side, not reconciled, not averaged.

Also verbatim, the offer attached to the lead form:

> "Hãy để lại thông tin để nhận tư vấn 1-1 miễn phí và **một bản kế hoạch SEO AIO sơ bộ** dành riêng cho website của bạn."

Translation (mine): "Leave your details to receive a free 1-1 consultation and **a preliminary SEO AIO plan** specific to your website."

And a market-sizing claim, vendor-reported, unsourced on the page:

> "Tính đến đầu năm 2026, ChatGPT đã có hơn 180 triệu người dùng hoạt động hàng tháng..."
Translation (mine): "As of the start of 2026, ChatGPT had more than 180 million monthly active users..." [Note, mine: this figure is far below every other published ChatGPT MAU figure this project has seen; the agency cites no source. Recorded as an example of the evidential quality of these pages, not used as a number.]

---

## What this pull establishes, stated once

| Agency | Retainer price, published | Audit / visibility check price | Channel |
|---|---|---|---|
| TopOnSeek | none — quote only | **free**, self-serve, no registration, 15 seconds | own site, 2026-09-17 |
| Midas | từ 80 triệu/tháng, 12-month | **free** ("sau buổi khảo sát miễn phí") | own site, 2026-09-17 |
| SEODO | từ 18 triệu / từ 25 triệu / 200tr / 350tr | **free** ("tư vấn miễn phí" + free preliminary plan) | own site, 2026-09-17 |

Three of three agencies checked give the audit away. Zero of three publish a price for an audit as a standalone deliverable.

## Caveats

- Three agencies of the eight wave 1d named. Hashmeta VN, Nextop, seo.danang.vn and Fast Marketing were not re-fetched this pass — `unknown — checked 2026-09-17, not pulled`.
- These are sales pages. A free audit advertised on a sales page does not prove no client ever paid for one; it proves no agency of the three advertises a price for one.
- No Vietnamese agency page checked, in this pass or wave 1d's, offers an answer-**integrity** or injection-audit line item. That negative now rests on 8 agency landing pages across two passes, still all landing-page-level.
- The TOS tool was not run against a domain. Its scoring is asserted by the page, not verified by us. Whether "đo thật" ("really measured") means live engine queries or static signal checks is `unknown — checked toponseek.com/ai-visibility-check 2026-09-17`; the six named pillars (robots.txt, llms.txt, structured data, content, E-E-A-T, technical) are all static-signal checks, which suggests the latter.
