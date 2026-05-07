import sqlite3

db_path = 'clinic_track.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE patients ADD COLUMN age INTEGER;")
    print("Added age column.")
except sqlite3.OperationalError as e:
    print(f"age column might already exist: {e}")

try:
    cursor.execute("ALTER TABLE patients ADD COLUMN gender VARCHAR(10);")
    print("Added gender column.")
except sqlite3.OperationalError as e:
    print(f"gender column might already exist: {e}")

conn.commit()
conn.close()
print("Migration completed.")
