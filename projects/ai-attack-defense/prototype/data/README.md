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
