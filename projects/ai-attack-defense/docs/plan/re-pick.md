# Re-pick — what, if anything, this project should build now

Wave 2a-bis, 2026-09-17. Replaces the pick in `niche-and-solutions.md`; that file stays as the record of what was argued.

Inputs: `../review/market-check.md` (binding, not re-argued), `niche-and-solutions.md`, `../explore/*` including `dataset-baselines.md` and `ungated-path.md`, `../../prototype/data/`, and two new pulls made this wave — `../../raw/repick-vietnam-ai-law-pull.md` (primary statute text of Law 134/2025/QH15) and `../../raw/repick-endpoint-absence-pulls.md` (independent falsification of the one absence claim 2b left standing). Research layer: `../../../../docs/method/scope.md`, `markets/vietnam-sg-access.md`, `markets/ai-attack-defense-services.md`, `customers/first-customers.md`, `competitors/ai-attack-defense-roster.md`.

Verdict is the user's. This file produces the evidence and one recommendation, with the case against it stated at full strength.

---

## 1. Post-mortem — one mechanism, five failures

Five load-bearing beliefs broke in 2b and this wave. They broke the same way.

| Belief | Where it broke | What was actually behind it |
|---|---|---|
| No shipping guardrail supports Vietnamese | Azure's own language table lists `vi` | Three vendors checked, written up as a market absence |
| HiddenLayer scans files, not behavior | No raw file anywhere says it | A 35-format marketing list, inferred from |
| Nothing in SEA mandates AI testing | Law 134/2025/QH15, in force 2026-03-01 | A file that called itself the pass's weakest |
| Questionnaires ask about independent AI red teaming | Source says "reportedly" plus an `unknown` | A hedge dropped in one re-quote |
| No US market access | `scope.md`: "a business call, not a research finding" | A priced workaround, read as a wall |

**The mechanism: a hedge does not survive a citation.** Every one of these broke at the moment a compiled file quoted another compiled file. The quote kept the sentence and dropped the qualifier, and each restatement read as independent confirmation of the last. `ai-attack-defense-services.md` line 47 says questionnaires "reportedly" ask about red teaming and flags `unknown — checked CSA's CAIQ 2026-09-16`; `explore/sea-compliance-triggers.md` re-quotes it with both gone; `niche-and-solutions.md` §3 then prints it as the strongest-graded trigger in its table. Format list → inference → "Confirmed elsewhere" → "documented rather than assumed" is the same chain with different words.

**Lesson 1, actionable.** `../../../../CLAUDE.md` says "never compile from memory. Every compiled claim traces to a file in `docs/raw/`." Compiling from another *compiled* file is the same failure and the rule does not say so. Make it explicit: **a compiled file may cite `raw/` or quote a hedge verbatim including its hedge. It may not cite another compiled file's conclusion.** If a claim is needed from a compiled file, copy that claim's raw citation, not its sentence.

**Lesson 2, actionable.** The repo already demands `unknown — checked <channel> <date>` for a missing *number*. It never applied the same discipline to a missing *product*, which is where four of five kills landed. **An absence claim is written as `no X found in {A, B, C} — checked <channel> <date>`. The brace list is mandatory.** A sentence with no brace list is not an absence claim, it is a guess. "NOTHING found" and "no shipping product does X" are different claims and this repo wrote the second holding evidence for the first.

**Lesson 3, the one that should change how a pick is made.** This project ranked its candidates on absence claims. Absence claims are the claim type with the worst survival rate here: five attacked in 2b, one survived; that survivor has since been 60 % killed by this wave's own sweep. The observed base rate for an unattacked absence claim in this repo is roughly one in five. **Ranking a product on an absence that has not been attacked is the error, not any individual absence.** 2a even knew this — its §6 ordered 2b's attack list by absence claims — and picked on them anyway, a week before the attack ran.

The sibling project killed this session failed on the same shape: a compiled claim its own evidence did not support. That is a repo-level defect, not two agents' bad luck.

---

## 2. Vietnam's AI Law, worked properly

Primary text pulled this wave: `raw/repick-vietnam-ai-law-pull.md`. The gazette PDF has no text layer; the 20 pages were rendered and transcribed visually. Pages 3 and 10–18 are `unknown — not transcribed 2026-09-17`. Everything below is from the transcribed pages, verbatim in the raw file.

### What it requires, of whom, when

| Duty | Who | Trigger | Article |
|---|---|---|---|
| Self-classify into high / medium / low | Nhà cung cấp (provider) | Before deployment | 10.1 |
| Keep a classification dossier | Provider | Medium and high only | 10.1 |
| Notify the result to Bộ KH&CN via a one-stop portal | Provider | Medium and high, before deployment | 10.3 |
| Disclose to users that they face an AI | Provider | Any system interacting with humans | 11.1 |
| Machine-readable marking of generated audio/image/video | Provider | All | 11.2 |
| Explain on demand — purpose, function, main inputs, risk controls | Provider, deployer | Medium and high, on inspection | 14.1.e, 15.1.b |
| Conformity assessment before deployment | Provider | **High risk only** | 13.1 |
| Third-party certification by a registered body | Provider | High risk **on a PM list that does not exist** | 13.2.a, 13.4 |
| Risk management, data governance, technical dossier, activity log, human oversight | Provider | High risk | 14.1.a–g |
| Legal contact point in Vietnam | Foreign provider | High risk | 14.6 |

Scope, Điều 2: "cơ quan, tổ chức, cá nhân Việt Nam và tổ chức, cá nhân nước ngoài tham gia vào hoạt động trí tuệ nhân tạo tại Việt Nam."

Dates, Điều 34–35: in force **2026-03-01**. Systems already deployed get **12 months → 2027-03-01**, or **18 months → 2027-09-01** for health, education, finance. During that window they keep operating unless the regulator finds serious-harm risk.

Enforcement: reclassification, dossier supplementation, suspension, and "xử lý theo quy định của pháp luật" (Điều 10.6). **No penalty article appears in the pages transcribed** — `unknown`, pages 10–18.

### "Independent assessment" when the methodology is undefined

2b, working from law-firm summaries, reported medium-risk systems face "sample audits or assessments by independent organizations". The primary text says, verbatim (Điều 10.5.b): *"Hệ thống trí tuệ nhân tạo có rủi ro trung bình được giám sát thông qua báo cáo, kiểm tra chọn mẫu hoặc đánh giá của tổ chức độc lập."*

The grammatical subject is the supervising authority, not the provider. Independent assessment is **one of three alternatives the regulator may choose**, alongside reports and sample inspection. It is not a duty a medium-risk provider must discharge, and nothing obliges anyone to buy one.

The only mandatory assessment is Điều 13, and it binds **high risk only**. Within high risk, third-party certification applies only to a Prime-Minister list that has not been issued (13.4); everything else may self-assess (13.2.b).

And the assessment's content is circular: Điều 13.2 defines *đánh giá sự phù hợp* as "việc xác nhận hệ thống trí tuệ nhân tạo đáp ứng các yêu cầu tại Điều 14". Điều 14 is **entirely process duties** — maintain a risk-management measure, govern training and test data, keep a technical dossier and activity log, design for human oversight, be transparent, explain on request, cooperate with inspection. **There is no performance, accuracy or safety threshold anywhere in it.** Nothing in the transcribed text mentions adversarial testing, red teaming, guardrails, jailbreaks, or language coverage.

So the undefined artifact is not undefined in an open-ended way that invites a first mover. It is defined as *conformity with a management process*, which is the ISO 42001 shape the 2026 SIG already adopted (`../review/market-check.md` §4) — and it is deferred in detail to a Government decree issued under Điều 9.3, 10.7, 11.6, 13.6. No decree, and no high-risk list, was found on the gazette portal this pass: `unknown — checked vanban.chinhphu.vn 2026-09-17`, where list pages return HTTP 500.

### Who in Vietnam must comply

An HCMC software firm that trains or fine-tunes a model for a foreign client is a *nhà phát triển* (Điều 3.3) and carries almost no direct duty — the duties attach to the *nhà cung cấp* who ships under its own brand, and the *bên triển khai* who operates it. A Vietnamese company running its own public chatbot is the *nhà cung cấp*, self-classifies, and on the statute's own wording lands in medium risk if users cannot tell they are talking to an AI (Điều 9.1.b) — or arguably in low risk precisely *because* Điều 11.1 makes it disclose. The statute does not settle this; Điều 9.3 hands it to the Government. **Assigning a consumer chatbot to medium risk remains an inference, not a finding.**

### Can two people sell into this?

| Route | Verdict | Why |
|---|---|---|
| Registered assessment body (Điều 13.5) | **No** | Registration conditions unpublished; accreditation business, field sales, against stated preference |
| Assessment/consulting service, unregistered | **Possible, not attractive** | Real: 13.2.b self-assessment support, 15.1.b explanation drafting. Relationship-sold, Vietnamese prices, the services lane pass 2 already attacked |
| Tool: dossier generator for Điều 10.1 / 14.1.c | **Buildable, unspecifiable today** | Contents deferred to an unissued decree; and it is compliance paperwork, not AI security |
| Tool: Điều 11 self-check — does our own product disclose AI, is generated media marked | **The one real overlap** | Small, in skill, testable. But marking format deferred to Chính phủ (11.2, 11.6); a checklist is hard to charge for |
| Not at all | **Defensible** | See below |

**The uncomfortable finding, stated plainly: the law is a real trigger and it points away from this project's competence.** Everything AISB teaches — jailbreaks, guardrails, checkpoint integrity, endpoint hardening, extraction — is absent from the statute. What the statute demands is classification, disclosure, labelling, dossiers and explanation. The nearest technical hooks are Điều 14.1.b (training and test-data quality governance) and Điều 12 (incident detection), both stated at a generality no tool satisfies. The trigger this repo spent three passes hunting exists, in the founders' own jurisdiction, and it belongs to a compliance-documentation business.

**Known vs inferred.** Known and filed: law number, name, adoption, effective date, the three tiers and their definitions, self-classification, the notification duty, the medium-risk supervision sentence and its subject, the high-risk-only scope of mandatory assessment, Điều 14's content, both transition deadlines. Inferred by this agent: that a consumer chatbot is medium risk; that "conformity with Điều 14" implies an ISO-42001-shaped artifact; that the absence of a decree means no product can be specified today. Unknown: penalties, the high-risk list, any decree, whether the Điều 8 portal exists.

---

## 3. Survivor audit — eleven products

Never-tested is not alive.

| # | Product | Status | Reason, one line |
|---|---|---|---|
| 1.1 | `refusal-diff` | **Dead** | `ams-scanner` 0.1.3 occupies it; incumbent-limit claim had no source |
| 1.2 | Trigger-backdoor susceptibility scan | **Never tested** | Prior art never re-checked; no buyer ever named |
| 1.3 | Publisher release-integrity report | **Never tested** | Nobody asks for it; `ams-scanner` output is the nearer artifact |
| 2.1 | Endpoint exposure grader | **Alive but changed, badly** | 3 of 5 checks already ship free — §4 |
| 2.2 | Extraction-cost estimator | **Alive but changed** | Absence holds; buyer unevidenced; dual-use still unresolved |
| 3.1 | ATLAS coverage matrix | **Dead** | MITRE's own `atlas-navigator` plus a 2026-06 data feed |
| 3.2 | Questionnaire evidence pack | **Alive but changed** | Only quoted trigger in the repo; its geography disqualification was overstated |
| 4.1 | Vietnamese guardrail benchmark | **Dead as pitched** | Not first, not novel; survives only as an unpublished blog post |
| 4.2 | Vietnamese guardrail regression CI | **Dead** | `promptfoo eval` in CI, free, MIT, OpenAI-owned |
| 4.3 | Train a Vietnamese moderation classifier | **Never tested** | Wrong skill; Qwen3Guard already claims 119 languages |
| 5.1 | Agent affordance linter | **Never tested** | Snyk `agent-scan` check list still unread after two waves assigned it |

Five dead, three alive-but-changed, three never-tested. **Nothing is untouched, and no survivor has a buyer.**

One correction that runs toward 3.2 and should be recorded rather than acted on. 2a disqualified the evidence pack on "no US market access", citing `vietnam-sg-access.md`. That file also says a merchant of record removes the entity question entirely at **5 % + 50¢ per transaction, $0 fixed, no entity at all**, and `scope.md` says the US-buyer question is "a business call, not a research finding. Note it, do not assume it." Selling a digital product to a US/EU buyer from HCMC is **priced, not blocked**. What is genuinely blocked is AWS Marketplace (Vietnam and Singapore both excluded) and direct US banking. 3.2's real problem is that it is a US/EU *relationship* sale, not that the money cannot move — and its final evidentiary link, whether an AI-testing questionnaire item has ever reached a Vietnamese supplier, is still unevidenced.

---

## 4. The endpoint exposure grader (N2 / 2.1), re-verified

2b left this as the only absence that survived falsification. Its evidence was one tool: garak's 43 probe modules. This wave attacked it across nuclei-templates, promptfoo, DeepTeam, Giskard, PyRIT, wallbreaker, vLLM's own docs, MITRE ATLAS, OWASP and the vendor AI-SPM lane. Raw: `raw/repick-endpoint-absence-pulls.md`, 22 pull blocks.

| Sub-claim | Verdict | Evidence |
|---|---|---|
| a. logprob / top_logprobs / top_k exposure grading | **Survives** | Zero hits across seven tools; ATLAS `AML.M0002` names it, ships `references: []` |
| b. Assistant-prefill acceptance | **Killed** | `JailbrokenAI/wallbreaker`, 1,459 stars, `tools/prefill.py`, `supports_native_prefill` |
| c. Control/special-token passthrough | **Killed twice** | promptfoo plugin `special-token-injection`; wallbreaker `chat_template_inject` |
| d. Unauth admin, `/v1/models`, CORS, rate limit, debug | **Killed decisively** | 8+ nuclei templates; `Ollama-Security-Auditor` covers most of (d) in one CLI |
| e. Extraction economics | **Survives** | Only a 2024 research supplement, 23 stars, no cost model, aimed at an emulator |

Strongest kill, verbatim from `nuclei-templates` `http/exposures/apis/vllm-openai-api-exposed.yaml`: *"Detects a vLLM inference server exposing its OpenAI-compatible API without authentication… vLLM does not enable an API key by default; it is only enforced when the server is started with `--api-key`."* `verified: true`.

Worse for the thesis than any single kill: wallbreaker's `chat_template_inject` already prints the grade the product would have sold — *"Hosted chat endpoints often escape literal control tokens - if it has no effect, the target re-tokenizes them as plain text."*

**Same error shape as §1.** 2b's claim was true about garak and false as a market claim, because the checked set was one tool and the sentence was written as if it were the market. The brace-list rule in §1 would have caught it.

**Who buys it.** Nobody named, in any pulled source. Candidate 1: a team running its own vLLM/Ollama gateway — which today runs `nuclei` free and gets (d), the part that actually causes breaches. Candidate 2: a pentest firm wanting a checklist — `nuclei` *is* the checklist, and `Ollama-Security-Auditor` is the CLI. **What triggers the purchase: nothing found.** `unknown — checked this repo's markets/ and customers/ layer 2026-09-17`.

**Does it connect to the AI Law? No.** Nothing in Điều 9–15 concerns serving-endpoint configuration. The nearest hook, Điều 14.1.a/b for high-risk providers, names no control. And (e) carries product 2.2's unresolved dual-use problem — a tool that measures extraction cost performs extraction — untouched since 2a.

**2.1 does not clear the bar. Do not build it.** What is left of it is two checks with no buyer, wrapped in a grade report, competing against free tools that already cover the three checks anyone asks about.

---

## 5. Recommendation

**Do not build. Run one three-day evidence test, pre-registered, and let its result decide between revive and stop.**

The test is deliberately **not** the Vietnamese guardrail measurement, even though `ungated-path.md` has made that nearly free. The measurement answers "is there a gap". Three waves have established that this project's problem is not finding gaps — every gap it found was occupied or unbought — and that its one real trigger arrived from the law, not from the tooling. The unknown worth three days is whether that trigger has a countable buyer yet.

### The test: does Law 134/2025/QH15 have a countable buyer?

Three desk probes, all free, all against Vietnamese primary sources.

**P1 — the Điều 8 portal.** Locate the *Cổng thông tin điện tử một cửa về trí tuệ nhân tạo* and count what it publishes. Điều 8.1 obliges it to receive classification notifications and to publish "thông tin về hệ thống trí tuệ nhân tạo, kết quả đánh giá sự phù hợp". If it is live, **the count of medium- and high-risk systems notified since 2026-03-01 is the addressable market, primary and filed** — the first hard demand number this project would ever have held. This wave probed six candidate hostnames plus `mst.gov.vn` and found nothing: `unknown — checked 2026-09-17, portal not located`. That probe was shallow, with no browser and no search budget.

**P2 — the decree and the list.** Find any Nghị định issued under Điều 9.3 / 10.7 / 11.6 / 13.6, and the Thủ tướng's *Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao* under Điều 13.4. If a decree exists, read what an assessment and a classification dossier must contain. If none exists, no compliance product is specifiable.

**P3 — the assessment-body register.** Find the register of *tổ chức đánh giá sự phù hợp* for AI under Điều 13.5. Its entry count is the competitor count; its conditions are the barrier to entry.

**Cost.** Two to three days of one person. Cash: zero. The real input is a browser (`vbpl.vn` and `phapluat.gov.vn` are now Next.js SPAs that return a loading shell to `curl`) and a WebSearch budget, both of which this session lacked. Boundary: reading published government registers, nothing else.

### Pre-registered decision rule — written now, not adjustable after

| Result | Decision |
|---|---|
| P1 portal live, **≥50** medium/high systems published, **and** P2 decree specifies assessment content | **Revive.** Build one artifact against the published spec — the Điều 10.1 / 14.1.c dossier generator, or the Điều 11 self-disclosure checker. One artifact, no platform |
| P1 live but **<50** entries, **or** P2 decree absent | **Hold.** Nothing is specifiable. Re-run P1–P3 on 2026-12-01 and 2027-01-15. Build nothing in between |
| P1 not locatable **and** P2 no decree **and** P3 no register | **Stop.** Six months after the law took force the state has published no counterpart, no spec, no register — and this project has no other live candidate |

The 50 threshold is chosen by this agent, not derived, and is stated so it cannot be moved later. Its justification: below roughly fifty notified systems, a compliance-artifact product cannot reach a dozen customers at any price, and this repo has no Vietnamese price point at all (`../review/market-check.md` §6b, UNRESOLVED). **A "Hold" is explicitly not a licence to build 2.1 or publish 4.1 as a consolation.**

### The case against this recommendation, at full strength

1. **It is more research from an agent asked to decide.** Three waves have produced zero buyers and eleven dead-or-unproven products. The most likely output of a fourth research wave is a twelfth. This project's actual pattern is research substituting for contact with a buyer, and my recommendation continues it.
2. **Even a "Revive" is a pivot.** It hands the team a compliance-forms product that uses none of AISB and none of the technical skill the brief was written around. The brief's own trap list said "find the trigger, not the fear" — the trigger was found and it is attached to a different business. Renaming that as a revive is generous.
3. **A better test exists and I am not recommending it.** AI Hay, Vbee and Filum AI are named in `vietnam-sg-access.md`; the founders are in HCMC. Three conversations answer P1–P3's business half — do you know about 134/2025/QH15, have you classified, would you pay — in a way no portal count can, and proximity is the one structural advantage this team has. I do not recommend it because it is outside an agent's remit and because `first-customers.md` rates its own channel evidence weakest in the repo. **A human should probably run it in parallel; on information per day it dominates my test.**
4. **I am declining a nearly-free measurement.** `ungated-path.md` has staged MIT-licensed paired VI/EN corpora (MultiJail 315 items, SEA-HELM 600 items, ViHOS 11,056 comments) and found Qwen3Guard-Gen-0.6B ungated and runnable on this machine. If the paired disagreement came back large, it would be the only published asset this project could put in front of a Vietnamese buyer, and distribution — not gap-finding — is the unsolved half. Declining it forfeits the cheapest visibility shot available. My counter: a benchmark that is not a first, on a corpus that is not the specified one, against guardrails no Vietnamese company runs, published by two unknown people, is a blog post with an unmeasured conversion rate — and AI Singapore can close the wedge with one `git revert` of a data-cleanup note.
5. **Stopping outright is defensible on this evidence and I did not choose it.** Nothing here clears the bar. The only reason not to stop today is that one probe, costing three days and no money, can turn the single largest correction in the project's evidence base into a countable number — and that number does not exist anywhere else.

---

## 6. What wave 2c designs

**Nothing.** There is no design work to do: no candidate has a buyer, and the one live opening has an unpublished specification. 2c should not open.

If a wave runs next it is an evidence wave, not a design wave: run P1–P3 from §5 with a browser and a WebSearch budget, write to `docs/explore/`, and append the decision-rule outcome verbatim to `STATE.md`. Design resumes only on a "Revive".

---

## Caveats

- The statute transcription is by this agent from rendered page images; the gazette PDF has no text layer. Pages 3 and 10–18 were not transcribed — penalties and the state-management chapter are `unknown`.
- Every absence verdict here is bounded as `checked <channel> 2026-09-17`, never "does not exist". §4 is itself the proof of what that bound is worth: 2b's surviving absence lost three of five sub-claims to one wider sweep.
- The vendor AI-SPM lane (Wiz, Prisma AIRS, Orca, AWS Inspector) went unreached — direct fetches 404'd and WebSearch was globally exhausted at 200/200. Sub-claim (a) could still fall to one of them.
- The 50-system threshold, the three-day estimate, the risk tier of a consumer chatbot, and the reading that "conformity with Điều 14" is an ISO-42001-shaped artifact are this agent's judgement, labelled, not sourced.
- No SEA price point and no buyer count for AI security testing exists anywhere in this repo. Every business argument above is therefore about direction, not magnitude.
- Nobody in this repo has yet read a HiddenLayer, Palo Alto Prisma AIRS, Cranium or Pillar product page, and the Azure/HiddenLayer exclusion sentence and the Enkrypt ranking are both still unverified. They no longer change the recommendation — 1.1 is dead on the `ams-scanner` finding alone — but they remain open.
