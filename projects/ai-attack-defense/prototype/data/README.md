# prototype/data/ — staging status

**Nothing is staged here.** Checked 2026-09-17 (wave 1c, dataset + baseline pulls).

## ViHSD (arXiv 2103.11528 — NOT 2103.10069, see `../../raw/vihsd-vitosa-pull.md` for the citation correction)

**Not downloaded. Gated.** Official source `nlp.uit.edu.vn/datasets` requires a signed "corpus user agreement" (email to sonlt@uit.edu.vn) before release. The official Hugging Face org copy (`uitnlp/vihsd`) is independently gated (`"gated":"auto"`, confirmed by API and by a direct unauthenticated fetch returning "Access to dataset uitnlp/vihsd is restricted..."). Per this project's hard rule ("no account creation, no signups, no licence acceptance"), no agreement was signed and nothing was downloaded — from the official channel or from any of the several un-gated third-party Hugging Face mirrors found (downloading via a mirror would route around the licensor's stated terms, which this pass treats as equivalent to not having permission). Full detail, all mirrors checked, and licence text quoted verbatim: `../../raw/vihsd-vitosa-pull.md`.

## ViToSA (arXiv 2506.00636)

**Not downloaded. Gated.** Both official Hugging Face repos (`UIT-ViToSA/ViToSA-1.0`, `UIT-ViToSA/ViToSA-2.0`) are `"gated":"auto"`. Also out of scope by task shape — it's audio toxic-span detection (11,000 audio clips + transcripts), not text-level CLEAN/OFFENSIVE/HATE classification, so it would not directly substitute for ViHSD in the settling measurement even if it were ungated. Detail: `../../raw/vihsd-vitosa-pull.md`.

## SEA-HELM's derived Vietnamese toxicity sample (`aisingapore/Safety-Toxicity-Detection`)

**Not downloaded. Also gated** (`"gated":"auto"` on Hugging Face). This is itself a 1,000-item sample drawn from ViHSD, so staging it would face the same underlying-licence question as ViHSD directly (it's licensed `cc-by-nc-sa-4.0`/`cc-by-nc-3.0`/`cc-by-nc-4.0` per source dataset, and is gated regardless of the tag). Detail: `../../raw/sea-helm-safety-pull.md`.

## Translation models (for the VI/EN paired condition)

**Identified, not downloaded this pass** (staging weights was judged a follow-on execution step, not part of this wave's dataset/baseline-pull mandate). Both are ungated, free, Apache-2.0/OpenRAIL:
- `Helsinki-NLP/opus-mt-vi-en` + `Helsinki-NLP/opus-mt-en-vi` (recommended default pair)
- `VietAI/envit5-translation` (single bidirectional alternative)

Detail: `../../raw/translation-path-pull.md`.

## Net effect on the settling measurement

The dataset the settling measurement is specified against (ViHSD) cannot be staged in this repository without either (a) signing UIT's corpus user agreement (a step this wave is barred from taking and did not take), or (b) using an unofficial mirror that bypasses the licensor's terms (not done). **Whoever runs the benchmark must first decide whether to sign the UIT agreement** — that is a decision for a human or a later wave with the authority to accept terms on the project's behalf, not something resolved by this pull.

---

# Wave 1d additions (2026-09-17, ungated-corpus scout) — appended, nothing above edited

Full detail: `../../docs/explore/ungated-path.md`, `../../raw/ungated-vietnamese-corpora-pull.md`, `../../raw/ungated-guardrails-pull.md`.

## ViHOS/ — STAGED

Source: `github.com/phusroyal/ViHOS` (author's own repo, arXiv 2301.10186, EACL 2023). **Licence: MIT** (whole repo, quoted verbatim in the raw pull). Pull date: 2026-09-17. Ungated — plain unauthenticated download.

Files: `Span_Extraction_based_version/train.csv` (8,853 rows observed), `Span_Extraction_based_version/dev.csv` (1,113 rows observed), `Test_data/test.csv` (1,107 rows observed), `README.md`, `LICENSE`, `data_README.md`. Paper's stated counts: 8,844/1,106/1,106 comments (small discrepancy vs. observed row counts, not resolved). Schema: `content` (raw comment text) + `index_spans` (character indices of hate/offensive span, `[]` if clean) — comment-level toxic/clean is derivable. Native Vietnamese, human-annotated, **not NE-anonymized** (unlike ViHSD — spot-checked rows show apparent real personal names).

## MultiJail/ — STAGED

Source: `huggingface.co/datasets/DAMO-NLP-SG/MultiJail` (arXiv 2310.06474, ICLR 2024). **Licence: MIT**, `gated:false` confirmed via HF API. Pull date: 2026-09-17.

File: `MultiJail.csv` (344,347 bytes). Card states 315 English unsafe prompts, each **manually translated by native speakers** into 9 languages including Vietnamese (categorized "high-resource" alongside Chinese and Italian) — every row carries the same prompt in all 10 languages side by side, so this is a ready-made paired VI/EN adversarial-prompt set with no translation step needed. Every row is an unsafe/harmful prompt by design (published academic red-team corpus).

## SEAHELM-aegis2-vi-en/ — STAGED

Source: `github.com/aisingapore/SEA-HELM`, path `seahelm_tasks/safety/safeguard/general/data/`. **Licence: MIT** (repo-level). Pull date: 2026-09-17. Never HF-gated — plain files in a public code repo (this is the exact paired-EN/VI Aegis2 task wave 1c and wave 2b found "committed but switched off pending data cleanup"; the files themselves carry no restriction beyond the repo's MIT licence).

Files: `vi_general.jsonl` (838,860 bytes, 600 rows), `en_general.jsonl` (625,065 bytes, 600 rows, same items paired), `README.md` (the task-omission note), `task_config.yaml` (full prompt templates, S1–S14 taxonomy), `LICENSE`. Machine-translated from NVIDIA's English Aegis2 dataset — not native Vietnamese (flagged, unlike ViHOS and MultiJail).

## Translation models — confirmed ungated, still NOT downloaded (unchanged from wave 1c)

Re-confirmed via HF API this wave (`../../raw/translation-path-confirm-pull.md`): `Helsinki-NLP/opus-mt-vi-en` (`gated:false`, apache-2.0, 10,036 downloads) and `opus-mt-en-vi` (`gated:false`, apache-2.0, 7,364 downloads). Still not staged — not needed for MultiJail or the SEA-HELM pair (both already paired), only relevant if ViHOS is the chosen corpus and an English arm is wanted.

## Net effect, updated

The measurement can run today, zero licence acceptance, on a substitute corpus (ViHOS, MultiJail, or the SEA-HELM pair — pick one per `../../docs/explore/ungated-path.md`'s closing verdict) against Qwen3Guard-Gen-0.6B (open weights, Apache 2.0, fits this machine's free VRAM without quantization) and/or `omni-moderation-latest` / Azure AI Content Safety (free-tier hosted, no content-licence gate). ViHSD itself remains gated and unstaged — that has not changed.
