# Services lane — raw pulls (pass 2)

Research agent 8, pass 2, 2026-09-16. Stress-tests the pass-1 services-lane conclusion in `../markets/ai-attack-defense.md` with real (non-aggregator) pricing, demand-channel evidence, regulatory-mandate evidence, supply-side earnings, boutique-firm census, counter-evidence, and productization case studies. Verbatim blocks only, source's own words. Raw is exempt from compression.

---

## 1. USAC "Penetration Testing as a Service" — SAM.gov opportunity

Source: https://sam.gov/workspace/contract/opp/b13eeb1c32b14563bee9f39cadf3a7fb/view — procurement-filed — fetched 2026-09-16

Page rendered as a JS shell ("Sam Acquisition 360") when fetched without a browser session; no scope, value, or dates extracted. Confirmed via search snippet only: "USAC RFP: Penetration Testing as a Service," proposal deadline referenced as March 30, 2026. General pentest RFP, not AI-specific. unknown — checked SAM.gov via WebFetch 2026-09-16, page requires JS rendering not available to this fetch method.

## 2. Rebellion Defense DOD AI contracts (search-derived, not primary)

Source: (aggregated from WebSearch synthesis, no single primary URL resolved) — analyst-derived — fetched 2026-09-16

Search-tool synthesis stated: "Rebellion Defense secured $420 million across multiple DOD AI contracts focused on threat modeling and automated red-teaming." No primary contract record, SAM.gov ID, or USAspending award ID was located to verify this figure. Flagged low-confidence — treat as unknown — checked WebSearch synthesis 2026-09-16, no primary source resolved.

## 3. GSA CALC tool — no longer returns pentest labor rates

Source: WebSearch synthesis of GSA schedule pricing query — vendor-reported/analyst-derived — fetched 2026-09-16

"Unfortunately, US General Services Administration awarded labour rates could not be retrieved: the CALC tool now redirects to a notice page carrying no data, and a GSA price list PDF returned HTTP 404." GSA schedule pentest labor rates are unknown — checked GSA CALC tool 2026-09-16, tool returns no data.

## 4. Standard pentest pricing — deepstrike.io 2026 breakdown

Source: https://deepstrike.io/blog/penetration-testing-cost — vendor-reported — fetched 2026-09-16

Quoted figures extracted from page, dated "Updated September 14, 2026":
- Web App: "$5,000–$30,000+"
- Network: "$5,000–$40,000+"
- API: "$6,000–$30,000"
- Mobile App: "$7,000–$35,000 (per OS)"
- Cloud: "$10,000–$50,000+"
- Black Box: "$5,000–$50,000" / Grey Box: "$6,000–$35,000" / White Box: "$7,000–$40,000+"
- PCI DSS: "$12,000–$25,000" / HIPAA: "$10,000–$50,000" / SOC 2: "$5,000–$20,000" / ISO 27001: "$5,000–$50,000" / FedRAMP: "$15,000–$75,000+"
- Small Business (annual): "$8,000–$20,000" / Mid-Market: "$20,000–$50,000" / Enterprise: "$50,000–$150,000+"
- Hourly: "Hourly rates for skilled testers typically range from $100 to $300"
- UK daily rates: "around £800–£1,500"
No AI/LLM-specific pentest pricing line item on this page.

## 5. Synack 2026 pentest pricing table, including red team and PTaaS tiers

Source: https://www.synack.com/blog/penetration-testing-cost/ — vendor-reported — fetched 2026-09-16, article dated "June 25, 2026"

| Test Type | Range |
|---|---|
| Web application | $5,000–$30,000 |
| External network | $4,000–$12,000 |
| Internal network | $5,000–$35,000 |
| API | $5,000–$30,000 |
| Mobile application | $7,000–$35,000 |
| Cloud | $10,000–$50,000 |
| Red team/adversary simulation | $30,000–$150,000+ |
| Social engineering | $3,000–$12,000 |
| Annual PTaaS (continuous) | $20,000–$100,000+ |

"Overall market average: ~$18,300 per engagement; typical range $10,000–$30,000." On AI vs. automated pricing: "AI-assisted PTaaS models are changing the cost-per-coverage calculation" delivering "continuous coverage across a broader surface"; PTaaS "carries a higher sticker price than a single engagement, but it covers retests, continuous validation, and a far larger share of your attack surface." On manual vs. automated: "Manual testing by senior researchers costs more per day than automated scanning, but it also produces fewer false positives and more reliable findings." No explicit AI-pentest premium/discount figure stated.

## 6. Astra AI pentest pricing — explicit AI-specific price line

Source: https://www.getastra.com/ai-pentest — vendor-reported — fetched 2026-09-16

"AI pentesting services typically range from $5,000 to $50,000+, depending on scope, complexity, and assets tested." Scope: "automated scans, manual pentests, two complimentary rescans, and certification." Timeline: "10-15 business days depending on scope and asset complexity." No explicit statement of premium or discount vs. standard web-app pentest — the $5k–$50k AI band overlaps the $5k–$30k standard web-app band from the deepstrike and Synack tables above, i.e. no clear AI premium demonstrated across these three vendor price sheets.

## 7. Cobalt PTaaS — published autonomous-pentest price point

Source: https://www.cobalt.io/pricing — vendor-reported — fetched 2026-09-16

"Autonomous Pentest: $3,500 per test (limited time offer for new and existing customers)." Subscription tiers "Standard, Premium, and Enterprise" have no published dollar figures — "get a quote." Credit model: "A Cobalt Credit represents the equivalent of 8 hours of offensive security testing," per-credit price undisclosed. "AI & LLM Pentest" service listed as a named SKU with no price shown — links to "learn more" only.

## 8. Pentera and Horizon3.ai NodeZero — enterprise autonomous-pentest pricing

Source: https://www.mindfort.ai/blog/best-pentera-alternatives — vendor-reported/analyst-derived — fetched 2026-09-16

"Pentera can get very cost inefficient, with an average deal size around $100,000." Separately reported elsewhere in the same search pass: "Pentera is approximately $50K/yr according to Gartner/G2." On NodeZero: "Pricing is custom and not published, and it can get very expensive." Separately reported: NodeZero "Approximately EUR 35,000/year," SaaS subscription, "unlimited testing within contracted scope." Both figures for NodeZero are third-party estimates, not vendor rate cards — conflicting figures side by side, not averaged.

## 9. OWASP Vendor Evaluation Criteria for AI Red Teaming Providers & Tooling v1.0

Source: https://genai.owasp.org/resource/owasp-vendor-evaluation-criteria-for-ai-red-teaming-providers-tooling-v1-0/ — filed (standards body) — fetched 2026-09-16, published 2026-02-04

Purpose stated as "a practical guide for organizations assessing vendors that offer AI red teaming services or automated testing tools," covering "green flags, red flags, realistic threat models, evaluation rigor, tooling quality, and governance considerations," scoped to "basic GenAI systems (chatbots, RAG applications)" and "advanced systems (tool-calling agents, MCP architectures, multi-agent workflows)." States its aim is helping "decision-makers distinguish meaningful adversarial testing from superficial 'jailbreak-only' offerings." No pricing benchmark included in the document.

## 10. AI Red Teamers — no public pricing, no named clients

Source: https://airedteamers.com — company-stated — fetched 2026-09-16

Three service lines named: "SECURE" ("AI red teaming, pentesting, and ecosystem assessments"), "ENABLE" ("AI security training for every role from interns to dev team to boardroom"), "COMPLY" ("Shadow AI governance, policy & acceptable use, and compliance frameworks" aligned to "ISO 42001 and NIST AI RMF"). Specializes in "LLM penetration testing and agentic AI assessments." No pricing and no named client disclosed on the page.

## 11. Redbot Security — one named client, no pricing

Source: https://redbotsecurity.com — company-stated — fetched 2026-09-16

AI service line: "LLM security, prompt injection, model abuse, and AI exposure testing." One named client in a testimonial: "Metro Water." Certifications emphasized: "OSCP, CRTO, GPEN, etc." No pricing or headcount published.

## 12. Doyensec — AI security service page

Source: https://doyensec.com/services/ai-security.html — company-stated — fetched 2026-09-16

"Comprehensive AI security audits to ensure your AI-driven systems are resilient, compliant, and free from vulnerabilities." Methodology maps to "OWASP API Security Top 10," "OWASP Machine Learning Security Top 10," and unnamed "industry standard AI-focused guidelines." Testing areas: "input validation, output rendering, access controls, and LLM-specific vulnerabilities including prompt injection, denial-of-service scenarios, training data poisoning, and sandbox escape vectors." Self-description: "the preferred partner of companies specializing in AI development and integration" since "these technologies emerged." Research team "dedicates 25% of time to self-directed research." No pricing, no case studies on the service page. Company operating since at least 2017 per copyright footer.

## 13. AI Security Directory — AI model security / red-team vendor census

Source: https://aisecuritydirectory.com/api/v1/search?category=ai-model-security-red-team — vendor-reported (third-party directory) — fetched 2026-09-16, directory "last updated 2026-08-13," "460 vendors across 21 categories"

24 vendors listed in this category with founding years: 0din by Mozilla (2024, "Mozilla's bug bounty program for generative AI models, chatbots, and agents"), AISY (2025, "early-stage London startup"), Alice (2018), Arize AI (2020), Arthur AI (2018), Bifrost/Maxim AI (2023), Cranium (2023), DeepKeep (2021), Fiddler AI (2018), Gray Swan (2024, "stress-tests and hardens frontier models"), HiddenLayer (2022), Lakera (2021, Zurich), Mindgard (2022), Mirror Security (2024, Dublin), OpenAI (2015), Patronus AI (2023, New York), Preamble (2020, Pittsburgh, "prompt-injection defense, red teaming, and AI agent assessments"), Promptfoo (2023, "open-source LLM evaluation and red-teaming toolkit"), Straiker (2024), TrendAI (2026, Trend Micro unit), TrojAI (2019), Verno Labs (2025, "offensive LLMs that red team AI agents"), Votal AI (2024), WhyLabs (2019). No team size or pricing fields populated for any entry. Note: this category is dominated by product companies (monitoring, firewall, evaluation platforms), not services boutiques — confirms the market map's product/services split, does not itself list new services boutiques.

## 14. Mend.io — "Best AI Red Teaming Companies" listicle

Source: https://www.mend.io/blog/best-ai-red-teaming-companies/ — vendor-reported — fetched 2026-09-16

Seven entries named: Mend.io itself ("automate adversarial testing for conversational AI"), Mindgard ("maps attack surfaces and connects red teaming with runtime detection"), HackerOne ("uses vetted security experts to identify vulnerabilities"), Redbot Security ("multi-phase simulation exercises"), CrowdStrike, Schellman, Shaip ("human-led evaluation"). No founding dates, team sizes, pricing, or named client case studies provided for any entry.

## 15. Richard Stiennon — "Ten New AI Security Vendors"

Source: https://stiennon.substack.com/p/ten-new-ai-security-vendors — analyst-derived (independent analyst) — fetched 2026-09-16

Ten vendors named: Arambh Labs, Armadin ("$189.9M total" funding), Astelia, Ciphero ("2025" founded, "$2.5M pre-seed"), C1 ("rebranded 2026"), CyberAGI, EnforceAuth, Evoke ("$4M pre-seed"), FlintX, Hackerdogs. Most lack disclosed founding dates, team sizes, or pricing. Only Armadin, Ciphero, and Evoke have disclosed funding amounts; none of the ten are named as services-only boutiques in the extracted content.

## 16. HackerOne — AI vulnerability report growth, 2025–2026

Source: WebSearch synthesis of HackerOne reporting — vendor-reported — fetched 2026-09-16

"HackerOne reported $81 million in payouts in 2025, with valid AI vulnerability reports up 210 percent and prompt injection up 540 percent." "AI features are now in scope on over 1,100 HackerOne programs, representing a 270% year-over-year increase." "For AI/LLM-specific vulnerabilities, the median real-world AI bug payout in 2026 is closer to $500-$2,500." Caveat noted in the same source pass: "many 'prompt injection' submissions get closed, and some programs that host AI-adjacent programs often don't know how to triage LLM-specific bugs."

## 17. Edwin Kwan — HackerOne slashes bug-bounty payouts as AI floods programs (counter-evidence)

Source: https://edwinkwan.com/2026/05/22/hackerone-slashes-bug-bounty-payouts-as-ai-floods-open-source-security-programs/ — company-stated/press-derived — fetched 2026-09-16, dated 2026-05-22

Internet Bug Bounty (IBB) reward cuts: "Critical vulnerabilities: $9,250 → $2,257," "High-severity findings: $4,429 → $1,009," "Medium-severity reports: $1,843 → $297" — over 75% cut. "AI-assisted tooling has made the discovery of plausible security flaws significantly cheaper and faster, and the volume of reports flowing into open-source security programs has grown to the point where maintainers are struggling to process them." Commoditization stated directly: "finding a plausible bug is becoming commoditised, but the work of verifying impact, deduplicating reports, making patch decisions, and coordinating disclosure remains an irreducibly human and time-intensive process." "The IBB program has been paused and is not currently accepting new submissions while HackerOne evaluates structural adjustments." Trust risk flagged: "If serious researchers cannot trust that the terms under which they reported a vulnerability will be honoured, they will either price that uncertainty into their participation or withdraw from structured programs entirely."

## 18. Wraith.sh — AI bug bounty program payout summary, 2026

Source: https://wraith.sh/learn/ai-bug-bounty-programs — vendor-reported/aggregator — fetched 2026-09-16

OpenAI Safety Bug Bounty: "Max payout: $100,000 for exceptional findings," "Standard max: $20,000," "Launched March 2026 with $1M annual pool." OpenAI Security Bug Bounty: "Range: $200–$100,000." Anthropic: "Max payout: $15,000 per finding," tracks "Model Safety (jailbreaks) and Product Security," on HackerOne "now open submissions." Google AI VRP: "Range: Up to $30,000 base payouts"; critical exclusion quoted: "Prompt injection, jailbreaks, and alignment issues are explicitly excluded"; "Sensitive data exfiltration bonus: up to $15,000." Microsoft Copilot: "Range: $250–$30,000," "Updated April 2026 to include moderate-severity findings ($5,000 max)." xAI/Grok: "Payouts: Not publicly documented." Cross-program: "Median payouts cluster $500–$5,000 across programs. Gray Swan Arena pools ($40K–$300K+) split among top competitors rather than per-finding awards."

## 19. Anthropic Model Safety Bug Bounty — HackerOne program history and totals

Source: https://www.hackerone.com/blog/anthropic-expands-their-model-safety-bug-bounty-program — company-stated/vendor-reported — fetched 2026-09-16

"Maximum Reward: $15,000 per submission for novel, universal jailbreak attacks." Scope: "CBRN (chemical, biological, radiological, and nuclear)" and "cybersecurity." Program quote: "Participants will be given early access to test our latest safety mitigation system before its public deployment... participants will be challenged to identify potential vulnerabilities." Universal-jailbreak definition: qualifies when it "consistently bypasses safety measures across multiple harmful topics — specifically defined by the ability to trigger responses to a predetermined set of restricted questions." Program began "invite-only," expanded to public. From a separate search-pass total: "As of May 2026, total rewards paid reached approximately $550,835," "Rewards are classified into 4 levels based on vulnerability severity, with Medium and High level vulnerabilities accounting for approximately 87% of the total."

## 20. OpenAI Safety Bug Bounty — Bugcrowd program

Source: https://bugcrowd.com/engagements/openai-safety — company-stated — fetched 2026-09-16

Page rendered as navigation shell only (no reward table extracted directly from the live fetch — logged as a partial pull). Cross-confirmed via search pass: "OpenAI has launched a Safety Bug Bounty Program in collaboration with Bugcrowd... launched in March 2026 with a $1 million annual pool," payouts "up to $100,000 for critical issues," "Standard payouts go up to $20,000." Scope: "third-party prompt injection and data exfiltration attacks, disallowed actions performed by agentic OpenAI products... at scale, and other harmful actions."

## 21. XBOW — #1 HackerOne US leaderboard ranking

Source: https://xbow.com/blog/top-1-how-xbow-did-it — company-stated — fetched 2026-09-16

"Top position in the US ranking" on HackerOne. Cumulative reports: "Nearly 1,060 vulnerabilities reported in total." Past-90-day severity breakdown at time of writing: "54 critical, 242 high, 524 medium, 65 low severity issues." Report disposition: "130 resolved by programs," "303 triaged (mostly by VDP programs)," "33 marked as new," "125 pending review," "208 duplicates," "209 informative," "36 not applicable." Cross-confirmed via search: XBOW's "agent reached the top of HackerOne's US leaderboard in Q2 2025 after submitting nearly 1,060 reports," earning "2,059 points without years of accumulated submissions, while top human researchers typically build reputation over years of consistent contributions." No payout amounts disclosed in the article. Self-description: "XBOW is an enterprise solution."

## 22. XBOW — pricing/business-model framing (counter-evidence: headcount replacement)

Source: https://xbow.com/pricing — company-stated — fetched 2026-09-16

"Usage-based pricing that scales with your coverage, not a fixed annual engagement." Cloud marketplace purchasing available via "AWS, Google Cloud, Oracle, and Microsoft." Positioning: "Continuous coverage, not an annual snapshot" and "Validated findings with proof-of-concept exploits and remediation." Direct labor-substitution framing quoted verbatim: **"It's coverage without the headcount."**

## 23. XBOW funding — $75M and $120M rounds (press)

Source: https://it.slashdot.org/story/25/07/05/1847237/xbows-ai-powered-pentester-grabs-top-rank-on-hackerone-raises-75m-to-grow-platform ; https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker — press-derived — fetched 2026-09-16 (titles only; full body not independently re-fetched)

Headline facts as titled: "XBOW's AI-Powered Pentester Grabs Top Rank on HackerOne, Raises $75M to Grow Platform" (dated story path 25/07/05, i.e. 2025-07-05) and "XBOW Raises $120M to Scale its Autonomous Hacker" (dated story path 20260318, i.e. 2026-03-18). Confirms two funding rounds in ~8 months around the leaderboard milestone — venture capital is backing the automation side of this exact lane pass 1 flagged as the human-services opportunity.

## 24. Cyber insurance — AI questions now standard at renewal

Source: https://aisafeiq.com/blog/cyber-insurance-7-ai-questions-2026 — vendor-reported (insurance advisory blog) — fetched 2026-09-16, dated 2026-05-24

Seven questions quoted: (1) "Do You Have a Written AI Use Policy?" — insurers want "a document. Not a verbal policy. Not an informal understanding." (2) "Are Employees Trained on AI Misuse?" requires "documented evidence that employees received training on AI safety." (3) "Can You Document It?" demands "a stack of completion certificates, a training completion report, a policy acknowledgment for every employee." (4) "Do You Have an AI Risk Assessment on File?" expects "a documented evaluation of which AI tools your organization uses, what data they can access." (5) "Is AI Governance Part of Your Security Program?" checks whether "AI is managed as part of your information security infrastructure or handled informally." (6) "Has AI Been Involved in Any Prior Incidents?" investigates "undisclosed AI-related incidents." (7) "Do You Audit AI Tool Usage?" requires visibility into "which AI tools are in active use across your organization." Statistics: "81% of cyber insurers now include AI governance questions in renewal applications." Sublimit example: "a $5M policy capped at $500K for AI incidents." None of the seven questions explicitly names third-party red-teaming as mandatory — governance documentation is the ask, not adversarial testing per se, though search-pass synthesis separately reported: "Some insurers introduced 'AI Security Riders' in 2026: add-ons that require proof of red-teaming... and documented risk assessments before they extend coverage" (source: WebSearch synthesis, unconfirmed against a named carrier — unknown — checked WebSearch synthesis 2026-09-16, no named carrier rider document located).

## 25. NYDFS — Heightened Cybersecurity Risks Associated with Frontier AI Models

Source: https://www.dfs.ny.gov/industry-guidance/industry-letters/20260521-heightened-cybersecurity-risks-assoc-with-frontier-ai-models — filed (state regulator) — fetched 2026-09-16, dated 2026-05-21

Risk framing quoted: "frontier artificial intelligence models that amplify the potency, scale, and speed of identifying vulnerabilities and exploits in information systems." Testing-adjacent language: "additional testing and validation procedures, including human oversight, for AI-generated code prior to deployment in production environments"; review and testing of "threat-relevant operational resilience procedures." Does **not** mandate red-teaming or adversarial testing by name — the advisory pushes expedited vulnerability management and code-review discipline, not third-party AI security testing procurement.

## 26. NYDFS — 2024 AI cybersecurity industry letter (title/date only, body not retrieved)

Source: https://www.dfs.ny.gov/industry_guidance/industry-letters/il20241016-cyber-risks-ai-and-strategies-combat-related-risks — filed (state regulator) — fetched 2026-09-16

Confirmed via the DFS industry-letters index page: "Cybersecurity Risks Arising from Artificial Intelligence and Strategies to Combat Related Risks," dated 2024-10-16, category "Cybersecurity." Direct fetch of the letter body returned HTTP 404 under two URL-slug variants tried. Body content is unknown — checked dfs.ny.gov 2026-09-16, page 404s on both hyphen and underscore slug variants; needs a re-check via the site's own search or archive.org in a later pass.

## 27. FCA — AI Lab and AI Live Testing service

Source: https://www.fca.org.uk/firms/innovation/ai-lab — filed (UK regulator) — fetched 2026-09-16

"The AI Lab provides a pathway for the FCA, firms and wider stakeholders to engage in AI-related insights, discussions and case studies," aiming "to enable the safe and responsible use of AI in UK financial markets, driving growth, competitiveness and innovation." AI Live Testing offers firms "a safe place to test AI systems in real-world conditions, with appropriate regulatory support and oversight," targeted at firms "further along in AI development and are ready to use it in live markets." Eligibility: firms must "actively deploy AI within specific use cases," have "completed proof-of-concept development," have "considered pre-deployment and post-deployment monitoring approaches," and be "willing to collaborate and share findings with the FCA." Dates: second cohort application window "January 19 – March 24, 2026," notification "Mid-April 2026," testing commencement "Late April 2026." No mention of red-teaming or adversarial testing as a requirement — this is a regulatory sandbox program, not a testing mandate.

## 28. ISO/IEC 42001 — audit stages and red-teaming's place in the AIMS

Source: https://cloudsecurityalliance.org/articles/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework — filed (standards/CSA) — fetched 2026-09-16, dated 2025-05-08

Stage 1: "the auditor assesses your organization's readiness for the full audit, with particular attention to the design of your AIMS, including policies and documentation." Stage 2: "auditors typically interview staff and observe and evaluate the processes and performance of your AIMS." "To issue an accredited certificate, an audit organization must undergo the accreditation process in order to become a formally accredited certification body." Red-teaming is not stated as a mandatory certification test — it is referenced elsewhere as fitting into governance programs, not as a required audit procedure itself. Separately captured elsewhere in the same source family: red-team programs "can be placed under Operation (scope, procedures, toolchains, safety gates), Performance Evaluation (metrics, internal audits, management review), and Improvement (nonconformity handling, corrective actions), transforming adversarial testing into certification-grade evidence" — i.e. red-teaming is optional supporting evidence an org can submit, not a pass/fail line item the standard itself requires.

## 29. ISO/IEC 42006:2025 — certification-body standard, and Schellman's ANAB accreditation

Source: WebSearch synthesis (Schellman, ANAB pages) — filed — fetched 2026-09-16

"ISO/IEC 42006:2025 is an international standard that specifies the requirements for bodies providing audit and certification of artificial intelligence management systems." "ANAB accredits certification bodies that issue certifications to ISO/IEC 42001 artificial intelligence management systems." "Schellman is the first ANAB-accredited certification body for ISO 42001." ISO 42001 itself: "published December 18, 2023," is "the first international standard that tells an organization how to establish policy, roles, competence, lifecycle controls, supplier oversight, monitoring, internal audit, and continual improvement specifically for AI."

## 30. SOC 2 Type II — AI evidence gap, 2026

Source: WebSearch synthesis of SOC 2/AI compliance blogs (futureagi.com, konfirmity.com, soc2vendors.com, knowlee.ai) — vendor-reported — fetched 2026-09-16

"Auditors increasingly ask LLM vendors about prompt and output retention, training-data segregation, model-version pinning, and red-team coverage." "Auditors are starting to ask for prompt-injection test artifacts: a documented adversarial test suite, results, and mitigation evidence." "SOC 2 auditors in 2026 demand AI-specific evidence including model registry, prompt logs, red-team suites, and vendor DPAs with zero-data-retention." Critical standards-gap admission: "AI controls in SOC 2 audits sit in a regulatory gap in 2026: the AICPA has published no authoritative AI-specific SOC 2 standard, yet auditors are now demanding AI-specific evidence in real engagements." This is the clearest confirmation across all regimes checked: auditor practice is running ahead of any written standard, and it is auditor discretion — not a published rule — creating red-team demand.

## 31. GovAI Contracts tracker — methodology

Source: https://github.com/Nandanhegde1/govai-contracts — procurement-filed (aggregator of primary data) — fetched 2026-09-16

"An independent index cataloging all U.S. federal AI/ML/data-science contract awards and open opportunities." Data sources: "USAspending.gov (awards via public API)" and "SAM.gov (active solicitations via opportunities API)," both "public domain." Update frequency: "every 6 hours through automated GitHub Actions workflows." Filtering: "queries AI-relevant NAICS codes (541511, 541512, 541513, 541515, 541715, 518210) then filters results by AI/ML keyword presence in award descriptions to exclude generic IT contracts." Exports at "/export/all.csv and /export/all.json." Database size at fetch time: "700 federal AI contracts."

## 32. HiddenLayer — two USAF SBIR-style contracts for ML red-teaming tooling

Source: https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=red%20team — procurement-filed — fetched 2026-09-16

Record 1: Vendor "HIDDENLAYER INC," agency "Department of Defense · Department of the Air Force," contract value "$1.80M," award date "February 9, 2024," end date "August 11, 2025," description: "MACHINE LEARNING SECURITY ATTACK WORKBENCH FOR RED TEAMING OF AUTONOMOUS ASSETS." Record 2 (from the "adversarial" query on the same tracker): same vendor and agency, value "$1.25M," dates "Sep 21, 2023 → Mar 24, 2025," description: "HiddenLayer Machine Learning Detection & Response - Defense Against Adversarial Machine Learning Attacks." Both are government-funded R&D/tooling contracts to a named AI-security vendor, not a services engagement purchased from an open-market pentest firm — the government money in this niche is going to product/tooling builders, not services buyers of AI red-teaming labor.

## 33. Peraton Labs — DARPA ML contract (adjacent, not red-team specific)

Source: https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=adversarial — procurement-filed — fetched 2026-09-16

Vendor "PERATON LABS INC," agency "Department of Defense (DARPA)," value "$16.60M," dates "May 5, 2020 → May 5, 2024," description paraphrased in the tool's extraction as focused on "developing technology to speed up applications like distributed training of machine learning classifiers" — general ML infrastructure research, not adversarial security testing; included here to show a false-positive risk in "adversarial" keyword search over this database.

## 34. CACI NSS and Aperio Global — DHS AI-security-adjacent support contracts

Source: https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=security%20assessment ; ?q=vulnerability — procurement-filed — fetched 2026-09-16

"CACI NSS, LLC" ($1.29M, DHS): "Artificial intelligence safety & security executive steering committee support" — governance/committee support, not testing. "APERIO GLOBAL LLC" ($1.54M, DHS/USCIS), award date "October 18, 2024," period "October 18, 2024 – May 31, 2025": "Cybersecurity artificial intelligence support (CAIS) in support of OIT ISD to obtain AI professional services that will improve USCIS's ability to identify, protect, respond, ad recover from increased cybersecurity threats." Neither record names red-teaming, penetration testing, or adversarial testing specifically as the deliverable — both are broader "AI security support" labor contracts.

## 35. AI2 Incorporated — USAF secure-LLM contract

Source: https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=LLM%20security — procurement-filed — fetched 2026-09-16

Vendor "AI2 INCORPORATED," agency "Department of Defense · Department of the Air Force," value "$1.35M," award date "August 16, 2024," end date "December 16, 2025," description: "Secure Large Language Models to Enable General Artificial Intelligence for Critical Department of the Air Force Applications." NAICS 541715. Development contract, not a red-team/pentest services buy.

## 36. No "penetration testing" keyword hits in the 700-contract AI database

Source: https://govai-contracts.nandanhegde1096.workers.dev/contracts/?q=penetration%20testing — procurement-filed — fetched 2026-09-16

Direct search result: "no records matching 'penetration testing' were found" among the tracked 700 federal AI/ML contracts. Same null result for "prompt injection." **This is a load-bearing negative finding**: across the best available free index of US federal AI contract awards, zero records explicitly buy AI penetration testing or AI red-teaming as a named services line item — the money that exists goes to tooling/platform R&D (HiddenLayer) or broad "AI security support" labor (CACI, Aperio), not to an open-market AI pentest engagement.

## 37. Upwork/gig-platform AI/ML freelancer rate bands, 2026

Source: WebSearch synthesis of Upwork rate pages/benchmarks (upwork.com, gigradar.io) — vendor-reported (platform-published) — fetched 2026-09-16

"AI/ML freelancer rates in 2026 commonly range from $50 to $300+/hour depending on experience and specialization, with junior (0-2 years) at $50-$80/hour, mid-level (2-5 years) at $80-$130/hour, and senior (5-10+ years) commanding higher rates." Separately: "senior AI and machine-learning work reaches $100 to $300, with top-tier strategy or advisory engagements at $200 to $500-plus." Cybersecurity-specific: "Senior-level cybersecurity experts with specialized skills... typically in the higher end of the $38-$64 per hour range or above for strategic consulting" — notably lower than the AI/ML band, suggesting general security consulting on Upwork is priced below AI-specialist consulting, not above it. No AI-security-specific (as opposed to general AI/ML or general security) rate band was separately published on the pages checked.

## 38. Trail of Bits — third-party revenue and headcount estimate

Source: https://www.konaequity.com/company/trail-of-bits-4862904543/ — analyst-derived (third-party data aggregator) — fetched 2026-09-16 (title/snippet only, not independently re-verified by direct fetch)

Snippet title: "Trail of Bits - $8.7 M Revenue, Employees & Growth." Search-pass synthesis reported "Annual revenue of $8.7 million in 2026" and "Employee count of 101 as of June 30, 2026" — implying roughly $86K revenue per head. Not company-confirmed; third-party aggregator figure.

## 39. NCC Group — filed revenue, conflicting third-party headcount

Source: https://en.wikipedia.org/wiki/NCC_Group — filed (public company financials, via Wikipedia tertiary summary) — fetched 2026-09-16

"Revenue: £238.9 million" and "Net Income: £17.1 million" for fiscal 2025. Employee count per Wikipedia: "2025: 2,140 employees." A separate third-party source (Revelio Labs, via search synthesis) reported "3,130 employees as of December 2025" — a ~46% discrepancy between two non-primary sources, presented side by side per repo rule, not averaged. Company history: "formed when National Computing Centre sold commercial divisions" in "June 1999"; "Admitted to trading on AIM" "July 12, 2004" (raised £38.1 million); moved "to the London Stock Exchange main market" "July 2007"; "completed sale of Escode business to TDR Capital" "May 2026." No AI-specific security service mentioned in the Wikipedia summary — the company's own current site was not independently re-checked for an AI-testing service line in this pass.

## 40. Praetorian — services-to-product framing via the Chariot platform

Source: https://www.praetorian.com/ — company-stated — fetched 2026-09-16

Current self-positioning is platform-first: "Praetorian Guard platform... combining Agentic AI, Workflow Automation, and Offensive Capabilities" with human expertise, unified under "Chariot," covering "Attack Surface Management, Vulnerability Management, Cyber Threat Intelligence, Attack Path Mapping, Continuous Penetration Testing, Breach & Attack Simulation." Value claim: "25-50% spend reduction" and "50-70% reduction of low-impact remediation activity" versus buying separate point tools. No founding date, no pricing — "Contact Sales" and "Recorded Demo" only. Illustrates the pattern the brief asked about: a firm that started in offensive-security services now sells itself primarily as a consolidated platform product, with services (continuous pentest) folded in as one module rather than the headline offering.

## 41. Cyber insurance questionnaire growth, 2026

Source: WebSearch synthesis of cyber-insurance renewal blogs (gogravity.net, acaglobal.com) — vendor-reported — fetched 2026-09-16

"Cyber insurance questionnaires have grown from 30 questions to 200-400 questions covering controls assessment, incident history, third-party vendor risk, AI use, ransomware preparedness, employee training programs, BCDR, and evidence to back every claim." "A new section on AI governance appeared on applications from carriers across the market in 2025 and accelerating into 2026." "2026 renewals are expected to ask about AI data governance and software supply chain." "Insurance underwriters added AI questions to applications, AI language to policies, and AI conditions to payouts, making answers binding for coverage eligibility."

## 42. Vendor security questionnaires — AI red-teaming as a line item

Source: WebSearch synthesis of vendor-questionnaire commentary (pentesttesting.com and related) — vendor-reported — fetched 2026-09-16

"Vendor security questionnaires typically ask whether products have undergone independent AI red teaming, which attack classes were tested, what evidence exists, and whether findings map to recognized frameworks." Illustrative composite scenario quoted: "vendors receiving security questionnaires covering encryption, access control, incident response, penetration testing, and data retention, with an AI section asking about independent red teaming, tested attack classes, evidence, and framework mapping." No confirmation found that CSA's standard CAIQ (Consensus Assessments Initiative Questionnaire) itself has an AI red-teaming field as of 2026-09-16 — unknown — checked WebSearch 2026-09-16, no CAIQ version update located naming AI red-teaming explicitly.

