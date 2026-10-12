This is an EmDash site -- a CMS built on Astro with a full admin UI.

## Commands

```bash
pnpm dev              # Start the Astro dev server
npx emdash types      # Regenerate TypeScript types from a running site
```

The admin UI is at `http://localhost:4321/_emdash/admin`.

## Key Files

| File                     | Purpose                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------- |
| `astro.config.mjs`       | Astro config with `emdash()` integration, database, and storage                    |
| `src/live.config.ts`     | EmDash loader registration (boilerplate -- don't modify)                           |
| `seed/seed.json`         | Schema definition + demo content (collections, fields, taxonomies, menus, widgets) |
| `emdash-env.d.ts`        | Generated types for collections (auto-regenerated on dev server start)             |
| `src/layouts/Base.astro` | Base layout with EmDash wiring (menus, search, page contributions)                 |
| `src/pages/`             | Astro pages -- all server-rendered                                                 |

## Skills

Agent skills are in `.agents/skills/`. Load them when working on specific tasks:

- **building-emdash-site** -- Querying content, rendering Portable Text, schema design, seed files, site features (menus, widgets, search, SEO, comments, bylines). Start here.
- **creating-plugins** -- Building EmDash plugins with hooks, storage, admin UI, API routes, and Portable Text block types.
- **emdash-cli** -- CLI commands for content management, seeding, type generation, and visual editing flow.

## Documentation

The EmDash docs are available as an MCP server at `https://docs.emdashcms.com/mcp`. When you need to verify an API, hook, config option, field type, or pattern, call `search_docs` against the live documentation rather than relying on training-data recall. The docs reflect current behaviour; assumptions may not.

This template ships with `.mcp.json`, `.cursor/mcp.json`, and `.vscode/mcp.json` so Claude Code, Cursor, and VS Code auto-discover the docs server. Other tools (OpenCode, Windsurf, etc.) need a manual one-time setup -- see [docs.emdashcms.com/docs-mcp](https://docs.emdashcms.com/docs-mcp).

## Rules

- All content pages must be server-rendered (`output: "server"`). No `getStaticPaths()` for CMS content.
- Image fields are objects (`{ src, alt }`), not strings. Use `<Image image={...} />` from `"emdash/ui"`.
- `entry.id` is the slug (for URLs). `entry.data.id` is the database ULID (for API calls like `getEntryTerms`).
- When Astro's cache is enabled, pass content-query hints to `Astro.cache.set(cacheHint)`. Use the `WithCacheHint` variants for site settings, menus, taxonomies, and widget areas rendered by cached routes.
- Taxonomy names in queries must match the seed's `"name"` field exactly (e.g., `"category"` not `"categories"`).

## This Site

The Koojo Custom Powder Coating website, rebuilt from Wix on Astro + EmDash. The structure follows the 2026 website blueprint: 92 URLs, one primary keyword per page. Existing URLs never change, and blog posts keep the Wix `/post/` path.

## Routes

| URL | Source | Template |
| --- | --- | --- |
| `/` | `pages/home` (blocks) | `src/pages/index.astro` |
| `/about-us`, `/capabilities`, `/certification`, `/privacy-policy` | `pages` | `src/pages/[slug].astro` |
| `/contact-us`, `/get-a-quote` | `pages` | their own files in `src/pages/` |
| `/services`, `/industries`, `/locations` | `pages` entry + child collection | `src/components/HubPage.astro` |
| `/services/*`, `/industries/*`, `/locations/*` | `services`, `industries`, `locations` | `src/components/LandingPage.astro` |
| `/projects`, `/projects/*` | `projects` + `project_category` taxonomy | `src/pages/projects/` |
| `/blog`, `/blog/categories/*`, `/post/*` | `posts` + `category` taxonomy | `src/pages/blog/`, `src/pages/post/` |

Hub pages take their H1, intro, body and FAQ from the `pages` entry with the same slug (`services`, `industries`, `locations`, `projects`, `blog`).

## Schema

- Every collection has `primary_keyword`, `seo_title` and `seo_description`. `entrySeo()` in `src/lib/site.ts` uses the admin SEO panel first, then these fields.
- `services`, `industries` and `locations` share one field set: `title`, `nav_label`, `summary`, `content`, `faqs`, `related`, `sort_order`. Lists are ordered by `sort_order`.
- `related` is a repeater of `{ label, url, kind }` and carries the blueprint's internal-linking rules.
- `posts.published_date` holds the original Wix publish date; posts are ordered by it. `posts.retarget` flags the seven posts that still need a new title, H1 and intro.
- The home page is built from blocks: the template's hero, features, testimonials and FAQ, plus `site_stats`, `site_cards` (cards for every published entry of a collection) and `site_cta`.
- Footer service and location links are read from the collections, so a page appears there when it is published. Wave 2 locations are drafts.

## Seed

`seed/seed.json` is generated. Edit `scripts/seed/content.py` and run `python3 scripts/seed/build.py`; do not edit the JSON by hand. The 33 migrated posts are in `scripts/seed/wix-posts.json` (produced by `wix_posts_to_portable_text.py` from the live site). Collections and menus are applied on first request; content is applied by the setup wizard or `npx emdash seed seed/seed.json`. A seed never overwrites existing data.

## SEO rules (from the blueprint)

- One primary keyword per URL, in the title tag, H1 and first 100 words of that page only.
- City names are primary keywords only under `/locations`. Service and industry pages mention cities in body copy, never in the title or H1.
- Blog posts target how / why / what / vs / cost questions only.
- FAQ questions are written once and never repeated on another page.
- `LocalBusiness` schema goes on the homepage and Contact Us only. Location pages use `Service` with `areaServed`.

## Styling

The look is a shop-floor spec sheet: warm paper, near-black ink, one safety orange, rounded corners (`--radius-*` tokens) and pill buttons, hairline rules, no shadows or icon tiles. Keep it that way.

- Type: Archivo (headings, `--font-display`), IBM Plex Sans (body), IBM Plex Mono (labels, specs, captions; use the `.label` class). Fonts are loaded in `astro.config.mjs`.
- Tokens are overridden in `src/styles/theme.css`; `--color-ink` / `--color-paper` are fixed colours for the dark bands and footer, the rest switch with light and dark mode.
- Sections open with `<header class="section-header" data-label="...">`: mono label on the left, headline on the right, left-aligned. Do not centre section headings.
- Lists of pages are ruled, numbered indexes (`blocks/Cards.astro`), not card grids. Photos are real shop photos; do not add stock images or illustrations.
- Home page blocks also include `site_steps` (numbered process) and `site_swatches` (RAL colour chips).
- Business details (address, phone, hours) are in `src/lib/site.ts`.
