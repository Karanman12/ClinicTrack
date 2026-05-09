from database import engine, SessionLocal
from sqlalchemy import text

def migrate():
    db = SessionLocal()
    try:
        # Using text() for raw SQL execution in SQLAlchemy 2.0+
        db.execute(text("ALTER TABLE visits ADD COLUMN visit_type VARCHAR(50)"))
        db.commit()
        print("Successfully added visit_type column to visits table.")
    except Exception as e:
        print(f"Migration failed: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    migrate()
