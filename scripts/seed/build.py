"""Build seed/seed.json from content.py and the migrated Wix posts.

Usage: python3 scripts/seed/build.py

The seed is only applied to an empty database, so re-running this does not
touch content that editors have already changed in the admin.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)

import content as C  # noqa: E402

_n = 0


def key(prefix="k"):
	global _n
	_n += 1
	return f"{prefix}{_n}"


LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def spans(text):
	"""Turn 'plain [label](url) plain' into Portable Text children + markDefs."""
	children, defs, pos = [], [], 0
	for m in LINK.finditer(text):
		if m.start() > pos:
			children.append({"_type": "span", "_key": key("s"), "text": text[pos:m.start()], "marks": []})
		k = key("l")
		defs.append({"_type": "link", "_key": k, "href": m.group(2)})
		children.append({"_type": "span", "_key": key("s"), "text": m.group(1), "marks": [k]})
		pos = m.end()
	if pos < len(text):
		children.append({"_type": "span", "_key": key("s"), "text": text[pos:], "marks": []})
	return children, defs


def block(text, style="normal", list_item=None):
	children, defs = spans(text)
	b = {"_type": "block", "_key": key("b"), "style": style, "markDefs": defs, "children": children}
	if list_item:
		b["listItem"] = list_item
		b["level"] = 1
	return b


def portable(body):
	out = []
	for item in body or []:
		if isinstance(item, list):
			out += [block(t, list_item="bullet") for t in item]
		elif item.startswith("### "):
			out.append(block(item[4:], "h3"))
		elif item.startswith("## "):
			out.append(block(item[3:], "h2"))
		else:
			out.append(block(item))
	return out


def faqs(pairs):
	return [{"question": q, "answer": a} for q, a in pairs or []]


def excerpt(text, limit=158):
	text = re.sub(r"\s+", " ", text or "").strip()
	if len(text) <= limit:
		return text
	cut = text[:limit]
	stop = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
	return cut[: stop + 1] if stop > 60 else cut[: cut.rfind(" ")].rstrip(",;:") + "…"


# --- schema ---------------------------------------------------------------

def f(slug, label, type_, **extra):
	return {"slug": slug, "label": label, "type": type_, **extra}


FAQ_FIELD = f("faqs", "FAQs", "repeater", validation={"maxItems": 12, "subFields": [
	f("question", "Question", "string", required=True),
	f("answer", "Answer", "text", required=True),
]})
RELATED_FIELD = f("related", "Related links", "repeater", validation={"maxItems": 8, "subFields": [
	f("label", "Link text", "string", required=True),
	f("url", "URL", "string", required=True),
	f("kind", "Kind", "select", options=["service", "industry", "project", "page"]),
]})
SEO_FIELDS = [
	f("primary_keyword", "Primary keyword (one per page, from the keyword map)", "string"),
	f("seo_title", "SEO title tag", "string"),
	f("seo_description", "Meta description", "text"),
]


def landing_fields(*extra):
	return [
		f("title", "Title (H1)", "string", required=True, searchable=True),
		f("nav_label", "Short label (cards, menus)", "string"),
		f("summary", "Summary (cards and intro)", "text", searchable=True),
		f("featured_image", "Featured image", "image"),
		*extra,
		f("content", "Content", "portableText", searchable=True),
		FAQ_FIELD,
		RELATED_FIELD,
		f("sort_order", "Sort order", "integer"),
		*SEO_FIELDS,
	]


SUPPORTS = ["drafts", "revisions", "preview", "search", "seo"]

PAGE_BLOCKS = ["marketing_hero", "marketing_features", "marketing_testimonials", "marketing_faq", "site_stats", "site_cards", "site_cta", "site_steps", "site_swatches"]

COLLECTIONS = [
	{
		"slug": "pages", "label": "Pages", "labelSingular": "Page", "supports": SUPPORTS, "urlPattern": "/{slug}",
		"fields": [
			f("title", "Title (H1)", "string", required=True, searchable=True),
			f("intro", "Intro", "text", searchable=True),
			f("featured_image", "Featured image", "image"),
			f("body", "Body", "portableText", searchable=True),
			f("content", "Sections", "blocks", validation={"allowedTypes": PAGE_BLOCKS, "maxItems": 20}),
			FAQ_FIELD,
			*SEO_FIELDS,
		],
	},
	{"slug": "services", "label": "Services", "labelSingular": "Service", "supports": SUPPORTS, "urlPattern": "/services/{slug}", "fields": landing_fields()},
	{"slug": "industries", "label": "Industries", "labelSingular": "Industry", "supports": SUPPORTS, "urlPattern": "/industries/{slug}", "fields": landing_fields()},
	{
		"slug": "locations", "label": "Locations", "labelSingular": "Location", "supports": SUPPORTS, "urlPattern": "/locations/{slug}",
		"fields": landing_fields(
			f("city", "City", "string", required=True),
			f("region", "Region", "string"),
			f("wave", "Launch wave", "select", validation={"options": ["1", "2"]}),
			f("drive_time", "Drive time from the Milton shop", "string"),
			f("local_industries", "Local industries served", "text"),
			f("pickup_details", "Pickup and delivery details", "text"),
		),
	},
	{
		"slug": "projects", "label": "Projects", "labelSingular": "Project", "supports": SUPPORTS, "urlPattern": "/projects/{slug}",
		"fields": [
			f("title", "Title (H1)", "string", required=True, searchable=True),
			f("summary", "Summary", "text", searchable=True),
			f("featured_image", "Featured image", "image"),
			f("client_industry", "Client industry", "string"),
			f("part", "Part", "string"),
			f("metal", "Metal", "string"),
			f("size_weight", "Size / weight", "string"),
			f("prep", "Preparation method", "string"),
			f("powder_colour", "Powder type and colour code", "string"),
			f("turnaround", "Turnaround", "string"),
			f("content", "Case study", "portableText", searchable=True),
			f("gallery", "Before / after photos", "repeater", validation={"maxItems": 12, "subFields": [
				f("image", "Image", "image", required=True),
				f("caption", "Caption", "string"),
			]}),
			RELATED_FIELD,
			f("sort_order", "Sort order", "integer"),
			*SEO_FIELDS,
		],
	},
	{
		"slug": "posts", "label": "Blog posts", "labelSingular": "Blog post", "supports": [*SUPPORTS, "scheduling"], "urlPattern": "/post/{slug}",
		"fields": [
			f("title", "Title (H1)", "string", required=True, searchable=True),
			f("excerpt", "Excerpt", "text", searchable=True),
			f("featured_image", "Featured image", "image"),
			f("content", "Content", "portableText", searchable=True),
			FAQ_FIELD,
			f("published_date", "Original publish date", "datetime"),
			f("retarget", "Needs retargeting (new title, H1 and intro for the primary keyword)", "boolean"),
			*SEO_FIELDS,
		],
	},
]


def versioned(slug, label, description, fields, category="Site"):
	return {"slug": slug, "label": label, "description": description, "category": category, "currentVersion": 1, "versions": [{"version": 1, "fields": fields}]}


URL_PATTERN = "^(?:$|(?:https?://|mailto:|tel:|/(?!/)|#).+)$"

NEW_BLOCK_TYPES = [
	versioned("site_stats", "Stats", "A row of headline numbers", [
		f("items", "Stats", "repeater", required=True, validation={"minItems": 1, "maxItems": 6, "subFields": [
			f("value", "Value", "string", required=True),
			f("label", "Label", "string", required=True),
		]}),
	]),
	versioned("site_cards", "Collection cards", "Cards linking to every published service, industry, location or project", [
		f("headline", "Headline", "string"),
		f("subheadline", "Subheadline", "text"),
		f("source", "Show", "select", required=True, validation={"options": ["services", "industries", "locations", "projects"]}),
		f("link_label", "Link label", "string"),
		f("link_url", "Link URL", "string", validation={"pattern": URL_PATTERN}),
	]),
	versioned("site_steps", "Process steps", "A numbered sequence of steps", [
		f("headline", "Headline", "string"),
		f("subheadline", "Subheadline", "text"),
		f("steps", "Steps", "repeater", required=True, validation={"minItems": 1, "maxItems": 9, "subFields": [
			f("title", "Title", "string", required=True),
			f("description", "Description", "text", required=True),
		]}),
	]),
	versioned("site_swatches", "Colour swatches", "A strip of colour chips with their codes", [
		f("headline", "Headline", "string"),
		f("text", "Text", "text"),
		f("link_label", "Link label", "string"),
		f("link_url", "Link URL", "string", validation={"pattern": URL_PATTERN}),
		f("swatches", "Swatches", "repeater", required=True, validation={"minItems": 1, "maxItems": 12, "subFields": [
			f("code", "Code (e.g. RAL 9005)", "string", required=True),
			f("name", "Name", "string", required=True),
			f("hex", "Screen colour (#rrggbb)", "string", required=True),
		]}),
	]),
	versioned("site_cta", "Call to action", "A closing band with one button", [
		f("headline", "Headline", "string", required=True),
		f("text", "Text", "text"),
		f("button_label", "Button label", "string"),
		f("button_url", "Button URL", "string", validation={"pattern": URL_PATTERN}),
	]),
]


# --- content --------------------------------------------------------------

def seo(entry, description=None):
	return {
		"primary_keyword": entry.get("keyword") or None,
		"seo_title": entry.get("seo_title") or None,
		"seo_description": entry.get("seo_description") or description or None,
	}


def clean(data):
	return {k: v for k, v in data.items() if v not in (None, "", [])}


def stamp(blocks):
	return [{"_version": 1, **b} for b in blocks or []]


def build():
	template = json.load(open(os.path.join(HERE, "template-block-types.json"), encoding="utf-8"))
	services = {s["slug"]: s for s in C.SERVICES}
	industries = {i["slug"]: i for i in C.INDUSTRIES}
	projects = {p["slug"]: p for p in C.PROJECTS}

	def link(kind, slug):
		if kind == "service":
			return {"label": services[slug]["nav_label"], "url": f"/services/{slug}", "kind": kind}
		if kind == "industry":
			return {"label": industries[slug]["nav_label"], "url": f"/industries/{slug}", "kind": kind}
		return {"label": projects[slug]["title"], "url": f"/projects/{slug}", "kind": kind}

	out = {"pages": [], "services": [], "industries": [], "locations": [], "projects": [], "posts": []}

	for i, s in enumerate(C.SERVICES):
		related = [link("service", x) for x in s["services"]] + [link("industry", x) for x in s["industries"]]
		if s["project"]:
			related.append(link("project", s["project"]))
		out["services"].append({"id": f"service-{s['slug']}", "slug": s["slug"], "status": "published", "data": clean({
			"title": s["title"], "nav_label": s["nav_label"], "summary": s["summary"], "featured_image": s.get("image"),
			"content": portable(s["body"]), "faqs": faqs(s["faqs"]), "related": related, "sort_order": i + 1, **seo(s, s["summary"]),
		})})

	for i, s in enumerate(C.INDUSTRIES):
		related = [link("service", x) for x in s["services"]] + [link("project", s["project"])]
		related.append({"label": "Capabilities", "url": "/capabilities", "kind": "page"})
		out["industries"].append({"id": f"industry-{s['slug']}", "slug": s["slug"], "status": "published", "data": clean({
			"title": s["title"], "nav_label": s["nav_label"], "summary": s["summary"], "featured_image": s.get("image"),
			"content": portable(s["body"]), "faqs": faqs(s["faqs"]), "related": related, "sort_order": i + 1, **seo(s, s["summary"]),
		})})

	for i, loc in enumerate(C.LOCATIONS):
		city = loc["city"]
		slug = "powder-coating-" + city.lower().replace(" ", "-")
		hq = " (HQ)" if city == "Milton" else ""
		entry = {"keyword": loc.get("keyword") or f"powder coating {city}", "seo_title": loc.get("seo_title") or f"Powder Coating {city} | Koojo Custom Powder Coating", "seo_description": loc.get("seo_description") or loc["summary"]}
		out["locations"].append({"id": f"location-{slug}", "slug": slug, "status": "published" if loc["wave"] == 1 else "draft", "data": clean({
			"title": f"Powder Coating {city}", "nav_label": f"{city}{hq}", "city": city, "region": loc["region"], "wave": str(loc["wave"]),
			"summary": loc["summary"], "content": portable(loc["body"]), "faqs": faqs(loc["faqs"]),
			"related": [link("service", x) for x in C.LOCATION_SERVICES], "sort_order": i + 1, **seo(entry, loc.get("seo_description") or loc["summary"]),
		})})

	for i, p in enumerate(C.PROJECTS):
		entry = {"keyword": p["keyword"], "seo_title": p.get("seo_title") or f"{p['title']} | Powder Coating Case Study | Koojo", "seo_description": p.get("seo_description") or p["summary"]}
		out["projects"].append({"id": f"project-{p['slug']}", "slug": p["slug"], "status": "published", "taxonomies": {"project_category": [p["category"]]}, "data": clean({
			"title": p["title"], "summary": p["summary"], "featured_image": p["image"], "client_industry": p["client_industry"], "part": p["part"],
			"metal": p.get("metal"), "size_weight": p.get("size_weight"), "prep": p.get("prep"), "powder_colour": p.get("powder_colour"), "turnaround": p.get("turnaround"),
			"content": portable(p.get("body")),
			"related": [link("service", p["service"]), link("industry", p["industry"])], "sort_order": i + 1, **seo(entry, p.get("seo_description") or p["summary"]),
		})})

	wix = {p["slug"]: p for p in json.load(open(os.path.join(HERE, "wix-posts.json"), encoding="utf-8"))}
	post_slugs = set(wix) | {n[0] for n in C.NEW_POSTS}

	def fix_href(href):
		"""Old posts link to each other without the /post/ prefix; those 404 on the live site."""
		bare = href.strip("/")
		if href.startswith("/") and "/" not in bare and bare:
			match = [s for s in post_slugs if s == bare or s.startswith(bare + "-")]
			if match:
				return "/post/" + sorted(match, key=len)[0]
		return href

	for slug, cat in C.POST_CATEGORIES.items():
		p = wix[slug]
		for b in p["content"]:
			for d in b.get("markDefs", []):
				d["href"] = fix_href(d["href"])
		desc = excerpt(p["description"])
		data = {
			"title": p["title"], "excerpt": desc, "content": p["content"], "faqs": p["faqs"], "published_date": p["published"],
			"retarget": True if slug in C.RETARGET_POSTS else None,
			"primary_keyword": C.POST_KEYWORDS[slug], "seo_description": desc,
		}
		if p["image"]:
			# Wix transcodes by the requested extension; JPEG is ~10x smaller than the PNG originals.
			name = re.sub(r"[^a-z0-9-]", "", slug)[:60] + ".jpg"
			data["featured_image"] = C.img(p["image"].rsplit("/", 1)[1], p["title"], name)
		out["posts"].append({"id": f"post-{slug}", "slug": slug, "status": "published", "taxonomies": {"category": [cat]}, "bylines": [{"byline": "byline-koojo"}], "data": clean(data)})

	for slug, title, keyword, cat in C.NEW_POSTS:
		out["posts"].append({"id": f"post-{slug}", "slug": slug, "status": "draft", "taxonomies": {"category": [cat]}, "bylines": [{"byline": "byline-koojo"}], "data": {"title": title, "primary_keyword": keyword}})

	privacy = json.load(open(os.path.join(HERE, "wix-privacy-policy.json"), encoding="utf-8"))
	for p in C.PAGES:
		body = privacy if p.get("body") == "WIX:privacy-policy" else portable(p.get("body"))
		out["pages"].append({"id": f"page-{p['slug']}", "slug": p["slug"], "status": "published", "data": clean({
			"title": p["title"], "intro": p.get("intro"), "featured_image": p.get("image"), "body": body,
			"content": stamp(p.get("blocks")), "faqs": faqs(p.get("faqs")), **seo(p, p.get("intro")),
		})})

	keep = {"marketing_hero", "marketing_features", "marketing_testimonials", "marketing_faq"}
	seed = {
		"$schema": "https://emdashcms.com/seed.schema.json",
		"version": "1",
		"meta": {"name": "Koojo Custom Powder Coating", "description": "Site structure and content from the 2026 website blueprint", "author": "Koojo"},
		"settings": C.SETTINGS,
		"blockTypes": [b for b in template if b["slug"] in keep] + NEW_BLOCK_TYPES,
		"collections": COLLECTIONS,
		"taxonomies": [
			{"name": "category", "label": "Blog categories", "labelSingular": "Blog category", "hierarchical": False, "collections": ["posts"],
				"terms": [{"slug": s, "label": l, "description": d} for s, l, _, d in C.BLOG_CATEGORIES]},
			{"name": "project_category", "label": "Project categories", "labelSingular": "Project category", "hierarchical": False, "collections": ["projects"],
				"terms": [{"slug": s, "label": l} for s, l in C.PROJECT_CATEGORIES]},
		],
		"menus": [{"name": m["name"], "label": m["label"], "items": [{"type": "custom", "label": l, "url": u} for l, u in m["items"]]} for m in C.MENUS],
		"redirects": [{"source": s, "destination": d, "type": 301} for s, d in C.REDIRECTS],
		"bylines": [{"id": "byline-koojo", "slug": "koojo-powder-coating", "displayName": "Koojo Powder Coating"}],
		"content": out,
	}
	path = os.path.join(ROOT, "seed", "seed.json")
	json.dump(seed, open(path, "w", encoding="utf-8"), indent="\t", ensure_ascii=False)
	counts = {k: (len(v), sum(1 for e in v if e["status"] == "published")) for k, v in out.items()}
	print(f"wrote {os.path.relpath(path, ROOT)} ({os.path.getsize(path) // 1024} KB)")
	for k, (total, pub) in counts.items():
		print(f"  {k:11} {total:3} entries, {pub:3} published")


if __name__ == "__main__":
	build()
