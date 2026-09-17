# ai-ads-injection

Source: `MegaPlan.md` §1. Research behind it: `../../docs/markets/ai-search-ads.md`, `../../docs/findings/injection-feasibility.md`, `../../docs/raw/injection-feasibility-pulls.md`, `../../docs/competitors/ai-search-ads-roster.md`.

## The question

Can a site you control detect an AI chatbot's retrieval fetch and serve it different text than a human gets — and does that changed text move the model's answer?

Three sub-questions, in order:

1. **Detection.** Are AI-assistant fetches identifiable from the origin? User-agent, published IP ranges, rDNS, ASN, TLS fingerprint, request shape. Which engines retrieve live vs serve from index.
2. **Delivery.** Can edge config (Cloudflare Workers / rules, or equivalent) branch on that signal and serve variant content? What does the CDN actually expose.
3. **Influence.** Does added product-placement text in a retrieved page shift the model's answer — without reading as an injection attack to the model. Nudge, not steer.

## Boundary — hard

Authorized testing on infrastructure the tester owns. Own domain, own pages, own content. Measure what public assistants do when they fetch it. No third-party site targeting, no payloads aimed at anyone else's pipeline, no evasion of anyone's abuse detection. Sub-question 3 is measured by asking a public assistant about *your own* page and reading the answer.

The policy read — ToS of each engine, what "cloaking" means to each, what ad-disclosure regimes require — is part of the deliverable, not an afterthought. `../../docs/raw/tos-browser-pulls.md` has a start.

## What "done" looks like

- `docs/explore/` — terrain: what is published on AI-crawler identification, who sells GEO / AI-visibility today, what they measure.
- `docs/review/` — this idea checked against `../../docs/findings/`. Pass 2 already ran an injection-feasibility agent; say what it settled and what it left open.
- `raw/` — measured output. Server logs of real assistant fetches, header dumps, DNS/ASN lookups, assistant answer text before and after a page change.
- `prototype/` — smallest thing that runs end to end: a page, an edge rule, a log reader that says which fetches were assistants. If no real domain is available, build it to run locally and say so.
- `docs/outcome/` — does this work, what killed it or what carried, and the legal/policy ceiling on it.

## Known traps

- Most "AI crawler" lists are vendor-reported. Label them, verify against published ranges where the engine publishes them.
- Live retrieval, training crawl, and index serve are three different things. Do not merge them.
- Answer variation between identical prompts is large. An A/B on one prompt proves nothing — repeat and count.
