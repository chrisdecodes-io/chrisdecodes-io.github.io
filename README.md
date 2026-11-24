# Chris Decodes hub

Public website: https://chrisdecodes-io.github.io/

A focused home for Chris Decodes, a standalone Skills section and the Instagram, Substack and GitHub destinations. The broader resource library is deferred while Christopher decides what belongs in it.

Current visual decisions and supersessions: [website maintenance notes](HOME-NOTES.md).

## Build and preview

Run `node scripts/build.mjs`, then `python3 scripts/check.py`. No package installation is required. Generated HTML is committed. To preview, run `python3 -m http.server 4186 --bind 127.0.0.1` from this directory and open http://127.0.0.1:4186/.

GitHub Pages publishes `main` from the repository root. `.nojekyll` preserves the static deployment. Asset URLs include content hashes so updates do not reuse stale CSS or animation files. No account, backend, tracking or browser-side GitHub authentication is required.

## Navigation and release scope

The main navigation and footer offer Home, Skills and About Chris. `data/site.json` supplies those shared labels and destinations.

Home opens with the exact approved tagline as its single main heading. The blue Featured panel highlights recent approved public content; the current feature is the already-published starter prompt, labeled as a prompt. Eligible items are selected from the catalog’s explicit feature flag or released Skills entries, ordered by publication date.

Below the panel, five destinations highlight Skills, Instagram, Substack, GitHub and About Chris. About Chris fills a compact final row on desktop. Christopher explicitly reaffirmed the importance of the social squares. Instagram and Substack remain non-clickable, clearly labeled placeholders until their URLs are confirmed; GitHub is linked to the public profile. The top header also retains prominent channel access and a visible Home button.

`/skills/` is the only resource section. It has no empty search/filter controls and makes no available-download claims. No public skills have been released. Adding a private skill to the public catalog requires separate release approval.

The old `/resources/`, `/projects/` and `/guides/` routes forward to Skills, with ordinary fallback links for browsers without JavaScript. Old root query links also forward to Skills. These are compatibility routes, not additional maintained sections.

The already-public starter prompt remains at `/resources/task-context-starter-prompt/` with its original text download. Its catalog record has `listed: false`; it is featured on Home as a prompt, and is not labeled as a skill or part of the active Skills collection. Its detail page explains that it is a standalone example. This preserves old links without reopening the broader resource-library scope.

`data/resources.json` is the explicit release catalog. Do not scan or publish private repositories automatically. The generic article feed and empty standalone Projects/Resources pages have been retired. The latest user-directed Skills focus supersedes earlier broader resource-navigation plans.

## Visual and character direction

Preserve cream #F4F1EA, rich blue #173FBF, the restrained corner lift toward #4667CC, Organic Emphasis headings and Inter supporting text. Use the restored CTA lockup in the header and footer: the original stacked ink wordmark beside the cream-on-blue CD square, proportionally scaled as one centered group. The original stacked wordmark masters remain unchanged. Use sentence case, preserving official names.

Show the exact tagline once per content page: in the Home introduction and in inner-page footers. Keep welcome eyebrows, repeated introduction copy, sidebar slogans and duplicate Featured labels out of the page. The footer adds navigation, not a new heading or card.

Center the cat within its reserved open media area. The desktop blue panel uses a right-hand media column; mobile gives the cat a centered slot beside the status text. Empty-state character/text groups stay centered and compact. Preserve proportional scaling, inward orientation and clear controls.

One peeking character takes turns among three distinct section edges per content page, completing the dip before moving. The Home footer peek replaces the earlier Rest placement. Curious accompanies Featured, and Work accompanies the Skills empty state. `assets/characters/usage.json` records purposes, exact approved collection sources, timings and hashes. Original Expressive v7 artwork and full 12-second timing are retained. Curious uses the approved November 24 neck refinement. Earlier short forward/reverse website derivatives are superseded. The shared library Curious exports carry the same approved correction; other character selections retain their separate approvals.

Videos loop silently at normal speed, without pause controls; OS reduced-motion preferences do not alter playback under Christopher’s explicit website instruction. Matching stills provide unsupported/blocked-playback fallbacks. Characters load/play only while in the viewport, so the footer is lazy-loaded. Decorative media cannot intercept clicks.

Font notices remain in `assets/licenses/`. Brand artwork and characters are included for this Chris Decodes site; no blanket redistribution license is granted. This README is the website maintenance/retrieval entry point. No other-client or other-Mac adoption is claimed.

## Curious neck refinement, November 24, 2026

Christopher approved propagation of the corrected Curious motion. The Home Featured banner uses one smaller tilt and quiet return, preserving the artwork, 12-second timing, blinks, tail and inward facing placement. Current exports in the shared character library and original export pack match this correction; old media remain in their history folders. See `assets/characters/usage.json`. The correction recipe and QA are in the shared collection’s `Curious-Refinement-2026-11-24.json` and source checkpoint. The separate Curious Notice animation is unchanged.

The CTA wordmark is reproducible with `python3 scripts/prepare-cta-wordmark.py`. Its receipt is `assets/wordmark-cta-usage.json`; the unchanged source letter paths are checked by `scripts/check.py`. The earlier horizontal derivative is superseded and unused. Home’s Claude, ChatGPT and Codex cluster uses consistent cream-on-blue platform marks; see `assets/platforms/usage.json` and HOME-NOTES.md for roles and behavior.
