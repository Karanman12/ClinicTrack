from fastapi import APIRouter, Depends, Request, Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from typing import Optional

import crud
import schemas
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/settings")
async def view_settings(request: Request, db: Session = Depends(get_db)):
    settings = crud.get_clinic_settings(db)
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse(request=request, name="settings.html", context={"settings": settings, "doctors": doctors})

@router.post("/settings/update")
async def update_settings(
    request: Request,
    clinic_name: str = Form(...),
    address: Optional[str] = Form(None),
    logo_url: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    settings_data = schemas.ClinicSettingsBase(
        clinic_name=clinic_name,
        address=address,
        logo_url=logo_url
    )
    crud.update_clinic_settings(db, settings_data)
    return RedirectResponse(url="/settings", status_code=303)

@router.post("/settings/doctors/new")
async def create_doctor_route(
    request: Request,
    name: str = Form(...),
    degree: Optional[str] = Form(None),
    specialization: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    doctor_data = schemas.DoctorCreate(name=name, degree=degree, specialization=specialization, phone=phone)
    crud.create_doctor(db, doctor_data)
    return RedirectResponse(url="/settings", status_code=303)

@router.post("/settings/doctors/{doctor_id}/delete")
async def delete_doctor_route(doctor_id: int, request: Request, db: Session = Depends(get_db)):
    success = crud.delete_doctor(db, doctor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return RedirectResponse(url="/settings", status_code=303)
