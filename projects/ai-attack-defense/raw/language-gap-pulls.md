# Vietnamese / SEA language-gap evidence — raw

Pull date: 2026-09-17. Method: arXiv API (`export.arxiv.org/api/query`, direct HTTP, not WebSearch) for paper discovery and abstracts; `ar5iv.labs.arxiv.org` full-text HTML fetch + plain-text search for language-name mentions; `gh api` for the XSafety benchmark's GitHub repo file listing; `WebFetch` for two shipping-tool docs (Llama Guard 3 model card, NeMo Guardrails repo, Lakera Guard marketing page). WebSearch used sparingly per quota-budget instruction; noted where used.

## Paper 1 — XSafety / "All Languages Matter: On the Multilingual Safety of Large Language Models"

arXiv 2310.00905, published 2023-10-02. Abstract verbatim: "...we build the first multilingual safety benchmark for LLMs, XSafety, in response to the global deployment of LLMs in practice. XSafety covers 14 kinds of commonly used safety issues across 10 languages that span several language families. We utilize XSafety to empirically study the multilingual safety for 4 widely-used LLMs... Experimental results show that all LLMs produce significantly more unsafe responses for non-English queries than English ones..."

GitHub repo `Jarviswang94/Multilingual_safety_benchmark` directory listing (`gh api repos/Jarviswang94/Multilingual_safety_benchmark/contents/`), verbatim folder names = the 10 language codes: `ar, bn, de, en, fr, hi, ja, ru, sp, zh` (Arabic, Bengali, German, English, French, Hindi, Japanese, Russian, Spanish, Chinese). **No Vietnamese, Thai, Indonesian, or Filipino/Tagalog code present.** A leading, widely-cited multilingual safety benchmark excludes all Southeast Asian languages by construction.

## Paper 2 — "Benchmarking LLM Guardrails in Handling Multilingual Toxicity"

arXiv 2410.22153, published 2024-10-29. Abstract verbatim: "...we introduce a comprehensive multilingual test suite, spanning seven datasets and over ten languages, to benchmark the performance of state-of-the-art guardrails... Our findings show that existing guardrails are still ineffective at handling multilingual toxicity and lack robustness against jailbreaking prompts."

Full-text search (ar5iv HTML, fetched 2026-09-17) hits:
- "Thai" — FOUND. Context verbatim: "Figure 1: The guardrails are providing inconsistent predictions for English and Thai inputs with the same semantic meaning. In this case, we are using LLaMa-Guard-3 as the guardrail model which supports Thai." — this is the paper's own headline example, a **directly measured** guardrail inconsistency on a named SEA language.
- "Indonesian" — FOUND. Context verbatim: "...we translate the test set into other languages: Chinese, German, Russian, Arabic, Korean, Indonesian, Bengali, and Swahili via Google Translate API. Following previous paper Deng et al. 2023, we separate the language into three groups: high[-resource]..."
- "Vietnamese" — not found anywhere in full text.
- "Bahasa", "Tagalog", "Filipino" — not found.

## Paper 3 — SEA-HELM: Southeast Asian Holistic Evaluation of Language Models

arXiv 2502.14301, published 2025-02-20. Abstract verbatim: "...we present SEA-HELM, a holistic linguistic and cultural LLM evaluation suite that emphasises SEA languages, comprising five core pillars: (1) NLP Classics, (2) LLM-specifics, (3) SEA Linguistics, (4) SEA Culture, (5) Safety. SEA-HELM currently supports Filipino, Indonesian, Tamil, Thai, and Vietnamese." This is the strongest positive hit found: a named Safety pillar, and Vietnamese explicitly named as a supported language, published by AI Singapore per the arXiv listing (org not independently re-verified this pull).

## Paper 4 — ML-Bench & ML-Guard

arXiv 2605.00689, published 2026-05-01 (most recent multilingual safety-guardrail paper found). Abstract verbatim: "...we introduce ML-Bench, a policy-grounded multilingual safety benchmark covering 14 languages... we develop ML-Guard, a Diffusion Large Language Model (dLLM)-based guardrail model..."

Full-text search (ar5iv HTML, 87KB->353KB rendered, fetched 2026-09-17) for common English language names: `Vietnamese, Thai, Indonesian, Bahasa, Tagalog, Filipino, Malay, Burmese, Khmer, Lao, Myanmar, Cebuano, Javanese` — **zero matches, all 12 terms.** The specific 14-language list is not spelled out in the abstract or the sections searched; this is a text-search negative result, not a confirmed exclusion (the paper may use ISO codes or a table/figure not captured as text by the ar5iv renderer) — `unknown — checked ar5iv full-text 2026-09-17, no SEA language name found by string search, could be a renderer/table-extraction limitation`.

## Paper 5 — MrGuard: A Multilingual Reasoning Guardrail

arXiv 2504.15241, published 2025-04-21. Proposes a trained multilingual guardrail model; abstract does not name specific languages tested. Not independently checked for Vietnamese coverage this pull — `unknown — checked abstract only 2026-09-17`.

## Paper 6 — IndoSafety

arXiv 2506.02573, published 2025-06-03. Abstract verbatim: "...we present IndoSafety, the first high-quality, human-verified safety evaluation dataset tailored for the Indonesian context, covering five language varieties: formal and colloquial Indonesian, along with three major local languages: Javanese, Sundanese, and Minangkabau... existing Indonesian-centric LLMs often generate unsafe outputs, particularly in colloquial and local language settings." Bahasa/Indonesian-specific, not Vietnamese or Thai.

## Paper 7 — Low-Resource Languages Jailbreak GPT-4 (Yong et al.)

arXiv 2310.02446, published 2023-10-03. Abstract verbatim: "...by successfully circumventing GPT-4's safeguard through translating unsafe English inputs into low-resource languages. On the AdvBenchmark, GPT-4 engages with the unsafe translated inputs and provides actionable items... 79% of the time..." Full-text search for "Vietnamese" on ar5iv render: **not found.** This paper's tested languages (per repo/paper convention referenced elsewhere in this project's `D:\ai\ai-playground\docs\reference\measurement.md`, which cites the same arXiv id) are genuinely low-resource languages (Zulu, Scots Gaelic, Hmong, Guarani-class), not Vietnamese, which has ~85M speakers and comparatively larger NLP resources. Read: the most-cited "low-resource-language jailbreak" paper is not evidence about Vietnamese specifically — Vietnamese sits in a different resource tier than the languages that paper tested.

## Vietnamese-specific toxicity/safety NLP research exists, separately from guardrail tooling

- arXiv 2103.10069, "Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese," published 2021-03-18 (the ViHSD dataset paper).
- arXiv 2506.00636, "ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances," published 2025-05-31.

Both are academic Vietnamese-language toxicity/hate-speech classification datasets. Neither is cited as an input to, or integrated with, any of the shipping guardrail tools checked below.

## Shipping tool language-support checks

- **Llama Guard 3** (`meta-llama/PurpleLlama`, model card on Hugging Face, fetched via WebFetch 2026-09-17): verbatim quote — "Llama Guard 3 supports content safety for the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai." Thai is the only SEA language named. Vietnamese and Indonesian are absent from this list on the shipping model's own card.
- **NeMo Guardrails** (`github.com/NVIDIA-NeMo/Guardrails`, fetched via WebFetch 2026-09-17): no mention of multilingual support or any named language anywhere in the README/docs content retrieved. Silence, not a denial.
- **Lakera Guard** (`lakera.ai/lakera-guard`, fetched via WebFetch 2026-09-17): verbatim marketing claim — "Observing 100+ languages in real-time." No named language list, no Vietnamese-specific claim, unverifiable as stated.

## WebSearch use this pull

One WebSearch call used to locate the MAS FEAT principles (see `sea-compliance-pulls.md`); none used for language-gap research — arXiv API + ar5iv + gh api + WebFetch covered it without touching quota.

## Caveats

- ar5iv full-text rendering can miss content presented only in tables/figures (raster or non-HTML-table format) — a "not found" string-search result is evidence of absence in the renderable text, not proof the paper never discusses that language.
- No benchmark found that tests Vietnamese guardrail performance with a numeric ASR or accuracy figure specific to Vietnamese — SEA-HELM's paper confirms Vietnamese is *in scope* for its Safety pillar but this pull did not extract a Vietnamese-specific safety score from it (would require reading the SEA-HELM leaderboard/paper body, not done this pass — budgeted out).
- "100+ languages" (Lakera) and any other vendor multilingual claim in `../../../docs/markets/ai-attack-defense.md` is unverified marketing language, consistent with that file's existing caveat that vendor performance claims are self-reported.
