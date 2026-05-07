import sqlite3

db_path = 'clinic_track.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE visits ADD COLUMN amount INTEGER;")
    print("Added amount column to visits.")
except sqlite3.OperationalError as e:
    print(f"amount column might already exist: {e}")

conn.commit()
conn.close()
print("Migration completed.")
