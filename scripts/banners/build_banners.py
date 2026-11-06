"""Draw the page banner illustrations (public/banners/*.svg).

Shop-manual style line drawings in the site's palette: warm paper, ink lines,
one safety orange, a light grid and a spec-sheet title strip. They are
illustrations, never stand-ins for real photos. Run:

    python3 scripts/banners/build_banners.py
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "..", "public", "banners")

W, H = 1200, 900
PAPER = "#f4f2ed"
GRID = "#e4dfd5"
INK = "#161412"
MUTED = "#8a837a"
ORANGE = "#c8400a"
SOFT = "#ebe8e1"
MONO = "IBM Plex Mono, ui-monospace, monospace"


def esc(s):
	return s.replace("&", "&amp;").replace("<", "&lt;")


def line(x1, y1, x2, y2, w=6, c=INK, dash=None, cap="round"):
	d = f' stroke-dasharray="{dash}"' if dash else ""
	return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="{cap}"{d}/>'


def rect(x, y, w, h, sw=6, c=INK, fill="none", r=0, dash=None):
	d = f' stroke-dasharray="{dash}"' if dash else ""
	return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{c}" stroke-width="{sw}"{d}/>'


def circle(cx, cy, r, sw=6, c=INK, fill="none"):
	return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>'


def path(d, sw=6, c=INK, fill="none", dash=None):
	da = f' stroke-dasharray="{dash}"' if dash else ""
	return f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}/>'


def text(x, y, s, size=22, c=INK, anchor="start", weight=500, spacing=3):
	return (f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" font-weight="{weight}" '
		f'letter-spacing="{spacing}" fill="{c}" text-anchor="{anchor}">{esc(s.upper())}</text>')


def dim(x1, y, x2, label):
	"""Horizontal dimension line with end ticks and a label."""
	return "".join([
		line(x1, y, x2, y, 2, MUTED),
		line(x1, y - 14, x1, y + 14, 2, MUTED),
		line(x2, y - 14, x2, y + 14, 2, MUTED),
		f'<rect x="{(x1 + x2) / 2 - 70}" y="{y - 18}" width="140" height="36" fill="{PAPER}"/>',
		text((x1 + x2) / 2, y + 8, label, 22, INK, "middle", 600),
	])


def frame(body, label, fig):
	grid = "".join(line(x, 0, x, H, 1, GRID, cap="butt") for x in range(0, W + 1, 60))
	grid += "".join(line(0, y, W, y, 1, GRID, cap="butt") for y in range(0, H + 1, 60))
	ticks = "".join([
		path("M60 110 V60 H110", 3), path(f"M{W - 110} 60 H{W - 60} V110", 3),
		path(f"M60 {H - 170} V{H - 120} H110", 3), path(f"M{W - 110} {H - 120} H{W - 60} V{H - 170}", 3),
	])
	strip = "".join([
		line(60, H - 90, W - 60, H - 90, 2),
		circle(76, H - 52, 8, 0, ORANGE, ORANGE),
		text(98, H - 44, f"Koojo  /  {label}", 22, INK, "start", 600),
		text(W - 60, H - 44, fig, 22, MUTED, "end"),
	])
	return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)}">'
		f'<rect width="{W}" height="{H}" fill="{PAPER}"/>{grid}{ticks}<g>{body}</g>{strip}</svg>')


# ---------------------------------------------------------------- motifs

def hooks(x1, x2, y, n, drop=60):
	out = [line(x1 - 40, y, x2 + 40, y, 5)]
	step = (x2 - x1) / max(n - 1, 1)
	for i in range(n):
		x = x1 + i * step
		out.append(path(f"M{x} {y} v{drop - 18} q0 18 -14 18", 4))
	return "".join(out)


def box_frame(x, y, w, h, depth=(90, -60), braces=True, coat=True):
	"""Welded frame drawn in oblique projection."""
	dx, dy = depth
	out = [rect(x + dx, y + dy, w, h, 6, MUTED)]
	out.append(rect(x, y, w, h, 7))
	for px, py in [(x, y), (x + w, y), (x, y + h), (x + w, y + h)]:
		out.append(line(px, py, px + dx, py + dy, 6))
	if braces:
		out.append(line(x, y + h, x + w / 2, y, 5))
		out.append(line(x + w / 2, y, x + w, y + h, 5))
	if coat:
		out.append(line(x + 6, y, x + w - 6, y, 12, ORANGE))
	return "".join(out)


def m_truss():
	body = hooks(330, 870, 190, 4)
	body += box_frame(260, 300, 620, 300)
	body += line(260, 450, 880, 450, 5)
	for i in range(5):
		cx = 320 + i * 125
		body += circle(cx, 450, 7, 0, ORANGE, ORANGE)
	body += dim(260, 680, 880, "welded frame")
	return body


def m_conveyor():
	body = box_frame(200, 300, 760, 170, (70, -50), braces=False)
	for i in range(7):
		cx = 250 + i * 110
		body += circle(cx, 385, 34, 5)
		body += circle(cx, 385, 6, 0, ORANGE, ORANGE)
	for x in (230, 520, 810):
		body += line(x, 470, x, 620, 7) + line(x - 40, 620, x + 40, 620, 7)
	body += line(200, 300, 960, 300, 12, ORANGE)
	body += dim(200, 690, 960, "conveyor frame")
	return body


def m_skid():
	body = box_frame(280, 330, 560, 260, (80, -60))
	for x in (330, 500, 670, 790):
		body += path(f"M{x} 220 q-14 26 0 40 q14 -14 0 -40", 4, ORANGE, ORANGE)
	body += line(240, 640, 960, 640, 4, MUTED, "2 14")
	body += dim(280, 700, 840, "line frame")
	return body


def m_bracket():
	body = rect(280, 230, 640, 380, 7, INK, SOFT, 18)
	for i, (cx, cy) in enumerate([(360, 310), (840, 310), (360, 530), (840, 530), (600, 420)]):
		body += circle(cx, cy, 34, 6)
		body += circle(cx, cy, 20, 0, ORANGE, ORANGE) if i < 4 else circle(cx, cy, 60, 6)
	body += line(560, 420, 640, 420, 4, MUTED) + line(600, 380, 600, 460, 4, MUTED)
	body += text(600, 680, "masked threads + bore", 24, INK, "middle", 600)
	return body


def m_stairs():
	"""Stair stringer with posts and a coated handrail."""
	run, rise, base_x, base_y, steps = 100, 56, 230, 650, 7
	pts = [f"M{base_x} {base_y}"]
	x, y = base_x, base_y
	for _ in range(steps):
		y -= rise
		pts.append(f"L{x} {y}")
		x += run
		pts.append(f"L{x} {y}")
	body = path(" ".join(pts), 7)
	body += line(base_x, base_y, base_x + run * steps, base_y - rise * steps, 6, MUTED)
	post = 150
	tops = []
	for i in range(steps):
		px = base_x + 40 + i * run
		py = base_y - rise * (i + 1)
		body += line(px, py, px, py - post, 5)
		tops.append((px, py - post))
	(x1, y1), (x2, y2) = tops[0], tops[-1]
	body += line(x1 - 30, y1 + 17, x2 + 30, y2 - 17, 10, ORANGE)  # handrail
	return body


def m_wheel(tread=False):
	cx, cy, r = 600, 420, 230
	body = circle(cx, cy, r, 8)
	body += circle(cx, cy, r - 34, 12, ORANGE)
	body += circle(cx, cy, 60, 7) + circle(cx, cy, 14, 0, INK, INK)
	for k in range(5):
		a = math.radians(k * 72 - 90)
		for off in (-0.12, 0.12):
			x1, y1 = cx + 62 * math.cos(a + off * 2), cy + 62 * math.sin(a + off * 2)
			x2, y2 = cx + (r - 50) * math.cos(a + off), cy + (r - 50) * math.sin(a + off)
			body += line(x1, y1, x2, y2, 6)
	if tread:
		for k in range(36):
			a = math.radians(k * 10)
			body += line(cx + r * math.cos(a), cy + r * math.sin(a), cx + (r + 26) * math.cos(a + 0.05), cy + (r + 26) * math.sin(a + 0.05), 6)
	return body


def m_bollards():
	body = line(160, 640, 1040, 640, 5)
	for i, x in enumerate((300, 600, 900)):
		body += rect(x - 55, 260, 110, 380, 7, INK, SOFT, 50)
		body += line(x - 52, 360, x + 52, 360, 16, ORANGE, cap="butt")
		body += line(x - 52, 400, x + 52, 400, 16, ORANGE, cap="butt")
		body += line(x - 80, 640, x + 80, 640, 10)
	body += text(600, 700, "site protection posts", 24, INK, "middle", 600)
	return body


def m_gate():
	body = path("M260 640 V320 Q600 120 940 320 V640", 8)
	for i in range(9):
		x = 300 + i * 75
		top = 320 - 120 * math.sin(math.pi * (x - 260) / 680)
		body += line(x, 640, x, top + 30, 5)
		body += circle(x, top + 10, 12, 0, ORANGE, ORANGE)
	for x in (390, 600, 810):
		body += path(f"M{x - 50} 520 q50 -70 100 0 q-50 70 -100 0", 4)
	body += line(240, 640, 960, 640, 8)
	return body


def m_oven():
	body = rect(180, 250, 840, 330, 8, INK, SOFT, 12)
	body += rect(200, 270, 120, 290, 5)
	body += line(300, 400, 300, 430, 6)
	body += box_frame(420, 360, 420, 150, (50, -36), coat=False)
	for x in (480, 640, 800):
		body += path(f"M{x} 300 q-16 -20 0 -40 q16 -20 0 -40", 5, ORANGE)
	body += dim(180, 640, 1020, "23 ft")
	body += text(600, 712, "up to 6,000 lb", 24, INK, "middle", 600)
	return body


def m_spray():
	body = path("M220 470 h120 l40 -40 h80 v80 h-80 l-40 -40", 7)
	body += path("M300 470 v120 h50 v-90", 7)
	body += line(460, 470, 520, 470, 7)
	for i in range(60):
		a = math.radians(-22 + (i * 37 % 44))
		d = 60 + (i * 53 % 260)
		body += circle(520 + d * math.cos(a), 470 + d * math.sin(a), 5 if i % 3 else 7, 0, ORANGE, ORANGE)
	body += rect(840, 300, 140, 340, 7, INK, SOFT, 10)
	body += line(846, 300, 846, 640, 14, ORANGE, cap="butt")
	body += hooks(910, 910, 200, 1, 100)
	return body


def m_gauge():
	cx, cy = 520, 430
	body = circle(cx, cy, 220, 8) + circle(cx, cy, 190, 3, MUTED)
	for k in range(11):
		a = math.radians(150 + k * 24)
		body += line(cx + 160 * math.cos(a), cy + 160 * math.sin(a), cx + 188 * math.cos(a), cy + 188 * math.sin(a), 5)
	a = math.radians(150 + 6.5 * 24)
	body += line(cx, cy, cx + 150 * math.cos(a), cy + 150 * math.sin(a), 8, ORANGE)
	body += circle(cx, cy, 16, 0, INK, INK)
	body += text(cx, cy + 110, "dft  mils", 26, INK, "middle", 600)
	body += circle(860, 300, 90, 7) + path("M815 300 l32 32 l60 -66", 12, ORANGE)
	body += rect(790, 470, 150, 190, 6, INK, SOFT, 8)
	for y in (520, 560, 600):
		body += line(815, y, 915, y, 4, MUTED)
	return body


def m_quote():
	body = rect(300, 180, 460, 520, 8, INK, SOFT, 16)
	body += rect(440, 150, 180, 60, 7, INK, PAPER, 10)
	for i, y in enumerate((280, 340, 400, 460, 520)):
		body += rect(340, y - 18, 30, 30, 5)
		if i < 3:
			body += path(f"M344 {y - 4} l10 10 l18 -22", 6, ORANGE)
		body += line(400, y, 700, y, 5, MUTED)
	body += line(400, 620, 600, 620, 7)
	body += rect(800, 260, 70, 420, 6)
	for i in range(14):
		y = 280 + i * 28
		body += line(800, y, 800 + (34 if i % 2 else 22), y, 4)
	return body


def m_shield():
	body = path("M600 170 L820 250 V430 Q820 600 600 690 Q380 600 380 430 V250 Z", 9, INK, SOFT)
	body += rect(530, 420, 140, 120, 8, INK, PAPER, 14)
	body += path("M560 420 V380 Q560 330 600 330 Q640 330 640 380 V420", 8)
	body += circle(600, 470, 12, 0, ORANGE, ORANGE) + line(600, 470, 600, 505, 8, ORANGE)
	return body


def m_shop(pin=False):
	body = path("M180 640 V340 L420 230 L660 340 V640", 8)
	body += rect(660, 340, 380, 300, 8)
	body += rect(720, 420, 260, 220, 6, INK, SOFT)
	for y in range(450, 640, 30):
		body += line(726, y, 974, y, 3, MUTED)
	body += rect(250, 470, 120, 170, 6) + rect(460, 400, 130, 90, 6)
	body += rect(700, 360, 300, 44, 0, ORANGE, ORANGE, 6)
	body += text(850, 391, "koojo", 26, PAPER, "middle", 700, 6)
	body += line(140, 640, 1080, 640, 6)
	if pin:
		body += path("M300 200 c-40 0 -60 30 -60 60 c0 50 60 100 60 100 c0 0 60 -50 60 -100 c0 -30 -20 -60 -60 -60 z", 6, ORANGE, ORANGE)
		body += circle(300, 260, 18, 0, PAPER, PAPER)
	return body


def m_book():
	body = path("M600 260 Q480 200 280 230 V640 Q480 610 600 670 Q720 610 920 640 V230 Q720 200 600 260 Z", 8, INK, SOFT)
	body += line(600, 260, 600, 670, 6)
	for i, y in enumerate((320, 380, 440, 500, 560)):
		body += line(330, y - 6 * (i % 2), 550, y, 4, MUTED)
	for i, c in enumerate((INK, ORANGE, MUTED, "#2f6f8f")):
		body += rect(660 + (i % 2) * 120, 320 + (i // 2) * 130, 100, 100, 0, c, c, 10)
	return body


# ---------------------------------------------------------------- maps

# Rough positions on the map, relative to the Milton shop.
CITIES = {
	"Milton": (600, 430), "Halton Hills": (540, 300), "Brampton": (760, 290), "Mississauga": (820, 430),
	"Oakville": (720, 560), "Burlington": (590, 610), "Hamilton": (430, 660), "Guelph": (320, 330), "Cambridge": (250, 520),
}


def m_map(focus=None):
	body = path("M820 760 Q900 640 1140 600 V840 H820 Z", 0, SOFT, SOFT)
	body += text(1000, 760, "lake ontario", 20, MUTED, "middle")
	body += path("M120 470 Q400 420 600 430 Q850 440 1100 330", 10, MUTED)  # 401
	body += path("M160 600 Q420 540 600 470 Q820 390 1100 400", 6, MUTED, dash="2 16")  # 407
	body += text(1070, 315, "401", 20, MUTED, "end")
	body += text(1080, 385, "407", 20, MUTED, "end")
	mx, my = CITIES["Milton"]
	names = [focus] if focus and focus != "Milton" else [c for c in CITIES if c != "Milton"]
	for name in names:
		x, y = CITIES[name]
		body += line(mx, my, x, y, 5, ORANGE, "14 12")
	for name, (x, y) in CITIES.items():
		if name == "Milton":
			continue
		on = focus in (None, name) or focus == "Milton"
		body += circle(x, y, 13 if on else 8, 0, ORANGE if on else MUTED, ORANGE if on else MUTED)
		w = len(name) * (14 if on else 11) + 16
		body += f'<rect x="{x - w / 2}" y="{y - 50}" width="{w}" height="32" rx="4" fill="{PAPER}"/>'
		body += text(x, y - 26, name, 20 if on else 16, INK if on else MUTED, "middle", 600 if on else 500)
	body += rect(mx - 22, my - 22, 44, 44, 0, INK, INK, 6)
	body += f'<rect x="{mx - 110}" y="{my + 32}" width="220" height="34" rx="4" fill="{PAPER}"/>'
	body += text(mx, my + 56, "koojo · milton", 20, INK, "middle", 700)
	return body


# ---------------------------------------------------------------- pages

BANNERS = {
	# standalone pages
	"about-us": ("About Koojo", m_shop()),
	"contact-us": ("Contact", m_shop(pin=True)),
	"get-a-quote": ("Request a quote", m_quote()),
	"capabilities": ("Large part capacity", m_oven()),
	"certification": ("Quality assurance", m_gauge()),
	"privacy-policy": ("Privacy", m_shield()),
	"blog": ("Powder coating guides", m_book()),
	# hubs
	"services": ("Services", m_spray()),
	"industries": ("Industries", m_truss()),
	"locations": ("Service areas", m_map()),
	"projects": ("Our work", m_gate()),
	# industries
	"industry-metal-fabricators-welding-shops": ("Metal fabricators", m_truss()),
	"industry-manufacturing-automation": ("Manufacturing", m_conveyor()),
	"industry-machine-shops": ("Machine shops", m_bracket()),
	"industry-contractors-construction": ("Contractors", m_stairs()),
	"industry-food-processing-equipment": ("Food processing", m_skid()),
	"industry-agricultural-heavy-equipment": ("Heavy equipment", m_wheel(tread=True)),
	"industry-municipal-institutional": ("Municipal", m_bollards()),
}
for city in CITIES:
	BANNERS["location-" + city.lower().replace(" ", "-")] = (f"Powder coating {city}", m_map(city))


def main():
	os.makedirs(OUT, exist_ok=True)
	for i, (name, (label, body)) in enumerate(BANNERS.items(), 1):
		with open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8") as f:
			f.write(frame(body, label, f"fig. {i:02d}"))
	print(f"wrote {len(BANNERS)} banners to {os.path.relpath(OUT)}")


if __name__ == "__main__":
	main()
