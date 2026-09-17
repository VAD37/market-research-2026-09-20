# Two-founder AI companies — raw pulls

Pulled 2026-09-16. Question: named AI companies founded by exactly two people — who they were, prior background, what they built, what it earned. Channel notes: this session's WebSearch budget was exhausted after ~4 calls (see Block 0); everything after that is WebFetch against guessed-but-likely URLs (Wikipedia articles, Wikipedia's own `Special:Search`, company About/blog pages, and Sacra profiles). WebFetch itself is a summarizing layer, not a raw-HTML dump — where the tool returned text already inside quotation marks, that is verbatim from the source page; unquoted lines are the fetch tool's own paraphrase of the page, flagged as such below. No number here was guessed; every "unknown" is an explicit checked-and-not-found.

---

## Block 0 — WebSearch quota exhausted
- Channel: WebSearch
- Date: 2026-09-16
- Queries attempted: "Harvey AI legal startup founders Winston Weinberg Gabriel Pereyra background OpenAI lawyer"; "two-founder AI startup shut down 2024 2025 acquihire co-founder failed"

Tool response, verbatim: "Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls). Continue with the information already gathered instead of issuing more searches. If more searches are genuinely needed, ask the user to raise CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION."

All subsequent pulls are WebFetch only. Bing HTML search and DuckDuckGo HTML/lite search were tried as substitutes and both returned HTTP 403 (bot-blocked) — recorded, not guessed around.

---

# SECTION A — Two-founder AI-era cases (founded 2022-01-01 or later)

## Block 1 — Harvey (legal AI) — tech/non-technical split
- URL: https://en.wikipedia.org/wiki/Harvey_(software)
- Date: 2026-09-16
- Channel: WebFetch

Founded: summer 2022. Founders per article: "Winston Weinberg (CEO): Securities and antitrust litigator at O'Melveny & Myers" and "Gabriel Pereyra (President): Research scientist at Google DeepMind and Meta." Sells: "Customized large language models for law firms and in-house legal teams" — document analysis, due diligence, litigation support, regulatory compliance. This is a clean lawyer/researcher split (one legal-domain, one ML-research) — the "one builds, one sells" pattern, though Pereyra's title (President) is not purely technical and Weinberg's title (CEO) is not purely sales; division-of-labor quote not located this session.

Funding/valuation timeline (all vendor-reported/trade-press per Wikipedia, quoted): "$5 million in funding led by the OpenAI Startup Fund" (November 2022); "$23 million" Series A, Sequoia-led (April 2023); "$80 million in a Series B funding round...valued the company at $715 million" (December 2023); "$100 million in a Series C funding round that valued the company at $1.5 billion" (July 2024); "$300 million in a Series D funding round...valued the company at $3 billion" (February 2025); "$300 million Series E...boosting its valuation to about $5 billion" (June 2025); "$160 million Series F...valuing the legal AI company at roughly $8 billion" (December 2025); "$200 million...at a valuation of $11 billion" (March 2026); "$550 million...at a valuation of $15.5 billion" (September 2026).

Revenue: "$190 million" (2025) — analyst-derived/trade-press per Wikipedia, no primary filing cited.

Headcount: "82 employees" (March 2024), company "stated that it intended to double that figure by the end of 2024."

Time to first paying customer / time to $1M ARR: unknown — checked https://en.wikipedia.org/wiki/Harvey_(software) 2026-09-16, not stated. Attempted https://harvey.ai/about and https://harvey.ai/blog — the /about URL 404'd; /blog returned only a funding-announcement banner ("We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence") with no founder bios or ARR detail.

---

## Block 2 — ElevenLabs (voice AI) — two technical, different specialties
- URL: https://en.wikipedia.org/wiki/ElevenLabs
- Date: 2026-09-16
- Channel: WebFetch

Founded 2022. Founders: "Piotr Dąbkowski (CTO): Ex-Google machine learning engineer, raised in Poland" and "Mati Staniszewski (CEO): Ex-Palantir deployment strategist, raised in Poland." Both technical/product backgrounds rather than a clean technical/sales split — flagged as two-technical (Staniszewski's Palantir "deployment strategist" role is the closer-to-commercial side, but is not a sales/BD title). Sells: "natural-sounding speech synthesis software using deep learning" — TTS, voice cloning, AI dubbing, music generation, conversational AI agents.

Funding/valuation, quoted: "$2 million pre-seed round" (January 2023); "$19 million Series A funding round at a valuation of about $100 million" (June 2023); "$80 million in Series B funding raising the total valuation of the company to $1.1 billion" (January 22, 2024); "$180 million Series C funding raising the total valuation of the company to $3.3 billion" (January 30, 2025); employee tender offer at "$6.6 billion valuation" (September 2025); "$500 million at an $11 billion valuation" (February 4, 2026).

Headcount: "400 (2026)." Revenue/ARR: not disclosed in this article — unknown, checked 2026-09-16.

---

## Block 3 — Decagon (customer-service AI agents) — two technical-adjacent
- URL: https://decagon.ai/about (WebFetch) and https://sacra.com/c/decagon/ (WebFetch)
- Date: 2026-09-16
- Channel: WebFetch

decagon.ai/about names "Jesse Zhang - Co-founder & CEO" and "Ashwin Sreenivas - Co-founder & President"; no individual bios on that page. Sacra's profile (analyst-derived) adds combined background: "Combined experience from Google, Citadel Securities, Palantir, and their previous startups Lowkey and Helia" — not attributed to which founder did what, so the technical/non-technical split cannot be confirmed from what was pulled. Founded August 2023 per Sacra.

Sacra-reported metrics (analyst-derived, not company-filed): revenue "$100M annualized" (July 2026); ARR "$44M" (end of 2025), growing "340%" year-over-year in 2025, "Q3 2025 GAAP revenue and ARR each grew more than 3x year over year"; valuation "$4.5B" (January 2026) on a "$250M" Series D (January 2026); prior rounds: Series C "$131M" (June 2025), Series B "$65M" (October 2024), Series A "$35M" (July 2024); total raised "~$481M." decagon.ai/about also states "10M+" customers served, "80% deflection rate," "93% agent quality score," and names customers Avis Budget Group, Chime, Oura Health, 1-800-FLOWERS.COM, Hunter Douglas.

Caveat: Sacra is a third-party research firm (analyst-derived), not a primary filing; Decagon is private and does not publish audited financials.

---

## Block 4 — Clay (GTM/sales data platform)
- URL: https://www.clay.com/about, https://www.clay.com (WebFetch) and https://sacra.com/c/clay/ (WebFetch)
- Date: 2026-09-16
- Channel: WebFetch

Only one founder name surfaced across all pulls this session: "Co-founder Kareem Amin is mentioned in a Sequoia Capital podcast title" (clay.com/about fetch) and Sacra lists him as current CEO. Second co-founder's name: unknown — checked https://www.clay.com/about, https://www.clay.com, https://sacra.com/c/clay/ 2026-09-16, not disclosed on any of the three pages fetched. Founding date per clay.com/about: "Clay began in Brooklyn in 2017" building "a spreadsheet that let anyone connect information and automate work without writing code," later repositioned to go-to-market/sales use. Sacra gives a conflicting founding-date note: "Founded: 2019 (note: one section states 'Founded in 2019' regarding pre-seed fundraising, creating a discrepancy in the source material)" — both dates recorded side by side, not resolved.

Sacra-reported (analyst-derived) financials: ARR "$150M" (May 2026), up from "$108M" (end of 2025); revenue growth "260% year-over-year" (2025); valuation "$5 billion" via January 2026 employee tender (DST-led) vs. "$3.1 billion post-money valuation" Series C (August 2025, CapitalG-led) — both figures kept side by side, not averaged. Prior funding: Series B "$46 million" (June 2024) plus a "$40 million" Series B expansion (2024); Series A "$13.5 million" (2023, Sequoia-led); seed "$2.5 million" (2021, First Round Capital-led). Total primary equity raised "at least $202 million." clay.com's own homepage adds "Trusted by more than 500,000 leading GTM teams" and a January 28, 2026 NYT-sourced line: "Clay allows employees to sell shares at a $5b valuation."

---

## Block 5 — Sierra (enterprise AI agents) — two-technical/product veterans, no financials disclosed
- URL: https://sierra.ai/about
- Date: 2026-09-16
- Channel: WebFetch

Founders: Bret Taylor and Clay Bavor, described as having "met at Google." Bret Taylor's listed background: "Co-CEO of Salesforce (most recent role before founding)... Founder of Quip... CTO of Facebook... Co-creator of Google Maps at Google... OpenAI board member." Clay Bavor's: "18 years at Google... Led Google Labs (most recent role)... Started and led Google's AR/VR effort (Project Starline)... Led Google Lens development... Led product and design teams for Google Workspace." Both are product/business/technical hybrids rather than a clean builder/seller split — flagged as two-technical-executive, not technical/non-technical.

Founding-story quote from the page: "With decades of experience shaping groundbreaking innovations for the world's top tech companies, they set out to redefine what AI assistance can be." What it sells: AI-powered customer-experience agents; named customer case studies CLEAR, Casper, Minted.

Financials: unknown — checked https://sierra.ai/about 2026-09-16. Page states: "No financial metrics disclosed... the page contains no information about revenue, ARR, funding, valuation, or customer count."

---

## Block 6 — Photoroom (AI photo/product-image editing) — product/technical split
- URL: https://www.photoroom.com/about and YC page https://www.ycombinator.com/companies/photoroom
- Date: 2026-09-16
- Channel: WebFetch

Founded 2019, YC batch Summer 2020. Founders: "Matt Rouif (CEO, Co-founder)" and "Eliot Andres (Co-founder)." Rouif's background (YC page, company-stated): "Polytechnique & Stanford graduate," built ski-resort apps ("50+ resorts globally"), co-founded HeyCrowd (social survey app), led product for the Replay video editor which "Apple awarded 'best app' of the year," then GoPro acquired Replay and Rouif "oversaw all image editing products" there before starting Photoroom. Andres's background: "three years of computer vision and deep learning expertise, plus prior mobile app development experience across five different applications." This is a genuine product/business (Rouif) vs. computer-vision-technical (Andres) split, though both have engineering-adjacent histories.

Founding-story quote (company-stated): "With the designer out of office, he spent hours manually tracing edges with a lasso tool. By the time he finished, one thing was clear: there had to be a better way."

Metrics: "40 million app downloads" (by November 2022); "$19 million funding raise" (November 2022); "$500 million valuation" (February 2024); "7 billion images" processed per year, "1 million brands" using the product, "#1 mobile app across 40+ countries," "1M+ businesses" selling with it (current, undated on the fetched page). Revenue/ARR: unknown — checked https://www.photoroom.com/about 2026-09-16, not disclosed.

---

## Block 7 — Wordware (AI-agent-building IDE) — two technical, both ex-AI-startup exits
- URL: https://www.ycombinator.com/companies/wordware
- Date: 2026-09-16
- Channel: WebFetch

Founders: "Filip Kozera (CEO/Cofounder): Previously cofounded KRISTALIC (acquired), studied Deep Learning at Cambridge" and "Robert Chandler (CTO/Cofounder): Early engineer at Five AI (acquired by Bosch), led Offline Perception team, 10+ years in AI, studied Information Engineering at Cambridge." Both are technical founders with prior AI-company exits — flagged explicitly as two-technical, not a builder/seller split.

Division-of-labor / origin quote (Kozera, company-stated on YC page): "I met Robert (my CTO) at the University of Cambridge. We have both worked with LLMs since BERT and created well-performing stacks before AI Ops was a term. We both have exits in the field."

Funding: "$30 million seed round," described on the page as "the largest in YC history," backed by Spark Capital, Felicis, and Y Combinator. Batch: Summer 2024. Traction: "In production with 7 YC Companies" (as of the November 2024 launch announcement quoted on the page). Team size: "~20 people," San Francisco. Revenue/ARR: unknown — checked https://www.ycombinator.com/companies/wordware 2026-09-16, not disclosed.

---

## Block 8 — Lovable (AI app-builder / "vibe coding") — two founders confirmed, backgrounds not found
- URL: https://en.wikipedia.org/wiki/Lovable_(company)
- Date: 2026-09-16
- Channel: WebFetch

Founded 2023, Stockholm, Sweden. Founders (2, per article): "Anton Osika" and "Fabian Hedin." Backgrounds: unknown — checked https://en.wikipedia.org/wiki/Lovable_(company) 2026-09-16; the article states no biographical detail on either founder. (Caution for the compiler: some press coverage names a third Lovable co-founder; this Wikipedia pull only supports two. Recheck before treating "two founders" as settled.)

Sells: "a Swedish vibe coding platform" — "software that allows users to enter prompts to automate software development."

Funding/ARR/valuation, quoted: "$200 million Series A led by Accel" at "$1.8 billion valuation" (February 2025); ARR "reached $200 million" (November 2025); "$330 million in a Series B funding round" at "$6.6 billion valuation" (December 2025); "$400 million Series C round" at "$13.3 billion valuation" (August 2026).

Time to $1M ARR / first paying customer: unknown — checked same URL, not stated.

---

## Block 9 — Character.AI — two-technical founders, "acquihire" back into Google (borderline failure, see also Section C)
- URL: https://en.wikipedia.org/wiki/Character.AI and https://sacra.com/c/character-ai/
- Date: 2026-09-16
- Channel: WebFetch

Founded November 2021 by "Noam Shazeer and Daniel de Freitas, both former Google engineers." Per Wikipedia: "Shazeer was a lead author on 'Attention Is All You Need,' described as foundational to modern chatbots. De Freitas led design of Google's experimental AI initially called Meena, which became LaMDA." Both are research-technical — flagged as two-technical, not a builder/seller split.

Sells: generative-AI chatbot service — users converse with customizable characters. Beta launch: September 16, 2022.

Funding/valuation: "$43 million in seed funding at the time of its initial foundation in 2021"; Series B "$150 million" (March 2023) at which point "Character.ai became valued at approximately $1 billion." Sacra (analyst-derived) adds later figures: revenue "$30.00M" (2025 annualized), projected "$50 million at the end of 2025"; funding total "$193.00M" (2023).

August 2024 Google deal: Wikipedia states "Google hired Noam Shazeer, the CEO of Character.ai, and entered into a non-exclusive agreement to use Character.ai's technology" but "does not disclose a purchase price." Sacra likewise: "no transaction price is disclosed," only that the departure "eliminated the company's primary AI expertise" and intensified competitive pressure from Google's own Gemini integration. Deal price: unknown — checked both sources 2026-09-16, not disclosed in either (public reporting elsewhere widely cites a ~$2.7 billion licensing figure, but that number was not confirmed by either source fetched this session, so it is NOT recorded as a fact here).

Current CEO per Sacra: Karandeep Anand (i.e., neither original founder still runs the company day-to-day).

---

## Block 10 — Granola (AI meeting notes) — one founder confirmed, second unknown
- URL: https://www.granola.ai and https://sacra.com/c/granola/
- Date: 2026-09-16
- Channel: WebFetch

CEO confirmed: "Chris Pedregal." Second co-founder's name and both founders' backgrounds: unknown — checked https://www.granola.ai, https://sacra.com/c/granola/, and https://www.granola.ai/blog/granola-raises-seed (404) 2026-09-16; none disclosed a second name. Founded 2023, London, UK, per Sacra.

Sells: desktop AI meeting-notes app; distinguishing feature (company-stated): "works differently from competitors like Otter.ai and Fireflies.ai" by "running locally on Mac rather than joining meetings as a bot," letting users "enhance their own notes with AI post-meeting." Pricing (company-stated): "$18/user/month for individuals, a deliberately lower $14/user/month for business users...and $35/user/month for enterprises," with access after 25 free meetings. Customer logos shown: PostHog, Intercom, Figma, Brex, Ramp, Replit, Lovable, Cursor, Bumble, Asana, Vanta, Linear.

Funding (Sacra, analyst-derived): "Total: $24.20M across 25 rounds"; specific round dates/amounts not itemized on the page fetched. Revenue/ARR/valuation: unknown — checked same URLs 2026-09-16, not disclosed. A March 2026 TechCrunch headline is cited secondhand inside a Wikipedia "List of unicorn startup companies" search snippet: "Granola raises $125M, hits $1.5B valuation as it expands from meeting notetaker to enterprise AI app" (Mehta, Ivan, TechCrunch, 2026-03-25) — recorded as trade-press, not independently fetched/confirmed from TechCrunch itself this session.

---

## Block 11 — Cal AI (calorie-tracking app) — could not confirm founder count or names
- URL: https://www.calai.app
- Date: 2026-09-16
- Channel: WebFetch

Attempted to verify the widely-discussed "teenage two-founder" story for this app (reportedly Zach Yadegari and a co-founder). Result: unknown — checked https://www.calai.app 2026-09-16; fetch tool reported "no information available regarding founders' names or backgrounds, whether founders were teenagers or attended high school, company founding date, or revenue/ARR/funding figures with dates." Also checked https://sacra.com/c/cal-ai/ (404) and Wikipedia (no article exists for "Cal AI"). This entry is included specifically to document a negative/unconfirmed result, per instructions not to guess. Do not compile founder names for Cal AI from memory — recheck via a source with WebSearch budget before using this case.

---

## Block 12 — Cluely (AI "undetectable" meeting/exam assistant) — founder claims not verified this session
- URL: https://cluely.com
- Date: 2026-09-16
- Channel: WebFetch

The brief named Roy Lee and Neel Shanmugam (Columbia) as Cluely's founders as a hypothesis to verify. Result: not verified. The fetched homepage content contains product description only: "takes perfect meeting notes and gives real-time answers, all while completely undetectable," "12+ Languages," "300ms Response time," "95% Transcription accuracy," works with Zoom/Slack/Webex/Teams/Google Meet. Fetch tool explicitly noted: "the webpage does not contain any information about the company's founding story, founder names..., or their educational backgrounds." No revenue/ARR/funding disclosed on the page. unknown — checked https://cluely.com 2026-09-16 for both founder identity and financials. Flag for the compiler: do not assert Roy Lee/Neel Shanmugam as confirmed founders based on this raw file; that needs a source this session did not reach (WebSearch was exhausted before this could be chased down).

---

## Block 13 — Legora (AI for lawyers) — thin pull, no founders, no financials
- URL: https://www.legora.com/about
- Date: 2026-09-16
- Channel: WebFetch

Page discloses no founder names or backgrounds, and no financial metrics: "the page contains no information regarding revenue, ARR, funding amounts, or valuation." Customer-count claims (company-stated): "375+ coworkers, 1480+ customers, 30+ markets" (figures as labeled on the page, ambiguous whether "coworkers" means Legora's own headcount or a customer-side figure — recorded as-is, not resolved). One investor quote (General Catalyst's Jeannette zu Fürstenberg) calling it "redefining how legal work gets done," labeled as investor commentary, not company data. unknown — checked https://www.legora.com/about 2026-09-16 for founders/financials.

---

# SECTION B — Verified NOT two-founder (checked because the brief said "verify, do not assume")

## Block 14 — Cursor / Anysphere — FOUR founders, not two
- URL: https://en.wikipedia.org/wiki/Cursor_(code_editor) (fetched twice under two titles, same content)
- Date: 2026-09-16
- Channel: WebFetch

"The company was incorporated in 2022 by Michael Truell, Sualeh Asif, Arvid Lunnemark and Aman Sanger while they were students at Massachusetts Institute of Technology (MIT)." Four founders — excluded from the two-founder set, kept here as a named check.

Financials (context, since this is a widely-cited case): seed "$8 million," OpenAI Startup Fund-led (October 2023); ARR crossed "$100 million" (January 2025), "$500 million ARR" (June 2025); Series C "$900 million" at "$9.9 billion" post-money valuation (June 2025); Series D "$2.3 billion" at "$29.3 billion" valuation (November 2025); "exceeded $1 billion" annualized revenue / "$3 billion ARR" (May 2026); acquired by SpaceX at "$60 billion" valuation (August 2026, completed).

---

## Block 15 — Midjourney — ONE founder, not two
- URL: https://en.wikipedia.org/wiki/Midjourney
- Date: 2026-09-16
- Channel: WebFetch

"The Midjourney team is led by David Holz, who co-founded Leap Motion." Article names no second founder. Open beta launch: July 12, 2022. Holz "told The Register in August 2022 that the company was already profitable" — no revenue figure attached. Company description: "an independent research lab" ("Midjourney, Inc."). Headcount/valuation/funding: unknown — checked same URL 2026-09-16, not disclosed in the article.

---

## Block 16 — Inflection AI — THREE founders, not two; $650M Microsoft "acquihire," pre-2022-era company but instructive
- URL: https://en.wikipedia.org/wiki/Inflection_AI
- Date: 2026-09-16
- Channel: WebFetch

Founded 2022 by "Reid Hoffman" (LinkedIn co-founder), "Mustafa Suleyman" (DeepMind co-founder), and "Karén Simonyan." Three founders. Raised "US$1.3 billion at $4 billion valuation" (June 2023). March 2024: Suleyman and Simonyan departed for Microsoft AI; Microsoft "acqui-hire of nearly the entire 70-person workforce"; Microsoft paid "Inflection $650 million to license its technology," and "the proceeds were used to reimburse Inflection AI's investors." UK Competition and Markets Authority "concluded that the deal amounted to a 'merger situation,' but did not pose a threat to competition." Not a two-founder case, but recorded because it is a close structural cousin of the Character.AI pattern (talent+license deal, not asset sale, after a founder split from the company).

---

# SECTION C — Two-founder AI companies that failed / shut down / sold cheap

## Block 17 — Humane Inc. — two ex-Apple founders, sold to HP for roughly half of funds raised
- URL: https://en.wikipedia.org/wiki/Humane_(company) [note: actual working title was Humane_Inc.]
- Date: 2026-09-16
- Channel: WebFetch

Founded 2018. Founders: "Imran Chaudhri" and "Bethany Bongiorno," both "Former Apple Inc. employee." (Publicly the two are also known as a married couple, both ex-Apple designers; that specific relationship detail was not itself re-confirmed by this Wikipedia pull, so it is noted here only as background color, not as sourced fact.)

Funding: "By November 2023, the company had raised $230 million." Product: the AI Pin, announced November 9, 2023 at $699, began shipping April 2024, price cut to $499 by October 2024. HP acquisition: February 2025, for "$116 million." Deal scope: "the majority of Humane's employees, software platform, and intellectual property, including the AI Pin's CosmOS operating system and over 300 patents and patent applications, but excludes the AI Pin device business itself." Service discontinued February 28, 2025: "existing devices would no longer connect to the company's servers." Net: $116M sale price against $230M+ raised — sold for roughly half of disclosed funding, and the flagship hardware product itself was killed outright.

---

## Block 18 — Neeva — two ex-Google ad executives, shut down and sold to Snowflake below "success" but above raised capital
- URL: https://en.wikipedia.org/wiki/Neeva
- Date: 2026-09-16
- Channel: WebFetch

Founded 2019. Founders: "Sridhar Ramaswamy (former Google executive)" and "Vivek Raghunathan." Prior funding: "Neeva had raised $77.5m from investors." May 2023: "Snowflake announced the acquisition of Neeva for $185.4 million in cash." Product shut down June 2, 2023. Reason given by the co-founders (company-stated, quoted): "the main reason for that decision was how hard it was to persuade normal users to make the switch." They committed to compensating users for unused account balances. Post-acquisition, "Sridhar Ramaswamy became CEO of Snowflake," described as being "to accelerate the search in the Cloud through Artificial Intelligence." Note for the compiler: the acquisition price ($185.4M) is higher than funds raised ($77.5M) on paper, but the underlying consumer-search product was shut down entirely — a product failure wrapped inside a financially "successful" acquisition; do not read this as a clean win.

---

## Block 19 — Argo AI — two ex-Google/Uber ATG technical founders, shut down by Ford/VW after $7.25B valuation
- URL: https://en.wikipedia.org/wiki/Argo_AI
- Date: 2026-09-16
- Channel: WebFetch

Founded November 2016. Founders: "Bryan Salesky (CEO) – Previously director of hardware development for Google's autonomous vehicle initiative (2013-2016); earlier worked at Carnegie Mellon's National Robotics Engineering Center" and "Peter Rander (President) – Previously engineering lead for Uber's Advanced Technology Group (2015-2016); also worked at Carnegie Mellon's National Robotics Engineering Center." Both technical/engineering backgrounds — flagged two-technical, not a builder/seller split.

"In June 2020, Argo was valued at $7.25 billion." Shutdown announced by Ford, October 2022, after "significant losses." Ford "assumed a $2.7 billion accounting charge and wrote off a cash investment of about $500 million for Argo AI"; "Volkswagen expensed €1.9 billion." Reason: failure to secure additional investment from Amazon and a strategic pivot; Ford CEO Jim Farley: "profitable, fully autonomous vehicles at scale are a long way off." Resources folded into Ford's Latitude AI and VW's CARIAD. Pre-2022 founding (2016) — included as an older, instructive analog for the failure set since it is a clean two-founder, both-technical AI company with fully disclosed collapse numbers.

---

## Block 20 (context, NOT two-founder) — Element AI and Builder.ai, checked and excluded from the failure set
- URL: https://en.wikipedia.org/wiki/Element_AI ; https://en.wikipedia.org/wiki/Builder.ai
- Date: 2026-09-16
- Channel: WebFetch

Element AI: founding group per article included "Jean-François Gagné," "Yoshua Bengio," "Nicolas Chapados, Anne Martel, Philippe Beaudoin, Jean-Sébastien Cournoyer" — five-plus founders, not two. Sold to ServiceNow November 30, 2020 for "US $230 million," described in the article as: "the company was running out of money and options and sold for US $230 million." Prior funding: "US$102 million" Series A (mid-2017) plus a "CAD$5 million" Canadian government loan (December 2018). Excluded from the two-founder failure list but kept as a comparison point on cheap-sale mechanics.

Builder.ai: article states "One confirmed founder (Duggal)" — Sachin Dev Duggal; a listed second name, Saurabh Dhoot, is explicitly disclaimed: "he was not involved in its founding." Not a two-founder company. Collapse detail kept for context: Bloomberg (May 2025) "accused the firm of using round-tripping to artificially boost revenue figures between 2021-2024," having "sometimes inflated sales figures by more than 20%"; funding raised included "$29.5 million" Series A (2018) and "$230 million" (2023, backers included Microsoft, Insight Partners, SoftBank, Qatar Investment Authority); bankruptcy proceedings announced May 20, 2025; creditors "seized $50 million borrowed in October 2024"; by June 2025 the company "had laid off 80% of its workforce, or around 1,000 people." Earlier fraud precedent noted in the same article: "August 2019: The Wall Street Journal reported that Engineer.ai" (Builder.ai's earlier name) "used human engineers rather than AI for most of its coding work."

---

# SECTION D — Older (pre-AI-era) two-founder analogs, for contrast

## Block 21 — WhatsApp — two-founder, technical/ops split, $19B acquisition (2014)
- URL: https://en.wikipedia.org/wiki/WhatsApp
- Date: 2026-09-16
- Channel: WebFetch

Founded May 3, 2009. Founders: "Jan Koum" and "Brian Acton," both "Former Yahoo employee." February 19, 2014: "Facebook, Inc. agreed to acquire the company for US$19 billion" — "Facebook paid $4 billion in cash, $12 billion in Facebook shares, and an additional $3 billion in restricted stock units granted to WhatsApp's founders." Described in the article as "its largest acquisition to date" and "the largest acquisition of a venture-capital-backed company in history" at that time. Not an AI company at founding, included per the brief's instruction to allow 2-3 older instructive analogs of the two-founder pattern.

---

## Block 22 — Mailchimp — commonly described as "two founders," Wikipedia names a third
- URL: https://en.wikipedia.org/wiki/Mailchimp
- Date: 2026-09-16
- Channel: WebFetch

Founded 2001. Article: "Ben Chestnut and Dan Kurzius (Mark Armstrong also co-founded)" — three names given, though press coverage generally credits Chestnut and Kurzius as the two who ran it long-term (Armstrong's exit not detailed in this pull). Founders' prior-employer/education background: unknown — checked same URL 2026-09-16, "the Wikipedia article provides no background information."

Revenue: "$700 million (2019)." Acquired by Intuit, completed November 1, 2021, for "approximately $5.7 billion in cash, 10.1 million shares of Purchaser common stock...with a fair value of approximately $6.3 billion." Growth data: after introducing freemium in 2009, "its user base had grown from 85,000 to 450,000" within a year; "By June 2014, it was sending over 10 billion emails per month"; at acquisition, "more than 13 million users globally, including approximately 2.4 million monthly active users." Flagged for the compiler: this is the cleanest large-number bootstrapped case found this session, but the "exactly two founders" claim is only as solid as ignoring Armstrong — do not present it as unambiguous.

---

## Block 23 — DataRobot (2012) — attempted, could not confirm founders this session
- URL: https://www.datarobot.com/about-us/ ; Wikipedia article does not exist under this or related titles
- Date: 2026-09-16
- Channel: WebFetch

Sought as a pre-AI-era, two-technical-founder analog (publicly known, outside this session, as Jeremy Achin and Tom de Godoy). Result: the About page states only "Founded in 2012, DataRobot has spent more than a decade at the frontier of applied AI" and names current CEO Debanjan Saha; "the webpage does not mention Jeremy Achin or Tom de Godoy by name, nor does it provide details about the founders' backgrounds." Wikipedia searches for "DataRobot" and "DataRobot Jeremy Achin" both returned "There were no results matching the query." unknown — checked https://www.datarobot.com/about-us/ 2026-09-16 and Wikipedia search 2026-09-16; do not compile founder names for DataRobot from memory on the strength of this file.

---

# SECTION E — Founder-count outcome data (methodology + sample size for each figure)

## Block 24 — Noam Wasserman, "The Founder's Dilemmas" — sample size only, no team-size breakdown recovered
- URL: https://en.wikipedia.org/wiki/Noam_T._Wasserman ; https://hbr.org/2008/02/the-founders-dilemma
- Date: 2026-09-16
- Channel: WebFetch

Wasserman bio page: his book draws on a dataset of "10,000 founders from 3,500 start-ups" (peer-reviewed/academic-derived, exact stat quoted). The Wikipedia bio page explicitly does not carry the solo-vs-2-vs-3+ breakdown: "the Wikipedia article does not contain specific data regarding: Solo founder versus co-founder outcomes; Equity split patterns; Success or failure rates by team structure."

The original 2008 Harvard Business Review article ("The Founder's Dilemma") is paywalled past the abstract; the visible portion states the underlying study covered "212 American start-ups that sprang up in the late 1990s and early 2000s" and that "most founders surrendered" control at some point (sentence cut off by paywall). Methodology detail beyond that: unknown — checked https://hbr.org/2008/02/the-founders-dilemma 2026-09-16, "the specific statistics you requested are not present in the extracted content... behind a subscription paywall."

A related Wikipedia page, "Organizational founder," was checked for a team-size stat and returned none — only a generic list of failure factors: "trouble in funding, sudden market shutdown, not having the right team or poor scaling plan" (no numbers attached).

---

## Block 25 — CB Insights, startup failure-reasons report — has a sample size, but no founder-team-size cut
- URL: https://www.cbinsights.com/research/report/startup-failure-reasons-top/
- Date: 2026-09-16
- Channel: WebFetch

Methodology, quoted: "Using the CB Insights platform, we identified 431 VC-backed startups that publicly shut down since 2023, excluding companies that had a prior exit. We then categorized the companies (with sufficient data) by primary reasons for failure." Of the 431, "385 companies for which failure reasons could be identified." Top reasons, quoted: "Ran out of capital (70%)," "Poor product-market fit (43%)," "Bad timing (29%)," "Unsustainable unit economics (19%)." Note: "many startups cited multiple reasons for their failure, the chart below exceeds 100%" (multi-coded, not mutually exclusive). "Not the right team" / founder-count as an explicit category: unknown — checked same URL 2026-09-16, this CB Insights report as fetched does not break failures out by founding-team size (solo vs. 2 vs. 3+); it also does not use "not the right team" as one of its named categories in what was pulled.

---

## Block 26 — Qualitative-only sources found: Paul Graham essay, Y Combinator, Startup Genome
- URL: https://www.paulgraham.com/13sentences.html ; https://en.wikipedia.org/wiki/Y_Combinator ; https://en.wikipedia.org/wiki/Startup_Genome (404) ; https://www.ycombinator.com/blog/should-you-have-a-co-founder (404)
- Date: 2026-09-16
- Channel: WebFetch

Paul Graham, "Startups in 13 Sentences" (essay, opinion — not a study, no sample size), quoted: "Cofounders are for a startup what location is for real estate." "You can change anything about a house except where it is. In a startup you can change your idea easily, but changing your cofounders is hard." "The success of a startup is almost always a function of its founders." On failure causes generally (no team-size stat): "Most startups fail before they make something people want, and the most common form of failure is running out of money," and "though the immediate cause of death in a startup tends to be running out of money, the underlying cause is usually lack of focus." The essay "does not specify an ideal number of founders."

Wikipedia's "Y Combinator" article: checked for batch-level founder-count statistics; none found — "no statistics on founding team size, number of founders per batch company, or solo versus co-founder success rates."

Startup Genome report: wikipedia.org/wiki/Startup_Genome returned HTTP 404 — no Wikipedia article exists under that title; the primary Startup Genome report site was not located this session (WebSearch exhausted, and no guessable direct report URL was found). unknown — could not access.

A direct YC blog post on cofounder count (guessed URL https://www.ycombinator.com/blog/should-you-have-a-co-founder) returned HTTP 404 — guessed URL was wrong or the post does not exist at that path; not re-attempted (would require WebSearch, which is exhausted).

Bottom line for the compiler: no source pulled this session gives a clean, sourced percentage comparing solo-founder vs. two-founder vs. three-plus-founder success/funding/failure rates with a stated sample size. The closest things found are (a) Wasserman's 10,000-founder/3,500-startup dataset, whose team-size breakdown is locked behind the book itself, and (b) CB Insights' 431-company failure-reasons study, which does not cut by team size at all. Any specific "X% of two-founder startups succeed vs Y% of solo-founder startups" figure the compiler may recall from elsewhere was NOT confirmed by this research pass and should not be used without a fresh, dated pull.
