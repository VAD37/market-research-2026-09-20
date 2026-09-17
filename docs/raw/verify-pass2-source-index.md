# Verify pass 2 — source index

2026-09-16. Every URL touched during the pass-2 verification worklist, grouped by worklist item. Paired with `verify-pass2-pulls.md`, which has the verbatim quotes and per-item verdicts. **[direct fetch]** = raw curl against a public API (GitHub REST, SEC EDGAR full-text search / EDGAR archive) — high reliability. **[WebFetch]** = fetched through the WebFetch tool, which summarizes HTML via a small model — treat as slightly lower fidelity. **[WebSearch]** = search-result synthesis; exhausted at 200/200 calls partway through item 2, unavailable for everything after.

## 1. EU AI Act deferral

- https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force — EC official — [WebFetch] — used, confirmed dates + in-force status
- https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113 — EC official — [WebFetch] — used, base Art. 113 text incl. GPAI 2025-08-02 clause
- https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — law firm — [WebFetch] — used, dates + status-at-time-of-writing
- https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/ — policy non-profit — [WebFetch] — used, full timeline table
- https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-omnibus-on-ai — EU Parliament official — [WebFetch] — used, legislative stage dates
- https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/ — industry non-profit — [WebSearch snippet] — used, Art. 50 unaffected + transition detail
- https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng — EUR-Lex primary — [WebSearch] — surfaced, not independently fetched with content
- Various law-firm alerts corroborating Reg. (EU) 2026/1744 publication/force dates: White & Case (https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act), Hunton (https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force), NicFab Blog (https://www.nicfab.eu/en/posts/digital-omnibus-ai-official-journal/) — [WebSearch snippet synthesis] — used for cross-corroboration only, no direct fetch of any

### Not fetched — open for pass 3 (item 1)
- https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng — [WebFetch] — returned empty content (likely JS-gated / bot-blocked)
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202601744 — [WebFetch] — returned empty content
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02024R1689-20260727 (consolidated AI Act text) — [WebFetch] — returned empty content
- https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32026R1744 — [WebFetch] — returned empty content
- https://eur-lex.europa.eu/eli/reg/2026/1744/oj — [WebFetch] — returned empty content
- https://artificialintelligenceact.eu/the-act/ — [WebFetch] — page fetched but did not contain the timeline detail needed

## 2. Hermes Agent GitHub

- https://api.github.com/repos/NousResearch/hermes-agent — [direct fetch] — used, full repo stats
- https://api.github.com/repos/NousResearch/hermes-agent/releases/tags/v2026.9.14 — [direct fetch] — used, latest release notes
- https://api.github.com/repos/NousResearch/hermes-agent/contributors (paginated, anon=true and anon=false) — [direct fetch] — used, contributor counts
- https://api.github.com/orgs/NousResearch/repos — [direct fetch] — used, full repo list w/ stars
- https://api.github.com/search/repositories?q=hermes-agent+org:NousResearch — [direct fetch] — used, confirms single canonical repo
- https://hermes-agent.nousresearch.com — [WebFetch] — used, Portal pricing tiers + Business/Enterprise links
- https://nousresearch.com/blog — [WebFetch] — used, checked for Business/Enterprise launch post (not found)
- https://nousresearch.com — [WebFetch] — used, general check, no Business/Enterprise mention
- https://github.com/NousResearch/hermes-agent — [WebFetch] — used, README description cross-check
- https://github.com/NousResearch — [WebFetch] — used pre-API-pivot; results later superseded/discounted by direct API pull (see caveat in pulls file 2c)
- https://github.com/search?q=hermes+agent+nous&type=repositories — [WebFetch] — used pre-API-pivot; results discounted (suspected extraction artifact, see pulls file 2c)

### Not fetched / failed — open for pass 3 (item 2)
- https://portal.nousresearch.com/business — [WebFetch] — HTTP 429 (rate limited) on two attempts; Business/Enterprise tier prices and exact 2026-09-14 launch date still unconfirmed
- https://hermes-agent.nousresearch.com/pricing — [WebFetch] — HTTP 404

## 3. PyRIT / Garak / DeepTeam / Promptfoo

- https://api.github.com/repos/microsoft/PyRIT (+ /releases/latest, /contributors) — [direct fetch] — used
- https://api.github.com/repos/Azure/PyRIT — [direct fetch] — used, confirms archived stub
- https://api.github.com/repos/NVIDIA/garak (+ /releases/latest, /contributors) — [direct fetch] — used
- https://api.github.com/repos/leondz/garak — [direct fetch] — used, confirms 301/redirect to NVIDIA/garak
- https://api.github.com/repos/confident-ai/deepteam (+ /releases/latest, /contributors) — [direct fetch] — used
- https://api.github.com/repos/promptfoo/promptfoo (+ /releases/latest, /contributors) — [direct fetch] — used
- https://www.promptfoo.dev/blog — [WebFetch] — used, located acquisition post title/slug
- https://www.promptfoo.dev/blog/promptfoo-joining-openai/ — [WebFetch] — used, full acquisition announcement

### Not fetched / failed — open for pass 3 (item 3)
- https://www.promptfoo.dev/blog/promptfoo-is-joining-openai/ — [WebFetch] — HTTP 404 (wrong slug guess; correct slug found via blog listing instead)
- https://openai.com/index/promptfoo/ — [WebFetch] — HTTP 403 Forbidden

## 4. AI-search visibility pricing pages

- https://www.tryprofound.com/pricing — [WebFetch] — used (fetched twice, same result both times)
- https://peec.ai/pricing — [WebFetch] — used, no prices retrievable
- https://peec.ai/en/pricing — [WebFetch] — used, no prices retrievable
- https://peec.ai — [WebFetch] — used, homepage has no pricing content, confirms link-only
- https://www.athenahq.ai/pricing — [WebFetch] — used
- https://otterly.ai/pricing — [WebFetch] — used
- https://ahrefs.com/brand-radar — [WebFetch] — used
- https://www.semrush.com/lp/ai-visibility-index/ — [WebFetch] — used, "Semrush One" naming confirmed, no price

### Not fetched / failed — open for pass 3 (item 4)
- https://www.semrush.com/ai-visibility/ — [WebFetch] — HTTP 404
- https://www.semrush.com/goodcontent/ai-visibility/ — [WebFetch] — resolved to generic Semrush Holdings page, no product-specific content
- https://www.semrush.com/features/ai-toolkit/ — [WebFetch] — HTTP 404
- Peec AI's exact euro/dollar figures — no working URL found this pass; pricing appears to be client-side-rendered and not present in fetched HTML

## 5. Profound valuation; Peec AI raise

- https://www.tryprofound.com/blog — [WebFetch] — used, Series C + Series D mentions on listing page
- https://www.tryprofound.com/blog/series-d — [WebFetch] — used, full Series D announcement
- https://peec.ai/blog — [WebFetch] — used, located Series A post title/slug
- https://peec.ai/blog/we-raised-21m-series-a-to-help-brands-win-in-ai-search — [WebFetch] — used, full Series A announcement incl. total funding + ARR

### Not fetched — open for pass 3 (item 5)
- The origin of pass 1's "$10M ARR, $200M valuation" headline for Peec AI — not located this pass. Company's own November 2025 post states $4M+ ARR; no primary source for $10M ARR / $200M valuation was found. Needs a targeted WebSearch in pass 3 once budget resets.

## 6. Decawork

- https://www.ycombinator.com/companies/decawork — [WebFetch] — used, primary YC company page
- https://decawork.ai — [WebFetch] — used, live company site
- https://decawork.com — [WebFetch] — HTTP 404 (not the live domain)
- https://www.decawork.com — [WebFetch] — HTTP 404 (not the live domain)

## 7. AI-security deal values

- https://www.sec.gov/Archives/edgar/data/858877/000119312524257224/d875468dex991.htm — Cisco 8-K EX-99.1 — [direct fetch] — used (Robust Intelligence)
- https://efts.sec.gov/LATEST/search-index?q=%22Robust%20Intelligence%22&forms=8-K&ciks=0000858877 — SEC EDGAR full-text search — [direct fetch] — used to locate the above
- https://snyk.io/news/ — [WebFetch] — used, located Invariant Labs press release slug
- https://snyk.io/news/snyk-acquires-invariant-labs-to-accelerate-agentic-ai-security-innovation/ — [WebFetch] — used, full announcement
- https://www.sec.gov/Archives/edgar/data/1535527/000153552726000018/crwd-20260416.htm — CrowdStrike 8-K — [direct fetch] — used (Pangea, incidental mention)
- https://efts.sec.gov/LATEST/search-index?q=%22Pangea%22&forms=8-K&ciks=0001535527 (and a date-scoped variant, 2025-08-01 to 2025-10-31) — SEC EDGAR full-text search — [direct fetch] — used; date-scoped query returned zero hits (no dedicated Pangea 8-K exists)
- https://www.sec.gov/Archives/edgar/data/1015922/000117891325003335/exhibit_99-1.htm — Check Point 6-K EX-99.1 — [direct fetch] — used (Lakera)
- https://efts.sec.gov/LATEST/search-index?q=%22Lakera%22 — SEC EDGAR full-text search — [direct fetch] — used to locate the above
- https://www.sec.gov/Archives/edgar/data/1048695/000104869525000143/ex991-item7019112025.htm — F5 8-K EX-99.1 — [direct fetch] — used (CalypsoAI)
- https://efts.sec.gov/LATEST/search-index?q=%22CalypsoAI%22 — SEC EDGAR full-text search — [direct fetch] — used to locate the above
- https://www.anaconda.com/blog/anaconda-acquires-enkrypt-ai — [WebFetch] — used (Enkrypt AI)
- https://efts.sec.gov/LATEST/search-index?q=%22Aim%20Security%22 — SEC EDGAR full-text search — [direct fetch] — used, only noise hits (unrelated 2005-era "AIM" filings)
- https://efts.sec.gov/LATEST/search-index?q=%22Enkrypt%22 — SEC EDGAR full-text search — [direct fetch] — used, only noise hits (unrelated 2003-era filing)
- https://efts.sec.gov/LATEST/search-index?q=%22AIceberg%22 — SEC EDGAR full-text search — [direct fetch] — used, zero hits
- https://efts.sec.gov/LATEST/search-index?q=%22Invariant%20Labs%22 — SEC EDGAR full-text search — [direct fetch] — used, zero hits (Snyk is private, expected)
- https://efts.sec.gov/LATEST/search-index?q=%22Pangea%22 (unscoped) — SEC EDGAR full-text search — [direct fetch] — used, mostly noise (unrelated "Pangea" company name hits), CrowdStrike hit extracted separately above

### Not fetched / failed — open for pass 3 (item 7)
- https://www.catonetworks.com/news/cato-networks-acquires-aim-security/ — [WebFetch] — guessed slug, empty content
- https://www.catonetworks.com/news/ — [WebFetch] — empty content
- https://www.catonetworks.com/news — [WebFetch] — empty content
- https://www.catonetworks.com/blog/ — [WebFetch] — empty content
- https://craniumai.com/news/cranium-acquires-aiceberg — [WebFetch] — guessed slug, HTTP 404
- https://craniumai.com/blog — [WebFetch] — empty content
- https://craniumai.com — [WebFetch] — empty content
- Cato Networks and Cranium AI's press/newsroom pages both appear to be JS-rendered SPAs that return no usable static content to the fetch tool. Needs either a browser-automation tool (claude-in-chrome) or WebSearch (budget exhausted this session) in pass 3 to find the correct press-release URLs.
- Palo Alto Networks → Protect AI ($634.5M) — not re-checked this pass; pass 1's SEC-filed citation was not re-verified or re-fetched (no new information sought, carried forward as-is).

## Session-level note

WebSearch quota (200 calls) was exhausted early in item 2, shared across this session. Items 2 (partially) through 7 relied on: direct API/EDGAR fetches (most reliable), WebFetch against known or guessed vendor URLs, and a small number of pre-exhaustion WebSearch snippet results carried into item 1. Any "not fetched" line above involving a guessed URL should be re-attempted in pass 3 with WebSearch available, or via a browser-automation tool for JS-rendered sites (Cato Networks, Cranium AI, Peec AI's pricing page).
