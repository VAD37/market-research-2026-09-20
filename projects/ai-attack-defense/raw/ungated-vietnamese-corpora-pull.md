# Ungated Vietnamese toxicity/safety corpora — raw pull

Wave 1d, pull date 2026-09-17. Method: direct fetch — HuggingFace Datasets HTTP API (`huggingface.co/api/datasets/...`), `gh api` against GitHub (authenticated, no browser), `raw.githubusercontent.com` file downloads, arXiv `export.arxiv.org` API. No browser tools, no account creation, no licence acceptance.

## FOUND — ungated, downloaded, staged in `prototype/data/`

### 1. ViHOS (Vietnamese Hate and Offensive Spans)

- **Paper**: arXiv 2301.10186 ("ViHOS: Hate Speech Spans Detection for Vietnamese", EACL 2023 Main Conference). Authors: Phu Gia Hoang, Canh Duc Luu, Khanh Quoc Tran, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen (UIT — same lab that publishes ViHSD).
- **Official repo**: `github.com/phusroyal/ViHOS` (author's own repo — "phusroyal" = Phu [Gia] Hoang, first author). 38 stars. Default branch `master`.
- **Licence, verbatim (LICENSE file, fetched via `gh api repos/phusroyal/ViHOS/contents/LICENSE`)**:
  ```
  MIT License

  Copyright (c) 2023 Phu Hoang Gia

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions: ...
  ```
  Licence covers the whole repo, including the `data/` folder — no separate data licence, no gate, no HF gating check needed (this is a GitHub repo, not an HF dataset).
- **Disclaimer, verbatim (README.md)**: "This project contains real comments that could be considered profane, offensive, or abusive."
- **Item counts, verbatim (README.md)**: "ViHOS contains 26,476 human-annotated spans on 11,056 comments (5,360 comments have hate and offensive spans, and 5,696 comments do not)." Splits: "Train set: 8,844 comments. Dev set: 1,106 comments. Test set: 1,106 comments."
- **Observed on download** (2026-09-17): `data/Span_Extraction_based_version/train.csv` = 8,853 data rows (8854 lines incl. header), `dev.csv` = 1,113 data rows, `data/Test_data/test.csv` = 1,107 data rows. Close to the paper's stated 8,844/1,106/1,106 (small discrepancy not resolved — could be blank-line artifacts or a later data revision; not investigated further).
- **Label schema**: span-level BIO tagging (`B-T`/`I-T`/`O`) for hate/offensive spans within a comment (Sequence-labeling version), or `content` + `index_spans` (character indices of the toxic span, empty list `[]` if none) in the Span-Extraction version used here. Comment-level toxic/clean is derivable: a comment with a non-empty `index_spans` list is toxic (hate-or-offensive), empty list is clean — this gives a binary toxic/clean label per comment, close to but not identical to ViHSD's 3-class CLEAN/OFFENSIVE/HATE.
- **Native or machine-translated**: Native Vietnamese, human-annotated (crowdsourced per HF mirror `cardData`: `annotations_creators: crowdsourced`). Collected from social media (same general provenance family as ViHSD).
- **NOT NE-anonymized**: unlike ViHSD, spot-checked rows show what appear to be real personal names left in the comment text (e.g. row 4 of `train.csv`: `"Giang Giang Đỗ Thị Ngọc Hà trend mới kìa kìa"`). Flag for whoever uses this data downstream — the original authors published it this way under MIT, but a derivative publication should consider re-redacting.
- **Downloads with no account, no agreement**: confirmed — plain `curl` against `raw.githubusercontent.com`, HTTP 200, no auth header, no redirect to a login/agreement page.
- **Third-party HF mirrors also found, not used** (repo is already ungated at the source, so no need to route through a mirror): `htdung167/ViHOS` (gated:false, downloads:18), `phusroyal/ViHOS` (gated:false, license:mit, downloads:128 — this is the author's own HF mirror, consistent with the GitHub repo), `visolex/ViHOS` (gated:false, downloads:36).
- **Staged**: `prototype/data/ViHOS/` — `Span_Extraction_based_version/{train,dev}.csv`, `Test_data/test.csv`, `README.md`, `LICENSE`, `data_README.md`. Total ~1.28MB.

### 2. MultiJail (DAMO-NLP-SG)

- **Paper**: arXiv 2310.06474 ("Multilingual Jailbreak Challenges in Large Language Models", Deng, Zhang, Pan, Bing, ICLR 2024).
- **HF dataset**: `huggingface.co/datasets/DAMO-NLP-SG/MultiJail`. API-confirmed: `"gated": false`, `"license": "mit"`, 969 downloads, `sha: 93d65c778925d55973b9ff30c7bccc8545494eb6`.
- **GitHub repo**: `github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs` (MIT-licensed at the GitHub level too, per `gh api repos/.../license` → `spdx_id: MIT`).
- **Content, verbatim (dataset card + GitHub README)**: "We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages. The languages were categorized based on resource availability... **High-resource languages: Chinese (zh), Italian (it), Vietnamese (vi)**. Medium-resource languages: Arabic (ar), Korean (ko), Thai (th). Low-resource languages: Bengali (bn), Swahili (sw), Javanese (jv)."
- **Translation method, verbatim (GitHub README, `github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs`)**: "We carefully gather English harmful queries and **manually translate them by native speakers** into 9 non-English languages, ranging from high-resource to low-resource." — i.e. Vietnamese items are native, human-translated, NOT machine-translated.
- **Structure**: single CSV, columns `id, source, tags, en, zh, it, vi, ar, ko, th, bn, sw, jv` — every row carries the SAME prompt across all 10 languages side by side. This gives a perfectly paired VI/EN adversarial-prompt set with zero additional translation or fidelity-filtering step needed.
- **Downloaded** 2026-09-17: `MultiJail.csv`, 344,347 bytes. Header + 442 raw lines (`wc -l`); actual record count is `unknown — precise count needs a CSV-aware parser because some cells contain embedded newlines; the dataset card states 315 rows` — record it as 315 per the card, not the raw line count.
- **Content warning**: every row is an unsafe/harmful prompt (sexual exploitation, violence, etc. — categories are in the `tags` column) by design; this is the published academic red-team corpus, not new offensive material generated by this pull.
- **Ethics statement, verbatim**: "We are aware of the potential misuse of our findings and emphasize that our research is solely for academic purposes and ethical use... we commit to open-sourcing the data used in our study."
- **Staged**: `prototype/data/MultiJail/MultiJail.csv` (344,347 bytes), `README.md`.

### 3. SEA-HELM's `safeguard_general` Vietnamese/English pair (Aegis2-taxonomy, machine-translated)

- **Source**: `github.com/aisingapore/SEA-HELM`, path `seahelm_tasks/safety/safeguard/general/data/`. Repo licence: MIT (`gh api repos/aisingapore/SEA-HELM` → `license.spdx_id: MIT`).
- This is the exact resource wave 1c and wave 2b both identified as existing but "switched off pending data cleanup" — it is **not gated**, it is plain files in a public MIT-licensed GitHub repo. No HF gate applies because it was never published as a separate HF dataset; it lives as flat `.jsonl` files in the code repo.
- **Files fetched** (`raw.githubusercontent.com/aisingapore/SEA-HELM/main/...`): `vi_general.jsonl` (838,860 bytes, 600 lines) and `en_general.jsonl` (625,065 bytes, 600 lines) — same 600 items, Vietnamese and English versions of each, confirmed same row count.
- **Note on `data/README.md`, verbatim**: "Omitted from the safeguard category pending further checks/data cleanup for the dataset (e.g. aegis2)." — this is a task-activation note in the benchmark harness, not a data-licence restriction. The files themselves carry no separate licence marker; they inherit the repo's MIT licence.
- **Schema, from sample rows**: each line is a JSON object `{"prompt_label": "Có hại"|"Sạch"/"Harmful"|"Safe", "response_label": ..., "prompts": [{"prompt_text": ..., "response_text": ...}]}`. Labels follow the Llama-Guard-style S1–S14 taxonomy (from `config.yaml`: Violent Crimes, Non-Violent Crimes, Sex Crimes, Child Exploitation, Defamation, Specialized Advice, Privacy, Intellectual Property, Indiscriminate Weapons, Hate, Self-Harm, Sexual Content, Elections, Code Interpreter Abuse).
- **Provenance**: machine-translated from NVIDIA's Aegis2 English dataset (per wave 1c's `raw/sea-helm-safety-pull.md`) — NOT native Vietnamese. Flagged accordingly.
- **Staged**: `prototype/data/SEAHELM-aegis2-vi-en/` — `vi_general.jsonl` (838,860 bytes), `en_general.jsonl` (625,065 bytes), `README.md`, `task_config.yaml` (the full task definition incl. per-language prompt templates), `LICENSE` (SEA-HELM repo's MIT licence, 1,069 bytes).

## CHECKED, NOT USED — Vietnamese absent or licence unsuitable

| Candidate | Source checked | Vietnamese present? | Licence / gate | Verdict |
|---|---|---|---|---|
| RTP-LX (Microsoft) | `huggingface.co/datasets/ToxicityPrompts/RTP-LX` API — full sibling file list (28 language-code parquet files) | **No.** Full list: ar, bcms, cs, da, de, en, es, fi, fr, he, hi, hu, id, it, ja, ko, nl, no_nb, pl, pt, ru, sv, sw, th, tr, uk, zh_hans, zh_hant — no `vi` | odc-by, ungated | Not usable — Vietnamese absent |
| PolygloToxicityPrompts | `huggingface.co/datasets/ToxicityPrompts/PolygloToxicityPrompts` API, `cardData.language` | **No.** 17 languages: en, nl, pl, sv, ru, hi, ja, ko, zh, es, fr, it, id, ar, cs, de, pt | cc-by-4.0, ungated | Not usable — Vietnamese absent |
| Multilingual HateCheck | `mteb/multi-hatecheck` + individual `Paul/hatecheck-*` HF repos | **No.** Languages found: Arabic, Dutch, French, German, Hindi, Italian, Mandarin, Polish, Portuguese, Spanish | varies, ungated | Not usable — Vietnamese absent |
| Aya RedTeaming | `CohereLabs/aya_redteaming` API, `cardData.language` | **No.** 8 languages: en, hi, fr, es, ar, ru, sr, tl (Tagalog, not Vietnamese) | apache-2.0, ungated | Not usable — Vietnamese absent |
| Jigsaw Multilingual Toxic Comment Classification | `serjtroshin/jigsaw_multilingual` HF mirror | Mirror repo is empty (only `.gitattributes`); original Kaggle competition data (per general knowledge, not independently re-verified this pass) covers tr/es/it/pt/fr/ru + en, no Vietnamese | n/a | Not usable — empty mirror, and Vietnamese was never in this set |
| UIT-ViCTSD ("Constructive and Toxic Speech Detection", the dataset wave 1/2a originally mis-cited as ViHSD) | `tarudesu/ViCTSD`, `SEACrowd/uit_victsd` HF mirrors | Yes (native Vietnamese) | HF mirrors show `gated:false` but **no confirmed licence tag** on either mirror (`license: None` / `license: unknown`); wave 1c's earlier finding (in `dataset-baselines.md`'s sibling-paper note) associates the official UIT release with CC BY-NC-SA 4.0, which was not independently re-confirmed this pass | **Not staged** — licence unclear/unconfirmed on the mirrors, and if UIT's own CC BY-NC-SA terms apply, downloading via an unofficial mirror without the licence text raises the same "routing around the licensor" concern flagged for ViHSD. Recorded as a candidate for a future pass that reaches the official UIT source directly, not downloaded here. |
| SEA-HELM `toxicity_detection` HF dataset | `aisingapore/Safety-Toxicity-Detection` | Yes (it's ViHSD itself, resampled) | **Gated** (`"gated":"auto"` per wave 1c's prior finding) — this is a repackaging of ViHSD and inherits the same gate | Not usable — gated |

## Method notes

- HF search endpoint `huggingface.co/api/datasets?search=<query>` matches on dataset id/slug more than description; several queries with spaces (e.g. "vietnamese hate speech", "vietnamese offensive") returned zero hits even though relevant datasets exist under other names — cross-checked by trying dataset-name-shaped queries (ViHOS, VOZ-HSD, UIT-VSFC) instead.
- `VOZ-HSD` mirrors were found (`gamusa/VOZ-HSD-Hate-Comments`, `tarudesu/VOZ-HSD`, others) but not pursued in depth this pass — provenance (scraped Vietnamese forum "VOZ") and licensing were not verified, and ViHOS + MultiJail + the SEA-HELM pair already covered the priority need. Flagged as an open follow-up, not a negative finding.
- `UIT-VSFC` (Vietnamese Students' Feedback Corpus — sentiment/topic, not hate speech) mirrors were found but are out of scope (wrong task shape) and not pursued.
