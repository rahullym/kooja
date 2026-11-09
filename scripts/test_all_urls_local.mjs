import { spawn } from 'node:child_process';
import http from 'node:http';

const URLS = [
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
  '/capabilities'
];

async function checkUrl(port, path) {
  return new Promise((resolve) => {
    const req = http.get(`http://127.0.0.1:${port}${path}`, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        const titleMatch = data.match(/<title>([^<]+)<\/title>/i);
        const title = titleMatch ? titleMatch[1].trim() : 'No Title';
        
        // Check for bracket placeholders
        const brackets = (data.match(/\[(?:confirm|add live rating|add rating|Verified Google review)[^\]]*\]/gi) || []);
        
        // Check for corrupted strings
        const corrupted = (data.match(/jTqLm|BlYLm|A_,Y|E\?&QR/gi) || []);
        
        // Check for rating or reviews
        const hasRating = data.includes('5.0 ★ Google Rating') || data.includes('5.0 ★ (Verified Reviews)') || data.includes('5/5 Stars');
        
        resolve({
          path,
          status: res.statusCode,
          title,
          bracketsCount: brackets.length,
          corruptedCount: corrupted.length,
          hasRating,
          contentLength: data.length
        });
      });
    });
    req.on('error', err => {
      resolve({ path, status: 'ERROR', error: err.message });
    });
  });
}

async function run() {
  const PORT = 4399;
  const env = { ...process.env, PORT: String(PORT), HOST: '127.0.0.1' };
  
  console.log(`Starting standalone server on port ${PORT}...`);
  const serverProc = spawn('node', ['dist/server/entry.mjs'], { env, stdio: ['ignore', 'pipe', 'pipe'] });
  
  let started = false;
  serverProc.stdout.on('data', (d) => {
    const msg = d.toString();
    if (msg.includes('http://') || msg.includes('Server') || msg.includes('listening')) {
      started = true;
    }
  });
  serverProc.stderr.on('data', d => console.error('server err:', d.toString()));
  
  // Wait up to 5s for server to start
  for (let i = 0; i < 20; i++) {
    await new Promise(r => setTimeout(r, 250));
    try {
      const probe = await checkUrl(PORT, '/');
      if (probe.status === 200) {
        started = true;
        break;
      }
    } catch (e) {}
  }
  
  if (!started) {
    console.error('Failed to start server within timeout.');
    serverProc.kill();
    process.exit(1);
  }
  
  console.log(`Server started. Auditing all ${URLS.length} URLs...\n`);
  
  const results = [];
  let failures = 0;
  
  for (let i = 0; i < URLS.length; i++) {
    const url = URLS[i];
    const r = await checkUrl(PORT, url);
    results.push(r);
    
    const isOk = r.status === 200 && r.bracketsCount === 0 && r.corruptedCount === 0;
    const mark = isOk ? '✓ PASS' : '✗ FAIL';
    if (!isOk) failures++;
    
    console.log(`${(i+1).toString().padStart(2)}. [${r.status}] ${mark} ${url} | Title: ${(r.title || r.error || 'N/A').slice(0, 45)} | Len: ${r.contentLength || 0} bytes | Brackets: ${r.bracketsCount ?? 'N/A'}`);
  }
  
  console.log(`\n======================================================`);
  console.log(`AUDIT COMPLETE: ${URLS.length - failures}/${URLS.length} URLs PASSED.`);
  console.log(`Total Failures: ${failures}`);
  console.log(`======================================================`);
  
  serverProc.kill();
  if (failures > 0) process.exit(1);
}

run();
