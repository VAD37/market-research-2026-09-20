# Small-business blind spots — where the wedge is

2026-09-17. Research delegated to a general-purpose agent (33 tool uses, direct fetch + search), findings verified against the sources it cited. Evidence: `../../raw/smallbiz-blind-spots-pulls.md`. Scope: sub-question asking which big-company practices a 3-10 person business measurably does not do, and why (expensive / lacks data / lacks skill).

## Ranked by strength of sourcing

| Rank | Practice | Size-stratified evidence? | Verdict |
|---|---|---|---|
| 1 | **Pricing review** | **Yes, direct, size-stratified, dated 2024** | Strongest finding in this pass |
| 2 | Management-reporting / KPI discipline | Yes for BI adoption (size-stratified); academic anchor excludes firms <50 employees | Strong but the academic literature has a hole exactly at the size this project targets |
| 3 | Cohort/funnel analysis | Proxy only (via BI-tooling adoption) | Moderate — no direct study found |
| 4 | Competitive monitoring | Recent data exists, not size-stratified | Weak |
| 5 | Churn post-mortems | Vendor how-to content only | Weakest — no adoption-rate study found |
| 6 | Pipeline/CRM hygiene | Numbers exist but trail dead-ends in circular blog citations | Unverifiable — deliberately excluded, not guessed |

## The sharpest finding: pricing review

**Source: Price Intelligently by SBI, "The State of B2B SaaS Pricing in 2024," survey of 760 B2B SaaS leaders, stratified by revenue band ($0-1M through $1bn+).** Vendor-reported, but a real survey with a real n and real size stratification — not an aggregator estimate.

> "Large companies are most likely to employ value-based pricing, because they have the most resources to do the proper research to figure out their value. But value-based pricing is powerful and shouldn't be reserved for big business."

The report's own chart ("Most common pricing strategies by annual revenue," p.11): the smallest cohort ($0-1M ARR) is heaviest on **competitor pricing (~54%, the highest of any band)** and lightest on **value-based pricing (~20%, the lowest of any band)**. By $500M+ revenue, value-based pricing becomes the plurality strategy (~45%) and competitor pricing falls to ~28%.

> "Most common inputs to pricing research process: Competitive analysis 43%, Current customer feedback 34%, Previous market research 14%, Previous experience 7%, No formal process 2%."

**Why, per the source explicitly**: cost of the research, not lack of desire. Proper value-based pricing research is "time-consuming and expensive to implement properly" — small firms substitute a free, low-effort proxy (copying competitor list prices) instead of running willingness-to-pay research. **This is the one blind spot in this pass with a clean resource-constraint story and a directly automatable fix**: willingness-to-pay research, competitor price tracking, and periodic repricing recommendations are all agent-shaped tasks.

## Second-strongest: management reporting / KPI discipline

**Source: CIO.com, "Are SMBs invited to the business intelligence (BI) party?", 2023-02-06, citing Fortune Business Insights market data.**

> "the overall adoption rate of business intelligence is just 26% compared to 80% in companies with over 5,000 employees"

Cited reasons in the article: "lack of scalable technology infrastructure," "insufficient skilled workforce," budget/perception barriers.

**Academic anchor, and its own gap**: Bloom & Van Reenen, "Measuring and Explaining Management Practices Across Firms and Countries," CEP Discussion Paper No. 716 (2006; published QJE 2007, 122(4):1351-1408) — the seminal World Management Survey. Its "Performance tracking" / "Performance review" dimensions score firms 1-5; a Score-1 real example from the paper: "A manager of a US firm tracks a range of measures when he does not think that output is sufficient. He last requested these reports about 8 months ago and had them printed for a week until output increased again." Better-managed firms track and review KPIs continuously and formally; poorly-managed firms (6.9% of the sample scored <=2) do it reactively or not at all — predicts productivity, profitability, survival and sales growth at p<0.01.

**The gap in the gap**: the WMS sample is medium manufacturers, 50-10,000 employees. The paper explicitly excludes firms under 50 employees because "very small firms have little publicly available data" (p.14). **That exclusion is itself evidence of the mechanism**: sub-10-person firms lack the disclosure/data infrastructure that even makes formal measurement possible in the first place — nobody has rigorously studied firms this project's size doing this practice, because the data to study them doesn't exist. That is a "needs data they don't have" answer, sourced by absence rather than by a direct number.

## Weaker findings, recorded so nobody re-chases them without new leads

- **Cohort/funnel analysis**: no source found that measures this specifically by company size; the BI-adoption proxy above is the closest available signal.
- **Competitive monitoring**: Crayon's "2026 State of Competitive Intelligence" has current numbers ("nearly 8 in 10 teams actively track 30 competitors or fewer," "67% track just ten or fewer sources") but not broken out by company size.
- **Churn post-mortems**: only vendor how-to content (Avoma, Paddle, TheySaid) recommending the practice; one unattributed methodology claim ("only 27.4% of stated exit-survey reasons matched the root cause") whose source study could not be verified — excluded.
- **Pipeline/CRM hygiene**: aggregator pages (SuperOffice, Wave Connect, sellerscommerce) cite figures like "50% of businesses under 10 employees use a CRM" vs. "95-98% enterprise adoption," but every trail dead-ends in circular blog citations with no traceable primary study. Per this repo's evidence rules, excluded rather than guessed. `unknown — checked web search/fetch 2026-09-17`.

## Read for the design phase

The pricing-review finding is the one to build the wedge argument on: it is size-stratified, dated, resource-attributed by the source itself, and the fix (WTP research, competitor price tracking, repricing cadence) is exactly the shape of "small bounded task" the brief says agent execution can be trusted for (sub-question 3) — research a person/topic, record a fact, watch a trend — as opposed to the "don't trust agent-authored dashboards" side of the line.

The KPI-discipline finding is second-strongest but has a structural hole: no primary study covers firms this small, because firms this small don't generate the data that would let researchers study them. That absence is itself an argument for the product — if academia can't get data on how 3-10-person firms track their own numbers, that is one more data point that they mostly don't, formally.

## Caveats

- All figures are vendor-reported (Price Intelligently/SBI) or a single secondary article citing a market-research firm (CIO.com/Fortune Business Insights), not independently re-verified against the primary Fortune Business Insights report this pass.
- The Bloom & Van Reenen paper is 2006/2007-dated (a 20-year-old primary study), used here only for its methodology and its explicit small-firm-exclusion admission, not as a current adoption number.
- Three of six practices (competitive monitoring, churn post-mortems, pipeline/CRM hygiene) have no defensible size-stratified source as of this pull — treat their absence from a strong evidence base as a research gap, not as evidence the practices aren't also blind spots.
- The researching agent used both web search and direct fetch; exact source URLs are in `../../raw/smallbiz-blind-spots-pulls.md`.
