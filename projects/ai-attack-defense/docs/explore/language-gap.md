# Vietnamese / Southeast Asian language gap in AI safety evaluation

Explore phase, 2026-09-17. Source: `../../raw/language-gap-pulls.md` (arXiv API + full-text search, GitHub repo inspection, WebFetch of three shipping tools' own docs). Question from the project brief: is the "Vietnamese-language evaluation is thin ground" premise supported, including evidence against it.

## The finding, stated directly

**Real, but narrower and more nuanced than "Vietnamese is totally unaddressed."** The evidence splits three ways:

1. **Major general-purpose multilingual safety benchmarks exclude Southeast Asian languages entirely.** XSafety (arXiv 2310.00905, 2023-10-02) — a widely-cited 10-language, 14-issue-type multilingual safety benchmark — covers Arabic, Bengali, German, English, French, Hindi, Japanese, Russian, Spanish, Chinese. Confirmed via the benchmark's own GitHub repo folder structure (`gh api`, 2026-09-17): zero SEA languages. ML-Bench (arXiv 2605.00689, 2026-05-01, the newest multilingual safety-guardrail benchmark found), 14 languages: a full-text search for Vietnamese/Thai/Indonesian/Bahasa/Tagalog/Filipino/Malay/Burmese/Khmer/Lao/Myanmar/Cebuano/Javanese returned zero matches on all twelve terms.

2. **Thai has a measured, documented guardrail-performance gap. Vietnamese does not — because it has not been directly tested by name in any benchmark found this pass.** "Benchmarking LLM Guardrails in Handling Multilingual Toxicity" (arXiv 2410.22153, 2024-10-29) leads its own paper with a figure captioned: "guardrails are providing inconsistent predictions for English and Thai inputs with the same semantic meaning... we are using LLaMa-Guard-3 as the guardrail model which supports Thai." That is a shipping guardrail, tested, and shown inconsistent on a SEA language it claims to support. The same paper's translated toxicity test set includes Indonesian, not Vietnamese. No paper found in this pass runs that same guardrail-inconsistency test on Vietnamese specifically.

3. **A dedicated SEA-focused benchmark does cover Vietnamese, with a named Safety pillar.** SEA-HELM (arXiv 2502.14301, 2025-02-20), from AI Singapore per the listing: "SEA-HELM currently supports Filipino, Indonesian, Tamil, Thai, and Vietnamese," across five pillars including "(5) Safety." This is the one benchmark found that puts Vietnamese safety evaluation on the map by name. Its actual Vietnamese safety scores were not extracted this pass (would require reading the paper body/leaderboard, budgeted out) — its existence is confirmed, its findings are not yet summarized here.

## Shipping guardrails: what they claim, checked directly

| Tool | Vietnamese support claim | Source |
|---|---|---|
| Llama Guard 3 (Meta, Purple Llama) | **Not supported.** Model card verbatim: "Llama Guard 3 supports content safety for the following languages: English, French, German, Hindi, Italian, Portuguese, Spanish, Thai." | Hugging Face model card, fetched 2026-09-17 |
| NeMo Guardrails (NVIDIA) | **No claim either way.** No mention of multilingual support anywhere in the repo's README/docs | GitHub repo, fetched 2026-09-17 |
| Lakera Guard | **Vague, unverifiable.** Marketing copy: "Observing 100+ languages in real-time" — no named language list | lakera.ai, fetched 2026-09-17 |

Of the three most-cited shipping guardrails checked, exactly one publishes a language list, and it does not include Vietnamese. The other two neither confirm nor deny — silence, not evidence of support.

## Evidence against the "Vietnamese is low-resource and therefore jailbreak-vulnerable" framing

The most-cited paper on cross-lingual jailbreak vulnerability, "Low-Resource Languages Jailbreak GPT-4" (Yong et al., arXiv 2310.02446, 2023-10-03, 79% ASR via translation), does **not** test Vietnamese — a full-text search found no mention of it. That paper's tested languages are genuinely low-resource (Zulu, Scots Gaelic, Hmong, Guarani-class, per the same paper cited independently in this machine's `D:\ai\ai-playground\docs\reference\measurement.md`). Vietnamese has roughly 85 million speakers and a comparatively developed NLP research base — it sits in a different resource tier. **The "low-resource language jailbreak" literature is not, by default, evidence about Vietnamese.** Separately, dedicated Vietnamese-language toxicity/hate-speech research does exist as academic NLP work — ViHSD (arXiv 2103.10069, 2021-03-18) and ViToSA (arXiv 2506.00636, 2025-05-31) — meaning the raw research material to build a Vietnamese safety classifier exists. It is simply not integrated into any shipping guardrail checked in this pass.

## Read for the planner

The gap is not "nobody has ever studied Vietnamese safety." It is: **no shipping, commercially-deployed guardrail confirms Vietnamese support, and no benchmark found in this pass has run the same kind of direct guardrail-inconsistency test on Vietnamese that arXiv 2410.22153 ran on Thai.** SEA-HELM proves Vietnamese safety evaluation is an active, current (2025-02) research topic — the wedge is not "invent Vietnamese safety research from nothing," it is "there is no product, and even the newest general multilingual-safety benchmarks (ML-Bench, 2026-05) still skip the region." That is a narrower, more defensible claim than "Vietnamese is unaddressed," and it is buildable evidence for a "guardrail regression testing for Vietnamese" niche — provided the prototype cites SEA-HELM and the ViHSD/ViToSA datasets rather than claiming to be first.

## Caveats

- No numeric Vietnamese-specific guardrail ASR or accuracy figure was found or extracted in this pass — the strongest claim available is "excluded from major benchmarks" and "no shipping tool confirms support," not "measured X% gap for Vietnamese specifically." SEA-HELM likely has such a number; extracting it is unfinished work for a follow-up pass.
- ML-Bench's exact 14-language list was not confirmed beyond a full-text string search — the paper may use ISO codes or a table format the fetch renderer did not surface as searchable text. Labeled `unknown — checked ar5iv full-text 2026-09-17` in the raw file.
- MrGuard (arXiv 2504.15241) was checked only at the abstract level; its actual tested-language list was not extracted this pass.
- Lakera's "100+ languages" claim is unverifiable marketing copy, consistent with this repo's existing caveat that vendor performance claims are self-reported and unverified.
- This file answers the coverage/evidence question. It does not size Vietnamese-speaking demand for such a tool or identify a buyer — that is `sea-compliance-triggers.md` and the customer-side research already in `../../../docs/customers/first-customers.md`.
