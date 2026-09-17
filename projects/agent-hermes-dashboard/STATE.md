# STATE — agent-hermes-dashboard

Append-only running log. Newest entry at the bottom. Write the plan BEFORE the work, the result AFTER it. An agent that dies mid-run must leave its successor enough to continue.

Entry format:

```
## <UTC+7 timestamp> — <agent role> — <phase>
PLAN: what is about to happen
DID: what happened
FILES: paths written
OPEN: what is unfinished, and what the next agent should pick up first
```

---

## 2026-09-17 — main thread — scaffold
PLAN: create project folder, brief, state log.
DID: folder skeleton + `CLAUDE.md` written from `MegaPlan.md` and the three research passes in `../../docs/`.
FILES: `CLAUDE.md`, `STATE.md`, `docs/{explore,plan,design,review,execution,outcome}/`, `raw/`, `prototype/`.
OPEN: explore phase not started.
