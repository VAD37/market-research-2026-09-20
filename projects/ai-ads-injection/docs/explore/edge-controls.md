# Edge controls — what the CDN actually exposes for branching on a crawler signal

2026-09-17. New ground — pass 2 did not cover the delivery question. Sourced from `raw/policy-and-edge-pulls.md` (WebFetch pulls, 2026-09-17). Primary: Cloudflare. Alternative: Fastly.

## Cloudflare — the concrete primitives, ranked by what they can actually do

| Primitive | Can vary response BODY? | Signal it reads | Plan tier | Source |
|---|---|---|---|---|
| **Workers** | **Yes — full response, including body, is under script control.** Vendor's own example category: "Conditional response... Return a response based on the incoming request's URL, HTTP method, User Agent, IP address, ASN or device type." | UA, IP, ASN, device type, and (if wired in) `request.cf.botManagement.score`/`.verified_bot` | Free tier runs Workers; the bot-management object's richer fields are gated by plan (see below) | `developers.cloudflare.com/workers/examples/` |
| **WAF custom rules** | **No.** Action list is Block, Managed Challenge, Skip, Log (Log is Enterprise-only). No content-rewrite or serve-alternate action exists. | `cf.bot_management.score`, `cf.bot_management.verified_bot`, and general Rules-language expressions (ASN, UA, etc. — exact field syntax not itself confirmed this pass beyond the bot-management fields) | Custom rules available from Pro up; bot-management fields effectively Enterprise (see plan note) | `developers.cloudflare.com/waf/custom-rules/` |
| **Transform Rules** | **No — explicitly out of scope.** "Transform Rules can modify URI path, query string, and HTTP headers of requests and responses." No body-modification capability stated anywhere in the doc. | URL, headers only | Available lower tiers | `developers.cloudflare.com/rules/transform/` |
| **AI Crawl Control** | No. It is visibility + access control: "Set allow or block rules for individual crawlers," monitor activity, track robots.txt compliance. No content-differentiation feature described. | Named AI crawler identity (OpenAI, Anthropic, etc. — Cloudflare's own crawler classification, built on the same verified-bot machinery) | "Zero-config on all Cloudflare plans" (product page's own claim) | `developers.cloudflare.com/ai-crawl-control/`, page stamped "Last Updated: August 14, 2026" |
| **Pay per crawl** | N/A — a payment gate (HTTP 402), not a content-branching tool. Requires Web Bot Auth (Ed25519 key pairs, HTTP Message Signatures). | Cryptographic crawler self-identification (`signature-agent` etc.), opt-in by the crawler operator | **Still private beta** as of the 2026-08-14 page stamp — 14+ months after the 2025-07-01 launch pass 2 found. Not a usable prototype dependency. | same page |

**The one primitive that matters for this project's sub-question 2 is Workers.** Everything else in Cloudflare's stack either can't touch the response body (WAF, Transform Rules) or isn't a content-branching tool at all (AI Crawl Control, Pay per crawl).

## Bot-management field names (the signal a Worker or WAF rule reads)

From `developers.cloudflare.com/bots/reference/bot-management-variables/`:

- `cf.bot_management.score` — integer 1-99, Cloudflare's certainty the request is automated (1 = certain bot, 99 = certain human).
- `cf.bot_management.verified_bot` — boolean, true if the request comes from Cloudflare's allowlist of "good, automated bots (such as Google Search Engine and Pingdom)."
- `cf.bot_management.static_resource`, `.corporate_proxy`, `.signed_agent` (Web Bot Auth), `.ja3_hash`, `.ja4` (TLS fingerprint), `.detection_ids`, `.tags`.
- Workers access path: `request.cf.botManagement.score` (JS object, not the WAF-expression dotted form).

**Plan-tier catch:** per-request `cf.bot_management.score`/`verified_bot` in a rule is described on Cloudflare's bot-solutions overview as an **Enterprise-tier** capability ("Bot Management for Enterprise... per-request bot scores, custom rules, per-endpoint handling"). The free tier's "Bot Fight Mode" is a domain-wide challenge toggle, not a scored signal a Worker script can branch on. **Open, not reconciled this pass:** AI Crawl Control claims "zero-config on all plans" and does classify named AI crawlers, but whether a *free-tier* Worker script can read that same crawler-identity signal (as opposed to only the paid Bot Management score) was not confirmed — `unknown — checked developers.cloudflare.com 2026-09-17`. The safe, always-available Worker path that needs no Enterprise plan is to match request IP against the vendor-published JSON range files directly inside the Worker script — no Cloudflare bot-management field required at all. That is the primitive the prototype should use.

## Cloudflare's own terms — no explicit customer-facing cloaking clause found

`cloudflare.com/website-terms/` (effective 2025-08-01) bars using bots to scrape *Cloudflare's own site* for ML training — that is Cloudflare protecting itself, not a rule governing what a Cloudflare customer may configure on their own zone. No clause was found addressing whether a customer serving different content to a verified AI crawler vs a human visitor on their own domain violates Cloudflare's terms. `unknown — checked cloudflare.com 2026-09-17` — this is a real gap: Cloudflare ships the primitive (Workers + verified-bot detection) and says nothing about whether using it for differential serving is an acceptable use of the product.

## Alternative — Fastly

| Primitive | Capability | Gate |
|---|---|---|
| VCL (`vcl_recv` etc.) | Can condition on request properties (UA, IP, geo) in principle — general VCL capability, confirmed by Fastly's own subroutine reference, but no literal code example or bot-specific field was found this pass, and the dedicated "detecting bots" VCL guide page 404'd | Included at base Fastly tier (not separately confirmed) |
| **Bot Management** (product) | AI-crawler-aware: "identifies automated traffic ranging from AI crawlers and fetchers, to headless browsers and malicious bots." Actions: Block, Allow, Rate-limit, Dynamic Challenges, Deception, plus an unspecified "AI monetization capabilities" (Fastly's apparent answer to pay-per-crawl, not detailed) | **Sales-gated, no public pricing** — "request a demo or contact sales." No named distinction of OpenAI/Anthropic/Perplexity specifically as "good" bots in what was fetched, unlike Cloudflare's named verified-bot allowlist. |

**Read:** Fastly's AI-crawler awareness lives in an enterprise product behind a sales call; Cloudflare's equivalent (AI Crawl Control) is free and self-serve. For a two-person team with no capital (per `../../../../docs/findings/cross-read.md`'s team-constraint scorecard), Cloudflare is the only realistic starting CDN. Vercel, Netlify and Caddy were named as alternatives in the brief but not evaluated this pass — time budget went to Cloudflare (primary) and one alternative (Fastly) as instructed.

## What this means for the prototype

The smallest thing that runs: a Worker script on a Cloudflare free-tier zone that (a) fetches and caches the published IP-range JSON for OpenAI/Anthropic/Perplexity/Google/CommonCrawl, (b) checks the incoming request's IP against those ranges (CIDR match, no Cloudflare Enterprise bot-score needed), and (c) serves variant response body accordingly. This needs no paid Cloudflare tier and no Pay-per-crawl/Web-Bot-Auth machinery. It does need a domain — none exists on this machine (`raw/local-infra-check.txt`) — and a Cloudflare account, neither of which currently exists for this project.

## Caveats

- WAF custom-rule field syntax beyond the bot-management dotted names (e.g. matching ASN or UA directly in a WAF expression) was not confirmed with an example this pass — `unknown — checked developers.cloudflare.com 2026-09-17`.
- The Workers "Conditional response" example's actual script body was not retrieved (WebFetch returned only the example's title/description from the index page) — next pull.
- Fastly's VCL bot-detection guide 404'd; the general VCL capability described here is inferred from the subroutine reference page and Fastly's general documentation model, not from a worked example — flagged as thinner evidence than the Cloudflare side.
- Vercel Edge Middleware, Netlify Edge Functions and Caddy were not evaluated — the brief asked for Cloudflare plus **one** alternative, and Fastly was chosen because pass 2 had already touched Fastly's crawler-traffic reporting.
