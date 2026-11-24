# Home feature and destinations

The blue Home banner highlights recent approved public content, including prompts and skills. The catalog field `featured: true` explicitly permits a previously public item to appear here even when it is outside the Skills collection. Eligible entries are ordered by `publishedOn`; catalog order breaks same-day ties. Display the actual resource type and action.

The published task context starter prompt is the current feature. It remains outside the standalone Skills collection. No new resources or private skills are released.

Skills has its own Home tile alongside Instagram, Substack, GitHub and About Chris. Keep the three social squares visible. Main navigation remains Home, Skills and About Chris.

This supersedes the earlier maintenance note describing a Skills-only blue banner and four tiles. Preserve the pending Curious neck-refinement review recorded in README.md; this layout change does not adopt or alter that animation candidate.

## Heading, shortcut and footer treatment

Headings use a larger, distinct hierarchy: page titles, feature titles, then blue destination and section headings. Preserve the approved Emphasis face and readable wrapping on narrow screens. Sidebar Quick access adds Featured, Starter prompt and Find Chris Decodes, all derived from data/site.json and pointing to existing content. Avoid adding unreleased collection pages.

Footer branding uses the approved Organic v2 transparent blue CD SVG from brand/assets/cd-logo-organic-v2/CD-transparent-blue.svg, adopted October 16, 2026. It is proportionally scaled as a quiet Home link at the footer corner; no redesign or artwork alteration. This mark complements the cream-on-blue header wordmark. Selection follows Christopher’s request for CD footer/corner branding; keep it separate from the cat and navigation controls.

## Square CD logo and edge peeks

The footer now uses the approved Organic v2 CD-blue-cream.svg, cream letters on blue, proportionally scaled as the Home link. This supersedes the transparent blue footer variant.

Approved peeking cat placements: Home and Skills footer edge, About channel-section edge, and the starter prompt’s copyable-text section edge. Keep one peek per page, beyond the primary reading area and clear of controls. Retain Curious in the feature and Work in Skills. The Home footer peek replaces Rest, avoiding stacked companions.

The website peek is a 13-second transparent derivative of existing approved source clips: 49 entry frames, two 147-frame quiet continuations, 28 opaque dip frames, and 19 fully hidden frames. No artwork generation or deformation. Align source row 436 of 512 to the section edge; clip beneath that originating edge. Source library remains unchanged. Rebuild with scripts/prepare-peek.py and an installed FFmpeg binary path. Provenance and output hash are in assets/characters/usage.json.

## Three-position peek sequence

One peek per page rotates right, left and center along its originating section edge. Reposition only during the 19 fully transparent end frames after the complete opaque dip. Existing approved idle continuation supplies natural blinks while the cat holds in place; do not add rapid blinking or move the cat while visible. The loop remains 13 seconds. No extra simultaneous peeking cats, extra empty sections or artwork changes.

## Separate section locations supersede same-edge rotation

The three peek slots now sit at different vertical sections. Home: Featured, destination grid and footer. Skills: introduction, collection and footer. About: Skills explanation, channel section and footer. Prompt detail: usage instructions, prompt text and footer. At most one slot is active. Advance after the opaque dip reaches its fully transparent ending. If scrolling leaves the active slot offscreen, a visible section may start from the hidden entry; no visible character teleports. Idle blink source and 13-second pacing are unchanged. Existing source artwork and release scope remain unchanged.

## Compact spacing and companion scale

Section-edge clearance is 80 px on desktop and 64 px on mobile, based on the visible peek artwork rather than its transparent 512 px canvas. Footer spacing combines 40/32 px main bottom padding with 32 px footer clearance. Keep all three peek locations and the physical ledge mask intact.

The featured Curious container is 300 px on wide screens (25% larger), 225 px on medium screens and 115 px on mobile. Skills Work is 270 px wide, 230 px on medium screens and 180 px on mobile. Preserve proportions and center the visible art beside copy; do not crop or alter the source animation. This follows Christopher’s request for proportionate cats and less open space.

## Tagline typography

Retain the exact approved wording and punctuation. On Home, set the two sentences on deliberate lines in Inter: a quiet graphite opening and a stronger blue closing, with restrained tracking and 1.5 line height. This establishes a clear reading rhythm beneath the Emphasis title. Inner-page footers use a smaller companion treatment with blue closing emphasis. No repeated slogan in the sidebar or header. The tagline remains live text and appears once per content page.

## Header and footer finish

Use a consistent paper-colored header and footer with a quiet cool-gray boundary. Header: compact cream-on-blue wordmark, lighter Home control with house icon, matching channel link surfaces, and a solid blue GitHub action. On mobile, branding/Home share the first row and three channels share the second.

Footer: group the cream-on-blue CD mark and Chris Decodes name as one brand block, paired with compact navigation. Inner-page tagline belongs under the name; Home keeps its only tagline in the introduction. Mobile stacks the navigation below a subtle divider. Preserve clear keyboard focus, the approved logos and section-edge peek clearance.

## Exact footer wordmark and whole-site review

The footer name is now assets/wordmark-ink.svg, the approved fixed outlined Chris Decodes wordmark, alongside the cream-on-blue CD monogram. Do not retype it using Emphasis or a substitute font. Use the same artwork across every content page, scale proportionally (132 px desktop, 120 px mobile), and keep the live-text tagline separate. Header uses the matching cream wordmark. This fulfills Christopher’s request for the true brand wordmark lettering.

## Adopted balanced frame

The shared generator places Home left, the cream-on-blue wordmark at the true center, and channels right in equal-sided header columns. Below 1024 px the channels occupy a centered second row. Instagram/Substack use quiet text/status treatments; GitHub remains blue. Footer CD-and-wordmark lockup, optional inner-page tagline and navigation are vertically stacked and centered on a full-width paper background. These choices supersede earlier left/right frame arrangements.

The page frame is capped at 1440 px; body content remains left-aligned. Desktop page headings cap at 56 px and Featured headings at 40 px. Home grid headings return to ink by Christopher’s explicit direction. Existing companion scale, compact 80/64 px peek clearance, silent animation timing and three-section sequence remain unchanged.

Header/footer CSS is consolidated into the final authoritative frame section of styles.css, replacing competing old rules. Reuse that section for future refinements. Review evidence covers four content pages at 1920, 1440, 1024, 900, 390 and 320 px, with exact center alignment and no horizontal overflow.

## Proportional Home spacing

Featured uses 32 px wide-screen padding. Grid cards use 24 px padding with a 210 px minimum height, allowing content to determine final height, and ink headings at 2 rem. On desktop the last About Chris destination spans the grid as a compact copy-and-action row; this removes the empty half-row without adding content. Mobile keeps the single-column card flow. Keep the 80/64 px section-edge allowance for the visible peek; shrinking transparent canvas clearance must not crowd surrounding text.

## Solid destination pictograms

Use flat ultramarine #173FBF rounded-square fields with filled cream #F4F1EA pictograms. Skills uses a puzzle piece, Instagram a camera, Substack a publication/bookmark mark, GitHub a code folder and About Chris a person. These functional inline SVGs are decorative (`aria-hidden`), alongside live ink headings. No AI sparkle, thin outline icon set, pale icon wells or gradients. This supersedes the initial line-icon treatment by Christopher’s explicit direction.

Keep fields at 36 px, with 32 px fields and 1.8 rem headings below 361 px so About Chris stays on one line. Coming-soon availability remains explicit in text and placeholders remain non-interactive; icon color stays in the brand palette. Preserve approved wordmark and CD artwork unchanged.

## Horizontal wordmark and tagline-led Home

Header and footer use assets/wordmark-horizontal-ink.svg on cream, without a blue wordmark container. This website-specific derivative repositions the exact 12 approved smooth wordmark paths into two word groups on a shared optical baseline. There is no retyping, path redrawing, stretching or source-library change. scripts/prepare-wordmark.py reproduces it from the checked approved assets/wordmark-ink.svg; assets/wordmark-horizontal-usage.json records source hash, output hash, bounds and method.

Header widths are 240 px desktop, 200 px below 1024, 140 px on phones and 128 px below 361. Footer widths are 180 px desktop and 156 px mobile, beside the unchanged CD square. Keep Home solid blue with cream lettering and icon, with dark-blue hover. Below 361 px compact Home’s padding, icon and text to maintain at least 8 px separation from the centered wordmark at a 320 px viewport.

Home has one main heading: the exact approved tagline, split into its two sentences. Use Inter, ink opening and blue closing, at a 40 px desktop maximum and 28 px on phones. The old repeated Chris Decodes heading and separate tagline paragraph are superseded. Keep one complete tagline per content page and preserve the peek’s 80/64 px clearance.

## Restored CTA lockup supersedes horizontal wordmark

Christopher rejected the horizontal arrangement and requested the CTA watermark treatment. Header and footer now use the original stacked smooth wordmark beside the CD square, following the adopted refined-v2 proportions: square 176, gap 49.3 and wordmark 516, normalized as one centered group. Header group widths are 220/192/160/128 px; footer groups are 236 px desktop and 220 px mobile. No blue pill surrounds the wordmark.

assets/wordmark-cta-ink.svg changes only the transparent viewBox margins of the approved stacked source; all letter shapes, positions and spacing remain original. scripts/prepare-cta-wordmark.py is the rebuild route, and assets/wordmark-cta-usage.json records provenance. The horizontal SVG/recipe are historical rollback artifacts, with no active page use. Original shared brand masters remain unchanged.

## Consistent floating platform cluster

The Home introduction displays the three explicitly named platforms: Claude, ChatGPT and Codex. Reuse the existing platform mark geometry in a unified cream-on-blue treatment, with matching rounded frames, visible labels, radius, spacing and gentle eighteen-second two-axis drift, with one shared path and staggered timing. Do not substitute generic AI symbols. Optical image sizing compensates for different source padding, preserving proportions.

Desktop places the cluster beside the tagline; mobile uses a compact centered row beneath it. These marks are descriptive, non-interactive list items, separate from resource releases. All three remain clear of the text and peeking cat. New decorative CSS floating respects reduced-motion preferences; the existing user-directed cat-video behavior is unchanged. Public asset identities and hashes are in assets/platforms/usage.json.

The floating platform cluster uses bounded X/Y travel rather than a fixed vertical bob: 14×12 px on wide screens, 6×8 px at intermediate widths and 8×10 px on mobile. Shared timing and geometry keep the three marks coherent; the amplitudes preserve text, neighboring icon and peek clearance.

## Wordmark serif for the tagline

Christopher selected the serif associated with “Chris” in the approved watermark. Home’s main tagline and inner-page footer taglines now use the bundled CD Wordmark Led Editorial Preview at its native regular 400 weight, without synthetic bolding. This supersedes the earlier Inter tagline treatment only; body copy, controls and platform labels remain Inter. Preserve the exact approved wording, ink opening and blue closing.

The website copy is assets/WordmarkEditorial.ttf. Its source identity, SHA-256, role and OFL license route are recorded in assets/wordmark-editorial-usage.json. This is a website-specific selection, not a change to the shared brand masters or production engines. Home remains 40 px maximum and 28 px on phones; footer taglines use 16 px. The shared generator preloads the font for all four content pages. Review covered all four pages at 1920, 1440, 1024, 900, 390 and 320 px, with loaded native-weight text and no horizontal overflow.

## Closer platform marks and alternating Home walk

Christopher requested the platform marks nearer the tagline and a walking cat when the peek is absent. The wide-screen intro now caps the text column at 580 px with a 20 px cluster gap; intermediate layouts use 16 px and mobile places the same centered trio 12 px below the text. Keep the marks grouped, labeled and clear of the heading through their complete drift envelopes.

Home alone includes a reserved cream walking lane immediately above Featured, within the existing 80/64 px peek clearance. Reuse the approved Decoder Cat Flow Neon Walk 2026-10-20 / Loop asset v1 transparent WebM and still without altering artwork, source gait timing or alpha. The one-second native gait repeats during an offscreen-to-offscreen crossing lasting 8–18 seconds, scaled to the lane and cat width. It is a secondary character interlude, not a resource or additional release.

The walking interlude starts only after a visible peek completes its opaque dip. All peek slots are deactivated while the walk crosses; the next visible section then receives the peek. Scrolling the lane out of view ends the walk and returns control to visible peek locations. Inner pages retain the existing three-location peek behavior and primary Curious/Work roles are unchanged. Asset identity, source, limits and checksum are in assets/characters/usage.json. No generation, new engine integration or shared library modification is involved.

## Leftward Home accents

Christopher requested both the platform cluster and the peek above Featured farther left. The wide-screen tagline column now caps at 550 px with a 12 px gap; intermediate layouts reserve a 240 px second column for the 220 px cluster, leaving 20 px on its right. On mobile the cluster aligns to the content’s left edge with an 8 px drift allowance. The Featured peek now uses the shared left-position placement (24 px inset desktop, 12 px mobile). Grid and footer peek positions and the exclusive walking interlude remain unchanged. Preserve heading and platform-label clearance across the full floating cycle.

## Compact platform layout restored

Christopher rejected the surrounding-icon composition because it introduced too much empty space. Restore the compact layout from dd7f502: icons grouped close to the tagline on desktop and left-aligned beneath it on mobile, with the shared 18-second drift. Preserve the left Featured peek and alternating walking interlude. Do not reintroduce reserved rows above and below the heading merely to surround it with platform marks; future refinements should preserve the compact opening.

## More motion inside the compact frame

Christopher requested slightly more icon travel while preserving the compact layout and avoiding extra whitespace. The grid, tagline, orbit region and Featured geometry remain exactly as in the restored compact layout. Keep the 280×144 px wide-screen orbit, 220×136 px intermediate orbit and existing 82 px mobile row. Only the bounded animation paths and timings change.

Use asymmetric vertical travel to let ChatGPT descend within the group and the lower icons rise, with gentle sideways variation. Cycles are 20/22/24 seconds for Claude/ChatGPT/Codex. Mobile increases horizontal travel to ±14 px, with −10/+2 px vertical limits so the labels remain above the walking lane. Asset styling and the existing cat sequence are unchanged. Full conservative envelopes include the actual blue frames and visible labels; they must stay inside the orbit horizontally, clear of the tagline and one another, and above the cat lane.

Before/after measurements at 1920, 1440, 1151, 1150, 1024, 900, 761, 760, 390 and 320 px confirmed identical intro, heading, orbit and Featured boxes, no overflow and all clearance checks passing. Preserve this compact geometry in later motion revisions. Detailed motion limits and asset provenance remain in assets/platforms/usage.json.

## Preferred resource detail format

Christopher explicitly approved the starter prompt page on November 24, 2026 as an easy-access, easy-use format to carry forward. Reuse its structure for future public resource detail pages: descriptive name and practical purpose, supported apps/formats, requirements, concise setup/use steps, the usable content or package, and immediate relevant actions. Keep Copy prompt for text, Download only when an actual file exists, and View source only for a verified public destination. Use the shared generator and resource catalog so this pattern stays consistent.

The page structure can serve prompts, instruction sets and skills without implying that they are the same resource type. A prompt is task input, instructions provide reusable guidance, and a skill packages reusable instructions and any supporting files for a defined task. Label the actual type and adapt the usage steps and actions to its requirements. Approval of the presentation format does not approve publishing a private resource. Retrieval: README’s preferred resource-format link → this section → scripts/build.mjs and the existing task context starter prompt entry in data/resources.json.

## Separate Prompts, Instructions and Skills collections

Christopher requested respective pages after approving the starter prompt’s easy-access format. Main navigation, Home tiles and footer now expose Prompts (/prompts/), Instructions (/instructions/) and Skills (/skills/) alongside Home and About Chris. Shared labels, descriptions and destinations live in data/site.json; one generator template builds the three collections from data/resources.json. The existing prompt is listed under Prompts, keeps its detail URL and original downloadable text, and now has a Prompts breadcrumb and selected navigation. Instructions and Skills remain empty until separately approved resources exist. This supersedes the earlier Skills-only navigation decision. Social destinations, compact Home geometry and cat pacing remain in effect. Work supports both instruction-set and skill empty states without implying a release.

Christopher also requested explicit purpose, expected outcomes and important usage information. Use the shared detail template for all three types, with Purpose, Expected outcomes, supported apps/formats, How to use it, What you need, usable content, relevant actions and material limitations. Purpose is the catalog description; expectedOutcomes, requirements and instructions are required arrays. Outcomes describe what the resource helps produce without promising correctness. Include limitations when they affect use. Copy text labels and feedback adapt to the resource type; if clipboard access stalls, select the content and tell the user how to copy it. Downloads still require an actual file. No new private resources, versions or compatibility claims are introduced.

Retrieval: README navigation/release scope and preferred-format link → this section and Preferred resource detail format → scripts/build.mjs, data/site.json and data/resources.json. Checked six content pages at six desktop/mobile widths, active collection navigation, empty states, old type/category routes, copy feedback/fallback selection and browser Back. The prompt file remains byte-for-byte equal to its approved content.

## Direct resource descriptions and usage

Christopher requested another clarity review because Prompts, Instructions and Skills can be confusing. Lead with the user action and purpose: paste a prompt for a task; save instructions as response rules for a chat or project; add a skill’s saved task steps to an app that supports skills. Acknowledge that all three give an AI directions, rather than presenting them as entirely unrelated. Home tiles and About derive their short explanations from the same collection configuration. Avoid unexplained terms such as task packages and triggers. Do not imply that every AI app supports skills or that saved rules apply outside their stated scope.

Each collection now includes three concise How to use steps from data/site.json. Empty collections state that no resource is available before those steps; the instructions describe what to do when a resource is added. Resource-specific pages must supply the actual supported app, setup location and usage procedure rather than inventing universal installation steps. The starter prompt now explicitly tells users to copy or open the text download, paste it into the assistant’s message box, replace bracketed fields and send it. Its original prompt text and download remain unchanged. Purpose and expected outcomes use plain terms such as message, background and desired answer format.

Current review covered six content pages at six desktop/mobile widths, including 320 px, with readable wraps and no horizontal overflow. Navigation, shared brand styling, compact Home layout, public release scope and cat behavior remain unchanged. Retrieval: README’s preferred resource-format link → these maintenance notes → data/site.json useSteps/descriptions and data/resources.json usage steps.

## Definition-led descriptions

Christopher refined the description preference: lead with a definition, while keeping direct actions in the separate How to use steps. A prompt is a task-request message; instructions are behavior rules within their stated scope; a skill packages reusable task instructions for an app that supports skills, with optional supporting files. Home tiles use short definition phrases, collection introductions use full definitions, and About reuses the same tile descriptions. The starter prompt description now defines it as a reusable message template; its four usage steps and actual downloadable prompt text are unchanged. This supersedes the action-led description wording only, not the requirement for explicit usage guidance. Definitions and usage steps remain in data/site.json and data/resources.json, reached through README’s existing resource-format and wording links.
