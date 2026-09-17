# ai-attack-defense

Source: `MegaPlan.md` §3. Research behind it: `../../docs/markets/ai-attack-defense.md`, `../../docs/markets/ai-attack-defense-services.md`, `../../docs/competitors/ai-attack-defense-roster.md`, `../../docs/raw/services-lane-pulls.md`, `../../docs/markets/vietnam-sg-access.md`.

## Context on this machine

`D:\ai\aisb` — AISB, real current AI-security teaching material. Modules: LLM internals, logprobs, instruction hierarchies, prompt injection, coding agents, monitoring, control protocols, safety simulator, tokenization, jailbreaking, guardrails, knowledge distillation, weight extraction, model editing, backdooring, safety finetuning (and undoing it), adversarial vision/language, prefix tuning, watermarking, threat modeling, NVIDIA container toolkit, GPU rowhammer. Read its `CLAUDE.md`, `AGENTS.md`, `aisb_utils` and the module list.

Also scan for reusable context: `D:\ai\security`, `D:\projects\lv1-auditor`, `D:\projects\smart-contract`, `D:\projects\audit-history`, `D:\audits`.

AISB is curriculum. The gap to look for: what a practitioner learns there and then cannot buy as a working tool.

## The question

Find a niche inside AI attack/defense, list the product solutions it implies, then build one very small thing for someone in Southeast Asia who needs it.

## Sub-questions

1. **Curriculum-to-market gap.** Per AISB module: is there a shipping product? Free, paid, or nothing. The "nothing" rows are the candidate list.
2. **Niche selection.** One niche, narrow. Not "AI security" — something like "guardrail regression testing for a Vietnamese-language support chatbot" narrow.
3. **SEA buyer.** Who in Southeast Asia has this problem, buys software, and is reachable without a field sales motion. `../../docs/markets/vietnam-sg-access.md` and `../../docs/customers/first-customers.md` carry the access read — use it, do not redo it.
4. **Solution list.** Ranked list of possible products for the niche, each with build size and what makes it defensible.
5. **Build one.** Super small. Runs. Solves one real instance of the problem.

## Boundary — hard

Defensive and educational. Offensive technique only as test material against systems you control or public benchmarks published for study (AISB's own material qualifies). No third-party targeting, no evasion tooling built for misuse. Red-team payloads already in AISB may be reused as test inputs against your own prototype.

## What "done" looks like

- `docs/explore/` — AISB module inventory with a market column. What this machine already holds that is reusable.
- `docs/plan/` — the niche, argued from evidence, plus the ranked solution list.
- `docs/review/` — against `../../docs/competitors/ai-attack-defense-roster.md` and the services-lane finding. Pass 2 ran an adversarial pass on the services conclusion; read it, do not re-litigate it.
- `prototype/` — one small tool, runs, with a real test case from AISB material as input.
- `docs/outcome/` — who exactly would pay, what it does not do, what breaks at scale.

## Known traps

- Market read says platform plays are crowded and funded. Stated preference: small tool that works. Honor it.
- SEA buyers for security tooling skew toward compliance triggers. Find the trigger, not the fear.
- Localization — Vietnamese-language attack/defense evaluation — is thin ground and may be the whole wedge. Check before assuming.
