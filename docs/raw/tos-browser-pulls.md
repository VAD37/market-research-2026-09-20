# ToS pulls via browser — the four pages that 403'd in pass 2

Pulled 2026-09-16 by the main thread using the Chrome extension, after the user granted browser access. Channel: `mcp__claude-in-chrome__navigate` + `get_page_text`. Every one of these URLs returned HTTP 403 to WebFetch during pass 2.

Answers open question E2 in `../method/open-questions.md`.

## Block 1 — OpenAI Terms of Use (consumer)

URL: https://openai.com/policies/row-terms-of-use/
Fetched: 2026-09-16, browser
Page states: **Published: January 1, 2026** / **Effective: January 1, 2026**

Scope, in the page's own words:

> "These Terms of Use apply to your use of ChatGPT, DALL·E, and OpenAI's other services for individuals"

> "Our Business Terms govern use of ChatGPT Enterprise, our APIs, and our other services for businesses and developers."

Under the heading **"What you cannot do"**, the full list as published:

> "You may not use our Services for any illegal, harmful, or abusive activity. For example, you may not:
> Use our Services in a way that infringes, misappropriates or violates anyone's rights.
> Modify, copy, lease, sell or distribute any of our Services.
> Attempt to or assist anyone to reverse engineer, decompile or discover the source code or underlying components of our Services, including our models, algorithms, or systems (except to the extent this restriction is prohibited by applicable law).
> Automatically or programmatically extract data or Output (defined below).
> Represent that Output was human-generated when it was not.
> Interfere with or disrupt our Services, including circumvent any rate limits or restrictions or bypass any protective measures or safety mitigations we put on our Services.
> Use Output to develop models that compete with OpenAI."

The fourth bullet is the operative one. The page carries no emphasis of its own.

Also relevant, under "Content":

> "Input and Output are collectively 'Content.'"

> "As between you and OpenAI, and to the extent permitted by applicable law, you (a) retain your ownership rights in Input and (b) own the Output."

So: the user owns the Output, and is separately barred from extracting it programmatically. Ownership and the extraction ban are independent clauses.

Governing law and dispute terms:

> "California law will govern these Terms except for its conflicts of laws principles."

> "MANDATORY ARBITRATION. You and OpenAI agree to resolve any claims arising out of or relating to these Terms or our Services, regardless of when the claim arose, even if it was before these Terms existed (a 'Dispute'), through final and binding arbitration."

Arbitration opt-out exists: "within 30 days of account creation or of any updates to these arbitration terms within 30 days after the update has taken effect".

Exception to arbitration that matters here:

> "This section does not require informal dispute resolution or arbitration of the following claims: (i) individual claims brought in small claims court; and (ii) injunctive or other equitable relief to stop unauthorized use or abuse of the Services or intellectual property infringement or misappropriation."

Unauthorized use is carved out of arbitration and goes to court — San Francisco, California, exclusively.

## Block 2 — OpenAI Service Terms (the API side)

URL: https://openai.com/policies/service-terms/
Fetched: 2026-09-16, browser
Page states: **Updated: September 10, 2026** — six days before this pull.

Section 1, "API", the entire use restriction:

> "Customer will only, and will ensure that its End Users only, use APIs in accordance with the applicable documentation at https://platform.openai.com/docs"

That is the only use restriction in the API section. **No programmatic-extraction prohibition appears on the API path.** The rest of section 1 is OpenAI's IP indemnification of API customers and its six carve-outs.

The Service Terms state their own precedence:

> "If there is a conflict between the Service Terms and your Agreement, the Service Terms will control."

Section 2, Beta Services:

> "Beta Services are offered 'as-is' to allow testing and evaluation and are excluded from any indemnification obligations OpenAI may have to you."

Section 6, Visual Capabilities — relevant to any harness submitting images:

> "You may not use Visual Capabilities to assist in identifying a person nor to solicit or infer private or sensitive information about a person."

Section 8, Voice:

> "ChatGPT Voice Output is for non-commercial use only and may not be distributed or repackaged as a standalone audio recording or any other sound file."

`unknown — checked 2026-09-16`: the OpenAI Services Agreement / Business Terms were not fetched this pass. Section 1 points to them and they control for API customers. Fetch before relying on this block.

## Block 3 — Perplexity Terms of Service (consumer)

URL: https://www.perplexity.ai/hub/legal/terms-of-service
Fetched: 2026-09-16, browser
Page states: **Last updated: January 23rd, 2026**

Scope, and the API carve-out, verbatim:

> "These Terms do not govern use of the Company's APIs (which are governed by the Perplexity API Terms of Service located here: https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service) or Perplexity Pro for Enterprise"

Section 5.1, the licence grant:

> "We hereby permit you to use the Services for your personal, non-commercial use only, provided that you comply with these Terms in connection with all such use."

Section 5.2, "Restrictions On Your Use of the Services." Opening qualifier, verbatim:

> "You may not do any of the following in connection with your use of the Services, unless applicable laws or regulations prohibit these restrictions or you have our written permission to do so"

The four sub-clauses bearing on a measurement harness:

> "(a) download, modify, copy, distribute, transmit, display, perform, reproduce, duplicate, publish, license, create derivative works from, or offer for sale any information contained on, or obtained from or through, the Services, except for temporary files that are automatically cached by your web browser for display purposes, or as otherwise expressly permitted in these Terms;"

> "(d) use automation software (bots), hacks, modifications (mods) or any other unauthorized third-party software designed to modify the Services;"

> "(e) exploit the Services for any commercial purpose, including without limitation communicating or facilitating any commercial advertisement or solicitation;"

> "(i) use any robot, spider, crawlers, scraper, or other automatic device, process, software or queries that intercepts, 'mines,' scrapes, extracts, or otherwise accesses the Services to monitor, extract, copy or collect information or data from or through the Services, or engage in any manual process to do the same;"

Note the final clause of (i): **"or engage in any manual process to do the same."** Manual collection is prohibited on the same terms as automated collection. Hand-running queries and recording the answers sits inside the restriction, not outside it.

Section 1.1.2, on citation:

> "You may not (i) publish any Output generated by the Services without clearly citing the Services, or (ii) misrepresent the source of any Output or the fact that it was generated by artificial intelligence."

Dispute terms: JAMS arbitration, class-action waiver, 30-day opt-out to support@perplexity.ai. Exceptions that go to court:

> "(b) Claims where the sole form of relief sought is injunctive relief (including public injunctive relief); or (c) intellectual property Claims."

`unknown — checked 2026-09-16`: the Perplexity API Terms of Service at https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service was not fetched. It controls the API path, which is the route that matters. Next pull.

`unknown — checked 2026-09-16`: the page truncated at 50,000 of 56,200 characters. Sections after "Shopping with Perplexity Pro" were not read.

## Block 4 — what these pages settle

Compiler's reading, not a quote:

1. **Consumer surfaces are closed.** OpenAI bars programmatic extraction of Output. Perplexity bars automated *and manual* collection, limits use to personal and non-commercial, and bars commercial exploitation outright. A product that measures answers by querying the consumer product breaches both.
2. **The API path is not closed by these documents.** OpenAI's Service Terms impose only "use in accordance with the documentation." Perplexity's consumer ToS explicitly does not govern its API. Neither API agreement was read this pass.
3. **Perplexity 5.2's carve-out is "written permission."** A negotiated agreement is a named route through the restriction, not a loophole.
4. **Enforcement runs through court, not arbitration.** Both companies carve unauthorized use and injunctive relief out of their arbitration clauses.
