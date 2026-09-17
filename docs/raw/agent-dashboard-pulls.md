## GitHub — NousResearch/hermes-agent
- URL: https://github.com/NousResearch/hermes-agent
- Pulled: 2026-09-16
- Method: WebFetch

Description: "A self-improving AI agent built by Nous Research featuring an integrated learning loop that creates skills from experience, maintains persistent memory, and runs across multiple platforms (CLI, Telegram, Discord, Slack, etc.)."
Star count observed: 246.1k (note: other pulls same week show 214k and "100,000+" — see caveats). License: MIT.
Key features listed: "Built-in learning loop with autonomous skill creation; Multi-platform support (Telegram, Discord, Slack, WhatsApp, Signal, CLI); Persistent memory with FTS5 session search; Scheduled automation via cron; Parallel subagent delegation; Support for multiple LLM providers (Nous Portal, OpenRouter, OpenAI, etc.); Seven terminal backends (Docker, SSH, Modal, Vercel Sandbox, etc.); MCP server integration; Context file support."
Languages: Python, JavaScript/Node.js, Shell scripting.
Dashboard mention: "References to Nous Portal dashboard for unified API key management across 300+ models and integrated tooling."

## Nous Research — Hermes Agent official site
- URL: https://hermes-agent.nousresearch.com/
- Pulled: 2026-09-16
- Method: WebFetch

"Hermes Agent is an open-source AI agent platform developed by Nous Research that emphasizes multi-platform connectivity and persistent memory."
Connectivity: "Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI — and a growing list of platforms"
Memory: "learns your projects, auto-generates skills, and never forgets how it solved a problem."
Automation: "reports, backups, and briefings — running unattended through the gateway."
Delegation: "isolated subagents with their own conversations, terminals, and Python RPC scripts."
Capabilities: web search, browser automation, vision, image generation, text-to-speech.
Sandboxing: "Five execution backends are available—local, Docker, SSH, Singularity, and Modal—with container hardening."
License: MIT, free/OSS via GitHub.
Hosting: local desktop (macOS 12+, Windows 10/11, Linux); cloud via Nous Portal; terminal install.
Pricing (Nous Portal): "Tiered subscription through Nous Portal (Free, Plus $20/month, Super $100/month, Ultra $200/month), including monthly model credits and access to 200+ models."
Creator: Nous Research, Inc.

## TechCrunch — Nous Research funding at $1.5B valuation
- URL: https://techcrunch.com/2026/07/13/hermes-agent-maker-nous-research-in-talks-for-new-funding-at-1-5b-valuation/
- Pulled: 2026-09-16
- Method: WebFetch

"Nous Research develops the open-source Hermes agent, an AI tool that runs locally or on cloud servers to automate tasks. The company also creates specialized language models focused on coding and mathematics."
Funding round: "At least $75 million" at "$1.5 billion" valuation, lead investor Robot Ventures, with USV and other prominent investors. Date: July 13, 2026.
Previous funding: "Total of $70 million raised before this round from Paradigm, Robot Ventures, North Island Ventures, Delphi Ventures, OSS Capital, and Balaji Srinivasan."
Founders: Jeffrey Quesnelle, Karan Malhotra, Ryan Teknium, Shivani Mitra (founded 2023).
Traction (article-stated, unclear primary/secondary source): "GitHub presence with approximately 214,000 stars and nearly 40,000 forks."
Headcount: not mentioned in article.

## Nous Research — corporate homepage
- URL: https://nousresearch.com/
- Pulled: 2026-09-16
- Method: WebFetch

Self-description: "a leader in the American open source AI movement," tagline "Artificial Intelligence Made Human," positions itself as "THE AI ACCELERATOR COMPANY."
Mission: advancing "human rights and freedoms by creating and proliferating open source language models."
Products listed: Hermes models (Hermes 4, Hermes Agent), Nous Portal, Nous Chat, Simulators.
No headcount, funding, or pricing details found on this page per fetch.

## AlphaSignal — Nous Research packages Hermes Agent for Teams and Private Infrastructure
- URL: https://alphasignal.ai/news/nous-research-packages-hermes-agent-for-teams-and-private-infrastructure
- Pulled: 2026-09-16
- Method: WebFetch

Announcement date: September 14, 2026.
Hermes Business (Team tier): managed tier within Nous Portal. "One shared credit balance and per-member caps" — pooled credits with individual spending limits; access to 248 models through Portal catalog; messaging integrations; shared skill library (conversation histories/personal memories remain individual). Pricing not disclosed.
Hermes Enterprise (self-hosted): organization-controlled infra (on-prem or private cloud); contract-based pricing (undisclosed terms); self-hosted agent/memory/skill systems; open-weight or privately hosted model flexibility; "no telemetry or tracking requirements in core deployment"; private skills/agent infra; "Infrastructure and data controls set by the customer." Article notes: "procurement teams will need additional details on SSO, audit logs, backup procedures, and SLAs not covered in the announcement."

## Context Studios — Hermes Web Dashboard: The Agent Control Plane Has Arrived
- URL: https://www.contextstudios.ai/blog/hermes-web-dashboard-the-agent-control-plane-has-arrived
- Pulled: 2026-09-16
- Method: WebFetch

Dashboard runs on localhost port 9119. Features: "Status page with real-time agent version, gateway state, session counts, and recent session previews"; "Live log viewer filtering by file, severity level, and component"; "Session browser with full-text search across message content and resumable chat history"; "Cron scheduler interface displaying job timing, last-run output, and next triggers"; "API Keys manager organizing credentials by category with redacted previews and deletion controls"; "Configuration editor covering '150+ config fields' with form-based interface and dropdown validation"; "Embedded TUI (terminal interface) accessible via browser using xterm.js and WebSocket streams."
Positioning — three-pattern landscape for agent operations per the article: (1) "Hosted control planes (Claude Code, Codex) - vendor-managed infrastructure"; (2) "Spec-driven orchestration (OpenAI Symphony) - orchestration framework without built-in UI"; (3) "Self-hosted dashboards (Hermes) - agent runtime plus operations UI combined."
"The dashboard addresses requirements unique to long-running agents: credential governance, session archaeology, approval-mode management, and cron visibility that CLIs cannot provide at scale."
Approval/governance: config has approval-mode settings (`ask`, `yolo`, `deny`) controlling autonomous execution vs. human confirmation — "a 'governance decision' rather than developer preference suitable for team audit."
Limitations (article-stated): "The current release lacks multi-user authentication, requiring reverse proxy solutions (nginx, Tailscale, VPN) for shared-server deployments. No explicit multi-agent orchestration or cost-tracking features are mentioned."

## Search snippet aggregation — Hermes 4 model card / OpenRouter / HF
- URL: https://huggingface.co/NousResearch/Hermes-4-405B ; https://openrouter.ai/nousresearch/hermes-4-405b
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet, not full fetch)

"Hermes 4 is the family of open-weight models Nous Research released in August 2025, in 14B, 70B and 405B parameter sizes." License: "The 14B, based on Qwen3-14B, uses the permissive Apache-2.0 licence. The 70B and 405B start from Llama 3.1 and inherit the Llama3 licence, which imposes some conditions on large-scale use." Features: "hybrid reasoning: one model answers directly or deliberates with think tags before replying, and it keeps the Hermes tool-calling format for agents." Also: "structured outputs, including JSON mode, schema adherence, function calling, and tool use." Training: "Post-training corpus: Massively increased dataset size from 1M samples and 1.2B tokens to ~5M samples / ~60B tokens." Benchmarks (405B, reasoning on): "96.2% on MATH-500, 78.1% on AIME 2025 and 61.4% on LiveCodeBench." Context: "131,072 token context window."

## Search snippet — Nous Research Hermes Agent launch timeline (Vellum, Startup Fortune, Releasebot)
- URL: https://www.vellum.ai/blog/official-hermes-agent-breakdown ; https://startupfortune.com/nous-research-brings-hermes-agent-out-of-the-terminal/ ; https://releasebot.io/updates/nousresearch/hermes-agent
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet, not full fetch)

"Hermes Agent is Nous Research's open-source AI agent, released in February 2026." "Hermes Desktop, announced in public preview on June 2, brings Hermes Agent into a native app for macOS, Windows and Linux." "the Herald release on August 3, 2026 alone carried roughly 3,650 commits, 1,400 merged pull requests, and contributions from more than 650 people." "Nous Research opened team and enterprise tiers for its self-hosted Hermes Agent, adding shared balances, per-member caps, and on-prem deployment."

## Search aggregation — AI Agent Observability market sizing + enterprise spend
- URL: https://www.globemarketresearch.com/press-release/ai-agent-observability-market-news ; https://www.digitalapplied.com/blog/ai-agent-adoption-2026-enterprise-data-points
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"56% of enterprises now have a formal 'AI agent owner' or 'agentic ops' lead, up from 11% in 2024" (attributed by digitalapplied to Gartner data referenced in article).
"Average annual spend on agent evals and observability ranges from $310k for mid-market to $2.4M for Fortune 500 companies." (source attribution unclear/not explicit in article).
"71% of enterprises report increased 2026 budget for AI evaluation tooling specifically" (attributed to Forrester/BCG 2026 surveys per article).
"Only 38% of production agents run automated evals on every prompt change" (attributed to a Forrester 2026 panel per article).
"The global AI Agent Observability Market was valued at USD 0.9 billion in 2026 and is projected to reach approximately USD 14.0 billion by 2035, growing at a CAGR of 35.6%. North America held the largest regional share of 44.3%, representing approximately USD 0.40 billion in 2026." — analyst-derived market-research report (globemarketresearch), methodology not disclosed in snippet.
"57% of organizations now run AI agents in production, yet observability remains the lowest-rated part of the AI stack, and fewer than one in three teams are satisfied with their current tooling." (article-stated, source of underlying survey not disclosed in snippet).

## Grand View Research — AI Agents Market Report
- URL: https://www.grandviewresearch.com/industry-analysis/ai-agents-market-report ; https://www.grandviewresearch.com/press-release/global-ai-agents-market-report
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"Grand View Research projects the AI agents market to be $10.9 billion in 2026, up from $7.6 billion in 2025." "The global AI agents market size is expected to reach USD 182.97 billion by 2033, registering a CAGR of 49.6% from 2026 to 2033." Analyst-derived (Grand View Research, a paid market-research firm; methodology not disclosed in snippet).
"Key players operating in the AI agents market include Alibaba Group Holding Limited, Amazon Web Services, Inc., Apple Inc., Baidu, Google, IBM Corporation, Meta, Microsoft, NVIDIA Corporation, and Salesforce." — note: this is the broad "AI agents" market, not an "agent control plane / dashboard" sub-segment; no report found sizing the control-plane sub-segment specifically.

## MarketsAndMarkets / other orchestration market sizing (conflicting, side by side)
- URL: https://www.marketsandmarkets.com/Market-Reports/agentic-ai-market-208190735.html ; https://www.fortunebusinessinsights.com/ai-orchestration-market-107177 ; https://www.snsinsider.com/reports/ai-agent-orchestration-platform-market-10638 ; https://dimensionmarketresearch.com/report/ai-agent-orchestration-market/
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

Conflicting 2026 estimates, all analyst-derived, none averaged:
"AI orchestration market is projected to grow from USD 13.99 billion in 2026" (one report) "to USD 60.34 billion by 2034, exhibiting a CAGR of 20.05%."
"AI Agent Orchestration Market is valued at $11.0 Bn in 2026" (separate report).
"Agentic AI Workflow Orchestration Platform Market worth USD 3.53 billion in 2026" (Mordor Intelligence report, narrower definition).
"AI orchestration Market projected to reach $13.96 billion in 2026" (Fortune Business Insights — near-duplicate of MarketsandMarkets figure, different firm).
"Global agentic AI market estimated at USD 19.33 billion in 2026" (broadest-scope report).
"AI Agent Orchestration Platform Market expected to reach USD 107.34 Billion by 2035, growing at a CAGR of 22.67%" (SNS Insider).

## Decawork (YC S26) — the agent control plane for IT teams
- URL: https://www.ycombinator.com/companies/decawork ; https://lemstudio.co/yc-companies/decawork-33047
- Pulled: 2026-09-16
- Method: WebFetch + WebSearch

"Decawork gives IT teams one place to deploy, govern and maintain the AI agents running across their company." Founded 2026 by Sarthak Aggarwal and Aman Raj, 2 employees, based in Bengaluru, YC Summer 2026 batch.
Problem framing (company-stated): "Agent sprawl occurs when deployment gets messy, agents go live with access to real systems and real data, and maintenance falls in the gap. In April, Vercel was breached through an AI tool a single employee had connected with broad workspace permissions, and last month, researchers showed GitHub's own AI agent could leak private code."
Features: "Every agent ships one standard way - its own identity and scoped credentials, with IT's sign-off before it goes live. Every action is logged and attributed and IT is alerted when something fails. IT decides what it can access, reviews sensitive actions, sees what it did, and can pause or retire it from one place."
Also: "Standardized agent deployment with identity and scoped credentials; IT approval requirements before agents go live; Real-time monitoring and alerting for agent failures; Automated retirement of unused agents; Complete agent visibility and audit trails; Access controls and approval gates for sensitive operations."
No pricing or funding amount disclosed in sources checked.

## Omnara — open-source control plane for managed agents
- URL: https://github.com/omnara-ai/omnara
- Pulled: 2026-09-16
- Method: WebFetch

Tagline: "The open-source alternative to Claude Managed Agents." "Omnara is an open source platform for running managed agents." Stars: 2.9k. License: Apache-2.0.
Features: "Durable execution: Agent state is committed atomically to Postgres. Agents recover automatically from crashes, restarts, and temporary machine disconnects." "Flexible infrastructure: Support for multiple sandboxes (Blaxel, Daytona, Modal, Unikraft) and custom machines." "Model agnostic: Compatible with various model providers including OpenRouter, LiteLLM, and Ollama." "Access control: Role-based access management for organizations and projects." "Deployment options: Available as cloud service or self-hosted under open-source license." CLI, TypeScript SDK, REST API.
Investors listed (per startupintros.com aggregation, unverified primary): Andreessen Horowitz, Bain Capital Ventures, Better Tomorrow Ventures, Blackbird Ventures Australia, Conversion Capital, Daffy, Endure Capital, Fifth Wall, Founders Fund, General Catalyst, QED Investors, Ravelin Capital — note: this investor list looks unusually broad/generic for a 2.9k-star OSS repo and should be treated with caution pending a primary-source check (e.g. Crunchbase filing).

## Fiddler AI — Control Plane product page
- URL: https://www.fiddler.ai/control-plane
- Pulled: 2026-09-16
- Method: WebFetch

"Observe, enforce, govern every agent, from the creation layer to production." Target buyers: government/defense, financial services (lending, trading, fraud detection), healthcare (clinical), insurance (claims, underwriting, risk).
Approval/control: "Enforces policy where agents operate, blocking destructive commands, data leaks, and risky tool usage." Human approval for high-risk decisions; inline enforcement at request/response boundaries.
Cost: "Fleet-wide spend and adoption from individual agent to org-wide rollup." "Fiddler Centor Models to reduce evaluation costs by running guardrails in-environment rather than relying on external LLM API calls."
Observability: "Complete execution paths, from application to session to agent to span" with native OpenTelemetry support, real-time alerts, root-cause diagnostics, "100+ metrics for hallucination, toxicity, PII/PHI detection."
Pricing: not disclosed on page; contact sales.

## OpenAI — AgentKit / Agent Builder wind-down (Montana Labs analysis)
- URL: https://montanalabs.ai/news/openai-s-agentkit-and-the-eight-month-lifespan-of-agent-builder/
- Pulled: 2026-09-16
- Method: WebFetch

Timeline: "Launch: October 6, 2025." "Wind-down notice: June 3, 2026." "Sunset deadline: November 30, 2026." "Total lifespan: ~8 months."
Replacement paths: "Agents SDK – For workflows meant to run as code" and "Workspace Agents in ChatGPT – For natural-language prompting use cases."
Framing: visual-canvas Agent Builder and standalone Evals product are "being split between a code path and a ChatGPT-native path, with the middle-layer builder tools retired." Market read: "the durable layer was the code-level SDK, not the visual builder layered on top of it." "Companies standardizing on Agent Builder now face migration risk—they must rebuild against the Agents SDK before November 2026."

## Temporal — durable execution for AI agents
- URL: https://temporal.io/blog/temporal-agent-harness-durable-agent-infrastructure ; https://www.reactify-solutions.com/articles/durable-ai-agents-2026
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"Durable execution is the technique that lets an AI agent finish its task even if the process crashes, restarts or hits an API rate limit halfway through." "Temporal's new Agent Harness brings durable execution, tool-call approvals, and typed interfaces to production AI agents."
"The agents that shipped in 2024 ran for thirty seconds and lost their state when the laptop lid closed. The agents shipping in 2026 run for hours, pause for a human approval that lands the next morning, resume from a crash with the same tool-call history, and bill nothing while they wait. Replit's Agent 3, OpenAI's Codex web agent, and the long-running automation at Cursor all run on Temporal." "Since 2026 Temporal ships official integrations with the OpenAI and Vercel agent SDKs."

## OpenTelemetry GenAI semantic conventions — state as of mid-2026
- URL: https://john-hodge.com/blog/opentelemetry-genai-semantic-conventions/ ; https://greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"As of July 17, 2026, no GenAI-specific span, event, metric, or attribute in the dedicated repository is marked Stable; the GenAI conventions remain Development." "The conventions now model the whole agent execution as a span tree, not just single LLM calls, with invoke_agent covering the full agent lifecycle — create_agent, invoke_agent, invoke_workflow, execute_tool, retrieval, plan, plus memory operations." "The main semantic-conventions repository deprecated and moved all gen_ai content in v1.42.0 (June 2026)... The MCP conventions moved into the same GenAI repo with the v1.42.0 extraction." "The vocabulary is usable today and worth adopting, but it is a moving target, not a frozen contract... instrument against them, but expect churn, and pin the version you build on."

## Sandboxed tool execution cost — E2B / Modal / Daytona pricing
- URL: https://bex.co/blog/2026/09/09/e2b-daytona-modal-sandbox-pricing-self-hosted
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"E2B and Daytona charge $0.0504 per vCPU-hour plus $0.0162 per GiB-hour (billed per second), with a typical agent run of 2 vCPU, 4 GiB RAM, alive for ten minutes costing about $0.028. Modal appears approximately 3x more expensive on the rate sheet, landing around $0.040 for the same configuration." "E2B's ~$0.05/vCPU-hour pricing is competitive for moderate workloads, but at 200 concurrent sandboxes the monthly cost approaches $17K, substantially higher than multi-tenant alternatives." "Sandboxes for AI agents must be programmatically driven, ephemeral, and cost-attributable per task."

## Agentic identity / IAM for AI agents
- URL: https://www.pingidentity.com/en/resources/identity-fundamentals/agentic-ai.html ; https://www.barchart.com/story/news/36542803/sailpoint-signs-strategic-collaboration-agreement-with-aws-to-secure-agentic-ai-with-a-unified-identity-governance-layer
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippet)

"Agentic IAM is the framework of policies, technologies, and controls used to manage AI agents as distinct, governed non-human identities (NHIs) within an organization." "Every stage of an agent's lifecycle needs purpose-built identity governance, from OIDC authentication and OAuth subject-actor trust binding to MCP-based resource discovery, just-in-time provisioning, and layered policy evaluation." "Human-in-the-loop isn't optional for high-risk actions, as sensitive operations trigger step-up authentication, liveness validation, and active human approval." "SailPoint and AWS announced a strategic collaboration agreement in March 2026 establishing SailPoint as a preferred identity governance solution for agentic AI."

## Harvard Business Review — "AI Agent Manager" role (via secondary summary)
- URL: https://blog.theinterviewguys.com/what-an-ai-agent-manager-actually-does/
- Pulled: 2026-09-16
- Method: WebFetch

"The role was formally defined by Harvard Business Review in February 2026 in an article by Suraj Srinivasan (Harvard Business School) and Vivienne Wei (Salesforce)." Duties: "defining tasks for AI agents, reviewing outputs, handling exceptions, optimizing workflows, and ensuring quality standards." Companies cited with this role: Salesforce, ServiceNow. Salary (source: this secondary article, no primary comp survey named): "Average: $103,178 annually. Range: $55,000–$194,000." Quote attributed to "One Salesforce agent manager": "I start and end my day in dashboards." "Over 70% of new AI deployments in 2026 focus on action-based agents performing concrete tasks rather than answering questions, driving demand for this oversight role." Tools cited: "Salesforce Agentforce, Microsoft Copilot, and workflow automation platforms."

## thecrunch.io — AI Agent Dashboard & Platforms 2026 Comparison Guide
- URL: https://thecrunch.io/ai-agent-dashboard/
- Pulled: 2026-09-16
- Method: WebFetch

10-platform comparison table (article-stated pricing, verify independently): LangSmith ($39/user/mo, LangChain-native), Langfuse ($59/mo, self-hostable OSS), Helicone ($20/mo, low-friction proxy), Arize Phoenix (free OSS, notebook-first eval), Braintrust ($249/mo, eval-driven dev), Portkey ($49/mo, AI gateway/multi-provider control), AgentOps ($40/mo, agent-specific monitoring for CrewAI/AutoGen/LangGraph), Galileo (custom, regulated-industry eval), Humanloop ($750/mo, non-engineer prompt collaboration), n8n ($20/mo cloud, visual orchestration).
Weaknesses noted: "LangSmith: ... limited framework flexibility." "Langfuse: ... smaller ecosystem than LangSmith." "Helicone: Minimal integration friction; basic feature set compared to specialized platforms." "Portkey: Multi-model support; primarily gateway-focused rather than deep observability." "AgentOps: Agent-specific; less suitable for non-agentic LLM applications."

## Funding/pricing aggregation — LangGraph Platform, CrewAI, Arize, Langfuse/ClickHouse, Helicone/Mintlify, n8n, Lindy
- URL: https://www.truefoundry.com/blog/langgraph-pricing ; https://checkthat.ai/brands/crewai/pricing ; https://pitchbook.com/profiles/company/432489-61 (Arize) ; https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability ; https://www.mintlify.com/blog/mintlify-acquires-helicone ; https://tech.eu/2026/05/12/n8n-s-valuation-doubles-to-5-2bn-following-sap-strategic-investment/ ; https://www.clay.com/dossier/lindy-funding
- Pulled: 2026-09-16
- Method: WebSearch (aggregated snippets)

LangGraph Platform: "free Developer tier, a Plus tier at $39 per user per month (requires LangSmith Plus subscription), and custom-priced Enterprise tier... 100,000 node executions included, with node executions beyond quota costing $0.001 each. Uptime billed at $0.0007/min (Dev) and $0.0036/min (Production)." "LangGraph's monthly cost spans roughly $1 for a local hobby setup to about $3,515 for a high-volume, dedicated-deployment workload at Plus-tier list rates, as of September 2026."
CrewAI: "Enterprise tier features custom pricing, with estimates around $60,000-$120,000 annually." "$18M funding round" (amount undated in snippet). Adoption claim (company-stated, May 2026 disclosure): "most of Fortune 500 companies use CrewAI, up from roughly half of the Fortune 500 during the 2024 enterprise beta." PyPI installs: "CrewAI receives approximately 1.3 million monthly PyPI installs versus AG2's 100,000."
Arize: funding "$131M over 4 rounds," latest "$70M on Feb 20, 2025," "Series D Valuation of $741.84M as of Apr 2026." Headcount: "209" (Jun 30 2026) vs "growing 24% QoQ, from 178 to 221 employees" (Jul 24 2026) — two different snapshots, both Tracxn/PitchBook-sourced, not primary.
Langfuse/ClickHouse: "ClickHouse announced on January 16, 2026, its acquisition of Langfuse." "Langfuse, founded in 2023, was a leading open-source platform for LLM observability, evaluations, and prompt management with more than 2,000 paying customers and is trusted by 19 of the Fortune 50 and 63 of the Fortune 500 companies" (company-stated). ClickHouse itself raised "$400 million" Series D "valued ClickHouse at $15 billion." "Langfuse's roadmap remains focused on building the best LLM engineering platform with continued commitment to open source and self-hosting."
Helicone/Mintlify: "On March 3, 2026, Helicone announced it was joining Mintlify." "By the time of its acquisition in early 2026, Helicone had grown to serve more than 16,000 organizations, track over 33 million end users, and process over 14.2 trillion tokens across its three years of operation" (company-stated). Post-acquisition: "active feature development has ended — only security patches, bug fixes, and new model support will continue."
n8n: "n8n is valued at $5.2 billion as of May 12, 2026, more than double the $2.5 billion mark n8n carried after its $180 million Series C just seven months earlier, in October 2025," following "a strategic investment from German software giant SAP." "n8n has raised $254M in funding from investors like Accel, Sequoia Capital and Felicis Ventures." (One source, valueaddvc.com, additionally claims "$40M ARR" — company/analyst-stated, unverified primary.)
Zapier Agents reliability complaint: "Trustpilot score of 1.4 out of 5 from hundreds of reviewers, complaints center on surprise billing, task overages, and inconsistent Zap execution (duplicate records, missed triggers, runaway loops)."
Lindy: "Lindy has raised $53.6M, with its largest being a $35 million Series B round in January 2023." Valuation "$288M" is an UpMarket third-party estimate, not company-disclosed.
