# Crawler-analytics products that already exist — raw pull

Pulled: 2026-09-17, wave 2b. Method: direct `curl -L` with a desktop Chrome UA, HTML stripped to text locally. No WebSearch (budget exhausted 200/200), no browser extension (dead all session). Every block below is the vendor's own page text, verbatim or lightly de-tagged; bracketed notes are mine.

---

## 1. Known Agents (formerly Dark Visitors) — Bit Flip LLC

`https://darkvisitors.com/` → HTTP 200, 46,368 bytes. The page serves **Known Agents** branding and links to `https://knownagents.com/`. Footer: `© 2026 Bit Flip LLC`. Treat `darkvisitors.com` and `knownagents.com` as the same product under a rename. Kind: vendor-reported.

### 1a. Homepage, verbatim fragments

> "See how AI agents are crawling your website / referring customers to you / buying your products / using your tools"

> "Half of your traffic isn't human anymore. Track, control, and optimize for AI agents and bots."

> "Get Started for Free →"

> "Join 5,000+ websites ready for the next era of the internet, or request a demo."

> "Introducing The Agentic Web Index. See everything AI agents and bots are doing across 5,000+ websites. Explore the Data →"

Product nav, verbatim: `Agent Analytics`, `AI Chat Referral Tracking`, `Automatic Robots.txt`, `Agent Identification API`.
Setup-guide nav, verbatim: `Send Visit Events`, `Set Up Automatic Robots.txt`, `Block Bad Bots`, `Use the Agent Identification API`.
Resources nav: `Agent Directory`, `The Agentic Web Index`. Free Tools: `AI Bot Robots.txt Checker`.

Homepage chart legend (the agent taxonomy it reports on), verbatim series labels:
`AI Agent`, `AI Coding Agent`, `AI Assistant`, `AI Search Crawler`, `AI Data Scraper`. Y-axis label: `Agent Visits`.

Integration guides linked from the homepage nav (`/docs/analytics/...`), verbatim slugs:
`akamai`, `aws`, `cloudflare-worker`, `fastly`, `google-cloud`, `nodejs`, `rest-api`, `vercel`, `wordpress`, `wordpress-vip`.
[Note, mine: `cloudflare-worker` is a published, supported integration path — the same primitive wave 1's `edge-controls.md` identified as the only Cloudflare way to do this.]

### 1b. Pricing page — `https://darkvisitors.com/pricing`, HTTP 200

> "Pricing. Getting started is completely free and self-serve, even for enterprises. Connect your website first and upgrade later only if needed."

| Plan | Price | Projects | Events/month | Features |
|---|---|---|---|---|
| Start Here | **$0 / month** "For most websites" | 1 | 100K | Basic features |
| Startup | **$29 / month** "For small businesses" | 3 | 1M | Premium features |
| Growth | **$299 / month** "For medium businesses" | 10 | 10M | Premium features |
| Enterprise | Custom, "Request a Demo" | Unlimited | Usage-based | Custom features & API |

Feature-comparison rows, verbatim: `CSV Export — Download reports for custom analysis`; `MCP Access — Connect AI assistants to project reports`; `Automatic Robots.txt — Generate an automatically updating robots.txt that blocks all known agents`; `WordPress Rule Enforcement — Block agents who ignore your robots.txt rules with the WordPress plugin`; `Agent Identification API — Used for implementing access policies based on verified agent identity`; `Reporting API — Used for custom dashboards and report automation`.

> "★★★★★ 4.8 Out of 5 Stars on WordPress. Known Agents is trusted by thousands of websites across the internet."

FAQ, verbatim: "Agents account for about half of all website traffic. Start with roughly twice your monthly human visit count..."

### 1c. Agent Analytics — `https://knownagents.com/products/agent-analytics`, HTTP 200

> "Agent Analytics. See every crawler, scraper, and AI agent visiting your website in real time."

### 1d. Agent Identification API — `https://knownagents.com/products/agent-identification-api`, HTTP 200

> "Agent Identification API. Identify AI agents and other bots from incoming network requests, from your own code."

Sample response shown on the page, verbatim:

```
// Response
{ "agent_token": "Claude-User", "agent_type_name": "AI Assistant", "operator_name": "Anthropic", "result": "verified" }
```

> "The Agent Identification API tells you exactly which agent is behind every request, and proves it isn't spoofed."

> "We keep track of 2,000+ agents, so you don't have to. Leave the collection, categorization, and maintenance to us, so you can focus on what makes your product unique."

Stated buildables, verbatim: "Content Licensing — Grant verified agents access to licensed articles, archives, and datasets"; "Monetization — Enforce paywalls, charge for access, and meter verified agent usage"; "Abuse Prevention — Detect spoofed agents and challenge suspicious automated traffic"; "Data Enrichment — Supplement your logs with agent name, category, and operator".

Published agent taxonomy (verbatim definitions, abridged to the two that matter here):
> "AI Assistant — Fetches website content in response to a user prompt, to include in an AI-generated answer"
> "AI Search Crawler — Indexes website content to possibly include as citations in AI-powered search results"

### 1e. The Agentic Web Index — `https://darkvisitors.com/insights`, HTTP 200, 495,609 bytes

Schema.org `Dataset` block on the page, verbatim:

> "name": "The Agentic Web Index", "description": "A continuously updating analysis of bot vs. human traffic, AI training, fetching, search indexing, browsing, robots.txt compliance, and AI chat referrals across 5,000+ websites.", "url": "https://knownagents.com/insights", "creator": {"@type": "Organization", "name": "Known Agents"}, **"isAccessibleForFree": true**, "variableMeasured": ["Bot vs. human traffic", "AI agent activity", "Robots.txt effectiveness", "Bot impersonation and spoofing", "AI chat referrals"]

Section list, verbatim: `Overview`, `AI-Related Activity`, `AI Training`, `AI Fetching`, `AI Search Indexing`, `AI Browsing`, `Robots.txt & Compliance`, `Spoofing & Security`, `AI Chat Referrals`, `Methodology`, `FAQ`.

Headline metrics, verbatim (vendor-reported, "Key ecosystem metrics across 5,000+ websites using Agent Analytics and AI Chat Referral Tracking"):

| Metric | Value | Change vs previous 90 days | Vendor's own definition |
|---|---|---|---|
| Bot vs. Human Traffic | 33% | ↓ 2% | "The amount of visits from known agents vs. humans" |
| Agentrification | 28% | ↑ 7% | "The percentage of bot traffic that's AI-related" |
| AI Chat Referral Volume | 0.1% | ↑ 14% | "The percentage of human website visits that come from AI chat" |
| Robots.txt Effectiveness | 94.3% | — | "How often bots follow robots.txt rules" |

Time-series x-axis on the "Traffic by Agent Type" chart runs `Jun 19` → **`Sep 16`** [i.e. data through the day before this pull].

Spoofing section, verbatim:

> "Spoofing & Security. See which agents are most frequently impersonated, and how spoofing activity changes over time. A visit is considered spoofed when it claims a recognized agent identity but fails that agent's supported authentication method, such as **verified IP or HTTP message signature (Web Bot Auth)**."

> "Active Threat: AI Bot Spoofing Campaign. We are observing a widespread campaign impersonating AI bots to scan websites for vulnerabilities. The attacker appears to be targeting credential and configuration paths used by AI coding tools."

Top spoofed agent identity listed first: `Googlebot`. Also visible in the blocked-agents list: `Amazonbot — AI Data Scraper — 17.1% — Agents blocked by the most top websites`.

### 1f. AI Chat Referral Tracking — `https://darkvisitors.com/products/ai-chat-referral-tracking`, HTTP 200

> "Measure human traffic from ChatGPT, Claude, Gemini, and all other AI chat platforms."

> "Are you showing up in AI chat responses? Find out how AI assistants are talking about you, and which pages they're recommending to people."

Stated dimensions, verbatim: "Platforms — Which AI assistants do your customers use?"; "**Citations — Which links appear in AI chat responses?**"; "Referrals — Which links do people actually click on?"; "Click-Through — How often people are clicking citations at all?"; "Geography — Where are these new visitors coming from?"

Platforms named: ChatGPT, Claude, Copilot, DeepSeek, Gemini, Meta AI, Mistral, Perplexity.
Illustrative figure on page: "6.7% — Links in AI chat responses that were clicked".

> "Track AI chat referrals for free in under 5 minutes."

> "MCP Access — Analyze your referral traffic by asking ChatGPT, Claude, etc. Plus team access, historical import, CSV export, and long-term reporting."

---

## 2. Cloudflare AI Crawl Control — `https://developers.cloudflare.com/ai-crawl-control/`, HTTP 200

Page stamp, verbatim: **"Last updated Aug 14, 2026"**. Kind: vendor-reported.

> "Available on all plans"

> "Monitor and control how AI services access your website content."

> "AI Crawl Control (formerly AI Audit) gives you visibility into which AI services are accessing your content, and provides tools to manage access according to your preferences."

Bulleted capabilities, verbatim:
> "See which AI services access your content - Monitor the dashboard to see crawler activity and request patterns"
> "Control access with granular policies - Set allow or block rules for individual crawlers"
> "Monitor robots.txt compliance - Track which crawlers follow your directives and create enforcement rules"
> "Explore monetization options - Set up pay per crawl pricing for content access (private beta)"
> "**Deploy with zero configuration - Works automatically on all Cloudflare plans**"

Feature pages listed in nav: `Analyze AI traffic — Gain insight into how AI crawlers are interacting with your pages`; `Track robots.txt`; `Manage AI crawlers`; `Pay Per Crawl` (still marked **Beta**, consistent with wave 1's finding). Reference section includes `GraphQL API`, `Bot reference`, `Worker templates`.

### 2a. Cloudflare's AI Crawl Control Worker templates — `https://developers.cloudflare.com/ai-crawl-control/reference/worker-templates/`, HTTP 200

Only one template is published, verbatim:

> "x402 Payment-Gated Proxy. The x402-proxy template implements payment-gated access using the x402 protocol — an open payment standard built around HTTP 402 (Payment Required). Use it to monetize crawler access, paywall specific routes, or charge bots while letting humans through free."

[Note, mine: Cloudflare ships a Worker template that branches behaviour on crawler identity — payment gate, not variant body. No template for logging or for content variation.]

---

## Caveats

- Everything above is vendor marketing copy on the vendor's own site. No customer, contract, revenue or independent audit figure was found for Known Agents. "5,000+ websites" and "thousands of websites" are vendor-stated, unverified.
- The Agentic Web Index's headline percentages are computed over a self-selected panel of sites that installed a free analytics product. No methodology text was extracted this pass — the `Methodology` section exists on the page but its body was not transcribed. `unknown — checked darkvisitors.com/insights 2026-09-17`.
- Known Agents' funding, headcount and founding date were not pulled — `unknown — checked darkvisitors.com/about not fetched, 2026-09-17`. The only corporate fact captured is the footer, `© 2026 Bit Flip LLC`.
- `https://www.tryprofound.com/products/agent-analytics` returned HTTP 404 on 2026-09-17 — Profound was not confirmed to sell origin-log agent analytics either way. `unknown — checked tryprofound.com 2026-09-17`.
- `https://knownagents.com/agentic-web-index` 404s; the index lives at `/insights` on both domains.
