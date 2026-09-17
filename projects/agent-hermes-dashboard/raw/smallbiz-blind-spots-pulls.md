### Source: delegated general-purpose research agent — SMB practice-gap evidence review
- Pull date: 2026-09-17 (agent ran ~449s, 33 tool uses, mix of WebSearch and WebFetch — this agent's own quota, not the parent's)
- Method: sub-agent dispatched with instructions to find sourced evidence (surveys, vendor research, academic literature) on 6 candidate SMB practice gaps, ranked by strength/recency of sourcing, explicitly told to skip rather than guess. This file is the agent's full returned report, relayed verbatim below — NOT a direct primary-source fetch by the main research thread. Where the agent quotes a primary source, that quote is one level removed (agent's transcript, not this thread's own fetch) — treat accordingly; the compiled `../docs/explore/smallbiz-blind-spots.md` cites this file, and the underlying primary URLs are listed at the bottom for anyone who wants to re-fetch directly.

## Agent's full report, verbatim

Six weeks of searching turned up genuinely strong, size-stratified evidence for two of the six practices, decent proxy evidence for two more, and essentially nothing citable for the last two. Ranked by strength/recency of sourcing:

### 1. Pricing review — strongest evidence

Source: Price Intelligently by SBI, "The State of B2B SaaS Pricing in 2024" (2024), survey of 760 B2B SaaS leaders, stratified by revenue band ($0-1M through $1bn+).

Direct quote: "Large companies are most likely to employ value-based pricing, because they have the most resources to do the proper research to figure out their value. But value-based pricing is powerful and shouldn't be reserved for big business."

The report's own "Most common pricing strategies by annual revenue" chart (p.11) shows the smallest cohort ($0-1M ARR) is heaviest on competitor pricing (~54%, the highest of any band) and lightest on value-based pricing (~20%, the lowest of any band); by $500M+ revenue, value-based pricing becomes the plurality strategy (~45%) and competitor pricing falls to ~28%. Elsewhere: "Most common inputs to pricing research process: Competitive analysis 43%, Current customer feedback 34%, Previous market research 14%, Previous experience 7%, No formal process 2%."

Why (per the source, explicitly): resource cost. Proper value-based research is "time-consuming and expensive to implement properly" — small firms substitute a free, low-effort proxy (copying competitor list prices) instead of running willingness-to-pay research. This is a direct, size-stratified, dated, resource-attributed data point — the strongest single finding in this review.

### 2. Management-reporting / KPI discipline — strong but indirect on firm size

Source: CIO.com, "Are SMBs invited to the business intelligence (BI) party?" (Feb 6, 2023), citing Fortune Business Insights market data.

Quote (near-verbatim from the article): "the overall adoption rate of business intelligence is just 26% compared to 80% in companies with over 5,000 employees." Cited reasons in the article: "lack of scalable technology infrastructure," "insufficient skilled workforce," and budget/perception barriers ("BI doesn't align with budget constraints").

Corroborating academic anchor: Bloom & Van Reenen, "Measuring and Explaining Management Practices Across Firms and Countries," CEP Discussion Paper No. 716 (March 2006; published as QJE 2007, 122(4): 1351-1408) — the seminal World Management Survey paper. Their interview guide's "Performance tracking" and "Performance review" dimensions score firms 1-5, with a Score-1 real example: "A manager of a US firm tracks a range of measures when he does not think that output is sufficient. He last requested these reports about 8 months ago and had them printed for a week until output increased again." Better-managed firms track and review KPIs continuously and formally; badly-managed firms (6.9% of their sample scored <=2) do it reactively or not at all, and this predicts productivity, profitability, survival and sales growth (p<0.01 across specifications).

Caveat: the WMS sample is medium manufacturers (50-10,000 employees) — the paper explicitly excludes firms under 50 employees because "very small firms have little publicly available data" (p.14). That line is itself evidence of the "why": micro-firms lack the disclosure/data infrastructure that even makes formal measurement possible, which is why no rigorous size-stratified study of sub-10-person firms' reporting discipline appears to exist.

### 3. Cohort/funnel analysis — moderate, via analytics-tooling proxy

Same CIO.com/Fortune Business Insights BI-adoption gap (26% vs. 80%) is the best available proxy, since cohort/funnel analysis is a specific application of BI/product-analytics tooling. No source found specifically measuring cohort- or funnel-analysis adoption broken out by company size — a genuine evidence gap, not something the agent was willing to guess at.

### 4. Competitive monitoring — weak

Crayon, "The 2026 State of Competitive Intelligence" has real recent numbers (e.g., "nearly 8 in 10 teams actively track 30 competitors or fewer," "67% track just ten or fewer sources") but the published version accessible does not break results out by company size. No survey located that gives a clean "X% of small firms vs. Y% of large firms track competitors" figure. Skipped rather than guessed.

### 5. Churn post-mortems — weakest

Only vendor how-to content found (Avoma, Paddle, TheySaid) recommending exit interviews/churn post-mortems as best practice, and one unattributed methodology claim ("only 27.4% of stated exit-survey reasons matched the root cause") whose original study could not be verified. No adoption-rate survey by company size exists in what was found.

### 6. Pipeline/CRM hygiene — unverifiable

Multiple secondary aggregator pages (SuperOffice, Wave Connect, sellerscommerce) cite figures like "50% of businesses under 10 employees use a CRM" vs. "95-98% enterprise adoption," but none traced to a primary, datable study confirmed directly — the trail dead-ends in circular blog citations. Per instruction to skip rather than guess, not included as usable numbers.

### Agent's recommendation for the product

The one number worth building a business case on is the pricing-strategy gap (Price Intelligently/SBI 2024): small companies default to copying competitor prices because value-based pricing research is expensive and skill-intensive, not because they don't see the value. That's a clean, sourced, resource-constraint story — and a very automatable one (willingness-to-pay research, competitor price tracking, and periodic repricing recommendations).

### Sources (as given by the agent)

- Price Intelligently by SBI, *The State of B2B SaaS Pricing in 2024* — https://sbigrowth.com/hubfs/1-Research%20Reports/11.2024%20State%20of%20B2B%20SaaS%20Pricing%20Price%20Intelligently/SBI_StateofB2BSaaSPricing2024.pdf (2024)
- CIO.com, "Are SMBs invited to the business intelligence (BI) party?" — https://www.cio.com/article/453900/are-smbs-invited-to-the-business-intelligence-bi-party.html (Feb 6, 2023)
- Nick Bloom & John Van Reenen, "Measuring and Explaining Management Practices Across Firms and Countries," CEP Discussion Paper No. 716 — https://worldmanagementsurvey.org/wp-content/images/2011/01/WP_Measuring-and-Explaining-Management-Practices-Across-Firms-and-Countries-Bloom-and-Van-Reenen.pdf (March 2006; published QJE 2007, 122(4):1351-1408)
- Crayon, *The 2026 State of Competitive Intelligence* — https://www.crayon.co/state-of-competitive-intelligence-2026 (2026)

Not cited / could not verify (excluded per instructions): churn-post-mortem adoption rates by company size; CRM/pipeline-tracking adoption rates by company size; cohort/funnel-analysis-specific adoption rates by company size. Recorded as `unknown — checked web search/fetch 2026-09-17`.

## Note on evidence chain

This file is a relay of a sub-agent's report, not a first-hand pull by the explore agent that owns this project. The sub-agent's own tool transcript (its actual fetches) is not preserved here — only its final synthesized report, with the URLs it cites. Per `../../../CLAUDE.md`'s evidence rule ("never compile from memory"), this is treated as acceptable because the sub-agent's report itself functions as a dated, attributed source document, and every number in the compiled `../docs/explore/smallbiz-blind-spots.md` traces to this file. A future pass wanting first-hand primary-source pulls should re-fetch the four URLs above directly.
