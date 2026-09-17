# Dataset + baseline pulls — staging N4/4.1's settling measurement

Wave 1c, 2026-09-17. Scope: five gaps 2a left open before the Vietnamese-guardrail settling measurement (`docs/plan/niche-and-solutions.md` §4, "The single measurement that settles it") can be built. This wave pulls facts and stages inputs; it does not run the benchmark, evaluate the niche, or write plan/review files. Sources: `raw/vihsd-vitosa-pull.md`, `raw/sea-helm-safety-pull.md`, `raw/guardrail-language-claims-pull.md`, `raw/local-runnability-pull.md`, `raw/translation-path-pull.md`. Method throughout: direct fetch (arXiv, GitHub `gh api`, Hugging Face API, vendor docs) — no browser tools (a sibling agent holds Chrome on another project), no account creation, no licence acceptance, no paid calls.

## Gap 1 — ViHSD / ViToSA: the dataset itself

**Citation correction, first.** `docs/explore/language-gap.md` and `docs/plan/niche-and-solutions.md` both cite **arXiv 2103.10069** for ViHSD. That ID is wrong — it is **UIT-ViCTSD** ("Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese," CC BY-NC-SA 4.0, a different dataset, sibling Springer-proceedings chapter by an overlapping author team). **The correct ID is arXiv 2103.11528** ("A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts," confirmed via `export.arxiv.org` search API). This file, and every downstream reference in this wave, uses 2103.11528. Not correcting the two files that carry the error — out of this wave's boundary.

**Label schema, verbatim (Table 1 of the paper):**

| Label | Definition (verbatim) |
|---|---|
| CLEAN | "The comments have no harassment at all." |
| OFFENSIVE | "The comments contain harassment contents, even profanity words, but do not attack any specific object." |
| HATE | "The comments have harassment and abusive contents and directly aim at an individual or a group of people based on their characteristics, religion, and nationality." |

**Item counts, exact (Fig. 2 of the paper):**

| Split | CLEAN | OFFENSIVE | HATE | Total |
|---|---|---|---|---|
| Train | 19,886 | 1,606 | 2,556 | 24,048 |
| Dev | 2,190 | 212 | 270 | 2,672 |
| Test | 5,548 | 444 | 688 | 6,680 |
| **All** | **27,624** | **2,262** | **3,514** | **33,400** |

**Collection:** Facebook pages + YouTube channels, "high-interactive rate," no comment restrictions; named entities removed for anonymity. **Annotation:** 2-annotator pass, 3rd/4th annotator escalation on disagreement, majority vote; inter-annotator agreement (202-comment sample) **Cohen's κ = 0.52** — paper's own words: "just in moderate level." Best baseline (BERT, multilingual-cased): 86.88% accuracy, 62.69% macro-F1 — paper flags the accuracy/F1 gap as a symptom of class imbalance, not model strength.

**Licence — GATED, quoted verbatim, not staged.** Official channel (`nlp.uit.edu.vn/datasets`): "Please contact us via email: sonlt@uit.edu.vn (Mr. Son Luu) to sign the corpus user agreement and then receive the corpus." Official Hugging Face org copy (`uitnlp/vihsd`) is independently `"gated":"auto"`. **No agreement signed, nothing downloaded** — including from the several un-gated third-party HF mirrors found (routing around the licensor's terms via a mirror was treated as equivalent to not having permission, and not done).

**ViToSA (arXiv 2506.00636 — this ID was already correct):** audio toxic-span detection, 11,000 clips / 25 hours, INTERSPEECH 2025. Both official HF repos (`ViToSA-1.0`, `ViToSA-2.0`) are `"gated":"auto"`. Not downloaded. Also not a task-shape match for the settling measurement (span-level audio labels, not document-level text classification).

**Status: PARTIALLY CLOSED.** Label schema, counts, methodology, and IAA are fully pulled and usable for designing the stratified sample. The dataset itself is not staged — licence blocks it.

## Gap 2 — SEA-HELM's Vietnamese safety pillar

SEA-HELM (arXiv 2502.14301) Safety pillar has **two sub-tasks**, both confirmed via the live `aisingapore/SEA-HELM` GitHub repo (config files read directly):

| Sub-task | Dataset | Vietnamese source | What it tests |
|---|---|---|---|
| `toxicity_detection` (in the paper) | `aisingapore/Safety-Toxicity-Detection` | 1,000-item sample of **ViHSD itself** | Prompts the **general chat LLM under test** (e.g. GPT-4o, Llama-3, Qwen, Gemma) zero-shot to output Sạch/Công kích/Thù ghét |
| `safeguard/general` (added to repo after the paper) | Machine-translated NVIDIA Aegis2, Llama-Guard-style S1-S14 taxonomy | `vi_general.jsonl`, machine-translated from English | Prompts the **general chat LLM under test** zero-shot for Safe/Harmful |

**Neither sub-task evaluates a dedicated guardrail product.** Llama Guard 3, `omni-moderation-latest`, and Lakera do not appear anywhere in SEA-HELM's method — both tasks ask a general-purpose chat model to self-classify. **Neither runs a VI-vs-EN paired-translation design** — Vietnamese accuracy is reported in isolation, with no matched-English control.

**Numeric scores: not obtained.** The paper's Table 2 gives only a 5-pillar-blended per-language aggregate (e.g. gpt-4o-2024-08-06 VI=68.1, DeepSeek-R1 VI=68.0) — not a Safety-only breakout. The live leaderboard (`leaderboard.sea-lion.ai`) is a JS-rendered SPA; no static results file exists in the GitHub repo or the `aisingapore` HF org (27 dataset repos enumerated, none is a results/scores dataset). Per-model Vietnamese-Safety-only scores are `unknown — checked leaderboard.sea-lion.ai 2026-09-17, JS-rendered, no browser tool available for this wave`.

**Honest read: does SEA-HELM already answer the question? No.** It proves Vietnamese ViHSD-based toxicity evaluation is already a maintained, live metric — for general LLMs prompted as classifiers, not for the three specific guardrail *products* in 2a's spec, and never in a VI-vs-EN paired design. The wedge survives this check, narrower than "first Vietnamese safety number ever" (SEA-HELM already has Vietnamese safety numbers, for a different object) but intact as "first test of whether *shipping guardrail products* hold on Vietnamese vs. English translation."

**Status: PARTIALLY CLOSED.** What the pillar measures is fully resolved. Actual numeric scores are unreachable with this wave's tools.

## Gap 3 — Guardrail language claims, verbatim

| Guardrail | Vietnamese named? | Verbatim language claim | Invocation | Cost | Licence gate |
|---|---|---|---|---|---|
| **Llama Guard 3 8B** | **No** — stops at Thai | "Llama Guard 3 supports content safety for the following languages : English, French, German, Hindi, Italian, Portuguese, Spanish, Thai." | Local weights (BF16 or INT8), or unconfirmed third-party hosting | Free weights once gated; hosted pricing unconfirmed | **Yes — `"gated":"manual"`**, Llama 3.1 Community Licence, Meta reviews each request |
| **`omni-moderation-latest`** | No claim either way (page is silent) | — | REST `POST https://api.openai.com/v1/moderations` | **"The moderation endpoint is free to use"** (verbatim) | No data-licence gate; needs an OpenAI API key |
| **Lakera Guard** | No named list | "Observing 100+ languages in real-time" — unverifiable marketing copy, no list | REST `POST https://api.lakera.ai/v2/guard` | Free tier asserted ("Start for free"); limits unconfirmed (pricing page is JS-rendered) | No licence-agreement gate found |
| **NeMo Guardrails** | No claim either way (silent) | — | Local Python library (`LLMRails`), wraps a caller-supplied LLM backend | Free (Apache 2.0); cost = whatever backend LLM you plug in | No |
| **ShieldGemma 9B** (open alternative) | **No — explicit English-only**: "available in English with open weights" | — | Local weights only — "isn't deployed by any Inference Provider" | Free weights once gated | Yes — Gemma licence |

Independent re-fetch of Llama Guard 3 / NeMo / Lakera matches wave 1's `raw/language-gap-pulls.md` findings word-for-word — not a one-off render artifact. New this pass: `omni-moderation-latest` is **silent** on language (like NeMo — absence, not denial), and is the only guardrail confirmed **free with no tier structure at all**. Also new: Llama Guard 3's own machine-readable HF metadata tag (`cardData.language`) is `["en"]`-only, narrower even than its 8-language prose claim.

**Status: CLOSED.** All five guardrails have a verbatim, sourced language claim (or documented silence) plus invocation/cost/gate detail. Pricing/rate-limit numbers on JS-rendered vendor pages (Lakera, Together, Groq) are the one residual `unknown`.

## Gap 4 — Runnability on this machine

**Llama Guard 3 8B requirements:** 8B params; BF16 ≈16GB VRAM, INT8 (vendor checkpoint) ≈8GB, 4-bit community quantization ≈5GB (computed-by-us from standard bytes/param arithmetic — not vendor-benchmarked). Licence gate is Meta's **manual-approval** tier (`"gated":"manual"`), stricter than an auto-accept click-through.

**This machine (checked directly, 2026-09-17):** GPU = NVIDIA RTX 3060 Ti, **8192 MiB total VRAM, 6668 MiB free** at check time. Python: `pythoncore-3.14-64` (default) plus an unregistered uv-managed `cpython-3.9.25`. **No `torch`, `transformers`, `vllm`, or `ollama` installed.** `uv` is present (could provision an env). D: drive has 276.7 GiB free.

**Verdict: local run is marginal, not blocked.**
- BF16 (16GB) — does not fit, ruled out.
- INT8 (~8GB) — does not comfortably fit within 6.7GB free; would OOM or leave no KV-cache headroom.
- 4-bit quantized (~5GB) — the only precision plausibly viable here, not verified empirically (no weights downloaded).
- Software stack (torch/transformers) is not installed but is a free, no-licence `pip`/`uv` step.
- **The blocking step is Meta's manual licence gate, not hardware or software.** No hosted alternative with confirmed live pricing was found (Together: "not available... launching soon"; OpenRouter: not found in fetched catalog; Groq: pricing page unreachable via fetch).

**Status: CLOSED** on the facts; **the local-vs-hosted decision for Llama Guard 3 specifically is open** and gated on a licence-acceptance call this wave does not make.

## Gap 5 — Vietnamese→English translation path, no paid spend

**Recommended: `Helsinki-NLP/opus-mt-vi-en` + `Helsinki-NLP/opus-mt-en-vi`** (MarianMT pair). Both confirmed ungated (`"gated":false`), Apache 2.0, small enough for CPU inference at this measurement's volume (500-1,000 items). Vendor-reported quality on Tatoeba: BLEU 42.8, chrF 0.608 (not independently verified). Standard `transformers` invocation, no API key, fully offline once downloaded.

**Alternative: `VietAI/envit5-translation`** — single bidirectional T5-base model (language-prefix controlled), OpenRAIL licence, ungated, 6,023 downloads. Simpler pipeline (one model, both directions) at the cost of a less permissive licence family (OpenRAIL terms not fetched in full this pass) and a larger footprint.

**Open item, not resolved this pass:** the spec's back-translation *fidelity filter* ("discard items whose meaning did not survive") needs a similarity metric — BLEU/chrF against the round-tripped text, or a multilingual sentence-embedding cosine check (e.g. `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, not verified this pass). Flagged for whoever executes the measurement.

**Status: CLOSED** on identifying a concrete, free, local option. Neither model's weights were downloaded (staging weights judged a follow-on execution step, not this wave's mandate) — both are ungated and free, so downloading them later requires no licence acceptance.

## Can the settling measurement be built here — verdict

**Staged and ready:**
- ViHSD's exact label schema, class counts, and methodology (enough to design the stratified sample once the data itself is obtained).
- A confirmed, verbatim, per-guardrail language claim for all three guardrails under test plus two comparators — this is the core evidentiary artifact the whole niche leans on, and it holds up under independent re-fetch.
- A concrete, free, local VI↔EN translation path (Helsinki-NLP OPUS-MT).
- A clear map of this machine's actual compute (RTX 3060 Ti, 8GB VRAM, no ML stack installed yet, plenty of disk).

**Blocked, not staged:**
- **The dataset itself.** ViHSD requires UIT to grant access via a signed corpus user agreement — a human decision, not something this wave can or should make unilaterally. Nothing was downloaded from the official source or from ungated mirrors.
- **Llama Guard 3 8B's weights.** Gated on Meta's manual-approval tier. No confirmed working hosted alternative was found with live pricing.
- **A working fidelity-filter method for back-translation** — identified in outline, not selected or implemented.

**What it would cost, once the ViHSD and Llama Guard gates are cleared by someone with authority to accept those terms:** near-zero cash (`omni-moderation-latest` free; Lakera free tier asserted; MT models free; local 4-bit Llama Guard inference free once weights are obtained) — the binding constraint is **licence-acceptance authority**, not money, not compute, and not missing facts. Everything this wave could pull without crossing that line has been pulled.

## Caveats (carried from `raw/`, not repeated in full)

- Lakera/Together/Groq pricing and rate-limit numbers are `unknown` — JS-rendered pages, no browser tool available to this wave.
- The arXiv-ID citation error (2103.10069 → 2103.11528) is corrected here for this wave's own use; `docs/explore/language-gap.md` and `docs/plan/niche-and-solutions.md` still carry the wrong ID and were not edited (out of boundary).
- SEA-HELM's per-model Vietnamese-Safety-only numeric scores are unreachable without a browser or reverse-engineering the leaderboard's backend API — neither done.
- Community GGUF requantizations of Llama Guard 3 8B (which might sidestep the manual gate's *download* step while still being subject to the same underlying Llama licence) were not searched for or evaluated — a licence-compliance judgment call left to 2c or a human, not decided here.
