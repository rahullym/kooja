import { existsSync } from "node:fs";
import { defineConfig, devices } from "@playwright/test";

const port = process.env.E2E_PORT || "4455";
// Use a system Chromium when Playwright's own browser is not installed.
const systemChromium = ["/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/google-chrome"].find(existsSync);
const launchOptions = process.env.PLAYWRIGHT_CHROMIUM_PATH
	? { executablePath: process.env.PLAYWRIGHT_CHROMIUM_PATH }
	: systemChromium && !process.env.PLAYWRIGHT_USE_BUNDLED
		? { executablePath: systemChromium }
		: {};

export default defineConfig({
	testDir: "tests/e2e",
	timeout: 60_000,
	fullyParallel: true,
	reporter: "list",
	use: {
		baseURL: `http://127.0.0.1:${port}`,
		launchOptions,
	},
	projects: [{ name: "chromium", use: { ...devices["Desktop Chrome"], launchOptions } }],
	webServer: {
		command: "node scripts/e2e-server.mjs",
		url: `http://127.0.0.1:${port}/blog`,
		timeout: 300_000,
		reuseExistingServer: !process.env.CI,
		env: { E2E_PORT: port },
	},
});
