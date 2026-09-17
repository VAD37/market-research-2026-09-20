# Wave 2b adversarial review — the pick's own economics

Pull date: 2026-09-17. Purpose: verify the "~$27,000/yr senior Vietnamese developer" figure `docs/plan/niche-and-solutions.md` §4 uses as its pricing-ceiling argument, and establish what the product could charge and to how many buyers.

---

## PULL 1 — ITviec salary report, primary figure

Source: ITviec, "Vietnam IT Salary & Recruitment Market Report 2025-2026".
URL: https://itviec.com/report/vietnam-it-salary-and-recruitment-market
Method: WebFetch, 2026-09-17. Label: **vendor-reported** (job board's own survey).

Report metadata as returned:
- Sample size: **1,839 respondents**
- Survey periods: **2025-05-27 to 2025-07-31** and **2025-10-21 to 2025-11-11**
- Publication year: 2025

Salary table, Back-end Developer, VND per month, by experience band:

| Experience | VND/month |
|---|---|
| 3–4 years | 30.1 million |
| 5–8 years | 39.9 million |
| **>8 years** | **54.9 million** |

Tech Lead: median 51.8 million overall; >8 years 68.45 million.

The report as fetched gives **no USD conversion** and **no separate AI-engineer band**.

### Arithmetic and the conversion gap

54.9 million VND/month × 12 = **658.8 million VND/year**, gross salary to the employee.

USD equivalent depends on an FX rate that was **not pulled**: at 24,400 VND/USD it is ~$27,000; at 26,300 VND/USD it is ~$25,000. `unknown — VND/USD rate not pulled 2026-09-17`.

Note the band: 54.9M VND/month is the **">8 years, Back-end Developer"** cell, not a generic "senior" figure. Employer total cost (statutory social/health/unemployment insurance contributions on top of gross) was **not pulled** and is not included.

Corroborating WebSearch synthesis, 2026-09-17, query "ITviec IT salary report 2025 2026 Vietnam senior developer average salary VND per month": "Senior developers with seven-plus years typically earn 50-61 million VND per month"; "Senior data or AI engineers reach VND 57 million or above at three to four years of experience"; "66.1% of companies increased IT headcount in 2025".

---

## PULL 2 — what the product could charge, and to how many buyers

Channels checked 2026-09-17 for a Southeast Asian or Vietnamese price point for AI security testing, guardrail evaluation, or LLM red-teaming tooling:

- `../../../docs/markets/ai-attack-defense.md` and `../../../docs/markets/ai-attack-defense-services.md` — both carry only US/EU vendor-published or aggregator-derived bands. `docs/plan/niche-and-solutions.md`'s own caveat states this: "No SEA price point for AI security testing exists anywhere in this repo."
- No new pull attempted against a Vietnamese vendor price list this pass — no such vendor is named anywhere in this project's research layer.

**Buyer population size.** `../../../docs/markets/vietnam-sg-access.md` names three Vietnamese companies operating public Vietnamese-language LLM products (AI Hay, Vbee, Filum AI). No census, directory, or count of Vietnamese companies operating a public Vietnamese-language chatbot was pulled this pass or any prior pass.

Status: **`unknown — checked this repo's markets/ and customers/ layer 2026-09-17; neither a SEA price point nor a buyer count exists in any pulled source`.** Neither number is derivable from what is pulled, and inventing either would poison the compiled tables.
