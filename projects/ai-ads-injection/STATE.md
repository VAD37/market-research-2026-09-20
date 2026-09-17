# STATE — ai-ads-injection

Append-only running log. Newest entry at the bottom. Write the plan BEFORE the work, the result AFTER it. An agent that dies mid-run must leave its successor enough to continue.

Entry format:

```
## <UTC+7 timestamp> — <agent role> — <phase>
PLAN: what is about to happen
DID: what happened
FILES: paths written
OPEN: what is unfinished, and what the next agent should pick up first
```

---

## 2026-09-17 — main thread — scaffold
PLAN: create project folder, brief, state log.
DID: folder skeleton + `CLAUDE.md` written from `MegaPlan.md` and the three research passes in `../../docs/`.
FILES: `CLAUDE.md`, `STATE.md`, `docs/{explore,plan,design,review,execution,outcome}/`, `raw/`, `prototype/`.
OPEN: explore phase not started.

## 2026-09-17 — explore agent — phase 1 start
PLAN: read carried-over research (injection-feasibility, ai-search-ads, roster, tos-pulls, cross-read, pass3-read) — done. Next: check local machine for domain/Cloudflare/server access; fetch engine crawler IP-range files fresh; nslookup/whois samples; write docs/explore/{carrier-state,detection-surface,edge-controls,policy-ceiling,who-sells-this}.md; raw/ pulls for everything measured.
DID: (pending)
FILES: (pending)
OPEN: (pending)

## 2026-09-17 — explore agent — measurement chunk complete
PLAN: (see prior entry)
DID: Checked local machine for domain/Cloudflare/server access — none found (raw/local-infra-check.txt). Fetched 9 crawler IP-range JSON files fresh (raw/oai-*.json, anthropic-bots.json, perplexitybot.json, perplexity-user.json, googlebot.json, ccbot.json; index in raw/crawler-ip-ranges-2026-09-17.md — Anthropic's file has 26 prefixes now vs pass 2's relayed 20). Ran rDNS lookups against 8.8.8.8 on samples from each engine (raw/rdns-lookups.txt) — key finding: OpenAI and OAI-AdsBot IPs have NO PTR records at all; Perplexity/CCBot resolve to generic AWS EC2 hostnames; Anthropic resolves to generic GCP/AWS hostnames; only Google has vanity rDNS (*.googlebot.com) supporting its documented forward-confirm method. Ran ASN lookups via ip-api.com (raw/asn-lookups.txt) — OpenAI = 100% Azure/AS8075 on sampled ranges; Anthropic spans AWS+GCP (no Azure); Perplexity+CCBot both AWS us-east-1/AS14618, numerically adjacent in 18.97.0.0/16 (flagged, not conclusive). Pulled Cloudflare edge-control docs (bot score fields, WAF actions, Transform Rules limits, AI Crawl Control/Pay-per-crawl still private beta 14+ months on) and Fastly (Bot Management is AI-crawler-aware but enterprise/sales-gated; VCL bot-detection doc 404'd) — raw/policy-and-edge-pulls.md. Pulled ad-disclosure primary sources: FTC Endorsement Guides (no AI mention), DSA Article 26 (via third-party mirror, eur-lex itself JS-gated), UCPD Annex I item 11 "advertorial" verbatim via UK statutory instrument (eur-lex JS-gated). Vietnam Law on Advertising NOT reached — 404s/403/timeout on 4 URLs, WebSearch returned "unavailable" (quota likely still exhausted). Bing webmaster guidelines and OpenAI ads-terms pages are JS-shell/403'd — need browser access, not done this pass.
FILES: raw/local-infra-check.txt, raw/crawler-ip-ranges-2026-09-17.md, raw/{oai-gptbot,oai-searchbot,oai-chatgptuser,oai-adsbot,anthropic-bots,perplexitybot,perplexity-user,googlebot,ccbot}.json, raw/nslookup-samples.txt, raw/rdns-lookups.txt, raw/asn-lookups.txt, raw/policy-and-edge-pulls.md, raw/ucpd-annex1-uk.html, raw/ucpd-annex1-uk2.html, raw/bing-webmaster-guidelines.html (empty/JS-shell, no cloak text), raw/vn-advertising-law.html (404 page, negative-finding evidence).
OPEN: Vietnam advertising law text; Bing/Copilot cloaking policy; OpenAI ads-terms disclosure rule; Fastly VCL bot-detection primitive at non-enterprise tier; full Workers "Conditional response" example script body — all need browser access (claude-in-chrome) or a WebSearch reset, next agent's first move. Next: write the five docs/explore/*.md deliverables from what is gathered.

## 2026-09-17 — explore agent — phase 1 complete
PLAN: (see prior entries)
DID: Wrote all five required docs/explore/*.md deliverables: carrier-state.md (pass 2's settled vs open items, quoted verbatim, plus this pass's resolutions — Anthropic IP count 20→26, OpenAI Azure ASN confirmed), detection-surface.md (per-engine table with measured rDNS/ASN, key finding: only Google/CommonCrawl have vanity rDNS, OpenAI/Anthropic/Perplexity crawlers sit on generic cloud rDNS or none at all — IP-list matching is the only reliable method for those three), edge-controls.md (Workers is the only Cloudflare primitive that can vary response body; WAF rules and Transform Rules cannot; Pay-per-crawl still private beta 14mo on; Fastly's AI-aware bot product is enterprise/sales-gated), policy-ceiling.md (Google cloaking/spam policy carried from pass 2; FTC Endorsement Guides have no AI mention; UCPD Annex I item 11 "advertorial" quoted verbatim as the sharpest primary-source hit; DSA Art 26 applicability to AI answers unresolved; Vietnam law unreached), who-sells-this.md (roster spot-checked, unchanged in 24h; injection-audit gap re-confirmed, no new vendor found). All cite raw/ evidence pulled this session.
FILES: docs/explore/{carrier-state,detection-surface,edge-controls,policy-ceiling,who-sells-this}.md — all written, all cite raw/.
OPEN: (unchanged from prior entry — see there) OpenAI Business Terms/Services Agreement and Perplexity API ToS never read by any pass (highest-value gap for plan phase); Vietnam advertising law unreached; Bing/Copilot policy and OpenAI ads-terms need browser access; WebSearch returned "unavailable" once today, budget accordingly. Phase 1 (explore) is done. Handing off to phase 2 (Opus plan/design agent) — it should start from carrier-state.md, then read the other four explore docs, then decide the plan.
