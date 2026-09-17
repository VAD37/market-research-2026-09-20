# Vietnamese <-> English machine translation path — no paid spend

Source: Hugging Face model API (`huggingface.co/api/models/...`, direct curl), Hugging Face model card via WebFetch. Pull date 2026-09-17. Method: direct fetch, no browser tools, no download performed (models are ungated — staging would be a follow-on step, not done in this pull since the task is to identify the option, not execute the benchmark).

## Concrete option: Helsinki-NLP OPUS-MT (MarianMT), bidirectional pair

Two separate small models, one per direction — needed for the settling measurement's round-trip back-translation fidelity check (VI→EN→VI or EN→VI→EN).

| Model | Direction | Licence | Gated? | Size class |
|---|---|---|---|---|
| `Helsinki-NLP/opus-mt-vi-en` | Vietnamese → English | Apache 2.0 | `false` (confirmed via HF API) | Marian, small (~300MB typical for this family) |
| `Helsinki-NLP/opus-mt-en-vi` | English → Vietnamese | Apache 2.0 | `false` (confirmed via HF API) | Marian; `usedStorage` field reports ~2.0GB total across all stored formats (pytorch + tf) — the actual needed single-format download is smaller |

**Reported quality (`opus-mt-vi-en` model card, verbatim):** "BLEU score of 42.8 and chrF score of 0.608 on the Tatoeba test set" — vendor-reported (Helsinki-NLP / OPUS-MT project), not independently verified this pass.

**Invocation (from the model card, standard `transformers` pattern):**
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-vi-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-vi-en")
```
CPU-runnable (Marian models are small enough that GPU is not required for the volumes in this measurement, ~500-2,000 paired items). No API key. Fully offline once weights are downloaded. `transformers` is not currently installed on this machine (per `raw/local-runnability-pull.md`) — a `pip install transformers torch` (or `uv add`) step is needed before use, which is free.

## Alternative option: VietAI/envit5-translation (single bidirectional model)

| Field | Value |
|---|---|
| Model | `VietAI/envit5-translation` |
| Architecture | T5ForConditionalGeneration (T5-base scale) |
| Licence | `openrail` (per HF API `cardData.license`) |
| Gated? | `false` (confirmed via HF API) |
| Direction | Bidirectional — single model handles both `vi→en` and `en→vi` via a language-prefix token in the input (e.g. `"vi: <text>"` per the model card's own widget example) |
| Downloads | 6,023 (HF API `downloads` field, as of 2026-09-17) |
| Training data | `cc100` (per `cardData.datasets`) |

One model instead of two covers both translation directions, which simplifies the back-translation loop (same model, both hops) at the cost of a somewhat larger download (T5-base class, single-format download roughly several hundred MB to ~1GB; the API's `usedStorage: 4403461479` bytes reflects multiple redundant formats — pytorch, tf, flax — stored in the repo, not what a single-format local download requires).

## Recommendation for the settling measurement

Either option satisfies "no paid API spend." **Helsinki-NLP's pair is the safer default** — Apache 2.0 (least restrictive), smaller per-direction footprint, and is the most widely used MT baseline for exactly this language pair (highest ecosystem maturity for a small Marian model). VietAI/envit5 is a reasonable second choice if a single bidirectional model is preferred for pipeline simplicity, but `openrail` licences carry use-based restrictions that should be read in full before shipping anything downstream (not fetched/quoted in full this pass — flagged, not verified).

Neither model was downloaded in this pass — staging the actual weights is a follow-on execution step for whoever runs the benchmark (2c or later), not part of this wave's dataset/baseline-pull mandate. Both are confirmed ungated and free, so download requires no licence acceptance and is in-bounds when it happens.

## Back-translation fidelity filtering — what "discard items whose meaning did not survive" requires

The settling measurement's spec (`docs/plan/niche-and-solutions.md` §4) calls for back-translating a sample and discarding items whose meaning did not survive. This needs a similarity/fidelity metric between the original Vietnamese and the round-tripped Vietnamese (or a VI-EN semantic-similarity check). Not pulled this pass (out of the five assigned gaps) — options that exist and are free/local once `transformers`/`sentence-transformers` are installed: BLEU/chrF between original and round-tripped text (cheap, already computable with the same MT models' own eval metric), or a multilingual sentence-embedding model (e.g. `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, ungated, Apache 2.0 — not independently verified this pass) for cosine-similarity fidelity scoring. Flagged as an open item for whoever executes the measurement, not resolved here.

## Caveats

- BLEU/chrF numbers for the Helsinki-NLP models are vendor-reported (Helsinki-NLP/OPUS-MT project), not independently measured by this pass.
- Neither model's translation quality was tested against actual ViHSD-style informal/slang Vietnamese social-media text (heavy abbreviation, teencode, per `raw/vihsd-vitosa-pull.md`) — general-domain MT models are known to degrade on this register; this is a real risk for the paired VI/EN measurement's fidelity, not evaluated here.
- `openrail` licence terms for VietAI/envit5-translation were not fetched in full text this pass — flagged as unread, not verified permissive-for-this-use.
