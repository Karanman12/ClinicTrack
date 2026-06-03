from fastapi import APIRouter, Depends, Request, Form, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from datetime import datetime
from typing import Optional

import crud
import schemas
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/visits")
async def list_visits(request: Request, db: Session = Depends(get_db)):
    # Optional global visit history list
    return {"message": "Visits list route works"}

@router.get("/patients/{patient_id}/visits/new")
async def new_visit_form(request: Request, patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    settings = crud.get_clinic_settings(db)
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse(request=request, name="visit_form.html", context={"patient": patient, "settings": settings, "doctors": doctors})

@router.post("/patients/{patient_id}/visits/new")
async def create_visit(
    request: Request,
    patient_id: int,
    doctor_id: Optional[int] = Form(None),
    visit_type: Optional[str] = Form(None),
    symptoms: Optional[str] = Form(None),
    diagnosis: Optional[str] = Form(None),
    prescription: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    weight: Optional[str] = Form(None),
    blood_pressure: Optional[str] = Form(None),
    temperature: Optional[str] = Form(None),
    amount: Optional[str] = Form("0.0"),
    followup_date: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    followup_dt = None
    if followup_date and followup_date.strip():
        try:
            followup_dt = datetime.strptime(followup_date, "%Y-%m-%d")
        except ValueError:
            pass

    weight_val = None
    if weight and weight.strip():
        try:
            weight_val = float(weight.strip())
        except ValueError:
            pass

    temp_val = None
    if temperature and temperature.strip():
        try:
            temp_val = float(temperature.strip())
        except ValueError:
            pass

    amount_val = 0.0
    if amount and amount.strip():
        try:
            amount_val = float(amount.strip())
        except ValueError:
            pass
        
    visit_data = schemas.VisitCreate(
        patient_id=patient_id,
        doctor_id=doctor_id,
        visit_type=visit_type,
        symptoms=symptoms,
        diagnosis=diagnosis,
        prescription=prescription,
        notes=notes,
        weight=weight_val,
        blood_pressure=blood_pressure,
        temperature=temp_val,
        amount=amount_val,
        followup_date=followup_dt
    )
    crud.create_visit(db, visit_data)
    return RedirectResponse(url=f"/patients/{patient_id}", status_code=303)

@router.post("/visits/{visit_id}/delete")
async def delete_visit_route(visit_id: int, request: Request, db: Session = Depends(get_db)):
    visit = crud.get_visit(db, visit_id)
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    patient_id = visit.patient_id
    crud.delete_visit(db, visit_id)
    return RedirectResponse(url=f"/patients/{patient_id}", status_code=303)

@router.get("/visits/{visit_id}/pdf")
async def export_prescription_pdf(visit_id: int, request: Request, db: Session = Depends(get_db)):
    visit = crud.get_visit(db, visit_id)
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    
    settings = crud.get_clinic_settings(db)
    return templates.TemplateResponse(request=request, name="prescription.html", context={"visit": visit, "settings": settings})


@router.get("/visits/{visit_id}/edit")
async def edit_visit_form(request: Request, visit_id: int, db: Session = Depends(get_db)):
    visit = crud.get_visit(db, visit_id)
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    patient = visit.patient
    settings = crud.get_clinic_settings(db)
    doctors = crud.get_doctors(db)
    return templates.TemplateResponse(
        request=request,
        name="visit_form.html",
        context={
            "patient": patient,
            "visit": visit,
            "settings": settings,
            "doctors": doctors
        }
    )


@router.post("/visits/{visit_id}/edit")
async def update_visit_route(
    request: Request,
    visit_id: int,
    doctor_id: Optional[int] = Form(None),
    visit_type: Optional[str] = Form(None),
    symptoms: Optional[str] = Form(None),
    diagnosis: Optional[str] = Form(None),
    prescription: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    weight: Optional[str] = Form(None),
    blood_pressure: Optional[str] = Form(None),
    temperature: Optional[str] = Form(None),
    amount: Optional[str] = Form("0.0"),
    followup_date: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    visit = crud.get_visit(db, visit_id)
    if not visit:
        raise HTTPException(status_code=404, detail="Visit not found")
    
    followup_dt = None
    if followup_date and followup_date.strip():
        try:
            followup_dt = datetime.strptime(followup_date, "%Y-%m-%d")
        except ValueError:
            pass

    weight_val = None
    if weight and weight.strip():
        try:
            weight_val = float(weight.strip())
        except ValueError:
            pass

    temp_val = None
    if temperature and temperature.strip():
        try:
            temp_val = float(temperature.strip())
        except ValueError:
            pass

    amount_val = 0.0
    if amount and amount.strip():
        try:
            amount_val = float(amount.strip())
        except ValueError:
            pass
        
    visit_update = schemas.VisitBase(
        doctor_id=doctor_id,
        visit_type=visit_type,
        symptoms=symptoms,
        diagnosis=diagnosis,
        prescription=prescription,
        notes=notes,
        weight=weight_val,
        blood_pressure=blood_pressure,
        temperature=temp_val,
        amount=amount_val,
        followup_date=followup_dt
    )
    crud.update_visit(db, visit_id, visit_update)
    return RedirectResponse(url=f"/patients/{visit.patient_id}", status_code=303)

