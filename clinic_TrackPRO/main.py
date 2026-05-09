"""
main.py — FastAPI application for ClinicTrack

Routes:
  GET  /                → Home page (patient list + add form)
  POST /add_patient     → Create a new patient
  GET  /patient/{id}    → Patient profile + visit history
  POST /add_visit/{id}  → Add a visit for a patient
  GET  /suggest?q=      → Autocomplete API for symptoms
"""

from fastapi import FastAPI, Depends, Request, Form, Query
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, get_db, Base
from models import Patient, Visit, Settings

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(title="ClinicTrack", description="Patient & Visit Manager for Small Clinics")

# Create all tables on startup (if they don't exist yet)
Base.metadata.create_all(bind=engine)

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 template directory
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------------------------
# Common symptoms list — used by the autocomplete API
# ---------------------------------------------------------------------------

COMMON_SYMPTOMS = [
    "fever", "cough", "cold", "headache", "body ache",
    "sore throat", "runny nose", "sneezing", "fatigue", "weakness",
    "nausea", "vomiting", "diarrhea", "constipation", "abdominal pain",
    "chest pain", "shortness of breath", "dizziness", "back pain",
    "joint pain", "muscle pain", "skin rash", "itching", "swelling",
    "blurred vision", "ear pain", "weight loss", "weight gain",
    "loss of appetite", "insomnia", "anxiety", "depression",
    "frequent urination", "burning urination", "blood in urine",
    "blood in stool", "high blood pressure", "low blood pressure",
    "diabetes", "allergies",
]

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/")
def landing_page(request: Request):
    """
    Landing page — modern start page for ClinicTrack.
    """
    return templates.TemplateResponse(request=request, name="start.html")


@app.get("/app")
def dashboard(request: Request, db: Session = Depends(get_db)):
    """
    Main app dashboard — shows patient list.
    """
    patients = db.query(Patient).order_by(Patient.created_at.desc()).all()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"patients": patients, "selected_patient": None},
    )


@app.get("/app/patient/{patient_id}")
def patient_dashboard(patient_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Main app dashboard — with selected patient details.
    """
    patients = db.query(Patient).order_by(Patient.created_at.desc()).all()
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if not patient:
        return RedirectResponse(url="/app", status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"patients": patients, "selected_patient": patient},
    )


@app.post("/add_patient")
def add_patient(
    name: str = Form(...),
    phone: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    Create a new patient and redirect back to the home page.
    """
    patient = Patient(name=name.strip(), phone=phone.strip(), age=age, gender=gender.strip())
    db.add(patient)
    db.commit()
    return RedirectResponse(url=f"/app/patient/{patient.id}", status_code=303)


@app.post("/update_patient/{patient_id}")
def update_patient(
    patient_id: int,
    name: str = Form(...),
    phone: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    db: Session = Depends(get_db),
):
    """
    Update an existing patient's details.
    """
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        patient.name = name.strip()
        patient.phone = phone.strip()
        patient.age = age
        patient.gender = gender.strip()
        db.commit()
    return RedirectResponse(url=f"/app/patient/{patient_id}", status_code=303)


@app.post("/add_visit/{patient_id}")
def add_visit(
    patient_id: int,
    symptoms: str = Form(...),
    prescription: str = Form(...),
    notes: str = Form(""),
    visit_type: str = Form(""),
    amount: int = Form(0),
    db: Session = Depends(get_db),
):
    """
    Add a visit record for this patient, then redirect to their profile.
    """
    visit = Visit(
        patient_id=patient_id,
        symptoms=symptoms.strip(),
        prescription=prescription.strip(),
        notes=notes.strip(),
        visit_type=visit_type.strip() if visit_type else None,
        amount=amount,
    )
    db.add(visit)
    db.commit()
    return RedirectResponse(url=f"/app/patient/{patient_id}", status_code=303)


@app.post("/delete_patient/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """
    Delete a patient (cascades to their visits).
    """
    patient = db.query(Patient).filter(Patient.id == patient_id).first()
    if patient:
        db.delete(patient)
        db.commit()
    return RedirectResponse(url="/app", status_code=303)


@app.post("/delete_visit/{visit_id}")
def delete_visit(visit_id: int, db: Session = Depends(get_db)):
    """
    Delete a specific visit record.
    """
    visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if visit:
        patient_id = visit.patient_id
        db.delete(visit)
        db.commit()
        return RedirectResponse(url=f"/app/patient/{patient_id}", status_code=303)
    return RedirectResponse(url="/app", status_code=303)


@app.post("/update_visit/{visit_id}")
def update_visit(
    visit_id: int,
    symptoms: str = Form(...),
    prescription: str = Form(...),
    notes: str = Form(""),
    visit_type: str = Form(""),
    amount: int = Form(0),
    db: Session = Depends(get_db),
):
    """
    Update an existing visit record.
    """
    visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if visit:
        visit.symptoms = symptoms.strip()
        visit.prescription = prescription.strip()
        visit.notes = notes.strip()
        visit.visit_type = visit_type.strip() if visit_type else None
        visit.amount = amount
        db.commit()
        return RedirectResponse(url=f"/app/patient/{visit.patient_id}", status_code=303)
    return RedirectResponse(url="/app", status_code=303)



@app.get("/print_prescription/{visit_id}")
def print_prescription(visit_id: int, request: Request, db: Session = Depends(get_db)):
    """
    Render a clean, printable prescription page for a specific visit.
    """
    visit = db.query(Visit).filter(Visit.id == visit_id).first()
    if not visit:
        return RedirectResponse(url="/app", status_code=303)
    settings = db.query(Settings).first()
    return templates.TemplateResponse(
        request=request,
        name="prescription.html",
        context={"visit": visit, "patient": visit.patient, "settings": settings},
    )


@app.get("/suggest")
def suggest(q: str = Query("")):
    """
    Autocomplete API — returns symptom suggestions matching the query.
    Example: /suggest?q=fe → ["fever"]
    """
    query = q.lower().strip()
    if not query:
        return []
    matches = [s for s in COMMON_SYMPTOMS if s.startswith(query)]
    return matches[:10]  # Cap at 10 suggestions


@app.get("/settings")
def settings_page(request: Request, db: Session = Depends(get_db)):
    """
    Settings page — fetch or create default settings.
    """
    settings = db.query(Settings).first()
    if not settings:
        settings = Settings(clinic_name="", doctor_name="")
        db.add(settings)
        db.commit()
    return templates.TemplateResponse(
        request=request,
        name="settings.html",
        context={"settings": settings},
    )


@app.post("/settings")
def save_settings(
    clinic_name: str = Form(...),
    doctor_name: str = Form(...),
    degree: str = Form(""),
    phone: str = Form(""),
    address: str = Form(""),
    db: Session = Depends(get_db),
):
    """
    Save clinic settings — updates first record or creates new one.
    """
    settings = db.query(Settings).first()
    if settings:
        settings.clinic_name = clinic_name.strip()
        settings.doctor_name = doctor_name.strip()
        settings.degree = degree.strip() if degree else None
        settings.phone = phone.strip() if phone else None
        settings.address = address.strip() if address else None
    else:
        settings = Settings(
            clinic_name=clinic_name.strip(),
            doctor_name=doctor_name.strip(),
            degree=degree.strip() if degree else None,
            phone=phone.strip() if phone else None,
            address=address.strip() if address else None,
        )
        db.add(settings)
    db.commit()
    return RedirectResponse(url="/settings", status_code=303)
