# Idea set — eight shapes, one pick, one fallback

Wave 2a, 2026-09-17. Inputs: `../explore/` (5 files, each backed by `../../raw/`), and read-only `../../../../docs/{markets,competitors,findings,customers,method}/`. Wave 2b attacks this file; wave 2c designs whatever survives. Everything below is compiled, not remembered — except the section fenced as **DAYDREAM**, which is speculation and labelled as such.

## The frame these candidates are picked inside

Four constraints from `../../../../docs/method/scope.md`, all confirmed by the user 2026-09-16, none negotiable here: two people, one technical builder; Ho Chi Minh City; **no US market access**; no funding; remote-first, no field sales motion.

Three facts from wave 1 that decide which shapes are even legal:

1. **Per-task cost and duration are free.** `Stop`/`SubagentStop` hook payloads carry `cost: {input_tokens, output_tokens}` and `duration_ms`; `claude -p --output-format json` returns `total_cost_usd`. Source: `../explore/task-telemetry.md` → `../../raw/claude-code-docs-2026-09-17.md` L130, L38-39.
2. **Recurrence detection and fact-staleness are not free.** Confirmed absent from the platform, not merely undocumented. `../explore/task-telemetry.md`. That absence is the only thing in this project that has to be invented rather than wired up.
3. **The OAuth fork.** Non-bare `claude -p` uses subscription login by default; `--bare` and the Agent SDK need an API key; Anthropic's SDK quickstart states verbatim *"Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products"*. `../explore/claude-code-substrate.md` → `../../raw/claude-code-docs-2026-09-17.md` L19-21, L33-34.

Constraint 3 is not resolved here, per instruction. It is carried as a filter: **a candidate survives the single-tenant constraint if no customer ever needs their own claude.ai login.** Two legal shapes exist — the team runs everything on its own subscription and ships the *output* (single-tenant, service-shaped), or the customer supplies an API key (multi-tenant, but then the customer is technical and pays compute). A candidate that needs a non-technical customer to log into Claude is dead on arrival.

## Candidate set

| ID | Shape | Who pays | Build, 1 person | What kills it | Survives single-tenant? |
|---|---|---|---|---|---|
| **A** | Framework-agnostic fleet supervision dashboard | AI-agent-manager persona, SMB/mid-market | 8-16 weeks + ongoing infra | Frontier vendors already ship consoles | Only as bring-your-own-API-key |
| **B** | Single-job blind-spot agent: competitor-price watch, repricing memo | Sub-$1M-ARR B2B SaaS founder | 2-4 weeks | Cheap incumbent trackers; advice nobody trusts | **Yes** — output ships, not login |
| **C** | Recurrence-to-tool graduation engine, standalone | Developers; hosted tier or sponsorship | 3-5 weeks | Braintrust Patterns; Anthropic ships it | **Yes** — local, no auth at all |
| **D** | Mocking morning report as the entire product | Prosumer/solo operator, low ticket | 1-2 weeks | Novelty churn; zero sourced demand | Yes — team's key, per-seat price |
| **E** | Agent-ops done-for-you, run as a service | HCMC/SEA SMB clients, monthly retainer | 1-2 weeks tooling, then labour | Doesn't scale; needs proximity and time | Yes — team operates the account |
| **F** | Provenance and staleness layer for agent-authored facts | Developers; plugin/MCP, paid tier | 3-4 weeks | It is a feature, not a product | **Yes** — local |
| **G** | Narrow agent shipped into a marketplace (Shopify) | Merchants, per-seat via marketplace | 4-6 weeks | Saturated store; evidence doesn't transfer | Yes — team's key, priced per install |
| **H** | Cost-and-limit governor for unattended subscription runs | Solo devs / small teams running Claude Code | 3-7 days | Anthropic absorbs it; $9.99 price ceiling | **Yes** — local, reads own telemetry |

### A — the supervision layer as the product

The brief's default shape and the one the research layer argues hardest against. `../../../../docs/markets/agent-dashboard.md` records all three frontier vendors shipping their own agent-fleet console inside twelve months (Anthropic Claude Managed Agents Apr 2026, Google Gemini Enterprise Oct 2025 + Vertex folded in Apr 2026, Microsoft Agent Framework 1.0 2026) and OpenAI killing its own third-party-shaped Agent Builder in an **8-month lifespan** (launched 2025-10-06, sunset 2026-11-30). `../explore/control-planes.md` adds the 2026 delta: the two nearest-to-novel features on the market — Braintrust "Topics"/"Patterns" and LangSmith's spend-cap Gateway — were both shipped by **already-funded incumbents into developer-first products**. The one genuinely open square is the non-technical buyer, and that is precisely the buyer a two-person team in HCMC cannot reach without a sales motion (`../../../../docs/customers/first-customers.md`: the best-evidenced channel is 1-on-1 referral inside networks the team is not adjacent to). Multi-tenant by nature, so it survives the OAuth constraint only by making every customer bring an API key — which re-selects for the technical buyer the lane is already saturated with.

### B — the single-job blind-spot agent

One job, end to end, no dashboard: watch a named competitor's pricing page on a cadence, record each observed price as a dated fact with a staleness clock, and produce a periodic memo. The evidence is `../explore/smallbiz-blind-spots.md` → `../../raw/smallbiz-blind-spots-pulls.md`: Price Intelligently/SBI, *The State of B2B SaaS Pricing in 2024*, n=760, revenue-stratified — the $0-1M ARR cohort runs competitor pricing ~54% (highest of any band) and value-based ~20% (lowest), inverted at $500M+ (~28% / ~45%); the source attributes the gap explicitly to research being *"time-consuming and expensive to implement properly"*. That is the only size-stratified, dated, resource-attributed blind spot wave 1 found. It is also the shape the brief says agent execution can be trusted for (sub-question 3: watch a trend, record a fact, run a recurring chore) — **provided the product stops at the recorded fact and does not cross into the repricing recommendation**, which is agent-authored advice and lands on the untrusted side of the brief's own line. Survives single-tenant cleanly: the customer receives a memo, never a login.

### C — the graduation engine alone

The invention from fact 2, extracted and shipped by itself: read the local task record, cluster repeated work, and when a task crosses a threshold, emit a dedicated skill / subagent / slash command for that specific case. `../explore/task-telemetry.md` confirms `/usage`'s `Loops` row rolls up *already-defined* scheduled tasks only and does not detect that two ad-hoc prompts were the same task. Nothing in the platform does. The competitive problem is named in `../explore/control-planes.md`: Braintrust shipped **Topics** (continuous trace clustering, GA 2026-06-01) and **Patterns** (automatic recurring-behaviour identification with recommendations, public preview 2026-09-03), both vendor-reported and neither hands-on verified. If Patterns already closes the loop from cluster to generated tool, C is a reimplementation with no distribution. Runs entirely on local hooks, needs no auth of any kind, so the OAuth fork does not touch it.

### D — the mocking morning report as the whole product

The persona as the product rather than as a skin: one daily briefing, in the dabbing voice, over whatever numbers the operator connects. This is the only candidate whose asset is the collaborator rather than the builder — an animator and storyteller is a distribution capability, and personality-led distribution needs no field sales and no US entity. It is also the only candidate with **zero sourced demand: `unknown — not pulled, wave 1 did not cover it`.** One adjacent data point cuts against it: Hermes's own `SOUL.md`, fetched 2026-09-17 (`../explore/hermes-substrate.md`, STATE.md 2026-09-17 entry), specifies a **direct / no-filler** communication style and not a mocking one — the nearest comparable persona spec in the substrate this project is cloning made the opposite choice deliberately.

### E — run it as a service for local clients

The two of them operate the supervision layer on behalf of HCMC/SEA clients for a retainer; the software is internal tooling that never ships. This is the one candidate where geography is an asset rather than a tax. `../../../../docs/findings/market-gaps-2026.md` states it directly: *"The access gap is the only one where being in Ho Chi Minh City is an advantage rather than a cost."* And `../../../../docs/customers/first-customers.md` holds the single strongest channel account in the whole repo — a consultant at 100% capacity, **$10,000/week**, whose stated channel is 1-on-1 pro-bono help inside influential groups, which is exactly a proximity play. Against it: the same file's 928-point account of the technical/non-technical split where the non-technical founder brought the first eight customers in four months and then left for a $190K salary keeping 40%; the collaborator travels; and the user's stated preference in `scope.md` is the technical side.

### F — the trust boundary as the product

Not the dashboard, the provenance. Every fact an agent records carries which raw artifact it came from, when it was fetched, how stale it now is, and a re-check action — shipped as a plugin/MCP into other people's agent stacks rather than as a destination UI. Directly grounded: `../explore/task-telemetry.md` lists staleness-of-a-recorded-fact as **not obtainable** from any platform primitive and notes the build would sit on the agent's own state store's timestamps (Hermes's SQLite + FTS5 `hermes_state_*` split has them — `../explore/hermes-substrate.md`). It answers the brief's sub-question 3 exactly. The problem is size: this is a feature that a trace vendor bolts on in a sprint, and nobody buys provenance before they have been burned by its absence.

### G — narrow agent into a marketplace

Pick one bounded job and ship it where a Vietnam-based team can actually reach buyers and get paid. `../../../../docs/customers/first-customers.md` makes the case on rails, not on product: Shopify is *"You keep 100% of your first $1,000,000 USD in gross app revenue"* plus 2.9% processing and a one-time $19 registration, paid via Hyperwallet — the same cross-border rail as Upwork — while **AWS Marketplace's seller-eligibility list does not include Vietnam**, and Microsoft's Partner Center confirms only eligibility, never volume. Marketplace distribution intermediates the two things this team lacks: trust and a payment rail. The hole is the product half — the pricing evidence in B is about **B2B SaaS companies**, and no source in this repo says an ecommerce merchant has the same blind spot.

### H — the cost-and-limit governor

The smallest candidate and the only one the team needs regardless of which product it picks: a local governor that watches the subscription window, queues or defers work before it hits the wall, kills runaway spend, and attributes cost per task. Every input is primary-doc sourced in `../../raw/claude-code-docs-2026-09-17.md`: the subscription allowance resets on *"a rolling five-hour window and a weekly window"* and failure is a hard stop naming a reset time (L52-55 of `../explore/claude-code-substrate.md`); `autoContinueAtUsageLimit` exists as a managed setting; **agent teams cost ~7x a standard session** when teammates run in plan mode (raw L77); scheduled tasks *"fire on interval even while session idle, sending full context each time"* (raw L76); and `total_cost_usd` plus hook `duration_ms` make the arithmetic free. Against it: `/usage`'s `Loops` row (v2.1.242+) is Anthropic already walking into this space, and `../explore/control-planes.md` records CrewTower — a macOS menu-bar controller for Claude Code/Codex/Cursor sessions — at **$9.99 one-time**, which is the observed price ceiling for this shape.

## What dies on the single-tenant constraint

**A dies as a product and survives only as a tool.** A fleet supervision dashboard whose buyer is explicitly non-technical cannot ask that buyer for an API key, and cannot offer them a claude.ai login. It becomes either an internal tool (which is E) or a developer product (which is the saturated lane). Nothing else in the set dies outright, because every other candidate either runs locally on the operator's own machine (C, F, H), or ships an artifact rather than a session (B, D, E, G).

The second-order casualty is **per-customer unit economics**, which the constraint pushes onto the team's own bill in B, D, E and G. The size of the subscription allowance is the number that decides whether that works, and it is **`unknown — no primary-doc figure found, checked code.claude.com/docs 2026-09-17`** (`../explore/claude-code-substrate.md` caveats). Wave 2c cannot size a per-customer run without it.

## The pick

**Conditional, and the condition is named.** No candidate in this set has direct demand evidence. Every argument above rests on either an *absence of supply* (`../explore/control-planes.md`'s SMB-gap search, self-flagged as "hard search, incomplete" under WebSearch quota) or a *practice gap* (the SBI pricing survey). Neither is a customer saying they would pay. `../../../../docs/findings/market-gaps-2026.md` searched demand-side complaint channels for exactly this kind of signal and found none for agent supervision — with three of four channels blocked, so it is a weak negative, not a clean one. State that plainly before reading the pick: **this is a pick among candidates, not a finding that the market exists.**

**Primary: B, scoped to the recorded fact and not the recommendation.** One agent, one recurring job, output-shaped, sold to a buyer reachable over the internet in English with no US entity and no field sales.

Strongest argument for it: it is the only candidate whose problem has a size-stratified, dated, resource-attributed source — SBI 2024, n=760, and the source attributes the gap to cost of research rather than to indifference, which is the precise condition under which automating supply changes behaviour. It lands on the trusted side of the brief's own line, it is 2-4 weeks for one person, and it is the only shape where a mocking memo has a legitimate target: an agent that dabs at *"you charge $29 because your competitor charges $29"* is mocking a decision the evidence says the buyer actually made.

Strongest argument against it, stated at full strength: **the source is a pricing-research vendor reporting that small firms under-invest in pricing research.** Price Intelligently sells the exact service the finding says is missing, the ~54% / ~20% figures were read off a chart on p.11 by a delegated sub-agent and were never fetched first-hand by this project, and the population is B2B SaaS companies — not the 3-10-person small business the brief is aimed at. Worse, the mechanism does not transfer automatically: *"they don't do it because it's expensive"* is compatible with *"they don't value it,"* and pricing consultants already exist at prices sub-$1M-ARR firms decline to pay. Making supply cheap does not create willingness to pay; it may only reveal that there wasn't any. And the moment the product crosses from recorded fact to repricing advice it violates the brief's own trust position — which means the version that is defensible is also the version that is least differentiated from a generic page-change watcher.

**Fallback: H.** Not because it is a bigger business — it is plainly smaller, and CrewTower's $9.99 one-time is the visible ceiling — but because its expected cost is close to zero. It is the tool the team must build to run B, D, E or G unattended at all; every input is already primary-doc sourced; the build is days; and if it sells nothing it still buys the team the ability to keep any of the others alive on a subscription. Its kill condition is the sharpest in the set and should be treated as likely: Anthropic ships adjacent to it every release, and `/usage`'s `Loops` row is already half of it.

**C is the one to watch, not to start.** If wave 2b establishes hands-on that Braintrust Patterns does not close the cluster-to-generated-tool loop, C becomes the most defensible technical claim in the set, because it is the only candidate whose core mechanism is confirmed absent from every platform rather than merely absent from a search.

## Tone — where it stops being funny

Kept on purpose, per the brief, and treated here as a hypothesis with a failure boundary rather than as a mistake.

It works where the target is a decision the operator already knows was lazy and the underlying fact is verifiable — the pricing memo is the clean case.

It stops working, and starts creating liability, at four named lines: (1) **when the number is wrong** — mocking plus wrong compounds trust loss rather than adding it, and every cost figure this stack can produce is explicitly a *"client-side estimate at list price,"* not a bill (`../explore/task-telemetry.md`); (2) **when the output leaves the operator** — a mocking line inside a client-facing board pack is the operator's liability, not the agent's; (3) **when it mocks advice it also authored** — a confident insult attached to a recommendation is the strongest possible framing for the weakest possible epistemics, and it is exactly the combination sub-question 3 says not to trust; (4) **when a person rather than a decision is the target** — a task record naming who overrode an agent is an HR artifact.

Whether the register carries at all in a Vietnamese or wider SEA business context is **`unknown — not pulled, wave 1 did not cover it`**, and is not asserted either way here.

---

## DAYDREAM — speculation, not evidence. Nothing in this section is sourced. Wave 2b: do not fact-check this section; it is fiction by construction.

*Everything from here to the next horizontal rule is what-if. No claim below traces to a raw file, and none should be quoted back into any other document as a finding.*

**18 months out, if B works.** The unit is not a dashboard and not a report — it is a *watched fact*. A customer names something they want to stay true (a competitor's price, a regulation's text, a supplier's lead time, a rival's headcount) and the fact gets a clock. The product's whole surface is a list of facts, each with a date, a source artifact, and a colour that says how stale it is. Revenue is per watched fact per month, which is a unit a non-technical buyer can price in their head — the thing every agent product currently fails at. At a hundred customers times a few dozen facts each, the interesting asset is not the software; it is a corpus of what small companies actually choose to keep an eye on, which is a demand signal nobody else has because nobody else made the unit of sale that small.

**The second product falls out of the first.** Once facts are watched, recurrence is visible for free: the same fact re-checked the same way sixty times is the graduation trigger C was going to have to invent from scratch, except now it arrives with a customer attached. The second product is the graduation itself sold back — *"you have re-run this by hand every Monday for four months, here is the tool, it costs less than the four months did."* That ordering matters: B earns the data that makes C defensible, where C on its own has to guess at what recurs.

**What the unfair advantage compounds into.** Two things, neither of which a funded competitor can copy quickly. First, a cost floor: the team runs on a subscription with per-task cost visible at the hook level, so they know the true marginal cost of every watched fact to four decimal places while a competitor priced off API list rates does not. Second, voice as a moat that is genuinely non-technical — the mocking register is the collaborator's craft, and craft is the one input that does not get absorbed when the platform vendor ships the feature. The pessimistic version of the same 18 months is short and should be held next to it: the frontier vendor ships watched-facts-with-staleness as a checkbox, the corpus turns out to be a hundred customers all watching the same six things, and the voice reads as a novelty the second a memo is wrong.

---

## What wave 2b must attack

Load-bearing claims in this file, ranked by how much collapses if they are wrong.

| # | Claim | Where it sits | Why it could be wrong |
|---|---|---|---|
| 1 | Self-use of subscription OAuth for paid customer output is permitted | Candidate B, E, G; "What dies" | Wave 1 flags it as interpretation, explicitly not counsel |
| 2 | SBI ~54% competitor / ~20% value-based, $0-1M ARR band | Candidate B, the pick | Vendor sells the missing service; chart read second-hand |
| 3 | No cheap incumbent already watches competitor prices | Candidate B | **`unknown — not pulled`.** Prisync, Competera, Visualping unchecked |
| 4 | No SMB-targeted agent supervision product exists | Candidates A, E | Negative from a quota-constrained search, self-flagged incomplete |
| 5 | `Stop`/`SubagentStop` really carry `cost` and `duration_ms` | Candidates C, F, H; the cost floor | Docs-only; `hooks.md` came back structured, never measured live |
| 6 | Braintrust Patterns does not close cluster→generated-tool | Candidate C | Vendor blog only, preview-stage, zero hands-on verification |
| 7 | A Vietnam-based pair can collect recurring USD from foreign buyers | Candidates B, D, G | **`unknown — not pulled`.** Stripe/Paddle/Hyperwallet eligibility unchecked |
| 8 | One subscription can sustain N customers' daily unattended runs | Unit economics of B, D, E, G | Allowance size is `unknown — no primary-doc figure found` |
| 9 | A repricing recommendation is trusted-task-shaped | Candidate B as originally framed | It is not. Named internal contradiction, resolved by scoping down |
| 10 | CrewTower $9.99 is the price ceiling for governor-shaped tools | Fallback H | n=1, from the same quota-constrained pull as #4 |
| 11 | Demand exists for a mocking-persona briefing | Candidate D, tone hypothesis | **`unknown — not pulled`.** Zero sources. Hermes SOUL.md cuts against |
| 12 | Marketplace distribution substitutes for the missing sales motion | Candidate G | Eligibility confirmed, volume never was, for any marketplace |

Claims 1, 2 and 3 together decide whether the pick stands. If 1 fails, B and E need a different compute model and the whole set narrows to C, F and H. If 2 fails, B loses its only evidential leg and the honest output of this project becomes "no candidate clears the bar." If 3 fails, B is a commodity.

## Caveats

- This file compiles from `../explore/`, which itself compiles from `../../raw/`. Two of the five explore files (`control-planes.md`, `smallbiz-blind-spots.md`) are relays of delegated sub-agent reports rather than first-hand fetches — that chain is disclosed in both files' own caveats and in `../../raw/smallbiz-blind-spots-pulls.md`'s evidence-chain note, and it weakens every claim resting on them, which here means #2 and #4.
- Build-size estimates in the candidate table are this agent's judgement, not measured, not sourced. They are the one column with no evidence behind it and should be read as ordering, not duration.
- No candidate here was costed. Per-customer compute cost is unresolvable until claim #8 is closed.
- The pick is a pick among candidates. It is not a recommendation to build, and per `../../../../CLAUDE.md` the verdict is the user's.
