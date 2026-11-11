import fs from 'node:fs';
import pg from 'pg';

function loadEnv() {
  const env = { ...process.env };
  const candidates = ['.env.production.local', '.env.production', '.env.local'];
  for (const file of candidates) {
    if (!fs.existsSync(file)) continue;
    const lines = fs.readFileSync(file, 'utf-8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const idx = trimmed.indexOf('=');
      if (idx !== -1) {
        const k = trimmed.slice(0, idx).trim();
        const v = trimmed.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
        if (!env[k] || file === '.env.production.local') {
          env[k] = v;
        }
      }
    }
    if (env.DATABASE_URL_UNPOOLED || env.DATABASE_URL) break;
  }
  return env;
}

const env = loadEnv();
const connectionString = env.DATABASE_URL_UNPOOLED || env.DATABASE_URL;
if (!connectionString) {
  console.error('ERROR: DATABASE_URL_UNPOOLED or DATABASE_URL not found');
  process.exit(1);
}

const client = new pg.Client({ connectionString });
await client.connect();

const seed = JSON.parse(fs.readFileSync('seed/seed.json', 'utf-8'));
const collections = ['pages', 'services', 'industries', 'locations', 'projects'];

// System/non-data columns managed by EmDash
const SYSTEM_COLS = new Set([
  'id', 'slug', 'status', 'author_id', 'primary_byline_id',
  'created_at', 'updated_at', 'published_at', 'scheduled_at', 'deleted_at',
  'version', 'live_revision_id', 'draft_revision_id', 'locale', 'translation_group'
]);

try {
  await client.query('BEGIN');
  let totalSynced = 0;

  for (const col of collections) {
    const table = `ec_${col}`;
    const seedItems = seed.content?.[col] || [];

    const colsRes = await client.query(
      `SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = $1`,
      [table]
    );
    const colTypes = Object.fromEntries(colsRes.rows.map(r => [r.column_name, r.data_type]));
    const colNullable = Object.fromEntries(colsRes.rows.map(r => [r.column_name, r.is_nullable === 'YES']));

    console.log(`\n================ Syncing ${table} (${seedItems.length} items) ================`);

    for (const item of seedItems) {
      const existing = await client.query(`SELECT * FROM ${table} WHERE slug = $1`, [item.slug]);
      const now = new Date().toISOString();
      const data = { ...(item.data || {}) };

      if (existing.rows.length === 0) {
        console.log(`INSERTING: ${item.slug}`);
        const fields = ['id', 'slug', 'status', 'created_at', 'updated_at', 'published_at'];
        const values = [item.id || item.slug, item.slug, item.status || 'published', now, now, now];

        for (const [k, v] of Object.entries(data)) {
          if (!colTypes[k]) continue;
          fields.push(k);
          if (colTypes[k] === 'json' || colTypes[k] === 'jsonb' || typeof v === 'object') {
            values.push(v !== undefined && v !== null ? JSON.stringify(v) : null);
          } else {
            values.push(v ?? null);
          }
        }

        const placeholders = fields.map((_, i) => `$${i + 1}`).join(', ');
        await client.query(`INSERT INTO ${table} (${fields.join(', ')}) VALUES (${placeholders})`, values);
        totalSynced++;
      } else {
        const row = existing.rows[0];
        const updateFields = ['status = $1', 'updated_at = $2'];
        const values = [item.status || 'published', now];

        if (item.status === 'published' && (!row.published_at || row.status !== 'published')) {
          updateFields.push(`published_at = $${values.length + 1}`);
          values.push(now);
        }

        // Preserve existing featured_image or gallery if present in Neon
        let preservedImage = null;
        if (row.featured_image) {
          try {
            preservedImage = typeof row.featured_image === 'string'
              ? JSON.parse(row.featured_image)
              : row.featured_image;
          } catch {
            preservedImage = row.featured_image;
          }
        }

        // Update all content columns defined in table schema
        for (const k of Object.keys(colTypes)) {
          if (SYSTEM_COLS.has(k)) continue;
          if (k === 'featured_image' && row.featured_image) continue;
          if (k === 'gallery' && row.gallery) continue;

          const v = data[k];
          updateFields.push(`${k} = $${values.length + 1}`);
          if (v === undefined || v === null) {
            if (!colNullable[k]) {
              if (colTypes[k] === 'json' || colTypes[k] === 'jsonb') {
                values.push('[]');
              } else if (colTypes[k] === 'integer') {
                values.push(0);
              } else {
                values.push('');
              }
            } else {
              values.push(null);
            }
          } else if (colTypes[k] === 'json' || colTypes[k] === 'jsonb' || typeof v === 'object') {
            values.push(JSON.stringify(v));
          } else {
            values.push(v);
          }
        }

        values.push(item.slug);
        const query = `UPDATE ${table} SET ${updateFields.join(', ')} WHERE slug = $${values.length}`;
        await client.query(query, values);

        // Also update the live revision so revisions.data matches ec_<table>
        if (row.live_revision_id) {
          const revData = { ...data };
          if (preservedImage) {
            revData.featured_image = preservedImage;
          }
          await client.query(
            `UPDATE revisions SET data = $1 WHERE id = $2`,
            [JSON.stringify(revData), row.live_revision_id]
          );
        }

        totalSynced++;
        console.log(`UPDATED: ${item.slug} (ec + revision)`);
      }
    }
  }

  await client.query('COMMIT');
  console.log(`\n--- Successfully synchronized ${totalSynced} records + revisions into Neon Postgres! ---`);
} catch (err) {
  await client.query('ROLLBACK');
  console.error('ERROR during Neon sync, rolled back:', err);
  process.exit(1);
} finally {
  await client.end();
}
