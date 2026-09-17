# AI Attack/Defense — Raw Source Pulls

Topic: ai-attack-defense — AI security for tech companies (offensive testing + defense).
Compiled 2026-09-16.

---

## Research and Markets — AI Red Teaming Services Market Report
- URL: https://www.researchandmarkets.com/reports/6215045/ai-red-teaming-services-market-report
- Pulled: 2026-09-16
- Method: WebFetch

Market defined as: "systematically testing AI systems to identify vulnerabilities, biases, and potential risks before deployment" using "advanced AI techniques, cybersecurity tools, and ethical hacking methodologies."

Figures extracted: 2025 market value $1.75 billion; 2026 market value $2.26 billion; 2030 forecast $6.17 billion; historic CAGR (2025-2026) 28.8%; forecast CAGR (2026-2030) 28.5%. Service types scoped: penetration testing, vulnerability assessment, adversarial attack simulation, security auditing. Deployment modes: on-premises and cloud. Org sizes: SME and large enterprise. Applications: BFSI, healthcare, government, retail, manufacturing. Report is 250 pages, published February 2026, covers 2020-2035.
LABEL: analyst-derived (vendor market-research report; methodology not independently verified).

---

## AI Red Teaming Market — Conflicting Sizing (via WebSearch aggregation of multiple analyst firms)
- URL: https://www.astuteanalytica.com/industry-report/ai-red-teaming-and-security-testing-market ; https://market.us/report/ai-red-teaming-services-market/ ; https://dataintelo.com/report/ai-red-teaming-market
- Pulled: 2026-09-16
- Method: WebSearch

Conflicting figures found across analyst firms, none reconciled:
- Research and Markets: $1.75B (2025) -> $2.26B (2026) -> $6.17B (2030), CAGR 28.8%/28.5%. LABEL: analyst-derived.
- market.us: "USD 1.3 billion in 2025, growing to reach USD 18.6 billion by 2035 at a CAGR of 30.5%". LABEL: analyst-derived.
- Astute Analytica / other source: "$4.2 billion in 2025 and projects it reaching $21.8 billion by 2034 at a CAGR of 20.1%". LABEL: analyst-derived.
- Dataintelo: "USD 500.8 million in 2025, projecting USD 8,042.8 million by 2035 with a CAGR of 32.0%". LABEL: analyst-derived.
Also found: "AI red-teaming demand is projected to surge 35% by 2028, with almost no supply to meet it" and "AI red teaming alone is now a standalone market, projected to grow from $1.75B (2025) to $6.17B by 2030 at a 28.5% CAGR" (same R&M figure restated). LABEL: analyst-derived, source article unclear/secondary.
NOTE: Wide variance ($500M to $4.2B for the SAME 2025 base year) shows these are not reconcilable — treat all as rough analyst estimates, never averaged.

---

## Help Net Security — CISOs and AI budget 2026 (RH-ISAC report coverage)
- URL: https://www.helpnetsecurity.com/2026/04/06/rh-isac-enterprise-security-spending-report/
- Pulled: 2026-09-16
- Method: WebSearch (search-engine synthesis, not full fetch)

Reported via search snippet: "Despite nearly flat overall budget growth (an average of 5% in 2026, with 45% of organizations reporting no increase at all), AI has become the dominant driver of net-new cybersecurity spending, with 69% of CISOs naming it their top investment priority." Also: "Software accounts for 35% of the security budget in 2026, up from 29% last year."
LABEL: analyst-derived (RH-ISAC survey, as reported by Help Net Security).

---

## Buyer / budget-line signal — vendor framing (Mindgard/HiddenLayer positioning)
- URL: (aggregated from WebSearch snippets referencing mindgard.ai and hiddenlayer.com positioning)
- Pulled: 2026-09-16
- Method: WebSearch

Quoted framing: "If the program is fully CISO-led and lives entirely in the security organization — and you already have engineering's eval and observability stack solved elsewhere — dedicated vendors like Mindgard or HiddenLayer work well." Implies two competing buyer paths: CISO/AppSec-owned security budget vs. ML/engineering-owned eval budget.
LABEL: vendor-adjacent commentary (third-party comparison site, not a vendor's own claim, not an independent survey).

---

## AI Red Teaming Pricing — AI Vyuh Security blog
- URL: https://security.aivyuh.com/blog/ai-red-teaming-pricing-2026/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted tiers:
- One-Time Security Audit: "1–2 weeks" at "$8K–$25K", delivers "Vulnerability report with severity scoring and remediation guidance."
- Focused Red Team (Single Agent): "2–4 weeks" priced "$16K–$50K", "Attack simulation with proof-of-concept exploits and risk scoring."
- Comprehensive Red Team (Multi-Agent): "4–8 weeks" at "$50K–$150K+", "Full attack surface mapping, lateral movement testing, executive report."
- Continuous Red Teaming Subscription: "Ongoing" at "$5K–$20K/mo", "Automated scanning plus periodic manual testing and regression checks."
- Compliance-Driven Assessment: "2–6 weeks" costing "$20K–$75K", "Framework-mapped findings with audit-ready documentation."
- Internal tiers cited: Quick Scan "$5K–$10K"; Standard Assessment "$10K–$20K"; Deep Dive "$20K–$25K."
No hourly/day rates specified in this source.
LABEL: vendor-stated (single boutique vendor's own published pricing guide — may reflect that vendor's ambitions rather than market average).

---

## AI Red Team day/hourly rates — search aggregation (bluefire-redteam, infosec.qa)
- URL: https://bluefire-redteam.com/red-team-cost/ ; https://infosec.qa/blog/ai-red-teamer-salary-2026/
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "senior specialists clear $120-$200/hour, while an average contractor rate is approximately $67.60/hour." Also: "red team engagements cost $10K–$100K+ depending on scope, duration and complexity." General AI consulting (not AI-security-specific) context: "average AI consultant hourly rate in 2026 is $150-$300/hr, though the full market spans $80-$600."
LABEL: vendor/aggregator-stated (marketing/content sites, not a payroll or engagement dataset).

---

## Getastra — AI/LLM Penetration Testing Companies list
- URL: https://www.getastra.com/blog/ai-security/llm-and-ai-penetration-testing-companies/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: "Adoption has outrun assurance" — "2 out of every 3 organizations now use generative AI regularly, yet prompt injection sits at #1 on the OWASP Top 10." And: "most traditional pentest firms are not built to test it" — implying market coverage remains inadequate despite vendor proliferation.
Pricing/scope table extracted: Astra Security "plans from low-thousands/yr", tests RAG/agent/MCP; Bishop Fox "Enterprise, custom", agent testing yes; NetSPI "Enterprise, custom"; Praetorian "Custom enterprise engagements", agent yes; Trail of Bits "Scoped individually", MCP yes; NCC Group "Custom enterprise pricing"; Mindgard "Platform subscription, custom-quoted", agent yes; Lakera "Subscription; free Guard tier"; HackerOne "Program-based, custom", RAG/agent yes.
LABEL: vendor-comparison-site-stated (Astra Security's own blog; Astra is itself a competitor in this list — self-interested source, treat pricing claims about competitors as unverified).

---

## Open-source frameworks comparison — genai.qa / appsecsanta / braintrust (aggregated)
- URL: https://genai.qa/blog/garak-vs-pyrit-vs-deepteam/ ; https://appsecsanta.com/ai-security-tools/llm-red-teaming ; https://www.braintrust.dev/articles/best-llm-red-teaming-tools-2026
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Garak has 37+ probe modules and is the deepest open-source scanner... NVIDIA's Apache 2.0 command-line LLM vulnerability scanner." "Promptfoo covers 50+ vulnerability types with YAML configs and CI/CD integration... oriented around developer workflow integration rather than deep security research." "PyRIT supports multi-modal and multi-turn attacks including crescendo and TAP... Microsoft's MIT-licensed Python toolkit." "DeepTeam covers 40+ vulnerability types mapped to the OWASP Top 10 for LLM Applications... Apache 2.0 from the DeepEval team... mapped to the OWASP Top 10 for LLMs and Agents, NIST AI RMF, and MITRE ATLAS."
Guidance quoted verbatim: "run garak when you want a fast, broad vulnerability sweep with no code, PyRIT when you want to build adaptive multi-turn attack campaigns in Python, and DeepTeam when you need findings mapped to OWASP and NIST categories for a report someone will audit."
LABEL: third-party comparison sites (not vendor-stated, not independently benchmarked by us).

---

## GitHub — NVIDIA/garak (primary source)
- URL: https://github.com/NVIDIA/garak
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: "garak checks if an LLM can be made to fail in a way we don't want. garak probes for hallucination, data leakage, prompt injection, misinformation, toxicity generation, jailbreaks, and many other weaknesses." License: Apache-2.0. Maturity: "9.3k GitHub stars and 1.3k forks... 4,611 commits."
LABEL: primary source (project's own repo).

---

## GitHub — Azure/PyRIT (primary source, now archived/moved)
- URL: https://github.com/Azure/PyRIT
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: "PyRIT is an open source framework built to empower security professionals and engineers to proactively identify risks in generative AI systems." License: MIT. Stars: 115. Forks: 27. "Status: Archived as of March 27, 2026 (now read-only)... moved to https://github.com/microsoft/PyRIT for ongoing development."
LABEL: primary source (project's own repo). NOTE: star count (115) here is far lower than garak's 9.3k — likely reflects the archived/old repo location, not the live microsoft/PyRIT repo; flag as needing a pass-2 recheck against the new location.

---

## Promptfoo — Pricing page (primary source)
- URL: https://www.promptfoo.dev/pricing/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: Community tier: "Free Forever" — "Our open-source tool, perfect for individual developers and small teams" — includes "red teaming (10k probes/month), vulnerability scanning, and community support." Enterprise: "Custom" — "Enterprise pricing is customized based on your team's size and needs" — adds "team collaboration, continuous monitoring, centralized dashboard, customizable attack profiles, SSO, API access, managed cloud deployment, and professional support." On-Premise: "Custom" — adds "deployment on client infrastructure, complete data isolation, dedicated runner, and assigned deployment engineer."
LABEL: vendor-stated (primary/company page). No dollar figures published for paid tiers.

---

## Palo Alto Networks — Protect AI acquisition (primary press release)
- URL: https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-completes-acquisition-of-protect-ai
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: Completion date "July 22, 2025." Protect AI described as "an innovative leader in securing Artificial Intelligence (AI) applications and models" bringing "model scanning, posture management, AI red teaming, and AI agent security." Rationale: "Organizations are increasingly building complex ecosystems of AI models, applications, and agents. This creates a dynamic new attack surface with risks that traditional security approaches cannot address." Integrated into "Prisma AIRS platform."
Additional (via SEC 10-K/8-K search snippet, WebSearch): "total purchase consideration was $634.5 million... $607.4 million in cash and $27.1 million in fair value of replacement awards"; announced April 28, 2025.
LABEL: company-stated (Palo Alto Networks press release) + filed (SEC 10-K/8-K figures).

---

## Check Point — Lakera acquisition (primary press release)
- URL: https://www.checkpoint.com/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: Announced "September 16, 2025, with closing expected in Q4 2025. No financial terms were disclosed." Lakera described as "one of the world's leading AI-native security platforms for Agentic AI applications" providing "runtime protection for large language models, generative AI, and autonomous agents" against "prompt injection, data leakage, and model manipulation." Performance claim: "detection rates above 98 percent with sub-50ms latency and false positives below 0.5 percent." Traction claim: "trusted by Fortune 500 enterprises worldwide... powered by a team of 11 PhDs" with R&D in Zurich and San Francisco. Will form "Check Point's Global Center of Excellence for AI Security."
Deal value from separate WebSearch (Calcalist/CyberScoop): "estimated at $300 million" (undisclosed officially).
LABEL: company-stated (Check Point press release, incl. vendor performance claims — NOT independently verified) + analyst-derived (deal value, per Calcalist reporting).

---

## Snyk — Invariant Labs acquisition (primary press release)
- URL: https://snyk.io/news/snyk-acquires-invariant-labs-to-accelerate-agentic-ai-security-innovation/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: Deal date "June 24, 2025." Deal terms not disclosed. Invariant Labs (ETH Zurich spin-off, founded 2024 by Prof. Martin Vechev, Prof. Florian Tramèr and three graduates) built "Guardrails, a security layer for LLM and agent systems" and "MCP-Scan," and is credited with discovering "tool poisoning" and "MCP rug pulls" (April 2025). CEO quote: "This acquisition is an important integration into Snyk's recently launched AI Trust Platform that adds the ability to secure applications from emergent threats." Snyk goal: "a single platform to address both current application and agentic AI vulnerabilities."
LABEL: company-stated (Snyk press release).

---

## CrowdStrike — Pangea acquisition (primary press release)
- URL: https://www.crowdstrike.com/en-us/press-releases/crowdstrike-to-acquire-pangea-to-secure-every-layer-of-enterprise-ai/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: Announced "September 16, 2025, at Fal.Con 2025." Terms not disclosed in press release (WebSearch separately reports "CrowdStrike is reportedly paying roughly $260 million" — analyst-derived, per SDxCentral). Pangea "provides prompt-layer protection for enterprise AI applications" including "blocking prompt injection attacks, controlling risky AI use." CEO George Kurtz: "AI is rewriting the enterprise attack surface at breakneck speed. Each prompt becomes an entry point for the adversary." Goal: "industry's first complete AI Detection and Response (AIDR) platform," covering "data, models, agents, identities, infrastructure, and interactions."
LABEL: company-stated (CrowdStrike press release) + analyst-derived ($260M figure, SDxCentral).

---

## Cato Networks — Aim Security acquisition
- URL: https://www.securityweek.com/cybersecurity-ma-roundup-40-deals-announced-in-september-2025/ (aggregated with Calcalist reporting)
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Cato Networks acquired AI security company Aim Security... this is Cato's first-ever acquisition." "Financial terms of the deal were not officially disclosed, but Calcalist reported that Cato paid an estimated $300-350 million in cash and shares for Aim." Purpose: "expand its SASE Cloud Platform to enable enterprises to securely adopt AI agents and applications."
LABEL: company-stated (deal existence/rationale) + analyst-derived ($300-350M figure, per Calcalist).

---

## F5 — CalypsoAI acquisition
- URL: https://www.f5.com/company/news/press-releases/f5-to-acquire-calypsoai-to-bring-advanced-ai-guardrails-to-large-enterprises ; https://www.securityweek.com/f5-to-acquire-calypsoai-for-180-million/
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "F5 to Acquire CalypsoAI for $180 Million." "All shares of CalypsoAI, a company based in Ireland and the United States, were acquired by F5 for $180 million, mainly in cash." Expected to close "in F5's fourth quarter fiscal year 2025, ending September 30, 2025." CalypsoAI "founded in 2018... had raised over $40 million prior to its acquisition." Specializes in "protecting AI systems against emerging attack methods, including prompt injection and jailbreak attacks."
LABEL: company/press-stated ($180M figure appears consistently across multiple outlets — treat as reliable company-stated deal value, not SEC-filed).

---

## Cisco — Robust Intelligence acquisition
- URL: https://www.cisco.com/site/us/en/products/security/ai-defense/robust-intelligence-is-part-of-cisco/index.html ; https://blogs.cisco.com/news/fortifying-the-future-of-security-for-ai-cisco-announces-intent-to-acquire-robust-intelligence
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Robust Intelligence was acquired by Cisco in October 2024... reported to be for $400M." Company background: "San Francisco-based AI security company co-founded in 2019 by Harvard computer science professor Yaron Singer and Kojin Oshiba... pioneering the AI security category with... algorithmic red teaming and the industry's first AI Firewall." Became foundation of "Cisco AI Defense," offering "algorithmic red teaming, automated model assessment, and proactive AI risk mitigation aligned to OWASP and MITRE ATLAS standards."
LABEL: company-stated (Cisco blog) + analyst-derived ($400M figure reported, not officially confirmed in the fetched text).

---

## Softwarestrategiesblog — Agentic AI Security Startups Funding & M&A roundup
- URL: https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted table data — Top funded (adjacent, broader-security-with-AI-angle) startups: Cyera $1.7B+ total raised, Series F Jan 2026 $400M, valuation $9.0B. Saviynt ~$1.0B total, Series B growth Dec 2025 $700M, valuation $3.0B. Torq $332M total, Series D Jan 2026 $140M, valuation $1.2B. 7AI $166M total, Series A Dec 2025 $130M, valuation $700M. Noma Security $132M total, Series B Jul 2025 $100M. WitnessAI $85.5M total, Series B Jan 2026 $58M. Dropzone AI $57M total, Series B Jul 2025 $37M. Astelia $35M (Seed+A, Feb 2026). Runlayer $11M seed (Nov 2025). Helmet Security $9M seed (Dec 2025).
M&A: "Palo Alto Networks | CyberArk, Chronosphere, Protect AI | ~$29B" combined; "ServiceNow | Armis, Moveworks, Veza | $11.6B"; "Alphabet | Wiz | $32B — largest pure-play cybersecurity acquisition on record"; "Check Point | Lakera | Undisclosed."
RSAC 2026 (Mar 10-26) new funding: "$392 million in new agentic AI security funding was announced" — Oasis Security $120M Series B; XBOW $120M Series C; Surf AI $57M launch; RunSybil $40M seed/A; Qevlar AI $30M Series A; Eclypsium $25M strategic.
Traction: "Runlayer: eight unicorn customers in four months." "DXC (7AI deployment): 2.5 million alerts processed. 650,000+ investigations completed." "Manufact: 20% of US 500 companies have experimented with its MCP infrastructure."
MCP security funding specifically: "Total disclosed funding for pure-play MCP security: approximately $40 million across four startups" (Operant AI, Runlayer, Helmet Security, Manufact).
LABEL: analyst/blog-derived aggregation (secondary compilation of primary funding announcements — cross-check high-stakes figures against primary press releases before reuse).

---

## Menlo Ventures — Security for AI landscape
- URL: https://menlovc.com/perspective/security-for-ai-genai-risks-and-the-emerging-startup-landscape/
- Pulled: 2026-09-16
- Method: WebFetch

Quoted category breakdown: Governance — "Cranium" and "Credo" help organizations "create catalogs of AI services and assign risk scores." Observability — "Helicone" (broad model monitoring), "CalypsoAI" (security use-case-specific). Security: AI Firewalls — "Robust Intelligence," "Lakera," and "Prompt Security"; PII Redaction — "Private AI" and "Nightfall"; Red Teaming — "Lakera" and "Adversa"; Detection/Response — "Hiddenlayer" and "Lasso Security"; Federated Learning — "DynamoFL" and "FedML"; Synthetic Data — "Tonic" and "Gretel"; Code Scanning — "Protect AI"; Production Monitoring — "Giskard."
No specific market-sizing figures given; the article frames the opportunity as "massive opportunities" qualitatively only.
LABEL: VC-firm-stated (Menlo Ventures perspective piece — investor-interested source, categorization useful, sizing claims absent).

---

## MITRE ATLAS / OWASP LLM Top 10 — framework relationship
- URL: https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf ; https://www.vectra.ai/topics/mitre-atlas ; https://www.redfoxsec.com/blog/mitre-atlas-vs-owasp-llm-top-10-which-framework-should-you-use-in-2026
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems) is a knowledge base modeled after MITRE ATT&CK that documents adversarial tactics, techniques, and procedures (TTPs) specifically targeting machine learning systems," with "16 tactics and 84 techniques." "The OWASP LLM Top 10 is a community-driven list of the most critical security risks specific to Large Language Model applications." "ATLAS complements rather than competes with OWASP LLM Top 10 and NIST AI RMF — use all three for comprehensive coverage." Example mapping: "prompt injection is ATLAS technique AML.T0051 and OWASP LLM01."
LABEL: public/primary (OWASP and MITRE are open, public standards bodies — these are freely available frameworks, not proprietary IP).

---

## MCP security — OWASP MCP Top 10 (beta) and tool poisoning
- URL: https://labs.cloudsecurityalliance.org/research/csa-research-note-mcp-tool-poisoning-auto-execution-20260701/ ; https://github.com/snyk/agent-scan
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "The OWASP MCP Top 10 is in beta as of 2026" covering "token mismanagement and secret exposure (MCP01), privilege escalation via scope creep (MCP02), tool poisoning (MCP03), software supply chain attacks (MCP04), command injection and execution (MCP05), intent flow subversion (MCP06), insufficient authentication and authorization (MCP07), lack of audit and telemetry (MCP08), shadow MCP servers (MCP09), and context injection and over-sharing (MCP10)." Also: "Leading developer IDEs — including Cursor, Claude Code, Gemini CLI, GitHub Copilot, and Amazon Q — auto-execute project-defined MCP servers with developer-level OS privileges and no process isolation." "Tool poisoning is demonstrated, not theoretical: Invariant Labs proved in April 2025 that hidden instructions in tool descriptions enter the agent's context window as trusted content." Snyk's "agent-scan" OSS tool "detects 15+ distinct security risks across MCP servers and agent skills including prompt injection, tool poisoning, and tool shadowing."
LABEL: public standards-body-derived (OWASP MCP Top 10, beta) + primary research claim (Invariant Labs, now part of Snyk).

---

## HackerOne — AI vulnerability growth statistics (primary press releases)
- URL: https://www.hackerone.com/press-release/hackerone-launches-agentic-prompt-injection-testing-ai-vulnerabilities-surge-540 ; https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "AI vulnerabilities surged more than 200%, with prompt injection up 540%, confirming AI as the fastest-growing attack surface." "organizations expanded AI program adoption by 270% this year, while HackerOne's platform reported a 540% surge in prompt injection vulnerabilities." Earlier report figure: "210 percent growth in valid AI vulnerability reports, led by prompt injection." Bugcrowd figure (from earlier search): "82 percent of hackers are already using AI in their workflow" per Bugcrowd's 2026 report.
LABEL: company-stated (HackerOne's and Bugcrowd's own platform statistics — reflects HackerOne/Bugcrowd's bug-bounty submission volume, not total market activity).

---

## AI bug bounty programs — landscape (Wraith)
- URL: https://wraith.sh/learn/ai-bug-bounty-programs
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Every active AI bug bounty program in 2026 includes xAI/Grok, OpenAI, Anthropic, Google, Microsoft, Cohere, Mozilla 0din, and Gray Swan Arena. Payouts range from $200 for entry-level findings to $100,000 for exceptional discoveries." "Mozilla's 0din, OpenAI's Bugcrowd-hosted programs, and Anthropic's HackerOne program accept open submissions. However, Google's AI VRP excludes prompt injection and jailbreaks, so scope exclusions vary significantly across programs."
LABEL: third-party aggregator-stated (Wraith.sh; cross-check individual program terms against each vendor's own bug bounty page in pass 2).

---

## Gray Swan AI — funding and business model
- URL: https://www.forbes.com/sites/rashishrivastava/2026/05/28/this-ai-startups-army-of-15000-hackers-pressure-test-claude-gpt-5-and-gemini/ ; https://www.forbes.com/sites/sarahemerson/2024/10/29/this-hacker-team-is-bulletproofing-ai-models-for-companies-like-openai/
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "This AI Startup's Army Of 15,000 Hackers Pressure Test Claude, GPT-5 And Gemini" (Forbes headline, May 2026). "Gray Swan raised $40 million in Series A funding co-led by Wing VC and Madrona with participation from Snowflake Ventures, Hudson River Trading, and Samsung Next, bringing its valuation to $200 million." Partnerships: "OpenAI, Anthropic and the United Kingdom's AI Safety Institute." Model: crowdsourced jailbreaking arena/bounty platform (Gray Swan Arena) — "$40,000 in bounties" cited for one championship.
LABEL: company-stated (funding/valuation, per Forbes reporting) + vendor-claimed (15,000 hacker network size, unverified).

---

## EU AI Act — official implementation timeline
- URL: https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act
- Pulled: 2026-09-16
- Method: WebFetch

Quoted: "02 August 2026: The majority of rules of the AI Act come into force and enforcement starts for applicable rules" — includes "transparency obligations under Article 50," GPAI model obligations, prohibitions, AI literacy. "02 December 2026: New prohibitions targeting deepfakes and child safety materials take effect" plus a "Transitional deadline for certain providers of AI systems, including GPAI systems, generating synthetic content" for systems already on market before August 2026. "02 December 2027: Rules for high-risk AI systems in Annex III apply." "02 August 2028: Rules for high-risk AI embedded in regulated products covered by Annex I" — final milestone. Note: "The Digital Omnibus on AI amendments have modified certain provisions."
LABEL: filed/official (European Commission's own AI Act Service Desk — primary regulatory source).

---

## EU AI Act — high-risk deadline deferral (secondary legal commentary)
- URL: https://www.hklaw.com/en/insights/publications/2026/04/us-companies-face-eu-ai-acts-possible-august-2026-compliance-deadline ; https://www.hlc.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "the originally planned August 2, 2026 deadline for high-risk AI system obligations has been significantly delayed. For standalone high-risk AI systems classified under Annex III, the application of requirements is deferred until December 2, 2027, while obligations for high-risk AI systems embedded in regulated products in Annex I are deferred until August 2, 2028. This deferral replaces the current deadlines of August 2, 2026 for standalone high-risk AI systems and August 2, 2027 for high-risk AI systems embedded in regulated products." "The next hard date is August 2, 2026, featuring general application of the Act plus Article 50 transparency duties, which apply to every chatbot and every piece of synthetic content."
LABEL: filed/analyst-derived (law firm client-alert interpretation of the EU's own legislative delay — consistent with the EC's own timeline page above).

---

## ISO/IEC 42001 and NIST AI RMF — voluntary status confirmed
- URL: https://www.eccouncil.org/cybersecurity-exchange/responsible-ai-governance/eu-ai-act-nist-ai-rmf-and-iso-iec-42001-a-plain-english-comparison/ ; https://www.vanta.com/collection/iso-42001/nist-ai-rmf-and-iso-42001
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "ISO/IEC 42001 is a voluntary, certifiable management system standard — it provides auditable proof of AI governance maturity but creates no legal obligation." "NIST AI RMF is a voluntary operational framework — it provides the most detailed day-to-day risk management guidance but has no formal enforcement mechanism." "ISO 42001 requires a third-party audit; NIST AI RMF has no certification... formal audits or certifications by NIST do not yet exist." Timelines: "NIST AI RMF... you might be able to implement it within six to nine months. ISO 42001's certification timeline can be anywhere between 6–12 months or even longer." Adoption driver noted: "ISC2's Exam Guidance for AI (April 2026) cites NIST AI RMF and ISO 42001 as required compliance-tracking frameworks for AI governance professionals" (a professional-certification requirement, not a legal one).
LABEL: analyst-derived (compliance-tooling vendor content, e.g. Vanta; consistent across independent sources — treated as reliable secondary confirmation of a negative: no mandatory-purchase trigger from these two frameworks alone).

---

## Answer-engine poisoning — definition and vendor-solution gap (Wraith)
- URL: https://wraith.sh/learn/answer-engine-poisoning
- Pulled: 2026-09-16
- Method: WebFetch

Quoted definition: "an attacker publishes web content engineered to be cited, so the AI relays their misinformation, scam details, or instructions to everyone who asks." Distinguished from SEO poisoning: "AEP manipulates the synthesized answer itself" and "no click is required" — misinformation arrives "in the model's own confident voice." Distinguished from generic indirect prompt injection: AEP "targets multi-tenant public systems with broadcast payloads affecting thousands of users, not single applications."
Real-world evidence cited: "Schneier's test (2026): A fabricated claim published on Bruce Schneier's blog... within a day saw it repeated as fact by Google's AI Overviews and ChatGPT." Academic: "Nestaas, Debenedetti, and Tramer's research showed a targeted product became about 2.5 times more likely to be recommended" (citing arXiv 2406.18382, "Adversarial Search Engine Optimization for LLMs"). Also cites "Exposing Citation Vulnerabilities in Generative Engines" (arXiv 2510.06823). Third-party reporting cited: Aurascape, Huntress, Gizmodo.
EXPLICIT FINDING: "The document makes no mention of any commercial products designed to detect or defend against answer-engine poisoning." Defenses outlined are practices, not products: "Treat retrieved web content as untrusted input; cross-check high-stakes facts against authoritative sources; score source trust alongside relevance; detect injection patterns in retrieved content; display clear provenance to users."
LABEL: third-party publisher-stated (Wraith.sh educational content) citing primary academic research (arXiv papers) and independent real-world tests (Schneier). This is the key evidence for the AI-search overlap question.

---

## GEO/AEO tools — brand-visibility tools, NOT security products
- URL: https://gracker.ai/blog/best-geo-tools-for-cybersecurity ; https://scrunch.com/blog/best-answer-engine-optimization-aeo-generative-engine-optimization-geo-enterprise-platforms-2026 ; https://www.tryprofound.com/blog/best-generative-engine-optimization-tools
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Generative Engine Optimization (GEO) is the practice of getting your brand cited when AI engines answer user queries. An AEO/GEO platform is a software that helps brands track and improve how they appear in AI-generated search results across platforms like ChatGPT, Google AI Overviews, Gemini, Perplexity." Security framing found is aspirational, not a shipped defense feature: "The potential for adversarial manipulation of GE citation systems poses regulatory and ethical questions that the industry must address proactively." Enterprise differentiation is compliance-posture, not injection defense: "What separates a standard AEO/GEO tool from an enterprise platform is security, scale, and customizability... SOC 2 Type II certification, SSO, RBAC, and audit logs are table stakes." Named platforms: Profound AI, Semrush, Bluefish — all monitor/optimize brand visibility in AI answers; none described as detecting or blocking adversarial manipulation of what gets cited.
LABEL: vendor-comparison-site-stated. Confirms: GEO/AEO category exists and is well-funded/marketed, but it addresses brand visibility optimization, not adversarial defense against retrieval-layer prompt injection. Supports the prior-pass finding of no vendor productizing AI-search-manipulation defense specifically.

---

## HiddenLayer — funding and headcount
- URL: https://www.hiddenlayer.com/news/hiddenlayer-raises-50m-in-series-a-funding-to-safeguard-ai (Series A) ; https://cryptobriefing.com/hiddenlayer-100m-series-b-ai-security/ (Series B) ; https://profiles.crustdata.com/company/hiddenlayer (headcount)
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "The company raised $50M in Series A funding in 2023." "HiddenLayer confirmed the $100 million Series B on 2 September 2026. The round was led by Delta-v Capital, with Ten Eleven Ventures, Morgan Stanley, Microsoft's venture fund M12 and Booz Allen Ventures all participating." Headcount: "HiddenLayer has 169 employees as of May 2026" (consistent across sources for June 2026). Product scope: "HiddenLayer's ModelScanner supports 35+ formats including PyTorch, TensorFlow, ONNX, Keras, GGUF, pickle, and safetensors." "Pricing is based on the scope of models and deployments being protected" (no public price list).
LABEL: company-stated (funding rounds, per HiddenLayer's own announcements and press coverage) + third-party-derived (headcount, per Crustdata people-data aggregator — not company-confirmed).

---

## Mindgard — funding, headcount, and traction
- URL: https://dealroom.co/news/144657-mindgard-raises-30m-series-a-to-red-team-ai-systems/
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Mindgard raised $30 million in a Series A round led by Album VC, bringing the company's total funding to nearly $42 million. Karma Ventures joined, alongside returning backers .406 Ventures, Atlantic Bridge, IQ Capital, and Lakestar." "Founded in 2022 as a Lancaster University spinout and based in London and Boston." Traction claim: "the platform has uncovered more than 150 vulnerabilities across popular AI products, including a zero-day code execution flaw in Cursor IDE and defects in Google Antigravity and ChatGPT." Headcount: "As of June 2026, Mindgard has approximately 30 employees across 2 continents." Pricing: "Mindgard does not publish a public pricing page... sold through enterprise sales with quotes scoped to the number of AI systems under test."
LABEL: company-stated (funding, per Mindgard/Dealroom) + vendor-claimed (150+ vulnerabilities found — Mindgard's own claim, unverified) + third-party-derived (headcount, per LeadIQ-style aggregator).

---

## Cranium AI and Enkrypt AI — funding and further consolidation
- URL: https://cranium.ai/resources/press-release/cranium-series-a-funding-to-secure-ai/ ; https://pitchbook.com/profiles/company/536946-40 (Enkrypt AI)
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Cranium AI has raised $52M in total funding over multiple rounds... most recent funding round in July 2026." Investors: "Microsoft for Startups, Alternative Investment Management, Titanium Ventures, and York IE." Further consolidation: "Cranium AI's most recent deal was a Merger/Acquisition with AIceberg, made on 21-May-2026." Separately: "Enkrypt AI was acquired on 04-Aug-2026 by Anaconda" — Enkrypt "provided runtime protection for AI agents and generative AI applications, as well as automated adversarial testing for AI agents and models."
LABEL: analyst-derived (Pitchbook/Crunchbase/Tracxn-style aggregator data — deal dates and amounts not cross-checked against primary press releases in this pass).

---

## Pillar Security — funding
- URL: https://de.tradingview.com/news/reuters.com,2025-04-16:newsml_GNX4BnZsZ:0-pillar-security-raises-9m-to-help-enterprises-build-and-run-secure-ai-software
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Founded in 2023 by Dor Sarig (CEO) and Ziv Karliner (CTO), Pillar Security raised a $9M seed round announced in April 2025, led by Shield Capital, with Golden Ventures, Ground Up Ventures, and strategic angels."
LABEL: company-stated (per Reuters wire, republished by TradingView).

---

## Gartner — 2026 AI spending forecasts (context, not AI-security-specific)
- URL: https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-forecasts-worldwide-ai-spending-to-grow-47-percent-in-2026 ; https://www.gartner.com/en/newsroom/press-releases/2026-07-20-gartner-forecasts-worldwide-ai-platforms-and-models-market-to-grow-63-percent-in-2026
- Pulled: 2026-09-16
- Method: WebSearch

Quoted: "Worldwide spending on AI is forecast to total $2.59 trillion in 2026, a 47% increase year-over-year." "AI infrastructure... will be the largest segment... accounting for over 45% of spending." "Worldwide end-user spending on AI models and platforms is projected to total $64 billion in 2026, up 63.4% from $39 billion in 2025." NOTE: No Gartner figure found specifically scoped to "AI TRiSM" (Trust, Risk and Security Management) spend in this pass — general AI spend cited for context only, NOT to be conflated with the AI-security-testing market.
LABEL: analyst-derived (Gartner press releases — figures are for total AI spending, not AI security specifically; flagged for pass-2 to find a TRiSM-specific number if it exists).

---
