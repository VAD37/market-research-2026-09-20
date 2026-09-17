# Services lane — source index (pass 2)

Every URL touched during pass 2, grouped by theme. Pulls file: `services-lane-pulls.md`. One line each, one clause. WebSearch budget for this session was exhausted mid-pass (200/200) — remainder of the research ran on WebFetch against known/derived URLs only; this constrained coverage on themes 2 and 3 in particular (see "Not fetched" below).

## Real engagement pricing

- https://sam.gov/workspace/contract/opp/b13eeb1c32b14563bee9f39cadf3a7fb/view — USAC pentest-as-a-service RFP, page needs JS, only title/deadline confirmed via search snippet.
- https://deepstrike.io/blog/penetration-testing-cost — full vendor pentest price table by asset type, methodology, compliance, org size.
- https://www.synack.com/blog/penetration-testing-cost/ — pentest price table incl. red team and PTaaS tiers, market average $18,300.
- https://www.getastra.com/ai-pentest — explicit AI pentest price line, $5k–$50k+.
- https://www.getastra.com/blog/security-audit/ai-penetration-testing-cost/ — fetch returned no extractable pricing (nav shell only).
- https://www.cobalt.io/pricing — published $3,500 autonomous-pentest price point, credit model, AI&LLM Pentest SKU unpriced.
- https://www.cobalt.io/pricing (duplicate check) — confirms tier pricing is quote-only above the autonomous tier.
- https://www.mindfort.ai/blog/best-pentera-alternatives — Pentera ~$100K avg deal / ~$50K/yr, NodeZero ~€35K/yr, both third-party estimates.
- https://www.brightdefense.com/resources/penetration-testing-pricing/ — generic $150–$350+/hr, $1,200–$3,000+/day rates (search snippet only).
- https://www.blazeinfosec.com/post/how-much-does-penetration-testing-cost/ — $5,000–$35,000 typical range (search snippet only).
- https://www.redfoxsec.com/blog/how-much-does-web-application-penetration-testing-cost-2026-pricing-guide — web-app-specific cost guide, not separately fetched in full.
- https://penetrationtestingcost.com/ — "$5K-$100K+, Avg $18,300" headline (search snippet only, corroborates Synack figure).
- https://www.stingrai.io/blog/penetration-testing-cost-per-hour-2026 — hourly/day-rate guide, not separately fetched in full.
- GSA CALC tool (attempted, no working URL resolved) — returns no data as of 2026-09-16, GSA schedule labor rates unobtainable through this channel.

## Government / institutional procurement (strongest evidence tier)

- https://github.com/Nandanhegde1/govai-contracts — methodology for the federal AI contract tracker (USAspending + SAM.gov, NAICS-filtered, 700 records).
- https://govai-contracts.nandanhegde1096.workers.dev/ — live tracker homepage, 10 most recent/trending awards.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=red%20team — HiddenLayer $1.80M USAF red-team workbench contract.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=adversarial — HiddenLayer $1.25M + Peraton Labs $16.60M DARPA (false positive on keyword).
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=penetration%20testing — zero hits, load-bearing negative finding.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=security%20assessment — CACI NSS $1.29M + Aperio Global $1.54M DHS AI-security-support contracts.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=vulnerability — Aperio Global $1.54M contract detail.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=prompt%20injection — zero hits.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=LLM%20security — AI2 Incorporated $1.35M USAF secure-LLM contract.
- https://www.contractsfinder.service.gov.uk/Notice/2a11df1e-7a63-4596-8f6a-7a11aa87405c — UK Contracts Finder notice, HTTP 403 on fetch, not retrieved.
- USAspending.gov, SAM.gov direct search UIs — attempted via WebSearch (budget exhausted) and WebFetch (JS-rendered SPA, empty); not independently queried beyond the govai-contracts index above.

## Demand channel — how firms get hired

- https://genai.owasp.org/resource/owasp-vendor-evaluation-criteria-for-ai-red-teaming-providers-tooling-v1-0/ — OWASP buyer-side vendor evaluation criteria, published 2026-02-04.
- https://www.aigl.blog/vendor-evaluation-criteria-for-ai-red-teaming-providers-tooling/ — secondary discussion of the same OWASP document, not independently fetched.
- https://www.pentesttesting.com/ai-red-teaming-vendor-questionnaire/ — vendor-questionnaire commentary, composite scenario quoted in pulls #42.
- Vendor security questionnaire / CAIQ AI field — searched, no confirmed CAIQ version update found naming AI red-teaming.

## Compliance / regulatory mandate check

- https://www.dfs.ny.gov/industry_guidance/industry_letters — NYDFS industry-letters index, confirmed titles/dates for both AI letters.
- https://www.dfs.ny.gov/industry-guidance/industry-letters/20260521-heightened-cybersecurity-risks-assoc-with-frontier-ai-models — fetched in full, 2026-05-21 frontier-AI cybersecurity advisory.
- https://www.dfs.ny.gov/industry_guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks — 404 on fetch, title/date confirmed via index only.
- https://www.dfs.ny.gov/industry_guidance/industry_letters/il20241016_cyber_risk_ai — 404, alternate slug guess.
- https://www.dfs.ny.gov/industry-guidance/industry-letters/20241016-cyber-risks-ai-and-strategies-combat-related-risks — 404, alternate slug guess.
- https://www.fca.org.uk/firms/innovation/ai-lab — FCA AI Lab / AI Live Testing sandbox program, fetched in full.
- https://www.mas.gov.sg/news/media-releases — MAS site returned a service-unavailable error page, no content retrieved.
- https://www.mas.gov.sg/publications — same MAS error page, no content retrieved.
- https://cloudsecurityalliance.org/articles/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework — ISO 42001 audit-stage detail, dated 2025-05-08.
- ISO/IEC 42006:2025 and ANAB/Schellman accreditation — covered via WebSearch synthesis, no single primary URL independently re-fetched.
- SOC 2 Type II AI-evidence gap — covered via WebSearch synthesis of futureagi.com, konfirmity.com, soc2vendors.com, knowlee.ai; none individually re-fetched for full text.
- FedRAMP AI guidance — https://www.fedramp.gov/blog/ fetch returned empty content; not otherwise located this pass.
- Cyber insurance AI riders/questions — https://aisafeiq.com/blog/cyber-insurance-7-ai-questions-2026 fetched in full, dated 2026-05-24.
- Cyber insurance questionnaire growth — WebSearch synthesis of gogravity.net, acaglobal.com, denexus.io, getanchor.ai, wiley.law, buildmvpfast.com; none individually re-fetched.

## Supply side — bounty and freelance earnings

- https://wraith.sh/learn/ai-bug-bounty-programs — cross-program AI bounty payout table (OpenAI, Anthropic, Google, Microsoft, xAI).
- https://wraith.sh/learn/state-of-llm-bug-bounties-2026 — found via search, not independently fetched in full.
- https://bug-bounties.as93.net/learn/ai-llm-security-testing-for-bounties/ — found via search, not fetched.
- https://bugcrowd.com/engagements/openai-safety — fetch returned nav shell only, payout figures cross-confirmed via search synthesis instead.
- https://bugcrowd.com/engagements/openai — general OpenAI Bugcrowd program, not separately fetched.
- https://www.hackerone.com/blog/anthropic-expands-their-model-safety-bug-bounty-program — fetched in full, program history and $550,835 total-paid figure.
- https://www.hackerone.com/product/ai-red-teaming — found via search, not fetched.
- https://www.hackerone.com/reports/hacker-powered-security-report — 404 on fetch, not retrieved.
- https://edwinkwan.com/2026/05/22/hackerone-slashes-bug-bounty-payouts-as-ai-floods-open-source-security-programs/ — fetched in full, IBB payout-cut figures (counter-evidence).
- https://xbow.com/blog/top-1-how-xbow-did-it — fetched in full, leaderboard/report metrics.
- https://xbow.com/blog/democratizing-offensive-security — found via search, not separately fetched.
- https://xbow.com/blog/xbow-on-hackerone-whats-next — found via search, not separately fetched.
- https://xbow.com/pricing — fetched in full, "coverage without the headcount" quote.
- https://it.slashdot.org/story/25/07/05/1847237/xbows-ai-powered-pentester-grabs-top-rank-on-hackerone-raises-75m-to-grow-platform — title-only, $75M round dated 2025-07-05 per URL slug.
- https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker — title-only, $120M round dated 2026-03-18 per URL slug.
- https://www.crunchbase.com/organization/xbow — HTTP 403, not retrieved.
- https://www.techrepublic.com/article/news-ai-xbow-tops-hackerone-us-leaderboad/ — found via search, not separately fetched.
- Upwork rate pages (upwork.com/resources/upwork-hourly-rates, upwork.com/hire/cybersecurity-experts/, gigradar.io/blog/upwork-hourly-rate) — covered via WebSearch synthesis, AI/ML vs. general-security rate bands.
- Solo AI-security freelancer "making a living" blog search — not run, WebSearch budget exhausted before this query could execute; open for pass 3.

## Boutique / two-person firm census

- https://airedteamers.com — fetched in full, no pricing/clients disclosed (already on file from pass 1, re-confirmed).
- https://redbotsecurity.com/ — fetched in full, one named client (Metro Water), no pricing (already on file from pass 1, re-confirmed).
- https://doyensec.com/ and https://doyensec.com/services/ai-security.html — fetched in full, AI security audit service line, operating since ≥2017, no pricing.
- https://aisecuritydirectory.com/categories/ai-model-security-red-team and its API endpoint (aisecuritydirectory.com/api/v1/search?category=ai-model-security-red-team) — 24-vendor census with founding years, mostly product companies.
- https://www.mend.io/blog/best-ai-red-teaming-companies/ — 7-vendor listicle, no founding/pricing/client detail.
- https://stiennon.substack.com/p/ten-new-ai-security-vendors — 10-vendor list, mostly product startups, 3 with disclosed funding.
- https://neuraltrust.ai/blog/best-ai-red-teaming-platforms — found via search, not fetched.
- https://www.breachlock.com/resources/blog/top-5-red-teaming-companies-in-2025/ — found via search, not fetched.
- https://www.linkedin.com/pulse/ai-security-startups-watchlist-top-30-2025-tal-eliyahu-ozqwc — found via search, not fetched (LinkedIn, likely login-gated).
- https://bluefire-redteam.com/ai-red-teaming-services/ — found via search, not fetched.

## Counter-evidence — automation / commoditization

- https://www.cobalt.io/pricing — $3,500 autonomous-pentest price point undercutting the $8K–$25K services floor.
- https://xbow.com/pricing — labor-substitution framing ("coverage without the headcount").
- https://xbow.com/blog/top-1-how-xbow-did-it — autonomous system topping a human leaderboard.
- https://edwinkwan.com/2026/05/22/hackerone-slashes-bug-bounty-payouts-as-ai-floods-open-source-security-programs/ — payout collapse attributed to AI-generated report flood.
- https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=penetration%20testing — zero federal contracts for AI penetration testing as a named line item.
- https://www.mindfort.ai/blog/best-pentera-alternatives — Pentera/NodeZero enterprise autonomous-pentest platforms and pricing.
- Horizon3.ai and Pentera product pages — not independently fetched (queried only via the mindfort comparison above); open for pass 3 to get vendor-stated pricing directly.

## Productization path / services ceiling comparables

- https://www.praetorian.com/ — Chariot platform positioning, services-to-product framing.
- https://doyensec.com/ — stayed services, no disclosed ceiling metrics.
- https://en.wikipedia.org/wiki/NCC_Group — filed revenue £238.9M FY2025, conflicting headcount (2,140 Wikipedia vs. 3,130 third-party).
- https://www.konaequity.com/company/trail-of-bits-4862904543/ — third-party $8.7M revenue / 101 employees estimate.
- https://leadiq.com/c/trail-of-bits/5a1d9eb02300005a008ef82b, https://pitchbook.com/profiles/company/228293-29, https://tracxn.com/d/companies/trail-of-bits/, https://craft.co/trail-of-bits, https://rocketreach.co/trail-of-bits-profile_b5cbf24cf42e14c4, https://www.zoominfo.com/c/trail-of-bits/373697686 — Trail of Bits third-party profile aggregators found via search, not individually fetched (all likely republish similar estimates; risk of circular sourcing not resolved this pass).
- https://www.reveliolabs.com/companies/ncc-group/employees/ — source of the conflicting 3,130-employee NCC Group figure, not independently fetched (title/snippet only).
- Bishop Fox, Praetorian, Include Security, NetSPI revenue/headcount — WebSearch query to find these did not execute (budget exhausted); NetSPI pricing page attempt (netspi.com/pricing/) returned 404. Open for pass 3.
- Invariant Labs, Doyensec exit/ceiling case studies beyond what's in pass-1 roster — not separately researched this pass.

## Not fetched — open for pass 3

- UK Contracts Finder / Find a Tender AI red-teaming award records (403 on the one notice found; no replacement search run, budget exhausted).
- USAspending.gov / SAM.gov direct full-text search for AI red-teaming award records beyond the govai-contracts secondary index (that index's own primary API was not queried directly).
- State and university RFPs for AI security testing (California, university system procurement portals) — no query executed this pass.
- TED/EU tenders for AI security assessment services — no query executed this pass.
- GSA schedule pricing for security-assessment SINs — CALC tool nonfunctional as of 2026-09-16; try a GSA eLibrary contract-holder PDF directly next pass.
- MAS (Singapore) AI risk-management guidelines — site returned service-unavailable errors on both pages tried; retry with the specific Veritas/FEAT document URLs next pass.
- FCA-specific red-teaming/testing mandate beyond the AI Lab sandbox — not located; the sandbox is voluntary, not a mandate, and no separate FCA testing rule was found.
- FedRAMP AI-specific guidance document — https://www.fedramp.gov/blog/ returned empty; search the FedRAMP 20x program pages directly next pass.
- NYDFS 2024-10-16 letter full text — two slug guesses both 404'd; retry via the DFS site's own search box or web.archive.org.
- Named DoD guidance on AI system testing beyond the two NYDFS/HiddenLayer contract data points.
- Healthcare-sector AI testing guidance (FDA, ONC) — no query executed this pass.
- Solo/individual AI-security freelancer first-person accounts of income ("making a living") — no query executed, budget exhausted before this theme could be searched.
- NetSPI, Include Security, Bishop Fox, Praetorian named revenue/headcount/case-study detail — partially blocked (404, budget exhausted); revisit with fresh WebSearch budget.
- Bugcrowd's own OpenAI-safety program payout table (full page render) — fetch returned nav shell only; retry with a rendering-capable fetch tool (e.g. browser automation) next pass.
- CSA CAIQ questionnaire version history for an AI/red-teaming field addition — not confirmed either way.
