# Market gaps in AI, 2026-09 — source index

All rows fetched 2026-09-16 unless noted. Companion file: `market-gaps-2026-pulls.md`.

| source | URL | type | what it gave | date fetched |
|---|---|---|---|---|
| Reddit r/SaaS (JSON API) | https://www.reddit.com/r/SaaS/search.json?q=AI%20wish%20there%20was&restrict_sr=1 | demand-side forum, blocked | nothing — HTTP 200 but React app-shell HTML, no post data | 2026-09-16 |
| Reddit r/SaaS (old.reddit) | https://old.reddit.com/r/SaaS/search.json?q=AI&restrict_sr=1 | demand-side forum, blocked | nothing — 0 bytes returned | 2026-09-16 |
| Reddit (api subdomain) | https://api.reddit.com/r/SaaS/search?q=AI&restrict_sr=1 | demand-side forum, blocked | nothing — HTTP 403 on request line, app-shell HTML body | 2026-09-16 |
| Reddit via WebFetch | https://old.reddit.com/... and https://www.reddit.com/... | demand-side forum, blocked | nothing — WebFetch tool refuses both hostnames | 2026-09-16 |
| G2 (Otter.ai reviews) | https://www.g2.com/products/otter-ai/reviews?filters%5Bnps_score%5D%5B%5D=1 | review site, blocked | nothing — HTTP 403 Forbidden | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=AI+coding+assistant&tags=story | demand-side, trade-press proxy | connectivity check, sample coding-assistant story titles | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20coding%20assistant&tags=comment&hitsPerPage=30 | demand-side comments | 30 recent comments mentioning "AI coding assistant"; mostly generic sentiment, no scoped gap found | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=Ask%20HN%20AI&tags=story&hitsPerPage=30 | demand-side, Ask HN | ranked list of Ask HN AI threads by points; top hit off-topic (hearing aids) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=Show%20HN%20AI%20agent&tags=story&hitsPerPage=20 | demand-side, Show HN | ranked list of Show HN AI-agent launches by points; low traction across the board except SimCity/Epstein-files novelty projects | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=AI%20note%20taker&tags=story&hitsPerPage=20 | demand-side, Show HN | seed list for the notetaker-overcrowding survey (Block 1) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=AI%20SDR&tags=story&hitsPerPage=20 | demand-side, Show HN | AI SDR product launches, no strong gap signal found directly | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=shutting%20down%20AI&tags=story&hitsPerPage=30 | trade-press proxy | seed list, low signal on this exact phrase | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search?query=sunset%20AI%20product&tags=story&hitsPerPage=20 | trade-press proxy | seed list, low signal on this exact phrase | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20agent%20frustrating&tags=story&hitsPerPage=20 | demand-side | seed list, low signal | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=%22I%20wish%20there%20was%20an%20AI%22&hitsPerPage=20 | demand-side, exact phrase | 7 hits, one usable ("wish there was an AI tool that made me faster at coding," 2025-09-30, sarcastic) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=%22why%20is%20there%20no%20AI%22&hitsPerPage=20 | demand-side, exact phrase | 2 hits, neither a scoped product gap | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=%22nobody%20has%20built%22&hitsPerPage=20 | demand-side, exact phrase | 20 hits; used for Block 3 (tax-filing API) and Block 17 (mixed/rejected hits) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/47769711 | demand-side, single comment | full text of the "no Stripe for taxes" comment, Block 3 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20note%20taking%20apps%20crowded&hitsPerPage=15 | demand-side | 11 hits, contributed to Block 1 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=too%20many%20AI%20wrapper%20startups&hitsPerPage=20 | demand-side | 15 hits, used for Block 7 (overcrowding, AI-wrapper thesis) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20meeting%20notes%20free&hitsPerPage=20 | demand-side, Show HN | 20 hits, main source for Block 1 (CallBro, Biscotti, Compendium, Screenpipe, LymeScribe, Voicecard, MySamantha) and Block 2 (CallBro full text) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/48968135 | demand-side, single item | full CallBro Show HN text, Block 2 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/48894351 | demand-side, single item | full Biscotti Show HN text, Block 1 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/49431777 | demand-side, single item | full Voicecard Show HN text, Block 1 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/49289952 | demand-side, single item | full LymeScribe Show HN text, Block 1 | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=Zoom%20AI%20Companion%20free%20killed&hitsPerPage=15 | demand-side | 3 hits, none usable | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=%22we%20don%27t%20plan%20to%20support%22&hitsPerPage=20 | vendor-refusal search | 10 hits, all non-AI (Typesense, Zig, VMware Fusion, Backblaze, DataNitro) — no AI-specific "won't support" found via this phrase | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=%22out%20of%20scope%22%20AI%20feature%20request&hitsPerPage=20 | vendor-refusal search | 3 hits, none usable | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20tool%20no%20support%20for%20non-English&hitsPerPage=20 | non-English complaint search | 5 hits, none usable — pivoted to OpenAI/Cursor Discourse forums instead | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20SDR%20outbound%20spam&hitsPerPage=20 | demand-side | 3 hits, yielded Block 8 (Unspam, negative evidence) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20customer%20support%20chatbot%20terrible&hitsPerPage=20 | demand-side | 10 hits, mostly generic anti-chatbot sentiment predating LLMs, no scoped gap | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=Cursor%20offline%20support%20wont&hitsPerPage=15 | vendor-refusal search | 6 hits, none Cursor-specific/usable | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=local%20currency%20pricing%20AI%20subscription&hitsPerPage=20 | non-US complaint search | 9 hits, none directly usable — pivoted to OpenAI Discourse forum | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20tool%20no%20invoice%20VAT&hitsPerPage=15 | non-US complaint search | 15 hits, none usable | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=ChatGPT%20not%20available%20in%20my%20country&hitsPerPage=15 | non-US complaint search | 15 hits, none directly quotable at useful length — superseded by OpenAI Discourse forum search (much stronger) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=Adept%20AI%20Amazon&hitsPerPage=15 | trade-press proxy | 15 hits, located the Amazon/Nova/Adept shutdown comment (Block 4) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/49082451 → parent https://hn.algolia.com/api/v1/items/49082344 | trade-press proxy | resolved comment to parent story "Amazon overhauls its AI strategy, winding down most flagship models" (Business Insider, 2026-07-28) | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=Botkeeper&hitsPerPage=20 | trade-press proxy | did not resurface the shutdown comment under this query alone; comment already captured from an earlier query | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/items/46944882 | trade-press proxy | Botkeeper shutdown claim comment, Block 6 | 2026-09-16 |
| Botkeeper (company site) | https://www.botkeeper.com | vendor-stated, primary | no shutdown notice found — cross-check for Block 6, contradicts/does not confirm the HN claim | 2026-09-16 |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=Humane%20AI%20Pin%20shutting%20down&hitsPerPage=20 | trade-press proxy | 9 hits, located the two Verge-linked HN stories on the Humane/HP shutdown | 2026-09-16 |
| The Verge (fetched via curl, WebFetch refused this domain) | https://www.theverge.com/news/614883/humane-ai-hp-acquisition-pin-shutdown | trade-press, primary reporting | full verbatim shutdown terms, refund policy, dates — Block 5 | 2026-09-16 (article dated 2025-02-18) |
| Hacker News Algolia API | https://hn.algolia.com/api/v1/search_by_date?query=AI%20startup%20shutting%20down%202026&hitsPerPage=30 | trade-press proxy | 13 hits; surfaced the Botkeeper comment and unrelated older shutdowns (Olive, Argo.ai, Stockwell/Bodega) not used | 2026-09-16 |
| killedbygoogle.com | https://killedbygoogle.com/ | crowd-maintained tracker, unconfirmed vs. primary source | Firebase Studio, Pixel Studio, Doppl, Tenor API, Google Earth Pro shutdown dates — Block 16 | 2026-09-16 |
| OpenAI community forum (Discourse JSON API) | https://community.openai.com/search.json?q=not%20available%20in%20my%20country | demand-side, non-US complaints | ~20 posts across 2022-2026, 10+ countries — Block 14 | 2026-09-16 |
| OpenAI community forum (Discourse JSON API) | https://community.openai.com/search.json?q=payment%20local%20currency | demand-side, non-US complaints | India UPI request, Indonesia pricing complaint — seed for Block 15 | 2026-09-16 |
| OpenAI community forum (Discourse topic API) | https://community.openai.com/t/1254984.json | demand-side, non-US complaint, full text | India INR/UPI request, full text — Block 15 | 2026-09-16 |
| OpenAI community forum (Discourse topic API) | https://community.openai.com/t/1026197.json | demand-side, non-US complaint, full text | Indonesia affordability complaint, full text — Block 15 | 2026-09-16 |
| OpenAI community forum (HTML page, JS-rendered) | https://community.openai.com/search?q=not%20available%20in%20my%20country | demand-side, blocked | nothing — placeholder "This is not the content you are looking for", empty without JS | 2026-09-16 |
| Cursor community forum (Discourse JSON API) | https://forum.cursor.com/search.json?q=local%20model%20support | demand-side, vendor-lock complaint | 20+ posts; located topic 171317 (Cloud Agent third-party model request) — Block 12 | 2026-09-16 |
| Cursor community forum (Discourse JSON API) | https://forum.cursor.com/search.json?q=will%20not%20support | vendor-refusal search | 15 posts; located topic 171443 (Cyrillic fix) — Block 10 | 2026-09-16 |
| Cursor community forum (Discourse JSON API) | https://forum.cursor.com/search.json?q=not%20on%20our%20roadmap | vendor-refusal search | 10 posts; located topic 171082 (ACP auto-review) — Block 11 | 2026-09-16 |
| Cursor community forum (Discourse topic API) | https://forum.cursor.com/t/171082.json | vendor-stated, primary, full text | full ACP auto-review thread incl. staff reply, Block 11 | 2026-09-16 |
| Cursor community forum (Discourse JSON API) | https://forum.cursor.com/search.json?q=fully%20offline%20air-gapped | demand-side | 1 hit, not usable | 2026-09-16 |
| Cursor community forum (Discourse JSON API) | https://forum.cursor.com/search.json?q=India%20pricing%20currency | non-US complaint search | 1 hit; located topic 166818 — Block 13 | 2026-09-16 |
| Cursor community forum (Discourse topic API) | https://forum.cursor.com/t/166818.json | demand-side, non-US complaint, full text | full INR pricing request, view/post/like counts — Block 13 | 2026-09-16 |
| WebSearch tool | (n/a — query text withheld, no search performed) | search engine | "Web search was not performed: this session has used its web search budget (200 of 200 WebSearch calls)" — budget fully exhausted before this session's first query | 2026-09-16 |

## Caveats on this index

- Every Hacker News Algolia row above is a *demand-side proxy*, not an independent primary source for shutdown/product claims — HN comments frequently paraphrase or link trade press without the underlying article being independently fetched (see Block 4, Block 6). Treat HN-comment-only claims as unconfirmed until cross-checked.
- Reddit, the single most-requested channel in the brief, was completely unreachable this session (curl and WebFetch both failed, by different failure modes) — see Block 0 in the pulls file. This is a hole in coverage, not a finding of "no Reddit complaints exist."
- G2/Capterra low-star review mining (also requested in the brief) could not be executed — G2 403'd WebFetch; Capterra was not attempted after the G2 failure given the WebSearch budget was already at zero and no direct review-page URL was in hand.
- Discourse-based product forums (OpenAI community, Cursor forum) turned out to be the single best-yielding channel this session, better than HN for the non-US/non-English question specifically, because their `/search.json` and `/t/<id>.json` endpoints are open, unauthenticated, and not JS-gated — worth reusing for other product categories (Anthropic, Notion, Perplexity, etc. all run Discourse forums) in a follow-up pull if the main thread wants more of this signal.
