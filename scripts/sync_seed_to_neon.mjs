import fs from 'node:fs';
import pg from 'pg';

const envLines = fs.readFileSync('.env.production', 'utf-8').split('\n');
const env = {};
for (const line of envLines) {
  const trimmed = line.trim();
  if (!trimmed || trimmed.startsWith('#')) continue;
  const idx = trimmed.indexOf('=');
  if (idx !== -1) {
    env[trimmed.slice(0, idx).trim()] = trimmed.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
  }
}

const connectionString = env.DATABASE_URL_UNPOOLED || env.DATABASE_URL;
const client = new pg.Client({ connectionString });
await client.connect();

const seed = JSON.parse(fs.readFileSync('seed/seed.json', 'utf-8'));
const collections = ['pages', 'services', 'industries', 'locations', 'projects'];

for (const col of collections) {
  const table = `ec_${col}`;
  const seedItems = seed.content?.[col] || [];
  
  // Get table column info
  const colsRes = await client.query(`SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '${table}'`);
  const colTypes = Object.fromEntries(colsRes.rows.map(r => [r.column_name, r.data_type]));
  
  console.log(`\n================ Syncing ${table} (${seedItems.length} items) ================`);
  
  for (const item of seedItems) {
    const existing = await client.query(`SELECT * FROM ${table} WHERE slug = $1`, [item.slug]);
    const now = new Date().toISOString();
    
    if (existing.rows.length === 0) {
      console.log(`INSERTING: ${item.slug}`);
      const fields = ['id', 'slug', 'status', 'created_at', 'updated_at', 'published_at'];
      const values = [item.id || item.slug, item.slug, item.status || 'published', now, now, now];
      
      for (const [k, v] of Object.entries(item.data || {})) {
        if (!colTypes[k]) continue;
        fields.push(k);
        if (colTypes[k] === 'json' || colTypes[k] === 'jsonb') {
          values.push(v ? JSON.stringify(v) : null);
        } else {
          values.push(v ?? null);
        }
      }
      
      const placeholders = fields.map((_, i) => `$${i + 1}`).join(', ');
      await client.query(`INSERT INTO ${table} (${fields.join(', ')}) VALUES (${placeholders})`, values);
    } else {
      console.log(`UPDATING: ${item.slug} (was ${existing.rows[0].status} -> ${item.status || 'published'})`);
      const updateFields = ['status = $1', 'updated_at = $2'];
      const values = [item.status || 'published', now];
      
      if (item.status === 'published' && (!existing.rows[0].published_at || existing.rows[0].status !== 'published')) {
        updateFields.push(`published_at = $${values.length + 1}`);
        values.push(now);
      }
      
      for (const [k, v] of Object.entries(item.data || {})) {
        if (!colTypes[k]) continue;
        // If it's featured_image and existing already has one, keep existing unless seed has explicit non-$media object
        if (k === 'featured_image' && existing.rows[0].featured_image) {
          continue;
        }
        
        updateFields.push(`${k} = $${values.length + 1}`);
        if (colTypes[k] === 'json' || colTypes[k] === 'jsonb') {
          values.push(v ? JSON.stringify(v) : null);
        } else {
          values.push(v ?? null);
        }
      }
      
      values.push(item.slug);
      const query = `UPDATE ${table} SET ${updateFields.join(', ')} WHERE slug = $${values.length}`;
      await client.query(query, values);
    }
  }
}

console.log('\n--- Sync finished successfully! ---');
await client.end();
