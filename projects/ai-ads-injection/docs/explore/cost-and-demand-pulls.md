# Cost and demand pulls — four gaps closed for wave 2a/2b

2026-09-17, wave 1d. Sourced from `../../raw/{cloudflare-workers-limits-and-pricing,ad-verification-oai-adsbot-check,vietnam-ai-visibility-demand,cloudflare-differential-serving-position}.md` (all pulled 2026-09-17, plain fetch + WebSearch, no browser tools — browser work is wave 1b's lane). Does not edit `../plan/idea-set.md`; contradictions are stated here, both sides attributed, never reconciled.

## 1. Cloudflare Workers free tier — exact limits, what forces paid, domain cost

Source: `../../raw/cloudflare-workers-limits-and-pricing.md`. Kind: vendor-reported throughout (Cloudflare docs), except domain prices (vendor-reported, Porkbun — a comparable registrar, not Cloudflare itself).

| Resource | Free | Paid | Overage (Paid) |
|---|---|---|---|
| Workers requests | 100,000/day | No limit; 10M/month included | $0.30/additional million |
| Workers CPU time | 10 ms/invocation | 5 min/invocation cap (default 30s); 30M CPU-ms/month included | $0.02/additional million CPU-ms |
| Workers subrequests | 50/request | 10,000/request | — |
| KV reads | 100,000/day | Unlimited | — |
| KV writes (distinct keys) | 1,000/day | Unlimited | — |
| KV storage | 1 GB | Unlimited | — |
| D1 storage | 500 MB/database, 5 GB/account | 10 GB/database, 1 TB/account | — |
| D1 databases | 10 | 50,000 | — |
| R2 storage | 10 GB-month/month | — | $0.015/GB-month |
| R2 Class A ops (write/list) | 1M/month | — | $4.50/million |
| R2 Class B ops (read) | 10M/month | — | $0.36/million |
| Workers Paid plan base cost | — | **$5/month minimum** | — |

**What forces the paid plan:** Free tier's 100,000 req/day and 10ms CPU/invocation are hard caps with no overage-billing path stated by Cloudflare (the request errors past the cap, per the docs). Paid ($5/mo) is the only tier with an overage model. A single low-traffic instrumented domain doing IP-CIDR match + log is very unlikely to hit either cap.

**Domain cost:** Cloudflare Registrar's own per-TLD price list is not reachable by plain fetch (dashboard-gated; guessed static pricing paths 404'd). Its qualitative claim: "does not mark up domain prices at all," charges "the price charged by registries and ICANN." Used Porkbun as a comparable registrar per instruction: cheapest first-year is **.click at $1.54** (renews $10.81/yr — closest to flat over 2 years among discounted TLDs); **.site/.online at $1.96 first year but $28.84/yr renewal** (18x cliff); **.com flat at $11.08/$11.08**, no promo, no cliff.

**Bears on:** C1, C8 (Cloudflare + a domain is the entire infrastructure cost of the primary pick), and the cross-cutting "no capital" team constraint from `../../../../docs/findings/cross-read.md`. Directly answers wave 2b attack item 3 ("Workers free-tier request/CPU limits were never pulled").

**Status: closed.** Every Workers/KV/D1/R2 number requested was retrieved verbatim. Domain cost is closed via a comparable registrar, not Cloudflare's own list, which remains unreached by plain fetch — flagged, not blocking.

## 2. Ad-verification/brand-safety vendor coverage of OAI-AdsBot

Source: `../../raw/ad-verification-oai-adsbot-check.md`.

| Channel checked | Result | Kind |
|---|---|---|
| DoubleVerify homepage | No mention of ChatGPT/OpenAI/OAI-AdsBot | vendor-reported (absence) |
| IAS (Integral Ad Science) homepage | No mention | vendor-reported (absence) |
| HUMAN Security homepage | HTTP 403 — unreachable, not retried with browser | unreachable |
| Moat/Oracle | Not re-checked (already known discontinued per prior project research) | not pulled |
| Pixalate | Search-only, no hit | search-level absence |
| WebSearch (4 queries) | No vendor-to-OAI-AdsBot connection surfaced in any query | search-level absence |
| Digiday, 2026-06-30 | **Decisive**: OpenAI ads lead David Dugan, on record, quoted verbatim: "I don't have any names to announce" re third-party verification partners | third-party-reported, quoting company-stated remark |
| Digiday, 2026-04-16 | OpenAI building its own first-party conversion pixel; no vendor named | third-party-reported |

**Bears on:** C7 (OAI-AdsBot landing-page observability). This is a clean negative, not a stretch: as of 2026-09-17, checked DoubleVerify, IAS, HUMAN (partially), Moat/Oracle (not repulled), Pixalate, and adtech press, no ad-verification vendor publicly watches OAI-AdsBot or verifies ChatGPT ad delivery. OpenAI's own ads lead confirms, on the record and as recently as 2026-06-30, that no third-party verification partner exists yet. Directly answers wave 2b attack item 9 ("C7 is novel — never checked against ad-verification vendors").

**Status: closed.** The Digiday finding is dated, on-the-record, and directly responsive — a stronger answer than the homepage checks alone would have produced.

## 3. Vietnam-local demand signals for AI answer visibility

Source: `../../raw/vietnam-ai-visibility-demand.md`.

| Signal | Finding | Date | Kind |
|---|---|---|---|
| VN AI usage | ~80% of VN online users used AI in past 3 months; ChatGPT 81% platform share, Gemini 51%, Meta AI 36%, AI Hay (local) 9%, Kiki (local) 3% | Published 2025-08-25, fieldwork 2025-07-20/28 | third-party-reported (press paraphrase of Decision Lab survey) |
| Global chatbot share (context only, NOT Vietnam) | ChatGPT web-traffic share 64-65% (down from ~86% a year earlier), Gemini 21-22% (+315% YoY) | 2026-01-28 | third-party-reported (Similarweb via Vietstock) |
| Local GEO/AEO agencies | **8 confirmed**: TopOnSeek, Hashmeta VN, Nextop, SEODO, seo.danang.vn, Fast Marketing, Midas, and others selling branded "GEO"/"AEO" services targeting ChatGPT/Gemini/AI Overview | as of 2026-09-17 | vendor-reported (agency sites) |
| Local pricing (VND, not converted) | SEODO: từ 18tr / từ 200tr (trọn gói) / từ 350tr (trọn gói); Fast Marketing: 32tr–65tr/tháng (6-12mo terms); Midas: từ 80tr/tháng (12mo); TopOnSeek: quote-only | as of 2026-09-17 | vendor-reported, 4 agencies, conflicting scopes — sit side by side, not averaged |

**Note on conflicting figures:** SEODO's entry tier (từ 18 triệu) sits far below Fast Marketing's cheapest monthly tier (32.000.000đ/tháng, before multiplying by a 6-12 month term) and Midas's single quoted figure (từ 80 triệu/tháng). Package structures (one-time vs monthly vs bundled) differ and are not reconciled here.

**Bears on:** C6 (Vietnamese-language answer-visibility measurement). Wave 2a marked C6 as having **no demand evidence of any kind** — this closes that gap directly and reverses part of the read: local GEO/AEO service branding and local pricing **exist**, contradicting an assumption that "no vendor in the roster claims Vietnamese coverage" implies no Vietnamese-market activity at all (idea-set.md §"C6" support section, which only checked the existing English-language roster, not the Vietnamese market directly). What remains genuinely unsourced: a Vietnam-specific AI-assistant usage/penetration figure current to 2026 (the only VN figure found is 13+ months stale) and any local pricing specific to an *integrity/audit* offering (all agencies found sell visibility, not integrity, matching the pattern already noted for the English-language market).

**Status: partially closed.** Local GEO agency existence and pricing: closed. Fresh (2026) Vietnam-specific usage/penetration figure: still `unknown — checked WebSearch (Vietnamese-language queries) 2026-09-17`.

## 4. Cloudflare's own position on differential serving to AI crawlers

Source: `../../raw/cloudflare-differential-serving-position.md`. Timeboxed per instructions.

| Document checked | Result |
|---|---|
| Website Terms of Use (`cloudflare.com/website-terms/`, eff. 2025-08-01) | No clause on customer differential serving; Section 8 AI-restriction governs scraping *Cloudflare's own site*, not customer zones — re-confirms wave 1's prior finding |
| Self-Serve Subscription Agreement (`cloudflare.com/terms/`, eff. 2025-09-12) | No clause found; Section 2.2.1(f)/(e) govern obscuring Cloudflare's own interface / abusing Cloudflare's own account system, not customer content |
| Service-Specific Terms — Application Services / Bot Management | Bot Management clause is billing-only ("Customer will not be billed for... bad bots"); no content-differentiation clause |
| Cloudflare Blog, "Redirects for AI Training enforces canonical content," 2026-04-17 | **Closest signal found**: a shipped, paid-tier Cloudflare product that itself redirects verified AI *training* crawlers to canonical URLs while, quoted verbatim, "Human traffic, search indexing, and other automated traffic is unaffected" — Cloudflare's own product differentiates by crawler identity |

**Bears on:** the unresolved item flagged in `edge-controls.md` ("unknown — checked cloudflare.com 2026-09-17... whether using [Workers + verified-bot detection] for differential serving is an acceptable use of the product") and, downstream, C1/C3b's Cloudflare-side legal ceiling. No explicit ToS statement found, but Cloudflare ships a first-party feature that normalizes crawler-identity-based differential treatment for one purpose (keeping AI training data current) — a redirect-to-canonical-URL mechanism, not the project's same-URL/different-body mechanism, so it is suggestive precedent, not a direct match or a legal green light.

**Status: partially closed.** No operative ToS sentence exists to quote — recorded as a genuine absence, not a search failure (three separate customer-facing legal documents checked). The blog-product signal is a real finding but doesn't resolve the underlying question; Enterprise Terms and several adjacent Cloudflare blog posts (Bot Preference Sync, Content Signals Policy, "Your site, your rules") were not read, timeboxed as instructed, and may be 1b's adjacent ground per this wave's brief.

## Caveats

- Cloudflare Registrar's own numeric TLD price list was never reached; the domain-cost figures are a comparable registrar's (Porkbun), not Cloudflare's, per `../../raw/cloudflare-workers-limits-and-pricing.md`'s own caveat.
- D1 rows-read/rows-written per day and KV per-invocation operation caps were not fully surfaced by the fetch tool — flagged `unknown` in the raw file rather than guessed.
- Gap 2's HUMAN Security check was blocked (HTTP 403) and Moat/Oracle was not re-pulled this pass (relied on prior project research that it is discontinued) — both are minor incompleteness inside an otherwise decisive negative.
- Gap 3's Vietnam usage figure is 13+ months stale (2025-08 write-up of 2025-07 fieldwork) relative to this 2026-09-17 pull; no fresher Vietnam-specific figure was found. The freshest AI-market figure found (2026-01-28) is global, not Vietnam-specific, and is labeled as such everywhere it's used.
- Gap 4 was explicitly timeboxed per task instructions and is the least complete of the four; it should not be read as an exhaustive legal sweep — wave 1b's policy work is the authority for anything beyond Cloudflare-specific corporate terms.
- No number in this file was guessed. Every unresolved item is labeled `unknown — checked <channel> 2026-09-17` in the underlying raw/ file.
