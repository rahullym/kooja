// Astro session driver backed by the site's Postgres (Neon) database.
// Vercel has no session store of its own, and EmDash keeps signed-in admin
// users in the Astro session. Used only when a database URL is set.
import pg from "pg";

const TABLE = "astro_sessions";

let pool: pg.Pool | undefined;
let ready: Promise<unknown> | undefined;

function db() {
	pool ??= new pg.Pool({
		connectionString: process.env.DATABASE_URL_UNPOOLED || process.env.DATABASE_URL,
		max: 2,
		connectionTimeoutMillis: 10_000,
	});
	ready ??= pool.query(
		`CREATE TABLE IF NOT EXISTS ${TABLE} (
			key text PRIMARY KEY,
			value text NOT NULL,
			updated_at timestamptz NOT NULL DEFAULT now()
		)`,
	);
	return ready.then(() => pool!);
}

export default function postgresSessionDriver() {
	return {
		async getItem(key: string) {
			const { rows } = await (await db()).query(`SELECT value FROM ${TABLE} WHERE key = $1`, [key]);
			return rows[0] ? JSON.parse(rows[0].value) : null;
		},
		async setItem(key: string, value: unknown) {
			await (await db()).query(
				`INSERT INTO ${TABLE} (key, value) VALUES ($1, $2)
				 ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, updated_at = now()`,
				[key, JSON.stringify(value)],
			);
		},
		async removeItem(key: string) {
			await (await db()).query(`DELETE FROM ${TABLE} WHERE key = $1`, [key]);
		},
	};
}
