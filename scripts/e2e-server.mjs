// Serves the built site (dist/) against a throwaway SQLite database seeded
// from seed/seed.json, for the Playwright tests. Never touches ./data.db.
import { spawn, spawnSync } from "node:child_process";
import { existsSync, mkdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";

const root = fileURLToPath(new URL("..", import.meta.url));
const dir = path.join(root, ".e2e");
const db = path.join(dir, "data.db");
const port = process.env.E2E_PORT || "4455";

if (!existsSync(path.join(root, "dist/server/entry.mjs"))) {
	console.error("dist/ is missing: run `pnpm build` first.");
	process.exit(1);
}

if (!existsSync(db)) {
	mkdirSync(dir, { recursive: true });
	const seeded = spawnSync(
		"npx",
		["emdash", "seed", path.join(root, "seed/seed.json"), "-d", db, "--uploads-dir", path.join(dir, "uploads")],
		{ cwd: root, stdio: "inherit" },
	);
	if (seeded.status !== 0) process.exit(seeded.status ?? 1);
}

// sqlite({ url: "file:./data.db" }) and ./uploads resolve from the working directory.
const server = spawn(process.execPath, [path.join(root, "dist/server/entry.mjs")], {
	cwd: dir,
	env: { ...process.env, PORT: port, HOST: "127.0.0.1" },
	stdio: "inherit",
});
for (const signal of ["SIGINT", "SIGTERM"]) process.on(signal, () => server.kill(signal));
server.on("exit", (code) => process.exit(code ?? 0));
