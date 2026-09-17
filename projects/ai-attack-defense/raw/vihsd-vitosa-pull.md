# ViHSD / ViToSA — dataset pull

Source: arXiv (export.arxiv.org API + PDF), Hugging Face Datasets API (huggingface.co/api/datasets), nlp.uit.edu.vn/datasets (via WebFetch). Pull date: 2026-09-17. Method: direct HTTP fetch (curl) of arXiv abstract/API pages and PDF, direct fetch of HF dataset-listing API and gated dataset pages, WebFetch of the UIT NLP group's own datasets page. No browser tools used, no account created, no forms submitted.

## CORRECTION TO WAVE 1 / WAVE 2A CITATION

**arXiv 2103.10069 is NOT ViHSD.** Verified via direct fetch of `https://arxiv.org/abs/2103.10069` (citation_title meta tag, verbatim):

> `<meta name="citation_title" content="Constructive and Toxic Speech Detection for Open-domain Social Media Comments in Vietnamese" />`
> `<meta name="citation_author" content="Nguyen, Luan Thanh" /><meta name="citation_author" content="Van Nguyen, Kiet" /><meta name="citation_author" content="Nguyen, Ngan Luu-Thuy" />`
> `<meta name="citation_doi" content="10.1007/978-3-030-79457-6_49" />`

2103.10069 is **UIT-ViCTSD** (Vietnamese Constructive and Toxic Speech Detection dataset, 10,000 comments, 2 tasks: constructive / toxic, CC BY-NC-SA 4.0 per its own abstract page), a sibling paper in the same Springer IEA/AIE 2021 proceedings book (same ISBN prefix 978-3-030-79457-6, different chapter: `_49` vs ViHSD's `_35`), by an overlapping author team (Kiet Van Nguyen, Ngan Luu-Thuy Nguyen appear on both). This is a plausible source of the mix-up: two same-conference, same-lab, same-year papers on adjacent topics.

**The correct arXiv ID for ViHSD is 2103.11528.** Confirmed via `https://export.arxiv.org/api/query?search_query=all:ViHSD`:

> Title: "A Large-scale Dataset for Hate Speech Detection on Vietnamese Social Media Texts"
> Authors: Son T. Luu, Kiet Van Nguyen, Ngan Luu-Thuy Nguyen
> `arxiv:comment`: "IEA/AIE 2021: Advances and Trends in Artificial Intelligence. Artificial Intelligence Practices, pp 415-426"
> `arxiv:doi`: 10.1007/978-3-030-79457-6_35
> Published: 2021-03-22T00:55:47Z (v4 updated 2021-07-20T06:22:08Z)

This matches the citation embedded in the Hugging Face SEACrowd/uit_vihsd dataset card, which was already citing `10.1007/978-3-030-79457-6_35` correctly. **Every reference to "arXiv 2103.10069" for ViHSD in `docs/explore/language-gap.md` and `docs/plan/niche-and-solutions.md` is the wrong ID.** The dataset described (30K+ comments, CLEAN/OFFENSIVE/HATE) is real and exists — only the arXiv identifier is wrong. Flagging in `docs/explore/dataset-baselines.md`; not editing the two files that carry the error (out of scope for this wave).

## ViHSD (arXiv 2103.11528v4) — label schema, verbatim (Table 1 of the paper, full text pulled from PDF)

| Label | Description (verbatim) |
|---|---|
| CLEAN | "The comments have no harassment at all." |
| OFFENSIVE | "The comments contain harassment contents, even profanity words, but do not attack any specific object." |
| HATE | "The comments have harassment and abusive contents and directly aim at an individual or a group of people based on their characteristics, religion, and nationality." (plus 3 documented edge cases: explicit-word direct attack; implicit/no-explicit-word hate; figurative-meaning hate requiring social context) |

Numeric encoding: CLEAN=0, OFFENSIVE=1, HATE=2.

## Item counts per class (Fig. 2 of the paper, exact numbers)

| Split | CLEAN | OFFENSIVE | HATE | Split total |
|---|---|---|---|---|
| TRAIN | 19,886 | 1,606 | 2,556 | 24,048 |
| DEV | 2,190 | 212 | 270 | 2,672 |
| TEST | 5,548 | 444 | 688 | 6,680 |
| **Total** | **27,624** | **2,262** | **3,514** | **33,400** |

Paper states total = 33,400 comments; split proportion 7-1-2 (train-dev-test). Class distribution heavily skewed to CLEAN throughout (matches the paper's own observation).

## Data collection (verbatim, §3.1)

> "We collect users' comments about entertainment, celebrities, social issues, and politics from different Vietnamese Facebook pages and YouTube videos. We select Facebook pages and YouTube channels that have a high-interactive rate, and do not restrict comments. After collected data, we remove the name entities from the comments in order to maintain the anonymity."

## Annotation process (verbatim, §3.3)

> "Our annotation process contains two main phases... The first one is the training phase, which annotators are given a detailed guidelines, and annotate for a sample of data after reading carefully. Then we compute the inter-annotator agreement by Cohen Kappa index (κ)... After all annotators are well-trained, we go to annotation phase. Our annotation phase is inspired from the IEEE peer review process of articles. Two annotators annotate the entire dataset. If there are any different labels between two annotators, we let the third annotators annotate those labels. The fourth annotators annotate if all three annotators are disagreed... The final label are defined by Major voting."

## Inter-annotator agreement (verbatim, §3.4)

> "We randomly take 202 comments from the dataset and give them to four different annotators, denoted as A1, A2, A3 and A4... The final inter-annotator agreement for the dataset is κ = 0.52."

Pairwise Cohen's κ (Table 2): A1-A2 0.46, A1-A3 0.51, A1-A4 0.65, A2-A3 0.47, A2-A4 0.53, A3-A4 0.55. Paper's own characterization (§6, verbatim): "The current inter-annotator agreement of the ViHSD dataset is just in moderate level." Best baseline model (BERT, bert-base-multilingual-cased): 86.88% accuracy, 62.69% macro-F1 (§5.2). Paper's own read of this gap (verbatim, §5.2): "there is a large gap between the accuracy score and the F1-score, which caused by the imbalance in the dataset."

## Licence — verdict: GATED. Not downloaded.

The paper PDF/arXiv page itself states no explicit data licence (a standard Springer conference chapter; arXiv preprint carries arXiv's own non-exclusive distribution licence, not a data licence).

**The authoritative distribution channel is the UIT NLP group's own page, `https://nlp.uit.edu.vn/datasets`.** WebFetch of that page, verbatim quote on the access requirement for ViHSD:

> "Please contact us via email: sonlt@uit.edu.vn (Mr. Son Luu) to sign the corpus user agreement and then receive the corpus."

This is a licence-acceptance gate (a corpus user agreement to be signed). Per the hard rule in this task's instructions — "If it requires a form, an account, or licence acceptance, DO NOT accept anything — record what it requires and stop" — **no agreement was signed, no email was sent, nothing was downloaded from the official channel.**

**Hugging Face mirrors, checked via `https://huggingface.co/api/datasets`:**

| Repo | Gated? | License tag |
|---|---|---|
| `uitnlp/vihsd` (official UIT NLP org account) | **`"gated":"auto"`** — confirmed by direct fetch: raw README request returned "Access to dataset uitnlp/vihsd is restricted. You must have access to it and be authenticated to access it. Please log in." | `mit` (tag on a gated repo — the MIT tag does not override the access gate) |
| `ura-hcmut/UIT-ViHSD` | Not machine-gated, but its own dataset card states (verbatim, quoted by WebFetch of the HF listing description): "This is a copy instance of the original dataset provided by UIT. Please visit https://nlp.uit.edu.vn/datasets to obtain a usage permission before using this dataset." | `cc-by-nc-sa-4.0` |
| `sonlam1102/vihsd` | Referenced inside uitnlp's own card as the loader (`load_dataset("sonlam1102/vihsd", ...)`) — likely the first author's personal upload. Not independently confirmed ungated in this pass. | not confirmed |
| `SEACrowd/uit_vihsd` | Not machine-gated | `license:unknown` |
| `htdung167/ViHSD`, `phucdev/ViHSD`, `stair-lab/ViHSD`, `An24/ViHSD`, `clapAI/ViHSD`, `KalvinPhan/ViHSD`, `visolex/ViHSD`, `leminhhung0101/R-ViHSD` | Not machine-gated per API listing | No license tag present on most; unverified provenance |
| `vominhmanh/vihsd-explainable*`, `dongeov/vihsd-explainable`, `Greeed88/vihsd-explainable*` | Not machine-gated | `cc-by-4.0` — but these are **derivative/synthetic** (LLM-generated explanations layered on top of the base ViHSD text), not the base dataset under its own terms |

**Decision: treat as gated, do not stage.** The dataset's own maintainers (UIT NLP, the paper's authors) require a signed corpus user agreement through their official channel and gate their own HF org account the same way. Numerous un-gated third-party re-uploads exist on Hugging Face with inconsistent or absent licence tags, but downloading through one of those would route around the licensor's stated terms rather than satisfy them — this pass does not do that. **No ViHSD data of any kind is staged in `prototype/data/`.**

## ViToSA (arXiv 2506.00636v1) — briefer treatment, per instructions

Confirmed correct citation (this one was right in wave 1/2a's docs). Verbatim arXiv API record:

> Title: "ViToSA: Audio-Based Toxic Spans Detection on Vietnamese Speech Utterances"
> Authors: Huy Ba Do, Vy Le-Phuong Huynh, Luan Thanh Nguyen
> `arxiv:comment`: "Accepted for presentation at INTERSPEECH 2025"
> Abstract (verbatim): "...introduces ViToSA (Vietnamese Toxic Spans Audio), the first dataset for toxic spans detection in Vietnamese speech, comprising 11,000 audio samples (25 hours) with accurate human-annotated transcripts..."

**Not text hate-speech classification — audio toxic-span detection.** Not a direct substitute for ViHSD in the settling measurement (guardrails under test take text, not raw audio, so ViToSA's transcripts could theoretically serve as a second text source, but its item unit is a labeled span inside a transcript, not a document-level CLEAN/OFFENSIVE/HATE label — different task shape).

**Licence — gated, per Hugging Face dataset listing (`huggingface.co/api/datasets?search=ViToSA`):**

| Repo | Gated? | License tag |
|---|---|---|
| `UIT-ViToSA/ViToSA-1.0` (official, "developed by researchers from the University of Information Technology, VNU-HCM") | `"gated":"auto"` | `cc-by-nc-nd-4.0` |
| `UIT-ViToSA/ViToSA-2.0` (ICASSP 2026 follow-up) | `"gated":"auto"` | `apache-2.0` |

Both official ViToSA repos are gated regardless of the license tag shown (the same uitnlp/HF pattern as ViHSD: a permissive-looking tag on a gated repo). **Not downloaded.** No non-gated third-party mirror was found for ViToSA in this pass (unlike ViHSD, which has many).

## Caveats

- The arXiv-ID correction (2103.10069 → 2103.11528 for ViHSD) is a citation error carried through `docs/explore/language-gap.md` and `docs/plan/niche-and-solutions.md`. This file corrects it for wave 1c's own use; it does not edit those files per this wave's boundary.
- `sonlam1102/vihsd`'s gate status was not independently checked (HF API redirected the direct query; only referenced indirectly via uitnlp's card). Labeled `unknown — checked huggingface.co/api/datasets 2026-09-17`.
- The exact text of the HF "gated:auto" access-request form (what it asks for) was not retrieved — the page renders it client-side and was not fetched via browser tooling (out of bounds for this wave). Only the fact of gating and the official page's "corpus user agreement" language were confirmed.
- No numeric ViHSD score for any of the three guardrails under test (Llama Guard 3, omni-moderation-latest, Lakera) exists anywhere in this pull — the ViHSD paper only reports its own baseline classifiers (Text-CNN, GRU, BERT variants), none of which are the guardrails in the settling measurement's spec.
