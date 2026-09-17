# Verify pass 2 — primary-source pulls

2026-09-16. Fact-check pass on `../findings/cross-read.md` "Open questions — pass 2" worklist. Verbatim source blocks. Pulls via direct HTTP fetch (SEC EDGAR, GitHub API — text reproduced from raw response) are marked **[direct fetch]**. Pulls via the WebFetch tool (which summarizes fetched HTML through a small model) are marked **[WebFetch]** — quotes are that tool's extraction, not a raw HTML diff; treat as slightly lower-fidelity than [direct fetch]. WebSearch was exhausted (200/200) partway through this session; items past that point rely on WebFetch against known/guessed URLs only, noted per item.

---

## 1. EU AI Act deferral — Digital Omnibus status and dates

**Pass 1 had:** high-risk obligations deferred from 2026-08-02 to 2027-12-02 (Annex III standalone) and 2028-08-02 (Annex I embedded); Art. 50 transparency and GPAI both "in force 2026-08-02"; caveat that Digital Omnibus amendments were not checked against primary text and status (proposal vs law) was unconfirmed.

**What primary/tier-1 sources say:** The Digital Omnibus is **enacted law**, not a proposal — Regulation (EU) 2026/1744, published in the Official Journal 2026-07-24, entered into force 2026-07-27. The two deferred dates are confirmed exactly as pass 1 had them. But pass 1's "Art. 50 / GPAI — 2026-08-02" line conflates two different obligations: Art. 50 transparency did stay on the original 2026-08-02 schedule (confirmed unaffected by the deferral), but GPAI (Chapter V, Art. 51–56) obligations have applied since **2025-08-02** — a full year earlier — per the original (unamended) Article 113(b), which the Omnibus did not touch.

**Verdict: CORRECTED (GPAI date) / CONFIRMED (Annex III, Annex I, Digital Omnibus now law not proposal) / CONFIRMED (Art. 50 unaffected).**

### 1a. European Commission — AI Omnibus enters into force

Source: https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force — EC official (primary) — fetched via WebFetch 2026-09-16

> [WebFetch extraction] "The AI Omnibus 'enters into force' on 27 July 2026 across the EU—described as already in effect, not a proposal." / "High-risk AI systems in Annex III: 'Rules apply starting 2 December 2027'" / "High-risk AI embedded in physical products (Annex I): 'Rules apply starting 2 August 2028'"

### 1b. EC AI Act Service Desk — Article 113 (primary, official EC, base text not yet updated for Omnibus)

Source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113 — EC official (primary) — fetched via WebFetch 2026-09-16

> [WebFetch extraction, quoting the page's displayed article text] "shall enter into force on the twentieth day following that of its publication" and "shall apply from 2 August 2026." Exceptions: "(a) Chapters I and II shall apply from 2 February 2025"; "(b) Chapter III Section 4, Chapter V, Chapter VII and Chapter XII and Article 78 shall apply from 2 August 2025, with the exception of Article 101"; "(c) Article 6(1) and the corresponding obligations in this Regulation shall apply from 2 August 2027."
>
> Page disclaimer (paraphrased by WebFetch): the displayed Article 113 text "has not yet been updated" to reflect the Digital Omnibus amendments.

Note: clause (b) is the primary-source basis for GPAI (Chapter V) applying from **2025-08-02**, unamended by the Omnibus — this is the correction to pass 1.

### 1c. Gibson Dunn client alert — Omnibus agreement, dates and status

Source: https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ — law firm alert, tier-1 legal press — fetched via WebFetch 2026-09-16

> [WebFetch extraction] "Annex III Standalone High-Risk Systems: '2 December 2027'" / "Annex I Embedded High-Risk Systems: '2 August 2028'" / "Article 50 Transparency Obligations: Remain on original schedule of '2 August 2026' (largely unaffected)" / "GPAI Model Obligations (Articles 51–56): '2 August 2025' (already in force, no change)"
> Status as of the article's writing (2026-05-27): "provisional political agreement" — "Formal adoption and publication in the Official Journal are expected in the coming weeks."

### 1d. Future of Privacy Forum — full implementation timeline

Source: https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/ — non-profit policy research org, tier-1 secondary — fetched via WebFetch 2026-09-16

> [WebFetch extraction] "The AI Omnibus entered into force on 24 July 2026 (published in the Official Journal of the EU)." Timeline table: 2025-02-02 Art. 5 prohibitions + AI literacy; **2025-08-02 GPAI model rules (Chapter V)**, governance, confidentiality, penalties; 2026-08-02 general applicability + Art. 50 transparency (general); 2026-12-02 new CSAM/non-consensual-content prohibition + Art. 50(2) transitional marking for existing systems; 2027-08-02 GPAI models placed pre-2025-08-02 must comply, sandboxes operational; **2027-12-02** Chapter III high-risk applies to Annex III; **2028-08-02** Chapter III applies to Annex I.

Note: minor 3-day discrepancy across sources on "entered into force" (24 vs 27 July) — both figures recur across sources; likely publication (24th) vs. force (27th, "third day after publication... as a matter of urgency" per 1f below) — not a real conflict, recorded side by side.

### 1e. European Parliament Legislative Train Schedule — adoption timeline

Source: https://www.europarl.europa.eu/legislative-train/package-digital-package/file-digital-omnibus-on-ai — European Parliament official (primary) — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Status: "Adopted/Completed." Commission Proposal: 19 November 2025. Council position: 13 March 2026. Parliament position: 14 March 2026 (plenary). Provisional agreement: 7 May 2026 (trilogue). Formal adoption: 29 June 2026 (Council). Final signature: 8 July 2026. "Implementation deadlines were established: December 2, 2027 for standalone high-risk AI systems, and August 2, 2028 for embedded systems."

### 1f. Regulation (EU) 2026/1744 — publication / entry into force mechanics

Source: search-aggregated confirmation of https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng (EUR-Lex primary text) — EUR-Lex direct WebFetch attempts returned empty content three times (see source-index "Not fetched"); the following is corroborated across White & Case, Hunton, NicFab Blog (all tier-1/specialist legal press) — fetched via WebSearch snippet synthesis 2026-09-16

> "Regulation (EU) 2026/1744 was published in the Official Journal on July 24, 2026." "It entered into force on July 27, 2026 — six days before the EU AI Act's original August 2, 2026 high-risk deadline." "The regulation was written to enter into force 'as a matter of urgency' on the third day after publication rather than the standard 20-day window." Full title: "Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 amend[ing] Regulations (EU) 2024/1689, (EU) 2018/1139 and (EU) 2023/1230 as regards the simplification of the implementation of harmonised rules on artificial intelligence (Digital Omnibus on AI)."

### 1g. Article 50 transparency — confirmed unaffected, transition detail

Source: aggregated from Cloud Security Alliance Lab Space note (https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article-50-transparency-20260729/) and related tier-1 legal-blog corroboration — fetched via WebSearch snippet synthesis 2026-09-16

> "Unlike the Annex III high-risk compliance timeline, which the Digital Omnibus package pushed back to December 2, 2027, Article 50 was left out of that deferral: its core transparency and disclosure duties applied on schedule from August 2, 2026." "For generative systems that were already on the market before 2 August 2026, the machine-readable marking under Article 50(2) has a transition period until 2 December 2026."

**Caveat on this item:** EUR-Lex's own consolidated-text and OJ pages (eur-lex.europa.eu) would not render through WebFetch on four separate attempts (empty content each time — likely JS-gated or bot-blocked). The dates and status above are corroborated across five independent tier-1/primary sources (EC's own two pages, European Parliament's own legislative tracker, and two national/international law-firm alerts) that all agree, so confidence is high, but no direct EUR-Lex article-text quote was obtained. Flagged for pass 3 if a direct EUR-Lex quote becomes necessary.

---

## 2. Hermes Agent GitHub repository

**Pass 1 had:** star counts of 100k / 214k / 246k pulled across one week, flagged as not credible; repo identity itself (Hermes Agent vs Hermes model line) already resolved in pass 1.

**What the live GitHub API says [direct fetch, api.github.com]:** the repo exists, is real, and the **highest** of pass 1's three numbers is the current correct one.

**Verdict: CORRECTED (settles which of the three numbers is right) — 246,092 stars confirmed live, not a data-entry error, though still an exceptional number for the repo's age.**

### 2a. Repo identity and stats

Source: https://api.github.com/repos/NousResearch/hermes-agent — GitHub REST API — vendor-reported (platform data) — fetched 2026-09-16 [direct fetch]

```
full_name: NousResearch/hermes-agent
html_url: https://github.com/NousResearch/hermes-agent
description: The agent that grows with you
stargazers_count: 246092
forks_count: 51404
open_issues_count: 43490
watchers_count: 246092
subscribers_count: 958
license: MIT License (spdx_id: MIT)
created_at: 2025-07-22T22:22:28Z
pushed_at: 2026-09-16T15:45:10Z
archived: False
```

Contributors (non-anonymous), via `Link: rel="last"` header on `/contributors?per_page=1&anon=false`: page=401 → **401 contributors**. (An `anon=true` pagination run returned page=3572, i.e. including anonymous/unattributed commit identities — not a contributor headcount; 401 is the real figure.)

### 2b. Latest release

Source: https://api.github.com/repos/NousResearch/hermes-agent/releases/tags/v2026.9.14 — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

> "tag: v2026.9.14" / "name: Hermes Agent v0.21.3 (v2026.9.14)" / "published_at: 2026-09-14T16:04:14Z" / "Patch release. This tag rolls up the ~338 PRs merged since v0.21.2 into a stable tagged release for downstream consumers (Docker images, Hermes Cloud, hosted deployments)." / "the window since v0.21.2 contains 1,036 non-merge commits across 2,642 changed files (+131,690 / −37,096) and 338 merged PRs."

First release not independently dated this pass (release history goes back further than the API page fetched; not itemized here — mark **unknown — checked api.github.com/repos/NousResearch/hermes-agent/releases 2026-09-16, only most-recent releases pulled, oldest not paged through**).

### 2c. Candidate/adjacent repos found (not the match, listed per instructions)

Source: https://api.github.com/orgs/NousResearch/repos — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

Other NousResearch-org repos with "hermes" in the name (all far smaller): `hermes-agent-self-evolution` 5,353 stars; `hermes-paperclip-adapter` 1,887 stars; `Hermes-Function-Calling` 1,472 stars; `Hermes-Bot-Mode` 662 stars (archived per name, not confirmed); `hermes-memory-wiki` 5 stars; various `hermes-plugin-*` repos in single digits to low tens of stars. None is a duplicate of the main repo or a competing "real" Hermes Agent — `NousResearch/hermes-agent` is unambiguous as the primary repo. (A first WebFetch-based GitHub *search* pass, before this direct-API pass, returned a list of unrelated third-party "awesome-hermes-*" community repos on personal accounts (0xNyk, alchaincyf, kaminocorp, etc.) with plausible-sounding star counts — those could not be verified against the API and are suspected to be a WebFetch extraction artifact from a JS-heavy GitHub search page, not real data. Do not cite them.)

### 2d. Hermes Business / Enterprise tiers

**Pass 1 had:** "As of 2026-09-14 Nous added Hermes Business (team tier, shared credit pool, per-member caps) and Hermes Enterprise (self-hosted, contract pricing)."

Source: https://hermes-agent.nousresearch.com — vendor site — company-stated — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Four consumer Nous Portal tiers found: "Free: $0/month ... Free models only ... $0 monthly credits"; "Plus: $20/month ... $22.00 monthly credits — 10% bonus"; "Super: $100/month ... $110.00 monthly credits — 10% bonus"; "Ultra: $200/month ... $220.00 monthly credits — 10% bonus." Separately: "'Business' option available at portal.nousresearch.com/business" and "'Enterprise' option referenced at portal.nousresearch.com/business#hermes-pro." No price disclosed for either.

Source: https://portal.nousresearch.com/business — vendor site — attempted fetch returned **HTTP 429 (rate limited)** on two attempts 2026-09-16 — tier detail (shared credit pool, per-member caps, contract terms, exact launch date) not independently confirmed.

Source: https://nousresearch.com/blog — vendor blog listing — company-stated — fetched via WebFetch 2026-09-16

> [WebFetch extraction] 19 post titles listed (most recent visible: "Refactoring Hermes with 1,393 agents"). **No post titled or matching a Business/Enterprise-tier launch announcement appears in the listing.**

**Verdict on 2d: CONFIRMED that Business and Enterprise ("Hermes Pro") tiers exist as of 2026-09-16 (both referenced on the vendor's own portal). STILL UNKNOWN whether 2026-09-14 is the correct launch date — no dedicated primary announcement (blog post or press release) found; the only thing dated 2026-09-14 confirmed this pass is the v0.21.3 GitHub release, whose notes discuss remote-gateway/session-auth fixes for "Hermes Cloud," not a Business/Enterprise tier launch.**

---

## 3. PyRIT / Garak / DeepTeam / Promptfoo — live repo stats and Promptfoo acquisition

**Pass 1 had:** PyRIT 115 stars from archived Azure/PyRIT (flagged as wrong repo); Garak (NVIDIA) 9.3k stars; DeepTeam and Promptfoo not star-counted; Promptfoo/OpenAI acquisition unverified ("Mar 2026" in cross-read.md open question).

**What the live repos say [direct fetch, api.github.com]:**

**Verdict: CORRECTED (PyRIT) / CONFIRMED (Garak, close match) / CONFIRMED (Promptfoo–OpenAI acquisition, with exact date).**

### 3a. microsoft/PyRIT vs Azure/PyRIT

Source: https://api.github.com/repos/microsoft/PyRIT — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

```
full_name: microsoft/PyRIT | archived: False | stars: 4483 | forks: 889
open_issues: 107 | license: MIT | created_at: 2023-12-12T15:46:28Z
pushed_at: 2026-09-16T15:05:46Z
latest release: v1.1.0, published 2026-09-04T22:19:28Z
contributors (last page marker, per_page=1): page 164 → 164 contributors
```

Source: https://api.github.com/repos/Azure/PyRIT — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

```
full_name: Azure/PyRIT | archived: True | stars: 115 | forks: 27
open_issues: 0 | license: MIT | created_at: 2026-03-25T00:50:57Z (stub/redirect repo, not the original)
```

Pass 1's 115-star figure is confirmed to trace to this archived stub, which is not the live project. **microsoft/PyRIT (4,483 stars) is the correct live repo.**

### 3b. NVIDIA/garak

Source: https://api.github.com/repos/NVIDIA/garak — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

```
full_name: NVIDIA/garak | archived: False | stars: 9268 | forks: 1288
open_issues: 436 | license: Apache-2.0 | created_at: 2023-05-10T18:52:16Z
latest release: v0.17.0, published 2026-09-09T18:56:03Z
contributors (last page marker): page 129 → 129 contributors
```

Pass 1's "9.3k stars" rounds correctly against the live 9,268 — **confirmed, not corrected** (note: `leondz/garak`, the pre-NVIDIA original owner, now 301-redirects to NVIDIA/garak per API — single canonical repo, no ambiguity).

### 3c. confident-ai/deepteam

Source: https://api.github.com/repos/confident-ai/deepteam — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

```
full_name: confident-ai/deepteam | archived: False | stars: 2822 | forks: 459
open_issues: 65 | license: Apache-2.0 | created_at: 2025-03-05T06:34:21Z
latest release: v1.0.9 "First Stable Release", published 2025-11-12T14:18:25Z
contributors (last page marker): page 25 → 25 contributors
```

Not previously star-counted in pass 1 — new data point, CONFIRMED as the correct live repo (name and org match pass 1's tool description).

### 3d. promptfoo/promptfoo

Source: https://api.github.com/repos/promptfoo/promptfoo — GitHub REST API — vendor-reported — fetched 2026-09-16 [direct fetch]

```
full_name: promptfoo/promptfoo | archived: False | stars: 25180 | forks: 2324
open_issues: 633 | license: MIT | created_at: 2023-04-28T15:48:49Z
latest release: 0.123.0, published 2026-09-10T02:34:32Z
contributors (last page marker): page 338 → 338 contributors
```

### 3e. Promptfoo acquired by OpenAI

**Pass 1 / cross-read.md had:** unverified, listed as pass-2 open question ("Mar 2026" placeholder).

Source: https://www.promptfoo.dev/blog/promptfoo-joining-openai/ — company blog, company-stated (primary) — fetched via WebFetch 2026-09-16 (title located via blog listing page at https://www.promptfoo.dev/blog)

> [WebFetch extraction] Date: **March 9, 2026**. "Today we are announcing that Promptfoo has agreed to be acquired by OpenAI." "The closing of the acquisition is subject to customary closing conditions" — no financial terms disclosed. Founders quoted committing that "Promptfoo will remain open source and we will continue to serve users and customers" and to "continue to maintain the open-source suite as a best-in-class red teaming, static scanning, and evals tool for any AI model or application." Founders named: Ian Webster and Michael D'Angelo.

**Verdict: CONFIRMED — acquisition is real, primary-announced, dated 2026-03-09. Deal value not disclosed (company-stated silence, not a filed figure — OpenAI is private, no SEC filing exists).**

---

## 4. Primary pricing pages — AI-search visibility tools

**Pass 1 had:** pricing mostly from comparison blogs; explicit caveat that peec.ai, tryprofound.com/pricing, athenahq.ai, ahrefs.com were not fetched directly.

**Verdict: MIXED — CORRECTED (Profound, AthenaHQ), CONFIRMED (Otterly, directionally Ahrefs), STILL UNKNOWN (Peec AI exact prices, Semrush exact prices).**

### 4a. Profound

Source: https://www.tryprofound.com/pricing — vendor pricing page — vendor-reported — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Only two tiers visible: **"Trial" — Free** (limited AI Marketer credits, 10 prompts run once, ChatGPT only, unlimited seats, no support/SSO); **"Enterprise" — Custom** ("Tailored packages" — AI Marketer credits for whole team, tailored prompt tracking, up to 9 Answer Engines tracked, dedicated support, SSO/SAML + SOC2, unlimited seats). FAQ section separately mentions an "Agency Growth plan" with "400 credits per month per client workspace" but **no price given** for it. No $99, $399, or $499 tier appears anywhere on the current page.

**Pass 1 had:** "$99–$399/mo + Enterprise; also cited '$499/mo Lite' (conflict)." **CORRECTED: as of 2026-09-16 the vendor's own pricing page shows no public self-serve dollar tier at all — Free trial and Enterprise/contact-sales only.** Either the mid tiers were removed/consolidated into Enterprise since pass 1's aggregator snapshots, or those aggregator figures were never accurate. Cannot determine which without a dated historical snapshot (not pursued this pass).

### 4b. Peec AI

Source: https://peec.ai/pricing and https://peec.ai/en/pricing — vendor pricing page — attempted via WebFetch 2026-09-16

> [WebFetch extraction] Four tier names visible — "Starter," "Pro," "Advanced," "Enterprise" — labeled "Monthly," but **no dollar/euro figures rendered** in the fetched content on either URL. Likely client-side-rendered pricing not present in the HTML WebFetch received.

**Verdict: STILL UNKNOWN — unknown, checked https://peec.ai/pricing and https://peec.ai/en/pricing 2026-09-16, tier names visible, no prices retrievable.**

### 4c. AthenaHQ

Source: https://www.athenahq.ai/pricing — vendor pricing page — vendor-reported — fetched via WebFetch 2026-09-16

> [WebFetch extraction] **"Essential (Free)"** — "$25 free credit," 300 included credits, ChatGPT/Perplexity/AI Overviews/Gemini/Copilot, unlimited members. **"Starter ($295/month)"** — "$300/month free credit," 3,600 credits/month, 11 AI models including Claude/Grok/DeepSeek/Mistral, API access add-on, CSV export. **"Enterprise (Custom)"** — custom credit allocation, Knowledge Base, "Oracle" discrepancy detection, Citation Engine, SAML/OIDC SSO, audit logs, multi-region/language, white-glove setup.

**Pass 1 had:** single figure "$595/mo." **CORRECTED — current published entry tier is $295/mo (Starter), with a free tier below it; $595 does not appear on the current page.**

### 4d. Otterly AI

Source: https://otterly.ai/pricing — vendor pricing page — vendor-reported — fetched via WebFetch 2026-09-16

> [WebFetch extraction] **"Lite — $29/month"** (solo marketers/small teams; 15 search prompts; 4 engines — ChatGPT, Google AI Overviews, Perplexity, MS Copilot; unlimited team members; daily tracking). **"Standard — $189/month"** (100 prompts, same 4 engines, API + MCP access, Agent Analytics). **"Premium — $489/month"** (400 prompts, +10,000 GEO URL Audits/mo, 5,000 API requests/mo). **"Enterprise — Custom, 'Starting from $1,000/month'"** (custom prompt tracking, SSO, quarterly GEO health checks, dedicated CSM). Annual plans at 15% discount (Lite $25/mo, Standard $160/mo, Premium $422/mo equivalent).

**Verdict: CONFIRMED — pass 1's "$29/mo" entry point matches exactly; full tier structure now on file.**

### 4e. Ahrefs Brand Radar

Source: https://ahrefs.com/brand-radar — vendor page — vendor-reported — fetched via WebFetch 2026-09-16

> [WebFetch extraction] "Custom Prompts: 'Starts at $50/mo'" with "'$699/MO FOR ALL MODELS'." "AI Visibility Index: '$199/mo'" including "83 prompts/day" and "+2,500 checks/month." Base Ahrefs plans (Lite/Standard/Advanced/Enterprise) each include some free AI-prompt checks (150 to 2,500+/month) bundled at no extra charge.

**Pass 1 had:** "$199/mo per platform or $699/mo all 6, plus Ahrefs base $129–$1,499/mo." **Directionally CONFIRMED** — same $199 and $699 figures appear, though the vendor's own framing ($50/mo entry "Custom Prompts" tier, "AI Visibility Index" as the $199 product) is more granular than pass 1's summary. Base Ahrefs plan range not re-verified this pass.

### 4f. Semrush AI Visibility

Source: https://www.semrush.com/lp/ai-visibility-index/ — vendor page — vendor-reported — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Current umbrella product name: **"Semrush One"** — "The leading platform that unifies SEO authority and AI visibility." Also references "Semrush for Enterprise" and "Semrush MCP." **No price is publicly displayed** on this page; site directs to a 7-day free trial, the general /pricing/ page, or "Book a demo" for Enterprise. Two direct URL guesses (semrush.com/goodcontent/ai-visibility/, semrush.com/features/ai-toolkit/) returned no useful content or 404.

**Verdict: STILL UNKNOWN — unknown, checked semrush.com/lp/ai-visibility-index/ 2026-09-16; product now branded "Semrush One," no separate public price for the AI-visibility component found.**

---

## 5. Profound valuation conflict; Peec AI raise

**Pass 1 had:** Profound $1B (Feb 2026, company-stated) vs $1.8B (Bloomberg-relayed), "different points in time, not reconciled." Peec AI: $29M on file but "$10M ARR, $200M valuation" headline implied an unresolved post-Series-A raise.

**Verdict: BOTH RESOLVED — not conflicts, sequential events, both CONFIRMED via company blog.**

### 5a. Profound — Series C and Series D, primary

Source: https://www.tryprofound.com/blog (listing) and https://www.tryprofound.com/blog/series-d — company blog — company-stated — fetched via WebFetch 2026-09-16

> [WebFetch extraction, Series C mention on listing page] "Profound announced a $96 million Series C at a $1 billion valuation," dated **February 24, 2026**, "led by Lightspeed Venture Partners alongside Sequoia Capital, Kleiner Perkins, Evantic, Saga, and South Park Commons."
>
> [WebFetch extraction, dedicated Series D post] Post-money valuation: **"$1.8B."** Total raised this round: **"$180M in Series D."** Lead investors: **"Sequoia Capital and Kleiner Perkins."** Full list: "Sequoia Capital and Kleiner Perkins with participation from existing investors Lightspeed Venture Partners, Khosla Ventures, Saga Ventures, Evantic, and South Park Commons." Announcement date: **September 16, 2026** (i.e., published the same day this verification pass ran).

**Verdict: CONFIRMED, both figures — $1B was the Feb-2026 Series C valuation; $1.8B is the Sep-16-2026 Series D valuation. Not a conflict; pass 1 had two accurate numbers from two different, unlabeled dates.**

### 5b. Peec AI — funding total and ARR

Source: https://peec.ai/blog/we-raised-21m-series-a-to-help-brands-win-in-ai-search — company blog — company-stated — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Headline: "We raised $21M Series A to help brands win in AI search," by Marius Meiners, **November 18, 2025**. "Total funding to date: $29 million (including seed round)." "The seed round was 'led by 20VC in July 2025.'" ARR trajectory quoted directly: **"$0 to $4M+ ARR in 10 month[s]"**. Traction: "onboarded 1,300+ brands and agencies," "adding 300+ customers per month" since a February 2025 launch. Investor list for the Series A: Singular (lead), Antler, Combination VC, identity.vc, S20. Founders named in this post: Daniel Drabo, Tobias Siwonia, Marius Meiners (Co-founder & CEO).

**Verdict: CORRECTED / CONFIRMED, mixed.** Total funding **CONFIRMED at $29M** (seed + Series A combined, per the company's own post — pass 1's $29M figure was right, just unlabeled as a two-round total). Founder list **CONFIRMED** as TechCrunch had it (Drabo, Siwonia, Meiners) — Tracxn's "Gorbacheva" name is not corroborated by this primary source and looks like a Tracxn error. ARR figure is a **new conflict, not resolved**: company's own November 2025 post says "$4M+ ARR," while pass 1's caveat cited a separate, unsourced "$10M ARR" headline. Both recorded side by side; the $10M claim's origin was not found this pass either — **unknown — checked peec.ai/blog 2026-09-16, only the $4M+ figure is company-stated on the record.**

---

## 6. Decawork

**Pass 1 had:** YC S26, agent identity/governance for IT, two founders, undisclosed pricing.

Source: https://www.ycombinator.com/companies/decawork — Y Combinator official company page — primary/company-stated — fetched via WebFetch 2026-09-16

> [WebFetch extraction] "Training company-specific models that approve AI actions." Batch: **Summer 2026**. Founders: **Aman Raj (CEO)** and **Sarthak Aggarwal (CTO)**. Team size: 2. Status: Active. Location: San Francisco. Pitch: "The company trains small, customized AI models that evaluate and authorize agent actions in real time based on organizational policies, task context, and historical behavior." Problem framing: "Autonomous AI agents need system access but their actions can be unpredictable... companies lack a scalable way to manage this beyond fixed rules or manual approval at each step." Mechanism: "Decawork routes API requests through its platform, where company-specific policy models evaluate proposed actions against organizational guidelines before execution occurs."

Source: https://decawork.ai — live company site — company-stated — fetched via WebFetch 2026-09-16 (note: https://decawork.com and https://www.decawork.com both 404 — decawork.ai is the correct live domain)

> [WebFetch extraction] Tagline: "Company-specific models that approve AI actions in real time, based on your policies and the task at hand." No pricing information displayed anywhere on the site. Demo/example workspace shows "Gateway healthy" status and active agents spanning marketing, recruiting, HR, IT, security, finance, and engineering departments — broader than "IT approval gate" alone. Traction badges: "Backed by [Y Combinator]" and a Product Hunt feature; no user/customer counts or revenue disclosed.

**Verdict: CONFIRMED (YC batch, founders, team size, no pricing) / CORRECTED (scope — Decawork's own site frames the product across marketing/HR/IT/security/finance/engineering policy approval, not IT-governance-specific as pass 1's one-line summary implied) / STILL UNKNOWN (any traction numbers — none disclosed anywhere found).**

---

## 7. AI-security deal values — filed vs reported

**Pass 1 had:** only Protect AI/Palo Alto ($634.5M) as SEC-filed; all others analyst-derived, reported, or aggregator-only.

**Verdict: mostly CONFIRMED-BUT-UNDISCLOSED-VALUE (the acquisitions themselves now have a primary or SEC citation; dollar figures still do not appear in any primary document found) — two targets (Cato/Aim Security, Cranium/AIceberg) remain STILL UNKNOWN / not fetched.**

### 7a. Cisco → Robust Intelligence

Source: https://www.sec.gov/Archives/edgar/data/858877/000119312524257224/d875468dex991.htm — Cisco 8-K Exhibit 99.1 (Q1 FY2025 earnings release), filed 2024-11-13 — SEC-filed (primary) — fetched 2026-09-16 [direct fetch]

> "In the first quarter of fiscal 2025, we closed the following acquisitions: • DeepFactor, Inc., a privately held cloud-native application security company • Robust Intelligence, Inc., a privately held AI security solutions company"

No dollar figure for either deal appears anywhere in this exhibit (checked programmatically for every "$" in the document; all dollar figures present are Cisco's own revenue/EPS guidance and buyback totals, none attached to "Robust Intelligence").

**Verdict: CONFIRMED-FILED that the acquisition closed in Q1 FY2025 (i.e., by 2024-11-13). Deal value (~$400M, pass 1's figure) is STILL analyst-derived/reported-only — not present in this or any other filing found.**

### 7b. Snyk → Invariant Labs

Source: https://snyk.io/news/snyk-acquires-invariant-labs-to-accelerate-agentic-ai-security-innovation/ — Snyk company newsroom — company-stated (primary) — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Publication date: **June 24, 2025**. "This acquisition is an important integration into Snyk's recently launched AI Trust Platform that adds the ability to secure applications from emergent threats," said Peter McKay, CEO of Snyk. Brings in Invariant Labs' research team and "Guardrails" security layer. "No financial terms were disclosed."

**Verdict: CONFIRMED (date refined to 2025-06-24, from pass 1's "Jun 2025"). Value: CONFIRMED-BUT-UNDISCLOSED (company explicitly declines to state a figure) — matches pass 1's "undisclosed" label exactly.**

### 7c. CrowdStrike → Pangea

Source: https://www.sec.gov/Archives/edgar/data/1535527/000153552726000018/crwd-20260416.htm — CrowdStrike 8-K (executive-compensation/CEO-award related), items 5.02/7.01/9.01, filed 2026-04-21 — SEC-filed (primary) — fetched 2026-09-16 [direct fetch]

> "CrowdStrike's most recent acquisitions of Pangea, Onum, SGNL, and Seraphic Security collectively extend the Falcon platform into AI application security, network data intelligence, dynamic identity and access control, and browser security, each addressing a distinct and growing market opportunity."

An EDGAR full-text search scoped to CrowdStrike's CIK for "Pangea" in 8-K filings dated 2025-08-01 to 2025-10-31 (the deal's reported timeframe) returned **zero hits** — no dedicated acquisition 8-K was filed for Pangea specifically (likely deemed immaterial for a standalone Item 2.01 disclosure); the only SEC mention found is this later, incidental reference.

**Verdict: CONFIRMED-FILED that the acquisition happened (named in a 2026-04-21 SEC filing) — but no primary source (filed or press) with a dollar figure was found. Pass 1's ~$260M stays analyst-derived/reported-only.**

### 7d. Check Point → Lakera

Source: https://www.sec.gov/Archives/edgar/data/1015922/000117891325003335/exhibit_99-1.htm — Check Point 6-K Exhibit 99.1, filed 2025-09-16 — SEC-filed (primary) — fetched 2026-09-16 [direct fetch]

> "Check Point Acquires Lakera to Deliver End-to-End AI Security for Enterprises." "Redwood City, CA — September 16, 2025 — Check Point® Software Technologies Ltd. (NASDAQ: CHKP)... today announced it has entered into an agreement to acquire Lakera, one of the world's leading AI-native security platforms for Agentic AI applications." Quote from CEO Nadav Zafrir. No dollar figure anywhere in the exhibit (checked programmatically — zero "$" characters in the document).

**Verdict: CONFIRMED-FILED, date exact match to pass 1 (2025-09-16). Value: CONFIRMED-BUT-UNDISCLOSED-IN-FILING — pass 1's ~$300M stays analyst-derived, not filed.**

### 7e. F5 → CalypsoAI

Source: https://www.sec.gov/Archives/edgar/data/1048695/000104869525000143/ex991-item7019112025.htm — F5 8-K Exhibit 99.1, filed 2025-09-11 — SEC-filed (primary) — fetched 2026-09-16 [direct fetch]

> "F5 to acquire CalypsoAI to bring advanced AI guardrails to large enterprises." "SEATTLE, WASHINGTON AND DUBLIN, IRELAND – SEPTEMBER 11, 2025 – F5 (NASDAQ: FFIV)... today announced its intent to acquire a pioneer in enterprise AI security." Quote from CEO François Locoh-Donou. No dollar figure anywhere in the exhibit (checked programmatically — zero "$" characters).

**Verdict: CORRECTED — pass 1's table lists "$180M" for this deal without a label; the $180M figure does NOT appear in F5's own SEC-filed announcement. It is press-reported (e.g. trade press), not filed. Relabel as reported-only, not filed, pending a source for the $180M figure.**

### 7f. Anaconda → Enkrypt AI

Source: https://www.anaconda.com/blog/anaconda-acquires-enkrypt-ai — company blog — company-stated (primary) — fetched via WebFetch 2026-09-16

> [WebFetch extraction] Date: **August 4, 2026**. "Today, Anaconda is acquiring Enkrypt AI, the AI security and safety layer used by enterprises to secure, monitor, and govern their complete AI agent stack." No financial terms disclosed anywhere in the post.

**Verdict: CONFIRMED (date refined to 2026-08-04, from pass 1's "Aug 2026"). Value: CONFIRMED-BUT-UNDISCLOSED — matches pass 1's "undisclosed" label.**

### 7g. Cato Networks → Aim Security — NOT CONFIRMED THIS PASS

Attempted: https://www.catonetworks.com/news/cato-networks-acquires-aim-security/ (guessed slug, empty/no content), https://www.catonetworks.com/news/ (empty), https://www.catonetworks.com/blog/ (empty), https://www.catonetworks.com/news (empty) — all via WebFetch 2026-09-16, all returned no usable content (site likely JS-rendered / not crawlable by the fetch tool). WebSearch was unavailable (budget exhausted) to locate the correct press-release URL.

**Verdict: STILL UNKNOWN — unknown, checked catonetworks.com/news and /blog 2026-09-16 (multiple URL guesses, all empty). Pass 1's ~$300–350M stays reported-only, unconfirmed against any primary this pass.**

### 7h. Cranium AI → AIceberg — NOT CONFIRMED THIS PASS

Attempted: https://craniumai.com/news/cranium-acquires-aiceberg (guessed slug, 404), https://craniumai.com/blog (empty), https://craniumai.com (empty) — all via WebFetch 2026-09-16. Same failure mode as 7g.

**Verdict: STILL UNKNOWN — unknown, checked craniumai.com, /blog, and a guessed /news slug 2026-09-16, all empty or 404. Pass 1's "undisclosed (aggregator-derived)" stands, unconfirmed against any primary this pass.**

### 7i. Palo Alto Networks → Protect AI — carried forward, not re-checked

Pass 1's $634.5M SEC-filed figure was not re-fetched this pass (no new information found or sought); it stands as pass 1 recorded it.

---

## Session note on WebSearch budget

This session's WebSearch tool was exhausted (200/200 calls) roughly a third of the way through this worklist (after item 1 and the start of item 2). Every item from mid-item-2 onward relies on: (a) direct HTTP fetches via `curl` to GitHub's and SEC EDGAR's public REST/full-text-search APIs (labeled **[direct fetch]** above — high reliability, raw JSON/HTML), and (b) the WebFetch tool against URLs either already known from pass 1, guessed from vendor domain conventions, or discovered via link references inside other fetched pages. No further WebSearch-based discovery was possible. Where a guessed URL 404'd or returned empty, this is recorded per-item above and again in the source index below.
