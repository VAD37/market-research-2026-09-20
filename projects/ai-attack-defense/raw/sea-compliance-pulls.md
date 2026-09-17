# SEA compliance-trigger evidence — raw

Pull date: 2026-09-17. Method: WebSearch (quota was live this session despite the 2026-09-16 200/200 exhaustion note — several calls succeeded, two returned "unavailable" mid-session, treated as transient not hard-exhausted) and WebFetch against primary/near-primary pages. `../../../docs/markets/vietnam-sg-access.md` covers entity/banking/payments access only, not compliance triggers — no overlap to avoid redoing.

## Singapore — AI Verify (IMDA)

WebFetch of `aiverifyfoundation.sg/what-is-ai-verify/`, fetched 2026-09-17. Synthesis of page content: AI Verify is **voluntary** — "helping companies assess the responsible implementation of their AI system," framed as an optional governance approach. Documented requirement if adopted: align to 11 AI governance principles, collect documentary evidence, generate compliance reports. Page states no enforcement mechanism, no penalty, no mandatory deadline. Explicitly names three user types: AI application owners/developers "looking to demonstrate," internal compliance teams, and "External Auditors looking to validate your clients' implementation" — third-party validation is possible but not required by the framework itself.

## Singapore — MAS FEAT principles

WebSearch synthesis, fetched 2026-09-17 (primary MAS URL for the AI-in-financial-sector guidelines page returned a maintenance/unavailable page on WebFetch attempt — could not reach primary). Search-tool synthesis: "The Monetary Authority of Singapore (MAS) introduced 'FEAT' (fairness, ethics, accountability, and transparency) principles in 2018." 14 principles across 4 pillars. Fairness pillar quoted via synthesis: "Data and models used for AIDA-driven decisions should be regularly reviewed and validated for accuracy and relevance, and to minimize unintentional bias." No quoted mandatory-testing or red-teaming language found. **Labeled analyst/search-synthesis, not independently confirmed against the MAS primary document this pull** — `unknown — checked mas.gov.sg via WebFetch 2026-09-17, page returned maintenance/unavailable error`.

## Vietnam — Personal Data Protection Law (PDPL)

WebSearch synthesis, fetched 2026-09-17, citing (per the search tool's own result list, not independently re-fetched) Tilleke & Gibbins, IAPP, DLA Piper Data Protection Laws of the World, DFDL, and DataGuidance. Synthesis: Law No. 91/2025/QH15, passed by the National Assembly 2025-06-26, **effective 2026-01-01**. Implementing Decree No. 356/2025/ND-CP issued 2025-12-31, also effective 2026-01-01 — this decree supersedes the earlier Decree 13/2023/ND-CP named in the project brief. Automated-decision/AI provision per synthesis: "AI-driven processing that affects individuals requires transparency on automated decision logic, meaningful explanations of impact, and opt-out mechanisms." Also per synthesis: "enforceable data subject rights, mandatory data protection officers, formal impact assessment requirements, and criminal penalties alongside administrative fines." **Not independently verified against the law's primary text this pull** — `unknown — checked via WebSearch synthesis 2026-09-17, no primary Vietnamese-language statute text fetched`.

## Vietnam — AI Law / Law on Digital Technology Industry

Not independently re-pulled this session — already compiled in `../../../docs/findings/pass3-read.md` (read this session, not redone per instruction): "Vietnam's AI Law — passed 2025-12-10, effective 2026-03-01 — does require foreign high-risk-AI providers to hold a commercial presence or authorized representative." That file itself flags this as needing further primary verification (it was sourced from a Localization-play pass this project did not re-open). One direct-fetch attempt this pull (`vietnam-briefing.com` guessed URL) returned 404 — the correct URL was not located within this pull's budget.

## Indonesia — PDP Law (UU PDP)

WebSearch synthesis, fetched 2026-09-17, citing (per the tool's result list) Securiti.ai, Future of Privacy Forum, Regulations.AI, Pertama Partners, FKNK. Synthesis: "The personal data controller has an obligation to conduct a data protection impact assessment related to the processing of personal data with automated decision-making that has legal consequences on the owner of the personal data." Enforcement per synthesis: "administrative fines capped at 2% of their annual global revenue," plus "written warnings, temporary suspension of AI processing activities, and the mandatory deletion of illegally processed data." Transition period for UU PDP ended October 2024; "2026 marks the beginning of active enforcement" per synthesis. Forward-looking note per synthesis, unconfirmed against any bill text: "the forthcoming Perpres and RUU AI will introduce specific 'AI-conformity' penalties for providers who fail to register high-risk systems or perform mandatory impact assessments" — this is a proposed/future instrument, not current law. **Entirely search-synthesis sourced, no primary Indonesian statute or regulation text fetched this pull** — `unknown — checked via WebSearch synthesis 2026-09-17, primary UU PDP text and any AI-specific Perpres not fetched`.

## WebSearch quota behavior this session

Two consecutive WebSearch calls returned "Web search error: unavailable" mid-pull (for "Vietnam Law on Digital Technology Industry 2025 AI provisions" and a repeat Vietnam PDPL query), immediately followed by other WebSearch calls succeeding normally. Read as intermittent rate-limiting rather than the flat 200/200 exhaustion the brief warned about — the quota appears to have partially reset since 2026-09-16, but is not fully reliable. Recorded per instruction; further compliance-trigger research budget should assume some calls will silently fail and re-try or fall back to direct fetch.

## Caveats

- Every finding in this file above the "not independently re-pulled" line rests on WebSearch's own synthesis of secondary/law-firm-blog sources, not a fetched primary statute. This is weaker sourcing than the rest of this project's raw pulls and is labeled as such throughout `docs/explore/sea-compliance-triggers.md`.
- MAS's own primary guidance page could not be reached (maintenance error) — the FEAT-principles content here is second-hand.
- No penalty figure, enforcement-authority name, or "does it name AI systems" answer in this file has been checked against a primary legal text. Treat every row in the compiled doc as `analyst-derived / search-synthesis` unless marked otherwise.
