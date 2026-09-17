# Perspective API — supported languages, quota, registration, sunset — raw pull

Wave 1d, pull date 2026-09-17. Method: direct `curl` fetch of `developers.perspectiveapi.com` pages **using a Googlebot user-agent string** (`Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`). The site is a Salesforce Community (JS-rendered) page; a plain fetch (default UA, and via the WebFetch tool) returns only a "Loading... CSS Error" shell, which is what wave 2b hit on three prior attempts (`raw/review-guardrail-coverage-pulls.md` PULL 3). The Googlebot UA appears to receive server-side-rendered content (consistent with Salesforce serving a prerendered version to known crawlers) — this returned the full table and FAQ text below. Also checked: the API's own Google Discovery document (`www.googleapis.com/discovery/v1/apis/commentanalyzer/v1alpha1/rest`, no auth needed) and the `conversationai/perspectiveapi` GitHub repo via `gh api`. No account created, no API key requested, no registration performed.

## Supported languages, verbatim (table, `developers.perspectiveapi.com/s/about-the-api-attributes-and-languages`)

**Production attributes:**

| Attribute name | Description (verbatim) | Available Languages (verbatim) |
|---|---|---|
| TOXICITY | "A rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion." | Arabic (ar), Chinese (zh), Czech (cs), Dutch (nl), English (en), French (fr), German (de), Hindi (hi), Hinglish (hi-Latn), Indonesian (id), Italian (it), Japanese (ja), Korean (ko), Polish (pl), Portuguese (pt), Russian (ru), Spanish (es) |
| SEVERE_TOXICITY | "A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words." | de, en, es, fr, it, pt, ru |
| IDENTITY_ATTACK | "Negative or hateful comments targeting someone because of their identity." | de, en, es, fr, it, pt, ru |
| INSULT | "Insulting, inflammatory, or negative comment towards a person or a group of people." | de, en, es, fr, it, pt, ru |
| PROFANITY | "Swear words, curse words, or other obscene or profane language." | de, en, es, fr, it, pt, ru |
| THREAT | "Describes an intention to inflict pain, injury, or violence against an individual or group." | de, en, es, fr, it, pt, ru |

**Experimental attributes** (TOXICITY_EXPERIMENTAL, SEVERE_TOXICITY_EXPERIMENTAL, IDENTITY_ATTACK_EXPERIMENTAL, INSULT_EXPERIMENTAL, PROFANITY_EXPERIMENTAL, THREAT_EXPERIMENTAL, SEXUALLY_EXPLICIT, FLIRTATION): no separate language column found in the rendered text for this group; the page's own caveat, verbatim: "Expect language availability to change over time as we test attribute performance and move attributes to production."

**Bridging attributes** (AFFINITY_EXPERIMENTAL, COMPASSION_EXPERIMENTAL, and others in that family), verbatim: "These attributes are only available in English (en), and our results for performance and bias evaluation are included in the English model cards."

**Vietnamese: absent from every attribute's language list on this page.** A case-insensitive search for the string "vietnam" across the entire rendered page text returned zero matches.

## FAQ page — registration, cost, quota, and sunset, verbatim (`developers.perspectiveapi.com/s/about-the-api-faqs`, also `docs-get-started`)

**Cost, verbatim**: "Is there a cost to use Perspective? No, Perspective API is free to use. However, in the future, increases to QPS may incur a fee. If we do make this change to our service, we will notify you in advance, so you can make necessary adjustments to your project."

**Default quota, verbatim**: "By default, we set a quota limit to an average of **1 query per second (QPS)** for all Perspective projects. This limit should be enough for testing the API and for working in developer environments. If you're running a production website, you may need to request a quota increase."

**Registration requirement, verbatim**: "Why do I need to register to access the API? We ask Perspective API users to register for access, so that we can better understand and serve our users." Get-Started page, verbatim prerequisites: "You must have a Google account, giving you access to the suite of Google products including Google Cloud. You also must have a Google Cloud project to authenticate (but not necessarily host) your API requests." — the walkthrough (Sign in → Console → Create Project → name it → Enable the API → get a key) never mentions enabling billing or attaching a payment method; **no explicit statement either way was found confirming a billing account is or is not required to enable the API on a fresh Google Cloud project** — `unknown — checked 2026-09-17, not stated on any fetched page`.

**SUNSET — the API is shutting down, verbatim**:
> "Can I request usage or increased quotas during the transition period? Yes, you can submit requests until **February 2026**. After that, we will no longer accept any new requests. Can I extend my access past the final date? Unfortunately, no. **The API will no longer be in service after 2026.** What is the reason for the sunsetting? AI capabilities have evolved, and there is now less demand for a standalone tool specific to this area. Jigsaw's mission also continues to evolve to address new challenges... Are you offering migration support? No. We will not be offering direct migration support, but there are various tools available that were inspired by Perspective's capabilities."

Get-Started page repeats the same figures in different words, verbatim: "...at the end of 2026. You can submit requests until February 2026. After that, we will no longer accept any new requests. The API will no longer be in service after 2026."

**Dating note, important**: today's date for this pull is **2026-09-17**. Per the page's own text, the "submit requests until February 2026" window closed roughly seven months before this pull, and the "no longer in service after 2026" end-of-service point is roughly three and a half months away. This was not cross-checked against a second independent source (e.g. a Jigsaw blog post announcing the sunset with a specific announcement date) — the FAQ text itself carries no visible last-updated timestamp. Treat the exact status of "can a brand-new user still get a working API key today" as **`unknown — checked developers.perspectiveapi.com 2026-09-17, page text is internally consistent with a service already past its stated request-cutoff date, but no live registration attempt was made (would require creating a Google Cloud project, out of bounds under the hard no-account-creation rule)`**.

## Discovery document check (`www.googleapis.com/discovery/v1/apis/commentanalyzer/v1alpha1/rest`)

Fetched directly, HTTP 200, 20,085 bytes, no auth required. The `AnalyzeCommentRequest.languages` field is typed as a plain string array with no enum of valid values — the discovery document does not itself enumerate supported languages; the table on the developer site (above) is the only source found for the language list.

## Attributes' meaning, in brief (from the same table)

TOXICITY through THREAT are self-descriptive per the verbatim descriptions above. Two attributes recommended for use only in narrow ways per the page (not fully explored this pass, flagged for a design that wants attribute semantics beyond TOXICITY): SEXUALLY_EXPLICIT ("Contains references to sexual acts, body parts, or other lewd content") and FLIRTATION ("Pickup lines, complimenting appearance, subtle sexual innuendos, etc.") — both experimental, English-availability not separately confirmed.

## Verdict

Perspective API does **not** support Vietnamese in any of its 8 production or ~10+ experimental attributes — the earlier WebSearch-synthesis finding from wave 2b (`raw/review-guardrail-coverage-pulls.md` PULL 3, "Vietnamese not found in any Perspective language list reached") is **confirmed against the primary source, verbatim, not synthesized**. Independently, and more consequentially for design purposes: the service itself is in its final months (per its own dated language, sunsetting some time before the end of 2026) and has already passed the date after which "we will no longer accept any new requests" for quota increases — the FAQ text does not distinguish new-account registration from quota-increase requests, so whether a first-time API key can still be obtained today is not confirmed either way. **Perspective API should not be designed around for this project regardless of the language question.**
