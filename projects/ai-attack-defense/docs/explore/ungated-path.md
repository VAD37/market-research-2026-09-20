# The ungated path — can the Vietnamese guardrail measurement run with zero licence acceptance?

Wave 1d, 2026-09-17. Scope: wave 1c found the settling measurement in `docs/plan/niche-and-solutions.md` §4 blocked on two licence gates — ViHSD (email agreement to UIT) and Llama Guard 3 8B (Meta manual approval). This file hunts for a way to run the same *kind* of measurement — a shipping guardrail product tested on paired Vietnamese/English input — without accepting any licence, creating any account, or clicking through any gate. Sources: `raw/ungated-vietnamese-corpora-pull.md`, `raw/ungated-guardrails-pull.md`, `raw/perspective-api-pull.md`, `raw/translation-path-confirm-pull.md`, `raw/gated-resources-summary.md`. Method throughout: direct fetch (HuggingFace API, GitHub via `gh api`, arXiv, a Googlebot-UA `curl` trick for one JS-rendered vendor page) — no browser tools, no account creation, no licence acceptance, no paid calls. Does not edit `docs/explore/dataset-baselines.md`, `docs/plan/`, or `docs/review/` — contradictions with those files are noted here, side by side.

## 1. Ungated Vietnamese corpora

| Dataset | Source | Licence (verbatim) | Items | Label schema | Native or MT | No account/no agreement? |
|---|---|---|---|---|---|---|
| **ViHOS** | `github.com/phusroyal/ViHOS`, arXiv 2301.10186, EACL 2023 | MIT, full repo incl. data | 26,476 spans / 11,056 comments (8,853/1,113/1,107 train/dev/test observed on download) | Span-level hate/offensive BIO tags; comment-level toxic/clean derivable from non-empty span list | Native, human-annotated (crowdsourced) | **Yes** — plain `curl`, HTTP 200, no auth |
| **MultiJail** | `huggingface.co/datasets/DAMO-NLP-SG/MultiJail`, arXiv 2310.06474, ICLR 2024 | MIT | 315 prompts x 10 languages, paired row-for-row | No CLEAN/OFFENSIVE/HATE labels — every row is an unsafe/harmful prompt (harm-category `tags` column); binary "should this be flagged" by design | **Native, human-translated by native speakers** (verbatim: "We carefully gather English harmful queries and manually translate them by native speakers") | **Yes** — `gated:false` on HF API |
| **SEA-HELM `safeguard_general` vi/en pair** | `github.com/aisingapore/SEA-HELM`, path `seahelm_tasks/safety/safeguard/general/data/` | MIT (repo-level) | 600 items, vi and en, row-for-row paired | Safe/Harmful per Llama-Guard-style S1–S14 taxonomy | Machine-translated from NVIDIA Aegis2 (English) | **Yes** — plain files in a public MIT repo, never HF-gated |

**Checked and rejected** (Vietnamese absent, or licence unsuitable): RTP-LX (28 languages, no `vi`), PolygloToxicityPrompts (17 languages, no `vi`), Multilingual HateCheck (10 languages, no `vi`), Aya RedTeaming (8 languages, no `vi`), Jigsaw Multilingual (7 languages historically, no `vi`; HF mirror empty), UIT-ViCTSD (native Vietnamese, but licence unconfirmed on the ungated mirrors — not staged), `aisingapore/Safety-Toxicity-Detection` (a ViHSD resample, inherits ViHSD's gate). Full detail in `raw/ungated-vietnamese-corpora-pull.md`.

**Contradiction with `docs/explore/dataset-baselines.md` (wave 1c)**: that file states "the raw material exists and is public: ViHSD... and ViToSA... neither integrated into any shipping guardrail checked" and treats the dataset gate as the binding constraint. This wave's finding does not contradict that ViHSD itself is gated — it stands. What changes is the premise that ViHSD is the *only* usable Vietnamese corpus: three ungated substitutes now exist, one of them (the SEA-HELM pair) built for exactly the paired-condition design 2a specified, and MultiJail requiring no translation step at all.

## 2. Ungated guardrails naming Vietnamese or silent

| Guardrail | Gate | Licence | Size / VRAM fit (6.7GB free) | Language claim (verbatim) | Vietnamese named? |
|---|---|---|---|---|---|
| **Qwen3Guard-Gen/Stream, 0.6B/4B/8B** | **None** (`gated:false`) | Apache 2.0 | 0.6B fits without quantization (~1.5GB); 4B (~8.8GB) and 8B (~16.4GB) need 8-bit or 4-bit quantization, not verified empirically | "Multilingual Support: Qwen3Guard-Gen supports 119 languages and dialects" | Not by name in the Qwen3Guard paper itself, but the Qwen3 base model's own technical report **explicitly benchmarks "Vietnamese (vi)"** (Table 33) and lists `vie Latn` in its supported-language table (Table 36) |
| **IBM Granite Guardian 3.0–3.3, 2B–8B** | **None** (`gated:false`) | Apache 2.0 | Fits comfortably at smaller sizes | `language: [en]` machine-readable tag, no prose claim beyond it | No — explicit English-only, consistently across four versions |
| **Detoxify / `unitary/multilingual-toxic-xlm-roberta`** | **None** (`gated:false`) | Apache 2.0 | Small, fits easily | "trained on 7 different languages... english, french, spanish, italian, portuguese, turkish or russian" | No — explicit negative |
| **OpenSafetyLab/MD-Judge-v0.1** | **None** (`gated:false`) | Apache 2.0 | Small | `language: [en]` | No |
| WildGuard | Self-serve click-through (`gated:auto`) | Apache 2.0 | N/A — gated | `language: [en]` | No, and gated anyway |
| Aegis 1.0 / NemoGuard adapters | Effectively gated (adapter needs Meta's manual-gate base) | Llama licence + NVIDIA terms | N/A | `language: [en]` | No, and gated anyway |
| Llama Guard 3 8B / 1B, ShieldGemma | Manual (Meta / Google) | — | — | en/de/fr/it/pt/hi/es/th (LG3); English-only (SG) | No, and gated anyway |

Full detail, including the LoRA-adapter/base-model gate nuance, in `raw/ungated-guardrails-pull.md`.

## 3. Perspective API — checked directly, verbatim

Google's Perspective API is the one resource wave 2b flagged as "the most likely free, ungated, Vietnamese-capable classifier" and could not confirm because its docs render as a JavaScript shell to a plain fetch. This wave reached the underlying content with a Googlebot user-agent `curl` request (the page appears to serve prerendered HTML to known crawlers).

**Full verbatim language table** (`raw/perspective-api-pull.md`): TOXICITY supports 17 languages (Arabic, Chinese, Czech, Dutch, English, French, German, Hindi, Hinglish, Indonesian, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish); the five other production attributes (SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, THREAT) support only 7 (de, en, es, fr, it, pt, ru). **Vietnamese does not appear in any attribute's list.** This confirms wave 2b's WebSearch-synthesis finding against the primary source, verbatim.

**Registration**: needs a Google account + a Google Cloud project — not a content-licence click-through, but still account creation, which this project's hard rule does not perform. No statement found confirming or denying a billing account requirement.

**The bigger finding**: Perspective API is **sunsetting**. Verbatim: "you can submit requests until February 2026. After that, we will no longer accept any new requests... The API will no longer be in service after 2026." As of this pull (2026-09-17), the stated new-request cutoff has already passed and the service's own end-of-life is roughly three and a half months away. **Perspective API is not a viable design target regardless of the language question** — this is new information wave 2b did not have (its finding stopped at "docs never rendered").

## 4. Translation path — confirmed

`Helsinki-NLP/opus-mt-vi-en` and `opus-mt-en-vi`: both confirmed `gated:false`, Apache 2.0, via direct API fetch — exact IDs wave 1c already recommended, now independently re-verified. `VietAI/envit5-translation`: confirmed `gated:false`, OpenRAIL. Nothing downloaded (per this wave's scope; staging weights is a follow-on step). **Note**: if the corpus chosen is MultiJail or the SEA-HELM pair, no translation step is needed at all — both already ship native/paired Vietnamese and English side by side. Translation is only required if ViHOS is the chosen corpus (which has no English counterpart).

## 5. What remains gated — see `raw/gated-resources-summary.md` for the full table

Short version: ViHSD (email agreement to UIT), Llama Guard 3 8B/1B (Meta manual review), WildGuard (AI2 self-serve click-through), ShieldGemma (Google manual review), NVIDIA Aegis/NemoGuard adapters (gated via their Meta base). None of these gates block the measurement any longer — every one has an ungated substitute identified above that covers the same role.

## Closing verdict

**Can the measurement run today with zero licence acceptance?**

**Yes** — with a corpus and guardrail substitution, not the exact pairing 2a originally specified.

- **Corpus**: MultiJail (human-translated, natively paired VI/EN, no MT step needed, 315 items) or the SEA-HELM `vi_general.jsonl`/`en_general.jsonl` pair (machine-translated, natively paired, 600 items, Llama-Guard-style taxonomy) or ViHOS (native Vietnamese only, needs the free Helsinki-NLP OPUS-MT path for an English arm, 11,056 comments — the largest of the three).
- **Guardrail(s) under test**: Qwen3Guard-Gen-0.6B (fully open, Apache 2.0, runs today on this machine's free VRAM without quantization, and its 119-language claim is backed by a base-model benchmark table that explicitly names Vietnamese) is the strongest ungated candidate. `omni-moderation-latest` (free API key, no data-licence gate — already known from wave 1c) and Azure AI Content Safety (lists Vietnamese as "Supported" — wave 2b's finding) remain available as hosted comparators; neither requires a content-licence click, only a normal commercial API account.
- **What is lost versus the gated design**: (a) the specific ViHSD 3-class CLEAN/OFFENSIVE/HATE label schema and its exact stratified-sampling design — the substitutes carry different label shapes (binary toxic/clean for ViHOS, "is this unsafe" for MultiJail, Safe/Harmful-by-category for the SEA-HELM pair); (b) a direct test of Llama Guard 3 8B specifically — its documented negative (stops at Thai) is already fully evidenced without running it, so this loss is mostly cosmetic; (c) SEA-HELM's own published Vietnamese-safety numeric scores as a cross-check, since the leaderboard is a JS SPA unreachable without a browser tool (a tooling gap, not a licence gap).
- **How the result would have to be caveated**: any measurement run against ViHOS, MultiJail, or the SEA-HELM pair should say plainly that it did **not** use ViHSD, name which substitute corpus and label schema it used instead, and — if MultiJail is chosen — flag that the "Vietnamese" arm is a professionally human-translated version of an English-authored prompt set rather than organically-Vietnamese social-media text (the opposite direction of translation risk from a machine-translated English control arm, but a real difference in what is being measured). If Qwen3Guard is the guardrail under test, the write-up should note its 119-language Vietnamese claim is inherited from the base LLM's own reported benchmarks, not from a Qwen3Guard-specific published language table — a caveat with the same shape as Llama Guard 3's own HF metadata-vs-prose gap that wave 1c already flagged.

## Caveats

- Vietnamese-language coverage in Qwen3Guard's own paper is inferred from the Qwen3 base model's technical report, not stated directly in the Qwen3Guard paper. Flagged, not resolved, above.
- VOZ-HSD and UIT-VSFC mirrors were found on HuggingFace but not pursued to a licence/provenance conclusion this pass — open follow-up, not a negative finding.
- Whether Perspective API still issues new API keys today (as opposed to only refusing quota-increase requests) is `unknown — checked 2026-09-17`; moot regardless, since it doesn't support Vietnamese and the design should not depend on a sunsetting service either way.
- The Googlebot-UA fetch technique used to read Perspective API's pages is a workaround for a JS-rendered site, not a documented or guaranteed-stable access method — a future pull on the same URLs may not get the same result if the vendor changes its crawler-detection behaviour.
- ViHOS rows appear not to be NE-anonymized (unlike ViHSD) — spot-checked rows contain what look like real personal names. Flagged for whoever compiles a public-facing artifact from this data.
- Build-size, quantization-fit, and "which substitute is best" judgments in this file are this agent's own reasoning, not sourced — the underlying gate/licence/language facts above are sourced and verbatim; the recommendation layered on top is not.
