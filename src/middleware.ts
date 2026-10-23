// Locks the EmDash admin and API on the live site while the design is being
// finished. Set EMDASH_ADMIN_LOCKED=1 to enable; remove it and redeploy to
// open the admin again. Public pages and media files keep working.
import { defineMiddleware } from "astro:middleware";

const OPEN_PREFIXES = ["/_emdash/api/media/file/"];

export const onRequest = defineMiddleware((context, next) => {
	const { pathname } = context.url;
	if (
		process.env.EMDASH_ADMIN_LOCKED === "1" &&
		pathname.startsWith("/_emdash") &&
		!OPEN_PREFIXES.some((prefix) => pathname.startsWith(prefix))
	) {
		return new Response("Not found", { status: 404 });
	}
	return next();
});
