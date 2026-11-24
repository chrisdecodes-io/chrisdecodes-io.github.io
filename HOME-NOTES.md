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
