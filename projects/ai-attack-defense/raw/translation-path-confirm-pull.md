# VI<->EN translation path — model ID confirmation — raw pull

Wave 1d, pull date 2026-09-17. Method: HuggingFace Hub HTTP API. This confirms and slightly extends wave 1c's `raw/translation-path-pull.md` finding (which identified the models but did not pull machine-readable gate/licence fields for each exact ID). No weights downloaded — confirming gate-free status and exact IDs only, per this wave's mandate (staging weights judged a follow-on execution step, consistent with wave 1c's prior call).

## Helsinki-NLP/opus-mt-vi-en

- API-confirmed: `"gated": false`, `cardData.license: "apache-2.0"`, 10,036 downloads.
- Files present: `pytorch_model.bin`, `tf_model.h5` (both framework formats available; no safetensors variant seen in the sibling list).
- MarianMT architecture, part of the Helsinki-NLP OPUS-MT project (University of Helsinki).

## Helsinki-NLP/opus-mt-en-vi

- API-confirmed: `"gated": false`, `cardData.license: "apache-2.0"`, 7,364 downloads.
- Same file layout as the reverse-direction model.

## VietAI/envit5-translation (alternative, single bidirectional model)

- API-confirmed: `"gated": false`, `cardData.license: "openrail"`, 6,023 downloads.
- Files present: `flax_model.msgpack`, `pytorch_model.bin`, `spiece.model` (SentencePiece tokenizer), `tf_model.h5` — three framework formats plus tokenizer, all present.
- T5-based, single model handles both directions via a language-prefix instruction (per wave 1c's prior read); not re-verified this pass beyond confirming the gate/licence fields.

## Verdict

Both candidates confirmed exactly as wave 1c described: genuinely ungated (`gated: false` from the API directly, not inferred), free, and downloadable today with a plain unauthenticated HTTP GET — no HuggingFace account, no API token, no licence click-through. Apache 2.0 (Helsinki-NLP pair) is the more permissive licence family of the two; OpenRAIL (VietAI) carries use-based restrictions not read in full this pass or in wave 1c's. Recommendation carried forward unchanged: `Helsinki-NLP/opus-mt-vi-en` + `opus-mt-en-vi` as the default pair if/when a design proceeds to machine-translating a corpus.
