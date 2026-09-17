# Wave 2b adversarial review — traceability audit of the explore layer

Audit date: 2026-09-17. Method: `grep` over this project's `raw/` and over the repo-root `docs/` tree, checking whether load-bearing claims in `../docs/explore/*.md` trace to a pulled source. No new external pulls in this file — this is an audit of files already in the repo.

---

## AUDIT 1 — the HiddenLayer claim behind the fallback pick

### The claim, as it appears in the compiled layer

`../docs/explore/aisb-inventory.md`, row `5.1-model-editing`, verbatim:

> **NOTHING** found. HiddenLayer ModelScanner covers file-format malware (pickle/GGUF), not weight-level behavioral edits — the exact PoisonGPT threat model

Same file, row `5.2-backdooring`, verbatim:

> **Thin.** Academic techniques (Neural Cleanse, STRIP-class) exist as research code only, not a self-serve product. HiddenLayer claims platform-level detection, contact-sales, unverified

Same file, row `1.2-logprobs`: "HiddenLayer scans artifacts, not live logprob exposure". Row `3.5-weight-extraction`: "HiddenLayer scans model files post-hoc, not live API extraction risk".

`../docs/explore/shipping-tools.md`, HiddenLayer ModelScanner row, "Not covered" column, verbatim:

> Confirmed elsewhere: does not detect behavioral weight edits (ROME-style), only file-format-level threats — see `aisb-inventory.md` row 5.1

`../docs/plan/niche-and-solutions.md` §5, Fallback, verbatim:

> The cleanest absence claim wave 1 produced, and the one with a named incumbent whose limit is **documented rather than assumed**: HiddenLayer scans file formats, not behavior.

### The audit

Command: `grep -rn -i 'HiddenLayer\|ModelScanner' raw/*.md` inside `projects/ai-attack-defense/`, 2026-09-17.
Result: **zero matches.** No file in this project's `raw/` mentions HiddenLayer at all. `raw/shipping-tools-github-pulls.md`'s own HiddenLayer row states only "not on GitHub (closed-source), no public release cadence to check".

Command: `grep -rn -i 'modelscanner\|model scanner' --include=*.md .` inside `market-research/docs/`, 2026-09-17.
Result: two matches, both upstream of this project.

1. `docs/markets/ai-attack-defense.md:54`, a table row, verbatim:
   `| HiddenLayer ModelScanner | Supply-chain scan | 35+ model formats: pickle, GGUF, safetensors | custom quote | commercial |`
2. `docs/raw/ai-attack-defense-pulls.md:338`, verbatim:
   > "HiddenLayer's ModelScanner supports 35+ formats including PyTorch, TensorFlow, ONNX, Keras, GGUF, pickle, and safetensors." "Pricing is based on the scope of models and deployments being protected" (no public price list).

### What the raw source actually says versus what the compiled files say

The pulled source states a **list of supported file formats**. It makes no statement about behavioral weight edits, ROME-style edits, abliteration, or backdoor detection — neither asserting nor excluding them.

The exclusion ("covers file-format malware... **not** weight-level behavioral edits") is an **inference from a format list**. `shipping-tools.md` then labels that inference "Confirmed elsewhere" and cites `aisb-inventory.md`, which cites nothing. `niche-and-solutions.md` then upgrades it to "documented rather than assumed."

Chain: pulled format list → inference → "confirmed elsewhere" → "documented rather than assumed". Nothing was added at any step.

### Related, unaudited

`docs/competitors/ai-attack-defense-roster.md` lists HiddenLayer's products as "**Model scan, red team, runtime**" — three lines, of which the explore layer examines one. Funding: "$50M A 2023; $100M B Sep 2026". Headcount 169 (May 2026, third-party).

`aisb-inventory.md` row 5.2's "HiddenLayer claims platform-level detection, contact-sales, unverified" likewise traces to no raw file in this project.

---

## AUDIT 2 — the vendor-questionnaire hedge, dropped in transit

`docs/markets/ai-attack-defense-services.md` line 47, verbatim:

> **Vendor security questionnaires** reportedly ask whether a product "underwent independent AI red teaming, which attack classes were tested, what evidence exists." Could not confirm CSA's CAIQ has such a field: `unknown — checked 2026-09-16`.

`../docs/explore/sea-compliance-triggers.md`, re-quoting the same passage, verbatim:

> (a) a foreign counterparty's own compliance requirement flowing downstream (e.g., a US/EU customer's vendor-security questionnaire, per `../../../docs/raw/services-lane-pulls.md` Finding 2's "vendor security questionnaires... whether products have undergone independent AI red teaming")

The word "reportedly" and the `unknown — checked 2026-09-16` flag on CAIQ are both absent from the re-quote. `niche-and-solutions.md` inherits the firmer version.

---

## AUDIT 3 — claims that DID check out

Spot-checked against `raw/language-gap-pulls.md`, 2026-09-17, and all found accurately represented in `../docs/explore/language-gap.md` and in `../docs/plan/niche-and-solutions.md`:

- Llama Guard 3 model-card language list quoted verbatim and correctly: "English, French, German, Hindi, Italian, Portuguese, Spanish, Thai."
- XSafety's ten language folders `ar bn de en fr hi ja ru sp zh` — raw records the `gh api` directory listing; the compiled read matches.
- arXiv 2410.22153 Figure 1 caption on Thai, quoted verbatim and correctly, including "which supports Thai".
- arXiv 2310.02446's non-coverage of Vietnamese, recorded in raw as a full-text search negative and labelled as such in both compiled files.
- ML-Bench's SEA exclusion is labelled in raw as `unknown — checked ar5iv full-text 2026-09-17... could be a renderer/table-extraction limitation`, and `language-gap.md` repeats that caveat. `niche-and-solutions.md` §4 case-FOR argument 2 uses it as evidence but flags it itself at §6 item 14. Represented honestly.
- `language-gap.md`'s own caveat "No numeric Vietnamese-specific guardrail ASR or accuracy figure was found or extracted in this pass" is quoted verbatim by the plan as its case-AGAINST argument 1.

On the Vietnamese wedge, wave 2a represented its explore layer accurately and argued against itself in its own words. The traceability failures in this file are both on the **fallback** and on the **compliance** side, not on the primary pick's language evidence.
