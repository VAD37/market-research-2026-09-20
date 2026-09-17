# Raw pull — payment rail out of Vietnam for recurring USD subscriptions

Pull date: 2026-09-17. Method: read `../../../../docs/markets/vietnam-sg-access.md` first (already covers Stripe/VN, Paddle-as-concept, Upwork+Payoneer working from VN, the Singapore holding-company route) — this pull does NOT redo that. It adds: Paddle's actual unsupported-country list, Lemon Squeezy's named seller-country support, Wise Business VN eligibility, and Payoneer fee specifics for recurring-USD collection. WebSearch used (not exhausted despite wave 2b's flag), WebFetch direct on vendor docs pages. No signups, no trials.

## What the existing research layer already established (not repeated in full — see the file itself)

- Stripe does not support Vietnam as a business location (confirmed from Stripe's own country list).
- Singapore Pte Ltd route exists, costs S$315 + nominee director SGD 1,200-6,000/yr, unlocks Stripe.
- Upwork and Payoneer already work from Vietnam today via SBV-approved rails (Vietcombank/Techcombank/VPBank), with the caveat that "mandatory dong conversion means USD reserves cannot sit in a Vietnamese account long-term."
- Paddle is named as a merchant-of-record option at "5% + 50¢ per transaction," but the file's own caveat states: "Paddle's page states no Vietnam-specific seller eligibility either way." That is what this pull resolves.

## Paddle — merchant of record

Source: https://www.paddle.com/help/start/intro-to-paddle/which-countries-are-supported-by-paddle, fetched 2026-09-17.

Verbatim: "Paddle works with software businesses anywhere in the world with the exception of the unsupported countries listed below." Full unsupported list (28 countries/regions), verbatim: "Afghanistan, Antarctica, Belarus, Burma (Myanmar), Central African Republic, Cuba, Crimea (Region of Ukraine), Democratic Republic of Congo, Donetsk (Region of Ukraine), Haiti, Iran, Iraq, Kherson (Region of Ukraine), Libya, Luhansk (Region of Ukraine), Mali, Netherlands Antilles, Nicaragua, North Korea, Russia, Somalia, South Sudan, Sudan, Syria, Venezuela, Yemen, Zaporizhzhia (Region of Ukraine), Zimbabwe."

**Vietnam is not on this list.** Reading: Vietnam is supported by omission from the exclusion list, not by an explicit named inclusion — Paddle's page never enumerates a positive list of 200+ supported countries in the fetched content, only the exclusions. Treat as **supported, moderate confidence** (absence from a maintained exclusion list on the vendor's own page), not a direct "Vietnam: yes" statement.

KYC/business registration: page states only that "our team may from time to time request further information before processing an order or releasing a payment from any location or jurisdiction for risk and compliance purposes" — no VN-specific requirement named.

Fee: **5% + $0.50 per transaction** (multiple third-party pricing breakdowns, 2026-dated, consistent with the figure already on file in vietnam-sg-access.md). Additional costs found this pull, third-party-reported: currency-conversion spread ~1.5-2% when payout currency differs from transaction currency; Paddle Retain (failed-payment recovery) takes 10-15% of recovered revenue if used; enterprise custom pricing available above $25M ARR (not relevant at this team's scale).

## Lemon Squeezy — merchant of record

Source: https://docs.lemonsqueezy.com/help/getting-started/supported-countries, fetched 2026-09-17.

**Vietnam is explicitly named** in Lemon Squeezy's bank-payouts supported-country list (per fetch: "the full list includes Albania through Vietnam, with Vietnam appearing as the final country listed" alphabetically). This is a stronger confirmation than Paddle's (a positive inclusion, not an absence from an exclusion list). PayPal payout option also listed as available in 200+ countries/regions generally.

Fee: base **5% + $0.50 per transaction** (multiple 2026-dated third-party breakdowns, consistent across sources). Add-on fees reported (third-party): international transactions +1.5%, PayPal transactions +1.5%, subscription payments +0.5%, abandoned-cart recovery +5% (of recovered revenue), affiliate referrals +3%. One third-party estimate: effective rate for a $10,000/mo SaaS founder can land 5.5%-11% depending on customer geography/payment method/features used — vendor-neutral aggregator estimate, not Lemon Squeezy's own stated figure.

## Wise Business — for receiving

Sources: https://wise.com/vn/business/ (fetched directly, 2026-09-17, no eligibility statement or fee numbers surfaced in fetched content); WebSearch 2026-09-17 for VN-specific eligibility; https://wise.com/help/articles/2977930/who-can-open-a-wise-business-account (404, could not fetch primary eligibility page).

**Third-party-reported, not confirmed on Wise's own eligibility page**: a secondary source states "Wise does not operate in Vietnam, as Vietnam is grayed out in Wise's country selection dropdown" for opening a Wise Business account, and concludes "Vietnam companies would not be eligible for Wise Business accounts." Wise does maintain a Vietnam-facing marketing page (wise.com/vn/business/) but that appears to target Vietnam-based individuals/businesses sending or receiving money via Wise's personal/consumer rails, not necessarily business-account company registration in Vietnam.

`unknown — checked wise.com/vn/business/, wise.com/help/articles/2977930 (404) 2026-09-17 — Wise's own primary eligibility statement for a Vietnam-registered company was not reachable; the "not eligible" claim is third-party-reported only`.

Fee data point found (general, not VN-specific): receiving a SWIFT international payment in USD costs USD 6.11 (third-party-reported, source: a Wise-focused review site, not Wise's own fee page for this specific corridor).

## Payoneer — for receiving

Source: https://www.payoneer.com/pricing/, fetched directly 2026-09-17 (vendor's own page). Already established as working from Vietnam today per the existing research file; this pull adds fee specifics relevant to recurring USD subscription collection:

- Receiving via credit-card-funded payment request: **"Up to 3.99% + 0.49 USD or equivalent."**
- Moving funds between Payoneer balances (currency conversion): **0.50%.**
- Card transactions with currency conversion: **up to 3.5%.**
- Withdrawal to a bank account in a non-local currency (i.e., USD payout converted to VND at a Vietnamese bank), with currency conversion: **1.2%-4%, minimum fee up to $20.00 or equivalent.**
- Annual account fee: **$29.95**, but only applies if the account receives less than $6,000 USD (or equivalent) in any 12 consecutive months.
- Marketplace-sourced receipts (Upwork/Fiverr-style): third-party-reported at ~1% receiving fee (not from Payoneer's own pricing page directly — this figure came from a WebSearch summary of secondary sources, not the fetched primary page).
- Payoneer's own page states fees "depend on sender and recipient locations, payment method, and currencies" — treat all percentages above as ranges, not fixed rates for this team's specific corridor.

## What this adds to the file's existing ranking

The existing vietnam-sg-access.md ranking (revised after its own recovery pass) was: (1) merchant of record [Paddle] — no entity, no KYC wall; (2) Singapore Pte Ltd; (3) US LLC from Vietnam — broken in practice. This pull adds a second MoR option (Lemon Squeezy) with a **more explicit, name-level Vietnam confirmation** than Paddle's own page gives, at the same headline 5%+50¢ rate plus similar percentage add-ons. For receiving into a Vietnamese bank without an MoR (i.e., billing customers directly and moving the cash home), Payoneer is confirmed working with quantified fees (1.2%-4% VND conversion + per-transaction receiving fee); Wise Business eligibility for a Vietnam-registered company is unresolved by a primary source and third-party-reported as likely unavailable.

## Caveats

- Paddle's Vietnam status is inferred from absence off a 28-country exclusion list, not a positive statement — moderate, not full, confidence.
- Wise's Vietnam Business-account eligibility rests on one secondary source; Wise's own eligibility documentation could not be reached (404) this pull.
- Fee figures for Lemon Squeezy's add-ons (international/PayPal/subscription/abandoned-cart/affiliate surcharges) are third-party aggregator estimates, not fetched from Lemon Squeezy's own pricing page directly this pull — https://www.lemonsqueezy.com/pricing itself was not fetched, only searched.
- None of these rails were tested with an actual Vietnam-registered entity in this pull (no signups, per instruction) — every eligibility claim here is documentation-level, not a confirmed working account.
