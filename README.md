# Chris Decodes resource library

Public website: https://chrisdecodes-io.github.io/

A home hub for released Chris Decodes resources, projects and channels. Home provides eight clear tiles and a resource search; Resources contains the searchable catalog. This remains a resource library, with no article feed or publishing chronology.

## Build and preview

Run `node scripts/build.mjs` from this repository, then `python3 scripts/check.py`. No packages need installing. The generator reads `data/resources.json` and writes the catalog, collection pages, resource detail pages, text download and shared navigation. Run `python3 -m http.server 4186 --bind 127.0.0.1` and open http://127.0.0.1:4186/ for a local preview.

Generated HTML is committed. GitHub Pages publishes `main` from the repository root; `.nojekyll` keeps this a static site. No backend, account, analytics, API token or browser-side GitHub authentication is required. The fixed root-relative URLs target this user-site deployment.

## Page map and navigation

- `/`: Home, with one grid containing Resources, Skills, Projects, the available starter prompt, Instagram, Substack, GitHub and About Chris. The two social placeholders are non-clickable tiles. Search submits to `/resources/`.
- `/resources/`: searchable catalog. `?type=prompts`, `?type=templates` and `?type=workflows` select resource types; `q` preserves a search when changing type.
- `/skills/` and `/projects/`: dedicated collections with honest empty states until approved releases are added.
- `/resources/task-context-starter-prompt/`: instructions, requirements, copy, text download and source for the initial public resource.
- `/about/`: introduction and channel information. Instagram and Substack remain explicit placeholders; GitHub links to the confirmed profile.
- Old `/?type=...` and `/?q=...` links route to Resources while preserving recognized filters/search. `/guides/` prompting and `#start` map to Prompts; workflows maps to Workflows; other categories map to Resources.

`data/site.json` supplies the shared navigation, labels, descriptions, type destinations and exact tagline. The sidebar has only Home, Resources, Skills, Projects and About Chris. Resource types remain catalog filters rather than competing sidebar destinations. The header always offers a visible Home link beside the cream-on-blue wordmark plus Instagram, Substack and GitHub. Mobile headers use two rows. The footer links to Home, Resources, About Chris and Website source.

Use sentence case throughout, preserving official names. Show the exact full tagline once per page: in the Home introduction, and in the footer on inner pages. Keep slogans out of the sidebar. Search and filters need JavaScript; Home tiles, page links, resource instructions and downloads remain usable without it. The legacy guide route has an ordinary catalog link as its no-JavaScript fallback.

## Catalog and release boundary

`data/resources.json` is the sole resource catalog. The initial entry is the already-public starter prompt, with its original wording preserved. General advice articles have been removed. Skills, templates, workflows and projects have no available releases yet. Empty collections do not pretend files or products exist.

Every entry specifies its ID, title, type, purpose, compatibility, format, availability, instructions, requirements and relevant content/download/source. Version information is omitted until verified. Add only explicitly approved, sanitized public resources. Catalog selection never imports or releases private repository contents automatically. Run the generator, review the generated diff and check the action destinations before publishing. When removing a resource, also remove its generated detail page and download from the published source.

`app.js` handles search, type navigation, selected states, mobile navigation and prompt copying. `legacy-guides.js` preserves old links. `scripts/build.mjs` owns the common page shell, so header/sidebar changes are made once.

## Branding and character assignments

Preserve cream #F4F1EA, blue #173FBF, Organic Emphasis headings and Inter body/controls. Christopher selected the exact cream wordmark on a blue background. Use the fixed artwork, not a text reconstruction.

Decoder Cat is an inward-facing companion next to the relevant copy, not a detached ornament. Keep one visible character per main view, scale proportionally and protect the search, card and download reading lanes. Curious accompanies the library introduction or no-result state; Work accompanies Skills; Presenting accompanies Projects. Image alternatives are empty because the artwork is decorative and the adjacent text carries the meaning.

`assets/characters/usage.json` records source collections, exact source spans, roles, timings and derivative hashes. Source artwork remains in the established shared character library. Curious, Work and Presenting use the original approved Expressive v7 animations unchanged: 360 frames at 30 fps, twelve seconds each. Play the full gestures and their natural settling moments at normal speed, then loop. This calmer pacing supersedes the earlier short website derivatives and continuous-motion timing at the website scope. Matching transparent PNGs provide fallbacks. These website derivatives do not change the shared character library or production-engine defaults.

Christopher requested calm full gestures in this revision; continuous looping, no pause option and playback unaffected by the OS reduced-motion setting remain in effect. Browser videos are silent, looped and inline. Still posters remain if the format is unsupported or playback is blocked. Hidden character instances do not play. Do not reintroduce the short forward/reverse website loops. New playback choices remain website-specific and do not alter the shared source library.

Font license notices are preserved in `assets/licenses/`. The brand artwork and characters are included for this Chris Decodes site; no blanket right to redistribute them is granted. The website README is the maintenance and retrieval entry point for these assignments; no other-runtime or other-Mac adoption is claimed.
