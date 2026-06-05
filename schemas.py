from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# ==========================================
# Clinic Settings Schemas
# ==========================================
class ClinicSettingsBase(BaseModel):
    clinic_name: str
    doctor_name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    logo_url: Optional[str] = None

class ClinicSettingsCreate(ClinicSettingsBase):
    pass

class ClinicSettings(ClinicSettingsBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Doctor Schemas
# ==========================================
class DoctorBase(BaseModel):
    name: str
    degree: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Patient Schemas
# ==========================================
class PatientBase(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    phone: Optional[str] = None
    blood_group: Optional[str] = None
    allergies: Optional[str] = None
    address: Optional[str] = None
    notes: Optional[str] = None

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Visit Schemas
# ==========================================
class VisitBase(BaseModel):
    visit_type: Optional[str] = None
    symptoms: Optional[str] = None
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None
    notes: Optional[str] = None
    weight: Optional[float] = None
    blood_pressure: Optional[str] = None
    temperature: Optional[float] = None
    amount: Optional[float] = None
    followup_date: Optional[datetime] = None
    doctor_id: Optional[int] = None

class VisitCreate(VisitBase):
    patient_id: int

class Visit(VisitBase):
    id: int
    patient_id: int
    visit_date: datetime
    
    patient: Optional[Patient] = None
    doctor: Optional[Doctor] = None
    model_config = ConfigDict(from_attributes=True)


# ==========================================
# Aggregated Schemas
# ==========================================
class PatientWithVisits(Patient):
    """Detailed patient view including their visit history."""
    visits: List[Visit] = []
