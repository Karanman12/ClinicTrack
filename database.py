import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use PostgreSQL DATABASE_URL from environment (e.g., Render), fallback for local development to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./clinictrack.db")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = None
if not DATABASE_URL.startswith("sqlite"):
    try:
        # Try to connect to PostgreSQL to verify it's active
        test_engine = create_engine(
            DATABASE_URL, 
            pool_pre_ping=True,
            connect_args={"connect_timeout": 2}
        )
        with test_engine.connect() as conn:
            pass
        engine = test_engine
    except Exception:
        # Graceful silent fallback to local SQLite database when local PostgreSQL is not running
        DATABASE_URL = "sqlite:///./clinictrack.db"

if engine is None:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# Configure session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy ORM models
Base = declarative_base()

def get_db():
    """
    Dependency to yield a database session for each request.
    Ensures safe opening and closing of connections.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
