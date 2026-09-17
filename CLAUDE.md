# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A research repo, not a codebase. There is no build, no test suite, and no package manager. Every deliverable is markdown produced by a research pass. If a command is ever needed here it will be a one-off script under `docs/method/`, not an application.

**Subject: not yet set.** The repo is a fresh scaffold — `docs/` holds the category skeleton and nothing else. Before the first research pass, ask the user to name the market, the geography, and the decision the research has to serve. Record that answer in `docs/method/scope.md` and treat it as the standing brief.

Sibling repos under `D:\researchs\` (`startup/`, `hobby/`) run the same conventions. Read `D:\researchs\startup\CLAUDE.md` if a convention below needs a worked example.

## Hierarchy

Everything lives under `docs/`. The repo root holds only this file and any generated tracker (a CSV plus its rendered markdown) once one exists.

```
CLAUDE.md          this file — global rules, and the hierarchy
docs/
  CLAUDE.md        what each subfolder below is for, and what may not go in it
  method/          how the research runs: scope, pipeline, templates, conventions
  sources/         where data comes from — channels, and who is worth profiling
  raw/             raw pulls, source-attributed, uncompressed
  markets/         per-market sizing and structure
  competitors/     one profile per company, plus INDEX.md
  customers/       demand side — segments, interviews, personas
  findings/        compiled tables, rankings, cross-market reads
```

Three layers, and work flows one way through them:

**sources → raw → compiled.** `sources/` decides what to pull. `raw/` holds the pull verbatim. `markets/`, `competitors/`, `customers/` and `findings/` are compiled from `raw/` and never from memory. `method/` governs all of it.

`docs/CLAUDE.md` is the authority on the subfolders. Read it before writing any file into `docs/`.

## Rules

Evidence:

- Never compile from memory. Every compiled claim traces to a file in `docs/raw/`.
- Every number carries a source, labeled by kind: vendor-reported, analyst-derived, filed, or company-stated.
- Absolute dates. "As of 2026-09", never "recently".
- `unknown — checked <channel> 2026-09` beats a guess. A guessed number survives into the compiled tables and poisons them.
- Conflicting figures sit side by side, attributed. Never averaged.
- Every compiled doc carries a caveats section.
- The verdict is the user's call. Produce the evidence, not the go/no-go, unless asked.

Compression — applies to files, not only to chat:

- Prose in `docs/` is compressed before a file is done. Cut hedging, filler and restatement; keep the substance.
- Compression kills prose, never evidence. Numbers, dates, source labels, quoted text and URLs survive verbatim.
- State each fact once per file. No section restating a table row in prose.
- Table cell: 12 words. A cell that wants a paragraph means the paragraph belongs in `docs/raw/` and the cell carries the number.
- `docs/raw/` is exempt. Raw stays raw, in the source's own words.
- Generated files are exempt and never hand-edited. Fix the input, re-run the generator.

## Git

Not a git repo yet. If one is initialized, it is a restore point, not a workflow — no branch flow, no PRs. `.gitkeep` files hold the empty category folders.
