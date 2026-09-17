# Llama Guard 3 8B local runnability — requirements vs. this machine

Source: Hugging Face model API (`huggingface.co/api/models/meta-llama/Llama-Guard-3-8B`, direct curl, unauthenticated — metadata is public even though weights are gated), Hugging Face model card (WebFetch), and direct shell/PowerShell inspection of this machine. Pull date 2026-09-17. Method: direct fetch + local commands, no browser tools, no account created, no download attempted.

## What Llama Guard 3 8B requires

- **Size:** 8B parameters. Base model `meta-llama/Llama-3.1-8B` (per HF API `base_model` field), architecture `LlamaForCausalLM`.
- **Formats offered (per model card):** BF16 (half-precision, the default checkpoint) and a vendor-published `meta-llama/Llama-Guard-3-8B-INT8` quantized checkpoint. Vendor's own claim, verbatim: INT8 "reduc[es] the checkpoint size by about 40% with very small impact on model performance." Community GGUF/llama.cpp/Ollama-compatible requantizations are referenced generically on the model page ("llama.cpp, Ollama, LM Studio, or any compatible app") but no specific community repo was checked or downloaded this pass.
- **Licence gate — stronger than most:** HF API field `"gated":"manual"` (confirmed via direct `curl` of `huggingface.co/api/models/meta-llama/Llama-Guard-3-8B`) — this is Meta's **manual-approval** gate, not an auto-accept click-through. License field: `"license":"llama3.1"`. `extra_gated_prompt` in the API response begins: "### LLAMA 3.1 COMMUNITY LICENSE AGREEMENT / Llama 3.1 Version Release Date: July 23, 2024 / 'Agreement' means the terms and conditions for use, reproduction, distribution and modification of the Llama Materials..." — not accepted, not requested, per the hard rule.
- **Machine-readable language tag discrepancy, worth flagging:** the HF `cardData.language` field on this model is `["en"]` — English only — even though the model card's prose (quoted in `raw/guardrail-language-claims-pull.md`) names 8 languages including Thai. The structured metadata is narrower than the marketing/documentation prose. Neither one names Vietnamese.
- **VRAM, computed by us from standard bytes-per-parameter arithmetic (not a vendor-published number — vendor page states no VRAM figure):**

| Precision | Bytes/param | Weights-only size | Typical minimum VRAM incl. KV cache/activations (rule of thumb) |
|---|---|---|---|
| BF16 (default) | 2 | ~16 GB | ~18-20 GB |
| INT8 (vendor checkpoint) | 1 | ~8 GB (matches vendor's "~40% reduction" claim from 16GB, roughly) | ~9-10 GB |
| 4-bit (community GGUF, not checked/downloaded) | ~0.5-0.6 | ~4.5-5.5 GB | ~6-7 GB |

Labeled `computed-by-us 2026-09-17` — standard inference-memory arithmetic, not a specific benchmark citation.

## What this machine actually has (direct inspection, 2026-09-17)

- **GPU:** NVIDIA GeForce RTX 3060 Ti. `nvidia-smi --query-gpu=name,memory.total,memory.used,memory.free`: **8192 MiB total, 1357 MiB already in use (desktop/VS Code), 6668 MiB free** at time of check.
- **Python:** Two installations found via `py -0p`: `pythoncore-3.14-64` (default `python`/`py`, Python 3.14.3) and an Astral/uv-managed `cpython-3.9.25` (used by `pip`'s reported interpreter in one check). No `py -3.9` runtime is registered with the `py` launcher despite the uv-managed 3.9.25 existing on disk — `py -3.9` returned "No runtime installed that matches 3.9."
- **ML packages:** `pip show torch transformers vllm sentencepiece` → **all four: "Package(s) not found."** No `ollama` binary on PATH (`which ollama` → not found; `ollama --version` → command not found). `uv` (0.11.17) and `conda` (not found) were checked — `uv` is present and could provision a Python env with `torch`/`transformers` if needed, but nothing is installed yet.
- **Disk:** D: drive — 276.7 GiB free (`Get-PSDrive D`), ample for any of the weight sizes above.
- **CUDA toolkit:** present (`nvidia-smi` reports CUDA UMD 13.3; a CUDA Toolkit v13.3 directory exists on PATH), so GPU-accelerated inference is plausible once packages are installed.

## Verdict: local run is marginal, not blocked, not free

- **BF16 (16GB weights) does not fit** — only 6.7 GB VRAM free, 8 GB total. Ruled out on this machine regardless of what else is running.
- **INT8 (~8GB weights) does not comfortably fit** — exceeds current free VRAM (6.7 GB) and would consume the entire card even if nothing else were running, leaving no room for KV cache/activation memory. Would likely OOM or require closing every other GPU consumer and still be tight.
- **4-bit quantized (~5GB weights) is the only precision plausibly viable on this GPU** — fits within the 6.7 GB currently free with some headroom for KV cache on short inputs (single-turn moderation calls, which is exactly this measurement's use pattern). Not verified empirically (no weights downloaded, per the licence-gate rule); a projection from arithmetic, not a measured fact.
- **Software gap, separate from hardware:** no `torch`, `transformers`, `vllm`, or `ollama` is installed. Getting to a running state requires `pip`/`uv` package installation (free, no data-licence issue) **plus** clearing Meta's manual-approval gate for the weights themselves (or sourcing a community GGUF requantization, which was not checked in this pass and carries its own provenance/licence-compliance question this pass does not resolve).
- **Hosted path exists as the practical alternative:** per `raw/guardrail-language-claims-pull.md`, no confirmed live hosted endpoint with stated pricing was found this pass (Together.ai: "not available... launching soon"; OpenRouter: not found in fetched catalog; Groq: pricing page not fetchable). **The hosted path for Llama Guard 3 8B specifically is currently `unknown/unconfirmed`, not a clean fallback** — this narrows the settling measurement's real options to (a) clear Meta's manual gate and run a 4-bit quantization locally, or (b) find a working hosted provider not yet located in this pass, or (c) drop Llama Guard 3 from the three-guardrail panel and note the gap.

## Caveats

- VRAM figures are computed from standard bytes-per-parameter arithmetic, not measured on this machine or cited from a vendor benchmark — labeled accordingly.
- "6668 MiB free" is a point-in-time reading; background Windows/VS Code GPU usage fluctuates and actual availability at run-time may be lower.
- Community GGUF requantizations of Llama-Guard-3-8B were not searched for or evaluated in this pass (would need a licence-compliance judgment call this wave is not positioned to make unilaterally — flagging for 2c/human review rather than deciding it here).
- `py -3.9` not being registered with the launcher despite a uv-managed 3.9.25 existing is a minor environment quirk, not a blocker — `uv run` or invoking the interpreter path directly would work.
