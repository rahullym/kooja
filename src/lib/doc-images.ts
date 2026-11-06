import { getSorted } from "./site";

/**
 * Real shop photos for pages built from content documents. Only the photos
 * already on the site are used (service and project images); a section gets
 * one when it links to, or is titled after, that service or project.
 */
export type DocImage = { src?: string; alt?: string; id?: string; [key: string]: unknown };

const norm = (s: string) => s.toLowerCase().replace(/&/g, "and").replace(/colors/g, "colours").replace(/[^a-z0-9]/g, "");

export async function docImageIndex() {
	const [services, projects] = await Promise.all([getSorted("services"), getSorted("projects")]);
	const byUrl = new Map<string, DocImage>();
	const byName = new Map<string, DocImage>();
	const add = (url: string, names: (string | null | undefined)[], image: unknown) => {
		if (!image) return;
		byUrl.set(url, image as DocImage);
		for (const n of names) if (n) byName.set(norm(n), image as DocImage);
	};
	for (const e of services.entries) {
		const d = e.data as { title?: string; nav_label?: string | null; featured_image?: unknown };
		add(`/services/${e.id}`, [d.title, d.nav_label], d.featured_image);
	}
	for (const e of projects.entries) {
		const d = e.data as { title?: string; featured_image?: unknown };
		add(`/projects/${e.id}`, [d.title], d.featured_image);
	}

	return {
		/** First photo for any of these links (absolute koojo URLs are accepted). */
		forLinks(hrefs: string[]) {
			for (const href of hrefs) {
				const path = href.replace(/^https?:\/\/(www\.)?koojopowdercoating\.com/, "").replace(/\/$/, "");
				const hit = byUrl.get(path);
				if (hit) return hit;
			}
			return null;
		},
		/** First project photo whose project name appears in this text. */
		forText(text: string) {
			const n = norm(text);
			for (const [key, image] of byName) if (key.length > 12 && n.includes(key)) return image;
			return null;
		},
		/** Photo for a card or heading named after a service or project. */
		forName(name: string) {
			const n = norm(name);
			if (byName.has(n)) return byName.get(n)!;
			for (const [key, image] of byName) if (key.length > 8 && (n.includes(key) || key.includes(n))) return image;
			return null;
		},
	};
}

