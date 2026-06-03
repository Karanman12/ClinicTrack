from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

import crud
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def landing_page(request: Request):
    return templates.TemplateResponse(request=request, name="start.html")

@router.get("/dashboard")
async def dashboard(request: Request, db: Session = Depends(get_db)):
    metrics = crud.get_dashboard_metrics(db)
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context={"metrics": metrics, "settings": settings}
    )
