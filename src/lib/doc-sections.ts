/**
 * Splits a page built from a client content document into visual sections,
 * without changing the order or wording of anything in it. Each H2 starts a
 * section; strips, FAQs, inline CTAs and the gallery marker are sections of
 * their own. The layout of a section is chosen from its shape:
 *
 *   strip   - trust / spec strip, shown as a dark proof band
 *   steps   - H3 groups in a process / how-it-works section, numbered
 *   grid    - other H3 groups (services, industries, areas...), shown as cards
 *   quotes  - section with testimonials
 *   text    - everything else
 *   faq / cta / gallery
 */

export type PtBlock = {
	_type?: string;
	_key?: string;
	style?: string;
	listItem?: string;
	children?: { text?: string; marks?: string[] }[];
	markDefs?: { _key: string; _type: string; href?: string }[];
	[key: string]: unknown;
};

export type Group = { heading: PtBlock; blocks: PtBlock[] };

export type Section =
	| { kind: "strip"; block: PtBlock }
	| { kind: "faq"; block: PtBlock }
	| { kind: "cta"; block: PtBlock }
	| { kind: "gallery" }
	| {
			kind: "text" | "grid" | "steps" | "quotes";
			heading: PtBlock | null;
			/** Blocks before the first H3 (or all blocks for text sections). */
			intro: PtBlock[];
			groups: Group[];
			/** Blocks after the last group that are not part of a group (quotes sections only). */
			quotes: PtBlock[];
			outro: PtBlock[];
	  };

/** Blocks that only carry data for the hero / CTA band; they take no space in the body. */
const HIDDEN = new Set(["koojoByline", "koojoIntroInBody"]);

export const blockText = (b: PtBlock) => (b.children ?? []).map((c) => c.text ?? "").join("");

export const blockLinks = (blocks: PtBlock[]) =>
	blocks.flatMap((b) => [
		...(b.markDefs ?? []).map((d) => d.href ?? ""),
		...((b.items as { url?: string }[] | undefined) ?? []).map((i) => i.url ?? ""),
	]);

const STEPS = /process|step|how .*work|how we|how .*made|how to get|quoting|what happens/i;

export function docSections(value: unknown): Section[] {
	const blocks = (Array.isArray(value) ? value : []) as PtBlock[];
	const out: Section[] = [];
	let current: { heading: PtBlock | null; blocks: PtBlock[] } | null = null;

	const flush = () => {
		if (current && (current.heading || current.blocks.length)) {
			out.push(shape(current.heading, current.blocks));
		}
		current = null;
	};

	for (const b of blocks) {
		const t = b._type;
		if (t && HIDDEN.has(t)) continue;
		if (t === "koojoButtons" && b.inHero) continue;
		if (t === "koojoCta" && b.inBand) continue;
		if (t === "koojoStrip") {
			flush();
			out.push({ kind: "strip", block: b });
		} else if (t === "koojoFaq") {
			flush();
			out.push({ kind: "faq", block: b });
		} else if (t === "koojoCta") {
			flush();
			out.push({ kind: "cta", block: b });
		} else if (t === "koojoGallery") {
			flush();
			out.push({ kind: "gallery" });
		} else if (t === "block" && b.style === "h2") {
			flush();
			current = { heading: b, blocks: [] };
		} else {
			current ??= { heading: null, blocks: [] };
			current.blocks.push(b);
		}
	}
	flush();
	return out;
}

function shape(heading: PtBlock | null, blocks: PtBlock[]): Section {
	const isH3 = (b: PtBlock) => b._type === "block" && b.style === "h3";
	const isQuote = (b: PtBlock) => b._type === "block" && b.style === "blockquote";
	const first = blocks.findIndex(isH3);
	const intro = first === -1 ? blocks : blocks.slice(0, first);
	const groups: Group[] = [];
	if (first !== -1) {
		for (const b of blocks.slice(first)) {
			if (isH3(b)) groups.push({ heading: b, blocks: [] });
			else groups.at(-1)!.blocks.push(b);
		}
	}
	const title = heading ? blockText(heading) : "";

	// Short H3 groups read best as cards or steps; long or complex ones stay as text.
	const compact =
		groups.length >= 2 &&
		groups.every((g) => g.blocks.length <= 3 && g.blocks.every((b) => b._type === "block" && !b.listItem && !isQuote(b)));
	if (compact) {
		return { kind: STEPS.test(title) ? "steps" : "grid", heading, intro, groups, quotes: [], outro: [] };
	}

	if (first === -1 && blocks.some(isQuote)) {
		const q0 = blocks.findIndex(isQuote);
		let q1 = q0;
		while (q1 < blocks.length && isQuote(blocks[q1]!)) q1++;
		return {
			kind: "quotes",
			heading,
			intro: blocks.slice(0, q0),
			groups: [],
			quotes: blocks.slice(q0, q1),
			outro: blocks.slice(q1),
		};
	}

	return { kind: "text", heading, intro: blocks, groups: [], quotes: [], outro: [] };
}
