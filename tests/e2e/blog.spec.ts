import { expect, test, type Page } from "@playwright/test";

// The seed has 33 published posts and 8 drafts; nine guides per page.
const DRAFT_SLUG = "how-much-does-powder-coating-cost-ontario";
const VIEWPORTS = [
	{ name: "mobile", width: 375, height: 812 },
	{ name: "tablet", width: 768, height: 1024 },
	{ name: "desktop", width: 1440, height: 900 },
];

const meta = (page: Page, attr: "name" | "property", key: string) =>
	page.locator(`head meta[${attr}="${key}"]`).getAttribute("content");

async function firstPostUrl(page: Page) {
	await page.goto("/blog");
	const href = await page.locator(".all-guides .card-link").first().getAttribute("href");
	expect(href).toMatch(/^\/post\/[a-z0-9-]+$/);
	return href!;
}

async function expectNoHorizontalOverflow(page: Page) {
	const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
	expect(overflow).toBeLessThanOrEqual(0);
}

test.describe("navigation", () => {
	for (const vp of VIEWPORTS) {
		test(`header Blog link works on ${vp.name}`, async ({ page }) => {
			await page.setViewportSize(vp);
			await page.goto("/");
			const link = page.locator(".site-header .nav-links a", { hasText: /^Blog$/ });
			await expect(link).toHaveCount(1);
			await link.scrollIntoViewIfNeeded();
			await expect(link).toBeVisible();
			await link.click();
			await expect(page).toHaveURL(/\/blog$/);
			await expect(page.locator("h1")).toBeVisible();
			await expect(page.locator(".site-header .nav-links a", { hasText: /^Blog$/ })).toHaveAttribute("aria-current", "page");
		});
	}

	test("footer Company column links to the blog", async ({ page }) => {
		await page.goto("/contact-us");
		const column = page.locator(".footer-col", { has: page.locator("h4", { hasText: "Company" }) });
		const link = column.locator("a", { hasText: /^Blog$/ });
		await expect(link).toHaveCount(1);
		await link.click();
		await expect(page).toHaveURL(/\/blog$/);
	});

	test("/blogs and /blogs/<slug> redirect to the blog", async ({ page, request }) => {
		const res = await request.get("/blogs", { maxRedirects: 0 });
		expect(res.status()).toBe(301);
		expect(res.headers().location).toMatch(/\/blog$/);
		const post = await firstPostUrl(page);
		const slug = post.split("/").pop();
		await page.goto(`/blogs/${slug}`);
		await expect(page).toHaveURL(new RegExp(`/post/${slug}$`));
	});
});

test.describe("blog listing", () => {
	test("lists published posts as cards with image, category, date, excerpt and Read more", async ({ page }) => {
		const res = await page.goto("/blog");
		expect(res?.status()).toBe(200);
		const cards = page.locator(".all-guides .card");
		await expect(cards).toHaveCount(9);
		for (const card of await cards.all()) {
			await expect(card.locator(".card-media img, .card-placeholder")).toHaveCount(1);
			await expect(card.locator(".card-category")).not.toBeEmpty();
			await expect(card.locator(".card-meta")).toContainText(/\d{4}/);
			await expect(card.locator(".card-title a")).not.toBeEmpty();
			await expect(card.locator(".card-text")).not.toBeEmpty();
			await expect(card.locator(".card-cta")).toHaveText(/Read more/);
		}
		const img = cards.first().locator(".card-media img");
		await expect(img).toHaveAttribute("srcset", /\d+w/);
		await expect(img).toHaveAttribute("width", /\d+/);
		await expect(img).toHaveAttribute("loading", "lazy");
		// Images actually load from the media endpoint.
		await img.scrollIntoViewIfNeeded();
		await expect.poll(() => img.evaluate((el: HTMLImageElement) => el.complete && el.naturalWidth > 0)).toBe(true);
	});

	test("paginates nine guides per page", async ({ page }) => {
		await page.goto("/blog");
		const pager = page.getByRole("navigation", { name: "Blog pages" });
		await expect(pager).toBeVisible();
		const firstPageSlugs = await page.locator(".all-guides .card-link").evaluateAll((els) => els.map((el) => el.getAttribute("href")));
		await pager.locator('a[rel="next"]').click();
		await expect(page).toHaveURL(/\/blog\?page=2$/);
		await expect(page.locator(".all-guides .card")).toHaveCount(9);
		const secondPageSlugs = await page.locator(".all-guides .card-link").evaluateAll((els) => els.map((el) => el.getAttribute("href")));
		expect(secondPageSlugs.some((href) => firstPageSlugs.includes(href))).toBe(false);
		await expect(page).toHaveTitle(/Page 2/);
		await expect(page.locator('link[rel="canonical"]')).toHaveAttribute("href", /\/blog\?page=2$/);

		await page.goto("/blog?page=4");
		await expect(page.locator(".all-guides .card")).toHaveCount(6);
		await expect(page.getByRole("navigation", { name: "Blog pages" }).locator('a[rel="next"]')).toHaveCount(0);

		const missing = await page.goto("/blog?page=99");
		expect(missing?.status()).toBe(404);
	});

	test("category pages list and paginate their guides", async ({ page }) => {
		await page.goto("/blog");
		const topic = page.locator(".topics a").first();
		const href = await topic.getAttribute("href");
		const res = await page.goto(href!);
		expect(res?.status()).toBe(200);
		expect(await page.locator(".card").count()).toBeGreaterThan(0);
		expect(await page.locator(".card").count()).toBeLessThanOrEqual(9);
	});

	test("draft posts are not listed and do not resolve", async ({ page, request }) => {
		let listed = 0;
		for (let n = 1; n <= 4; n++) {
			await page.goto(`/blog?page=${n}`);
			await expect(page.locator(`.card a[href="/post/${DRAFT_SLUG}"]`)).toHaveCount(0);
			listed += await page.locator(".all-guides .card").count();
		}
		// 33 published posts; the 8 drafts in the seed are left out.
		expect(listed).toBe(33);
		const res = await request.get(`/post/${DRAFT_SLUG}`);
		expect(res.status()).toBe(404);
	});
});

test.describe("article detail", () => {
	test("every card on the first page opens its article without a 404", async ({ page, request }) => {
		await page.goto("/blog");
		const hrefs = await page.locator(".card-link").evaluateAll((els) => [...new Set(els.map((el) => el.getAttribute("href")))]);
		expect(hrefs.length).toBeGreaterThan(9);
		for (const href of hrefs) {
			const res = await request.get(href!);
			expect(res.status(), href!).toBe(200);
		}
	});

	test("clicking a card and Read more opens the full article layout", async ({ page }) => {
		await page.goto("/blog");
		const card = page.locator(".all-guides .card").first();
		const title = (await card.locator(".card-title").innerText()).trim();
		await card.locator(".card-cta").click();
		await expect(page).toHaveURL(/\/post\/[a-z0-9-]+$/);
		await expect(page.locator("h1")).toHaveText(title);
		await expect(page.locator(".post-image img")).toBeVisible();
		await expect(page.locator(".byline-author")).toContainText("By ");
		await expect(page.locator(".byline time")).toHaveAttribute("datetime", /^\d{4}-\d{2}-\d{2}T/);
		const body = page.locator(".post-body .prose");
		await expect(body).toBeVisible();
		expect(await body.locator("p").count()).toBeGreaterThan(1);
		expect(await body.locator("h2, h3").count()).toBeGreaterThan(0);

		const share = page.getByRole("navigation", { name: "Share this article" });
		const encodedPath = encodeURIComponent(new URL(page.url()).pathname);
		for (const network of ["linkedin", "facebook", "x", "email"]) {
			const shareHref = await share.locator(`a[data-share="${network}"]`).getAttribute("href");
			expect(shareHref, network).toContain(encodedPath);
		}
	});
});

test.describe("responsive layout", () => {
	for (const vp of VIEWPORTS) {
		test(`blog listing and article fit a ${vp.name} screen`, async ({ page }) => {
			await page.setViewportSize(vp);
			await page.goto("/blog");
			await expectNoHorizontalOverflow(page);
			const columns = await page
				.locator(".all-guides .card-grid")
				.evaluate((el) => getComputedStyle(el).gridTemplateColumns.split(" ").length);
			expect(columns).toBe(vp.width <= 600 ? 1 : vp.width <= 1024 ? 2 : 3);
			const cardImg = page.locator(".all-guides .card-media img").first();
			const imgBox = await cardImg.boundingBox();
			const cardBox = await page.locator(".all-guides .card").first().boundingBox();
			expect(imgBox!.width).toBeLessThanOrEqual(cardBox!.width + 1);

			const post = await page.locator(".all-guides .card-link").first().getAttribute("href");
			await page.goto(post!);
			await expectNoHorizontalOverflow(page);
			const hero = await page.locator(".post-image img").boundingBox();
			expect(hero!.width).toBeLessThanOrEqual(vp.width);
			const h1Size = await page.locator("h1").evaluate((el) => parseFloat(getComputedStyle(el).fontSize));
			expect(h1Size).toBeGreaterThan(16);
			expect(h1Size).toBeLessThan(vp.width / 4);
		});
	}
});

test.describe("SEO meta tags", () => {
	test("blog listing has title, description, canonical and Open Graph image", async ({ page }) => {
		await page.goto("/blog");
		await expect(page).toHaveTitle(/Powder Coating Guides/);
		expect(await meta(page, "name", "description")).toBeTruthy();
		await expect(page.locator('link[rel="canonical"]')).toHaveAttribute("href", /\/blog$/);
		expect(await meta(page, "property", "og:title")).toBeTruthy();
		expect(await meta(page, "property", "og:url")).toMatch(/\/blog$/);
		expect(await meta(page, "property", "og:image")).toMatch(/^https?:\/\/.+\/_emdash\/api\/media\/file\/.+/);
		expect(await meta(page, "name", "twitter:card")).toBeTruthy();
	});

	test("article pages have their own title, description, canonical, article tags and OG image", async ({ page, request }) => {
		const href = await firstPostUrl(page);
		await page.goto(href);
		const h1 = (await page.locator("h1").innerText()).trim();
		expect(await page.title()).toContain(h1.slice(0, 20));
		expect((await meta(page, "name", "description"))?.length).toBeGreaterThan(20);
		await expect(page.locator('link[rel="canonical"]')).toHaveAttribute("href", new RegExp(`${href}$`));
		expect(await meta(page, "property", "og:type")).toBe("article");
		expect(await meta(page, "property", "og:title")).toBeTruthy();
		expect(await meta(page, "property", "og:url")).toMatch(new RegExp(`${href}$`));
		expect(await meta(page, "property", "article:published_time")).toMatch(/^\d{4}-\d{2}-\d{2}T/);
		const ogImage = await meta(page, "property", "og:image");
		expect(ogImage).toMatch(/^https?:\/\/.+\/_emdash\/api\/media\/file\/.+/);
		// The social card image is a real, fetchable image.
		const img = await request.get(new URL(ogImage!).pathname);
		expect(img.status()).toBe(200);
		expect(img.headers()["content-type"]).toMatch(/^image\//);
		expect(await meta(page, "name", "twitter:image")).toBe(ogImage);

		const ld = await page.locator('script[type="application/ld+json"]').allTextContents();
		const posting = ld.map((text) => JSON.parse(text)).flatMap((d) => d["@graph"] ?? [d]).find((d) => d["@type"] === "BlogPosting");
		expect(posting?.headline).toBeTruthy();
	});
});
