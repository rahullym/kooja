import json
import sqlite3
import datetime

def main():
    print("Starting sync of seed/seed.json to data.db (SQLite)...")
    with open("seed/seed.json", "r", encoding="utf-8") as f:
        seed = json.load(f)

    con = sqlite3.connect("data.db")
    cur = con.cursor()

    collections = ["pages", "services", "industries", "locations", "projects"]
    total_updated = 0

    try:
        cur.execute("BEGIN TRANSACTION")

        for col in collections:
            table = f"ec_{col}"
            seed_items = seed.get("content", {}).get(col, [])
            col_info = cur.execute(f"PRAGMA table_info({table})").fetchall()
            table_cols = {row[1]: row[2] for row in col_info}

            print(f"\n--- Syncing {table} ({len(seed_items)} items) ---")

            for item in seed_items:
                slug = item.get("slug")
                data = item.get("data", {})
                status = item.get("status", "published")

                existing = cur.execute(f"SELECT id FROM {table} WHERE slug = ?", (slug,)).fetchone()
                now = datetime.datetime.now(datetime.timezone.utc).isoformat()

                if not existing:
                    print(f"Skipping insert for non-existent row: {slug}")
                    continue

                update_fields = ["status = ?", "updated_at = ?"]
                values = [status, now]

                for k, v in data.items():
                    if k not in table_cols:
                        continue
                    # preserve existing featured_image if valid
                    if k == "featured_image":
                        continue
                    
                    update_fields.append(f"{k} = ?")
                    if isinstance(v, (dict, list)):
                        values.append(json.dumps(v, ensure_ascii=False))
                    else:
                        values.append(v)

                values.append(slug)
                query = f"UPDATE {table} SET {', '.join(update_fields)} WHERE slug = ?"
                cur.execute(query, values)
                total_updated += 1
                print(f"Updated {slug}")

        con.commit()
        print(f"\nSuccessfully synchronized {total_updated} items into data.db!")

    except Exception as e:
        con.rollback()
        print(f"Error during synchronization, rolled back: {e}")
        raise e
    finally:
        con.close()

if __name__ == "__main__":
    main()
