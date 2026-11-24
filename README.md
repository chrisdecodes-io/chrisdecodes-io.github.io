# Chris Decodes hub

Public website: https://chrisdecodes-io.github.io/

A focused home for Chris Decodes, a standalone Skills section and the Instagram, Substack and GitHub destinations. The broader resource library is deferred while Christopher decides what belongs in it.

## Build and preview

Run `node scripts/build.mjs`, then `python3 scripts/check.py`. No package installation is required. Generated HTML is committed. To preview, run `python3 -m http.server 4186 --bind 127.0.0.1` from this directory and open http://127.0.0.1:4186/.

GitHub Pages publishes `main` from the repository root. `.nojekyll` preserves the static deployment. Asset URLs include content hashes so updates do not reuse stale CSS or animation files. No account, backend, tracking or browser-side GitHub authentication is required.

## Navigation and release scope

The main navigation and footer offer Home, Skills and About Chris. `data/site.json` supplies those shared labels and destinations.

Home has one Chris Decodes heading and the exact tagline. Its blue panel opens Skills. With no public skill releases, it describes the library and states that no skills are available. When an approved listed skill is added, the panel features the newest one by its `publishedOn` date, with catalog order as the same-day tie-breaker.

Below the panel, four tiles highlight Instagram, Substack, GitHub and About Chris. Christopher explicitly reaffirmed the importance of the social squares. Instagram and Substack remain non-clickable, clearly labeled placeholders until their URLs are confirmed; GitHub is linked to the public profile. The top header also retains prominent channel access and a visible Home button.

`/skills/` is the only resource section. It has no empty search/filter controls and makes no available-download claims. No public skills have been released. Adding a private skill to the public catalog requires separate release approval.

The old `/resources/`, `/projects/` and `/guides/` routes forward to Skills, with ordinary fallback links for browsers without JavaScript. Old root query links also forward to Skills. These are compatibility routes, not additional maintained sections.

The already-public starter prompt remains at `/resources/task-context-starter-prompt/` with its original text download. Its catalog record has `listed: false`; it is not promoted on Home, labeled as a skill, or part of the active Skills collection. Its detail page explains its earlier-example status. This preserves old links without reopening the broader resource-library scope.

`data/resources.json` is the explicit release catalog. Do not scan or publish private repositories automatically. The generic article feed and empty standalone Projects/Resources pages have been retired. The latest user-directed Skills focus supersedes earlier broader resource-navigation plans.

## Visual and character direction

Preserve cream #F4F1EA, rich blue #173FBF, the restrained corner lift toward #4667CC, Organic Emphasis headings and Inter supporting text. Keep the fixed cream wordmark on blue. Use sentence case, preserving official names.

Show the exact tagline once per content page: in the Home introduction and in inner-page footers. Keep welcome eyebrows, repeated introduction copy, sidebar slogans and duplicate Featured labels out of the page. The footer adds navigation, not a new heading or card.

Center the cat within its reserved open media area. The desktop blue panel uses a right-hand media column; mobile gives the cat a centered slot beside the status text. Empty-state character/text groups stay centered and compact. Preserve proportional scaling, inward orientation and clear controls.

The Home footer includes the approved Rest character beside the links as a quiet closing companion requested by Christopher. Curious accompanies the Home panel, and Work accompanies the Skills empty state. `assets/characters/usage.json` records purposes, exact approved collection sources, timings and hashes. Original Expressive v7 artwork and full 12-second animations remain unchanged. Earlier short forward/reverse website derivatives are superseded; the shared character library and engines are not changed.

Videos loop silently at normal speed, without pause controls; OS reduced-motion preferences do not alter playback under Christopher’s explicit website instruction. Matching stills provide unsupported/blocked-playback fallbacks. Characters load/play only while in the viewport, so the footer is lazy-loaded. Decorative media cannot intercept clicks.

Font notices remain in `assets/licenses/`. Brand artwork and characters are included for this Chris Decodes site; no blanket redistribution license is granted. This README is the website maintenance/retrieval entry point. No other-client or other-Mac adoption is claimed.
