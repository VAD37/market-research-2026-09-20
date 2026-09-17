# Adversarial review of the wave-2a pick

Wave 2b, 2026-09-17. Target: `../plan/niche-and-solutions.md`. Evidence: `../../raw/review-guardrail-coverage-pulls.md`, `../../raw/review-buyer-trigger-pulls.md`, `../../raw/review-economics-pulls.md`, plus wave 1's `../explore/*` and `../../raw/*`, and the research layer (`../../../../docs/markets/ai-attack-defense-services.md`, `../../../../docs/findings/pass2-read.md`, `../../../../docs/competitors/ai-attack-defense-roster.md`).

Pass 2 already ran an adversarial pass on the services conclusion (`../../../../docs/findings/pass2-read.md`). It is cited here, not re-litigated. Attack line 5 below is new ground — Vietnam, not US/EU.

## Verdict table

| # | Claim as 2a stated it | Verdict | Reason |
|---|---|---|---|
| 1a | No shipping guardrail supports Vietnamese | **KILLED** | Azure AI Content Safety lists `vi` as Supported |
| 1b | Nothing detects a behaviorally tampered checkpoint | **PENDING** | see §1b |
| 1c | Nothing audits LLM serving-endpoint config exposure | **SURVIVES** | garak has no prefill, logprob, control-token probe |
| 2 | SEA-HELM's Vietnamese safety number is unknown | **KILLED** | SEA-HELM runs ViHSD on `vi`, 70 models, published |
| 2b | The benchmark would be the first Vietnamese number | **KILLED** | Same dataset, same n=1,000, already scored |
| 2c | Paired VI-vs-EN guardrail disagreement is unmeasured | **SURVIVES** | SEA-HELM `toxicity` has no English arm |
| 3 | Product 4.1/4.2 is a new build | **KILLED** | promptfoo ships language config plus three moderation providers |
| 4 | Vendor questionnaires reach a Vietnamese supplier | **SURVIVES** | HCMC firm states clients send security questionnaires |
| 4b | Those questionnaires carry AI red-team items | **UNRESOLVED** | SIG 2026 AI content is ISO 42001 governance, not testing |
| 5 | Nothing in SEA mandates AI testing | **KILLED** | Vietnam AI Law 134/2025/QH15 in force 2026-03-01 |
| 6a | Senior Vietnamese developer ≈ $27k/year | **SURVIVES** | ITviec: 54.9M VND/month, >8-year back-end band |
| 6b | What 4.x could charge, to how many buyers | **UNRESOLVED** | No SEA price point or buyer count exists anywhere |

---

## 1. The absence claims

### 1a — "no shipping guardrail supports Vietnamese" → KILLED

**As 2a stated it.** `../plan/niche-and-solutions.md` §1 N4: "Of the three most-cited shipping guardrails checked in `../explore/language-gap.md`, exactly one publishes a language list — Llama Guard 3 — and it stops at Thai." §4 case FOR argument 1: "One list exists and Vietnamese is not on it." §6 attack item 2 named Perspective API, OpenAI, Azure, AWS and SEA providers as never checked.

**Checked.** Microsoft Learn Azure AI Content Safety language-support page (WebFetch 2026-09-17); OpenAI moderation guide via the 301 to `developers.openai.com` (WebFetch 2026-09-17) and the openai.com launch post (403); Perspective API docs on three URLs (all returned a JS loading shell) plus the `conversationai/perspectiveapi` GitHub repo (`gh api`, 2026-09-17); AWS Bedrock Guardrails supported page (WebFetch 2026-09-17). Full text in `../../raw/review-guardrail-coverage-pulls.md` PULLs 1–4.

**Found.** Azure AI Content Safety publishes a four-column language table. Its Vietnamese row, verbatim: `| Vietnamese | vi |  | ✔️ |` — column 4 **Supported**, column 3 **Specially trained** blank. Text moderation and Prompt Shields auto-detect language, so no code need be passed. That is a second published language list, and Vietnamese is on it.

The page's own qualifier, verbatim: *"Other Azure AI Content Safety models have been specifically trained and tested on the following languages: Chinese, English, French, German, Spanish, Italian, Japanese, Portuguese. However, these features can work in many other languages, but the quality might vary. In all cases, you should do your own testing to ensure that it works for your application."*

Supporting checks: OpenAI's moderation docs contain **no language statement at all** — silence, like NeMo. Perspective API: Vietnamese absent from every list reached, but the primary docs page never rendered, so this is `unknown — checked developers.perspectiveapi.com and support.perspectiveapi.com 2026-09-17, JS shell only`. AWS: the "supported" page covers regions and models, not languages — `unknown — checked 2026-09-17`.

**Verdict: KILLED as stated.** A narrower claim survives and is stronger: *no guardrail vendor publishes a Vietnamese-specific quality number, and the one vendor that lists Vietnamese explicitly excludes it from its trained-and-tested set and instructs the customer to test it themselves.* Microsoft wrote the product's pitch. But 2a's argument that the absence of a list is the wedge is gone — there are two lists now, and the second one says yes.

### 1b — "nothing detects a behaviorally tampered checkpoint"

PENDING — filled below.

### 1c — "nothing audits LLM serving-endpoint configuration exposure" → SURVIVES

**As 2a stated it.** §5, third pick: "Its absence claim is the **lowest-confidence** in the file: rows 1.1/1.2/1.3 read 'NOTHING dedicated found'... and garak's probe set already touches 1.3."

**Checked.** `gh api repos/NVIDIA/garak/contents/garak/probes` and `/detectors`, plus GitHub code search restricted to `path:garak/probes`, 2026-09-17. `../../raw/review-guardrail-coverage-pulls.md` PULL 7.

**Found.** 43 probe modules, none of which is a serving-config probe. Code search: `"logprob"` 0 hits, `"control token"` 0 hits, `"top_k"` 0 hits; `"prefill"` 1 hit and it is `garak/probes/base.py`, not a probe. garak tests model behaviour, not gateway configuration.

**Verdict: SURVIVES.** And this inverts 2a's own ranking logic. 2a demoted product 2.1 partly because its absence claim was the weakest in the file; on direct inspection it is the **only** absence claim in this review that survived a falsification attempt intact. 2a scored a guess, not a check.

---

## 2. Does SEA-HELM already answer the question → KILLED, with one sliver surviving

**As 2a stated it.** §4 case AGAINST 3: "SEA-HELM... 'currently supports Filipino, Indonesian, Tamil, Thai, and Vietnamese' with a named Safety pillar. Not virgin ground." §6 attack item 9: "Wave 1 budgeted this out twice. If SEA-HELM already publishes a Vietnamese safety number, the settling measurement must be designed against it... and part of the 'first number' claim dies." §4 pre-registers the dataset as **ViHSD, stratified subset ~500–1,000 items**, label schema "`unknown — not pulled`".

**Checked.** `github.com/aisingapore/SEA-HELM` source via `gh api`, 2026-09-17: `seahelm_tasks/safety/toxicity_detection/config.yaml`, `seahelm_tasks/safety/safeguard/general/config.yaml` and its `data/`, `seahelm_tasks/task_config.yaml`. Hugging Face cards `aisingapore/Safety-Toxicity-Detection` and `sonlam1102/vihsd` (WebFetch 2026-09-17). `leaderboard.sea-lion.ai` (WebFetch 2026-09-17). Full text in `../../raw/review-guardrail-coverage-pulls.md` PULL 5.

**Found — three things, each worse for the pick than the last.**

**(i) SEA-HELM's Vietnamese safety task is ViHSD, at the same sample size 2a pre-registered.** `toxicity_detection/config.yaml` has an active `vi` entry pointing at `aisingapore/Safety-Toxicity-Detection`. That dataset card's source table names **ViHSD** as the Vietnamese source, at **1,000 examples**. The Vietnamese prompt's label set — Sạch / Công kích / Thù ghét — is ViHSD's CLEAN / OFFENSIVE / HATE. `task_config.yaml`'s active `vi` list contains `"toxicity"`. The leaderboard reports 61 open-weight and 9 closed-weight models. 2a's §4 dataset row and §6 item 8 ("ViHSD's label schema... never opened") are both closed: the schema is three-class HATE / OFFENSIVE / CLEAN, and AI Singapore has been scoring it for a year and a half.

**(ii) The paired EN/VI safety-classification task already exists in the repo, built and switched off.** `safeguard/general/` carries `en_general.jsonl` **and** `vi_general.jsonl` (plus id, ms, my, ta, th, tl) against a verbatim Llama Guard **S1–S14** taxonomy, scored by `F1AccMetric` on `normalized_accuracy`. That is 2a's Metric 1 — paired English/Vietnamese recall on a shipping guardrail's own category list — already implemented by AI Singapore. It is absent from every language's active task list, and its `data/README.md` says, in full: *"Omitted from the safeguard category pending further checks/data cleanup for the dataset (e.g. aegis2)."* 2a's §4 case-AGAINST 6 — "closable by an incumbent in one release" — is not hypothetical. The release is written. It is a data-cleanup ticket away.

**(iii) The dataset licence is contested.** `sonlam1102/vihsd` says **MIT**. AI Singapore's `Safety-Toxicity-Detection` source table says ViHSD is **CC BY-NC 4.0**. Recorded side by side, not reconciled. If NC is right, a commercial product built on ViHSD has a problem the plan never considered.

**What survives.** SEA-HELM prompts a **general LLM** to act as a classifier. It does not call shipping guardrail **products** — no Llama Guard 3 endpoint, no OpenAI moderation API, no Azure AI Content Safety, no Lakera. And the active `toxicity` task has languages `id, vi, th, tl, my, ms` and **no `en` arm**, so SEA-HELM publishes no VI-vs-EN paired comparison on the same items. 2a's Metric 2 (paired verdict disagreement, directional) is genuinely unmeasured.

The leaderboard's numeric Vietnamese toxicity score renders client-side and was not extracted: `unknown — checked leaderboard.sea-lion.ai 2026-09-17`.

**Verdict: KILLED** on "first number" and on dataset novelty. **SURVIVES**, narrowly, on "nobody has run shipping guardrail products on paired Vietnamese/English items." The wedge shrank from "Vietnamese safety is unmeasured" to "four commercial moderation endpoints have not been A/B'd on one public Vietnamese corpus." That is a true statement and a much smaller one.

---

## 3. The free competitor → the 80% path exists, and it is one YAML file

**As 2a stated it.** §5 case against the primary: "4.2 competes with promptfoo — free, OSS, 25,180 stars, OpenAI-owned since 2026-03-09." §2 row 4.2's killer: "promptfoo already does CI red-teaming; VI corpus is the only differentiator."

**Checked.** promptfoo docs in-repo via `gh api repos/promptfoo/promptfoo/contents/site/docs/...`, 2026-09-17: `red-team/configuration.md`, `configuration/expected-outputs/moderation.md`, `guides/testing-guardrails.md`. Code search `multilingual repo:promptfoo/promptfoo path:site/docs` → 19 hits. Full text in `../../raw/review-guardrail-coverage-pulls.md` PULL 6.

**Found.** Three pieces that compose into the proposed benchmark, all shipping, all free, all MIT.

1. **Language is a first-class config field**, not a strategy. Verbatim: *"The `language` field allows you to specify the language(s) for generated tests... This setting applies globally to all plugins and strategies, ensuring consistent multilingual testing across your entire red team evaluation."* It takes an array or ISO 639-1 codes, and the docs frame it exactly as 2a does — *"research shows that many LLMs have weaker safety protections in non-English languages"*, with a tip recommending low-resource languages. `language: ['Vietnamese', 'English']` is the paired condition, one line.
2. **The `moderation` assertion natively calls three of the guardrails 2a wants to compare.** Verbatim: *"Currently, this supports OpenAI's moderation model, Meta's LlamaGuard models (LlamaGuard 3 and 4) via Replicate, and Azure Content Safety API."* Two of 2a's three named targets, plus the one that killed §1a.
3. **There is a published guide for exactly this job.** `guides/testing-guardrails.md`, "Testing Guardrails Services Directly": *"Call the guardrail directly to tune thresholds, compare services, or test input and output policies independently."* It also supplies the pass/fail discipline 2a hand-designed — `not-guardrails` for items that must be flagged, `guardrails` for benign items, execution failures tracked as indeterminate rather than as `flagged: false`.

Note for the record: `promptfoo.dev/docs/red-team/strategies/multilingual/` 404s and the strategies index lists no multilingual entry. The capability is only visible from the repo. A user searching the public docs site the way wave 1 searched would have missed it too.

**What promptfoo does not give you.** Its `language` field *generates* tests in a language; it does not load a human-labeled corpus and compute recall against ground truth. ViHSD ingestion, the English machine-translation arm, back-translation fidelity filtering, and the recall arithmetic are still the user's to write. That is a CSV, a YAML, and a scoring script — days for one person, and no part of it is a tool anyone would install.

**Verdict: KILLED for product 4.2.** A Vietnamese guardrail regression CI gate is `promptfoo eval` against a Vietnamese test file, in CI, today, free, from the company that owns the category. **KILLED as a build for 4.1.** What remains of 4.1 is a dataset, a config, and a write-up — a publication, which is what 2a said it was, but the plan's "1–2 wk" build estimate and its "defensible because: first measured Vietnamese number" column are both now wrong.

---

## 4. The buyer chain → it reaches Vietnam; the AI half of it does not

**As 2a stated it.** §3 trigger table, row 4.1/4.2: "Foreign client's vendor security questionnaire flowing downstream to a Vietnamese supplier... The downstream-questionnaire chain is **`unknown — not pulled`**." §6 item 7: "Zero evidence either way. This is the stated trigger for the primary pick."

**Checked.** Shared Assessments' own 2026 SIG page (Entra sign-in wall), Mitratech's SIG 2026 summary dated 2026-03-05, CSA's AI Controls Matrix artifact page, a third-party AICM coverage analysis, one Vietnamese software company's own compliance post dated 2026-06-08, and WebSearch on Vietnamese outsourcing certifications — all 2026-09-17. Full text in `../../raw/review-buyer-trigger-pulls.md` PULLs 1–3.

**Found — the chain reaches, the AI content is governance not testing.**

A Vietnamese supplier confirms receiving questionnaires, company-stated. 724SOFTWARE (Hanoi and HCMC, post dated 2026-06-08), verbatim: *"when a Fintech or Healthcare client sends a vendor security questionnaire asking about secure SDLC controls, an ISO 27001 certified team can map answers directly to audited Annex A controls rather than making informal assertions."* That settles the mechanism: foreign-client security questionnaires do land on Vietnamese software firms, and those firms pre-buy artifacts (ISO 27001, SOC 2 Type II, CMMI) to answer them.

What the questionnaires now ask about AI is **management-system governance**. The 2026 SIG's headline AI change, verbatim from Mitratech: *"The most significant addition is the comprehensive mapping to ISO 42001, the international standard for AI Management Systems"* and *"assess vendors on the whole AI lifecycle — from data collection and model training to deployment and bias monitoring."* Red teaming, adversarial testing and guardrails appear nowhere on that page.

The one AI-specific questionnaire that may carry testing items is CSA's **AI-CAIQ**, verbatim from CSA: *"A set of questions that map to the AICM. These questions can guide organizations in performing a self-assessment or an evaluation of third-party vendors."* AICM: released 2025-07-09, updated 2025-10-30, "243 control objectives distributed across 18 security domains." A third-party coverage analysis attributes AI-red-teaming language to **AIS-13** and AI-extended pen testing to **TVM-06**; the AICM workbook itself is registration-gated and was not obtained. `unknown — primary AICM control text not pulled 2026-09-17`.

**A representation finding against wave 1.** `../../../../docs/markets/ai-attack-defense-services.md` line 47 says vendor security questionnaires *"reportedly"* ask about independent AI red teaming, and flags *"Could not confirm CSA's CAIQ has such a field: `unknown — checked 2026-09-16`."* `../explore/sea-compliance-triggers.md` re-quotes that passage with the "reportedly" and the unknown both dropped. 2a then inherited the firmer version. Small, but it is the exact mechanism by which a hedge becomes a fact.

**Verdict: chain SURVIVES, AI content UNRESOLVED.** The pick's stated trigger has evidence for every link except the last one — that an AI red-teaming or guardrail-testing item has ever reached a Vietnamese supplier. Nothing found says it has. On this evidence alone, 4.x's non-regulatory trigger is reputation. But see §5.

---

## 5. Vietnam's own regime → the demand premise is wrong, and wrong in the pick's favour

**As 2a stated it.** §3, opening: "`../explore/sea-compliance-triggers.md`: **nothing in Southeast Asia mandates AI red-teaming or security testing as of 2026-09-17.**" §3 trigger table: "Vietnam's own content-control regime applied to a public-facing Vietnamese chatbot — **`unknown — not pulled`**. Highest-value open question in this file." Wave 1 characterised Vietnam's AI Law, carried forward unverified from `pass3-read.md`, as a "presence/representative requirement — **not a testing mandate**."

**Checked.** Tilleke & Gibbins and Baker McKenzie readings of Law No. 134/2025/QH15; Tilleke and Vietnam Briefing on Decree 147/2024/ND-CP; WebSearch on the Digital Technology Industry Law. All WebFetch/WebSearch 2026-09-17. `thuvienphapluat.vn` primary text returned 403. Full text in `../../raw/review-buyer-trigger-pulls.md` PULLs 4–5.

**Found.** Vietnam passed a standalone **Law on Artificial Intelligence, No. 134/2025/QH15**, adopted **2025-12-10**, **in force 2026-03-01** — six and a half months before this review. Both law firms report the same structure:

| Tier | Definition, verbatim (Tilleke) | Supervision, verbatim (Baker McKenzie) |
|---|---|---|
| High-risk | "may cause significant harm to life, health, or the lawful rights and interests" | "periodic audits and pre-market conformity assessments" |
| Medium-risk | "may have the potential to confuse, influence, or manipulate users" | "sample audits or assessments by independent organizations" |
| Low-risk | all remaining systems | "Monitored for incidents and complaints" |

High-risk providers must additionally "Maintain commercial presence or authorized representatives in Vietnam", "Undergo pre-market conformity certification (when specified by Prime Minister)" and "Submit to regular audits and testing procedures". Transparency obligations reach any public-facing system: users must be able to "recognize when they are interacting with an AI system", and deployers publishing AI-generated content must give "clear disclosure and visible labeling". Scope covers "Vietnamese organizations and individuals, as well as foreign entities that participate in AI-related activities within Vietnam". Existing systems get a **12-month** grace period, **18 months** for health, education and finance — so the compliance wall for a deployed Vietnamese chatbot falls around **2027-03-01**.

Separately, **Decree 147/2024/ND-CP** (in force 2024-12-25) puts content liability on providers of online information services: "Inspect, monitor, prevent, and remove violating content, services, and applications"; removal within "24 hours from the time of a request from the relevant authority"; complaints within "48 hours"; self-reporting within "24 hours" for content violating Article 8 of the Cybersecurity Law; enforcement by technical blocking plus administrative penalties. Neither AI nor chatbots are named anywhere in it.

**What this does not establish.** No source reached assigns a risk tier to a general-purpose public consumer chatbot — medium-risk fits the wording on its face and that is an inference, not a finding. No source says an audit or conformity assessment must include adversarial, safety or guardrail testing; both firms say the evaluation methodology is deferred to implementing regulations not yet issued. Nothing mentions language coverage as an audit criterion. And both readings are law-firm secondary — the statute text was not fetched.

**Verdict: KILLED.** The sentence 2a's entire §3 is built on — that no Southeast Asian regime mandates AI testing — is false as of 2026-03-01, in the pick's own jurisdiction, for the pick's own buyer. This is the largest single correction in the review, and wave 1's weakest-sourced file is where it hid.

The honest reading is narrower than a sales pitch. Vietnam mandates **independent assessment and periodic audit** for medium- and high-risk AI without yet defining what the assessment contains. That is a trigger with an undefined artifact. It is the best available position for whoever defines the artifact first, and it is not the same thing as a buyer with a budget line today.

---

## 6. The pick's own economics

**As 2a stated it.** §4 case AGAINST 4: "ITviec's 2025–2026 report puts senior Vietnamese backend salaries at ~54.9M VND/month (~$27,000/yr). A Vietnamese buyer will not pay the $8k–$50k band."

**Checked.** ITviec report page, WebFetch 2026-09-17; plus a WebSearch cross-read. `../../raw/review-economics-pulls.md`.

**Found.** The figure is real and correctly transcribed. ITviec "Vietnam IT Salary & Recruitment Market Report 2025-2026", n = **1,839**, surveyed 2025-05-27 to 2025-07-31 and 2025-10-21 to 2025-11-11. Back-end Developer: 3–4 yrs 30.1M, 5–8 yrs 39.9M, **>8 yrs 54.9M VND/month**. Three corrections to how 2a used it: it is the **>8-year** band, not "senior" generically; it is **gross salary**, excluding employer statutory contributions; and the report publishes **no USD conversion**. 54.9M × 12 = **658.8M VND/year**; the dollar figure depends on an FX rate not pulled — ~$27,000 at 24,400 VND/USD, ~$25,000 at 26,300. `unknown — VND/USD rate not pulled 2026-09-17`.

**What it could charge, to how many.** Neither is derivable. No SEA price point for AI security testing exists in any pulled source in this repo — `../plan/niche-and-solutions.md` says so in its own caveats and this review confirms it. No census or count of Vietnamese companies operating a public Vietnamese-language chatbot has ever been pulled; the research layer names three companies, which is a list, not a market.

**Verdict: 6a SURVIVES** with the three corrections. **6b UNRESOLVED** — `unknown — checked this repo's markets/ and customers/ layer 2026-09-17`. The pricing-ceiling argument stands as an argument and cannot be turned into a number.

---

## Does the pick stand?

**Not as argued.** Every load-bearing pillar under product 4.1 moved:

- Its absence premise is falsified — Azure publishes Vietnamese support (§1a).
- Its "first Vietnamese number" claim is falsified — SEA-HELM has scored ViHSD across 70 models (§2).
- Its paired EN/VI design is already implemented in SEA-HELM's repo and merely switched off (§2).
- Its build is a promptfoo config, and its CI sibling 4.2 is dead on arrival (§3).
- Its stated trigger is unevidenced at the final link (§4).

**It does not fall to the fallback either.** Product 1.1's trigger is still "they should care" by 2a's own admission, and product 2.1's absence claim is the only one in this file that survived a direct falsification attempt (§1c) — which is the opposite of the confidence ordering 2a used to rank them.

**What actually survives is the outcome 2a pre-registered as its consolation branch.** §4's decision rule reserves "repoint to a published guardrail picker" for an ambiguous measurement. The evidence now puts the pick there **before** the measurement runs: the only unmeasured question left is whether four commercial moderation endpoints disagree on paired Vietnamese and English items, and Microsoft has already written the reason a buyer would want to know — *"the quality might vary. In all cases, you should do your own testing."*

Against that, one thing moved in the pick's favour and it is the largest finding here: **Vietnam has a live AI law with an independent-assessment obligation and an undefined assessment artifact, biting deployed systems around 2027-03-01** (§5). That is a real trigger in the one jurisdiction this team can reach, and it was invisible to wave 1.

---

## Constraints for wave 2c

Not a design. The boundaries anything 2c designs has to sit inside.

1. **Do not claim a first.** SEA-HELM has published Vietnamese ViHSD safety scores for 61 open-weight and 9 closed-weight models since 2025-02. Anything 2c ships cites SEA-HELM and positions against it, or it is wrong on its first page.
2. **The measured object is the guardrail product, not the model.** SEA-HELM's gap is that it prompts general LLMs as classifiers. The unmeasured territory is commercial moderation endpoints — Llama Guard 3 8B, OpenAI `omni-moderation-latest`, **Azure AI Content Safety** (now mandatory, it is the one that killed the absence claim), Lakera Guard. Four, not three.
3. **The paired condition is the only novel half.** SEA-HELM's active `toxicity` task has no English arm. Metric 2 — directional VI-pass / EN-flag disagreement on identical items — is the measurement nobody has published. Metric 1 alone duplicates work already done.
4. **Build on promptfoo, do not rebuild it.** `redteam.language`, the `moderation` assertion, and `guardrails` / `not-guardrails` already exist and already cover three of the four endpoints. Writing a harness instead of a config is rework, and it is visible rework to anyone who reads the docs.
5. **Resolve the ViHSD licence before sampling.** MIT (`sonlam1102/vihsd`) versus CC BY-NC 4.0 (AI Singapore's source table). If NC governs, a commercial derivative is blocked and the artifact must stay a publication.
6. **Budget for SEA-HELM turning `safeguard_general` back on.** The EN/VI paired files are committed and blocked only by a data-cleanup note. Anything whose value depends on that task staying off has a countdown on it.
7. **Assume no compliance artifact is specified.** Vietnam's AI Law mandates independent assessment for medium- and high-risk AI and defers the methodology to implementing regulations. 2c may design toward that gap; it may not assert the law requires guardrail testing, because no source says so.
8. **Price is unknowable, so do not design around one.** No SEA price point and no buyer count exist. A design whose viability depends on a specific price or a specific buyer count is untestable on this evidence.
9. **The boundary holds unchanged.** Public academic dataset, defenses under test, operator-controlled endpoints only. Product 2.2's dual-use problem is untouched by this review and remains open.

---

## Caveats

- Every absence verdict here is bounded the same way wave 1's were: "checked channel X on 2026-09-17", never "does not exist". §1a is the proof — one unchecked vendor page inverted the claim.
- §4 and §5 rest entirely on law-firm, consultancy and vendor secondary sources. No primary statute text (Law 134/2025/QH15, Decree 147, Article 8 of the Cybersecurity Law) and no primary questionnaire document (SIG workbook, AI-CAIQ, AICM) was obtained. Both gates — `thuvienphapluat.vn` 403, Shared Assessments Entra wall, CSA registration — are browser-solvable by a later pass.
- The risk tier of a general consumer chatbot under Vietnam's AI Law is an inference from the medium-risk wording, not a finding.
- The SEA-HELM Vietnamese toxicity **score** was not extracted; the leaderboard renders client-side. Only the task's existence, dataset and configuration are confirmed.
- The ViHSD licence conflict is recorded unresolved and unaveraged.
- The USD conversion of 54.9M VND/month is a range, not a figure, because no FX rate was pulled.
- Perspective API's Vietnamese status is unconfirmed — its docs never rendered across three fetches.
- This review attacks claims. It does not redesign the product and proposes no new candidate, per its brief.
