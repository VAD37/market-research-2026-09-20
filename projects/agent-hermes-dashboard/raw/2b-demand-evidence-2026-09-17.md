### Source: direct-demand hunt for candidate B and candidate H

- Pull date: 2026-09-17
- Method: delegated breadth leg across Hacker News (hn.algolia.com API), GitHub issue search, freelance marketplaces, IndieHackers, and general web. Wave 2b **re-verified the volume claims first-hand** using the authenticated `gh` CLI (`gh api -X GET search/issues`), which avoids the unauthenticated 60-req/hr cap that truncated the delegated leg.
- Bar applied: demand evidence = a real person on a dated public page asking for this, complaining about the problem, paying for a manual version, or selling it as a service. Vendor marketing and market-size content excluded.

---

## PART 1 — FIRST-HAND VERIFICATION BY WAVE 2b

### GitHub issue volume on `anthropics/claude-code`, queried via `gh api` 2026-09-17

Title-scoped counts (tighter than the delegated leg's full-text counts, which mix body matches):

| Query | `total_count` |
|---|---|
| `"usage limit" in:title` | **828** |
| `"rate limit" in:title` | 733 |
| `"cost" in:title` | 355 |
| `"weekly limit" in:title` | 234 |
| `"budget" in:title` | 153 |

Full-text (untitled-scoped) for comparison: `usage limit` 5,207; `cost per task` 1,673; `budget cap` 634. **Control query**: `competitor pricing` on the same repo returns 42, which shows GitHub's full-text search is loose and these larger numbers are directional volume, not curated counts. The title-scoped numbers are the defensible ones.

Eight most recent `"usage limit" in:title` issues, verbatim titles and dates, fetched 2026-09-17:

```
2026-09-16 #94694 "Approaching weekly usage limit" banner fires at 54% weekly usage
2026-09-16 #94686 Feature request: historical usage-limit exhaustion count + timeline for Max/Pro accounts
2026-09-15 #94592 [Feature Request] Usage limits and rate limiting communication
2026-09-15 #94586 Weekly usage limit ~30% consumed by Tuesday on a single MCP-heavy session — limits too tight fo…
2026-09-15 #94424 Function hooks: an event when session usage or a rate-limit window changes, so trackers do not …
2026-09-14 #94222 [FEATURE] Mark a subagent killed by a usage limit as resumable, and keep it listed after a ses…
2026-09-14 #94211 [Bug] Disproportionate session usage consumption compared to weekly usage limits
2026-09-13 #93984 [Bug] Session Usage Limit Reached Prematurely with Claude Sonnet Medium Thinking
```

Eight in four days. #94424 is a request for the exact platform primitive candidate H would consume, and its wording ("so trackers do not …") presupposes that third-party trackers already exist.

### Tool star counts, verified via `gh api` 2026-09-17

| Repo | Stars | Last push |
|---|---|---|
| ccusage/ccusage | **18,591** | 2026-09-17 |
| puq-ai/claude-meter | 48 | 2026-09-11 |
| saadnvd1/hydra | 18 | 2026-04-21 |
| fabioconcina/claumon | 16 | 2026-07-30 |

Note: the delegated leg cited `ryoppippi/ccusage`; that path resolves to `ccusage/ccusage` (18,591★), the same repo verified in `2b-governor-already-solved-2026-09-17.md`.

---

## PART 2 — RELAY FROM THE DELEGATED LEG

### Candidate H — verdict STRONG

Verbatim issue quotes, dated, relayed (URLs given; bodies not re-fetched by wave 2b):

| URL | Date | Verbatim |
|---|---|---|
| github.com/anthropics/claude-code/issues/94770 | 2026-09-16 | "the orchestrating model has no budget awareness and defaults every subagent to the parent's (premium) model. On a document-synthesis task this burned ~70% of a weekly Fable 5.1 allowance, most of it wasted on subagents that were killed mid-flight by the rate limit." |
| github.com/anthropics/claude-code/issues/91220 | 2026-09-01 | "An orchestrating session kept a subagent working... between the operator's last instruction (23:00) and their next message (07:41)... woke to an exhausted weekly limit, three days from reset. One subagent, resumed 8 times, accounted for 50.7% of that week's entire consumption." |
| github.com/anthropics/claude-code/issues/89845 | 2026-08-26 | "Subagent cost is invisible, unattributable and unstoppable: background-task chips open uncapped sessions... consumed a weekly allowance in ninety minutes with no signal available to the operator until after the fact." |
| github.com/anthropics/claude-code/issues/92800 | 2026-09-08 | "Subagents aren't respecting my subscription budget limit and keep consuming paid credits without automatically stopping... We need strict credit caps and auto-stop safeguards for subagent workflows." |
| github.com/anthropics/claude-code/issues/93911 | 2026-09-12 | "The weekly limit ran out on work I did not ask for, and I could not continue my project until the limit reset. My development stopped." |
| github.com/anthropics/claude-code/issues/94289 | 2026-09-14 | "Claude Code shows how much budget is left... but it gives no visibility into what is burning that budget right now, or how fast." |
| github.com/anthropics/claude-code/issues/33323 | 2026-03-11 | "There's no way to queue up multiple tasks and have them execute sequentially... Prior Issues (all auto-closed by stale bot, not by team decision): #535 — 'The ability to queue up messages' (27+ upvotes, auto-closed)" |
| github.com/anthropics/claude-code/issues/92237 | 2026-09-04 | "this is illegal! im paying for this service! give me access to my services now!" |

Independent builds addressing the same problem, from Show HN (relay): Hydra "Never stop coding when your AI CLI hits a rate limit" (2026-04-21, 9 pts); Headroom "Claude Code usage limits, live in the macOS menu bar" (2026-06-11, 2 pts); Claude Meter (2026-02-10, 9 pts); Claumon "forecasting Claude Code usage limits with a Gamma process" (2026-06-11, 2 pts). HN front-page story "Claude Code weekly rate limits", 2025-07-28, **609 points**.

### Candidate B — verdict WEAK

| Channel | URL | Date | Verbatim | What it proves |
|---|---|---|---|---|
| Freelancer.com posted job | freelancer.com/projects/web-scraping/price-scraping-competitive-pricing | "over 1 year ago" as of 2026-09-17 → before ~2025-09 | "Are you an expert in web scraping and competitive price tracking? ... monitor and maintain the most competitive pricing for our 1,000+ wines... Monitor pricing trends and alert us when competitors change their pricing." Budget **$2-8 AUD/hour** | Someone paying for the manual version — but the buyer is an e-commerce wine retailer, not a B2B SaaS founder, and the budget is $2-8/hr |
| IndieHackers post | indiehackers.com/post/does-anyone-else-waste-hours-every-monday-checking-competitor-websites-842cacf3b5 | 2026-05-24 (sbakshi) | "Every Monday I'd open like 5 tabs. Competitor pricing page. Their blog. Job postings... Takes 2-3 hours. And I still miss stuff." Author adds: "Haven't written a single line of code yet. Wanted to talk to real people first." | Organic pain post — but from a founder validating a product idea, i.e. a would-be seller, not a buyer |
| IndieHackers comment, same thread | same | 2026-05-26 (hilgard) | "yeah this is real, but for me the bigger pain isn't the checking, it's that 90% of the changes don't matter." | One independent confirmation, with a refinement that undercuts the detect-and-report shape |
| Upwork posted job | upwork.com/freelance-jobs/apply/n8n-Developer-Needed-for-Competitor-Price-Monitoring-Automation_~022087532726039673733/ | unknown — page HTTP 403 | Title only: "n8n Developer Needed for AI Competitor Price Monitoring Automation" | A second real posting exists; budget, date and body unverifiable |

**Two "Ask HN" threads that look like demand and are not**, both excluded by the delegated leg after reading the bodies:

- news.ycombinator.com/item?id=47661051, 2026-04-06, "Ask HN: How do you track competitor moves without an enterprise budget?" — body is "I've been building Peerscope — watches competitor sites for pricing changes... $29/month. Waitlist at...". Vendor fishing. **0 comments.**
- news.ycombinator.com/item?id=46865447, 2026-02-03, "Ask HN: What's your competitive intelligence workflow as a small team?" — "I've been researching how founders track competitors... Wondering if this is a real pain point or just something people complain about but don't actually prioritize." **0 comments.**

**The supply-side pattern, relayed**: Show HN launches of this exact tool at least nine times across six years — pricemon.io (2026-03-07, 1 pt, 0 comments); spydelta.com (2025-03-24, 2 pts); parano.ai (2026-02-02, 1 pt); pagedeltas.com competitor-pricing-monitoring (2026-07-30, 1 pt, 0 comments); pingchange.com (2026-08-20, 2 pts); competitortracker.io (2026-08-07, 0 pts); rivalhunt.co (2023-09-07, two posts); Brandchirps (2020-01-20, 2020-08-29). Essentially none drew upvotes or comments.

---

## PART 3 — CHANNEL THAT FAILED, AND WHY IT MATTERS

**Reddit could not be reached at all, for either shape.** `WebFetch` refused both `www.reddit.com` and `old.reddit.com`; direct `curl` on `old.reddit.com/search.json` returned a bot-gated HTML shell instead of JSON; `WebSearch` with `site:reddit.com` never surfaced an actual reddit.com URL. This is the second independent wave to fail on Reddit (see `2b-price-tracker-longtail-2026-09-17.md` Part 3).

This matters asymmetrically. r/SaaS, r/Entrepreneur and r/microsaas are exactly where candidate B's persona would post, and the count-level data that would move candidate B's verdict from WEAK to STRONG or to NONE lives there. **Candidate B's demand verdict is therefore WEAK-on-an-incomplete-search, not a clean negative.**

For candidate H the Reddit gap is less damaging, because the GitHub-issue channel is native to its persona and was reached at full volume. Secondary citations (TechRadar, The Register) reference large Reddit threads by name — "Claude Code Limits Were Silently Reduced and It's MUCH Worse" (360+ comments in 6 days) and "20x max usage gone in 19 minutes" (330+ comments in 24 hours) — but neither was opened, so both are relayed existence claims only.

Fiverr gig listings could not be browsed directly. Freelance marketplaces were not searched for candidate H at all; no claim is made either way there.
