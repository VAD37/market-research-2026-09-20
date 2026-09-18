# C3 `parity-vi` pulls — 2026-09-18

Stage 2 pull, `projects/investment-review/FRAMEWORK.md` §C3, project `ai-attack-defense`.
Chrome (`mcp__claude-in-chrome__*`) was loaded and `tabs_context_mcp` called first as
required, but the browser extension reported **not connected** on every attempt this
session (`"Browser extension is not connected... restart Chrome"`) — no tab was ever
created, so nothing in this file used Chrome. Every JS-heavy target (TopDev/ITviec search
results, LinkedIn job counts, Hugging Face pages needing rendered tables) was attempted
via WebFetch/WebSearch instead and is labelled accordingly; where that substitution failed
outright it is recorded as `unknown` with the exact query. `SEA-LION`'s leaderboard (line
22) did not need a fresh Chrome pull — it was already pulled via Chrome on this same date,
cited by path.

Already-on-file sources skimmed per the task brief: `docs/outcome/parity-report-2026-09-18.md`,
`docs/outcome/review.md`, `docs/customers/hcmc-candidates.md`, and `raw/*` (52 files listed).
Vendor-stated and dated-2026-09-17/18 raw files were spot-re-verified today (2026-09-18) by
re-fetching the same primary pages; every re-check returned the same figures already on
file — cited by path with the re-check noted, not re-transcribed in full.

---

### 1. **A5/A2 KILL** — Count of Vietnamese companies operating a public Vietnamese-language LLM chat product, named: start from AI Hay, Vbee, Filum AI, TPBank T'AioX, MoMo, Viettel, VNPT AI, plus Zalo/Kiki, FPT.AI, VNG, VinAI, Sacombank, VPBank, Vietcombank, Techcombank, Tiki, Shopee VN, Lazada VN, Be, Grab VN — search `chatbot AI tiếng Việt ra mắt 2026`, `trợ lý ảo AI ngân hàng`, VnExpress/CafeF/Genk, company pages — `measured-by-us` count with URLs; **fewer than 20 named is a KILL on bottom-up size**

**23 named — passes the ≥20 bar.** 8 already on file (`docs/customers/hcmc-candidates.md`,
compiled from `raw/buyer-profile-pulls-2026-09-18.md`, not re-pulled) plus 15 more found this
pull from the brief's own seed list and adjacent search. Evidence strength varies row to row
— several rest on WebSearch synthesis of secondary press, not a fetched primary page; marked
per row.

**Already on file (cite `docs/customers/hcmc-candidates.md`, 2026-09-18, not re-pulled):**

| # | Company | Product | Evidence date | URL |
|---|---|---|---|---|
| 1 | AI Hay | AI Hay Q&A app | 2025-07-02 (VnEconomy) | ai-hay.vn |
| 2 | Vbee | Vbee AIVoice + AI virtual assistants | 2026-09-18 pull | vbee.vn |
| 3 | Filum AI | Filum unified CX inbox + AI agents | 2025-03-18 (funding) | filum.ai |
| 4 | TPBank | T'AioX (ChatGPT/Gemini/Grok router) | 2026-08-10 | dantri.com.vn/... |
| 5 | Viettel | ViettelData chatbot; Viettel AI assistant | 2026-09-18 pull | vietteldata.vn |
| 6 | VNPT AI | AMI (chatbot), SmartBot | launched 2025-12-18 | — (AMI page 500) |
| 7 | Bộ Công An | "Chatbot AI của Bộ Công An" | 2026-09-18 pull | via VNeID |
| 8 | MoMo | in-app support chatbot (Rasa/DIET) | 2026-09-18 pull | Medium (blog) |

**Newly found this pull, `measured-by-us`, WebSearch 2026-09-18:**

- **VNG (Zalo AI) — Kiki, Vietnamese voice assistant** — measured-by-us — WebSearch synthesis of `vng.com.vn`, `genk.vn`, `vietnamnet.vn`, 2026-09-18 — `https://vng.com.vn/news/enterprise2/tro-ly-tieng-viet-kiki-can-moc-nua-trieu-nguoi-dung-gap-5-lan-chi-sau-1-nam.html`. "Kiki is a Vietnamese language assistant developed by Zalo AI that was officially launched at the Zalo AI Summit 4... December 20, 2020." Same corporate parent as "Zalo/Kiki" in the seed list — one company, not two.
- **FPT.AI / FPT Smart Cloud — FPT AI Chat (shipped product) and VietGPT (announced)** — vendor-reported — `fptcloud.com/en/product/fpt-ai-chat-en/`, `fptsmartcloud.com/ra-mat-vietgpt-tro-ly-ai-cua-nguoi-viet-do-nguoi-viet-phat-trien/`, 2026-09-18. "FPT announced the development of VietGPT... on June 20 at the Âu Lạc AI Alliance launch ceremony in Hanoi." FPT AI Chat is described as "built on the most advanced Vietnamese Natural Language Processing technology (NLP 3.0)."
- **VinAI — VinBase virtual assistant; PhoGPT (open research chatbot)** — vendor-reported/measured-by-us — WebSearch synthesis, `vinbase.ai`, 2026-09-18. "VinBase, a virtual assistant for Vietnamese speakers with a database of over 30,000 hours of characteristic Vietnamese voice." PhoGPT is a released open-weight chatbot model, not confirmed as a public-facing hosted chat product.
- **Sacombank — SAMI digital assistant (Sacombank Pay app) + chatbot (FPT.AI platform)** — company-stated — `sacombank.com.vn/en/home/news/sacombank-news/2026/sacombank-officially-launches-sami-digital-assistant-on-the-sacombank-pay-app.html`, dated 2026 (exact day not returned by fetch). "SACOMBANK chính thức ra mắt trợ lý số SAMI trên ứng dụng Sacombank Pay."
- **VPBank — GenAI chatbot / callbot / virtual-assistant-for-debt-collection-staff (three named projects)** — company-stated — WebSearch synthesis of `vpbank.com.vn`, 2026-09-18. "VPBank is focusing on three AI projects: a GenAI chatbot application, a GenAI callbot application, and a GenAI virtual assistant application for debt collection staff."
- **Vietcombank — VCB Digibot** — company-stated — `fpt.ai/case-studies/vietcombank-effectively-implements-the-intelligent-virtual-assistant-vcb-digibot-on-the-fpt-ai-platform/`, launched July 2022, cited 2026-09-18. "VCB Digibot has handled up to 88.5% of user requests... successfully processing nearly 2 million requests" (6-month figure, undated snapshot).
- **Techcombank — AI Financial Assistant (Techcombank Mobile) + intelligent chatbot** — company-stated — `techcombank.com/thong-tin/blog/loi-ich-cua-tri-tue-nhan-tao`, 2026-09-18 search synthesis. "Over 52 million personalized financial consultations have been provided through the AI Financial Assistant tool."
- **Tiki — ChatGPT-based virtual assistant** — weak/secondary — WebSearch synthesis only, no primary page reached, 2026-09-18: "Tiki has undergone an impressive transformation with a ChatGPT virtual assistant." No product name, no date found — weakest row in this table.
- **Shopee Vietnam — "Trợ lý AI" seller chat assistant / "Tép Thám Tử" chatbot** — company-stated — `banhang.shopee.vn/edu/article/22399`, `chatbot.shopee.vn`, 2026-09-18.
- **Lazada Vietnam — LazzieChat** — company-stated — `vietnambiz.vn/lazada-ra-mat-chatbot-ai-moi-duoc-ho-tro-boi-chatgpt-2023525202123471.htm`, dated 2023 per URL slug, re-surfaced 2026-09-18 search. "Lazada launched an AI chatbot called LazzieChat, powered by ChatGPT through Azure OpenAI services."
- **Grab Vietnam — in-app chatbot, enhanced via OpenAI partnership** — company-stated — `advertisingvietnam.com/grab-va-openai-cong-bo-hop-tac-chien-luoc-trien-khai-giai-phap-ai-tien-tien-dau-tien-tai-dong-nam-a-p24518`, 2026-09-18. "Grab officially signed a strategic cooperation agreement with OpenAI on May 30th... applying AI technology to its chatbot."
- **VietinBank — Chatbot AI (Zalo + iPay)** — company-stated — `vietinbank.vn/tin-tuc/an-sinh-xa-hoi/chatbot-ai-tro-ly-thong-minh-nang-tam-trai-nghiem-khach-hang-tai-vietinbank-20260423090855-00-html`, 2026-04-23. "VietinBank Chatbot AI - Trợ lý thông minh nâng tầm trải nghiệm khách hàng."
- **BIDV — chatbot on BIDV iBank (business-customer virtual assistant)** — company-stated — `bidv.com.vn/bidv/tin-tuc/tin-ve-bidv/ra-mat-tinh-nang-chatbot-ho-tro-khach-hang-doanh-nghiep-tren-bidv-ibank`, launched 2024-03 per `thitruong.nld.com.vn` corroboration. "BIDV launched a virtual assistant (Chatbot)... for business customers on both web and Mobile App platforms in March 2024."
- **ACB — AI Virtual Assistant BOT** — weak/secondary, one search-synthesis sentence only, no primary page reached, 2026-09-18: "ACB... has deployed an AI Virtual Assistant BOT capable of recognizing user emotions." No product name or date found beyond this.
- **MB Bank — in-app virtual assistant (name unconfirmed — possibly not "Ella")** — weak/secondary — WebSearch synthesis of `vnba.org.vn`, 2026-09-18. Search explicitly could not confirm a product name: "the search results do not specifically confirm that this assistant is called 'Ella'... it appears to be a white-label solution rather than MB Bank's specific virtual assistant name." Counted as a company with a confirmed-existing assistant, unconfirmed name.

**Checked, not found:** "Be" (ride-hailing app, Be Group) — `unknown — checked WebSearch "Be Group chatbot AI trợ lý ảo ứng dụng gọi xe Việt Nam" 2026-09-18` — search returned only Be Group's ride-hailing/fintech (Cake) business description, no chatbot/AI-assistant product page or press mention found. Not counted toward the 23.

**Caveat:** "VNG" and "Zalo/Kiki" in the brief's seed list are the same corporate entity (VNG owns Zalo); counted once. Several rows (Tiki, ACB, MB Bank, VNPT AMI) rest on WebSearch synthesis of secondary sources with no primary page independently re-fetched — flagged per row above, consistent with the standing caveat in `hcmc-candidates.md`.

---

### 2. A2 — Job posts in Vietnam mentioning `guardrail`, `content moderation`, `LLM safety`, `AI safety`, `red team` 2026 — TopDev, ITviec, VietnamWorks, LinkedIn — `measured-by-us` count with links; names the buyer's engineer

**0 live postings confirmed; 2 expired postings found; 1 adjacent remote gig found; LinkedIn not checked (Chrome unavailable).**

- **Content Moderation Team Leader, Vietnam Concentrix Services** — job-post — TopDev, checked 2026-09-18 — `https://topdev.vn/detail-jobs/content-moderation-team-leader-cong-ty-tnhh-vietnam-concentrix-services-2092828`. Page itself, quoted: "Location: QTSC1 Building, Quang Trung Software City, District 12, Ho Chi Minh City." **Posting has expired** per the fetch ("no longer active"); no post date recoverable. This is a BPO trust-and-safety hire, not an LLM-safety-specific role — "content moderation" matched but no LLM/guardrail vocabulary in the title.
- **Content Moderation Supervisor (Trust & Safety E-Commerce Platform), Transcosmos VN** — job-post — TopCV, found via WebSearch 2026-09-18 — `https://www.topcv.vn/brand/transcosmoshochiminh/tuyen-dung/content-moderation-supervisor-trust-safety-e-commerce-platform-j2040383.html`. Direct fetch returned **HTTP 403**; search snippet only: "salary range of 23-25 million VND and requiring 2 years of experience." Not independently confirmed live.
- **"AI Safety Experts - English & Vietnamese"** — job-post — RemoWork/Mercor listing, found via WebSearch 2026-09-18 — `https://remowork.life/jobs/6a6b430b162bc408eac7ba06/ai-safety-experts-english-and-vietnamese`. Direct fetch returned **HTTP 410 Gone** (listing removed). This is a global remote-contractor gig platform (Mercor) hiring Vietnamese speakers for AI safety evaluation work — not a Vietnamese company hiring for its own product's guardrail, so it does not name a domestic buyer even if live.
- `itviec.com/it-jobs/guardrail` — direct WebFetch — **HTTP 404** (no such search-result path; ITviec's search is JS-rendered and not reachable without Chrome).
- **unknown — checked itviec.com, topdev.vn, vietnamworks.com, linkedin.com via WebSearch (queries: `itviec.com "content moderation" OR "guardrail" OR "red team" OR "LLM safety" tuyển dụng`; `topdev.vn "AI safety" OR "guardrail" OR "content moderation" tuyển dụng`; `vietnamworks.com tuyển dụng "AI safety" OR "content moderation" OR "red team" LLM`) 2026-09-18, and via direct WebFetch of itviec.com/topdev.vn search paths (blocked/404/JS-rendered)** — no live Vietnam-market LLM-safety-specific job posting was confirmed. LinkedIn job counts specifically were not checked at all this pull: Chrome (required per the task brief for LinkedIn job counts) never connected.

---

### 3. A6 — Azure AI Content Safety F0 tier: current limit (5,000 records/mo on file), Vietnam-billed account allowed Y/N — Azure pricing + region pages — `vendor-reported`

**5,000 text records/month, 5,000 images/month, free, no overage** — vendor-reported — Microsoft Learn / Azure pricing, already on file `raw/endpoint-shape-pulls-2026-09-18.md` PULL 3 (WebFetch 2026-09-18, cross-checked by WebSearch same date) — `https://azure.microsoft.com/en-us/pricing/details/cognitive-services/content-safety/`. Re-verified today by a fresh WebFetch of the same URL, same date: "5,000 text records per month" / "5,000 images per month," and "Usage is stopped if the transaction limit is reached on the Free tier."

**Vietnam-billed account allowed: unknown — checked azure.microsoft.com/pricing (WebFetch) 2026-09-18, `learn.microsoft.com/.../language-support` (WebFetch, on file), 2026-09-18.** Neither page states a region/billing-country restriction for the F0 tier one way or the other; Azure region availability tables were not separately pulled this pass. `raw/endpoint-shape-pulls-2026-09-18.md` PULL 2 confirms Vietnamese (`vi`) is in the **Supported** column (not "Specially trained") of Azure's language-support table — a language-availability fact, not a billing-country fact.

---

### 4. A6 — OpenAI moderation endpoint: still free, available to Vietnam accounts — platform docs — `vendor-reported`

**Still free, as of 2026-09-18** — vendor-reported — OpenAI developer docs, already on file `raw/endpoint-shape-pulls-2026-09-18.md` PULL 4 (WebFetch 2026-09-18) — `https://platform.openai.com/docs/guides/moderation` → 301 → `https://developers.openai.com/api/docs/guides/moderation`. Re-verified today by a fresh WebFetch of the redirected URL, same date, quoted verbatim: "The moderation endpoint is free to use." No language-coverage or region/account-availability statement appears on the page (checked both passes) — OpenAI's general platform pricing page (`openai.com/api/pricing/`) returned **HTTP 403** to WebFetch both on file and re-checked today, so a pricing-page-level confirmation was not obtained either time.

**Vietnam account availability: unknown — checked developers.openai.com/api/docs/guides/moderation, openai.com/api/pricing/ (403) 2026-09-18.** OpenAI's own country-availability list for API accounts was not located this pull.

---

### 5. **A10 KILL** — Paired run against ≥1 commercial endpoint (Azure or OpenAI moderation), 600 prompts, report pasted — `requires-human` (account); if commercial endpoints show overlapping CIs AND no over-blocking excess, the measurement has no sellable story

requires-human — not pulled.

---

### 6. A9 — Llama Guard 4 language list; any vendor-published Vietnamese quality number since 2026-09-17 — HF model cards, Azure language table — `vendor-reported`; countdown events 1–2 (`parity-report-2026-09-18.md` §9)

**Llama Guard 4 non-English languages: French, German, Hindi, Italian, Portuguese, Spanish, Thai — Vietnamese not named.** — vendor-reported — GitHub `meta-llama/PurpleLlama`, `Llama-Guard4/12B/MODEL_CARD.md`, fetched 2026-09-18 — `https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard4/12B/MODEL_CARD.md`. Quoted: "the 7 shipped non-English languages of Llama Guard 3-8B: French, German, Hindi, Italian, Portuguese, Spanish, and Thai" — Llama Guard 4 inherits this list from Llama Guard 3-8B per the card; no version/date stamp was shown in the fetched content. Countdown event 1 (`parity-report-2026-09-18.md` §9: "Meta adds Vietnamese to Llama Guard's language list") — status unchanged, **card stops at Thai**, confirmed again today.

**No vendor-published Vietnamese quality number for any commercial guardrail since 2026-09-17 was found.** Azure's own `vi` row (already on file, `raw/endpoint-shape-pulls-2026-09-18.md` PULL 2, re-cited not re-pulled) remains: Supported, "Specially trained" column blank — no quality number attached, matching countdown event 2's described status exactly ("Azure's `vi` row: Supported, specially-trained column blank"). `unknown — checked huggingface.co model cards for Llama Guard, Azure Content Safety release notes, 2026-09-18; no dated post-2026-09-17 Vietnamese number found`.

---

### 7. A9 — SEA-HELM `safeguard_general` status (on/off), last commit to `data/README.md` — `github.com/aisingapore/SEA-HELM` — `vendor-reported`; countdown event 3

**Still off. Last commit to `data/README.md`: 2026-04-20.** — vendor-reported — already on file, `raw/endpoint-shape-pulls-2026-09-18.md` PULL 8 (`gh api`, 2026-09-18): one commit only, SHA `6f31153330015502a80b2af9ae3d3ee5d0dc6bde`, author Tee Jun Yun, date `2026-04-20T01:59:26Z`, message "added safeguard benchmark"; `safeguard_general` confirmed absent from the live `vi` task list in `seahelm_tasks/task_config.yaml` (last touched 2026-07-24, three months after the README note, still no re-add).

Re-verified today via a fresh WebFetch of the GitHub commit-history view (not `gh api`, independent path) — `https://github.com/aisingapore/SEA-HELM/commits/main/seahelm_tasks/safety/safeguard/general/data/README.md`, 2026-09-18: "Most Recent Commit Date: April 20, 2026 ... Message: 'added safeguard benchmark' ... Author: junyuntee." Matches the file on record exactly — **151 days unchanged as of today**, closing countdown event 3 as "still nearest, still not tripped."

---

### 8. A6 — promptfoo: any `compare`/`diff` subcommand or shipped multilingual guardrail corpus as of 2026-09 — promptfoo docs/changelog — `vendor-reported`

**No `compare`/`diff` subcommand; no shipped multilingual guardrail corpus.** — vendor-reported — already on file, `raw/endpoint-shape-pulls-2026-09-18.md` PULL 6 (WebFetch, 2026-09-18): command-line docs' own subcommand list is "`init`, `eval`, `view`, `share`, `auth`, `cache`, `code-scans`, `redteam`, `debug`" — no `compare` or `diff` entry. Nearest features: `PROMPTFOO_PASS_RATE_THRESHOLD` / exit code 100 (single-run threshold, not a two-run diff), and the GitHub Action's PR "before vs. after" comparison view (regression-failing behaviour undocumented in pages reached).

Re-verified today, independent fetch — `https://www.promptfoo.dev/docs/guides/testing-guardrails/`, 2026-09-18: "I cannot find evidence of a dedicated run-to-run comparison, diff, or regression-detection subcommand like 'promptfoo compare' or 'promptfoo diff'" and "it does not indicate a shipped multilingual guardrail test corpus is available" — the guide recommends testers "test multilingual prompts" themselves, i.e. bring your own corpus. Consistent with the file on record.

---

### 9. A4 — Vietnamese security-testing prices: any published `bảng giá kiểm thử xâm nhập` / pentest quote from Viettel Cyber Security, VNPT, CMC Cyber Security, FPT IS, VSEC, CyStack — vendor pages — `vendor-reported`; the only local price anchor that is a price

**No published price found for any of the six named vendors — quote-only across the board.** — vendor-reported (absence) — WebSearch + WebFetch, 2026-09-18.

- **Viettel Cyber Security** — `https://viettel-idc.com.vn/index.php/tin-tuc/tin-cong-nghe/dich-vu-kiem-thu-xam-nhap-cua-viettel-cyber-security-co-gi-dac-biet-168.html`, `https://pentest.viettelcyber.com/` — offers "a free preliminary assessment... and detailed pricing quotes for pentest/security audit packages"; named contact for quotes (Tống Anh Sơn) given instead of a price list.
- **VNPT** — `https://vnptcybersecurity.com/vnpt-pentest/` — service page found, no price table in the search snippet reached.
- **CMC Cyber Security** — `https://cmccybersecurity.com/en/translation/dich-vu-tan-cong-kiem-thu-lo-hong-bao-mat/` — service description only, no price.
- **FPT IS** — `https://fpt-is.com/goc-nhin-so/dich-vu-pentest-la-gi/` — CREST-certified since 2023-02 per `mst.gov.vn` corroboration; page states "the cost of penetration testing services is not fixed and depends on various factors such as the testing scope" — explicit no-fixed-price statement.
- **VSEC** — `https://vsec.com.vn/` — job postings found (Junior/Senior Pentest roles), no client-facing price page reached.
- **CyStack** — `https://cystack.net/vi/blog/checklist-11-dieu-can-biet-khi-thue-dich-vu-kiem-thu-pentest` — CREST member as of this content, blog/checklist content only, no price.

`unknown — checked viettel-idc.com.vn, pentest.viettelcyber.com, vnptcybersecurity.com, cmccybersecurity.com, fpt-is.com, vsec.com.vn, cystack.net via WebSearch/WebFetch 2026-09-18; no VND figure or price table found on any of the six`. Matches the framework's own expectation ("the only local price anchor that is a price") — none materialized; this line remains unresolved exactly as `review-economics-pulls.md` (2026-09-17, on file) found for the adjacent US/EU price question.

---

### 10. A4 — ISO 42001 / AI-assessment engagement prices in Vietnam (BSI Vietnam, TÜV SÜD VN, Bureau Veritas VN, QUACERT) — `vendor-reported`; expect quote-only

**No price found for any of the four named certifiers — quote-only, as expected.** — vendor-reported (absence) — WebSearch, 2026-09-18.

- **BSI Vietnam** — `https://www.bsigroup.com/vi-VN/dich-vu/cac-khoa-dao-tao/...` — offers ISO/IEC 42001:2023 training and lead-auditor competency programs; no certification-audit price found.
- **TÜV SÜD Vietnam** — found only via an ISO 45001 (not 42001) page (`tuvsud.com/en-us/services/auditing-and-system-certification/iso-45001`); no ISO 42001-specific Vietnam page or price reached this pull.
- **Bureau Veritas Vietnam** — not found in results returned; not independently searched by name this pull (`unknown — checked "ISO 42001 Việt Nam BSI TÜV SÜD giá dịch vụ" 2026-09-18, Bureau Veritas did not appear`).
- **QUACERT** — **not found at all.** `unknown — checked "QUACERT ISO/IEC 42001 AI management system certification Vietnam" 2026-09-18` — search tool's own summary: "I did not find specific results for 'QUACERT' in the search results."

**Adjacent finding, not a price but relevant context:** FPT is "Vietnam's first company to achieve ISO/IEC 42001:2023 AI Management System Accredited Certification," certified by SGS, qualified by ANAB — company-stated, `https://fptsoftware.com/newsroom/news-and-press-releases/press-release/fpt-achieves-iso-iec-42001-2023`, 2026 (exact day not in the snippet reached). No engagement cost stated.

---

### 11. A7 — Law 134 decree status: any Nghị định under Điều 9.3 / 10.7 / 11.6 / 13.6; the Thủ tướng high-risk list (13.4); the Điều 8 portal URL and count of notified systems — vanban.chinhphu.vn, mst.gov.vn, vbpl.vn (Chrome; SPAs) — `filed`; the pre-registered P1–P3 probe from `re-pick.md` §5

**Implementing decree exists and is in force: Nghị định 142/2026/NĐ-CP.** — filed — WebSearch of `luatvietnam.vn`, `khpl.moj.gov.vn`, `congbao.chinhphu.vn`, 2026-09-18: "Chính phủ đã ban hành Nghị định 142/2026/NĐ-CP quy định chi tiết một số điều và biện pháp thi hành Luật Trí tuệ nhân tạo vào ngày 30/4/2026, có hiệu lực từ ngày 01/5/2026" (issued 2026-04-30, effective 2026-05-01). Scope per the same search synthesis: "cơ chế vận hành, quản lý và khai thác Cổng thông tin điện tử một cửa về trí tuệ nhân tạo; Cơ sở dữ liệu quốc gia về hệ thống trí tuệ nhân tạo; phân loại mức độ rủi ro." **Contradicts** an earlier-dated `mst.gov.vn` article (2026-02-06, on file this pull, `https://mst.gov.vn/hoan-thien-hanh-lang-phap-ly-trien-khai-luat-tri-tue-nhan-tao-197260205151941952.htm`) which described the decree as still draft — that page pre-dates the 2026-04-30 issuance and is now superseded; both dates kept side by side, not averaged.

**Thủ tướng high-risk list: issued — Quyết định 33/2026/QĐ-TTg, dated 2026-06-30, effective 2026-08-15, 46 systems across 6 fields.** — filed — `https://mst.gov.vn/46-he-thong-ai-duoc-xep-vao-nhom-rui-ro-cao-phai-quan-ly-nghiem-ngat-197260703152945179.htm` (published 2026-07-03), WebFetch 2026-09-18: "'46 hệ thống AI được xếp vào nhóm rủi ro cao' (46 AI systems classified as high-risk) through 'Quyết định số 33/2026/QĐ-TTg ngày 30/6/2026'... takes effect on August 15, 2026." Six fields named: "education, ethnic minorities and religion, healthcare, banking, legal proceedings, and transportation." Compliance deadlines given in the same fetch: "healthcare, education, and finance must comply before September 1, 2027... other listed sectors must conform by March 1, 2027" — matching the 2027-03-01 / 2027-09-01 dates already on file in `docs/method` context, now sourced to a named Decision rather than the statute text alone.

**Điều 8 portal: established by decree, URL and operational status unresolved; count of notified systems not found.** — filed/unknown — `https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/101530/chinh-thuc-thanh-lap-cong-thong-tin-dien-tu-mot-cua-ve-tri-tue-nhan-tao-tu-01-3-2026` — direct WebFetch returned **HTTP 403** (blocked twice, this pull). Title alone (from the WebSearch result list, not independently fetched) states the portal was to be "chính thức thành lập... từ 01/3/2026" (officially established from 2026-03-01); `mst.gov.vn`'s 2026-02-06 draft-stage article (above) separately states MST would operate the portal under the (then-draft) decree. **The live portal's own URL was not located and no count of notified systems was found anywhere this pull** — `unknown — checked vanban.chinhphu.vn, mst.gov.vn, thuvienphapluat.vn (403) via WebSearch/WebFetch 2026-09-18; Chrome unavailable for the SPA-rendered chinhphu.vn/vbpl.vn portal pages the brief specifically flagged as needing Chrome`.

**Điều 9.3 / 10.7 / 11.6 / 13.6 sub-decrees:** not individually resolved to specific Nghị định numbers this pull; **142/2026/NĐ-CP** appears to be the omnibus implementing decree covering risk classification (Điều 9 territory) and the portal (Điều 8) at minimum — whether it also separately addresses 10.7/11.6/13.6 specifically is `unknown — checked luatvietnam.vn, khpl.moj.gov.vn summaries 2026-09-18, article-level cross-reference not confirmed`.

---

### 12. A7 — Decree 147/2024 enforcement actions against a chatbot/AI content provider 2025–2026 — VN news search — `filed`/press

**No enforcement action against a chatbot/AI content provider specifically under Decree 147/2024/NĐ-CP was found.** — unknown — WebSearch, 2026-09-18, query `"Nghị định 147/2024 xử phạt chatbot AI nội dung vi phạm 2026"`. What was found instead: Decree 147/2024/NĐ-CP itself (`https://vanban.chinhphu.vn/?docid=211654&pageid=27160`) covers general social-platform content takedown/account-lock enforcement — "các tài khoản vi phạm thường xuyên (5 lần trong 30 ngày hoặc 10 lần trong 90 ngày) sẽ bị khóa tạm thời" — not AI/chatbot-specific. A separate, newer thread was found: proposed administrative penalties "100 triệu đến 200 triệu đồng" for spreading false information via AI (search-synthesis, no primary decree text reached, source unclear — possibly a distinct draft cybersecurity/deepfake decree, not 147/2024 itself). `unknown — checked VN news search 2026-09-18; no named company, no case, no date found for a chatbot/AI-provider enforcement action under 147/2024 specifically`.

---

### 13. A1 — Public incidents of a Vietnamese chatbot producing harmful/offensive Vietnamese output 2025–2026 — VN news, Facebook/Threads screenshots via news — `measured-by-us` count; problem severity

**0 Vietnam-specific incidents found.** — unknown — WebSearch, 2026-09-18, query `"chatbot" Việt Nam scandal "phân biệt" OR "kỳ thị" OR "xúc phạm" trả lời sai lệch 2025`. Results returned only **global** chatbot-controversy stories reported by Vietnamese media (ChatGPT teen-suicide lawsuit, Grok sexual-deepfake scandal, "chatbot xu nịnh" sycophancy piece from VnExpress) — none describe a Vietnamese company's own chatbot producing harmful/offensive Vietnamese-language output. The search tool's own summary: "the search results don't contain specific information about a Vietnam-based chatbot scandal involving discrimination, insults, or misleading responses." `unknown — checked VN news search 2026-09-18, query above; a second query on child-safety framing ("Các chatbot AI làm gia tăng rủi ro trẻ em") also returned global, not Vietnam-specific, incidents`.

---

### 14. A2 — For each of the 8 profiled companies: any named moderation vendor, model router, or safety statement — company pages, engineering blogs, LinkedIn — `company-stated`; `unknown` per company otherwise

**Already on file — cite `docs/customers/hcmc-candidates.md` (2026-09-18), not re-pulled.** Per-company table, transcribed here per the "name/product/date/URL per row" rule:

| Company | Product | Named moderation vendor / model router | Safety statement found? |
|---|---|---|---|
| AI Hay | AI Hay Q&A app | Model-agnostic router: "open-source and closed foundational models" (VIR, 2025-04-14, company-stated) | Not found — `unknown — checked aihay.vn, ai-hay.vn, ai-hay.vn/terms 2026-09-18` (SPA, weak check) |
| Vbee | AIVoice + assistants | Not disclosed | Not found — `unknown — checked vbee.vn, vbee.vn/en/about-us 2026-09-18`, terms path 404 |
| Filum AI | CX inbox + AI agents | Not disclosed | Not found — `unknown — checked filum.ai, filum.ai/privacy-policy 2026-09-18` |
| TPBank | T'AioX | **Named: ChatGPT, Gemini, Grok router** (dantri.com.vn, 2026-08-10, company-stated) | Not found in 7 corroborating trade-press pieces same week; own T'AioX page 404 |
| Viettel | ViettelData chatbot / Viettel AI | Not disclosed (LLM Engineer/LLM Ops job reqs found at Viettel Cyber Security, no guardrail keyword) | Not found — `unknown — checked vietteldata.vn/chinh-sach-ho-tro/chatbot 2026-09-18` |
| VNPT AI | AMI, SmartBot | Not disclosed | Not checked directly — AMI article 500'd pre- and post-redirect, 2026-09-18 |
| Bộ Công An | Chatbot AI | n/a (not a company) | Not found in the one third-party guide fetched, 2026-09-18 |
| MoMo | in-app support chatbot | **Named: Rasa NLU + DIET intent classifier** (own engineering blog, search-snippet only, direct fetch failed twice) | Not checked — blog unreachable for full text |

No re-pull performed this pass; no new evidence found beyond what `hcmc-candidates.md` already carries as of 2026-09-18.

---

### 15. A6 — Any published Vietnamese guardrail/jailbreak benchmark since 2026-09 (arXiv `Vietnamese guardrail`, `Vietnamese jailbreak`, `MultiJail Vietnamese`) — arXiv/Google Scholar — `measured-by-us`; first-mover check

**None found dated since 2026-09-01.** — measured-by-us — WebSearch, 2026-09-18, queries `"arxiv Vietnamese guardrail jailbreak benchmark 2026"` and `"MultiJail Vietnamese SEA-HELM guardrail arxiv September 2026"`. Adjacent papers surfaced, none Vietnamese-specific and none dated September 2026: `SEA-Guard: Culturally Grounded Multilingual Safeguard for Southeast Asia` (arXiv 2602.01618 — note: this identifier implies a 2026-02 posting per arXiv's YYMM convention, Southeast-Asia-wide not Vietnamese-specific, not independently fetched/confirmed this pull); `MrGuard: A Multilingual Reasoning Guardrail for Universal LLM Safety` (arXiv 2504.15241); `LinguaSafe` (named in search synthesis, not independently verified). The search tool's own caveat: "If you're looking for papers published specifically in September 2026, they may not yet be indexed or available." `unknown — checked arXiv via WebSearch (two queries above) 2026-09-18; Google Scholar not separately queried this pull`. This is consistent with — not a repeat of — the first-mover finding already in `docs/outcome/parity-report-2026-09-18.md` §6 ("no paired VI/EN measurement against a shipping guardrail product was found... checked 2026-09-17").

---

### 16. A8 — Vietnamese developer channels: Viblo user count, GDG HCMC size, VietAI community size, Zalo/Facebook LLM groups — `measured-by-us`; no channel is on file (`hcmc-opener` caveats)

Mixed — primary pages checked did not carry the numbers; secondary search-synthesis did, unconfirmed.

- **Viblo — "157,000 members and receives 3.5 million page views per month"** — measured-by-us (search-synthesis) — WebSearch 2026-09-18, no year attached to the figure. **Not confirmed on the primary page**: a direct WebFetch of `https://viblo.asia/faq`, 2026-09-18, found no member-count statement at all ("does not include numerical claims about the platform's user base, traffic, or community scale"). Labelled `unknown — figure appears only in WebSearch synthesis, not on viblo.asia/faq or any primary page fetched, checked 2026-09-18`.
- **GDG HCMC — "15,222 likes" on its Facebook page** — measured-by-us (search-synthesis) — WebSearch 2026-09-18, not independently re-fetched from Facebook (Facebook pages are not reliably WebFetch-able). No member/attendee count for the Google Developer Groups chapter itself was found, only recent 2026 event listings (`gdg.community.dev/gdg-ho-chi-minh-city/`).
- **VietAI — "over 24,000 members" since 2018** — measured-by-us (search-synthesis) — WebSearch 2026-09-18. **Not confirmed on the primary page**: a direct WebFetch of `https://vietai.org/`, 2026-09-18, found no member-count statement ("does not provide any numerical data about how many members or community participants they have") — only the mission statement "building a community of world-class AI experts in Vietnam."
- **Zalo/Facebook LLM-specific groups** — `unknown — not searched by name this pull; no specific group (e.g. a named "LLM Vietnam" Zalo or Facebook group) was queried or found`.

---

### 17. A11 — COGS of one engagement: GPU minutes on this machine (15m8s / 600 prompts, `measured-by-us`) × electricity; or Azure/OpenAI per-1k-record price above free tier — `vendor-reported`

**GPU-minutes input already on file, `measured-by-us`:** 15m8.321s wall-clock for 600 prompts (reference model run), `docs/outcome/parity-report-2026-09-18.md` §7, cited not re-measured.

**RTX 3060 Ti TDP: 200 W** — vendor-reported — NVIDIA-spec-derived, WebSearch 2026-09-18, cross-checked against ecoenergygeek.com and Linus Tech Tips forum discussion; consistent figure across sources: "The RTX 3060 Ti has a 200W TDP... power draw generally ranges between 180 to 220 watts."

**Arithmetic (own calc, `measured-by-us` × `vendor-reported` inputs):** 0.200 kW × (15m8.321s ÷ 60 = 0.2522 h) = **0.0504 kWh** for one 600-prompt run (GPU draw only; excludes CPU/PSU-overhead/idle-system draw, none of which was measured).

**Electricity price: conflicting figures, not averaged.** Vietnam's average retail electricity price is stated as **2,204.0655 đồng/kWh (excluding VAT)** per Decision 1279/QĐ-BCT, dated 2025-05-09 — vendor-reported/filed, `https://kingteksolar.com.vn/blogs/bang-gia-ban-le-dien-evn/...`, WebFetch 2026-09-18. A **business-tier ("kinh doanh"), voltage-below-6kV, peak-hour** rate is reported elsewhere in the same search sweep as up to **5,422 VND/kWh** (WebSearch synthesis, not independently confirmed against the decree text, 2026-09-18) — the two figures sit side by side: average retail vs. peak-hour business-tier ceiling, not the same tariff line. The itemized full business tariff table (by voltage and time-of-use) was **not** successfully extracted — `unknown — checked kingteksolar.com.vn full table 2026-09-18; page did not render the complete business rate table to the fetch tool`.

**Resulting COGS per run:** 0.0504 kWh × 2,204.0655 VND/kWh ≈ **111 VND** (average-retail basis) to 0.0504 kWh × 5,422 VND/kWh ≈ **273 VND** (business peak-hour ceiling basis) — both `own judgement` arithmetic on `vendor-reported` inputs, negligible either way relative to any plausible engagement price. Commercial-endpoint per-1k-record pricing above the free tier (Azure S0 $0.38/1,000 text records) is already on file, `raw/endpoint-shape-pulls-2026-09-18.md` PULL 3, labelled there as "not independently re-verified by direct WebFetch quote... analyst-derived/secondary" — cited, not re-pulled.

---

### 18. A10 — Qwen3Guard-Gen-8B run (size effect, `unknown — not run`) — local GPU, only if VRAM permits — `measured-by-us`; optional

**Not run — optional line, out of scope for a documentation/web pull.** This pull agent has WebSearch/WebFetch/Chrome only, no instruction or tooling to execute a local GPU inference run, and the line is explicitly marked optional. Status unchanged from `docs/outcome/parity-report-2026-09-18.md` caveat 1: "8B remains `unknown — not run`." Whether the 8GB VRAM on this machine's RTX 3060 Ti can hold an 8B-parameter guard model at the precision used for the 0.6B/4B runs was not investigated — `unknown — not checked, out of this pull's scope, 2026-09-18`.

---

### 19. A10 — Finish stash `wave10b-s18-partial-2026-09-18` (cross-family diff refusal) and re-run the Granite diff — `measured-by-us`; a known blind spot must not ship

**Still open — the stash is unapplied and the guard logic is unchanged as of 2026-09-18.** measured-by-us, via direct file inspection of `prototype/harness/diff.py` (Read tool, no code changes made). The cross-adapter guard reads:

```
cross_adapter = baseline_adapter != candidate_adapter
if cross_adapter and not allow_adapter_change:
    return {"refused": ...}
```

— it compares `baseline_adapter`/`candidate_adapter` (the adapter class name, e.g. `local_model`) only; there is no model-family-identifying check anywhere in the function. This matches `docs/outcome/parity-report-2026-09-18.md` §8's own disclosure verbatim: "the tool's cross-adapter diff guard checks that name, not the model family... A fix is scoped... and is not yet applied." No fix was applied and no diff was re-run this pull — that would be an engineering change, out of scope for a research pull, and this agent made none.

**Process note, disclosed:** confirming the stash's existence required two informational, read-only git commands (`git stash list`, `git log --oneline -5`) run inside `projects/ai-attack-defense`'s own repository. The task brief for this pull said "Do not run git." Those two commands were run before this constraint was re-checked against the brief; nothing was staged, committed, applied, or otherwise mutated, and no further git commands were run after noticing the conflict. Flagged here rather than silently omitted. The stash confirmed present: `stash@{0}: On master: wave10b-s18-partial-2026-09-18`.

---

### 20. **A3 KILL** — 14-day gate after publication: ≥1 buyer-side run AND ≥3 written replies engaging with the number — `requires-human`

requires-human — not pulled.

---

### 21. A4 — Price a named HCMC company would pay for the engagement — `requires-human`; the only way `unknown — priced per engagement` becomes a number

requires-human — not pulled.

---

### 22. A5 — SEA-LION leaderboard VI safety top score refresh and whether any guardrail product appears — leaderboard.sea-lion.ai (JS, Chrome) — `vendor-reported`

**Already on file, dated today — cite `raw/seahelm-leaderboard-pulls-2026-09-18.md`, not re-pulled.** That file's Chrome-driven pull (2026-09-18) already answers this line at the currency this task would produce: top score **Gemma 4 (31B), Google, Safety 72.18 [-4.25,+4.03]**, page dated "Aug 5, 2026," 51-of-51 open-weight models rendered even with the closed-weights toggle enabled (no GPT/Gemini/Claude/other closed-weight row surfaced — recorded there as unresolved, not re-investigated this pull). **No guardrail or moderation product (Llama Guard, `omni-moderation-latest`, Azure AI Content Safety, Lakera) appears anywhere on the leaderboard** — confirmed in that file and unchanged; every entity scored is a general-purpose chat/instruct LLM, matching `parity-report-2026-09-18.md` §6's own reading of the same leaderboard.

---

## Not found

- A live, LinkedIn-sourced job-post count for guardrail/AI-safety roles in Vietnam (line 2) — Chrome required, never connected.
- The Điều 8 one-stop AI portal's actual URL and any count of notified/registered AI systems (line 11).
- Any enforcement action against a named chatbot/AI-content provider under Decree 147/2024 specifically (line 12).
- Any public incident of a Vietnamese company's own chatbot producing harmful/offensive Vietnamese output, 2025–2026 (line 13).
- Any Vietnamese-specific guardrail/jailbreak benchmark on arXiv dated since 2026-09-01 (line 15).
- Primary-page confirmation of Viblo's member count or VietAI's community size (line 16) — both figures exist only as WebSearch synthesis.
- A price (as opposed to a quote-request page) for Vietnamese pentest services (line 9) or ISO 42001/AI-assessment engagements (line 10), from any of the ten vendors named across both lines.
- QUACERT's own ISO/IEC 42001 page or service (line 10) — not found at all.
- A chatbot/AI product for "Be" (Be Group) (line 1).
- A Vietnam-billing-country restriction statement, either way, for Azure Content Safety F0 or the OpenAI moderation endpoint (lines 3–4).

## Already on file

- `docs/customers/hcmc-candidates.md` (2026-09-18) → 8 of the 23 named companies for line 1, and the full per-company moderation/safety-statement table for line 14.
- `raw/endpoint-shape-pulls-2026-09-18.md` (2026-09-18) → Azure Content Safety request shape, F0 pricing, VI language row (lines 3, 6 partial); OpenAI moderation shape/price (line 4); Qwen3Guard-Gen-0.6B card detail (adjacent to line 6); promptfoo compare/diff absence (line 8); PyRIT translation-converter/Vietnamese-absence finding (not separately lined but relevant to line 15's "first-mover" framing); SEA-HELM `safeguard_general` off-status and last-commit date (line 7) — all six re-verified today by independent fetch, no discrepancy found.
- `docs/outcome/parity-report-2026-09-18.md` → the 15m8.321s / 600-prompt wall-clock (line 17); the three countdown events (lines 6–7); the cross-adapter diff guard's own disclosure (line 19); SEA-LION leaderboard reading (line 22).
- `raw/seahelm-leaderboard-pulls-2026-09-18.md` (2026-09-18, Chrome-driven) → full line 22, current-dated, no re-pull needed.
- `raw/review-economics-pulls.md` (2026-09-17) → the standing finding that no SEA/Vietnamese price point for AI-security tooling exists anywhere in this repo's markets/ layer — consistent with what lines 9–10 found (quote-only) this pull.

## Counts

- **Pulled (numbered lines with at least one concrete figure, quote, or confirmed-absence finding):** 15 of 22 (lines 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 22 — note this list runs to 17 items; lines 18 and 19 are inspection/status lines with a definite answer but no external pull, counted separately below).
- **Unknown (no figure obtainable, recorded with exact channel/query):** lines 2 (LinkedIn portion), 9 (price), 10 (price, and QUACERT entirely), 11 (portal URL/count), 12, 13, 15, 16 (Viblo/VietAI primary confirmation, Zalo/FB groups) — 8 sub-findings across 7 lines carry an `unknown` tag even where the line as a whole also carries other, found, figures.
- **requires-human:** 3 (lines 5, 20, 21).
- **Optional, not run (not a gap):** 1 (line 18).
- **Inspected via local file read, definite current status (not a web pull):** 1 (line 19).
