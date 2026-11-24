# Chris Decodes hub

Public website: https://chrisdecodes-io.github.io/

A focused home for Chris Decodes prompts, instructions and skills, alongside Instagram, Substack and GitHub. Each released resource has a practical detail page with its purpose, expected outcomes, requirements and usage steps.

Taglines use the wordmark-led Editorial serif associated with “Chris”, at its native regular weight. Body text remains Inter.

Current visual decisions and supersessions: [website maintenance notes](HOME-NOTES.md).

Preferred format for future resources: [starter-prompt detail page pattern](HOME-NOTES.md#preferred-resource-detail-format). Use [direct descriptions and usage steps](HOME-NOTES.md#direct-resource-descriptions-and-usage) to distinguish the resource types.

## Build and preview

Run `node scripts/build.mjs`, then `python3 scripts/check.py`. No package installation is required. Generated HTML is committed. To preview, run `python3 -m http.server 4186 --bind 127.0.0.1` from this directory and open http://127.0.0.1:4186/.

GitHub Pages publishes `main` from the repository root. `.nojekyll` preserves the static deployment. Asset URLs include content hashes so updates do not reuse stale CSS or animation files. No account, backend, tracking or browser-side GitHub authentication is required.

## Navigation and release scope

The shared main navigation and footer offer Home, Prompts, Instructions, Skills and About Chris. `data/site.json` supplies the labels, destinations and collection descriptions. Home uses a larger centered tagline with two platform icons on each side, a matching centered peek, the blue Featured panel and social tiles; each resource collection also has its own Home tile.

`/prompts/` lists the existing task context starter prompt. `/instructions/` and `/skills/` explain their respective resource types and show honest empty states. Collections show resources or availability before general usage steps, offer a useful next destination when empty, and derive entries and counts from `data/resources.json` through one shared template. No private skills or instruction sets have been released.

The starter prompt remains at `/resources/task-context-starter-prompt/`, with its original text and download unchanged and a Go to prompt shortcut that moves keyboard focus to the copyable text. Its catalog entry is now listed under Prompts, with a matching breadcrumb and selected navigation. Detail pages explicitly show Purpose, Expected outcomes, Works with, Format, How to use it, What you need, relevant content/actions and Things to know when applicable. Describe outcomes without guaranteeing model results. Only show actions backed by actual public content or files.

Legacy `/resources/` type links and old root type queries route to the corresponding active collection. `/guides/?category=prompting` routes to Prompts. Recognized Prompts, Instructions and Skills guide categories open their matching collection. Unknown or retired guide/project routes return to Home rather than an unrelated empty collection. The fallback HTML links offer all three current collections without JavaScript.

Keep `data/resources.json` as the explicit public-release catalog. Do not scan or publish private repositories automatically. The generic article feed and standalone Projects/Resources indexes remain retired. New collection pages do not authorize releasing additional content.

## Latest highlight

The blue Home banner selects the newest dated item from confirmed Instagram publications in `data/highlights.json` and eligible available resources in `data/resources.json`. A confirmed Instagram post wins a same-day tie; future-dated items do not appear before their Pacific publication date. Resource content and release status remain separate from Instagram highlights.

For a published Instagram post, add an entry with `id`, `title`, `description`, `publishedOn` (`YYYY-MM-DD`), direct HTTPS `url` (`/p/…/` or `/reel/…/`), and `confirmed: true`. Use the actual publication date, verify the destination and use an approved short summary. Do not put drafts, private media or planned posts here. Build, review and publish the site after updating the list. An Instagram highlight changes only the banner, not the resource collections.

Christopher confirmed on November 24, 2026 that no Instagram posts have been published yet. The list therefore remains empty and the existing starter prompt stays Featured. Update this website as part of publishing Instagram posts together: verify the live post URL and date, add approved title/summary metadata, link any already-released related resource, rebuild, review and publish, then verify the live highlight. There is no live Instagram feed, polling or automatic detection configured or requested.

## Channel links

`data/site.json` → `channels` is the single source for channel links in every header, the Home tiles and About Chris. Destinations are [Instagram chris.decodes](https://www.instagram.com/chris.decodes/), the [Substack @chrisdecodes profile](https://substack.com/@chrisdecodes) and [GitHub chrisdecodes-io](https://github.com/chrisdecodes-io). Header links use matching blue-and-cream buttons labeled Instagram, Substack and GitHub. Do not display private/public status labels unless Christopher requests them. Both former social placeholders are linked.

## Future additions

GitHub Pages remains the current host; no migration is planned. [Outbound affiliate links and brand inquiries](HOME-NOTES.md#future-affiliate-links-and-brand-inquiries) are deferred additions. No new section, contact address or affiliate offer is live.

## Visual and character direction

Preserve cream #F4F1EA, rich blue #173FBF, the restrained corner lift toward #4667CC, Organic Emphasis headings and Inter supporting text. Use the restored CTA lockup in the header and footer: the original stacked ink wordmark beside the cream-on-blue CD square, proportionally scaled as one centered group. The original stacked wordmark masters remain unchanged. Use sentence case, preserving official names.

Show the exact tagline once per content page: in the Home introduction and in inner-page footers. Keep welcome eyebrows, repeated introduction copy, sidebar slogans and duplicate Featured labels out of the page. The footer adds navigation, not a new heading or card.

Center the cat within its reserved open media area. The desktop blue panel uses a right-hand media column; mobile gives the cat a centered slot beside the status text. Empty-state character/text groups stay centered and compact. Preserve proportional scaling, inward orientation and clear controls.

One peeking character takes turns among three distinct section edges per content page, completing the dip before moving. The Home footer peek replaces the earlier Rest placement. Curious accompanies Featured, and Work accompanies the Skills and Instructions empty states. `assets/characters/usage.json` records purposes, exact approved collection sources, timings and hashes. Original Expressive v7 artwork and full 12-second timing are retained. Curious uses the approved November 24 neck refinement. Earlier short forward/reverse website derivatives are superseded. The shared library Curious exports carry the same approved correction; other character selections retain their separate approvals.

Videos loop silently without pause controls. The Home tagline peek uses a 1.12× entrance and 1.18× idle to shorten the hold by about 1.5 seconds, returning to 1× for the complete dip. Other peeks and primary companions retain normal speed; OS reduced-motion preferences do not alter playback under Christopher’s explicit website instruction. Matching stills provide unsupported/blocked-playback fallbacks. The Home walker travels horizontally at a fixed height, entering through Featured’s left boundary and exiting through its right boundary. Its entire frame starts and finishes outside the lane, with matching 10 px soft boundaries. The website-only walk derivative registers all 30 decoded frames to one paw baseline; see `assets/characters/walk-registration.json` and `scripts/prepare-walk.py`. Original shared artwork and native one-second gait timing remain unchanged. It returns to the tagline peek while that area remains visible. Characters load/play only while in the viewport, so the footer is lazy-loaded. Decorative media cannot intercept clicks.

Font notices remain in `assets/licenses/`. Brand artwork and characters are included for this Chris Decodes site; no blanket redistribution license is granted. This README is the website maintenance/retrieval entry point. No other-client or other-Mac adoption is claimed.

## Curious neck refinement, November 24, 2026

Christopher approved propagation of the corrected Curious motion. The Home Featured banner uses one smaller tilt and quiet return, preserving the artwork, 12-second timing, blinks, tail and inward facing placement. Current exports in the shared character library and original export pack match this correction; old media remain in their history folders. See `assets/characters/usage.json`. The correction recipe and QA are in the shared collection’s `Curious-Refinement-2026-11-24.json` and source checkpoint. The separate Curious Notice animation is unchanged.

The CTA wordmark is reproducible with `python3 scripts/prepare-cta-wordmark.py`. Its receipt is `assets/wordmark-cta-usage.json`; the unchanged source letter paths are checked by `scripts/check.py`. The earlier horizontal derivative is superseded and unused. Home’s Claude, ChatGPT and Codex cluster uses consistent cream-on-blue platform marks; see `assets/platforms/usage.json` and HOME-NOTES.md for roles and behavior.

## Home tagline and icon alignment

The Home tagline is centered in the content frame at up to 48 px on desktop, 32 px on phones and 30 px on the narrowest layout. Claude and the Claude Code pixel avatar flank the left; ChatGPT and Codex flank the right. Their full float envelopes must clear the words and cat lane. The Featured-edge peek follows the same centerline. Header branding retains the approved CD/wordmark proportions and common vertical center, with the complete lockup centered over the content/tagline column. When the sidebar collapses, it centers over the full page. Below 1200 px the channel buttons use a separate row, sharing that content centerline while the sidebar is visible.

Platform asset provenance is recorded in assets/platforms/usage.json. The Claude Code avatar reuses Lobe Icons vector geometry with its license in assets/licenses/lobe-icons-LICENSE. The GitHub Home square reuses the existing GitHub mark rather than the retired folder pictogram. Instructions uses one clear, centered clipboard checkmark.
