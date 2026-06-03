from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from typing import List, Optional

import models
import schemas

# ==========================================
# Dashboard Metrics
# ==========================================
def get_dashboard_metrics(db: Session):
    total_patients = db.query(models.Patient).count()
    total_visits = db.query(models.Visit).count()
    
    today = date.today()
    todays_visits = db.query(models.Visit).filter(func.date(models.Visit.visit_date) == today).count()
    
    # SQLite/PostgreSQL safe way to extract month/year or just simple filtering
    # For a robust approach, we can just aggregate all time or filter in Python if simple
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    from sqlalchemy import extract
    monthly_revenue = db.query(func.sum(models.Visit.amount)).filter(
        extract('month', models.Visit.visit_date) == current_month,
        extract('year', models.Visit.visit_date) == current_year
    ).scalar() or 0.0

    recent_patients = db.query(models.Patient).order_by(models.Patient.created_at.desc()).limit(5).all()
    
    upcoming_followups = db.query(models.Visit).filter(
        models.Visit.followup_date >= today
    ).order_by(models.Visit.followup_date.asc()).limit(5).all()

    return {
        "total_patients": total_patients,
        "total_visits": total_visits,
        "todays_visits": todays_visits,
        "monthly_revenue": float(monthly_revenue),
        "recent_patients": recent_patients,
        "upcoming_followups": upcoming_followups
    }

# ==========================================
# Patients
# ==========================================
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100, search: Optional[str] = None):
    query = db.query(models.Patient)
    if search:
        query = query.filter(models.Patient.name.ilike(f"%{search}%") | models.Patient.phone.ilike(f"%{search}%"))
    return query.order_by(models.Patient.created_at.desc()).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, patient_id: int, patient_update: schemas.PatientBase):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        update_data = patient_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_patient, key, value)
        db.commit()
        db.refresh(db_patient)
    return db_patient

def delete_patient(db: Session, patient_id: int):
    db_patient = get_patient(db, patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
        return True
    return False

# ==========================================
# Visits
# ==========================================
def get_visit(db: Session, visit_id: int):
    return db.query(models.Visit).filter(models.Visit.id == visit_id).first()

def get_visits_by_patient(db: Session, patient_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Visit).filter(models.Visit.patient_id == patient_id).order_by(models.Visit.visit_date.desc()).offset(skip).limit(limit).all()

def create_visit(db: Session, visit: schemas.VisitCreate):
    db_visit = models.Visit(**visit.model_dump())
    db.add(db_visit)
    db.commit()
    db.refresh(db_visit)
    return db_visit

def update_visit(db: Session, visit_id: int, visit_update: schemas.VisitBase):
    db_visit = get_visit(db, visit_id)
    if db_visit:
        update_data = visit_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_visit, key, value)
        db.commit()
        db.refresh(db_visit)
    return db_visit

def delete_visit(db: Session, visit_id: int):
    db_visit = get_visit(db, visit_id)
    if db_visit:
        db.delete(db_visit)
        db.commit()
        return True
    return False

# ==========================================
# Clinic Settings
# ==========================================
def get_clinic_settings(db: Session):
    settings = db.query(models.ClinicSettings).first()
    if not settings:
        settings = models.ClinicSettings(clinic_name="ClinicTrack Pro")
        db.add(settings)
        db.commit()
        db.refresh(settings)
    return settings

def update_clinic_settings(db: Session, settings_update: schemas.ClinicSettingsBase):
    db_settings = get_clinic_settings(db)
    update_data = settings_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_settings, key, value)
    db.commit()
    db.refresh(db_settings)
    return db_settings

# ==========================================
# Doctors
# ==========================================
def get_doctors(db: Session):
    return db.query(models.Doctor).order_by(models.Doctor.name.asc()).all()

def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.model_dump())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

def update_doctor(db: Session, doctor_id: int, doctor_update: schemas.DoctorBase):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        update_data = doctor_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_doctor, key, value)
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

def delete_doctor(db: Session, doctor_id: int):
    db_doctor = get_doctor(db, doctor_id)
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
        return True
    return False
