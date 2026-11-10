import { EventEmitter } from 'node:events';
import { handler } from '../dist/server/entry.mjs';

const urls = [
  // Homepage
  '/',
  // Services
  '/services',
  '/services/industrial-powder-coating',
  '/services/surface-preparation',
  '/services/sandblasting',
  '/services/custom-colors-finishes',
  '/services/restoration-recoating',
  '/services/automotive-powder-coating',
  '/services/wheel-rim-powder-coating',
  '/services/specialty-custom-projects',
  // Industries
  '/industries',
  '/industries/food-processing-equipment',
  '/industries/agricultural-heavy-equipment',
  '/industries/contractors-construction',
  '/industries/manufacturing-automation',
  '/industries/machine-shops',
  '/industries/metal-fabricators-welding-shops',
  '/industries/municipal-institutional',
  // Locations
  '/locations',
  '/locations/powder-coating-milton',
  '/locations/powder-coating-oakville',
  '/locations/powder-coating-burlington',
  '/locations/powder-coating-mississauga',
  '/locations/powder-coating-halton-hills',
  '/locations/powder-coating-brampton',
  '/locations/powder-coating-guelph',
  '/locations/powder-coating-cambridge',
  '/locations/powder-coating-hamilton',
  // Projects
  '/projects',
  '/projects/food-processing-line-frame',
  '/projects/automation-line-frame',
  '/projects/church-gates',
  '/projects/conveyor-frame-automotive-plant',
  '/projects/robotic-base',
  '/projects/safety-bollards',
  // Other pages
  '/blog',
  '/contact-us',
  '/get-a-quote',
  '/capabilities',
  '/certification',
  '/about-us',
  '/privacy-policy'
];

function renderUrl(urlPath) {
  return new Promise((resolve) => {
    const req = new EventEmitter();
    req.url = urlPath;
    req.method = 'GET';
    req.headers = { host: 'localhost:4321', 'user-agent': 'AuditRunner' };
    req.socket = { remoteAddress: '127.0.0.1', encrypted: false };

    const res = new EventEmitter();
    let chunks = [];
    res.statusCode = 200;
    res.setHeader = () => {};
    res.getHeader = () => {};
    res.writeHead = (code) => { res.statusCode = code; };
    res.write = (chunk) => { chunks.push(Buffer.from(chunk)); };
    res.end = (chunk) => {
      if (chunk) chunks.push(Buffer.from(chunk));
      resolve({ status: res.statusCode, data: Buffer.concat(chunks).toString('utf-8') });
    };

    handler(req, res);
  });
}

async function auditAll() {
  console.log(`Starting comprehensive audit of all ${urls.length} mandatory website URLs...`);
  let passed = 0;
  let failed = 0;
  const issues = [];
  let totalTablesFound = 0;

  for (const u of urls) {
    try {
      const res = await renderUrl(u);
      if (res.status !== 200) {
        issues.push(`${u}: HTTP status ${res.status}`);
        failed++;
        continue;
      }

      const html = res.data;
      // Check for bracket placeholders like [confirm...] or [add...]
      const placeholderMatch = html.match(/\[(?:confirm|add|insert)[^\]]*\]/gi);
      if (placeholderMatch) {
        issues.push(`${u}: Found placeholders: ${JSON.stringify(placeholderMatch)}`);
      }

      // Check for raw unrated Google Rating
      const rawRating = html.match(/Google Rating\s*\[/gi);
      if (rawRating) {
        issues.push(`${u}: Found unresolved rating bracket: ${rawRating}`);
      }

      // Count table tags
      const tableMatches = html.match(/<table[^>]*>/gi);
      const tableCount = tableMatches ? tableMatches.length : 0;
      totalTablesFound += tableCount;

      passed++;
      const tblStr = tableCount > 0 ? ` (${tableCount} table${tableCount > 1 ? 's' : ''})` : '';
      console.log(`✓ ${u.padEnd(46)} -> 200 OK${tblStr}`);
    } catch (e) {
      issues.push(`${u}: Error rendering: ${e.message}`);
      failed++;
    }
  }

  console.log('\n======================================================');
  console.log('       COMPLETE RESTORATION & AUDIT REPORT            ');
  console.log('======================================================');
  console.log(`Total URLs Audited: ${urls.length}`);
  console.log(`Pages 200 OK:      ${passed} / ${urls.length}`);
  console.log(`Pages Failed:      ${failed}`);
  console.log(`Native <table> elements rendered: ${totalTablesFound}`);
  if (issues.length > 0) {
    console.log('\nIssues detected:');
    issues.forEach(i => console.log(' - ' + i));
  } else {
    console.log('\n>>> SUCCESS: ALL 38 PAGES AUDITED WITH 0 PLACEHOLDERS & 0 ERRORS! <<<');
  }
}

auditAll().catch(console.error);
