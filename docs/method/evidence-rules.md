# Evidence rules — amendments after pass 4

2026-09-17. Written after three execution projects (`../../projects/ai-ads-injection/`, `../../projects/agent-hermes-dashboard/`, `../../projects/ai-attack-defense/`) each ran explore → idea → adversarial review → re-pick on the same day, each killed its own pick, and each diagnosed the same class of method failure independently.

Compiled from the three post-mortems: `../../projects/ai-ads-injection/docs/plan/re-pick.md` §1, `../../projects/agent-hermes-dashboard/docs/plan/re-pick.md` §1, `../../projects/ai-attack-defense/docs/plan/re-pick.md` §1. Every example below is a real failure from those files, cited. Nothing here is hypothetical.

`../../CLAUDE.md` already says: *"Never compile from memory. Every compiled claim traces to a file in `docs/raw/`."* Every failure this session obeyed that rule. The rule binds a claim to a **file**, and each failure happened inside the file, below the filename. These eight rules are the amendments. Each is an instruction with a mechanical test.

---

## The eight rules

### 1. A citation resolves to a cell or to a sentence, never to a file

A claim taken from a table cites file + row label + column header + the cell text. A claim taken from prose cites file + the quoted sentence. `See X.md` is not a citation.

*Failure it catches.* `../../projects/ai-ads-injection/docs/plan/idea-set.md` recorded that this idea's services shape "Passes all five constraints" and scored the non-technical partner **Strong**, citing `../findings/cross-read.md`. Those cells sit in cross-read's `ai-attack-defense` **column**. The `ai-search-ads` column of the same two rows reads "Fails", "Fails" and "Content and GEO storytelling" (`../../projects/ai-ads-injection/docs/plan/re-pick.md` §1, row 1).

*Test.* Can a reader reach the exact cell from what you wrote, without searching? If not, it is not cited.

### 2. A figure carries the subject it was measured in

Every price, verdict or scorecard row is tagged with the market, product or idea it was measured against. Re-using it for a different subject is an assumption, not a citation, and is labelled `transplanted from <subject>` alongside the existing kinds (vendor-reported, analyst-derived, filed, company-stated, measured-by-us).

*Failure it catches.* "$8k–$50k engagements" was carried into the ads project as its own price band. That band prices security audits in `../markets/ai-attack-defense.md`; the ads market's own anchor in `../customers/answer-integrity-buyer.md` is $1,500–$5,000 (`../../projects/ai-ads-injection/docs/plan/re-pick.md` §1, row 2).

*Test.* Name the subject the number was measured on. If it is not the subject you are writing about, relabel it or drop it.

### 3. A compiled file cites `raw/`, never another compiled file's conclusion

A compiled file may cite a raw pull, or quote a compiled file's sentence **verbatim including its hedge**. It may not cite another compiled file's conclusion as evidence. If a claim is needed from a compiled file, copy that claim's own raw citation, not its sentence.

*Failure it catches.* `../markets/ai-attack-defense-services.md:46` reads, verbatim and re-opened this pass: *"**Vendor security questionnaires** reportedly ask whether a product 'underwent independent AI red teaming, which attack classes were tested, what evidence exists.' Could not confirm CSA's CAIQ has such a field: `unknown — checked 2026-09-16`."* `../../projects/ai-attack-defense/docs/explore/sea-compliance-triggers.md` re-quoted it with both gone. `../../projects/ai-attack-defense/docs/plan/niche-and-solutions.md` §3 then printed it as the strongest-graded compliance trigger in its table. Each restatement read as independent confirmation of the last (`../../projects/ai-attack-defense/docs/plan/re-pick.md` §1, Lesson 1).

*Test.* For each citation in a compiled file, open the target. If the target is compiled and you are using its conclusion rather than a verbatim quote, the citation is invalid.

### 4. Everything that qualifies a sentence travels with the sentence

Hedges ("reportedly", "appears to"), `unknown — checked …` flags, and the source's own definition of a term inside the quote travel with the quote — or the quote is not used.

*Failures it catches.* Two, on the same day.

- The hedge case is rule 3's example: "reportedly" plus an `unknown` dropped in one re-quote.
- The definition case: `../findings/injection-feasibility.md`'s phrase "Step 4 is what nobody sells" was quoted as proof of unserved demand. The same file defines step 4 as live-engine transfer testing against perplexity.ai — barred by OpenAI's ToU effective 2026-01-01 and Perplexity ToS s5.2(i), and prohibited by §1 of the very idea file that quoted it (`../../projects/ai-ads-injection/docs/plan/re-pick.md` §1 row 3, and §2).

*Test.* Read the source sentence and your sentence side by side. Every qualifier and every defined term present in the first must be present or quoted in the second.

### 5. An absence claim carries its checked set

Written as: `no X found in {A, B, C} — checked <channel> <date>`. The brace list is mandatory. A sentence with no brace list is not an absence claim, it is a guess. This applies to a missing **product** exactly as `../../CLAUDE.md` already applies it to a missing **number**. An absence asserted over a document already sitting in `raw/` names the strings searched in it.

*Failures it catches.* Three.

- "No shipping guardrail supports Vietnamese" — three vendors checked, written up as a market absence; Azure's own language table lists `vi` (`../../projects/ai-attack-defense/docs/plan/re-pick.md` §1).
- The endpoint-exposure grader's one surviving absence rested on a single tool, garak's 43 probe modules, and was written as a market claim. A wider sweep killed three of its five sub-claims: `JailbrokenAI/wallbreaker` `tools/prefill.py`, promptfoo's `special-token-injection` plugin, and nuclei's `vllm-openai-api-exposed.yaml` (`verified: true`) — `../../projects/ai-attack-defense/raw/repick-endpoint-absence-pulls.md`, read in `../../projects/ai-attack-defense/docs/plan/re-pick.md` §4.
- `../../projects/ai-ads-injection/docs/explore/policy-ceiling-addendum.md` Gap 3 marked OpenAI's ad policies "Silent" on differential serving. The project's own `../../projects/ai-ads-injection/raw/openai-ad-policies.txt` carries "Ads must be consistent end-to-end" and "Destination integrity" (`../../projects/ai-ads-injection/docs/plan/re-pick.md` §1 row 4, and §3).

*Test.* Grep the file for absence words — no, none, nobody, nothing, silent, unserved, first, only. Each hit either has a brace list and a date, or is rewritten.

### 6. An unattacked absence may not rank a candidate

Observed base rate in this repo: **five absence claims were attacked in the `ai-attack-defense` review wave and one survived; that survivor then lost three of its five sub-claims to a wider sweep. Roughly one in five unattacked absence claims holds** (`../../projects/ai-attack-defense/docs/plan/re-pick.md` §1, Lesson 3).

What that implies, stated so it can be applied without judgement: an absence claim that has not been attacked carries **no ranking weight**. It may be listed as a hypothesis with its brace list. It may not be the reason a candidate is ranked first, and a candidate whose case rests only on unattacked absences is not ranked at all until one is attacked. Ranking on an unattacked absence is a 1-in-5 bet priced as a certainty. `ai-attack-defense` ordered its own attack list by absence claims in wave 2a, then picked on them a week before the attack ran.

*Test.* For the top-ranked candidate, list the claims its rank depends on. Any absence among them not yet falsified by a named wider sweep removes it from the ranking.

### 7. A load-bearing statistic carries its author's conclusion and its denominator

Beside a statistic a thesis rests on, record verbatim what the source's own author concludes from it. If the author's conclusion contradicts the thesis, that is the finding, not a caveat. And a count with no denominator is not a measurement.

*Failures it catches.* Two, same family.

- The SBI pricing figures survived full verification — PDF re-fetched, p.11 rasterised, numbers matched exactly — and pointed the opposite way from the thesis built on them: the $0-1M cohort uses competitor pricing at ~54%, the highest of any band, and the source calls that the error to correct (`../../projects/agent-hermes-dashboard/raw/2b-sbi-pricing-report-firsthand-2026-09-17.md`, read in that project's `re-pick.md` §1). Every provenance rule in this repo was obeyed. None of them catches inversion.
- "828 issues" was the entire demand case for the hermes project. 828 is 0.88% of the repo's 93,582 titled issues, ranks last of eleven comparable topics sampled the same day, and 87.8% are closed (`../../projects/agent-hermes-dashboard/raw/2abis-demand-signal-interrogation-2026-09-17.md`).

*Test.* Next to the number, write the author's own sentence about it, and the denominator. If either is missing, the statistic is not yet usable.

### 8. Load-bearing claims are re-opened, not remembered

Before a pick, a recommendation or a decision rule is written, each claim it rests on is re-read at its source **in the same pass**, and the document names which claims were re-opened. A claim carried forward from an earlier read is memory, whatever file it originally came from.

*Failure it catches.* All of the above. Every one of the ads project's four broken claims survived because it was carried forward from an earlier read (`../../projects/ai-ads-injection/docs/plan/re-pick.md` §1). This is the cheap rule, and the one that would have worked alone.

*Test.* The document carries a line naming the claims re-opened at source this pass. A load-bearing claim not on that list is either not load-bearing, or the document is not done.

---

## Three claims caught only by measurement or by primary text

Better searching would not have found any of these. Each was wrong inside a file that cited a real source correctly. The lesson, stated directly: **when a claim names a field, an endpoint, a grammatical subject or a table cell, stop reading about it and go read or run the thing itself.**

**1. The Claude Code hook payload — measured live, 2026-09-17.** `../../projects/agent-hermes-dashboard/docs/explore/claude-code-substrate.md` stated verbatim that `Stop` / `SubagentStop` "carry `cost: {input_tokens, output_tokens}` and `duration_ms` directly in the hook payload". `../../projects/agent-hermes-dashboard/docs/explore/task-telemetry.md` said the same, and its own caveats section asked for a live test. Two waves — an idea set, a pick and a review — carried it as a mechanism. Four live `claude -p` runs on Claude Code v2.1.259 (`../../projects/agent-hermes-dashboard/raw/hook-payload-measurement-2026-09-17.md`) found **neither field on either event**, reproduced twice including one real subagent spawn. `costUSD` and `duration_ms` occur zero times in the transcripts; `~/.claude/stats-cache.json`'s `costUSD` is hard-coded 0; there is no headless `/usage`. The claim broke in the direction that cost three candidates the most. `../../projects/CLAUDE.md` already says *"Measured beats argued"* — the rule existed and nobody ran the command.

**2. Vietnam Law 134/2025/QH15, Điều 10.5.b — the grammatical subject, from the gazette text.** Law-firm summaries said medium-risk AI systems face "sample audits or assessments by independent organizations", which reads as a duty to buy an assessment. The primary text (`../../projects/ai-attack-defense/raw/repick-vietnam-ai-law-pull.md`) says: *"Hệ thống trí tuệ nhân tạo có rủi ro trung bình được giám sát thông qua báo cáo, kiểm tra chọn mẫu hoặc đánh giá của tổ chức độc lập."* The subject is the supervising authority, not the provider; independent assessment is one of three alternatives the **regulator** may choose. Nothing obliges a medium-risk provider to buy one. The only mandatory assessment, Điều 13, binds high risk only, and its content (Điều 13.2 → Điều 14) is entirely process duties with no performance, accuracy or safety threshold. The gazette PDF has no text layer; the pages were rendered and transcribed visually. No amount of secondary reading produces this.

**3. `../findings/cross-read.md` — the column, read off the rendered table.** Rule 1's example. The claim was traced to the right file, the right table and the right rows, and read one column across. The check is mechanical and takes seconds: open the table, count columns.

The common shape: in all three, the file being cited was correct. Searching harder finds more files. Only execution and primary text find the error.

---

## What these rules do not fix

They are provenance-and-inference rules. They make compiled files honest about what a source says. They say nothing about whether anyone will pay. Every project this session had a tractable mechanism and unevidenced demand, and no rule here would have changed that — see `../findings/pass4-read.md`.

---

## Caveats

- The base rate in rule 6 is one project's count of its own attacked claims (five attacked, one survived). Small n from a single wave. It is a working figure, not a measured repo-wide rate.
- Rules 1, 2 and 4 are as proposed in `../../projects/ai-ads-injection/docs/plan/re-pick.md` §1; rules 3, 5 and 6 as proposed in `../../projects/ai-attack-defense/docs/plan/re-pick.md` §1; rule 7 as proposed in `../../projects/agent-hermes-dashboard/docs/plan/re-pick.md` §1. Rule 8 appears in the ads file and is the one all three imply. The merge, the ordering and the tests are this agent's.
- No rule here was tested by re-running a wave under it. The claim that each would have caught its example is a reading of the example, not an experiment.
- The three post-mortems were read in full this pass. The compiled files they indict (`idea-set.md`, `niche-and-solutions.md`, `sea-compliance-triggers.md`, `policy-ceiling-addendum.md`) were not re-read line by line. Two claims were re-opened at source this pass: `../findings/cross-read.md`'s constraint table, whose column layout was verified directly, and `../markets/ai-attack-defense-services.md:46`, quoted verbatim above.
- These rules add cost to every compiled file. Nobody has measured how much.

## One note for the user, not acted on

Rules 3, 5 and 8 amend sentences that live in `../../CLAUDE.md` itself — *"never compile from memory. Every compiled claim traces to a file in `docs/raw/`"* and *"`unknown — checked <channel> 2026-09` beats a guess"*. They arguably belong there rather than here, since an agent that reads only `CLAUDE.md` will not see them. This file does not modify `CLAUDE.md` at any level. Moving them is the user's call.
