# Crawler IP-range files — fresh pull, explore phase

Pull date: 2026-09-17. Method: `curl -sS -L` (direct fetch, this session's Bash tool) against each vendor's published JSON endpoint. Re-pulled independently of pass 2's `../../../docs/raw/injection-feasibility-pulls.md` fetch (2026-09-16) to check for drift and to get exact prefix counts; raw JSON saved as individual files in this same `raw/` directory (`oai-gptbot.json`, `oai-searchbot.json`, `oai-chatgptuser.json`, `oai-adsbot.json`, `anthropic-bots.json`, `perplexitybot.json`, `perplexity-user.json`, `googlebot.json`, `ccbot.json`).

## Command and status

```
curl -sS -L -m 15 "https://openai.com/gptbot.json" -o oai-gptbot.json
curl -sS -L -m 15 "https://openai.com/searchbot.json" -o oai-searchbot.json
curl -sS -L -m 15 "https://openai.com/chatgpt-user.json" -o oai-chatgptuser.json
curl -sS -L -m 15 "https://openai.com/adsbot.json" -o oai-adsbot.json
curl -sS -L -m 15 "https://claude.com/crawling/bots.json" -o anthropic-bots.json
curl -sS -L -m 15 "https://www.perplexity.com/perplexitybot.json" -o perplexitybot.json
curl -sS -L -m 15 "https://www.perplexity.com/perplexity-user.json" -o perplexity-user.json
curl -sS -L -m 15 "https://developers.google.com/static/search/apis/ipranges/googlebot.json" -o googlebot.json
curl -sS -L -m 15 "https://index.commoncrawl.org/ccbot.json" -o ccbot.json
```

All nine returned HTTP 200 after following redirects (perplexity.com issued a 302, google issued a 301, both auto-followed by `-L`).

## Prefix counts as of this pull, vs pass 2 (2026-09-16)

| File | creationTime in JSON | IPv4 prefixes this pull | Pass 2 count (2026-09-16) | Drift |
|---|---|---|---|---|
| oai-gptbot.json | 2025-10-30T11:00:00 | 21 | 21 | None — same creationTime, same list |
| oai-searchbot.json | 2026-01-02T11:00:00 | 39 | not counted in pass 2 | n/a |
| oai-chatgptuser.json | 2026-09-17T05:04:56 | 215 | not counted in pass 2 | creationTime is **hours before this pull** — this file regenerates frequently/on-demand, unlike gptbot.json's static Oct-2025 stamp |
| oai-adsbot.json | 2026-05-12T03:00:00 | 2 | not fetched in pass 2 (only description) | n/a — first direct pull |
| anthropic-bots.json | 2026-08-18T23:56:36Z | 26 | "20 prefixes, no per-bot labels" (via search relay, not fetched directly) | **26 vs 20 — count differs. Pass 2's number was WebSearch-relayed, not fetched; this pull is the first direct fetch of the file. Treat 26 as the current, verified count and pass 2's 20 as stale/relayed.** |
| perplexitybot.json | 2025-02-07T16:56:00 | 8 | not counted in pass 2 | n/a |
| perplexity-user.json | 2025-10-17T10:17:00 | 4 | not counted in pass 2 | n/a |
| googlebot.json | 2026-09-16T14:46:16 | 317 | n/a (not an idea-1 focus vendor) | pulled for reference/rDNS control only |
| ccbot.json | synctoken 20260811134000 | 5 (4 IPv4 + 1 IPv6 /56) | n/a | pulled for reference/rDNS control only |

## Notable content, read directly from the JSON

**Anthropic's combined list is multi-cloud, not single-vendor.** The 26 prefixes span Google Cloud (`34.x`, `35.x` blocks), Microsoft Azure (`40.124.101.48/28`, `20.102.46.224/28`, `20.64.57.208/28`), AWS (`16.58.26.69/32`, `18.225.238.228/32`, `18.227.226.255/32`), and one block, `216.73.216.0/22`, plus one single IP `136.107.176.208/32`, whose cloud ownership needed a separate ASN lookup (see `asn-lookups.txt` — both came back Amazon/Google respectively, not an Anthropic-owned ASN). No per-bot labeling inside the file — ClaudeBot, Claude-User and Claude-SearchBot are not distinguishable from this JSON alone, confirming pass 2's note.

**OAI-AdsBot is the smallest range by far** — 2 prefixes (`130.131.229.128/25`, `20.168.90.128/25`, 256 addresses total) vs GPTBot's 21 prefixes and ChatGPT-User's 215. Consistent with AdsBot being a narrow, purpose-built verification crawler rather than a general web crawler.

**oai-chatgptuser.json's creationTime is nearly live** (5:04:56 UTC on the pull day itself, pull happened ~07:04 UTC) — this file is regenerated far more often than gptbot.json (static since 2025-10-30). A detection scheme that caches OpenAI's published ranges needs to re-fetch ChatGPT-User's list on a much shorter cycle than GPTBot's, or it will silently miss new addresses. Not stated by OpenAI directly — inferred from the timestamp delta, measured-by-us.

**CCBot and Perplexity share a numeric neighborhood.** `ccbot.json` lists `18.97.9.168/29` and `18.97.14.80/29`/`18.97.14.88/30`; `perplexitybot.json` lists `18.97.1.228/30` and `18.97.9.96/29`; `perplexity-user.json` lists `18.97.21.0/30` and `18.97.43.80/29`. All sit inside AWS's `18.97.0.0/16` allocation (confirmed AS14618 AMAZON-AES us-east-1 by ASN lookup, see `asn-lookups.txt`). This does not prove shared crawling infrastructure between Common Crawl and Perplexity — `18.0.0.0/8` is one of AWS's largest customer-facing blocks and coincidental adjacency inside a /16 is unsurprising for any two AWS customers running EC2 crawlers in the same region — but it is close enough to be worth a note: rDNS and IP-range membership alone cannot distinguish "this is Perplexity's crawler" from "this is some other AWS-hosted crawler that happens to sit near Perplexity's published range," if an operator ever spoofed a source IP or if the published range is stale. Flagged, not concluded.
