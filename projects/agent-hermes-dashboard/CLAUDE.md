# agent-hermes-dashboard

Source: `MegaPlan.md` §2. Research behind it: `../../docs/markets/agent-dashboard.md`, `../../docs/competitors/agent-dashboard-roster.md`, `../../docs/raw/agent-dashboard-pulls.md`.

## The question

Can a small business get enterprise-grade execution from a team of agents — and is the supervision layer, not the agents, the product?

The meme frame, stated by the user and kept on purpose: the assistant is not deferential. Morning report dabs at your numbers and mocks weak decisions. Tone is a product decision — test it, do not sand it off by default.

## Sub-questions

1. **Hermes substrate.** What is Hermes actually, as of 2026-09 — model line, agent framework, repo, license, layout. `../../docs/method/scope.md` flags "confirm before building on it". Confirm it or replace it, in `docs/explore/`, with the source.
2. **Role mimicry.** Big-company roles (CFO, head of growth, ops, competitive intel, board-pack writer). Which map onto a 3-person business, which are theatre. Persona as prompt-and-tooling, not as costume.
3. **Trust boundary.** Stated position: do NOT trust agent-authored dashboards and charts by default. DO trust agent execution of small bounded tasks — research a person, record a fact, watch a trend, run a recurring chore. Where exactly is the line, and what does the UI do at that line.
4. **Observability.** Metrics for agent task workflow: cost per task, wall time, retry rate, human-override rate, task recurrence, staleness of a recorded fact. What a supervisor actually needs to see.
5. **Memory + recurrence.** Minimum viable: agent remembers each task it did; a repeated task graduates into a dedicated tool or workflow tailored to that case. Design that graduation path.
6. **Autonomy substrate.** Runs on Claude Code OAuth token plus usage. What that constrains — rate, cost, session model, what breaks unattended.

## What "done" looks like

- `docs/explore/` — Hermes confirmed or killed, with source. Existing agent control planes and what they show.
- `docs/design/` — the supervision layer: task record schema, recurrence detection, graduation to tool, trust boundary in the UI, the metrics panel.
- `docs/review/` — against `../../docs/competitors/agent-dashboard-roster.md`. Crowded lane; name who already does each piece.
- `prototype/` — runs. Smallest version: N tasks executed, each recorded with cost/time/outcome, one recurring task detected and promoted to a tool, one report generated in the mocking voice. Local, no cloud spend beyond token usage.
- `docs/outcome/` — what the prototype proved about delegation depth. How far delegation held before output stopped being trustworthy.

## Known traps

- The dashboard is the easy half and the worthless half. Chart-making agents are commodity. The record / recurrence / trust layer is the claim.
- "Enterprise capability for small business" is what every horizontal AI tool says. Find the one task where a 3-person shop is measurably blind, start there.
- Tone is a wedge and a liability. Note where it stops being funny.
