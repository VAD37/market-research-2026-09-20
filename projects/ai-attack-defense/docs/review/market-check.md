# Adversarial review of the wave-2a pick

Wave 2b, 2026-09-17. Target: `../plan/niche-and-solutions.md`. Evidence: `../../raw/review-guardrail-coverage-pulls.md`, `../../raw/review-buyer-trigger-pulls.md`, `../../raw/review-economics-pulls.md`, `../../raw/review-traceability-audit.md`, `../../raw/review-checkpoint-tamper-pulls.md`, plus wave 1's `../explore/*` and `../../raw/*` — including `../explore/dataset-baselines.md`, which landed from wave 1c mid-review and is used here — and the research layer (`../../../../docs/markets/ai-attack-defense-services.md`, `../../../../docs/findings/pass2-read.md`, `../../../../docs/competitors/ai-attack-defense-roster.md`).

Pass 2 already ran an adversarial pass on the services conclusion (`../../../../docs/findings/pass2-read.md`). It is cited here, not re-litigated. Attack line 5 below is new ground — Vietnam, not US/EU.

## Verdict table

| # | Claim as 2a stated it | Verdict | Reason |
|---|---|---|---|
| 1a | No shipping guardrail supports Vietnamese | **KILLED** | Azure AI Content Safety lists `vi` as Supported |
| 1b | HiddenLayer's limit is documented, not assumed | **KILLED** | No raw file supports it; only a format list |
| 1b' | Nothing detects a behaviorally tampered checkpoint | **KILLED** | `ams-scanner` 0.1.3 detects abliteration against claimed base |
| 1c | Nothing audits LLM serving-endpoint config exposure | **SURVIVES** | garak has no prefill, logprob, control-token probe |
| 1d | MITRE ATLAS has no interactive tool layer | **WEAKENED** | `mitre-atlas/atlas-navigator` exists; stale code, current data |
| 2 | SEA-HELM's Vietnamese safety number is unknown | **KILLED** | SEA-HELM runs ViHSD on `vi`, 70 models, published |
| 2b | The benchmark would be the first Vietnamese number | **KILLED** | Same dataset, same n=1,000, already scored |
| 2c | Paired VI-vs-EN guardrail disagreement is unmeasured | **SURVIVES** | SEA-HELM `toxicity` has no English arm |
| 2d | ViHSD is a public dataset, cited as arXiv 2103.10069 | **KILLED** | Wrong arXiv ID; licence contested; official copy gated |
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

Two further data points from wave 1c's independent re-fetch (`../explore/dataset-baselines.md`, 2026-09-17), which matched wave 1's quotes word for word: Llama Guard 3's machine-readable Hugging Face `cardData.language` tag is **`["en"]` only**, narrower than its own 8-language prose claim; and ShieldGemma 9B is **explicitly English-only** — "available in English with open weights". Both add to the absence side. Azure still kills the claim as stated.

Supporting checks: OpenAI's moderation docs contain **no language statement at all** — silence, like NeMo. Perspective API: Vietnamese absent from every list reached, but the primary docs page never rendered, so this is `unknown — checked developers.perspectiveapi.com and support.perspectiveapi.com 2026-09-17, JS shell only`. AWS: the "supported" page covers regions and models, not languages — `unknown — checked 2026-09-17`.

**Verdict: KILLED as stated.** A narrower claim survives and is stronger: *no guardrail vendor publishes a Vietnamese-specific quality number, and the one vendor that lists Vietnamese explicitly excludes it from its trained-and-tested set and instructs the customer to test it themselves.* Microsoft wrote the product's pitch. But 2a's argument that the absence of a list is the wedge is gone — there are two lists now, and the second one says yes.

### 1b — "nothing detects a behaviorally tampered checkpoint" → KILLED, and it never rested on evidence either

**As 2a stated it.** §5 Fallback, case for: "The cleanest absence claim wave 1 produced, and the one with a named incumbent whose limit is **documented rather than assumed**: HiddenLayer scans file formats, not behavior." §6 attack item 1: "The fallback rests entirely on this."

**Checked.** Two greps, 2026-09-17, recorded in `../../raw/review-traceability-audit.md` AUDIT 1: `HiddenLayer|ModelScanner` across this project's `raw/`, and `modelscanner|model scanner` across the repo-root `docs/` tree. A parallel falsification sweep of vendor product pages, cloud model catalogs, OSS and benchmarks returned late; its load-bearing items were **re-pulled directly by this review** and are recorded in `../../raw/review-checkpoint-tamper-pulls.md`, with the items that could not be re-pulled labelled AGENT-REPORTED, UNVERIFIED there.

**Found — the chain has no bottom.** This project's `raw/` mentions HiddenLayer **zero times**. The only pulled source anywhere in the repo is `../../../../docs/raw/ai-attack-defense-pulls.md:338`, verbatim: *"HiddenLayer's ModelScanner supports 35+ formats including PyTorch, TensorFlow, ONNX, Keras, GGUF, pickle, and safetensors."*

That is a list of supported **file formats**. It says nothing about behavioral weight edits — it neither asserts nor excludes them. The exclusion is an inference drawn from a format list in `../explore/aisb-inventory.md` row 5.1, which cites nothing; `../explore/shipping-tools.md` then labels that same inference **"Confirmed elsewhere"** and cites row 5.1 back; `../plan/niche-and-solutions.md` then calls it **"documented rather than assumed."** Format list → inference → "confirmed" → "documented", with no evidence added at any step.

Two aggravating facts. `../../../../docs/competitors/ai-attack-defense-roster.md` lists HiddenLayer's products as "**Model scan, red team, runtime**" — three lines, of which the explore layer examined one, and the two unexamined ones are where behavioral detection would live if it exists. And row 5.2's "HiddenLayer claims platform-level detection, contact-sales, unverified" likewise traces to no raw file.

**Verdict: KILLED, twice over.** A free Apache-2.0 tool from a Google Cloud org does the thing, and has since 2026-04-28. Separately, and independently damning, 2a's stated reason for preferring this fallback — that its incumbent's limit is *documented* — is false: it is assumed, from a marketing format list, via two files citing each other. The fallback was ranked above product 2.1 on an evidentiary distinction that does not exist, and the gap it was built for is occupied.

**And then the sweep came back with a product.** `ams-scanner` 0.1.3, PyPI, released **2026-04-28**, Apache-2.0, from **`GoogleCloudPlatform/activation-model-scanner`** (created 2026-03-23, pushed 2026-08-27, 33 stars, 9 forks, not archived). Both channels re-pulled directly by this review on 2026-09-17; `../../raw/review-checkpoint-tamper-pulls.md` PULL 1. PyPI summary, verbatim: *"Activation-based Model Scanner - Verify LLM safety via activation pattern analysis"*. Its tier-2 mode, verbatim: *"Verifies a model matches its claimed identity...Catches subtle modifications, abliteration, and weight substitution."* README, verbatim: *"AMS detects whether a model has intact safety training by measuring the separation of safety-relevant concepts in the model's activation space. Models with removed or degraded safety training (e.g., 'uncensored' fine-tunes, abliterated models) show collapsed safety directions that AMS can detect in seconds."*

That is product 1.1, built, published, free, by a Google Cloud organisation, five months before this review. Its own README also says: *"This is not an officially supported Google product."* 33 stars and an 0.1.x version number are not a market — but "nothing exists" is no longer the claim, and "we thought of it first" is gone.

**Two more verified items.** DeepTeam's open-weight guide already instructs the reader to do 1.1's job by hand — verbatim: *"**Compare against the base model.** Run the same assessment against the original model to identify what the fine-tune changed"*, under *"Fine-tuning can silently remove safety behaviors even when the training data is benign."* And the attack side is a mass-market tool: `p-e-w/heretic`, "Fully automatic censorship removal for language models", **31,632 stars**, pushed 2026-09-05. The defender's tool has 33 stars; the attacker's has 31,632.

**Not verified, and load-bearing.** The sweep reports Azure AI Foundry's HiddenLayer integration stating that *"Customers' fine-tuned models, models imported directly from Hugging Face, and proprietary models offered as-a-Service… are not scanned by HiddenLayer today"* — which, if true, is the quote wave 1 needed and never had. The page would not render on two attempts. It also reports Enkrypt AI's leaderboard rating `failspy/Llama-3-8B-Instruct-MopeyMule` — a model whose own card says verbatim *"this model is the same weights as Llama-3-8B-Instruct, however with a grumpy/irritable 'direction' induced and amplified"* using *"the orthogonalization technique described in this blog post from Andy Arditi et al."* (card verified by this review) — **50 places safer than the unmodified Meta checkpoint**, on a schema with no lineage field. The model card is verified; the ranking is not — the Space returned HTTP 401. `unknown — checked 2026-09-17, 401`.

**Nobody in this repo has ever read a HiddenLayer product page.** Not wave 1, not wave 2a, not this review. That is the first thing to do before anyone builds product 1.1 — along with re-pulling the Azure/HiddenLayer exclusion sentence and the Enkrypt ranking, because between them they are the difference between "the incumbents miss this" being evidence and being a hope.

### 1c — "nothing audits LLM serving-endpoint configuration exposure" → SURVIVES

**As 2a stated it.** §5, third pick: "Its absence claim is the **lowest-confidence** in the file: rows 1.1/1.2/1.3 read 'NOTHING dedicated found'... and garak's probe set already touches 1.3."

**Checked.** `gh api repos/NVIDIA/garak/contents/garak/probes` and `/detectors`, plus GitHub code search restricted to `path:garak/probes`, 2026-09-17. `../../raw/review-guardrail-coverage-pulls.md` PULL 7.

**Found.** 43 probe modules, none of which is a serving-config probe. Code search: `"logprob"` 0 hits, `"control token"` 0 hits, `"top_k"` 0 hits; `"prefill"` 1 hit and it is `garak/probes/base.py`, not a probe. garak tests model behaviour, not gateway configuration.

**Verdict: SURVIVES.** And this inverts 2a's own ranking logic.

### 1d — "MITRE ATLAS has no tool layer" → WEAKENED, and the plan contradicts itself

**As 2a stated it.** §1 N3: "MITRE ATLAS (16 tactics, 84 techniques) has **no maintained interactive tool layer** — no ATT&CK-Navigator equivalent." Same wording in `../explore/shipping-tools.md`, which calls it "the cleanest 'the standard exists, the product around it doesn't' gap found in this pass."

**Checked.** `gh api orgs/mitre-atlas/repos`, 2026-09-17. `../../raw/review-guardrail-coverage-pulls.md` PULL 8.

**Found.** A repo named **`atlas-navigator`** published by MITRE ATLAS itself, described verbatim as "Web app that provides basic navigation and annotation of ATLAS matrices, based on the ATT&CK Navigator". 13 stars, last pushed **2024-06-24**. Its data feed `atlas-navigator-data` — "Scripts and outputs for ATLAS data in STIX JSON and **ATT&CK Navigator layer formats**" — was pushed **2026-06-24**, 34 stars. The org also ships `atlas-knowledge-base-agent` (pushed 2026-08-05, 66 stars) and `arsenal`, a CALDERA plugin for adversary emulation of AI-enabled systems (126 stars).

**Verdict: WEAKENED.** The thing wave 1 said does not exist exists, is named that, and is MITRE's. Only the word "maintained" is defensible — the web app is 27 months stale while its data pipeline is three months old. Note also that 2a's own §2 row 3.1 lists the killer as "MITRE ships a Navigator; it is a UI over free data", directly contradicting §1 N3 two pages earlier. The plan had the right answer in one table and the wrong one in another. 2a demoted product 2.1 partly because its absence claim was the weakest in the file; on direct inspection it is the **only** absence claim in this review that survived a falsification attempt intact. 2a scored a guess, not a check.

---

## 2. Does SEA-HELM already answer the question → KILLED, with one sliver surviving

**As 2a stated it.** §4 case AGAINST 3: "SEA-HELM... 'currently supports Filipino, Indonesian, Tamil, Thai, and Vietnamese' with a named Safety pillar. Not virgin ground." §6 attack item 9: "Wave 1 budgeted this out twice. If SEA-HELM already publishes a Vietnamese safety number, the settling measurement must be designed against it... and part of the 'first number' claim dies." §4 pre-registers the dataset as **ViHSD, stratified subset ~500–1,000 items**, label schema "`unknown — not pulled`".

**Checked.** `github.com/aisingapore/SEA-HELM` source via `gh api`, 2026-09-17: `seahelm_tasks/safety/toxicity_detection/config.yaml`, `seahelm_tasks/safety/safeguard/general/config.yaml` and its `data/`, `seahelm_tasks/task_config.yaml`. Hugging Face cards `aisingapore/Safety-Toxicity-Detection` and `sonlam1102/vihsd` (WebFetch 2026-09-17). `leaderboard.sea-lion.ai` (WebFetch 2026-09-17). Full text in `../../raw/review-guardrail-coverage-pulls.md` PULL 5.

**Found — three things, each worse for the pick than the last.**

**(i) SEA-HELM's Vietnamese safety task is ViHSD, at the same sample size 2a pre-registered.** `toxicity_detection/config.yaml` has an active `vi` entry pointing at `aisingapore/Safety-Toxicity-Detection`. That dataset card's source table names **ViHSD** as the Vietnamese source, at **1,000 examples**. The Vietnamese prompt's label set — Sạch / Công kích / Thù ghét — is ViHSD's CLEAN / OFFENSIVE / HATE. `task_config.yaml`'s active `vi` list contains `"toxicity"`. The leaderboard reports 61 open-weight and 9 closed-weight models. 2a's §4 dataset row and §6 item 8 ("ViHSD's label schema... never opened") are both closed: the schema is three-class HATE / OFFENSIVE / CLEAN, and AI Singapore has been scoring it for a year and a half.

**(ii) The paired EN/VI safety-classification task already exists in the repo, built and switched off.** `safeguard/general/` carries `en_general.jsonl` **and** `vi_general.jsonl` (plus id, ms, my, ta, th, tl) against a verbatim Llama Guard **S1–S14** taxonomy, scored by `F1AccMetric` on `normalized_accuracy`. That is 2a's Metric 1 — paired English/Vietnamese recall on a shipping guardrail's own category list — already implemented by AI Singapore. It is absent from every language's active task list, and its `data/README.md` says, in full: *"Omitted from the safeguard category pending further checks/data cleanup for the dataset (e.g. aegis2)."* 2a's §4 case-AGAINST 6 — "closable by an incumbent in one release" — is not hypothetical. The release is written. It is a data-cleanup ticket away.

**(iii) The dataset licence is contested three ways, and the official channel is gated.** `sonlam1102/vihsd` says **MIT**. AI Singapore's `Safety-Toxicity-Detection` source table says ViHSD is **CC BY-NC 4.0**. `../explore/dataset-baselines.md` (wave 1c, 2026-09-17) found the official UIT channel requires a signed agreement, verbatim: *"Please contact us via email: sonlt@uit.edu.vn (Mr. Son Luu) to sign the corpus user agreement and then receive the corpus"*, and the official `uitnlp/vihsd` Hugging Face repo is `"gated":"auto"`. Three attributions, recorded side by side and not averaged. Two of them block a commercial derivative; the third permits it. The plan assumed the dataset was simply public.

**(iv) 2a cites the wrong paper for its own dataset.** Wave 1c established that arXiv **2103.10069** — the ID carried in `../explore/language-gap.md` and repeated twice in `../plan/niche-and-solutions.md` §4 and §5 — is **UIT-ViCTSD**, a different dataset. ViHSD is arXiv **2103.11528**. The plan's settling measurement names a dataset by an identifier that points somewhere else. Not fatal, and 1c has already corrected it downstream, but it is the kind of error that survives into a published benchmark's references.

**Convergence with wave 1c.** `../explore/dataset-baselines.md` reached the same answer independently and states it more conservatively: *"does SEA-HELM already answer the question? No... narrower than 'first Vietnamese safety number ever' (SEA-HELM already has Vietnamese safety numbers, for a different object) but intact as 'first test of whether shipping guardrail products hold on Vietnamese vs. English translation.'"* This review agrees on the surviving claim and goes one step further on the risk: 1c reports that `safeguard/general`'s `vi_general.jsonl` is **machine-translated NVIDIA Aegis2** against the Llama Guard S1–S14 taxonomy — i.e. the same English source items, rendered into Vietnamese by machine translation, which is exactly 2a's own paired design. AI Singapore has not published a paired comparison, but it holds both halves of one in a repo, disabled by a cleanup note.

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

4. **The corpus loads as a CSV.** Verbatim: *"promptfoo supports a special CSV file format"*, config `tests: file://tests.csv`; test files may also be YAML/JSON, JSONL, TS/JS, Google Sheets or Azure Blob. ViHSD is a labeled CSV.

**The concrete path, stated plainly.** Download ViHSD; add an English machine-translation column; `tests: file://vihsd.csv`; assert `not-moderation` against `openai`, against `replicate:moderation:meta/llama-guard-3-8b`, and against Azure AI Content Safety; set `redteam.language` if generated adversarial items are wanted alongside the labeled ones; `promptfoo eval --no-cache -o output.json`. No new tool. That is 2a's proposed benchmark, minus the recall arithmetic.

**This also closes an open item wave 1c could not.** `../explore/dataset-baselines.md` reports Llama Guard 3 8B is gated on Meta's **manual-approval** tier, that 4-bit is the only precision that plausibly fits this machine's 6,668 MiB free VRAM, and that "No hosted alternative with confirmed live pricing was found (Together: 'not available... launching soon'; OpenRouter: not found in fetched catalog; Groq: pricing page unreachable)." promptfoo's moderation docs name a working hosted route verbatim: `provider: 'replicate:moderation:meta/llama-guard-3-8b:146d1220d447cdcc639bc17c5f6137416042abee6ae153a2615e6ef5749205c8'`, with LlamaGuard 4 as the Replicate default. Replicate pricing was not pulled — `unknown — checked 2026-09-17`.

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

**And the fallback is gone.** 2a ranked product 1.1 above product 2.1 because 1.1's incumbent limit was "documented rather than assumed". It is not documented — it traces to a vendor format list and two files citing each other. Worse, the gap itself is occupied:  ships abliteration detection against a claimed base, free, from a Google Cloud org (§1b). Meanwhile 2.1's absence claim, which 2a called the file's lowest-confidence, is the only absence in this review that survived a direct falsification attempt (§1c). 2a's own swap rule in §5 — "If 2b finds 2.1's absence claim holds and 1.1's does not, the fallback should swap" — fires on both halves at once: **the fallback swaps to product 2.1, the endpoint exposure grader.** Note what that does not buy: 2.1's trigger is still inferred, and it was never the reason it lost.

**What actually survives is the outcome 2a pre-registered as its consolation branch.** §4's decision rule reserves "repoint to a published guardrail picker" for an ambiguous measurement. The evidence now puts the pick there **before** the measurement runs: the only unmeasured question left is whether four commercial moderation endpoints disagree on paired Vietnamese and English items, and Microsoft has already written the reason a buyer would want to know — *"the quality might vary. In all cases, you should do your own testing."*

Against that, one thing moved in the pick's favour and it is the largest finding here: **Vietnam has a live AI law with an independent-assessment obligation and an undefined assessment artifact, biting deployed systems around 2027-03-01** (§5). That is a real trigger in the one jurisdiction this team can reach, and it was invisible to wave 1.

---

## Constraints for wave 2c

Not a design. The boundaries anything 2c designs has to sit inside.

1. **Do not claim a first.** SEA-HELM has published Vietnamese ViHSD safety scores for 61 open-weight and 9 closed-weight models since 2025-02. Anything 2c ships cites SEA-HELM and positions against it, or it is wrong on its first page.
2. **The measured object is the guardrail product, not the model.** SEA-HELM's gap is that it prompts general LLMs as classifiers. The unmeasured territory is commercial moderation endpoints — Llama Guard 3 8B, OpenAI `omni-moderation-latest`, **Azure AI Content Safety** (now mandatory, it is the one that killed the absence claim), Lakera Guard. Four, not three.
3. **The paired condition is the only novel half.** SEA-HELM's active `toxicity` task has no English arm. Metric 2 — directional VI-pass / EN-flag disagreement on identical items — is the measurement nobody has published. Metric 1 alone duplicates work already done.
4. **Build on promptfoo, do not rebuild it.** `redteam.language`, the `moderation` assertion, and `guardrails` / `not-guardrails` already exist and already cover three of the four endpoints. Writing a harness instead of a config is rework, and it is visible rework to anyone who reads the docs.
5. **Resolve the ViHSD licence before sampling, and fix the citation.** Three attributions: MIT (`sonlam1102/vihsd`), CC BY-NC 4.0 (AI Singapore's source table), and a signed corpus user agreement with UIT for the official copy, which is `gated` on Hugging Face (wave 1c). Two of the three block a commercial derivative. Also: the dataset is arXiv **2103.11528**, not 2103.10069 — the plan cites a different dataset.
6. **The binding constraint on the measurement is licence-acceptance authority, not money or compute.** Wave 1c: ViHSD gated by UIT, Llama Guard 3 8B gated on Meta's manual-approval tier, this machine at 6,668 MiB free VRAM so 4-bit only. Both gates are human decisions outside an agent's remit. The Replicate route (§3) removes the Llama Guard hardware problem, not the ViHSD one. 2a's "days, not weeks, for one person" did not price either gate.
7. **Budget for SEA-HELM turning `safeguard_general` back on.** The EN/VI paired files are committed and blocked only by a data-cleanup note. Anything whose value depends on that task staying off has a countdown on it.
8. **Assume no compliance artifact is specified.** Vietnam's AI Law mandates independent assessment for medium- and high-risk AI and defers the methodology to implementing regulations. 2c may design toward that gap; it may not assert the law requires guardrail testing, because no source says so.
9. **Price is unknowable, so do not design around one.** No SEA price point and no buyer count exist. A design whose viability depends on a specific price or a specific buyer count is untestable on this evidence.
10. **If 2c designs the fallback instead, design 2.1, not 1.1.** The swap is triggered by §1b and §1c under 2a's own rule. 1.1's gap is occupied by ; anything built there is now a competitive entry against a Google Cloud org, not a first mover, and would still need HiddenLayer's, Palo Alto's and Cranium's product pages pulled, because no file in this repo has ever read one.
11. **Cite the raw file, not the compiled one.** Two of this review's four kills came from a compiled file restating an inference as a confirmation. Any claim 2c makes about what an incumbent does not do gets a quoted vendor sentence or an `unknown — checked <channel> <date>`.
12. **The boundary holds unchanged.** Public academic dataset, defenses under test, operator-controlled endpoints only. Product 2.2's dual-use problem is untouched by this review and remains open.

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
