# Who sells this — GEO / AI-search-visibility vendor landscape, checked against 2026-09-16 roster

2026-09-17. Baseline: `../../../../docs/competitors/ai-search-ads-roster.md` (pass 1, 2026-09-16) and `../../../../docs/markets/ai-search-ads.md`. One day of drift possible; this file adds only what changed or was newly checked, per instruction — it does not re-derive the roster.

## Spot-check: has anything moved in 24 hours?

Re-fetched Profound's own pricing page (`tryprofound.com/pricing`, 2026-09-17): **Trial (free, 10 prompts, ChatGPT only) and Enterprise (custom, demo required) — unchanged from the roster's "verified 2026-09-16" line.** No self-serve tier appeared. Peec AI (`peec.ai/pricing`) and AthenaHQ (`athenahq.ai/pricing`) both returned redirect codes (308/307) to the fetch tool and were not re-read in full — same "JS-rendered, price not retrievable" state the roster already flags for Peec AI; AthenaHQ's roster entry already carries a confirmed price (`Starter $295`) so this is not a new gap.

**Read: the roster is current.** A single day is too short a window for funding, pricing or headcount to move at this market's pace (compare: Profound's own two 2026 rounds were four months apart, Peec AI's seed-to-Series-A was four months). No correction is warranted to the existing roster from this check.

## What this explore pass adds that the roster does not cover: the injection-audit gap, re-confirmed

The roster and market file both name the same gap pass 1 and pass 3 independently found (`../../../../docs/findings/cross-read.md`): **no vendor sells an AI-search-answer integrity/injection audit.** This pass's own research supports that gap being real rather than an artifact of thin search:

- Cloudflare's AI Crawl Control (`docs/explore/edge-controls.md`) — the closest thing a platform vendor ships to "watch what AI crawlers do to your content" — is monitoring and allow/block, not answer-integrity testing. It tells you a crawler *visited*, not whether the *answer* it produced was manipulated or manipulable.
- Fastly's Bot Management is the same shape: detection and mitigation of automated traffic, not answer-content audit.
- None of the GEO/visibility vendors in the roster (Profound, Peec AI, AthenaHQ, Otterly AI, Ahrefs Brand Radar, Semrush, Goodie AI, Searchable) advertise adversarial testing of their own tracked answers — they measure *whether* a brand appears, not whether the appearance was bought via injected/undisclosed content on a third-party page.
- None of the AI-security vendors (Lakera→Check Point, HiddenLayer, TollBit, Garak/Promptfoo/PyRIT/DeepTeam) are search-answer-specific; TollBit gates crawler *access*, not answer *integrity*, same distinction as Cloudflare's product.

## What "sells" adjacent to this specific idea, not yet on the roster

Two categories touch this project's actual mechanism (differential serving to a detected AI crawler) more closely than pure GEO tracking does, and neither is on the existing roster because neither is a GEO vendor:

- **Crawler-access monetization**: Cloudflare Pay per crawl (still private beta, 14+ months on), TollBit (already rostered, "3,000+ sites incl. TIME, Fast Company," content-monetization framing), and Fastly's unnamed "AI monetization capabilities" (found this pass, no further detail available — sales-gated). These sell *letting a crawler in*, priced per-crawl — not differential content.
- **Bot-detection-as-a-platform-feature**: Cloudflare's free-tier AI Crawl Control and Fastly's enterprise Bot Management are the infrastructure this idea's detection half would sit on top of, not a competing product for the idea itself — they don't serve variant content, they only see and gate the crawler.

Neither category is a competitor to a differential-serving or answer-influence product; both are potential *dependencies* (see `docs/explore/edge-controls.md`) or *substitutes* for the narrower "know who's crawling me" half of the idea, already commoditized for free (pass 2's finding, unchanged: "The monitoring layer for crawler identity is already free and bundled. That prices the floor for anything built here.").

## Caveats

- This was a spot-check, not a re-run of pass 1's full vendor sweep. Peec AI and AthenaHQ pricing pages were not fully re-read; Searchable, Writesonic, SE Ranking, Goodie AI, Rankscale were not touched at all this pass.
- No new vendor name surfaced this pass. Absence of a new entrant in one day of light checking is not proof none exists — WebSearch (which would be the tool for a discovery sweep) returned "unavailable" when tried once today for an unrelated query.
- The "who sells this" question the brief poses is answered the same way pass 1 and pass 3 already answered it: nobody sells the AI-answer-integrity audit specifically. This pass did not find a reason to revise that conclusion, only additional supporting detail from the edge-control and policy research done in parallel.
