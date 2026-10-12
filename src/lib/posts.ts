import { getEmDashCollection } from "emdash";
import type { Card } from "../components/CardGrid.astro";
import { formatDate, postDate } from "./site";

/** All published posts, newest first by their original publish date. */
export async function getPosts(category?: string) {
	const result = await getEmDashCollection("posts", {
		limit: 200,
		...(category ? { where: { category } } : {}),
	});
	const entries = [...result.entries].sort(
		(a, b) => (postDate(b.data)?.getTime() ?? 0) - (postDate(a.data)?.getTime() ?? 0),
	);
	return { entries, cacheHint: result.cacheHint };
}

type PostEntry = Awaited<ReturnType<typeof getPosts>>["entries"][number];

export function postCard(entry: PostEntry): Card {
	return {
		title: entry.data.title,
		url: `/post/${entry.id}`,
		text: entry.data.excerpt,
		image: entry.data.featured_image,
		meta: formatDate(postDate(entry.data)),
	};
}

export function postCategory(entry: PostEntry) {
	return entry.data.terms?.category?.[0] ?? null;
}
