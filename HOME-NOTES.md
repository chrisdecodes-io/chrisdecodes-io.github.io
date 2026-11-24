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

## Centered compact Home introduction

Christopher approved centering the tagline and platform marks together within the main content area. The desktop group is capped at 842 px (550 px text + 12 px gap + 280 px icon region) with automatic horizontal margins. Tagline sentences are centered within their text column. Intermediate layouts use the icon region’s actual 220 px width, avoiding an unused right-hand column allowance. Mobile centers the tagline and the icon row below it, retaining the existing 82 px row and 12 px separation.

Before/after measurements at 1920, 1440, 1024, 900, 390 and 320 px showed no added intro height; 900 px became about 10 px shorter through improved wrapping. Full icon travel remains clear of the text, neighboring marks and cat lane. Resource cards and instructions stay left-aligned. The review also fixed a narrow-tablet Home-card title overflow by using one column from 761–899 px; 900 px and wider retain the existing two-column grid. No animation pacing, artwork, resource content or routes change. This supersedes the prior left-aligned Home opening only.

## Cat centered below the tagline

Christopher requested that the secondary cat below the Home tagline be centered beneath the tagline itself. The Featured-edge peek now uses a tagline-aligned slot rather than the old left inset. Its center follows the text column, not the combined text-and-platform group. The walking lane follows the same text-column width and center, so its crossing stays beneath the tagline. Existing 80/64 px vertical clearance, opaque peek dip, alternating playback, source gait and companion artwork remain unchanged. The standing crossing-duration calculation adapts to the shorter lane.

CSS derives these positions from the centered 842 px intro group: the non-text width is 292 px desktop or 232 px intermediate, with a 550/610 px maximum text column; mobile uses the full content width. Update these alignment variables if the intro column geometry changes. Ten-width measurements from 1920 to 320 px, including both breakpoints, confirm zero center error for the peek and walk lane, matching lane/text widths, unchanged intro heights and no overflow. Retrieval remains README → these notes → styles.css feature-peek-wrap/walk-track rules and scripts/build.mjs Home template.

## Confirmed channel links

Christopher authorized replacing the social placeholders and confirmed the Instagram handle chris.decodes. Verified destinations on November 24, 2026: Instagram https://www.instagram.com/chris.decodes/ (Chris Decodes | AI & Tech, currently private); Substack https://substack.com/@chrisdecodes (public Chris Decodes profile, also linked in the Instagram bio); GitHub https://github.com/chrisdecodes-io (existing profile). Use the public Substack profile for the hub; the chrisdecodes.substack.com publication currently presents a private-publication gate. No publication visibility or account settings were changed.

All channel URLs, descriptions, action labels and profile-status labels now live in data/site.json channels. The shared generator uses that configuration for the header, fully linked Home tiles and About channel section. This supersedes the earlier Instagram/Substack Coming soon placeholders. Instagram is labeled Private profile and Substack Public profile so visitors know the destination type. Status labels reflect this review, not automatic monitoring; update them when visibility changes. Keep canonical profile URLs without tracking parameters. README’s Channel links section is the retrieval route to this configuration. The website can serve as the primary Chris Decodes link hub; external profile bios were not edited in this task.

## Name-only matching channel buttons

Christopher requested removal of private/public profile labels and matching blue buttons for Instagram, Substack and GitHub. Header channel links now display only their platform names, with the same brand-blue background, cream lettering, 8 px radius, dark-blue hover and existing keyboard-focus treatment. Narrow-phone padding is reduced equally across all three buttons so labels fit at 320 px. Privacy badges are also removed from Home tiles and About, while their descriptions and Visit actions remain.

Canonical channel URLs are unchanged in data/site.json; statusLabel fields and rendering are removed so old privacy labels cannot reappear. This supersedes the prior status-label presentation, without changing account visibility. The shared header applies the same styling to all three channel links. Home and About were checked at 1920, 1440, 1024, 1023, 900, 390 and 320 px: matched colors/radii/heights, no clipped names, branding overlap or horizontal overflow. Retrieval: README Channel links → data/site.json channels and scripts/build.mjs channelLinks → authoritative styles.css header rules.

## Future affiliate links and brand inquiries

Christopher asked on November 24, 2026 to keep affiliate links and brand-outreach contact information in mind for the established hub. These are recorded future additions, not approved resources, live features, endorsements or outreach messages. Preserve the resource library as the primary experience and the compact Home layout.

Affiliate links: consider a secondary tools/resources area when actual products, destinations and recommendations are approved. Each entry should explain its practical purpose, who it suits and the affiliate relationship beside the relevant link. Do not invent first-hand use, endorsement, partner status or a commission arrangement. Revisit the applicable program and disclosure requirements when there is a concrete proposal.

Brand inquiries: consider a clearly named Brand inquiries or Contact link in About/footer, leading to a designated public business email or an intentionally selected contact form. A media kit can be added when one exists. Christopher must supply or select the public contact destination; do not reuse private account details as published contact information. No account setup or external messaging is authorized by this planning note.

Current hosting decision, confirmed by Christopher on November 24, 2026: keep GitHub Pages for now. The site is an educational resource hub; the contemplated affiliate feature consists of outbound links, with no on-site selling or checkout. No hosting migration is planned. Affiliate links and a brand contact section remain deferred ideas, not instructions to implement them now. This supersedes the earlier recommendation to move hosting before introducing any affiliate links; no provider-policy exception is asserted. Keep the public GitHub Pages site and established maintenance workflow in place. Retrieval: README Future additions → this section.

## Public commit attribution

Christopher confirmed that future commits and similar public attribution should omit his last name. Use Christopher as the Git author and committer display name. This Mac’s global Git name and this repository’s local Git name are set accordingly. This public repository uses the verified chrisdecodes-io account’s ID-based GitHub noreply address for future commits. Do not rewrite existing published history for this preference; Christopher explicitly scoped the change to future commits. On other machines or fresh clones, apply the name preference before committing and check for repository-specific overrides. A synced note does not establish that another machine’s Git configuration has changed.


## Usability review and walking entrance/exit repair, November 24, 2026

Keep the definition-led Home tiles and collection introductions. Show available entries or an honest empty state immediately after the definition, before general usage guidance. Empty Skills and Instructions collections offer Browse prompts and Back to Home. Use “None available yet” in empty Home tiles, without internal release terminology. The starter prompt introduction has a Go to prompt link; its fragment target accepts keyboard focus. Preserve the existing purpose, outcomes, requirements, copy action and verified text download as the pattern for future approved resources.

Supersedes the walking-lane part of “Cat centered below the tagline”: the narrow text-width clip produced an abrupt interior entrance/exit. Keep the peek centered beneath the tagline, but let the walking lane enter at the main-content/sidebar boundary on desktop and the left viewport edge on mobile. Its exit reaches the actual right viewport edge, including outer cream margins on wide displays. The complete cat frame begins outside and finishes outside the lane, so no interior cut happens. Do not let the lane cover sidebar controls.

Measure this lane on load, resize and each crossing. Pause CSS travel until the source video is playing so loading does not consume part of the entrance. Use the track’s visibility to start playback, since the actor intentionally begins offscreen. Pause travel with document visibility. Keep the native one-second approved gait, width-based 8–18-second crossing, silent playback, unchanged vertical clearance and exclusive peek/walk handoff. No character assets were modified.

Recognized legacy category/type links open the matching current collection. Unknown and retired category/project destinations return to Home, where visitors can choose, rather than sending them to an unrelated empty Skills page. Retrieval: README → these notes → scripts/build.mjs, cat-motion.js, styles.css and assets/characters/usage.json.

Verification: six content pages at 1920, 1440, 1024, 900, 390 and 320 px, one H1 and three header channels with no horizontal overflow; collection ordering/empty states; mobile menu; fragment focus, successful Copy prompt feedback and browser Back; compatibility URLs and matching download bytes. Timed desktop and mobile samples show off-lane entry, uninterrupted playback through the right edge, zero active peeks during travel, one after handoff, and the next cycle. See verification.json for the current reviewed scope.


## Instagram-responsive Featured selection, November 24, 2026

Christopher requested that the hub reflect Instagram posting and show the most recent highlight. Keep the compact blue Featured panel, Curious companion, Home tiles and resource pages. Its content now selects the most recent dated confirmed Instagram post or eligible available resource. Instagram wins a same-day tie. Future dates remain hidden until their Pacific publication date.

The explicit Instagram publication list is data/highlights.json, reached through README → Latest highlight → shared page generator. Record only confirmed post/reel links, real dates and approved short copy. This supports a posting-session update and can accept data from a separately approved integration later. It does not create a polling job or authorize private content release. Christopher confirmed that no Instagram posts have been published yet and selected updates when we publish together. Keep the list empty and the starter prompt Featured for now. At a joint Instagram publication, verify its live URL and actual publication date, add approved highlight copy, link any already-released related resource, rebuild/review/push and verify the deployed banner as part of that session. No automatic detection or polling is requested.


## Tagline cat pacing and banner-bound walk, November 24, 2026

Christopher requested a slightly shorter blank hold and sooner arrivals specifically below the tagline, then noted the walker went beyond the website composition. This supersedes the prior viewport-edge walking rule. Fit the walking lane to Featured, keep the entire character frame inside its width, rise from behind its left end and dip behind its right end. CSS translates the opaque figure vertically during the first 10% and final 12%; no fade, artwork change or cropped horizontal exit. Crossing duration is width-based, bounded to 7.5–17 seconds with a slightly quicker translation rate. Hide the inactive track as a whole so video visibility rules cannot leave a duplicate still beside the active peek.

For the Home tagline peek only, play the 49-frame entry at 1.12× and 294 idle frames at 1.18×, saving about 1.5 seconds of idle; restore 1× for the complete opaque dip. The encoded 390-frame source remains unchanged. After walking, return to the tagline peek if visible rather than handing to a barely visible lower section. Scrolling still transfers the peek to the grid/footer. Featured Curious, inner pages, other peek slots, native walking gait, artwork and reserved vertical space remain unchanged.

Review: full desktop and 390 px mobile cycles, ready playback, rise/cross/dip and immediate visible peek return; bounding boxes stay within Featured and the inactive walker is hidden. Generated checks and source-media hashes pass. The publication workflow remains update-together, with no Instagram posts published yet and the starter prompt retained as Featured.


## Straight, matching walking entrance and exit, November 24, 2026

Christopher found the walking rise strange and requested straight entry from one end with a matching exit. This supersedes the vertical rise/dip for the walking interlude only. Retain the Featured-width lane, fixed walking baseline and current timing, but begin the entire frame beyond its left boundary and finish beyond its right. Use identical horizontal masking at both ends, without vertical translation, fade or movement into the page’s outer margins. The separate peeking cat retains its complete physical dip. Artwork, native gait, earlier tagline return and other-page behavior remain unchanged.


## Registered walking ground line and full-cycle review, November 24, 2026

Christopher still saw the walking cat move up and down. The original selected Home tab was using an older stylesheet; refresh that actual tab after deployment instead of only opening a separate proof tab. The current horizontal CSS had no vertical keyframes, but decoded source frames had paw baselines between rows 615 and 621 on the 720 px canvas.

Create a website-only derivative that registers every frame’s opaque paw baseline to row 620 with integer vertical offsets from -1 to +5 source pixels. Preserve shapes, scale, source-frame order, colors, alpha and one-second 30 fps timing. The shared approved library source stays unchanged. No interpolation, warping, new illustration or retiming. Keep the source hash, per-frame offsets and actual encoded-frame measurements in assets/characters/walk-registration.json. Reproduce with scripts/prepare-walk.py and an available ffmpeg binary. The PNG poster comes from the registered first frame.

Retain straight horizontal entry/exit and the Featured-width lane. Derive the bottom offset from the registered visible-pixel boundary (621/720 of the frame), so paws meet the banner to within browser subpixel rounding at both sizes. Use matching 10 px horizontal edge masks to soften the boundary without any rise or dip. The entire frame starts and finishes outside the lane before state handoff. The separate peeking cat is unchanged.

Verification: decode all 30 delivered video frames with libvpx-vp9 and require the same row-620 baseline, zero restart baseline difference and no cropped visible pixels. Observe timed complete desktop and actual 390 px mobile cycles, including entry, exit and restart. Container and video Y stay constant, no CSS transform is present, and no peek is active during walking. Primary characters and inner pages remain unchanged. This supersedes earlier statements that the website walk media was byte-identical to the shared source.


## Larger centered tagline with four flanking icons, November 24, 2026

Christopher requested a larger centered tagline, platform icons on both sides, the Claude Code avatar, preserved peek/tagline alignment, a real GitHub mark in its square, a corrected Instructions tick, and review of header branding alignment. This supersedes the earlier text-and-right-cluster composition and its asymmetric peek offset.

Use the existing WordmarkEditorial serif at up to 48 px, retaining ink then blue and exact wording. Two labeled platform marks sit on each side: Claude/Claude Code on the left and ChatGPT/Codex on the right. Keep the same cream-on-blue tiles, bounded 20–24-second floats and existing shapes; use 5 px travel on desktop and 3 px on mobile to protect text. Scale side marks at phone widths so they stay beside the tagline without extra icon rows. Mobile typography is 32 px, or 30 px below 361 px. Preserve one H1 and one complete tagline.

The Featured-edge peek shares the heading’s centerline at every breakpoint. Walking behavior and the approved registered gait are unchanged. Header CD and wordmark preserve the approved CTA lockup proportions; measurements confirm a common vertical center and zero whole-lockup horizontal centering error, so no artwork or optical distortion is introduced.

Reuse the existing Claude Code pixel avatar vector from Lobe Icons, with source geometry, checksum and license recorded in assets/platforms/usage.json. GitHub reuses the existing local platform mark with native proportions, converted only to cream. Replace the folder pictogram in the GitHub card. Instructions uses one clean blue tick centered within its cream clipboard, without the interfering short list line.

Review: Home at actual 1920, 1440, 1024, 900, 760, 390 and 320 px; heading, peek and header centers match; no horizontal overflow. Conservative full-motion mark/label bounds do not intersect any tagline text line at all seven widths. The header lockup’s square and wordmark vertical centers match. Review the corrected grid icons and keyboard focus. Existing generated-site checks pass; no resource releases or route changes.


## Header branding aligned to the tagline, November 24, 2026

Christopher requested the CD logo and wordmark be centered more closely over the tagline. The approved lockup is now centered over the main content column rather than the entire page. Use half the actual shared sidebar-width token as its offset; when the sidebar collapses at 760 px, remove the offset. Keep the artwork, native proportions and common vertical center unchanged. This supersedes whole-page header centering only.

Move channels to a second row below 1200 px to preserve clearance; while the sidebar remains visible, that row shares the same content centerline. Home stays left aligned. Phone branding and channels use the full page center as before. Apply through the shared header styles across every page. Footer layout is unchanged.

Verification: brand, tagline and peek centerlines match at 1920, 1440, 1280, 1200, 1199, 1024, 900, 761, 760, 390 and 320 px. No overlap with Home or channels and no horizontal overflow. Skills, About and the starter prompt also match the main-column center at 1440, 900 and 390 px, retaining all three channel buttons.


## Freer platform flow within the compact opening, November 24, 2026

Christopher requested more freedom for the icons to flow around the tagline. Expand the former 5/3 px movement bounds without changing the introduction, heading size, icon size, centered header/peek or whitespace. At wide widths, each mark travels up to 32 px toward the tagline and 4 px outward; upper marks rise 14 px, lower marks 5 px, and both settle by up to 3 px. Reverse the lower pair’s path while retaining separate 20/23/22/24-second cycles and staggered phases. Keep the marks upright and source geometry unchanged.

Reduce inward travel to 14 px at intermediate widths, 8 px on phones and 5 px below 361 px. Phones get up to 10 px upper rise, 5 px lower rise and 3 px settling; outward travel is 2 px. Keep Claude Code’s label on one line above 760 px so the wider paths retain clean spacing between icons. Reduced-motion preference still makes these decorative icons static; cat behavior is unchanged.

Review full conservative mark-and-label envelopes, including asymmetric movement on both axes, against every actual tagline line and every neighboring icon at 1920, 1440, 1280, 1151, 1150, 1024, 951, 950, 900, 761, 760, 390, 361, 360 and 320 px. No intersections or horizontal overflow were found. A complete 25-second desktop observation confirms approximately 35–36 px total horizontal travel with visibly different paths; upper marks travel about 17 px vertically and lower marks 8 px. This supersedes the earlier 5/3 px movement limits only.


## Living icon drift and wordmark-first centering, November 24, 2026

Christopher requested more drift, a livelier but calm feel and a less slow pace. Replace the shared multi-stop path with independent eased horizontal and vertical loops. A platform-content wrapper handles the vertical axis while its token handles the horizontal axis. Separate durations and phases prevent every turn from stopping both axes together. Horizontal periods are 18/21/20/23 seconds for Claude/Claude Code/ChatGPT/Codex; vertical periods are 13/16/15/18 seconds. Lower marks reverse the horizontal axis. Keep icons and labels upright, without added glow, scaling or rotation.

Wide bounds extend 64 px inward and 12 px outward, with upper rise/drop 24/8 px and lower rise/drop 10/4 px. Intermediate and phone limits are recorded in assets/platforms/usage.json. Roomier narrow-phone text layouts get more vertical travel; the ChatGPT origin moves 4 px outward below 361 px to retain label clearance. Opening dimensions, whitespace, typography, artwork and cat behavior are unchanged. Decorative reduced-motion preference disables both axes.

Christopher clarified that the Chris Decodes wordmark itself should center over the tagline, with the CD square positioned relative to it. This supersedes centering the combined lockup. Offset the group by half its square-plus-gap width so the wordmark center matches the main-column center; keep the CD on its left above 760 px. At phone widths put the square on the right with the corresponding reversed group offset, preserving room for Home. Native artwork, relative sizes and vertical alignment stay unchanged. Footer layout is unchanged.

Review complete conservative icon/label envelopes at responsive breakpoints from 320 to 1920 px, including 400/401 and 410/411 px text-wrap boundaries. No intersections with text or neighboring icons, Home overlap or horizontal overflow remain. Wordmark/tagline centers differ by less than 0.02 CSS px from rounding. Observe complete desktop cycles and phone pacing: desktop horizontal motion spans about 76 px, with 32 px upper and 14 px lower vertical travel. Maintain source assignments through README and both platform/wordmark usage records.
