# Policy ceiling — cloaking policy per engine, plus ad-disclosure law

2026-09-17. Extends pass 2's policy read (`../../../../docs/findings/injection-feasibility.md` Q4, `../../../../docs/raw/tos-browser-pulls.md`) with the ad-disclosure regimes named in the brief. Sourced from `raw/policy-and-edge-pulls.md`. Primary sources quoted where fetched; `unknown — checked <channel> 2026-09-17` where not reached.

## Engine cloaking / differentiated-content policy

| Engine | Policy found | Quote | Status |
|---|---|---|---|
| Google | Yes — carried from pass 2, unchanged this pass | Cloaking: "Presenting different content to users and search engines with the intent to manipulate search rankings and mislead users." Named example: "inserting text or keywords into a page only when the user agent requesting the page is a search engine, not a human visitor." AI-response manipulation is separately named as spam, same page, `Last Updated: 2026-08-28`. | Settled (pass 2). Effective date of the AI-answer-manipulation wording (2026-05-15, secondary press) remains unconfirmed against Google's own changelog. |
| OpenAI | Consumer ToS bars programmatic extraction (pass 2, browser-fetched). Ads-specific terms (would govern OAI-AdsBot content requirements) — **not reached**, 403 to both WebFetch and curl this pass | n/a for ads terms | `unknown — checked openai.com 2026-09-17`, needs browser access |
| Anthropic | No dedicated cloaking/spam policy page found or fetched, either pass. Usage policy not re-checked this pass. | n/a | `unknown — checked 2026-09-17` |
| Perplexity | Consumer ToS bars automated *and manual* "monitor, extract, copy or collect information," personal/non-commercial use only, commercial exploitation barred outright (pass 2, browser-fetched, truncated at 50k/56.2k chars). No separate cloaking-specific clause found. | quoted in full in `tos-browser-pulls.md` | Settled for consumer ToS; API ToS never read (see `carrier-state.md` item 10). |
| Bing/Copilot (Microsoft) | Webmaster guidelines page is a client-rendered app shell — 125,562 bytes of HTML fetched via curl, zero occurrences of "cloak." | n/a | `unknown — checked bing.com 2026-09-17`, needs browser-rendered fetch |
| Meta | Not checked this pass. | n/a | `unknown — checked 2026-09-17` |

## Ad-disclosure regimes

### FTC Endorsement Guides (US)

Source: `ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking`, fetched 2026-09-17.

Operative sentence: **"if there's a connection between an endorser and the marketer that a significant minority of consumers wouldn't expect and it would affect how they evaluate the endorsement, that connection should be disclosed clearly and conspicuously."** And: **"The same is usually true if the endorser has been paid or given something of value to tout the product."**

**No mention of AI-generated recommendations, AI chatbots, or generative-AI answers anywhere in the fetched text.** The Guides, last substantively updated 2023 per the fetch, predate this fact pattern. Read for the idea: the FTC's disclosure *principle* (undisclosed material connection = deceptive) would plausibly extend to a chatbot recommending a paid-placement product without disclosure, by direct analogy to an undisclosed-paid-endorser — but **no FTC text says so explicitly**, and no FTC enforcement action against an AI-answer-embedded paid placement was found or searched for this pass.

### EU Digital Services Act, Article 26

Source: third-party mirror of the regulation text (`eu-digital-services-act.com`), cross-checked against a direct eur-lex.europa.eu fetch that returned no renderable body (JS-gated) — fetched 2026-09-17.

Para 1 requires online platforms let recipients identify "that the information is an advertisement," the advertiser's identity, who paid if different, and "meaningful information directly and easily accessible from the advertisement about the main parameters used to determine the recipient." Para 2 requires platforms let users self-flag commercial content and make it "identify[able] in a clear and unambiguous manner" to others. Para 3 bars targeted ads built on sensitive-category profiling.

**Applicability is genuinely unresolved.** Article 26 binds the *platform* displaying an ad. Whether a page an advertiser controls, retrieved and paraphrased by an AI assistant that never labels the result as an ad, falls inside "advertising… on its online platform" was not addressed by anything fetched this pass. `unknown — no DSA guidance found addressing AI-answer-embedded commercial content, checked 2026-09-17.`

### EU Unfair Commercial Practices Directive (2005/29/EC), Annex I item 11 — "advertorial"

Source: UK Consumer Protection from Unfair Trading Regulations 2008, Schedule 1 (`legislation.gov.uk/uksi/2008/1277/schedule/1/made`) — a statutory instrument implementing the Directive's Annex I list into UK domestic law without material alteration, used as a verified verbatim proxy since eur-lex.europa.eu itself returned no renderable body — fetched (curl, raw HTML) 2026-09-17.

Verbatim, item 11, one of the practices "which are in all circumstances considered unfair":

> **"Using editorial content in the media to promote a product where a trader has paid for the promotion without making that clear in the content or by images or sounds clearly identifiable by the consumer (advertorial)."**

**This is the sharpest primary-source hit found this pass for the idea's core mechanism.** Paying to place product-promoting text that an AI assistant then presents as if it were the page's own ordinary content, undisclosed, structurally matches "paid promotion dressed as editorial content" — the enumerated example is print/broadcast advertorial, not an AI-answer pipeline, and no EU or UK enforcement action extending item 11 to AI-generated answers was found or searched for. Untested application, not a settled reading — but this is a per-se violation category ("in all circumstances unfair"), stronger than the UCPD's general fairness test, if a regulator ever did extend it.

### Vietnam Law on Advertising (16/2012/QH13) — not reached

Four fetch attempts failed (wrong slug/404, connection timeout, HTTP 403, and one wrong-document hit — WIPOLex's linked ID resolved to a Dominican Republic law, not Vietnam's). One WebSearch call returned "Web search error: unavailable." `unknown — checked luatvietnam, vanbanphapluat, thuvienphapluat, WIPOLex, WebSearch 2026-09-17.` Named in the brief as "if reachable" — genuinely not reachable this pass with the tools available; next agent with browser access or a reset WebSearch budget should retry, since Vietnam is this team's home geography per `../../../../docs/findings/pass3-read.md`.

## Read across all of the above

No engine, and no ad-disclosure regime fetched this pass, has language written with an AI-answer-embedded paid placement specifically in mind. Google's cloaking/spam policy is the one directly-on-point primary source (it names AI-response manipulation explicitly), and it is unambiguous: differential serving keyed to a search/AI crawler's user-agent, done "with the intent to manipulate," is exactly what it prohibits. The general consumer-protection angle (FTC, UCPD) supplies a second, independent line of exposure — advertorial/undisclosed-paid-content rules that long predate AI and were not written with an escape hatch for "but a chatbot said it, not us." **Both lines point the same way: an undisclosed differential-serving product built on this mechanism sits on the wrong side of the line the market research (`../../../../docs/findings/injection-feasibility.md`) already drew.** A measurement/audit product — showing a client what an AI assistant already does with their own page, no undisclosed differential serving involved — does not trigger either line.

## Caveats

- DSA Article 26 and UCPD text came via third-party/UK-statutory-instrument proxies, not a direct eur-lex.europa.eu fetch — eur-lex returned an empty, JS-gated body to both WebFetch attempts. The UK SI is a faithful transposition by its own stated purpose but is not the EU original.
- No enforcement action — FTC, EU, or platform — applying any of these rules to an AI-answer-embedded paid placement specifically was found. Absence of a case is not evidence the theory is wrong; it may just mean nobody has done this yet at a scale that drew attention.
- Bing/Copilot and Meta cloaking policy, OpenAI's ads-specific terms, and Vietnam's advertising law are all open — see `carrier-state.md` for the consolidated open-items list.
