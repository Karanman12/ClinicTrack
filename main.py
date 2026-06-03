from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from database import engine, Base
from routes import dashboard, patients, visits, settings

# Create all tables (In production, consider using Alembic for migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ClinicTrack Pro", version="2.0")

# Setup templates and static files (will be used after frontend generation)
templates = Jinja2Templates(directory="templates")

# Only mount static directory if it exists to avoid startup errors during intermediate generation
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Include Modular Routers
app.include_router(dashboard.router, tags=["Dashboard"])
app.include_router(patients.router, tags=["Patients"])
app.include_router(visits.router, tags=["Visits"])
app.include_router(settings.router, tags=["Settings"])

if __name__ == "__main__":
    import uvicorn
    # Optional debug execution
    port = int(os.environ.get("PORT", 3000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
