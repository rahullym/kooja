import { getEmDashCollection, getSeoMeta } from "emdash";
import type { AstroGlobal } from "astro";

/**
 * Business details (NAP). Koojo has one address, so LocalBusiness schema is
 * emitted on the homepage and Contact Us only -- never per city.
 */
export const BUSINESS = {
	name: "Koojo Custom Powder Coating",
	street: "10874 Steeles Ave E",
	city: "Milton",
	region: "ON",
	postalCode: "L9T 2X8",
	country: "CA",
	phone: "(905) 876-7060",
	phoneHref: "tel:+19058767060",
	email: "sales@koojopowdercoating.com",
	hours: "Monday to Friday, 7 AM to 5 PM",
	foundingYear: 2012,
	mapUrl: "https://www.google.com/maps/search/?api=1&query=Koojo+Custom+Powder+Coating+10874+Steeles+Ave+E+Milton+ON",
	mapEmbed: "https://www.google.com/maps?q=10874+Steeles+Ave+E,+Milton,+ON+L9T+2X8&output=embed",
} as const;

export type Faq = { question: string; answer: string };
export type RelatedLink = { label: string; url: string; kind?: string | null };
export type Crumb = { label: string; url: string };

type SeoEntry = Parameters<typeof getSeoMeta>[0] & {
	data: { title?: string; seo_title?: string | null; seo_description?: string | null };
};

/**
 * Resolve title/description for a content entry. The SEO panel in the admin
 * wins; otherwise fall back to the seo_title / seo_description fields that
 * carry the keyword map, then to the entry's own title and summary.
 */
export function entrySeo(Astro: AstroGlobal, entry: SeoEntry, path: string, fallbackDescription?: string | null) {
	const seo = getSeoMeta(entry, {
		siteUrl: Astro.url.origin,
		path,
		defaultDescription: entry.data.seo_description || fallbackDescription || undefined,
	});
	const panelTitle = seo.title && seo.title !== entry.data.title ? seo.title : null;
	return {
		title: panelTitle || entry.data.seo_title || entry.data.title,
		description: seo.description,
		image: seo.ogImage,
		canonical: seo.canonical,
		robots: seo.robots,
	};
}

type Sortable = { id: string; data: { sort_order?: number | null } };

export async function getSorted<C extends "services" | "industries" | "locations" | "projects">(collection: C) {
	const result = await getEmDashCollection(collection, { limit: 100 });
	const entries = [...result.entries].sort(
		(a, b) => ((a as Sortable).data.sort_order ?? 999) - ((b as Sortable).data.sort_order ?? 999),
	);
	return { entries, cacheHint: result.cacheHint };
}

export function postDate(data: { published_date?: Date | string | null; publishedAt?: Date | null }) {
	const value = data.published_date ?? data.publishedAt;
	return value ? new Date(value) : null;
}

export function formatDate(date: Date | null) {
	return date ? date.toLocaleDateString("en-CA", { year: "numeric", month: "long", day: "numeric" }) : "";
}

// --- JSON-LD ---------------------------------------------------------------

const postalAddress = {
	"@type": "PostalAddress",
	streetAddress: BUSINESS.street,
	addressLocality: BUSINESS.city,
	addressRegion: BUSINESS.region,
	postalCode: BUSINESS.postalCode,
	addressCountry: BUSINESS.country,
};

const providerRef = (origin: string) => ({ "@type": "LocalBusiness", "@id": `${origin}/#business`, name: BUSINESS.name });

export function localBusinessLd(origin: string) {
	return {
		"@context": "https://schema.org",
		"@type": ["LocalBusiness", "Organization"],
		"@id": `${origin}/#business`,
		name: BUSINESS.name,
		url: `${origin}/`,
		telephone: "+1-905-876-7060",
		email: BUSINESS.email,
		foundingDate: String(BUSINESS.foundingYear),
		address: postalAddress,
		openingHoursSpecification: [
			{
				"@type": "OpeningHoursSpecification",
				dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
				opens: "07:00",
				closes: "17:00",
			},
		],
		areaServed: "Greater Toronto Area",
	};
}

export function faqLd(faqs: Faq[] | null | undefined) {
	if (!faqs?.length) return null;
	return {
		"@context": "https://schema.org",
		"@type": "FAQPage",
		mainEntity: faqs.map((faq) => ({
			"@type": "Question",
			name: faq.question,
			acceptedAnswer: { "@type": "Answer", text: faq.answer },
		})),
	};
}

export function serviceLd(origin: string, opts: { name: string; description?: string | null; url: string; areaServed?: string }) {
	return {
		"@context": "https://schema.org",
		"@type": "Service",
		name: opts.name,
		description: opts.description || undefined,
		url: opts.url,
		provider: providerRef(origin),
		areaServed: opts.areaServed
			? { "@type": "City", name: opts.areaServed }
			: { "@type": "AdministrativeArea", name: "Greater Toronto Area" },
	};
}

export function articleLd(
	origin: string,
	opts: { headline: string; description?: string | null; url: string; image?: string | null; published?: Date | null; modified?: Date | null; author?: string | null },
) {
	return {
		"@context": "https://schema.org",
		"@type": "Article",
		headline: opts.headline,
		description: opts.description || undefined,
		mainEntityOfPage: opts.url,
		image: opts.image ? { "@type": "ImageObject", url: opts.image } : undefined,
		datePublished: opts.published?.toISOString(),
		dateModified: (opts.modified ?? opts.published)?.toISOString(),
		author: { "@type": "Organization", name: opts.author || BUSINESS.name },
		publisher: providerRef(origin),
	};
}

export function collectionLd(opts: { name: string; description?: string | null; url: string; items: { name: string; url: string }[] }) {
	return {
		"@context": "https://schema.org",
		"@type": "CollectionPage",
		name: opts.name,
		description: opts.description || undefined,
		url: opts.url,
		mainEntity: {
			"@type": "ItemList",
			itemListElement: opts.items.map((item, i) => ({ "@type": "ListItem", position: i + 1, name: item.name, url: item.url })),
		},
	};
}

export function breadcrumbLd(origin: string, crumbs: Crumb[]) {
	return {
		"@context": "https://schema.org",
		"@type": "BreadcrumbList",
		itemListElement: crumbs.map((crumb, i) => ({ "@type": "ListItem", position: i + 1, name: crumb.label, item: `${origin}${crumb.url}` })),
	};
}

/**
 * Page copy from the client's content documents is stored as Portable Text
 * with a few custom blocks, so every section stays in the document's order:
 *   koojoByline  - line under the H1 (shown in the hero)
 *   koojoStrip   - trust / spec strip
 *   koojoCards   - card list written in the document
 *   koojoFaq     - FAQ heading, intro and questions, rendered in place
 *   koojoCta     - CTA band text; when it is the last block it fills the page's CTA band
 *   koojoMap     - Google Map slot
 *   koojoForm    - quote request form slot
 *   koojoIntroInBody - marker: show the intro in the body, not the hero
 *   koojoGallery - marker: where a page shows its photo gallery (the page splits its body there)
 *   koojoButtons - button row; `inHero` rows are shown in the page hero
 */
type Block = { _type?: string; [key: string]: unknown };

export type DocButton = { label: string; href: string };
export type DocCta = { heading?: string; text?: string[]; buttons?: DocButton[] };

export function docParts(value: unknown) {
	const blocks = (Array.isArray(value) ? value : []) as Block[];
	const byline = blocks.find((b) => b._type === "koojoByline") as { text?: string } | undefined;
	const last = blocks.at(-1);
	const cta = last?._type === "koojoCta" ? (last as DocCta) : undefined;
	return {
		/** True when the page was built from a content document. */
		fromDoc: blocks.some((b) => typeof b._type === "string" && b._type.startsWith("koojo")),
		byline: byline?.text ?? null,
		/** The intro paragraph is part of the body (the document puts a strip above it). */
		introInBody: blocks.some((b) => b._type === "koojoIntroInBody"),
		hasFaq: blocks.some((b) => b._type === "koojoFaq"),
		hasCards: blocks.some((b) => b._type === "koojoCards"),
		heroButtons: (blocks.find((b) => b._type === "koojoButtons" && b.inHero)?.items as DocButton[] | undefined) ?? null,
		hasForm: blocks.some((b) => b._type === "koojoForm"),
		hasMap: blocks.some((b) => b._type === "koojoMap"),
		cta,
	};
}

/** Anchor id for a heading, so "On this page" links can jump to it. */
export function headingId(text: string) {
	return text
		.toLowerCase()
		.replace(/&/g, "and")
		.replace(/[^a-z0-9]+/g, "-")
		.replace(/^-|-$/g, "")
		.slice(0, 60);
}

