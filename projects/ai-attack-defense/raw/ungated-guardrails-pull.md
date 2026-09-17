# Ungated guardrails/safety classifiers — raw pull

Wave 1d, pull date 2026-09-17. Method: HuggingFace Hub HTTP API (`huggingface.co/api/models/...`), `raw.githubusercontent.com` for README/config text, arXiv full text via `ar5iv.labs.arxiv.org`, `export.arxiv.org` API, and the technical-report PDF from `github.com/QwenLM/Qwen3` (read directly, not web-rendered). No browser tools. No account creation. No licence click-through performed for any gated model.

## FOUND — ungated, open-weight, no gate at all

### Qwen3Guard (Gen and Stream, 0.6B / 4B / 8B) — the standout positive result

- **HF repos**: `Qwen/Qwen3Guard-Gen-{0.6B,4B,8B}`, `Qwen/Qwen3Guard-Stream-{0.6B,4B,8B}`. All confirmed `"gated": false`, `"license": "apache-2.0"` via direct API fetch.
- **GitHub**: `github.com/QwenLM/Qwen3Guard`, MIT... (repo itself carries no separate GH licence field checked; model weights are Apache 2.0 per HF card, which governs use).
- **Paper**: arXiv 2510.14276, "Qwen3Guard Technical Report" (Zhao, Yuan, Huang, Hu, Zhang, Yang, Yu, Liu, Zhou, Lin et al., 2025).
- **Language claim, verbatim (HF model card, `Qwen/Qwen3Guard-Gen-8B/README.md`)**: "**Multilingual Support:** Qwen3Guard-Gen supports 119 languages and dialects, ensuring robust performance in global and cross-lingual applications."
- **Verbatim from the arXiv paper (ar5iv full text)**: "Both variants are available in three sizes (0.6B, 4B, and 8B parameters) and support up to 119 languages and dialects, providing comprehensive, scalable, and low-latency safety moderation for global LLM deployments." The paper's own language list is not enumerated by name in the Qwen3Guard paper itself — the 119-language figure is inherited from the Qwen3 base model.
- **Is Vietnamese specifically named?** Not in the Qwen3Guard paper's own text (no literal "Vietnam" string found in the ar5iv-rendered full text). However the **Qwen3 base model's own technical report explicitly names and benchmarks Vietnamese**, which is the strongest available evidence that Qwen3Guard's "119 languages" claim includes Vietnamese in substance, not just marketing count:
  - Qwen3 Technical Report (`github.com/QwenLM/Qwen3/blob/main/Qwen3_Technical_Report.pdf`, dated 2025-05-14), Table 33, verbatim: **"Benchmark scores for language: Vietnamese (vi)"** — a full results table (MLogiQA, INCLUDE, MT-AIME2024, PolyMath) with scores reported for Qwen3-235B-A22B down to Qwen3-0.6B, both thinking and non-thinking modes.
  - Same report, Table 36 ("Language families and language codes supported by Qwen3 in Belebele Benchmark"), Austroasiatic row, verbatim: **"vie Latn, khm Khmr"**.
  - Abstract, verbatim: "Compared to its predecessor Qwen2.5, Qwen3 expands multilingual support from 29 to 119 languages and dialects."
  - This is qualitatively different from Llama Guard 3's language claim (an 8-language prose list that stops at Thai) or Lakera's marketing "100+ languages, no list" — Qwen3's 119-language claim is backed by a per-language benchmark table naming Vietnamese explicitly, even though that table is for the base LLM, not the Qwen3Guard classifier head itself.
- **Sizes / VRAM fit** (from HF API `usedStorage`, includes all repo files at the checked commit): Gen-0.6B ≈ 1.51 GB total repo storage (BF16 weights fit easily within 6.7 GB free VRAM, no quantization needed). Gen-4B ≈ 8.83 GB (BF16 does not fit in 6.7 GB free; would need 8-bit ≈4.4GB or 4-bit ≈2.5GB quantization, neither verified empirically this pass). Gen-8B ≈ 16.39 GB (same order as Llama Guard 3 8B; needs 4-bit quantization to plausibly fit, ≈5GB estimate, not verified empirically). These are `computed-by-us` from standard bytes-per-parameter arithmetic and the API's reported storage figure, not vendor-benchmarked.
- **Verdict**: this is the single strongest "ungated guardrail with a credible multilingual claim reaching Vietnamese" found this pass. The 0.6B variant is small enough to run comfortably today on this machine's 6.7GB free VRAM without any quantization.

### IBM Granite Guardian (3.0 / 3.1 / 3.2 / 3.3, 2B–8B)

- **HF repos**: `ibm-granite/granite-guardian-3.{0,1,2,3}-{2b,5b,8b}` (exact set of sizes varies by version). All checked versions confirmed `"gated": false`, `"license": "apache-2.0"`.
- No dependency on any gated base model — fully standalone.
- **Language claim, verbatim (every version's HF `cardData`)**: `language: [en]` — explicit, machine-readable English-only tag, consistently across 3.0 through 3.3. No prose claim of additional language support found in any version's README body (checked 3.0-8b, 3.2-5b, 3.3-8b bodies directly — no "language" section beyond the front-matter tag).
- **Verdict**: genuinely ungated and free, but explicitly English-only like ShieldGemma — not usable for a Vietnamese measurement, but usable as a same-shape "known-negative" comparator if a design wants to show a fully-open, English-only alternative alongside Qwen3Guard.

### Detoxify / `unitary/*` toxic classifiers

- **HF repos**: `unitary/toxic-bert`, `unitary/multilingual-toxic-xlm-roberta` (the pip-installable `detoxify` library's underlying weights). Both `"gated": false`, `"license": "apache-2.0"`.
- **Language claim, verbatim (README)**: "The `multilingual` model has been trained on 7 different languages so it should only be tested on: `english`, `french`, `spanish`, `italian`, `portuguese`, `turkish` or `russian`." — **No Vietnamese**, explicit negative, matches the Jigsaw Multilingual Toxic Comment Classification competition's original 7-language set (which Detoxify's multilingual model is trained on).
- **Verdict**: ungated and free, but Vietnamese explicitly excluded by the vendor's own usage guidance.

### OpenSafetyLab/MD-Judge-v0.1 (SALAD-Bench judge model)

- **HF repo**: `OpenSafetyLab/MD-Judge-v0.1`. `"gated": false`, `"license": "apache-2.0"`, `cardData.language: [en]`.
- **Verdict**: ungated, free, standalone, but English-only — no Vietnamese claim at all.

## CHECKED, EFFECTIVELY GATED — either a direct HF gate, or a gated base-model dependency

### WildGuard (Allen AI)

- **HF repo**: `allenai/wildguard`. `"gated": "auto"` — this is a **self-serve click-through gate**, not Meta's manual-review tier, but it is still a gate under this project's hard rule (no clicking through any gate).
- **Gate text, verbatim (`extra_gated_prompt`)**: "Access to this model is automatically granted upon accepting the [AI2 Responsible Use Guidelines](https://allenai.org/responsible-use.pdf), and completing all fields below" — followed by a form (full name, organization, country, contact email, intended-use description, three checkboxes agreeing to AI2's terms).
- **Language**: `cardData.language: [en]` — English only, so even if the gate were cleared, no Vietnamese claim exists.
- **Distinction worth recording**: "auto" gates like this one grant access instantly once a human fills the form and clicks agree — no human reviewer, no waiting period — a materially lower barrier than Llama Guard 3 8B's `"gated":"manual"` (Meta reviews each request). Still out of bounds for this agent under the hard rule; a human user could clear it in under a minute if they chose to.

### NVIDIA Aegis / NemoGuard family (LlamaGuard- and Llama-3.1-based)

- **Checked**: `nvidia/Aegis-AI-Content-Safety-LlamaGuard-Defensive-1.0`, `-Permissive-1.0`, `nvidia/llama-3.1-nemoguard-8b-content-safety`.
- All three HF repos self-report `"gated": false` — **but this is misleading**: each repo ships only `adapter_config.json` + `adapter_model.safetensors` (a PEFT/LoRA adapter), never full merged weights. Running any of them requires downloading the base model first:
  - Aegis 1.0 LlamaGuard adapters: base is `meta-llama/LlamaGuard-7b` — confirmed `"gated": "manual"`.
  - NemoGuard-8B-ContentSafety (Aegis 2.0-trained): base is `meta-llama/Llama-3.1-8B-Instruct` — confirmed `"gated": "manual"`.
- **Licence, verbatim (NemoGuard-8B card)**: "GOVERNING TERMS: Use of this model is governed by the [NVIDIA Open Model License Agreement]... Additional Information: [Llama 3.1 Community License Agreement]... Built with Llama." — a stacked licence (NVIDIA's own terms plus Meta's).
- **Language, verbatim**: `cardData.language: [en]` for both. Card prose describes the *base* as "the multilingual Llama-3.1-8B-Instruct model," but the safety fine-tuning dataset (Aegis 2.0 / Nemotron Content Safety Dataset V2) and the resulting classifier are English-only per the card's own language tag.
- **Verdict**: effectively gated (Meta's manual tier, via the base model), and English-only regardless — no Vietnamese benefit even if cleared.

### Llama Guard 3 8B, Llama Guard 3 1B, ShieldGemma 9B/2B

- Already fully characterized in wave 1c (`raw/guardrail-language-claims-pull.md`, `raw/local-runnability-pull.md`). This pass independently re-confirmed via HF API: Llama Guard 3 8B `"gated":"manual"`; **Llama Guard 3 1B is also `"gated":"manual"`**, with the identical 8-language claim as the 8B model (`en, de, fr, it, pt, hi, es, th` — Thai, not Vietnamese) — so the smaller distilled variant offers no gate relief and no language improvement. ShieldGemma `"gated":"manual"`, English-only, unchanged.

## CHECKED, NEGATIVE (no Vietnamese-relevant open guardrail found)

- **Qwen-based non-guard safety classifiers**: `caskcsg/Libra-Guard-Qwen2.5-*` family found (ungated, ranges 0.5B–14B) — but `cardData.language: [zh]` only (Chinese-focused judge model for a Chinese red-teaming benchmark), not a multilingual or Vietnamese-relevant safety classifier. Not pursued further.
- **SeaLLM safety/guard variants**: HF search for "SeaLLM guard" and "SeaLLM safety" returned zero results. No SEA-specific guardrail product from the SeaLLM family was found.
- **Sailor safety variants**: HF search for "Sailor safety" returned zero results. No Sailor-branded guardrail found.
- **Perspective API**: covered in full in `raw/perspective-api-pull.md` — no Vietnamese in any attribute, and the service is sunsetting.

## Method notes

- HF's `"gated"` field has three observed states in this pull: `false` (no gate at all), `"auto"` (self-serve click-through, a form plus a checkbox, instantly granted), `"manual"` (a human reviewer at the model owner approves or denies each request, on their own timeline). This project's hard rule treats `"auto"` and `"manual"` identically — both require accepting terms, which this agent will not do — but they are materially different in how much a human user would need to do to clear them, and that distinction is preserved here for whoever reads this file.
- A model repo reporting `"gated": false` does not guarantee it is actually usable without any gate — LoRA/PEFT adapter repos (Aegis, NemoGuard) inherit their base model's gate. Always check `siblings` for `adapter_config.json` and, if present, resolve `base_model` before treating a "gated: false" result as final.
