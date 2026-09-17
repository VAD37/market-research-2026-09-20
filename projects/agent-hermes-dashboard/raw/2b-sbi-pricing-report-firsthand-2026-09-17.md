### Source: Price Intelligently by SBI, *The State of B2B SaaS Pricing in 2024* — FIRST-HAND PRIMARY PULL

- URL: https://sbigrowth.com/hubfs/1-Research%20Reports/11.2024%20State%20of%20B2B%20SaaS%20Pricing%20Price%20Intelligently/SBI_StateofB2BSaaSPricing2024.pdf
- Pull date: 2026-09-17
- Method: `curl -sL` direct download → HTTP 200, `application/pdf`, 255,857 bytes, 20 pages. Text layer extracted with `pdftotext -layout` (poppler). Chart values are NOT in the text layer (vector-rendered, no data labels), so pages 5 and 11 were rasterised at 200 dpi with PyMuPDF and read visually by this agent. This is a first-hand fetch by wave 2b, replacing the second-hand relay in `smallbiz-blind-spots-pulls.md`.
- Label: vendor-reported.

---

## 1. What the prior chain claimed, and what the document says

Prior chain: `raw/smallbiz-blind-spots-pulls.md` (delegated sub-agent relay, never fetched by this project) → `docs/explore/smallbiz-blind-spots.md` → `docs/plan/idea-set.md`.

### 1a. n = 760 — CONFIRMED verbatim

> "We spoke to 760 B2B SaaS leaders about how they are making their pricing decisions." (p.4)

### 1b. Chart p.11 "Most common pricing strategies by annual revenue" — CONFIRMED, read first-hand off the rendered page

Five revenue bands. Values as read from the bars (bars are unlabelled; read against the 10%-gridline axis):

| Band | Competitor pricing | Cost-plus pricing | Value-based pricing |
|---|---|---|---|
| $0-1m | ~54% | ~24% | ~21% |
| $1-9m | ~42% | ~34% | ~24% |
| $10-99m | ~42% | ~29% | ~29% |
| $100-499m | ~33% | ~33% | ~33% |
| $500m+ | ~28% | ~26% | ~45% |

The relayed figures (~54% / ~20% at $0-1m; ~45% / ~28% at $500M+) match this agent's own reading of the same chart. The chart is on p.11 as claimed.

### 1c. The headline quote — CONFIRMED verbatim, but truncated in the relay

> "If you look at the most common pricing strategies by annual revenue, we see that more mature companies shift both to value-based pricing and product-led tactics.
>
> Large companies are most likely to employ value-based pricing, because they have the most resources to do the proper research to figure out their value.
>
> But value-based pricing is powerful and shouldn't be reserved for big business. **Even companies as small as $1M ARR should be able to execute this without having to resource a giant in-house team.**" (p.11, sidebar)

The bolded final sentence was dropped by the relay.

### 1d. The "inputs to pricing research" figures — CONFIRMED

Chart, p.9: Competitive analysis 43% / Current customer feedback 34% / Previous market research 14% / Previous experience 7% / No formal process 2%. Body text on the same page gives the unrounded pair: "The most common input into pricing research is competitive analysis (42.5%), with current customer feedback following closely behind (33.7%)."

### 1e. The resource-cost attribution — **NOT what the relay said it was**

The relay stated: *"Why (per the source, explicitly): resource cost. Proper value-based research is 'time-consuming and expensive to implement properly' — small firms substitute a free, low-effort proxy (copying competitor list prices) instead of running willingness-to-pay research."*

The quoted phrase exists, verbatim, but it is on p.12, inside a paragraph about the drawbacks of value-based pricing as a method — with no reference to firm size, and not as an explanation of small-firm behaviour:

> "Let's explore the pitfalls of value-based pricing. It can be time-consuming and expensive to implement properly. With price sensitivity measurements and feature analysis you are only going to get approximations of the right pricing, packaging, and positioning for your product. But this is much closer to the truth than using only costs or competitors to set your price." (p.12)

The only other cost-adjacent statement is on p.9, also unstratified by size:

> "Market research that includes data on buyers who are not customers, in addition to your current customers, is most objective and useful to your pricing strategy. While it shouldn't be your only research metric, it's the biggest lever you could be ignoring because it's expensive or time consuming." (p.9)

The one genuinely size-attributed causal sentence in the whole document is 1c's "Large companies are most likely to employ value-based pricing, because they have the most resources" — a statement about large firms having resources, not about small firms being priced out of research. The "small firms substitute a free proxy because research is expensive" mechanism is the **sub-agent's synthesis**, not the report's claim.

---

## 2. Population definition — read first-hand, p.4 and p.5

> "The primary B2B target buyer for these businesses is predominantly in the **mid-market (50.7%)** followed by **enterprise (31.1%)** and **SMB (18.3%)**." (p.4)

> "When we look at the go-to-market models of the respondents we spoke to, the majority (62.5%) are either sales-led or sales-assisted, 37.4% of the businesses are product-led (PLG) or product-assisted." (p.4)

Chart p.5, "Survey respondents by go-to-market model": Sales-assisted 36% / Sales-led 27% / Product-assisted 22% / Product-led 16%.

Chart p.5, "Survey respondents by annual revenue" — data-labelled, read directly:

| Band | Share of respondents |
|---|---|
| $0-1m | **10.8%** |
| $1-9m | 12.9% |
| $10-49m | 16.4% |
| $50-99m | 9.5% |
| $100-249m | 15.5% |
| $250-499m | 9.7% |
| $500-999m | 15.4% |
| $1bn+ | 9.7% |

**Derived by this pull (this agent's arithmetic, not a published figure): the $0-1m cohort is 10.8% of 760 ≈ 82 respondents.** The load-bearing 54% / 21% figures are a subgroup of n≈82, not n=760.

The document nowhere reports employee headcount, and nowhere describes respondents as small businesses. Respondents are described throughout as "B2B SaaS leaders", "B2B pricing leaders", and "pricing professionals" — p.6 titles a chart "Primary success metric for pricing professionals".

No methodology section exists in the document: no fielding dates, no sampling frame, no recruitment method, no margin of error. Searched the full text layer for "methodolog", "sample", "survey" — the only hits are body-copy advice to readers about their own research, plus the two quoted lines above.

---

## 3. Publisher and commercial interest — verbatim, pp.19-20

> "How can Price Intelligently by SBI help? With over a decade of experience, Price Intelligently has worked with some of the largest subscription companies to implement value-based pricing and has developed a toolkit of frameworks, survey methods, and algorithms to collect and analyze quantitative and qualitative data. ... **Book yourself a free 30-minute consultation with our pricing experts** ... [button] **Book a free pricing audit**" (p.19)

> "SBI acquired Price Intelligently from Paddle in November 2024 to strengthens [sic] SBI's existing pricing practice..." (p.20)

Page 4 footer carries the data attribution: "Source: ProfitWell, By Paddle". Footnote p.3: "ProfitWell Metrics is the analytics team of Price Intelligently."

The document is a lead magnet that closes with a CTA to buy value-based pricing consulting, published by the firm that sells it.

---

## 4. Figures in the report that cut AGAINST a "small firms are blind" framing

Read first-hand, p.7:

> "Over 94% of pricing leaders update pricing and packaging at least once per year, with almost 40% updating as often as once per quarter."

> "Since September 2022, 98% of those surveyed have made updates to their pricing or packaging. Among them, 43.8% have made updates to both."

Chart p.7, "Frequency of pricing changes": Quarterly 38% / Semi-annually 31% / Annually 25% / Every few years 6%.
Chart p.7, "Updated pricing since September 2022": Both pricing and packaging 44% / Packaging only 35% / Pricing only 19% / **No updates 2%**.

Neither chart is broken out by revenue band, so these cannot be attributed to the $0-1m cohort specifically.

---

## 5. Directional reading of the p.11 chart — stated as this agent's reading, not the report's words

The chart does not show that the $0-1m cohort neglects competitor pricing. It shows the opposite: the $0-1m cohort uses competitor pricing **more than any other band (~54%)**, and the report's surrounding prose treats that as the error to be corrected:

> "The problem with competitive pricing is that you are putting a higher value on your competitors than your customers. Your customers don't care about your competitors, they care about you." (p.11, pull-quote)

> "Your competitors often won't know their own value. Mirroring them will likely end up in a 'blind leading the blind' phenomenon across your products." (p.11)

The practice the report identifies as under-used at $0-1m is **value-based pricing (~21%)**, whose input is willingness-to-pay research on non-customers — not competitor price observation.
