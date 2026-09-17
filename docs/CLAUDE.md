# docs/CLAUDE.md

Scope of each subfolder here. Root `../CLAUDE.md` holds the global rules; this file decides *where a file goes*. When two folders both look right, the rule is: raw text goes to `raw/`, and only the compiled read goes to the topic folder.

All folders are empty scaffolding right now. The first file into each one sets its format — write it against the template in `method/`, or write the template first.

## `method/`

How the research runs. Read before writing any file anywhere in `docs/`.

Holds: `scope.md` (the standing brief — market, geography, decision served), the pipeline from source to compiled read, per-file line budgets, the profile and table templates, naming conventions, and any generator script plus what it consumes.

Not here: findings. A conclusion about the market is never a method doc.

## `sources/`

The channel list, and the shortlist. Who or what is worth pulling, why it made the list, and where the pull happens — registries, filings, analyst reports, job boards, app stores, review sites, trade press.

Each entry: the channel, what it reliably yields, its refresh rate, its access cost, and its known bias.

Not here: the pulled data itself. That is `raw/`.

## `raw/`

Raw pulls, one file per source pull, source-attributed. The only place long verbatim text belongs.

Every file states at the top: the source, the URL or document ID, the pull date, and the pull method. Body stays in the source's own words. **Exempt from compression** — never rewrite a pull to make it shorter, and never edit a pull to fix it. A bad pull gets re-pulled and the old file kept with its date.

Not here: interpretation. A sentence starting "this suggests" belongs in a compiled folder.

## `markets/`

Per-market sizing and structure. One file per market or segment.

Covers: definition and boundary, size with the method that produced it (top-down, bottom-up, or vendor-reported — labeled), growth with its base period, the value chain and where margin sits, structural constraints (regulatory, distribution, capital), and the caveats.

Not here: individual company detail beyond what sizes the market. That is `competitors/`.

## `competitors/`

One profile per company, plus `INDEX.md` — the one-line-per-company table that is the entry point.

A profile covers: what it sells and to whom, business model and pricing, scale (revenue, headcount, customers — each labeled with its layer and source), trajectory with a number and a direction, positioning against the field, and the negatives. Every profile answers the same questions in the same order, set by the template in `method/`.

Not here: a ranking across companies. Cross-company reads are `findings/`.

## `customers/`

The demand side. Segments, buyer personas, jobs-to-be-done, willingness to pay, switching costs, and the buying process — who decides, who blocks, what the cycle takes.

Interview notes land in `raw/` verbatim first; only the synthesis lands here, and it cites the raw file.

Not here: a supply-side read of who serves those customers. That is `competitors/`.

## `findings/`

Compiled output that crosses files: ranked tables, scorecards, cross-market and cross-company comparisons, gaps and whitespace, and the summary a reader opens first.

Each finding cites the compiled files behind it, and through them the raw. A finding that cannot name its evidence is deleted, not softened.

Not here: new facts. If a finding introduces a number that appears nowhere else in `docs/`, the number is missing a pull — go get it.
