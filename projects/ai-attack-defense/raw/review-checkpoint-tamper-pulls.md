# Wave 2b adversarial review — falsifying "nothing detects a behaviorally tampered checkpoint"

Pull date: 2026-09-17. Purpose: falsify the absence claim under `../docs/plan/niche-and-solutions.md`'s fallback pick (product 1.1, `refusal-diff`).

Provenance note, important: a background falsification sweep was dispatched and returned after the review's first draft closed. **Every item below marked VERIFIED was re-pulled directly by wave 2b from the named channel on 2026-09-17.** Items marked AGENT-REPORTED, UNVERIFIED come from that sweep's report only and were not independently fetched — they are recorded here so a later pass can close them, and they are labelled as such wherever cited.

---

## PULL 1 — VERIFIED — Google Cloud Platform's Activation Model Scanner (AMS)

This is the product the absence claim said did not exist.

### 1a — PyPI

Source: PyPI JSON API. URL: https://pypi.org/pypi/ams-scanner/json. Method: WebFetch, 2026-09-17.

- Package: `ams-scanner`. Latest version **0.1.3**. Releases 0.1.0 and 0.1.3 both dated **2026-04-28**.
- Summary, verbatim: **"Activation-based Model Scanner - Verify LLM safety via activation pattern analysis"**
- Author/maintainer: Glen Messenger (glen.messenger@gmail.com), owner org `gke-ai-security`. Licence **Apache-2.0**.
- Project URLs all point at `https://github.com/GoogleCloudPlatform/activation-model-scanner`.
- On tier-2 verification, verbatim: **"Verifies a model matches its claimed identity...Catches subtle modifications, abliteration, and weight substitution."**

### 1b — GitHub

Source: `gh api repos/GoogleCloudPlatform/activation-model-scanner`, 2026-09-17.

`stars 33 | forks 9 | pushed 2026-08-27T16:25:06Z | created 2026-03-23T17:37:25Z | license Apache-2.0 | archived false | desc: Verify language model safety before deployment by analyzing activation patterns`

README.md, verbatim:

> **Verify language model safety before deployment by analyzing activation patterns.**
>
> **Disclaimer:** This is not an officially supported Google product. This project is not eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).
>
> AMS detects whether a model has intact safety training by measuring the separation of safety-relevant concepts in the model's activation space. Models with removed or degraded safety training (e.g., "uncensored" fine-tunes, abliterated models) show collapsed safety directions that AMS can detect in seconds.

README "Limitations" section, first item, verbatim:

> 1. **Base models:** Pre-trained models without instruction tuning naturally have weaker safety directions. AMS may flag these as unsafe even though they were never intended to have safety training.

AGENT-REPORTED, UNVERIFIED from the sweep: 19 downloads/month; 71% leave-one-out accuracy. Not re-pulled.

---

## PULL 2 — VERIFIED — DeepTeam documents the workflow and ships none of it

Source: `gh api "repos/confident-ai/deepteam/contents/docs/content/guides/(model-security)/guide-red-teaming-open-weight.mdx"`, base64-decoded, 2026-09-17. Located via code search `"original model" repo:confident-ai/deepteam` → `total_count: 1`.

Section "Community Fine-Tunes and Merges", lines 202–211, verbatim:

> ## Community Fine-Tunes and Merges
>
> If your deployment uses a community fine-tune, a LoRA merge, or a domain-adapted variant:
>
> 1. **Treat safety as unknown.** Fine-tuning can silently remove safety behaviors even when the training data is benign.
> 2. **Test before deploying.** Run a baseline assessment before any production exposure.
> 3. **Compare against the base model.** Run the same assessment against the original model to identify what the fine-tune changed.
> 4. **Monitor for regression.** Re-run the assessment after each model update.

AGENT-REPORTED, UNVERIFIED: DeepTeam repo code search for `tamper|abliterat` returns 0 hits; no differential harness, base-model resolver, deviation metric or verdict exists in code. Not re-pulled.

---

## PULL 3 — VERIFIED — the attack side is fully productized

Source: `gh api -X GET search/repositories -f q='heretic abliteration'`, 2026-09-17. Top three rows verbatim:

```
p-e-w/heretic | Fully automatic censorship removal for language models | stars 31632 | pushed 2026-09-05T16:11:52Z
dreamfast/heretic-docker | Docker container for running heretic LLM abliteration on NVIDIA Blackwell GPUs | stars 10 | pushed 2026-08-10T09:48:17Z
sunkencity999/blasphemer | Enhanced fork of Heretic (an automated LLM de-censoring tool) optimized for macOS (Apple Silicon) with checkpoint system and LM Studio integration | stars 26 | pushed 2026-07-22T21:17:12Z
```

AGENT-REPORTED, UNVERIFIED: Heretic drives 54% of new uncensored-model production (~338/month); 8,164 redistributions in circulation; Abliteration.ai sells de-refused GLM-5.3 at $5/M tokens. Not re-pulled.

---

## PULL 4 — VERIFIED — the orthogonalized derivative itself

Source: Hugging Face model card `failspy/Llama-3-8B-Instruct-MopeyMule`. URL: https://huggingface.co/failspy/Llama-3-8B-Instruct-MopeyMule. Method: WebFetch, 2026-09-17.

Verbatim:

> "This is not traditional fine-tuning. Rather, this model is the same weights as Llama-3-8B-Instruct, however with a grumpy/irritable 'direction' induced and amplified."

> "Using the orthogonalization technique described in this blog post from Andy Arditi et al."

The card describes running inference twice over 1,024 harmless Alpaca prompts — once with the standard chat template, once with a grumpy-oriented system prompt — to extract and then bake a direction into the weights. That is the same primitive as abliteration (Arditi et al., *Refusal in LLMs is mediated by a single direction*), pointed at a non-refusal direction.

---

## PULL 5 — AGENT-REPORTED, UNVERIFIED — Enkrypt AI's leaderboard rates the derivative safer than its base

Wave 2b attempted verification: `https://huggingface.co/spaces/EnkryptAI/LLM-Safety-Leaderboard` returned **HTTP 401** to WebFetch, 2026-09-17. `unknown — checked 2026-09-17, 401`.

Reported by the sweep from a live leaderboard payload of 282 rows fetched 2026-09-17, not re-pulled by wave 2b:

| Rank | Model | Source | Provider | Risk score |
|---|---|---|---|---|
| 51 | `Llama-3-8B-Instruct-MopeyMule` | `failspy` | `hf_local` | 23.31 |
| 101 | `Meta-Llama-3-8B-Instruct` | `meta` | openai_compatible | 27.94 |

Reported row schema: `model_name, risk_score, bias_score, cbrn_score, harmful_score, insecure_code_score, toxicity_score, robustness_score, jailbreak_score, evasion_score, safety_score, nist_score, owasp_score, source, provider, starScore, rank, performance, performanceRiskRatio` — reported to contain no `base_model`, `lineage`, `parent`, `derived_from`, `integrity` or `tamper` field, and zero occurrences of `abliterat*`, `uncensored` or `tamper*`. `dolphin-2.5-mixtral-8x7b` reported at rank 241, unflagged. Also reported: Enkrypt's `add-model` API takes `{scheme, host, port, base_path}` with no field for a checkpoint path or weights upload.

**Do not cite externally without re-pulling.** The model card in PULL 4 is verified; the ranking is not.

---

## PULL 6 — AGENT-REPORTED, UNVERIFIED — the rest of the sweep

Recorded verbatim as reported, none re-pulled by wave 2b. All require verification before use.

- **Azure AI Foundry / HiddenLayer**: reported to state that "Customers' fine-tuned models, models imported directly from Hugging Face, and proprietary models offered as-a-Service… are not scanned by HiddenLayer today", and to define the backdoor check as "Scans model functionality for evidence of supply chain attacks and backdoors such as **arbitrary code execution and network calls**." The sweep flags that the Community Hub page returned metadata only on two WebFetch attempts and that it could not verify the exclusion sentence itself. **This is the single most load-bearing unverified item in this file** — if it holds, the one catalog that says "tampering" does not scan the population at risk.
- **garak FAQ**: reported verbatim "LLM model parameters don't and can't have vulnerabilities themselves; it's just data" and "No meaningful comparison can be made of scores between different probes." Only file-touching probe reported as `HF_Files` → `primary_detector = "fileformats.FileIsPickled"`.
- **Google Vertex / Model Garden**: reported verbatim "we use the Hugging Face Malware Scanner to assess the safety of files… **we don't guarantee the absence of vulnerabilities or malicious code.** We recommend that you conduct your own security verifications."
- **AWS Bedrock Custom Model Import**: reported to accept arbitrary customer weights from S3 with no vetting language, only "Make sure that your import and use of the models in Amazon Bedrock complies with the terms or licenses applicable to the models." SageMaker JumpStart reported to carry no security-scanning claim.
- **Cisco AI Defense "AI Validation"**: reported to both "test models using algorithmically generated prompts across 200 categories" and "automatically scan open-source models, data, and files to block supply chain threats, such as malicious model files that can allow for arbitrary code execution" — the two capabilities reported as sitting side by side and never joined.
- **Endpoint-scoped red-teamers** — Virtue AI (VirtueRed), Haize Labs, Patronus, Lakera Red, SplxAI, Dynamo AI: all reported to evaluate a serving endpoint or application, not a checkpoint, and none to frame output as tamper-vs-base. Virtue AI and Haize Labs rows drawn from indexed copy after 429/403 on fetch — doubly unverified.
- **Research-only implementations** reported for the trigger-backdoor half: Microsoft's (23★, 3 commits), CLIBE (26★, one-day upload), WeightWatch, ToxScreen.
- **Benchmarks**: HELM Safety v1.0 reported to run HarmBench ASR and XSTest over-refusal; Azure Foundry's leaderboard reported to publish HarmBench ASR with "Guardrails… turned off"; MLCommons AILuminate reported to grade "Bare Models" but to gate the full 12,000-prompt set behind membership verification, with only 1,200 demo prompts public.
