import fs from 'node:fs';

const baseUrl = 'https://kooja-2u6f.vercel.app';

// Read all routes from seed
const seed = JSON.parse(fs.readFileSync('seed/seed.json', 'utf-8'));

const urls = [
  '/',
  '/about-us',
  '/capabilities',
  '/certification',
  '/contact-us',
  '/get-a-quote',
  '/privacy-policy',
  '/services',
  '/industries',
  '/locations',
  '/projects',
  '/blog'
];

for (const s of seed.content?.services || []) urls.push(`/services/${s.slug}`);
for (const i of seed.content?.industries || []) urls.push(`/industries/${i.slug}`);
for (const l of seed.content?.locations || []) urls.push(`/locations/${l.slug}`);
for (const p of seed.content?.projects || []) urls.push(`/projects/${p.slug}`);

console.log(`Auditing ${urls.length} pages against ${baseUrl}...`);

const results = [];
for (const path of urls) {
  const fullUrl = `${baseUrl}${path}`;
  try {
    const res = await fetch(fullUrl, { method: 'GET' });
    const text = await res.text();
    const titleMatch = text.match(/<title>([^<]+)<\/title>/i);
    const title = titleMatch ? titleMatch[1] : 'No title';
    results.push({ path, status: res.status, ok: res.ok, title, length: text.length });
    console.log(`[${res.status}] ${path} - ${title.slice(0, 50)} (${text.length} bytes)`);
  } catch (err) {
    results.push({ path, status: 'ERROR', ok: false, error: err.message });
    console.log(`[ERR] ${path} - ${err.message}`);
  }
}

const failed = results.filter(r => !r.ok);
console.log(`\nAudit complete: ${results.length - failed.length}/${results.length} succeeded.`);
if (failed.length > 0) {
  console.log('Failed pages:', failed);
}
