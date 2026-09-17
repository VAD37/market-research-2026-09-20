# Who pays for answer-engine integrity

Pass 2, 2026-09-16. Compiled from `../raw/buyer-integrity-pulls.md` (41 blocks) and `../raw/buyer-integrity-source-index.md`. Answers the #1 open question in `../findings/cross-read.md`.

Question as posed: a brand is damaged by what ChatGPT / AI Overviews / Perplexity says about it. Who holds the budget line — and has anyone bought anything in that shape.

## The answer, short

Pass 1 said "no buyer found." That narrows to: **one vendor is already selling it, into the brand-protection budget, and the rest of that category has not followed.**

BrandShield launched **AI Platforms Protection on 2026-04-01** — monitoring ChatGPT, Gemini, Perplexity and Grok for "impersonation, phishing links, misinformation, and counterfeit promotion" (vendor-stated). Sold to the buyer that already pays for domain and social brand protection. No pricing disclosed; demo-request only.

That is the whole affirmative case. Everything else found in this pass is either visibility spend, ad-adjacency spend, or post-harm legal cost.

## The DRP category — checked one by one

| Vendor | Covers LLM answer content | As of |
|---|---|---|
| BrandShield | **Yes, explicitly.** ChatGPT, Gemini, Perplexity, Grok | 2026-04-01 |
| Doppel | No. Domains, social, ads, apps, dark web | 2026-09-16 |
| Memcyco | No. Impersonation sites, account takeover | 2026-09-16 |
| Bolster / CheckPhish | No. Phishing pages, fraudulent ads | 2026-09-16 |
| Netcraft | No. Phishing, domain spoofing | 2026-09-16 |
| ZeroFox | No explicit claim. 180+ platforms, none named as answer engines | 2026-09-16 |
| Recorded Future, Red Points | unknown — no primary product page reached 2026-09-16 | — |

Every "No" here is a checked negative, not an absence of checking. In each case the vendor's "AI" language refers to its own detection engine, not to coverage of what answer engines say.

Read: the budget exists and is proven — these firms sell impersonation and takedown to real buyers today. One of eight has extended it to answer engines. That is a window, not a wall.

## Ad verification — adjacent, not the same problem

Every incumbent shipped an AI product in the last ten months. None of them verify AI answers.

| Vendor | Shipped | Date | What it does |
|---|---|---|---|
| DoubleVerify | DV AI Verification, AI SlopStopper | 2025-11-04 | Separates declared agents from undeclared bots; avoids ad placement near AI slop |
| DoubleVerify | SlopStopper for social | 2026-04-17 | 500M+ impressions monitored or blocked since Jan 2026 (company-stated) |
| HUMAN Security | Ad Integrity Suite | 2026-06-16 | IVT, brand safety, viewability. No answer-engine mention |
| HUMAN Security | LLM and AI Agent Governance | 2026-09-16 | Verifies agents by cryptographic signature; scraping-bot detection |
| IAS | IAS Agent | Q1 2026, free | Campaign-ops copilot. Internal, not a verification surface |
| Zefr | AI adjacency study | 2026-03-02 | Measures ad performance next to AI-generated content |

The distinction that matters: all of this is **"don't let my ad appear near AI slop."** None is **"stop the AI from making a false claim about my brand."** Same buyer, different product. HUMAN's agent-signature work is the closest technical adjacency — see `../markets/injection-feasibility.md` when written.

## Legal — the budget that is actually moving

Litigation is the strongest evidence in this pass that money changes hands over a wrong AI answer. It is defence cost after harm, not a subscription before it.

| Case | Status | Numbers |
|---|---|---|
| Starbuck v. Google, Del. Super. Ct. | Motion to dismiss **denied 2026-07-24** | Court credited false output reaching **2,843,917 unique users** |
| Starbuck v. Meta | Filed Apr 2026, settled Aug 2026 | No monetary terms. Meta agreed to work on removing AI bias |
| Wolf River Electric v. Google | Removed to D. Minn., live Jan 2026 | Damages **$110M–$210M** (plaintiffs' disclosures, 2025-06-03) |
| Brian Hood v. OpenAI, Australia | Threatened Apr 2023 | Outcome unknown — checked 2026-09-16 |
| OLG Hamm, Germany | Ruled **2026-05-12** | First-party chatbot; operator liable for hallucination |

Wolf River is the one with documented, itemized commercial harm: a **$174,044.12** nonprofit project terminated 2025-03-11 and a separate **$150,000** contract cancelled, from an AI Overview that attributed to it a lawsuit naming four other companies. Plaintiffs' earlier letter (2025-03-14) claimed **$24.7M** damage in 2024 alone. Headline damages figures conflict across outlets ($110M vs $210M) — both on file, unreconciled.

Two qualifiers: Starbuck is an individual plaintiff, not a company buying defence. OLG Hamm is liability for a company's **own** chatbot — a different fact pattern from a third-party answer engine, and closer to the AI-application-security market pass 1 already sized.

No law firm found marketing a discrete "AI defamation" practice line as of 2026-09-16. These matters run inside general AI-litigation groups (Quinn Emanuel, Cooley, Edelson).

## Insurance — the market is splitting in two directions

| Instrument | Direction | Date |
|---|---|---|
| ISO **CG 40 47 / CG 40 48** endorsements | **Excludes** generative-AI personal and advertising injury from CGL | effective Jan 2026 |
| Armilla AI, Lloyd's coverholder | **Affirmatively covers** defamation from AI output, to **$25M** per insured | expanded early 2026 |
| Coalition Affirmative AI Endorsement | Covers AI-enabled attacks on the insured's systems | 2024-03-26 |

"Personal and advertising injury" is the CGL grant that historically covered defamation. Where a carrier adopts CG 40 47/48, AI-linked defamation leaves the standard policy. Armilla pays defence "from dollar one... in a market where most general liability carriers are now refusing to defend the same claim" (company-stated).

Read: insurers have priced this risk as real enough to both exclude it and to underwrite it separately. An underwriting requirement is the classic mechanism that forces a security purchase. None found yet requiring answer-engine monitoring.

## Where marketing's money actually goes

Confirmed spend is on **visibility**, not integrity.

| Line | Price | Label |
|---|---|---|
| Boutique / SMB GEO retainer | $1,500–$5,000/mo | aggregator |
| Mid-market retainer | $5,000–$10,000/mo | aggregator |
| Enterprise retainer | $10,000–$50,000+/mo | aggregator |
| One-time GEO audit | $1,500–$5,000 | aggregator |
| GEO added to an SEO retainer | +20–30% of current MRR | aggregator |
| Reputation firm (Status Labs) | ~$2,500–$50,000/mo | aggregator, not vendor-confirmed |

**No price found anywhere, in any channel, for a defense-specific line item.** That is the finding.

Budget scale around it: CMOs allocate **15.3%** of marketing budget to AI (Gartner, 401 respondents, fielded Jan–Mar 2026, analyst-derived) — with no brand-safety or answer-integrity line named in the public release. On the security side, **69%** of CISOs name AI their top investment priority against ~5% overall budget growth (RH-ISAC, analyst-derived) — with those dollars going to AI application security, not to third-party answer monitoring.

Both budgets are growing. Neither has a bucket labelled this.

## The headcount signal

One named, funded, budgeted role: **Golden Hippo, "Director, AI Brand Visibility," $152,000–$200,000** plus bonus. Requires digital PR, SEO, schema markup, entity optimization, and crisis-communications experience. The role sits in PR/comms, not security — confirming pass 1's read on who is closest to owning this.

But the job as written is **presence and monitoring, not defence**. It does not ask the hire to detect or counter a manipulated answer. Listing closed 2025-12-05; evidence the budget existed, not that it is open.

Also found: Kendra Scott, "Manager, Search and AI Discovery" — snippet only, full text unconfirmed.

## Regulators are moving the wrong way for this idea

- FTC v. DoNotPay: **$193,000** consumer redress, Sep 2024 (filed).
- FTC v. Rytr consent order **set aside Dec 2025**, per the administration's AI Action Plan, on the grounds it burdened AI innovation.
- FTC policy statement, **Jul 2026**: hallucinations "in and of themselves" do not raise Section 5 issues; misrepresenting their likelihood still can.

No compliance mandate is forming behind answer accuracy. Same direction as pass 1's EU AI Act deferral finding. Demand here is discretionary through 2027 at least.

## Caveats

- BrandShield's launch date and scope are vendor-stated via secondary press. No customer, price or contract value found.
- Recorded Future and Red Points were not cleared — no primary product page reached. The DRP negative is seven of nine, not nine of nine.
- ZeroFox, Netcraft, Bolster and Memcyco negatives are search-level checks, not deep crawls of the vendor sites.
- **Conflict left standing:** two syntheses of the same Conductor "State of AEO/GEO" CMO survey (250+ execs) disagree on whether 2026 GEO budget is new money or reallocated from SEO, content and digital PR. Neither traceable to Conductor's own text. This decides whether an integrity line could draw on new dollars or must win a zero-sum fight. Re-fetch the primary report.
- Semrush's claimed $87,400 average enterprise ACV and 23 Fortune-100 clients: **unknown — checked WebSearch 2026-09-16.** No citable primary URL. Do not use.
- Digital Risk Protection market sizes came back at **$88–97B for 2026** across three analyst houses — two orders of magnitude above pass 1's AI-security sizings and above most published cybersecurity-software totals. Category definition is almost certainly non-standard. Do not use for sizing the DRP vendor set.
- Gartner, HUMAN and Library of Congress primary pages returned HTTP 403; Wolf River's Star Tribune page returned 429. All worked around via secondary sources and labelled as such.
- Brian Hood's outcome after the 2023 threat is unresolved, leaving the earliest case in this fact pattern open.
