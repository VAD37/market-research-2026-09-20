# Merchant-of-record seller eligibility for a Vietnam-resident seller — raw pull

Pulled: 2026-09-17, wave 2a-bis. Method: direct `curl -L` with a desktop Chrome UA, HTML stripped to text locally. No WebSearch (exhausted 200/200). No browser extension (never connected this session). Kind: vendor-reported throughout.

Why this pull: `docs/review/market-check.md` §9 constraint 7 says "Bill in VND or solve payments first — Merchant-of-record does not cover services billing; Stripe does not cover Vietnam." Its source, `../../../docs/markets/vietnam-sg-access.md`, says of the MoR route: "no entity, no KYC wall, no Form 5472. The only route with no residency requirement anywhere in it. Costs the most per transaction and **does not work for services billing**" — and, in its own caveats, "**Paddle's page states no Vietnam-specific seller eligibility either way.**" That leaves the *product*-billing case open. This pull closes it for two MoR vendors.

---

## 1. Polar — `https://docs.polar.sh/merchant-of-record/supported-countries` (HTTP 200)

Verbatim, "Payments & Merchant of Record" section:

> "We support payments globally except from countries with US sanctions (Cuba, Russia, Iran, North Korea, and Syria). As your Merchant of Record (MoR) we take on the liability for international sales taxes."

Verbatim, "Payouts" section — this is the seller-side sentence:

> "Polar uses Stripe Connect Express to issue payouts to residents or businesses in any of the countries below. See Payout Accounts for how to connect one."

The country list that follows that sentence ends, verbatim: `"... 🇦🇪 United Arab Emirates 🇬🇧 United Kingdom 🇺🇸 United States 🇺🇾 Uruguay 🇺🇿 Uzbekistan 🇻🇳 Vietnam"` — immediately before the page's "Frequently Asked Questions" heading.

Verbatim, the FAQ item directly under it:

> "Stripe isn't available in my country. Can I still use Polar? As the Merchant of Record, Polar takes care of charging customers, so Stripe Payments doesn't need to be available in your country."

## 2. Lemon Squeezy — `https://docs.lemonsqueezy.com/help/getting-started/supported-countries` (HTTP 200)

Verbatim:

> "Lemon Squeezy supports merchants and affiliates in hundreds of countries. Find out if your country is supported for payouts and purchases."

> "Lemon Squeezy can offer services to merchants and affiliates who can receive bank or PayPal payouts in one of the hundreds of countries we support."

The payout-country list on that page ends, verbatim: `"... United Arab Emirates United Kingdom United States Uruguay Uzbekistan Vietnam"`, followed immediately by the footnote `"(*) From May 2024, Stripe only accepts new accounts from India on an invite-only basis."`

## 3. Paddle — not closed

- `https://developer.paddle.com/concepts/sell/supported-countries-locales` (HTTP 200) and its `.md` sibling are **buyer-side only**: "Go global and sell in over 200 countries and territories". No seller/merchant eligibility statement on the page.
- `https://www.paddle.com/help/start/intro-to-paddle/which-countries-does-paddle-support` — HTTP 404.
- `https://www.paddle.com/help/start/intro-to-paddle/does-paddle-have-any-country-restrictions` — HTTP 404.
- `https://www.paddle.com/legal/seller-terms`, `.../paddle-seller-terms` — HTTP 404.
- `unknown — checked paddle.com + developer.paddle.com direct fetch, 2026-09-17`. Paddle's own seller-country position is still unresolved, as `vietnam-sg-access.md` already recorded.

---

## What this pull establishes, stated once

A seller resident in Vietnam can be paid out for a **digital product** by at least two merchant-of-record platforms, on each vendor's own documentation, without a foreign entity and without Stripe supporting Vietnam. It says nothing about **services** billing, where `vietnam-sg-access.md`'s finding is undisturbed.

## Caveats

- Both statements are vendor documentation, not a completed onboarding. Neither was tested by signing up; identity verification, payout-account approval and product-category review could still reject a Vietnamese seller. `unknown — not tested`.
- Polar's payouts run on Stripe Connect Express; Lemon Squeezy is Stripe-owned. Both therefore inherit Stripe-side KYC even though Stripe *Payments* is unavailable in Vietnam — the two are different products, and neither vendor page states which Stripe requirements apply to a Vietnamese payout account.
- Fees were not pulled this wave. `unknown — not pulled`.
- Neither page carries a visible last-updated stamp in the fetched text.
- Nothing here creates a buyer. It removes one structural reason to reject a product-shaped candidate; it supplies no demand evidence of any kind.
