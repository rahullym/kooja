import node from "@astrojs/node";
import react from "@astrojs/react";
import vercel from "@astrojs/vercel";
import icon from "astro-iconset";
import { defineConfig, fontProviders } from "astro/config";
import emdash, { local, s3 } from "emdash/astro";
import { postgres, sqlite } from "emdash/db";

// Vercel builds use the Vercel adapter, Neon (DATABASE_URL) and S3-compatible
// media storage (S3_* variables). Local dev falls back to SQLite and ./uploads.
const onVercel = !!process.env.VERCEL;
// Neon's Vercel integration sets both; EmDash migrations want a direct connection.
const databaseUrl = process.env.DATABASE_URL_UNPOOLED || process.env.DATABASE_URL;

export default defineConfig({
	output: "server",
	adapter: onVercel ? vercel() : node({ mode: "standalone" }),
	// The Vercel adapter has no session store; keep admin sessions in Postgres.
	...(databaseUrl && {
		session: {
			driver: { entrypoint: new URL("./src/lib/session-driver.ts", import.meta.url) },
			ttl: 60 * 60 * 24 * 30,
		},
	}),
	image: {
		layout: "constrained",
		responsiveStyles: true,
	},
	integrations: [
		react(),
		icon({
			// Only ship the Phosphor icons actually referenced in templates,
			// not the full @iconify-json/ph set.
			include: {
				ph: [
					"chart-bar",
					"check-circle",
					"clock",
					"cloud",
					"code",
					"currency-dollar",
					"envelope",
					"globe",
					"heart",
					"lifebuoy",
					"lightning",
					"lock",
					"shield-check",
					"sparkle",
					"star",
					"users-three",
				],
			},
		}),
		emdash({
			database: databaseUrl
				? postgres({
						connectionString: databaseUrl,
						// Serverless functions each hold their own pool; keep it small.
						pool: { max: 3, connectionTimeoutMillis: 10_000 },
					})
				: sqlite({ url: "file:./data.db" }),
			storage: process.env.S3_BUCKET
				? s3()
				: local({
						directory: "./uploads",
						baseUrl: "/_emdash/api/media/file",
					}),
		}),
	],
	fonts: [
		{
			provider: fontProviders.google(),
			name: "IBM Plex Sans",
			cssVariable: "--font-body",
			weights: [400, 500, 600],
			fallbacks: ["sans-serif"],
		},
		{
			provider: fontProviders.google(),
			name: "Archivo",
			cssVariable: "--font-display",
			weights: [600, 700, 800],
			fallbacks: ["sans-serif"],
		},
		{
			provider: fontProviders.google(),
			name: "IBM Plex Mono",
			cssVariable: "--font-mono",
			weights: [400, 500],
			fallbacks: ["monospace"],
		},
	],
	devToolbar: { enabled: false },
});
