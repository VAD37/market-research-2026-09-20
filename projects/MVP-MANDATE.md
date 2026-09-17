# MVP mandate — set by the user 2026-09-17

Supersedes the wave-2 "stop as scoped" verdicts. The research standing stays on file and
is not deleted; the user has decided to build regardless. Do not re-litigate the kill.
Use the kill evidence as design input: it tells you what the product must NOT claim.

## What must exist per project when this is done

1. **A thing that runs.** `prototype/` — one command starts it, no account, no API key
   required for the demo path, no paid call. Works offline or with fixtures.
2. **End-to-end user test.** A scripted fake user goes from landing on the product to
   getting the value, all the way through. Logged in `docs/execution/e2e-test.md` with
   actual command output pasted, not described.
3. **A sales page.** A single self-contained `site/index.html` that a stranger can read
   for 30 seconds and know:
   - what this is
   - what problem it solves
   - why it is different from the free/incumbent option (name the incumbent)
   - why you would need it
   - what value you get *right now*, with something to try on the page itself
4. **Outcome read.** `docs/outcome/` — what the demo proves, what it does not, what
   breaks at scale, and who exactly would pay.

## Hard constraints (unchanged, still in force)

- No account creation, no signups, no licence acceptance, no purchases, no paid API
  calls, no domain registration.
- Redact any token, key, OAuth value, email address or session identifier before writing
  anything into `raw/`.
- Never modify `C:\Users\vad\.claude\settings.json` or any global config. Test harnesses
  live in the project folder or the scratchpad.
- `D:\ai\aisb` and `D:\ai\ai-playground` are read-only source material.
- Agents write only inside their own project folder. Agents never run git.
- Authorized testing on owned infrastructure only. No third-party targeting.

## Honesty rule for the sales page

The page is a sales page, not a lie. Every capability claim on it must be backed by
something the prototype actually does, demonstrated in `docs/execution/e2e-test.md`.
Roadmap items are labeled as roadmap. No fake logos, no fake testimonials, no invented
customer counts, no fabricated benchmark numbers. A number on the page is either measured
by the prototype (label it) or cited from `raw/` (label it). This is not optional —
a page that fails it gets rejected in review.

## Stack constraints for `site/index.html`

Single file. Inline CSS and JS. No build step. No external fetch at page load — the demo
on the page runs on embedded fixture data. It will be published as a hosted page by the
main thread, so it must be self-contained and must render with no network.

## Stack constraints for `prototype/`

Python 3 stdlib-first, or plain Node, or static HTML+JS. Third-party deps only when they
are already installed on this machine — check before you depend on something. If you add
a dep, pin it in `prototype/requirements.txt` and state the install command in the README.
Prototype code is throwaway-grade but must RUN.

## Addendum — 2026-09-17, user grant

**Browser and container access granted.** The review phase may drive the Chrome extension,
take screenshots, and judge the sales page visually. Local website testing may use Docker
to build and serve. Still no spend, no account creation, no domain registration, no public
deployment by an agent — local serve and the main thread's hosted publish only.

**Vision review is mandatory, not optional.** A sales page is not accepted on source-read
alone. The review agent loads it in a real browser at desktop AND mobile width, screenshots
both, and looks at them. Findings about layout, hierarchy, legibility and whether the
30-second read actually lands come from the screenshot, not from reading the HTML.

**Every review phase ends with a self-interrogation section**, verbatim heading:

    ## Is this enough? What else can we do to improve it?

Under it: an honest verdict on whether the thing is ready to put in front of a buyer, then
a ranked list of concrete improvements — each with the effort it costs and what it would
change for the user. No filler entries. If the answer is "not enough", say so plainly and
say what the single most valuable next build is.

## Vision-review tooling — measured 2026-09-17

The Chrome extension (`mcp__claude-in-chrome__*`) is STILL NOT CONNECTED. Main thread tested
it: "Browser extension is not connected." Do not burn attempts on it.

**Use the Playwright MCP instead. It works — tested end to end on 2026-09-17.**

    mcp__MCP_DOCKER__browser_navigate      { url }
    mcp__MCP_DOCKER__browser_resize        { width, height }
    mcp__MCP_DOCKER__browser_take_screenshot { type:"png", filename, fullPage }
    mcp__MCP_DOCKER__browser_snapshot      accessibility tree
    mcp__MCP_DOCKER__browser_close

Screenshots come back as viewable images. `file:///D:/researchs/market-research/projects/<p>/site/index.html`
loads directly — no server needed for a self-contained page. Serve over HTTP only if the
page needs it: `python -m http.server` from the `site/` folder, or a Docker nginx if you
prefer; Docker 29.6.2 is installed and the user granted its use.

Review widths: **1440x900 desktop** and **390x844 mobile**. Screenshot both, `fullPage:true`,
and judge from the image.

## Toolchain — measured 2026-09-17

- Python **3.9.25** (uv shim). No `match`, no `X | Y` annotations without `from __future__ import annotations`.
- Installed pip packages, complete: cffi, charset-normalizer, cryptography, pdfminer.six,
  pypdf, setuptools, typing_extensions, pip. **No requests, no pandas, no numpy, no torch.**
  Stdlib first. `uv` venv install is allowed and free if genuinely needed, but the default
  demo path must run on bare stdlib with zero install.
- Node **v23.11.1**, Docker **29.6.2**.
