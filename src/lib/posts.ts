import { getEmDashCollection } from "emdash";
import type { Card } from "../components/CardGrid.astro";
import { formatDate, postDate } from "./site";

/** Guides shown per page on the blog index and category pages. */
export const POSTS_PER_PAGE = 9;

/** All published posts, newest first by their original publish date. Drafts never appear. */
export async function getPosts(category?: string) {
	const result = await getEmDashCollection("posts", {
		status: "published",
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
		category: postCategory(entry)?.label ?? null,
		cta: "Read more",
		placeholder: true,
	};
}

export function postCategory(entry: PostEntry) {
	return entry.data.terms?.category?.[0] ?? null;
}

export type Paged<T> = { items: T[]; page: number; totalPages: number };

/**
 * Slice a list for the `?page=N` query. Returns null for a page that does not
 * exist (not a number, below 1 or past the end) so the route can 404.
 */
export function paginate<T>(items: T[], pageParam: string | null, perPage = POSTS_PER_PAGE): Paged<T> | null {
	const totalPages = Math.max(1, Math.ceil(items.length / perPage));
	const page = pageParam === null ? 1 : Number(pageParam);
	if (!Number.isInteger(page) || page < 1 || page > totalPages) return null;
	return { items: items.slice((page - 1) * perPage, page * perPage), page, totalPages };
}

/** URL of a page in a paginated list; page 1 is the bare path. */
export function pageUrl(path: string, page: number) {
	return page > 1 ? `${path}?page=${page}` : path;
}

type ImageField = { id?: string; src?: string; meta?: { storageKey?: unknown } | Record<string, unknown> } | null | undefined;

/**
 * Absolute URL for an image field, for og:image. Local uploads carry only a
 * storage key, so resolve it the way EmDash's <Image> does.
 */
export function imageUrl(origin: string, image: ImageField, resolve?: (key: string) => string) {
	if (!image) return null;
	const key = typeof image.meta?.storageKey === "string" ? image.meta.storageKey : null;
	const src =
		image.src ||
		(key ? (resolve ? resolve(key) : `/_emdash/api/media/file/${key}`) : null) ||
		(image.id ? `/_emdash/api/media/file/${image.id}` : null);
	return src ? new URL(src, origin).href : null;
}
