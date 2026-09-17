# OpenAI Ad policies — the landing-page clauses wave 1b's addendum did not surface — raw pull

Pulled: 2026-09-17, wave 2b. Method: local text search of `raw/openai-ad-policies.txt` (wave 1b's Wayback pull of `https://openai.com/policies/ad-policies/`, page stamp **"Updated: August 10, 2026"**, snapshot archived 2026-08-18 15:48:37 UTC). No new network fetch. Kind: vendor-reported.

Why this pull: `docs/plan/idea-set.md` §2 made P3 (OpenAI Ads Terms) the conditional deciding C7 in one direction and C3a/C3b in the other, and named the decisive question — "does OpenAI's Ads Terms impose a landing-page-consistency rule on advertisers." `docs/explore/policy-ceiling-addendum.md` Gap 3 quoted two sentences from this document (interface imitation, truthfulness) and marked its mapping-table column (a) "Silent — governs OpenAI's own bought-ad surface." **The document contains landing-page and destination clauses that the addendum does not quote and its table does not account for.** They are below.

---

## Verbatim

Under the ad-category standards:

> "These standards apply to all ad assets, including copy, images or video, **and landing pages**. **Ads must be consistent end-to-end**: approved creatives may not link to destinations that introduce disallowed content (for example, a food delivery ad linking to alcohol delivery)."

Under "Advertiser identity":

> "**Destination integrity**: Ads must lead users to destinations that clearly relate to the advertiser and the offer being promoted. **Landing pages and destinations must accurately represent the advertiser, product, or service described in the ad** and may not mislead users through deceptive practices."

Under "Advertiser trustworthiness":

> "**Abuse of OpenAI Ads**: Advertisers may not defraud the OpenAI Ads platform or **attempt to circumvent our policies or enforcement processes**. This includes activities intended to undermine the integrity or security of our advertising ecosystem."

Already quoted by wave 1b, repeated here only because it is the same clause family:

> "Interface imitation: Ads must be clearly distinguishable from the ChatGPT product experience..."
> "OpenAI reserves the right to refuse to display ad content and website links for any reason."

## From the Advertising Terms (`raw/openai-advertising-terms.txt`, "Updated: June 12, 2026"), the definition that binds the above

> "**'Destinations' means the landing pages, mobile applications, and other destinations to which Ads direct users, including URLs, redirects, and waypoints.**"

> "4.5. Ad Review and Removal. OpenAI may review, reject, remove, or require modification of any Ad at any time, for any or no reason, including non-compliance with law, these Advertising Terms, the OpenAI Policies, or applicable technical specifications."

Order submission, same document: "Such information and materials may include budget, Campaign Parameters, **Destinations**, and Ads."

## Searched and NOT found

`crawl`, `AdsBot`, `cloak` — zero occurrences in `openai-ad-policies.txt`, `openai-advertising-terms.txt`, or `openai-ad-tools-terms.txt`. The rule is written as an outcome duty on the advertiser's destination, never as a rule about what a crawler is served.

---

## Read, stated once

P3 resolves toward the branch `docs/plan/idea-set.md` §4 labelled "If restrictive": OpenAI's current Ad policies **do** impose an advertiser-side destination rule — end-to-end consistency, accurate representation, and a bar on circumventing enforcement processes. On its own text this binds the advertiser, applies to "landing pages... including URLs, redirects, and waypoints," and is enforceable by OpenAI's unilateral removal right.

Two consequences follow from 2a's own conditional map, not from new reasoning:
- **C3a/C3b**: an advertiser who buys ChatGPT ads and also serves OAI-AdsBot a destination different from what a user gets is contracting against "Ads must be consistent end-to-end" and "attempt to circumvent our policies or enforcement processes."
- **C7**: the named rule that 2a said would give OAI-AdsBot observability a compliance hook exists and is dated 2026-08-10.

## Caveats

- Source is a Wayback snapshot (archived 2026-08-18) of a page stamped 2026-08-10, not a live fetch — `openai.com` 403s every direct method tried across three passes. Whether the live page still carries these clauses on 2026-09-17 is `unknown — checked openai.com direct (403), 2026-09-17`.
- "Consistent end-to-end" is not the phrase "cloaking" and OpenAI defines no test for differential serving. The inference that serving OAI-AdsBot a different body breaches it is an inference, flagged as such — no enforcement action applying this clause was found by any pass.
- These clauses bind **advertisers**, i.e. OpenAI's own ad customers. They still do not reach a non-customer website whose organic content GPTBot fetches — wave 1b's structural finding stands for that case and is not disturbed here.
- The other seven documents wave 1b read were not re-searched this pass for comparable missed clauses. `unknown — not re-checked 2026-09-17`.
