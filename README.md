# Chris Decodes resource library

Public website: https://chrisdecodes-io.github.io/

An accessible front door to released Chris Decodes resources and projects. Visitors browse by resource type, see what an item does and where it works, then open its instructions and available actions. This is a resource library, with no article feed or publishing chronology.

## Build and preview

Run `node scripts/build.mjs` from this repository, then `python3 scripts/check.py`. No packages need installing. The generator reads `data/resources.json` and writes the catalog, collection pages, resource detail pages, text download and shared navigation. Run `python3 -m http.server 4186 --bind 127.0.0.1` and open http://127.0.0.1:4186/ for a local preview.

Generated HTML is committed. GitHub Pages publishes `main` from the repository root; `.nojekyll` keeps this a static site. No backend, account, analytics, API token or browser-side GitHub authentication is required. The fixed root-relative URLs target this user-site deployment.

## Page map and navigation

- `/`: All resources, immediately showing the catalog, search and resource-type filter.
- `/?type=prompts`, `/?type=templates`, `/?type=workflows`: filtered catalog views with matching titles and selected sidebar entries. A `q` query preserves a search when changing type.
- `/skills/` and `/projects/`: dedicated collection pages with honest empty states until approved releases are added.
- `/resources/task-context-starter-prompt/`: purpose, compatibility, instructions, requirements, copy, text download and source for the initial public resource.
- `/about/`: brief introduction and channel destinations. Instagram and Substack remain explicit placeholders; GitHub links to the confirmed profile.
- `/guides/`: compatibility route to the catalog. The old prompting category and `#start` map to Prompts; workflows maps to Workflows; other categories map to All resources.

Use sentence case throughout. Preserve official names such as Chris Decodes, GitHub and Substack. Keep category labels and selected states consistent. Search and interactive filters need JavaScript; the static catalog links, resource instructions, download and dedicated collections remain accessible without it.

## Catalog and release boundary

`data/resources.json` is the sole resource catalog. The initial entry is the already-public starter prompt, with its original wording preserved. General advice articles have been removed. Skills, templates, workflows and projects have no available releases yet. Empty collections do not pretend files or products exist.

Every entry specifies its ID, title, type, purpose, compatibility, format, availability, instructions, requirements and relevant content/download/source. Version information is omitted until verified. Add only explicitly approved, sanitized public resources. Catalog selection never imports or releases private repository contents automatically. Run the generator, review the generated diff and check the action destinations before publishing. When removing a resource, also remove its generated detail page and download from the published source.

`app.js` handles search, type navigation, selected states, mobile navigation and prompt copying. `legacy-guides.js` preserves old links. `scripts/build.mjs` owns the common page shell, so header/sidebar changes are made once.

## Branding and character assignments

Preserve cream #F4F1EA, blue #173FBF, Organic Emphasis headings and Inter body/controls. Christopher selected the exact cream wordmark on a blue background. Use the fixed artwork, not a text reconstruction.

Decoder Cat is an inward-facing companion next to the relevant copy, not a detached ornament. Keep one visible character per main view, scale proportionally and protect the search, card and download reading lanes. Curious accompanies the library introduction or no-result state; Work accompanies Skills; Presenting accompanies Projects. Image alternatives are empty because the artwork is decorative and the adjacent text carries the meaning.

`assets/characters/usage.json` records source collections, exact source spans, roles, timings and derivative hashes. Source artwork remains in the established shared character library. Curious and Presenting use active spans from the approved Expressive v7 collection, played forward and back without duplicated endpoints to produce continuous 3.333-second loops. Work uses the approved four-second laptop loop unchanged. Matching transparent PNGs provide fallbacks. These website derivatives do not change the shared character library or production-engine defaults.

Christopher explicitly requested continuous looping, no pause option, and playback unaffected by the OS reduced-motion setting. Browser videos are silent, looped and inline. Still posters remain if the format is unsupported or playback is blocked. Hidden character instances do not play. This supersedes the initial static-only website plan at the website scope.

Font license notices are preserved in `assets/licenses/`. The brand artwork and characters are included for this Chris Decodes site; no blanket right to redistribute them is granted. The website README is the maintenance and retrieval entry point for these assignments; no other-runtime or other-Mac adoption is claimed.
