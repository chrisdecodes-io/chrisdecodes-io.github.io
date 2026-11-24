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
