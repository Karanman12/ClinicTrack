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

@router.get("/patients")
async def list_patients(request: Request, search: Optional[str] = None, db: Session = Depends(get_db)):
    patients = crud.get_patients(db, search=search)
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(request=request, name="patients.html", context={"patients": patients, "settings": settings, "search": search})

@router.get("/patients/new")
async def new_patient_form(request: Request, db: Session = Depends(get_db)):
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(request=request, name="patient_form.html", context={"settings": settings})

@router.get("/patients/{patient_id}/edit")
async def edit_patient_form(request: Request, patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(request=request, name="patient_form.html", context={"patient": patient, "settings": settings})

@router.post("/patients/{patient_id}/edit")
async def update_patient(
    request: Request,
    patient_id: int,
    name: str = Form(...),
    age: Optional[int] = Form(None),
    gender: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    blood_group: Optional[str] = Form(None),
    allergies: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    patient_update = schemas.PatientBase(
        name=name, age=age, gender=gender, phone=phone, 
        blood_group=blood_group, allergies=allergies, address=address, notes=notes
    )
    crud.update_patient(db, patient_id, patient_update)
    return RedirectResponse(url=f"/patients/{patient_id}", status_code=303)

@router.post("/patients/new")
async def create_patient(
    request: Request,
    name: str = Form(...),
    age: Optional[int] = Form(None),
    gender: Optional[str] = Form(None),
    phone: Optional[str] = Form(None),
    blood_group: Optional[str] = Form(None),
    allergies: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    patient_data = schemas.PatientCreate(
        name=name, age=age, gender=gender, phone=phone, 
        blood_group=blood_group, allergies=allergies, address=address, notes=notes
    )
    crud.create_patient(db, patient_data)
    return RedirectResponse(url="/patients", status_code=303)

@router.get("/patients/{patient_id}")
async def patient_profile(request: Request, patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    visits = crud.get_visits_by_patient(db, patient_id)
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(request=request, name="patient_profile.html", context={"patient": patient, "visits": visits, "settings": settings})

@router.post("/patients/{patient_id}/delete")
async def delete_patient_route(patient_id: int, request: Request, db: Session = Depends(get_db)):
    success = crud.delete_patient(db, patient_id)
    if not success:
        raise HTTPException(status_code=404, detail="Patient not found")
    return RedirectResponse(url="/patients", status_code=303)
