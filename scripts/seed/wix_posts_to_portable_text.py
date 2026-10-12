"""Convert downloaded Wix blog post HTML into EmDash seed entries (Portable Text).

Usage: python3 -I scripts/seed/wix_posts_to_portable_text.py <dir-of-post-html> <out.json>
"""
import glob
import json
import os
import re
import sys
from html.parser import HTMLParser

SITE = "https://www.koojopowdercoating.com"
BLOCK_TAGS = {"p": "normal", "h1": "h2", "h2": "h2", "h3": "h3", "h4": "h4", "h5": "h4", "h6": "h4", "li": "normal"}


class BodyParser(HTMLParser):
	def __init__(self):
		super().__init__(convert_charrefs=True)
		self.blocks = []
		self.cur = None
		self.marks = []
		self.lists = []
		self.n = 0

	def key(self, prefix):
		self.n += 1
		return f"{prefix}{self.n}"

	def open_block(self, style, list_item=None):
		self.close_block()
		self.cur = {"_type": "block", "_key": self.key("b"), "style": style, "markDefs": [], "children": []}
		if list_item:
			self.cur["listItem"] = list_item
			self.cur["level"] = max(1, len(self.lists))

	def close_block(self):
		cur, self.cur = self.cur, None
		if not cur:
			return
		# Merge adjacent spans with identical marks, then trim the block edges.
		merged = []
		for span in cur["children"]:
			if merged and merged[-1]["marks"] == span["marks"]:
				merged[-1]["text"] += span["text"]
			else:
				merged.append(span)
		if merged:
			merged[0]["text"] = merged[0]["text"].lstrip()
			merged[-1]["text"] = merged[-1]["text"].rstrip()
		merged = [s for s in merged if s["text"]]
		if not merged:
			return
		used = {m for s in merged for m in s["marks"]}
		cur["markDefs"] = [d for d in cur["markDefs"] if d["_key"] in used]
		cur["children"] = merged
		self.blocks.append(cur)

	def handle_starttag(self, tag, attrs):
		attrs = dict(attrs)
		if tag in ("ul", "ol"):
			self.close_block()
			self.lists.append("bullet" if tag == "ul" else "number")
		elif tag == "li":
			self.open_block("normal", self.lists[-1] if self.lists else "bullet")
		elif tag in BLOCK_TAGS:
			# Wix wraps list text in <p>; keep the list item block open.
			if not (self.cur and self.cur.get("listItem")):
				self.open_block(BLOCK_TAGS[tag])
		elif tag in ("strong", "b"):
			self.marks.append("strong")
		elif tag in ("em", "i"):
			self.marks.append("em")
		elif tag == "a":
			href = (attrs.get("href") or "").strip()
			if href.startswith(SITE):
				href = href[len(SITE):] or "/"
			if href and self.cur is not None:
				k = self.key("l")
				self.cur["markDefs"].append({"_type": "link", "_key": k, "href": href})
				self.marks.append(k)
			else:
				self.marks.append(None)
		elif tag == "br" and self.cur is not None and self.cur["children"]:
			self.text(" ")

	def handle_endtag(self, tag):
		if tag in ("ul", "ol"):
			self.close_block()
			if self.lists:
				self.lists.pop()
		elif tag == "li" or (tag in BLOCK_TAGS and not (self.cur and self.cur.get("listItem"))):
			self.close_block()
		elif tag in ("strong", "b"):
			self.pop("strong")
		elif tag in ("em", "i"):
			self.pop("em")
		elif tag == "a":
			for i in range(len(self.marks) - 1, -1, -1):
				if self.marks[i] not in ("strong", "em"):
					del self.marks[i]
					break

	def pop(self, mark):
		for i in range(len(self.marks) - 1, -1, -1):
			if self.marks[i] == mark:
				del self.marks[i]
				break

	def text(self, data):
		data = re.sub(r"\s+", " ", data.replace(" ", " "))
		if not data or self.cur is None:
			return
		marks = [m for m in dict.fromkeys(self.marks) if m]
		# A heading that is bold throughout does not need the mark.
		if self.cur["style"] != "normal":
			marks = [m for m in marks if m != "strong"]
		self.cur["children"].append({"_type": "span", "_key": self.key("s"), "text": data, "marks": marks})

	def handle_data(self, data):
		self.text(data)


def meta(html, prop):
	m = re.search(r'<meta (?:property|name)="%s" content="([^"]*)"' % re.escape(prop), html)
	return m.group(1).replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"') if m else None


def plain(block):
	return "".join(s["text"] for s in block["children"])


def split_faqs(blocks):
	"""Pull a trailing FAQ section (h2 'FAQ...' + h3 question / paragraph answers) out of the body."""
	for i, b in enumerate(blocks):
		if b["style"] in ("h2", "h3") and re.search(r"\bFAQs?\b|frequently asked", plain(b), re.I):
			faqs, q, a = [], None, []
			for nb in blocks[i + 1:]:
				t = plain(nb)
				is_q = nb["style"] in ("h3", "h4") or (
					nb["style"] == "normal" and t.endswith("?") and all("strong" in s["marks"] for s in nb["children"])
				)
				if nb["style"] == "h2":
					return blocks, []  # another section follows; leave the body untouched
				if is_q:
					if q and a:
						faqs.append({"question": q, "answer": " ".join(a)})
					q, a = re.sub(r"^(Q\d*[:.]|\d+[.)])\s*", "", t), []
				elif q:
					a.append(re.sub(r"^A[:.]\s*", "", t))
			if q and a:
				faqs.append({"question": q, "answer": " ".join(a)})
			# Fewer than three matches means the section is not in the Q/A shape we
			# understand; keep it in the body rather than lose text.
			if len(faqs) >= 3:
				return blocks[:i], faqs
	return blocks, []


def convert(path):
	html = open(path, encoding="utf8", errors="ignore").read()
	slug = os.path.basename(path)[:-5]
	i = html.find('data-hook="post-description"')
	j = html.find("<footer", i)
	parser = BodyParser()
	parser.feed(html[html.find(">", i) + 1:j])
	parser.close_block()
	body, faqs = split_faqs(parser.blocks)
	title = re.search(r'data-hook="post-title">(.*?)</h1>', html, re.S)
	title = re.sub(r"<[^>]+>", "", title.group(1)).strip() if title else slug
	title = title.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
	image = meta(html, "og:image")
	desc = meta(html, "description") or meta(html, "og:description") or ""
	return {
		"slug": slug,
		"title": title,
		"description": desc,
		"image": re.sub(r"/v1/.*$", "", image) if image else None,
		"published": meta(html, "article:published_time"),
		"modified": meta(html, "article:modified_time"),
		"content": body,
		"faqs": faqs,
		"words": sum(len(plain(b).split()) for b in body),
	}


if __name__ == "__main__":
	src, out = sys.argv[1], sys.argv[2]
	posts = [convert(f) for f in sorted(glob.glob(os.path.join(src, "*.html")))]
	json.dump(posts, open(out, "w"), indent=1, ensure_ascii=False)
	for p in posts:
		print(f"{p['slug'][:58]:58} {p['words']:5} words {len(p['content']):3} blocks {len(p['faqs'])} faqs img={'y' if p['image'] else 'n'}")
