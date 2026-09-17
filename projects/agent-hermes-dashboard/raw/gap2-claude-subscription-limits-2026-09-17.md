# Raw pull — Claude Pro/Max subscription allowance for Claude Code, as of 2026-09-17

Pull date: 2026-09-17. Method: WebFetch on Anthropic's own pricing page (redirect followed), plus WebSearch (quota was NOT exhausted despite wave 2b's flag that it hit 200/200 on 2026-09-16 — it worked without error on 2026-09-17) to locate press/community coverage, then WebFetch direct on the highest-quality primary and secondary pages found. Purpose: close wave 2a's gap #8 (idea-set.md attack list) — the subscription allowance size that unit economics for candidates B/D/E/G depend on.

## What Anthropic publishes on its own current docs/pricing pages — confirmed absence

- `claude.com/pricing` (redirected from `anthropic.com/pricing`, fetched 2026-09-17): Pro $17/mo (annual, $200 billed upfront) or $20/mo billed monthly; Max 5x from $100/mo; Max 20x from $100/mo [sic — page did not differentiate 5x/20x price in fetched content, both showed "$100"]. Verbatim: "Claude Code...is included in all paid plans. It shares the same usage limits as the rest of your plan, so your work in the terminal and your chats draw from one pool." Only comparative figure given: "Pro gives you at least 5x more usage per 5-hour session than Free. Max gives you 5x or 20x more usage per 5-hour session than Pro." No token, message, or hour count for Claude Code specifically.
- Consistent with wave 1 explore's own finding in `../docs/explore/claude-code-substrate.md`: "no primary-doc figure found for the exact size of the 5-hour/weekly allowance in tokens or dollars for a given Pro/Max tier — that number lives behind sign-in, not in public docs."
- **Anthropic publishes no exact current (2026-09) token/message/hour number for the 5-hour or weekly window on any public docs or pricing page checked 2026-09-17.** That absence is itself the answer to the "what does Anthropic publish" half of this gap.

## The one company-stated absolute figure that exists — company-stated to press, 2025-07-28, not on current docs

Source: TechCrunch, "Anthropic unveils new rate limits to curb Claude Code power users," 2025-07-28, fetched 2026-09-17. Verbatim per fetch: "Anthropic tells TechCrunch that most Pro users can expect..." — company-stated, given directly to the publication, not TechCrunch's own estimate.

- Effective date of these limits: 2025-08-28.
- **Pro ($20/mo)**: "40 to 80 hours of Sonnet 4 through Claude Code within their weekly rate limits."
- **Max $100/mo tier**: "140 to 280 hours of Sonnet 4 and 15 to 35 hours of Opus 4" per week.
- **Max $200/mo tier**: "240 to 480 hours of Sonnet 4 and 24 to 40 hours of Opus 4" per week.
- Anthropic's own caveat (per TechCrunch): usage varies by codebase size and other factors — these are ranges, not fixed numbers, even as company-stated figures.

This is a 2025-07/08 baseline. It has since been modified twice (below) by percentage, not by a restated absolute-hours figure.

## Changes since the 2025 baseline — company-stated percentages, third-party-relayed

1. **2026-05-06** (per bestagent.dev, third-party-reported, citing Anthropic): Anthropic "doubled Claude Code's five-hour rate limits" for Pro/Max/Team/seat-based Enterprise, and removed a "peak hours limit reduction" that had applied to Pro/Max.
2. **2026-05-13 through 2026-08-31/09-13** (dates vary slightly by source — some say boost extended through 08-19, others 08-31, expiring 09-13): a **temporary 50% boost** to weekly limits ran across Pro/Max/Team/seat-based Enterprise.
3. **2026-08-29 announcement, effective 2026-09-14**: Anthropic's own @ClaudeDevs account posted (quoted verbatim via Bleeping Computer, 2026-09-17 fetch): "Starting September 14, we're permanently raising standard weekly limits in Claude Code by 25% for Pro, Max, Team, and seat-based Enterprise plans." This 25% is measured against the **pre-boost 2025 standard baseline**, not against the boosted level users had been experiencing since May.
4. **Net effect, Anthropic's own admitted clarification** (per Bleeping Computer, notebookcheck.net, and others, all 2026-08/09 dated, all citing the same Anthropic post/clarification): because the 50% temporary boost expires 2026-09-13 — one day before the new "permanent 25% increase" takes effect 2026-09-14 — active users who had been running on the boosted level face a **net 17% reduction in total weekly capacity** versus what they had immediately before the change. Anthropic's clarification (deleted-and-reposted per Bleeping Computer) explicitly states: "Compared to today, this works out to a 17% reduction in weekly limits on Claude Code."

Sources for the 2026 change, all fetched/searched 2026-09-17, all third-party press relaying an Anthropic post (the original @ClaudeDevs X/Twitter post itself, https://x.com/ClaudeDevs/status/2093742321473065266 per Bleeping Computer's citation, was not independently re-fetched — X is not reliably fetchable by this tool):
- https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/ (fetched directly)
- https://www.notebookcheck.net/Anthropic-announces-a-25-increase-to-Claude-Code-limits-but-there-s-a-17-catch.1382735.0.html (found via search, not fetched)
- https://bestagent.dev/claude-code-usage-limits/ (fetched directly)

## No updated absolute-hours figure for the 2026-09-14 level

No source found (search + direct fetch) gives an updated hours-per-week number for the post-2026-09-14 level, comparable to the 2025-07-28 TechCrunch figures. Every 2026 source discusses the change only in percentage terms (25% up from pre-boost baseline, 17% down from the boosted level). `unknown — checked claude.com/pricing, TechCrunch, Bleeping Computer, notebookcheck.net, bestagent.dev 2026-09-17 — no absolute hours/tokens figure published for the current level`.

## Bottom line for unit economics (candidates B/D/E/G in idea-set.md)

If the 2025-07-28 company-stated Pro figure (40-80 hrs Sonnet 4/week) is used as a rough floor and the 2026-09-14 change is read as roughly restoring that same order of magnitude (25% above the 2025 baseline, per Anthropic's own framing), a Pro-tier seat running unattended work for paying customers has on the order of **~50-100 hours/week of Sonnet-class usage** to work with — a directional estimate constructed from two company-stated data points, not a directly published current number. Flag explicitly: this arithmetic is this pull's own construction, not an Anthropic-stated figure for 2026-09, and should be labeled as such wherever it's used downstream.
