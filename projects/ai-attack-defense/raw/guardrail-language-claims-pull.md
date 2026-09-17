# Guardrail language claims, invocation, cost — verbatim pull

Source: Hugging Face model cards (WebFetch + curl), OpenAI developer docs, Lakera marketing/docs pages, NVIDIA NeMo Guardrails GitHub repo, Google ShieldGemma model card, OpenRouter/Together/Groq hosting pages. Pull date 2026-09-17. Method: direct WebFetch/curl of vendor-owned pages, no browser tools, no account created, no purchase.

This re-verifies wave 1's Llama Guard 3 / NeMo / Lakera findings (`raw/language-gap-pulls.md`) via independent fetch (matches exactly — increases confidence it isn't a fetch artifact) and adds `omni-moderation-latest`, invocation/cost/rate-limit/free-tier detail for all five, and one open alternative (ShieldGemma).

## 1. Llama Guard 3 8B (Meta)

**Language claim, verbatim** (Hugging Face model card, `meta-llama/Llama-Guard-3-8B`, fetched 2026-09-17): "Llama Guard 3 supports content safety for the following languages : English, French, German, Hindi, Italian, Portuguese, Spanish, Thai." **Vietnamese is absent.** Identical wording to wave 1's independent pull — confirmed, not a one-off render artifact.

- **Invocation:** Local weights (safetensors), run via `transformers`/`vllm`/similar. Not a hosted-by-Meta API.
- **Access gate:** Model card, verbatim: users must "agree to share your contact information to access this model" under the **Llama 3.1 Community License Agreement**, plus comply with an Acceptable Use Policy, before the gated HF repo grants download access. Confirmed independently: `curl` of the raw README returned "Access to model meta-llama/Llama-Guard-3-8B is restricted. You must have access to it and be authenticated to access it."
- **Size:** 8B parameters (per model name/card).
- **Cost:** Free weights once the licence is accepted (no purchase) — but the acceptance step itself is a licence-acceptance gate, which this pass does **not** complete (see gap 4 below for what that means for this project).
- **Hosted alternative:** Model card lists "Featherless AI" as an inference provider. Checked Together.ai directly (`together.ai/models/llama-guard-3-8b`, fetched 2026-09-17) — verbatim: "This model is not available on Together's Serverless API... Launching soon." Checked OpenRouter's model search — no Llama Guard listing found in the fetched catalog page (JS-paginated catalog, may be incomplete). Groq's pricing page (fetched) did not surface per-model pricing (JS-rendered). **Hosted-inference pricing for Llama Guard 3 8B is `unknown — checked together.ai, openrouter.ai, groq.com 2026-09-17, no confirmed live paid or free hosted endpoint found by direct fetch`.**
- **Rate limits:** N/A for self-hosted; not established for any hosted provider in this pull.

## 2. OpenAI `omni-moderation-latest`

**Language claim:** Fetched `https://developers.openai.com/api/docs/guides/moderation` (platform.openai.com/docs/guides/moderation 301-redirects here as of 2026-09-17). **No statement about supported languages anywhere in the page — no language list, no multilingual claim, no exclusion statement.** Same silence pattern as NeMo: absence of a claim, not a denial of Vietnamese support.

- **Invocation:** REST endpoint `https://api.openai.com/v1/moderations`, POST request, via OpenAI client libraries or raw HTTP.
- **Model name:** `omni-moderation-latest` — explicitly documented as accepting both text and images. No other model version (e.g. `omni-moderation-2024-09-26`, `text-moderation-latest`) was surfaced in the fetched page content.
- **Cost, verbatim:** "The moderation endpoint is free to use." **This is the only guardrail under test with a confirmed-free, no-tier, no-signup-beyond-an-API-key cost model.**
- **Rate limits:** Not stated on the fetched page — OpenAI's standard per-org rate-limit tiers apply generally to API endpoints but a moderation-specific number was not found this pull; `unknown — checked developers.openai.com/api/docs/guides/moderation 2026-09-17`.
- **Free tier:** Yes — the endpoint itself carries no charge; only an OpenAI API account (no payment required to call moderation specifically, though account creation with OpenAI is needed for an API key — this is judged in scope since it's not "signing a data licence agreement," but flagged for the user's awareness).

## 3. Lakera Guard

**Language claim, verbatim** (lakera.ai marketing page, fetched 2026-09-17): "Observing 100+ languages in real-time." No named list, no Vietnamese-specific statement, unverifiable as stated — identical to wave 1's finding.

- **Invocation:** POST to `https://api.lakera.ai/v2/guard`, per `docs.lakera.ai/docs/quickstart` (fetched 2026-09-17): "make a POST request to the `guard` endpoint for each interaction with the LLM."
- **Cost / free tier:** The marketing page has a "Start for free" button linking to `platform.lakera.ai`. Pricing page (`lakera.ai/pricing` → redirects to `platform.lakera.ai/pricing`) is a client-rendered app page — fetch returned only navigation chrome, no tier numbers, no rate limits. **Free-tier existence is asserted by the "Start for free" CTA but its limits (requests/month, feature gating) are `unknown — checked platform.lakera.ai/pricing 2026-09-17, JS-rendered page returned no pricing content via fetch`.**
- **Rate limits:** Not found via direct fetch; same JS-rendering limitation.

## 4. NVIDIA NeMo Guardrails

**Language claim:** GitHub repo (`NVIDIA-NeMo/Guardrails`, fetched 2026-09-17): **no statement about supported languages or multilingual capability anywhere in the fetched README/docs content** — confirms wave 1's finding independently. Silence, not a denial.

- **Invocation:** Not a hosted API — a local Python library (`LLMRails` class) that wraps a caller-supplied LLM backend (OpenAI, LLaMA-2, Falcon, etc., per the docs). Runs as either a direct Python API call or a self-hosted guardrails server.
- **Licence:** Apache License 2.0 (open source, free to use and modify).
- **Cost:** The library itself is free. Actual cost depends entirely on which LLM backend it's configured to call (e.g. OpenAI API charges) — NeMo Guardrails is an orchestration layer, not a classifier model with its own inference cost.
- **Rate limits:** N/A — determined by whatever backend LLM/API is plugged in, not by NeMo Guardrails itself.

## 5. Open alternative — Google ShieldGemma (9B)

Chosen as the "one open alternative" distinct from Llama Guard 3: an openly-licensed (open-weights), self-hostable safety classifier from a different vendor, comparable in shape to Llama Guard.

**Language claim, verbatim** (Hugging Face model card `google/shieldgemma-9b`, fetched 2026-09-17): "available in English with open weights." **Vietnamese is not mentioned or supported — ShieldGemma is English-only by its own model card, a harder exclusion than Llama Guard 3's 8-language-but-no-Vietnamese list.**

- **Invocation:** Local weights, via `transformers`, `vllm`, `SGLang`, or quantized builds. Model card, verbatim: "isn't deployed by any Inference Provider" — **no hosted API exists for this model at all**, self-hosting is the only option.
- **Size:** 9B parameters.
- **Licence/access gate:** Gemma licence (Google), verbatim: "To access Gemma on Hugging Face, you're required to review and agree to Google's usage license." Another licence-acceptance gate, same pattern as Llama Guard 3, not accepted or downloaded in this pass.
- **Cost:** Free weights once the licence is accepted; no hosted-inference cost path exists at all (must self-host).
- **Rate limits:** N/A (self-hosted only).

## Cross-guardrail summary table

| Guardrail | Vietnamese named? | Invocation | Smallest-tier cost | Free tier | Licence gate to obtain |
|---|---|---|---|---|---|
| Llama Guard 3 8B | No — list stops at Thai | Local weights (HF gated) or third-party hosted (unconfirmed pricing) | Free weights; hosted cost unknown | Weights free once gated | Yes — Llama 3.1 Community Licence, contact-info share required |
| `omni-moderation-latest` | No claim either way (silent) | REST API `/v1/moderations` | **Free to use**, verbatim | Yes, no separate tier | No data-licence gate; needs an OpenAI API account |
| Lakera Guard | No named list — "100+ languages," unverifiable | REST API `/v2/guard` | Unknown — pricing page JS-rendered, not fetchable | Asserted ("Start for free") but limits unconfirmed | No licence-agreement gate found; account signup implied |
| NeMo Guardrails | No claim either way (silent) | Local Python library, needs external LLM backend | Free (Apache 2.0); cost = backend LLM cost | N/A — library is free | No — Apache 2.0, no gate |
| ShieldGemma 9B (open alt) | No — explicitly "English" only | Local weights only, no hosted API exists | Free weights once gated | N/A | Yes — Gemma licence, not accepted |

## Caveats

- Vendor pricing/rate-limit pages for Lakera and hosted Llama Guard providers (Together, Groq, OpenRouter) are JS-rendered single-page apps; WebFetch retrieves only the served HTML shell, not the client-side-loaded data. Browser tools are out of bounds for this wave (a sibling agent is using Chrome on another project) — these numbers are `unknown — checked <URL> 2026-09-17, JS-rendered, no browser tool available` rather than guessed.
- "100+ languages" (Lakera) remains unverifiable marketing copy — consistent with the caveat already on record in `docs/markets/ai-attack-defense.md`.
- No licence was accepted, no account was created, and no payment was made anywhere in this pull, per the hard rule.
