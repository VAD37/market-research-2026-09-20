### Source: what can actually be said about unit economics under an unpublished allowance

- Pull date: 2026-09-17
- Method: direct `curl` + WebFetch of Anthropic's own contract and help-centre pages. All quotes below are first-hand by wave 2b.
- Label: company-stated (Anthropic's own published contract and documentation).

---

## 1. The COGS is contractually unilateral — Anthropic's own Consumer Terms

Source: https://www.anthropic.com/legal/consumer-terms — fetched 2026-09-17, HTTP 200. Page header: "Consumer Terms of Service **Effective October 8, 2025**".

Verbatim, §"Changes to the Services":

> "We may sometimes add or remove features, **increase or decrease capacity limits**, offer new Services, or stop offering certain Services. Unless we specifically agree otherwise in a separate agreement with you, **we reserve the right to modify, suspend, or discontinue the Services or your access to the Services, in whole or in part, at any time without notice to you.**"

Verbatim, §"Use of our Services" (prohibited uses), two clauses that bear on any product built on a consumer subscription:

> "To develop any products or services that **compete with our Services**, including to develop or train any artificial intelligence or machine learning algorithms or models **or resell the Services**."

> "**Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, to access the Services through automated or non-human means, whether through a bot, script, or otherwise.**"

Searched the full extracted text for "usage limits" and "rate limit" as standalone clause terms: **no hits**. The contract governs capacity limits without ever stating one.

## 2. Anthropic announced a change to `claude -p` billing, scheduled it, and paused it the day before

Source: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan — fetched 2026-09-17, HTTP 200. Article dated "June 16, 2026". Verbatim, at the top of the page:

> "**Update June 15:** We're **pausing** the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage **still draw from your subscription's usage limits**. The previously announced monthly credit, which would have been available to eligible claimants in connection with these changes, **isn't available**. We're working to update the plan to better support how users build with Claude subscriptions. When we have an update, we'll share it before anything takes effect."

> "The content below reflects the page before June 15. It's preserved for reference but is no longer taking effect on June 15."

The paused plan, preserved verbatim on the same page:

> "Starting **June 15, 2026**, Claude Agent SDK and `claude -p` usage **no longer counts toward your Claude plan's usage limits**. Your subscription usage limits stay the same and stay reserved for interactive use of Claude Code, Claude Cowork, and Claude."

> "Available on Pro, Max, Team, and Enterprise plans starting on June 15, 2026. Claude Platform accounts using an API key don't receive a credit."

Monthly Agent SDK credit table as published, then withdrawn:

| Plan | Monthly credit |
|---|---|
| Pro | $20 |
| Max 5x | $100 |
| Max 20x | $200 |
| Team (Standard seats) | $20 |
| Team (Premium seats) | $100 |
| Enterprise (usage-based) | $20 |
| Enterprise (seat-based Premium seats) | $200 |

What the withdrawn credit would have covered, verbatim:

> "Claude Agent SDK usage in your own projects (Python or TypeScript) / The `claude -p` command in Claude Code (non-interactive mode) / The Claude Code GitHub Actions integration / **Third-party apps that authenticate with your Claude subscription through the Agent SDK**"

> "**Per-user, not pooled.** Credits belong to individual accounts. They can't be shared or pooled across teammates."
> "**Drains first.** Agent SDK usage draws from your monthly credit before any other source."
> "**Past the credit, usage moves to usage credits.** When your monthly credit runs out, additional Agent SDK usage flows to usage credits at standard API rates—but only if you've enabled usage credits. If usage credits aren't enabled, Agent SDK requests stop until your credit refresh[es]."

**Two findings from this page, both load-bearing:**

1. `claude -p` — the exact substrate candidates B, D, E, G and H run on — had its billing model rewritten, published, scheduled, and withdrawn inside a single announcement cycle, three months before this pull. The architectural risk in attack line 6 is not hypothetical; it materialised on 2026-06-15 and the page says another change is coming ("We're working to update the plan... When we have an update, we'll share it before anything takes effect").
2. The withdrawn plan explicitly contemplated "**Third-party apps that authenticate with your Claude subscription through the Agent SDK**" as a supported, credited category. That cuts against the strictest reading of the SDK quickstart's "Anthropic does not allow third party developers to offer claude.ai login" line that `docs/plan/idea-set.md` constraint 3 rests on — but the plan containing it was withdrawn, so it establishes nothing currently in force. Status: `unresolved — checked support.claude.com and anthropic.com/legal 2026-09-17`.

## 3. There IS a published-price overflow rail — usage credits

Source: https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans — fetched 2026-09-17, HTTP 200. Verbatim:

> "Usage credits allow individuals subscribed to paid Claude plans (**Pro, Max 5x, and Max 20x**) to continue using Claude seamlessly after reaching their included usage limits. Instead of being blocked when you hit your session limits, you can **switch to consumption-based pricing at standard API rates** and continue your work without interruption."

> "Your subsequent usage will be billed at standard API pricing rates. Your session limits reset every five hours as usual."

> "**Usage credit pricing** — Usage credits are billed at standard API rates; see our pricing page for details. **Price and plans are subject to change at Anthropic's discretion.**"

> "**Note:** There is a daily redemption limit of **$2000**."

Controls available, verbatim: "**Monthly spending cap:** Set a maximum amount you're willing to spend on usage credits each month. **Auto-reload settings:** Automatically add funds when your balance drops below a threshold. **Usage alerts:** Receive notifications when approaching your spend limits."

Coverage: "Usage credits apply to both Claude conversations and Claude Code terminal usage." (relay from the WebFetch summary of the same page; the verbatim sentence was not isolated in the raw extraction.)

## 4. What is still unpublished

Confirmed again, independently of wave 1c: Anthropic publishes no absolute current (2026-09) token, message or hour figure for the 5-hour or weekly window.

- https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code — fetched 2026-09-17. Contains no numeric Pro/Max window figure. Verbatim: "How you signed in determines how usage is metered." Enterprise gets "a pool of usage included in your organization's plan, reset on a rolling window"; API key users get "pay-as-you-go, billed per token."
- https://support.claude.com/en/articles/8324991-about-claude-s-max-plan-usage — **HTTP 404**, page gone as of 2026-09-17.
- Help-centre index search surfaced current articles ("What is the Max plan?", "How do usage and length limits work?", "Usage limit best practices"); the summarised content gives only relative multipliers — Max 5x "five times more usage per session than the Pro plan", Max 20x "20 times more" — and the disclaimer that the specific number "depends on various factors including message length, file attachments, model choice, and other features you use." Relay from search summary, not a verbatim page fetch.

This leaves wave 1c's finding intact: the only absolute figures are 2025-08-28 company-stated hours-per-week to TechCrunch, updated since only by percentage deltas (+50% temporary boost 2026-05-13 to ~2026-09-13; "permanent +25%" over the 2025 baseline effective 2026-09-14; Anthropic's own clarification that this nets to **-17%** versus the boosted level).
