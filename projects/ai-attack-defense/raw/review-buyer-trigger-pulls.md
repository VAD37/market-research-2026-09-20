# Wave 2b adversarial review — buyer chain and Vietnam content/AI regime

Pull date: 2026-09-17. Methods stated per pull. Purpose: settle two items `docs/plan/niche-and-solutions.md` flagged `unknown — not pulled` — (a) whether real vendor security questionnaires carry AI red-teaming or guardrail-testing items and whether that chain reaches a Vietnamese supplier, (b) whether Vietnam's content-control regime reaches a company operating a public Vietnamese-language chatbot and implies testing.

**Sourcing warning applying to every pull in this file except PULL 3:** these are law-firm, consultancy and vendor secondary sources reached through WebSearch and WebFetch. No primary statute text, and no primary questionnaire document (SIG workbook, CAIQ spreadsheet) was obtained — both sit behind registration or paywalls. Label: analyst-derived / search-synthesis.

---

## PULL 1 — Shared Assessments SIG, 2026 release

Attempt A: https://sharedassessments.org/blog/2026-sig-workbook-updates/ — WebFetch 2026-09-17 returned a **Microsoft Entra sign-in interstitial**, no content. `unknown — primary publisher page gated 2026-09-17`.

Attempt B: Mitratech, "SIG 2026: Key Updates and Considerations".
URL: https://mitratech.com/resource-hub/blog/sig-2026-key-updates-and-considerations/
Page publication date as returned: **2026-03-05**. Method: WebFetch, 2026-09-17.

Verbatim extracts:

> "the rapid deployment of third-party AI and the challenges of complex supply chain resilience"

> "The most significant addition is the comprehensive mapping to ISO 42001, the international standard for AI Management Systems."

> "You can now systematically query vendors on their internal AI governance controls using recognized industry standards."

> "assess vendors on the whole AI lifecycle — from data collection and model training to deployment and bias monitoring"

> "This effectively turns 'Shadow AI' risk into a visible, assessable metric."

> "AI Due Diligence is Now Mandatory: With ISO 42001 questions available, failure to screen vendors for AI governance may be viewed as a gap in oversight."

Explicitly **not** found on this page: NIST AI RMF, model testing, red teaming, adversarial testing, guardrails. The AI content of the 2026 SIG as described here is **governance** (ISO 42001 management-system questions), not **testing**.

Supporting WebSearch synthesis, 2026-09-17, query "Shared Assessments SIG 2026 questionnaire artificial intelligence red teaming content library update": reports the 2026 SIG "standardizes AI assessment, allowing you to assess vendors on the whole AI lifecycle", adds ISO 42001 and NIST AI RMF references, introduces "Hover Helpers" and "Scoping Presets (Lite, Core, Detail)", and that Shared Assessments launched "SIG Evolution (SIG EV)" in March 2026. The synthesis states directly: "the search results do not contain specific information about red teaming content library updates within the 2026 SIG questionnaire."

---

## PULL 2 — CSA AI Controls Matrix (AICM) and AI-CAIQ

Source: Cloud Security Alliance artifact page.
URL: https://cloudsecurityalliance.org/artifacts/ai-controls-matrix
Method: WebFetch, 2026-09-17.

Verbatim:

> "The AI Controls Matrix (AICM) is a first-of-its-kind vendor-agnostic framework for cloud-based AI systems."

Dates on the artifact page: **Released 07/09/2025; Updated 10/30/2025.** Scope: "243 control objectives distributed across 18 security domains."

On the questionnaire, verbatim:

> "A set of questions that map to the AICM. These questions can guide organizations in performing a self-assessment or an evaluation of third-party vendors."

This is the **AI-CAIQ** (AI Consensus Assessment Initiative Questionnaire). The CSA artifact page as fetched contains **no mention of red teaming or adversarial testing**.

Third-party coverage analysis (NOT primary CSA text — treat as analyst-derived):
URL: https://www.opensecurityarchitecture.org/frameworks/csa-aicm/coverage/ ("CSA AI Controls Matrix v1.0.3 — SP 800-53 Coverage"), WebFetch 2026-09-17. Control IDs and wording returned:

| Control ID | Wording as returned by that page |
|---|---|
| AIS-13 AI Sandboxing | "AICM requires AI red teaming including adversarial ML attacks, prompt injection testing, model extraction attempts, and AI-specific threat simulation." |
| MDS-03 Model Documentation | "Model validation and testing including accuracy validation, bias testing, robustness testing, and adversarial evaluation." |
| MDS-08 Model Integrity Checks | "adversarial attack testing, evasion resistance, and model hardening against adversarial inputs" |
| AIS-05 Application Security Testing | maps to "penetration testing; vulnerability scanning; developer security testing", gap noted as "AI-specific security testing including adversarial robustness testing, model extraction attacks, and training data poisoning assessments" |
| TVM-06 Penetration Testing | "AICM extends penetration testing to AI-specific attack vectors including adversarial inputs and model extraction attempts." |

Caveat on PULL 2: these strings come from a coverage-analysis site, not from the AICM spreadsheet itself. The AICM/AI-CAIQ workbook is a registration-gated CSA download and was not obtained. `unknown — primary AICM control text not pulled 2026-09-17`.

Secondary WebSearch synthesis, 2026-09-17, same query: AICM "is accompanied by the AI Consensus Assessment Initiative Questionnaire (AI-CAIQ) and a pathway to STAR for AI certification", and maps to "ISO/IEC 42001, NIST AI 600-1, and the BSI AIC4 Catalog".

---

## PULL 3 — Does the vendor-questionnaire chain reach a Vietnamese supplier

Source: 724SOFTWARE (a Vietnamese software company, offices Hanoi and Ho Chi Minh City), "What SOC 2 Type II and ISO 27001:2022 Actually Mean for a Vietnam Software Team Building in Regulated Industries".
URL: https://724software.com.vn/insights/what-soc-2-type-ii-and-iso-270012022-actually-mean-for-a-vietnam-software-team-building-in-regulated-industries
Page publication date as returned: **2026-06-08**. Method: WebFetch, 2026-09-17. Label: **company-stated**.

Verbatim, the one direct statement on questionnaires:

> "when a Fintech or Healthcare client sends a vendor security questionnaire asking about secure SDLC controls, an ISO 27001 certified team can map answers directly to audited Annex A controls rather than making informal assertions."

The page contains **no mention** of AI-specific security questions, AI red-teaming, or guardrail testing. It references "vulnerability management" and "penetration testing" as generic practices.

Supporting WebSearch synthesis, 2026-09-17, query "Vietnam software outsourcing company SOC 2 Type II ISO 27001 client security questionnaire compliance FPT KMS Saigon Technology": reports Saigon Technology as ISO 9001 + ISO 27001 third-party certified; TMA Solutions as CMMI Level 5, ISO 9001, ISO 27001, TL 9000; and that "Top Vietnamese vendors hold ISO 27001, ISO 9001, and CMMI Level 3 to Level 5 certifications... to meet client security questionnaire requirements." No AI-specific questionnaire content surfaced for any Vietnamese vendor.

---

## PULL 4 — Vietnam Decree 147/2024/ND-CP (internet services and online information)

Source: Tilleke & Gibbins, "A Closer Look at Vietnam's Decree 147 on Internet Services and Online Information".
URL: https://www.tilleke.com/insights/a-closer-look-at-vietnams-decree-147-on-internet-services-and-online-information/
Method: WebFetch, 2026-09-17. Label: analyst-derived (law firm).

Effective date: **2024-12-25**.

Scope as returned:
- Offshore providers offering "cross-border information provision", defined as provision by overseas organizations/individuals of "information and online information content services for service users in Vietnam"
- Onshore social network services offered by organizations with legal status in Vietnam
- Online game service providers; app store service providers
- Telecom, internet, web hosting, data center, and telecom application service providers
- Public internet access point owners offering paid services
- "Regulated cross-border providers" = those who lease Vietnam data storage **or** receive 100,000+ monthly visits from Vietnam for six consecutive months

Content obligations as returned:
- Remove content violating law within "24 hours from the time of a request from the relevant authority"
- Handle user complaints within "48 hours of receiving complaints" regarding prohibited content
- Report violations within "24 hours of self-discovery or receipt of feedback"
- "Inspect, monitor, prevent, and remove violating 'content, services, and applications'"
- Authenticate user accounts via Vietnamese mobile phone numbers or ID numbers
- Classify and display warnings for child-inappropriate content; report annually to authorities

Enforcement, verbatim: authorities may "enforce technical measures to block non-compliant content, services, and applications, as well as impose administrative penalties". No penalty amounts given.

**AI and chatbots: not mentioned** anywhere in the returned content.

Corroborating WebSearch synthesis, 2026-09-17: Decree 147 issued 2024-11-09, effective 2024-12-25; 24-hour removal on authority request; "Service providers must report to the relevant authority within 24 hours of self-discovery or receipt of feedback or complaints from users about content, services, and applications that violate **Article 8 of the Cybersecurity Law**."

Attempt at primary text: https://thuvienphapluat.vn/van-ban/Cong-nghe-thong-tin/Nghi-dinh-147-2024-ND-CP-...aspx returned **HTTP 403** to WebFetch 2026-09-17. `unknown — Vietnamese primary statute text not reached 2026-09-17`.

---

## PULL 5 — Vietnam Law on Artificial Intelligence, Law No. 134/2025/QH15

This is the item wave 1's `docs/explore/sea-compliance-triggers.md` carried forward unverified from `pass3-read.md` as a mere "presence/representative requirement". Two independent law-firm readings were pulled.

### 5a — Tilleke & Gibbins

URL: https://www.tilleke.com/insights/a-closer-look-at-vietnams-new-ai-law-what-it-means-for-ai-businesses/
Method: WebFetch, 2026-09-17. Label: analyst-derived (law firm, Vietnam practice).

- Law on Artificial Intelligence **No. 134/2025/QH15**, adopted **2025-12-10**, effective **2026-03-01**.
- Three risk tiers, verbatim definitions as returned:
  - High-risk: systems that "may cause significant harm to life, health, or the lawful rights and interests"
  - Medium-risk: systems that "may have the potential to confuse, influence, or manipulate users"
  - Low-risk: all remaining systems
- High-risk systems must undergo: "Mandatory conformity assessment before deployment"; "Third-party certification (if specified by prime minister's list)"; "Continuous risk management and data governance controls"; "Technical documentation maintenance"; "Human oversight protocols".
- Transparency, verbatim: developers and providers must ensure "users can recognize when they are interacting with an AI system"; "AI-generated audio, images, and videos are appropriately marked" per government standards; deployers must provide "clear disclosure and visible labeling" when AI-generated or AI-edited content is published publicly.
- Scope, verbatim: the law applies to "Vietnamese organizations and individuals, as well as foreign entities that participate in AI-related activities within Vietnam", with exclusions for national defense and security.

### 5b — Baker McKenzie

URL: https://www.bakermckenzie.com/en/insight/publications/2026/02/vietnam-artificial-intelligence-law-foundation-and-outlook
Method: WebFetch, 2026-09-17. Label: analyst-derived (law firm).

- Effective **2026-03-01**. Grace periods for existing AI systems: **12 months**, extended to **18 months** for health, education and finance.
- Risk tiers and their supervision routes:
  - High-risk (HRAI): "Subject to periodic audits and pre-market conformity assessments"
  - Medium-risk: "Supervised through reports and independent assessments"
  - Low-risk: "Monitored for incidents and complaints"
- HRAI provider obligations: "Maintain commercial presence or authorized representatives in Vietnam"; "Undergo pre-market conformity certification (when specified by Prime Minister)"; "Submit to regular audits and testing procedures".
- Testing and evaluation, verbatim: high-risk systems undergo "periodic audits or audits on signs of violation"; medium-risk systems require "sample audits or assessments by independent organizations"; "Specific evaluation methodologies will be detailed in implementing regulations."
- Content labelling: providers must mark AI-generated audio, image and video content in machine-readable formats; deployers must clearly indicate authenticity risks.
- Extraterritorial scope: applies to domestic and foreign entities conducting AI activities within Vietnam.

### 5c — corroborating search synthesis

WebSearch, 2026-09-17, query "Vietnam Law on Digital Technology Industry 2025 AI-generated content labelling identifier obligation high-risk AI effective 2026":

> "Vietnam enacted the Law on Digital Technology Industry ('DTI Law') on June 14, 2025, which will take effect on January 01, 2026. The DTI Law establishes a risk-based regulatory approach to AI, requiring stringent technical standards and data governance for AI in high-risk sectors (e.g., healthcare, finance, social order, safety), mandating labeling for interactive AI and identification marks for AI-generated content."

> "On 10 December 2025, the National Assembly of Vietnam passed Law No. 134/2025/QH15 on Artificial Intelligence (the 'AI Law'), taking effect on 1 March 2026, making Vietnam one of the first countries in Southeast Asia to establish a comprehensive, risk-based regulatory framework for AI systems."

> "AI deployed in sectors, such as finance, healthcare, education, infrastructure, and justice, is subject to pre-market approval and must undergo mandatory government assessment and registration before deployment. High-risk AI (HRAI) systems will be subject to periodic audits or audits on signs of violation."

### 5d — what is NOT established by these pulls

- No source reached states which risk tier a general-purpose public consumer chatbot falls into. The medium-risk definition ("may have the potential to confuse, influence, or manipulate users") is the closest fit on its face, but the classification is not confirmed for any named Vietnamese chatbot.
- No source reached says an audit or conformity assessment must include adversarial, safety or guardrail testing. Both sources say the evaluation methodology is deferred to implementing regulations not yet issued as of these pulls.
- No primary statute text of Law 134/2025/QH15 was fetched. Both readings are law-firm secondary.
- Nothing quoted mentions language coverage, Vietnamese-language safety, or content moderation quality as an audit criterion.
