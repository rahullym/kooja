import type { APIRoute } from "astro";
import { getEmDashCollection, getTaxonomyTerms } from "emdash";

/**
 * Replaces EmDash's generated pages sitemap for two reasons: the home entry
 * lives at "/" (not "/home"), and the blog category hubs are taxonomy pages
 * that no collection sitemap would list.
 */
export const GET: APIRoute = async ({ url }) => {
	const [{ entries: pages }, categories] = await Promise.all([
		getEmDashCollection("pages", { limit: 200 }),
		getTaxonomyTerms("category"),
	]);

	const urls = [
		...pages.map((page) => ({
			path: page.id === "home" ? "/" : `/${page.id}`,
			lastmod: page.data.updatedAt,
		})),
		...categories.map((term) => ({ path: `/blog/categories/${term.slug}`, lastmod: null })),
	];

	const body = urls
		.map(({ path, lastmod }) => {
			const mod = lastmod ? `\n    <lastmod>${new Date(lastmod).toISOString()}</lastmod>` : "";
			return `  <url>\n    <loc>${url.origin}${path}</loc>${mod}\n  </url>`;
		})
		.join("\n");

	return new Response(
		`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${body}\n</urlset>\n`,
		{ headers: { "Content-Type": "application/xml; charset=utf-8", "Cache-Control": "public, max-age=3600" } },
	);
};
