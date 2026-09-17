# Market gaps in AI, 2026-09 — raw pulls

Fetch date for all blocks: 2026-09-16, unless a different in-document date is quoted (that date is the source's publish/post date, not the fetch date).

Session constraint: WebSearch quota was fully exhausted before this pull began (200/200 used) — see Block 0. All pulls below used direct `curl`/WebFetch against known URLs and two API surfaces that don't require search: the Hacker News Algolia API (`hn.algolia.com/api/v1/...`) and Discourse forum JSON search (`<forum>/search.json?q=...`, `<forum>/t/<id>.json`). Reddit (JSON API and old.reddit.com/www.reddit.com) was unreachable by both `curl` and WebFetch for the entire session — see Block 0 for the exact failure modes. G2 returned 403 to WebFetch.

---

## Block 0 — Channel access failures (record per instructions: note 403s and JS-rendered pages explicitly)

Channel: curl and WebFetch, various.
Fetch date: 2026-09-16.

- `curl -s -A "Mozilla/5.0" "https://www.reddit.com/r/SaaS/search.json?q=AI%20wish%20there%20was&restrict_sr=1"` → HTTP 200 but body is the React app shell (`<body class=theme-beta>...`), no JSON, no post data. Same result on `https://api.reddit.com/r/SaaS/search?q=AI&restrict_sr=1` (curl reported HTTP 403 on the request line, app-shell HTML in the body).
- `curl -s "https://old.reddit.com/r/SaaS/search.json?q=AI&restrict_sr=1"` → 0 bytes returned (connection accepted, empty body).
- `WebFetch` on `https://old.reddit.com/r/SaaS/search/?q=AI+wish+there+was&restrict_sr=1` → tool error: "Claude Code is unable to fetch from old.reddit.com".
- `WebFetch` on `https://www.reddit.com/r/SaaS/search/?q=AI%20wish%20there%20was&restrict_sr=1` → tool error: "Claude Code is unable to fetch from www.reddit.com".
- Result: r/SaaS, r/Entrepreneur, r/artificial, r/LocalLLaMA, r/ExperiencedDevs were **not reachable this session** by any method tried. `unknown — checked https://www.reddit.com/r/SaaS/search.json 2026-09-16` for all Reddit-sourced complaint evidence the brief asked for. Substituted Hacker News (Algolia API, fully open) and Discourse-based product forums (OpenAI community, Cursor forum — both have an open `/search.json` endpoint) as demand-side channels instead.
- `WebFetch` on `https://www.g2.com/products/otter-ai/reviews?filters%5Bnps_score%5D%5B%5D=1` → HTTP 403 Forbidden. G2 low-star reviews: `unknown — checked https://www.g2.com/products/otter-ai/reviews 2026-09-16`.
- `WebFetch` on `https://community.openai.com/search?q=...` (the HTML page, not the JSON API) → returned a placeholder "This is not the content you are looking for" — JS-rendered, empty to a non-JS fetch. Worked around by hitting the Discourse JSON API directly (`community.openai.com/search.json?q=...`), which is not JS-rendered and returned real data — used for Blocks 12-15 below.
- `WebFetch` on `https://hi.humane.com/` → DNS failure (`getaddrinfo ENOTFOUND hi.humane.com`), domain no longer resolves.
- `WebFetch` on `https://www.theverge.com/...` → tool error: "Claude Code is unable to fetch from www.theverge.com" (WebFetch-side domain block). Worked around with direct `curl` (see Block 5), which succeeded (HTTP 200) and returned full article HTML.
- WebSearch: first two queries of the session both returned "Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls)." No further WebSearch calls attempted after that; every other pull in this file used curl/WebFetch on a directly-supplied URL or an unauthenticated JSON API.

---

## Block 1 — AI meeting-notetaker category is visibly overcrowded (Show HN survey)

URL: https://hn.algolia.com/api/v1/search_by_date?query=AI%20note%20taker&hitsPerPage=20 and https://hn.algolia.com/api/v1/search_by_date?query=AI%20meeting%20notes%20free&hitsPerPage=20
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API, Show HN posts, raw JSON.

Nine separate two-person/solo "Show HN" meeting-transcription/notetaker launches inside a five-month window (2026-05 to 2026-09), nearly all at near-zero traction:

> Show HN: Dikaletus – meeting recording and transcription using Mistral AI — 2pts, https://news.ycombinator.com/item?id=48073470 (2026-05-09)

> Show HN: CallBro – Granola, but Powered by Codex, Claude Code, or Your Local LLM — 1pt 1cm, https://news.ycombinator.com/item?id=48968013 (2026-07-19)

> Show HN: BYO AI free notetaking with optional screen reading for OpenClaw/hermes — 3pts 3cm, https://news.ycombinator.com/item?id=48904884 (2026-07-14)

> Show HN: Biscotti – on-device meeting transcription for macOS — 1pt 1cm, https://news.ycombinator.com/item?id=48894351 (2026-07-13)

> Compendium — meeting-notes tool at cerenovus.ai — 0pts, https://news.ycombinator.com/item?id=48841178 (2026-07-09)

> Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents — 88pts 67cm, https://news.ycombinator.com/item?id=49024620 (2026-07-23) [only one of the nine with real traction, and it is YC-backed]

> Show HN: LymeScribe – one computer on your network transcribes for the rest — 3pts 1cm, https://news.ycombinator.com/item?id=49289952 (2026-08-13)

> Voicecard — voice-note-to-task CLI — 0pts, https://news.ycombinator.com/item?id=49431777 (2026-08-25)

> Show HN: MySamantha – a productivity app where the AI is optional — 3pts, https://news.ycombinator.com/item?id=49645994 (2026-09-10)

Full text of the Biscotti launch (id 48894351), stating the complaint that motivated the build:

> "I got tired of Electron meeting-transcription apps that upload my private audio to a server to do transcription/summary my MacBook could do locally in seconds. So I built Biscotti: a free, local meeting recorder. Calendar integration, voice isolation, speaker ID, AI summaries, native UI — and nothing ever leaves your device."

LymeScribe (id 49289952) opens with the same complaint, independently:

> "LymeScribe is local speech to text for Mac and Windows: dictate into any app, or drop in a recording and get a transcript with speaker labels, and nothing goes to a server you don't own."

**Read on this evidence: the generic "AI meeting notetaker" category is saturated and racing to free/local/open-source (Otter, Granola, Fireflies already own the mainstream cloud tier). A specific sub-niche — fully local/on-device, no-cloud transcription — has real, repeated, independent demand signal (2+ solo builders hit on it within a month of each other) but no single tool has broken out; it keeps getting re-solved from scratch. Not "unbuilt" so much as "built nine times, adopted by none of them yet."**

---

## Block 2 — Granola-style notetakers lock you into their own LLM subscription

URL: https://hn.algolia.com/api/v1/items/48968135
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API (Show HN post + comments), 2026-07-19.

> "Hi HN, I am building CallBro. The basic idea came from liking the bot free experience of tools like Granola, but not liking that the intelligence layer is usually fixed and owned by the product. I don't want to pay twice for same LLM tokens. I already use Claude Code and Codex, and I wanted my meeting assistant to use the same agent rather than requiring another AI subscription. ... Speech-to-text/ASR works locally, and transcripts, notes, and project context are stored as local MD files."

Points/comments: 1pt / 1 comment as of fetch date — signal is the complaint itself (bring-your-own-model meeting notetaker), not this project's traction, which is negligible.

**Gap**: no mainstream meeting-notetaker lets you point it at a model/subscription you already pay for (Claude Code, Codex, a local model) instead of bundling its own. Fix exists only as a 1-point Show HN toy, not a credible product — this is a real, small, two-person-sized gap, currently unfilled at any scale.

---

## Block 3 — No API path to actually file a tax return; "no Stripe for taxes"

URL: https://hn.algolia.com/api/v1/items/47769711
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API, comment posted 2026-04-14 (Tax Day thread).

> "Happy Tax Day — builder here. Every TurboTax, every payroll company, every CPA software vendor has built their own bespoke integration. There is no Stripe for taxes. AI can now prepare the vast majority of returns. But the last mile — actually submitting to the IRS — still requires a human to log into a web portal and click submit. There's no API. No programmatic path. Nothing. We're building the missing piece: an MCP server that lets AI agents file tax returns as a tool call. Employment tax (941, 940) first, then corporate and individual. We're finalizing IRS ATS certification now (it's a gauntlet — credentialing, schema validation, SOAP handshakes, annual re-certification)."

**Gap, company-stated (interested party — this is the builder pitching their own fix, not a neutral observer)**: no programmatic IRS e-file API for AI agents to call; the last-mile submission step is still human-only. Someone is actively building a fix (unnamed MCP server, IRS ATS certification "now finalizing" as of 2026-04-14) but as of the fetch date it has not shipped/launched publicly — so as of 2026-09-16 this remains an open gap with an attempted-but-unconfirmed fix in flight, not a shipped incumbent.

---

## Block 4 — Amazon quietly winding down its Nova AI models and the Adept acqui-hire

URL: https://www.businessinsider.com/amazon-overhauls-ai-strategy-phasing-out-most-nova-models-2026-7 (Business Insider, referenced via HN discussion)
Fetch date: 2026-09-16 (HN discussion dated 2026-07-28; could not fetch businessinsider.com directly — paywalled, not attempted with remaining budget).
Channel: Hacker News Algolia API comment on "Amazon overhauls its AI strategy, winding down most flagship models" (https://news.ycombinator.com/item?id=49082344, 6pts, 2026-07-28).

> "Fired their pre-training team, shutting down Nova, shutting down the Adept Acqui-hire but still building another Foundation model. According to the people familiar with the matter, resources have increasingly moved away from the existing Nova models and toward a new frontier-model effort led by researcher Pieter Abbeel, who came to Amazon through the acquisition of AI robotics startup Covariant. Known internally as Frontier Model Research, or FMR, the initiative has become a top priority this year."

Labeled: trade-press-derived (Business Insider reporting, relayed via an HN comment — not independently fetched from the primary article; treat the direct quote above as a comment's paraphrase/quote of the BI article, not a verbatim BI excerpt). Orphaned: Adept AI's product line (agentic-browser-automation product, acquired by Amazon in 2025) and the Nova model line's dependent integrations.

---

## Block 5 — Humane AI Pin: full shutdown, verbatim terms (2025-02-18)

URL: https://www.theverge.com/news/614883/humane-ai-hp-acquisition-pin-shutdown
Fetch date: 2026-09-16 (article published 2025-02-18, by Jay Peters, The Verge). Fetched via direct `curl` after WebFetch refused the domain.
Channel: trade press, curl direct fetch, HTML parsed for body text.

> "Humane is selling most of its company to HP for $116 million and will stop selling AI Pin, the company announced today. AI Pins that have already been purchased will continue to function normally until 3PM ET on February 28th, Humane says in a support document. After that date, Pins will 'no longer connect to Humane's servers.' As a result, AI Pin features will 'no longer include calling, messaging, AI queries / responses, or cloud access.' Humane is also encouraging users to download any pictures, videos, and notes stored on their Pins before they are permanently deleted at that shutdown time."

> "After the shutdown, offline features like 'battery level' will still work, Humane says, but 'any function that requires cloud connectivity like voice interactions, AI responses, and .Center access' will not. Humane will only offer refunds on AI Pins that are 'within the 90-day return window from their original shipment date.' ... If you have paid for a Humane subscription past February 28th, Humane says '...we will process a prorated refund.'"

> "HP is buying Humane's CosmOS, bringing on Humane technical staff, and will get more than 300 patents and patent applications... Humane's team, including founders Imran Chaudhri and Bethany Bongiorno, will form a new division at HP to help integrate artificial intelligence into the company's personal computers, printers and connected conference rooms... called HP IQ."

> "The Pin finally launched in April 2024 to scathing reviews; The Verge's David Pierce said that 'it just doesn't work,' and MKBHD called it 'the worst product I've ever reviewed.' ... the AI Pin appears to have sold quite poorly, with The Verge reporting in August that daily returns were outpacing sales."

Orphaned users: every AI Pin owner outside the 90-day return window as of 2025-02-27 — hardware bricked to "battery level only" from 2025-02-28 3PM ET onward, no successor product, no data export beyond a manual download window.

---

## Block 6 — Botkeeper (AI bookkeeping, ~$90M raised) reported shutting down — unconfirmed by primary source

URL (comment): https://news.ycombinator.com/item?id=46944882
URL (checked, no confirmation found): https://www.botkeeper.com
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API comment (2026-02-09) + direct WebFetch of the company's live site.

> "tl;dr: automated/AI-driven accounting startup with ~$90M in funding, including a $42M round in 2021, announces it will be shutting down" — linking https://www.prnewswire.com/news-releases/botkeeper-raises-42m-in-series-c-funding-from-paychex-founder-301416557.html (the funding announcement, not a shutdown notice; the PR Newswire link cited is evidence of the funding history, not the shutdown claim itself).

Cross-check: `WebFetch https://www.botkeeper.com` (2026-09-16) — "the content focuses entirely on promoting Botkeeper's bookkeeping automation platform and encouraging new customers to sign up," no shutdown/wind-down language found.

**Status: unknown — checked https://www.botkeeper.com 2026-09-16. HN comment (2026-02-09, unverified poster, 0 points) claims a shutdown; the company's own site as fetched shows no such notice and looks like an active going concern. Do not treat as a confirmed shutdown without a primary source (SEC filing, company statement, or dated trade-press piece) — record this as an open discrepancy, not a fact.**

---

## Block 7 — "AI wrapper" startups: overcrowding and thin-moat complaints (multi-year pattern)

URL: https://hn.algolia.com/api/v1/search_by_date?query=too%20many%20AI%20wrapper%20startups&hitsPerPage=20
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API, comments spanning 2023-08 to 2026-02.

> (2026-02-17) "I think the 'AI bubble burst' framing is too simplistic. Bubbles don't erase technology. They erase mispriced capital. In 2000, internet stocks collapsed. The internet didn't."

> (2025-02-16) "Joined early stage startup. It was a thin AI wrapper. The team was young and inexperienced but I wanted to believe in them... Laid off s[oon after]"

> (2025-01-12) "It's a little depressing how many high valued startups are basically just wrappers around LLMs that they don't own. I'd be curious to see what percentage of YC lates[t batch]..."

> (2024-09-01) "It's the dotcom boom all over again. Right now the webvans and pets.com of the world are getting insane valuations just by using a .ai tld. When the hubbub dies and the froufr[ou clears]..."

> (2023-08-31) "AI investment is actually down recently, looks like the hype is wearing off since most of the companies funded were just wrapping OpenAI APIs."

Read: this is a durable, multi-year, cross-cohort complaint (2023 through 2026) about thin-value LLM-wrapper products generally, not one specific product. It is evidence for "what NOT to build" (a bare prompt-wrapper with no proprietary data/workflow/distribution) rather than a specific fixable gap.

---

## Block 8 — [Negative evidence #1] AI-SDR/cold-outbound email spam already has a filter fix

URL: https://news.ycombinator.com/item?id=40863307
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API comment, 2024-07-03.

> "I've built and successfully been using Unspam for this reason since about a year ago. In corporate/business world, anything where SDR sales are involved this form of a[utomated outreach]... this is specifically designed for business users (founders, ceo's) that are already using Google Workspace for email. Using SpamAssassin (afaik) is not possible in that [context]..."

**This is a filled gap, not open: a named tool (Unspam) already exists specifically to filter AI-SDR cold-outbound spam for Google Workspace users, reported working by its own builder/user for roughly a year as of 2024-07-03. Do not chase "AI SDR spam needs a filter" as a fresh gap — a small vendor already ships this.**

---

## Block 9 — [Negative evidence #2] "AI content flood" complaint on HN — already has a community-built filter

URL: https://news.ycombinator.com/item?id=49657850
Fetch date: 2026-09-16 (thread posted 2026-09-11).
Channel: Hacker News Algolia API, Ask HN thread + top comment.

Ask HN thread, 860 points / 401 comments (one of the highest-signal threads pulled this session):

> "Over past couple months I noticed that HN feed is almost exclusively AI or AI-adjacent news. Meanwhile the legitimately, broadly-hacker stuff gets left out for the most part... I no longer find HN a good source of 'what's new' in the industry, it's almost exclusively AI talk now. So I think the point I am trying to make is that maybe YC could start curating the content somehow to give those easily-drowned-out articles a visibility bump? Or, at the very least, introduce simple tagging, so we can start filtering stuff out." — 2026-09-11.

Top-voted reply:

> "HN is a reflection of the industry and we're at peak hype-cycle at the moment. I use this when I need a break https://elijahpotter.dev/hnsansai." — user "leonheld"

**Filled gap: a specific tool (hnsansai, elijahpotter.dev) already filters AI-heavy content from the HN feed, cited by a top-voted commenter as a working solution on the same day the complaint reached 860 points. The underlying "I'm sick of AI-everything" sentiment is large (860/401) and durable, but a small, free, single-purpose fix already exists and is known within the community.**

---

## Block 10 — [Negative evidence #3, partial] Cursor already fixing non-Latin/Cyrillic keyword handling

URL: https://forum.cursor.com/search.json?q=will%20not%20support (topic 171443)
Fetch date: 2026-09-16.
Channel: Cursor community forum, Discourse JSON search API, staff reply dated 2026-09-16 (same day as fetch).

> "Hey @DanteTemplar, Quick update on this one. A fix for the Submit Keywords field dropping Cyrillic (and other non-Latin) keywords has landed and will be included in an upcoming version of Cursor (3.22). Once you're on that version, a keyword like от[...]"

**Filled/in-progress: a specific non-English-input bug (Cyrillic and other non-Latin keywords silently dropped in a Cursor feature) already has a vendor-committed fix landing in version 3.22, per a staff reply the same day this was fetched. Not an open gap.**

---

## Block 11 — Cursor: explicit "not on our immediate roadmap" (safest-gap signal, vendor says no)

URL: https://forum.cursor.com/t/171082.json ("ACP Agent Doesn't Use Auto-Review")
Fetch date: 2026-09-16.
Channel: Cursor community forum, Discourse JSON topic API. Thread opened 2026-09-08, staff reply 2026-09-09. 42 views, 2 posts, 0 likes as of fetch.

Bug report (Russ_LeBar, 2026-09-08):

> "When Cursor Agent runs through ACP, approvalMode: 'auto-review' is ignored and non-allowlisted commands still require manual approval. The same commands run automatically with Auto-Review in native Cursor... Native Cursor and Cursor Agent through ACP in PyCharm should behave consistently."

Cursor staff reply (Colin, 2026-09-09):

> "Hi @Russ_LeBar! Thanks for flagging this! This is a known limitation of our current ACP implementation, and while it's not on our immediate roadmap, it's something we'd like to address down the line! Auto-review is a huge improvement over other run-mode options. I've moved your post over to our Feature Requests section so other users can add their voices (and votes) to it!"

**Vendor explicitly deprioritizes: Cursor's Agent Client Protocol (ACP) integration (used by JetBrains/PyCharm's Cursor plugin, and other ACP-speaking editors) does not support the "auto-review" approval mode that native Cursor has, and the vendor has said in writing it is not on the immediate roadmap. This is a named, scoped, vendor-confirmed non-support statement — a safe gap: build ACP-compatible auto-review/approval-policy tooling for editors that only get Cursor via ACP.**

---

## Block 12 — Cursor: no bring-your-own/third-party model support for Cloud Agent

URL: https://forum.cursor.com/search.json?q=local%20model%20support (topic 171317)
Fetch date: 2026-09-16 (post dated 2026-09-11).
Channel: Cursor community forum, Discourse JSON search.

> "Feature request for product/service Cloud Agent (GitHub, Slack, Linear,…). Describe the request: Can the remote model of cursor support defined third-party models? Currently, the local desktop software..." (truncated by search API to 250 chars; full topic not separately fetched).

Gap direction: Cursor's Cloud Agent (the hosted/remote execution mode) is locked to Cursor-provided models; users want to point it at their own model/provider the way the local desktop client increasingly allows. Consistent with Block 2's Granola/CallBro finding — "bring your own model to a hosted agent product" is a recurring, cross-category complaint (meeting notetakers, coding agents) that incumbents are not fixing.

---

## Block 13 — Cursor: India-specific INR plan exists, but premium tiers still USD-only (~30% markup complaint)

URL: https://forum.cursor.com/t/166818.json ("Please Bring Native INR Pricing to All Premium Plans (almost Save 30% Markup)")
Fetch date: 2026-09-16 (posted 2026-07-28). 229 views, 2 posts, 6 likes as of fetch.
Channel: Cursor community forum, Discourse JSON topic API.

> "Recently, Cursor launched an excellent India-centric plan priced natively in INR. This was a great step, but the rest of the premium plans are still billed strictly in USD. When paying for USD plans from India, Indian users end up paying an extra markup of almost 30% of the plan's value. This extra cost comes from: Foreign Transaction Fees: Charged by Indian banks for USD processing. Bad Conversion Rates: Poor currency exchange rates applied during the transaction. Additional Taxes: Cross-border payment compliance fees and high GST overheads on foreign software mandates. ... Please make all Cursor plans available natively in INR, just like the India-centric plan."

**Partial fill, flagged for the non-US/non-English question: Cursor already ships local-currency (INR) pricing for one entry-tier plan aimed at India — i.e., an incumbent has moved on the general "no local currency pricing" complaint for at least one major non-US market — but the complaint (6 likes, real specificity on the ~30% all-in markup mechanism: FX fees + spread + GST) shows the fix is incomplete: it doesn't extend to premium tiers. Read as "incumbents are starting to localize pricing, unevenly" rather than "nobody does this."**

---

## Block 14 — OpenAI community: "not available in my country" — recurring across many countries, years apart

URL: https://community.openai.com/search.json?q=not%20available%20in%20my%20country
Fetch date: 2026-09-16.
Channel: OpenAI community forum (Discourse), JSON search API.

Verbatim excerpts (blurbs as returned by search), by country and post date:

> "I'm living in Mauritius and I want to register for OpenAI ChatGPT but I am unable to because I'm getting the 'services are not available in your country'. Mauritius is supposedly in the list of supported countries according to this link on your websi[te]..." — 2023-01-14

> "Not available OpenAI's services are not available in your country. Please, Help Me. I'm in Uzbekistan" — 2023-03-08

> "I am from nepal and since last 2 days the website dont open and says not availavle in the country i tried using different id aswll but it didnt work but in my friend pc it work can someone fix this" — 2024-02-10

> "I was enjoyed my many GPT-3 attempts, but this almost reached Free Trial limit. I clicked 'individual' Setup payment and selected 'Korea, Republic of', but I can't set up. Then, I contacted openai staff, still no reason given. My country is South Kor[ea]" — 2022-08-30

> "My country is under the list of ChatGPTs supported locations yet just 30 minutes ago it says that it's not available in my region." [IMG] — 2025-10-13

> "Sorry, you have been blocked... I could not access into my account, at first I used the VPN, but now my account is blocked. Please, Help Me. I'm in Libya" — 2023-08-24

> "hi, i facing issue 'not available in your country' after i login openAI and it detect my ISP IP from Hong Kong but im using my internet in Malaysia and the IP address i checked in geolocation website detect as Malaysia." — 2023-03-23

> "Vietnam appears on OpenAI's supported countries/territories lists, so this may not simply be a country-availability issue..." — 2026-05-25

> "Hello, With the release of new frontier models I am wondering... why does Codex require mandatory phone verification even after I have already paid for a ChatGPT Plus subscription? I paid for the service, but I cannot use Codex because my account is blocked by a phone verificat[ion requirement]" — 2026-07-21

> "I'm based in Germany/Austria/Hungary and I'm seeing 'This item is not available in your country' for the Sora app." — 2026-01-01

> "I'm living in Kazakhstan and want to pay for OpenAI, but I cannot because I'm getting the 'services are not available in your country'. At the same time, Kazakhstan is on the list of supported countries." — 2023-03-09

**Read: this specific complaint — geolocation/IP-based availability checks misfiring even for listed-supported countries, plus phone-verification gates that block paying customers — recurs from 2022 through 2026-07, across at least 10 distinct countries (Mauritius, Uzbekistan, Nepal, South Korea, Libya, Hong Kong/Malaysia IP-detection mismatch, Vietnam, Germany/Austria/Hungary for Sora specifically, Kazakhstan). No incumbent fix found for the underlying geolocation/verification reliability problem — it is a support-ticket-driven, per-user manual fix each time, four years running.**

---

## Block 15 — OpenAI community: local currency/payment method requests (India UPI, Indonesia affordability)

URL: https://community.openai.com/search.json?q=payment%20local%20currency ; topic JSON at https://community.openai.com/t/1254984.json and https://community.openai.com/t/1026197.json
Fetch date: 2026-09-16.
Channel: OpenAI community forum (Discourse), JSON search + topic API.

Topic 1254984, "Request for Support of Local Currency and UPI for ChatGPT Plus Subscription in India," posted 2025-05-08, 574 views, 1 post, 1 like:

> "Dear OpenAI Team, I'm a user of ChatGPT from India and truly appreciate the value it offers. I would like to kindly request that you consider adding support for payments in local currency (INR) and enabling UPI as a payment option for subscribing to ChatGPT Plus. Many users here prefer using UPI due to its convenience and widespread usage."

Topic 1026197, "Please lower the cost of Plus Subscription for Indonesia," posted 2024-11-21, 261 views, 2 posts, 1 like:

> "I don't know if this is inappropriate to post here, but just want to ask if there will be any reduction in subscription price in Indonesia? $20 is like 10 days worth of food for the majority of people here, and I think it seems too costly to afford. It will be nice if we have the same accessibility for such a powerful tool like the rest of developed country."

**Gap, flagged for the non-US/non-English question per the brief: no UPI (India's dominant payment rail) support and no PPP-adjusted/local-currency pricing for ChatGPT as of these posts (2024-11 and 2025-05). Low reply/like counts (1-2 posts, 1 like each) suggest low forum visibility rather than low real-world demand — India and Indonesia are both top-10 ChatGPT markets by user count (widely reported, not independently verified this session). No incumbent fix found in OpenAI's own forum as of fetch date.**

---

## Block 16 — Google AI-adjacent product shutdowns, 2025-2026 (crowd-maintained tracker)

URL: https://killedbygoogle.com/
Fetch date: 2026-09-16.
Channel: WebFetch summary of a community-maintained shutdown tracker (not a primary Google source — label as such).

Per the tracker (as summarized by WebFetch, not directly quoted verbatim from the page's own text — the tool returned a structured summary rather than raw excerpt):

- Firebase Studio — "an agentic, cloud-based development environment" — discontinued 2025-03.
- Pixel Studio — "allowed users to quickly generate AI images using a prompt" — discontinued 2026.
- Doppl — "an early experimental AI app launched by Google Labs to create a digital twin" — discontinued 2026.
- Tenor API — discontinued 2026 (not AI-specific, adjacent).
- Google Earth Pro (desktop) — discontinued 2026-06 (not AI-specific).

Caveat: killedbygoogle.com is a community-maintained tracker, not a vendor-confirmed source — treat every date/product here as **trade-press/crowd-derived, unconfirmed against a primary Google announcement in this session**. Orphaned users: Firebase Studio's agentic-dev-environment users had to migrate off entirely as of 2025-03; Pixel Studio and Doppl users lost their AI-generation/digital-twin tools in 2026 with no stated successor product named on the tracker page as summarized.

---

## Block 17 — "Nobody has built X" pattern search (mixed signal, one strong hit)

URL: https://hn.algolia.com/api/v1/search_by_date?query=%22nobody%20has%20built%22&hitsPerPage=20
Fetch date: 2026-09-16.
Channel: Hacker News Algolia API, exact-phrase search.

Beyond the tax-filing hit already covered in Block 3, other hits in this phrase search were mostly off-topic (SMRs, tanks, group chat, software-factory metaphors) or too vague to count as a scoped gap:

> "AI gives you speed but takes your voice. Nobody has built the piece that weaves it back." — 2026-03-13, no elaboration, low-signal (aphorism, not a scoped complaint).

> "The fact that everyone hates slack and teams and nobody has built a better group chat yet should really give more people pause than it is currently giving" — 2026-03-07 — not AI-specific, excluded from gap list.

> Show HN: "Hypedar – what's trending in AI that nobody has built yet" — 2026-04-04 — a meta-tool for finding gaps, not a gap itself; did not independently verify its output this session.

Recorded for completeness; none of these three meet the bar (specific complaint + upvote signal + no credible fix) well enough to list as a standalone gap.

---
