# Koojo Custom Powder Coating

The koojopowdercoating.com website, built with [Astro](https://astro.build) and [EmDash CMS](https://emdashcms.com). It replaces the previous Wix site and follows the 2026 website blueprint (92 URLs, one primary keyword per page).

## Getting started

```bash
pnpm install
pnpm dev
```

Open the admin at `/_emdash/admin` and complete the setup wizard. It creates your admin account and loads the site content from `seed/seed.json`. The dev server prints the port it is using (4321 by default).

## Content

Everything on the site is editable in the admin: pages, services, industries, locations, projects and blog posts. See `AGENTS.md` for how URLs map to collections and templates.

The starting content is generated from `scripts/seed/content.py`:

```bash
python3 scripts/seed/build.py     # rewrites seed/seed.json
npx emdash seed seed/seed.json    # applies it to an empty local database
```

## Infrastructure

Local development uses SQLite (`data.db`) and a local `uploads/` folder. Production hosting is not configured yet.
