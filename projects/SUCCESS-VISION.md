# Success vision — the portfolio read

2026-09-17. Vision agent. Reads on top of the three per-project files: `ai-ads-injection/docs/outcome/success-vision.md`, `agent-hermes-dashboard/docs/outcome/success-vision.md`, `ai-attack-defense/docs/outcome/success-vision.md`. Grounded in `MVP-MANDATE.md`, `ORCHESTRATION.md`, `../MegaPlan.md`, each project's spec / build-log / e2e / plan / review, and the parent repo's `docs/findings/pass4-read.md`, `cross-read.md`, `pass3-read.md`, `docs/customers/first-customers.md`, `docs/markets/vietnam-sg-access.md`.

The user asked for a recommendation, not three equal options. This file gives one. The verdict is still the user's.

---

## What was actually built, in one line each

| Project | What exists today (measured) | What the original idea was |
|---|---|---|
| `aicrawlcheck` | Offline log classifier; checks claimed AI-crawler identity against 9 published range files; 5/5 adversarial spoofs caught; never run on a real log | Detect an AI fetch and serve it different text — barred, not built |
| `Foreman` | Ledger + recurrence detector + skill scaffold + mocking report; 0.365 s; 19/19 tests; error-path safety bug found and fixed | A brutal morning report that mocks your business decisions — needs data the tool cannot source |
| `parity-vi` | VI/EN paired guardrail harness, 300 pairs, diff with exit codes; every number reproduced from clean; never run against a real guardrail | A Vietnamese guardrail wedge — narrowed to "nobody has measured shipping products on paired items" |

All three are honest, deterministic, stdlib, offline, and correct against their own fixtures. All three have the same hole, in the same place: **the product's one moment has never happened on real input.** `aicrawlcheck` has never seen a real log. `Foreman` has never seen a real ledger. `parity-vi` has never seen a real guardrail. Each e2e doc names this as the top gap independently. That is the portfolio-level finding, and it should redirect wave 10 before anything cosmetic.

## The one-line win condition for each

- **`aicrawlcheck`** — a public repo plus one published measurement of real spoof rates on real logs; a calling card, not a business.
- **`Foreman`** — a free MIT tool that passes or fails the pre-registered 14-day gate (≥100 stars AND ≥3 unprompted paid asks), and a four-line joke that strangers screenshot; a distribution-and-voice test, not a business.
- **`parity-vi`** — one real parity number on a commercial moderation endpoint, published; three conversations in HCMC; one paid engagement at a Vietnamese price. The only one of the three whose honest win includes money.

## Do they share a buyer?

No. Three unrelated bets:

| | Buyer | Where they are | Channel available to this team |
|---|---|---|---|
| `aicrawlcheck` | Developer who reads server logs | Global, English-speaking forums | Publish; no sales motion |
| `Foreman` | Solo operator running Claude Code on a business | Global, Claude Code community | Publish; no sales motion |
| `parity-vi` | Engineer owning a Vietnamese chatbot | Ho Chi Minh City, named companies | **In person** — the only project where this team is adjacent to its buyer |

Nobody has contacted any of them, in any project, in any pass (`pass4-read.md` cross-read point 2). Every negative on file is a search-level negative.

What they share is not a buyer but a **DNA**: each is a small offline checker that takes a claim somebody else made — a user-agent header, a vendor's "supported" tick, a user's "I have a workflow" — and turns it into evidence with the source named per row. That competence is real and is demonstrated three times. It is the competence of an auditor, not a SaaS vendor. `cross-read.md` pattern 3 said services was the lane that works at n=1 for this team; the build phase confirmed it by accident: the team built three audit instruments.

## Ranked recommendation

**1. `parity-vi` — put the remaining effort here.**

It is the only project with (a) a named, reachable buyer in the team's own city, (b) the one sales channel the parent research rated strongest — 1-on-1 proximity — available, (c) a claim that survived adversarial review (paired VI/EN on shipping guardrail products, still unpublished by anyone found), (d) a revenue shape the research favours (per-engagement, works at n=1, report-writing is a real job for the non-technical partner), and (e) a nearly-free path to its own moment: Qwen3Guard-Gen-0.6B is ungated and fits this GPU, and the mandate permits a `uv` venv when genuinely needed. Against it, stated at full strength: promptfoo does most of it free; the law does not require it; SEA-HELM can switch on the paired corpus with one revert; the price is Vietnamese-sized and `unknown`; and the fixture demo is the most convincing fake of the three. None of those is closed by more research. One real run and three conversations close all of them one way or the other, inside two weeks, for $0.

**2. `aicrawlcheck` — ship it as-is, cheaply, and stop.**

The tool is done and honest. Its remaining value is one real-log run, a public repo, and a post with a measured number — a weekend, then leave it. It has no buyer and its method has a dated successor (Web Bot Auth). Do not build a hosted version, a dashboard, or answer sampling; each is barred, free elsewhere, or both. Its one open question worth an hour: do GoAccess / AWStats / Matomo already do this. If yes, a pull request to one of them is the entire product.

**3. `Foreman` — publish and run the gate, and let the gate decide.**

The buyer broke in review and nothing built since has re-found one. What Foreman carries that the other two do not is the user's own creative intent — the voice — and the collaborator's craft. Both deserve exactly the test the re-pick pre-registered and no more: free, MIT, one release post, fourteen days, count stars and unprompted paid asks. One change before publishing is worth making because it moves the "oh" moment from a fortnight after install to the first run: a `--from-history` scan over `~/.claude/history.jsonl`, which already holds every field recurrence detection needs (3,103/3,103 real entries parsed, `e2e-test.md`). Then let the number speak. "500 stars with zero paid asks is a stop" was written before anything was built; honour it.

**Effort split, if the user accepts this:** roughly 70 / 10 / 20. `parity-vi` gets the real run, the page rebuilt around it, and the human conversations. `aicrawlcheck` gets one real log and a repo. `Foreman` gets the history mode, the two one-line fixes the e2e named, a repo, and a clock.

## What changes for the wave 10 fix agents

Three redirections, in priority order, above any item in the review checklists:

1. **Real input before polish.** For each project, the first fix-wave task is the one that puts real data through the tool: one real anonymised log; one real ledger (history mode); one real guardrail (local Qwen3Guard adapter). Every page then leads with a real number labelled `measured, n=1` and demotes the fixture demo to "how it works." A fixture demo as the hero is the fake-demo trap in all three project files, and it is currently the hero in all three.
2. **Do not give the demos more polish than the reality has.** The pages are already more finished than the products. Layout fixes from the vision review are fine; new interactive flourishes on synthetic data are not.
3. **Hold the honesty lines the specs drew, especially the ones a "fix" would be tempted to loosen:** no digit in a Foreman voice template; no `keyword` gap charted; no second sentence about Law 134/2025/QH15; no 25-of-155 quoted as a rate; no "the only tool" anywhere; no vendor host in the `parity-vi` repo.

## Is there a fourth product hiding in what got built?

The build waves surfaced five things nobody set out to find:

| Finding | Where | What it is |
|---|---|---|
| Traefik's Docker provider cannot reach a moby v2 engine; file provider works | `infra/` | An upstream bug report, worth filing under the user's name |
| A safety guard on the happy path but not the exception path (`_log_failure` unguarded) | Foreman e2e | A review rule: "check every write in every `except` block" |
| `wc -l` over-counts CSV rows with embedded newlines (1,107/1,113/8,853 vs 1,106/1,106/8,844) | parity-vi spec + build | A one-line lesson; the paper's numbers were right |
| Python rounds half-to-even; a pre-registered number used half-up; surfaced only at 26/32 | parity-vi build | A one-line lesson about pre-registering the rounding rule |
| Masking the values you send but not the ones that come back (`/tokens/verify` response carried the token id) | infra README | A rule: "the response body is the half that gets forgotten" |

**None of these is a product.** Each is a paragraph. What they are, together, is evidence for the one thing this whole session produced that is not any of the three tools: **a repeatable method for building an honest MVP in a day and finding what is wrong with it by running it** — pre-registered numbers, code fixed to match the spec never the reverse, exit codes read on the command not the pipe, response bodies masked, every sales claim traced to an e2e line, a "what it does not do" section that is the product position. That method lives in `MVP-MANDATE.md`, `../docs/method/evidence-rules.md`, and the three specs' acceptance checklists. It is the team's actual output, and it is the kind of thing that sells as a service or as a reputation — "we build the thing and tell you exactly what it does not do" — not as software.

If there is a fourth product, it is the one all three tools are instruments of: **an honest measurement service** — your guardrail in Vietnamese, your AI-crawler traffic, your agent's repeated work — delivered as a report with the evidence per row and the limits on the first page. That is `cross-read.md` pattern 3 again, arrived at from the build side instead of the research side. It is not a new idea in this repo; it is the same idea confirmed from a fourth direction. The fourth idea slot in `../docs/method/scope.md` stays blank on this evidence — nothing here is new enough to fill it.

## What this file does not say

It does not say any of the three is a business. On the evidence, none is yet. It says which one can find out fastest, at zero cash, using the one advantage the team has — being in the same city as the buyer — and that the other two should be finished cheaply and left to be what they are: a calling card and a test.

## Caveats

- Every "win condition" above is imagination constrained by the e2e evidence; every number inside them is invented and labelled so in the project files.
- The 70/10/20 split is this agent's judgement, not derived.
- The `parity-vi` recommendation rests on three named companies none of whom has been contacted, a local-model route (`Qwen3Guard-Gen-0.6B` via `uv`) that has not been tried, and a services argument drawn from US/EU evidence. It is the least-bad bet, not a proven one.
- Whether `/insights` already does what Foreman does, and whether GoAccess/AWStats/Matomo already do what `aicrawlcheck` does, are both `unknown — never inspected`; either answer would move the second and third rankings but not the first.
- No wave 9 review had landed for any project at the time of writing; this file is written from the e2e docs, not from a review verdict.
- Verdict is the user's.
