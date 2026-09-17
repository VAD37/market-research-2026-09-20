# Detection-surface shelf life — is IP-list matching about to be superseded? — raw pull

Pulled: 2026-09-17, wave 2b. Method: direct `curl -L`, desktop Chrome UA. Answers wave 2a attack item 5 and this wave's attack line 6: how long does the measured "no PTR records, IP-list is the only method" finding stay true?

---

## 1. Cloudflare — Web Bot Auth is shipped, documented, and testable today

URL: `https://developers.cloudflare.com/bots/concepts/bot/verified-bots/web-bot-auth/` — HTTP 200, 157,771 bytes. Kind: vendor-reported.

Verbatim:

> "Web Bot Auth is an authentication method that leverages cryptographic signatures in HTTP messages to verify that a request comes from an automated bot. **Web Bot Auth is used as a verification method for verified bots and agents.** It relies on IETF drafts: a directory draft allowing the crawler to share their public keys, and a protocol draft defining how these keys should be used to attach the crawler's identity to HTTP requests."

Mechanism, verbatim (abridged to the operative parts):

> "Signature-Input header ... tag: This should be equal to `web-bot-auth`. keyid: This should be equal to the thumbprint computed in step 2. created ... expires ... nonce"

> "Signature-Agent header ... Cloudflare implements the Signature-Agent format from `draft-meunier-http-message-signatures-directory-03`, where the header value is a structured string such as `\"https://signature-agent.test\"`."

Example signed request shown on the page, verbatim:

```
Signature-Agent: "https://signature-agent.test"
Signature-Input: sig2=("@authority" "signature-agent") ;created=1735689600 ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U" ;alg="ed25519" ;expires=1735693200 ;nonce="e8N7S2MFd/qrd6T2R3tdfAuuANngKI7LFtKYI/vowzk4lAZYadIX6wW25MwG7DCT9RUKAJ0qVkU0mEeLElW1qg==" ;tag="web-bot-auth"
Signature: sig2=:jdq0SqOwHdyHr9+r5jw3iYZH6aNGKijYp/EstF4RQTQdi5N5YYKrD+mCT1HA1nZDsi6nJKuHxUi/5Syp3rLWBA==:
```

> "Note: You can test how Cloudflare interprets your signed requests against `https://crawltest.com/cdn-cgi/web-bot-auth`. This endpoint returns an HTTP 401 if your message is formatted correctly but your key is unknown, an HTTP 200 if the key is known and your message is verified, and an HTTP 400 otherwise."

> "Transitive trust and the Forwarded header. An agent that reaches your site is often not operated by the company that built it. A platfor[m]..." [truncated in the extraction]

**Searched and NOT found anywhere in this document:** `OpenAI`, `ChatGPT`, `Perplexity`, `Anthropic`. Cloudflare's Web Bot Auth page names no adopting AI operator. `unknown — checked developers.cloudflare.com/bots/.../web-bot-auth 2026-09-17` for which operators actually sign.

## 2. IETF — the underlying draft

URL: `https://datatracker.ietf.org/doc/draft-meunier-web-bot-auth-architecture/` — HTTP 200. Kind: standards-body (Internet-Draft, not an RFC).

Abstract, verbatim:

> "This document describes an architecture for identifying automated traffic using [HTTP-MESSAGE-SIGNATURES]. The goal is to allow automated HTTP clients to cryptographically sign outbound requests, allowing HTTP servers to verify their identity with confidence."
>
> "Authors: Thibault Meunier, Sandor Major"

[Note, mine: Meunier is the same name in Cloudflare's implemented `draft-meunier-http-message-signatures-directory-03`. An Internet-Draft is not a standard; no RFC number was found on the page this pass.]

## 3. A third party is already scoring engines on it in production

From `raw/wave2b-crawler-analytics-competitors.md` §1e, Known Agents' Agentic Web Index, verbatim:

> "A visit is considered spoofed when it claims a recognized agent identity but fails that agent's supported authentication method, such as **verified IP or HTTP message signature (Web Bot Auth)**."

[Note, mine: "verified IP **or** HTTP message signature" — a commercial product already treats the two as alternative, per-agent authentication methods as of 2026-09-17. That is evidence the transition is underway, not hypothetical.]

## 4. OpenAI's own current documentation — still IP ranges, no signatures

URL: `https://platform.openai.com/docs/bots` — HTTP 200, page text extracted 15,616 chars. Kind: vendor-reported. Pull date 2026-09-17.

Verbatim:

> "Overview of OpenAI Crawlers. OpenAI uses web crawlers ('robots') and user agents to perform actions for its products, either automatically or triggered by user request. OpenAI uses OAI-SearchBot and GPTBot robots.txt tags to enable webmasters to manage how their sites and content work with AI."

> "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links. To help ensure your site appears in search results, we recommend allowing OAI-SearchBot in your site's robots.txt file and **allowing requests from our published IP ranges below**."

> "Example user-agent string (the version number may change): `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot`"

> "When fetching robots.txt files, we may use a user-agent string with an additional robots.txt marker. The marker helps site owners more easily di[stinguish]..." [truncated in the extraction]

**Searched and NOT found anywhere in this document:** `signature`, `Signature`, `Web Bot Auth`, `verify`, `reverse DNS`.

[Note, mine: as of 2026-09-17 OpenAI's own crawler documentation still points site owners at user-agent plus published IP ranges and says nothing about request signing or reverse DNS. Wave 1's measurement (`raw/rdns-lookups.txt`: no PTR records on sampled OpenAI IPs) is consistent with vendor documentation, not contradicted by it.]

`https://openai.com/gptbot/` returned HTTP 403 on the same pull — the marketing URL is behind the same JS/bot challenge wave 1b hit. The developer-docs URL above is the reachable substitute.

---

## Read on shelf life, stated once

Two directions, both on file, not reconciled:

1. **Stable for now.** OpenAI's own docs, dated live 2026-09-17, still prescribe IP-range matching. Nothing in them signals a change.
2. **Migrating.** Cloudflare has a shipped, documented, publicly testable signature-verification path; the underlying IETF draft has named authors and a version-03 directory spec; and an independent commercial product already classifies agents by "verified IP **or** HTTP message signature" today.

The measurement is true today and has a named, dated successor mechanism already in production elsewhere. What is `unknown — checked cloudflare.com + platform.openai.com + datatracker.ietf.org 2026-09-17` is which AI operators sign, and on what timetable.

## Caveats

- Neither Cloudflare's page nor the IETF page names a single adopting AI operator. The claim "the transition is underway" rests on one third-party product's definition sentence plus Cloudflare shipping the verifier. That is suggestive, not a roster of adopters.
- `crawltest.com/cdn-cgi/web-bot-auth` was **not** exercised — no signing key exists and no test was run. Vendor-described behaviour only.
- The Internet-Draft was read only to its abstract and author line. Draft status, version and expiry were not transcribed.
- No Anthropic, Perplexity, Google or Microsoft crawler documentation was re-pulled this pass for signature support. `unknown — not checked 2026-09-17`.
