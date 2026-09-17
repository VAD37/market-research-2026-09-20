# Cloudflare Workers free/paid limits, KV/D1/R2 free allowances, domain cost — raw pull

Pulled: 2026-09-17. Method: WebFetch (plain fetch, no browser — browser tools reserved for wave 1b). All quotes are the fetch tool's verbatim rendering of the live page; page "Last Updated" stamps were not surfaced by the fetch tool and are noted as absent below.

## Source 1 — Workers limits table

URL: `https://developers.cloudflare.com/workers/platform/limits/`
Kind: vendor-reported (Cloudflare docs).

| Feature | Workers Free | Workers Paid |
|---|---|---|
| Requests | "100,000/day" | "No limit" |
| CPU time | "10 ms" | "5 min" |
| Memory | "128 MB" | "128 MB" |
| Subrequests | "50/request" | "10,000/request" |
| Simultaneous connections | "6" | "6" |
| Environment variables | "64/Worker" | "128/Worker" |
| Variable size | "5 KB" | "5 KB" |
| Worker size | "64 MiB" | "64 MiB" |
| Startup time | "1 second" | "1 second" |
| Number of Workers | "100" | "500" |
| Cron Triggers per account | "5" | "250" |
| Static Asset files | "20,000" | "100,000" |
| Individual file size | "25 MiB" | "25 MiB" |

Duration limit note (same page): for HTTP requests, no enforced wall-time limit while the client stays connected; for scheduled tasks (Cron Triggers, Queue consumers, Durable Object alarms), "15 min" maximum wall time applies to both plans.

## Source 2 — Workers pricing page

URL: `https://developers.cloudflare.com/workers/platform/pricing/`
Kind: vendor-reported.

**Workers Free:**
- "100,000 per day" requests
- "10 milliseconds of CPU time per invocation"
- No overage charges for either metric (free tier simply stops / errors past the cap — page states no overage billing exists on Free)

**Workers Paid ($5/month minimum):**
- "10 million included per month" requests, then "$0.30 per additional million"
- "30 million CPU milliseconds included per month" CPU time, then "$0.02 per additional million CPU milliseconds"
- CPU cap: "Max of 5 minutes of CPU time per invocation (default: 30 seconds)"
- "There are no additional charges for data transfer (egress) or throughput (bandwidth)" on the Paid plan.

**What forces the paid plan, read off these two sources together:** the Free plan's 100,000 requests/day and 10ms CPU/invocation are hard caps with no stated overage path — Cloudflare's own free-tier framing is "the request errors past the cap," not "you get billed." The Paid plan is the only tier with an overage-billing model at all. For this project's Worker (IP-range CIDR match against an incoming request, log, optionally serve variant body), 10ms CPU/invocation and 100k req/day are very unlikely to bind for a single low-traffic instrumented domain; the paid plan would only become necessary if traffic crossed 100,000 requests/day.

## Source 3 — Workers KV limits

URL: `https://developers.cloudflare.com/kv/platform/limits/`
Kind: vendor-reported.

| Feature | Free | Paid |
|---|---|---|
| Reads | "100,000 reads per day" | "Unlimited" |
| Writes to different keys | "1,000 writes per day" | "Unlimited" |
| Storage/account | "1 GB" | "Unlimited" |
| Key size | "512 bytes" | "512 bytes" |
| Value size | "25 MiB" | "25 MiB" |
| Keys/namespace | "Unlimited" | "Unlimited" |
| Namespaces per account | "1,000" | "1,000" |

Note: the fetch did not surface separate delete/day or list/day figures; the page frames per-invocation KV operations under a general limit the fetch summarized as "1,000 per invocation" for both tiers — not independently re-verified against the raw HTML this pass.

## Source 4 — D1 limits

URL: `https://developers.cloudflare.com/d1/platform/limits/`
Kind: vendor-reported.

| Feature | Free | Paid (Workers Paid) |
|---|---|---|
| Databases per account | "10" | "50,000" |
| Maximum database size | "500 MB" | "10 GB" |
| Maximum storage per account | "5 GB" | "1 TB" |
| Queries per Worker invocation | "50" | "1000" |

Note: rows-read/rows-written per day figures were not surfaced by this fetch — not in the summarized table returned. Flag: `unknown — checked developers.cloudflare.com/d1/platform/limits/ 2026-09-17, fetch tool did not return a rows-read/rows-written row`.

## Source 5 — R2 pricing (free allowance + paid rates)

URL: `https://developers.cloudflare.com/r2/pricing/`
Kind: vendor-reported.

**Free tier (monthly allowance):**
- Storage: "10 GB-month / month"
- Class A operations (writes/lists): "1 million requests / month"
- Class B operations (reads): "10 million requests / month"

**Paid (Standard storage):**
- Storage: "$0.015 / GB-month"
- Class A operations: "$4.50 / million requests"
- Class B operations: "$0.36 / million requests"
- Egress bandwidth: complimentary across all storage classes (no charge) — this is R2's headline differentiator vs S3.

Note: free tier applies to Standard storage only, not Infrequent Access.

## Source 6 — Cloudflare Registrar pricing model (no numeric TLD price list retrievable by plain fetch)

URLs tried: `https://developers.cloudflare.com/registrar/about/pricing/` (404), `https://www.cloudflare.com/products/registrar/` (200, no price table), `https://www.cloudflare.com/tld-pricing/` (404), `https://developers.cloudflare.com/registrar/` (200, no price table, points to `/registrar/llms.txt`), `https://developers.cloudflare.com/registrar/llms.txt` (200, index has no pricing-specific page listed).

Kind: vendor-reported (qualitative only — no per-TLD number retrievable this pass).

Quotes retrieved from `cloudflare.com/products/registrar/`:
- "Never pay more than we do"
- "Registration, transfer, and renewal prices are always at or below what registries and ICANN charge us."
- "Cloudflare Registrar does not mark up domain prices at all."
- "Cloudflare ensures customers only pay the price charged by registries and ICANN for domain registration and renewal, eliminating extra fees when buying a domain."
- "See registration, transfer, and renewal prices upfront, with no hidden fees or required add-ons."

**`unknown — checked developers.cloudflare.com/registrar 2026-09-17`: no per-TLD numeric price list is published on a plain-fetchable static page.** Cloudflare's actual TLD price list lives behind the dashboard/account login (consistent with a registrar that resells at wholesale registry price, which varies by TLD and can change with the registry). No account creation or purchase was attempted, per instructions.

## Source 7 — Comparable registrar, numeric TLD prices (since Cloudflare's own list is not plain-fetchable)

URL: `https://porkbun.com/products/domains`
Kind: vendor-reported (Porkbun, not Cloudflare — cited as "a comparable registrar" per the task instruction, not as a Cloudflare-equivalent price).

| TLD | Registration (list) | First-year sale price | Renewal |
|---|---|---|---|
| .com | $11.08/year | (none stated) | $11.08/year |
| .net | $12.52/year | (none stated) | $12.52/year |
| .org | $11.84/year | $7.98 | $11.84/year |
| .xyz | $14.21/year | $2.04 | $14.21/year |
| .dev | $12.87/year | $8.75 | $12.87/year |
| .click | $10.81/year | $1.54 | $10.81/year |
| .site | $28.84/year | $1.96 | $28.84/year |
| .online | $28.84/year | $1.96 | $28.84/year |

**Cheapest usable TLD by first-year price in this list: `.click` at $1.54, or `.site`/`.online` at $1.96 — but both `.site` and `.online` renew at $28.84/year**, an 18x jump from year 1 to year 2. `.click`'s renewal ($10.81) is much closer to its first-year-sale price, making it the cheaper TLD over a 2-year horizon among the discounted options. `.com` has no first-year discount but the flattest price ($11.08 registration = $11.08 renewal, no cliff).

Namecheap's public pricing page (`namecheap.com/domains/`) returned HTTP 403 to the fetch tool — not retrieved, not retried with a browser per instructions (1b owns browser work).

## Caveats

- Cloudflare's own per-TLD price list was not reached by plain fetch; the domain-cost figures above are from Porkbun, a comparable registrar, not Cloudflare Registrar itself. Cloudflare's qualitative claim ("at cost, no markup") means its actual price for a given TLD tracks the registry's wholesale price, which is a different (usually lower, since no markup) number than a retail registrar like Porkbun charges — this is a directional read, not a quoted number, and should not be treated as equal to Cloudflare's price.
- D1 rows-read/rows-written per day were not returned by the fetch tool's summary; flagged unknown above rather than guessed.
- KV per-invocation operation cap (stated by the fetch tool as "1,000 per invocation" for both tiers) was not independently re-verified against raw HTML — carried as reported, not re-confirmed.
- No page "Last Updated" stamp was captured for any Workers/KV/D1/R2 doc page this pass (the fetch tool's markdown conversion did not surface it) — dates given are pull dates, not doc-revision dates.
