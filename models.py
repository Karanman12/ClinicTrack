import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Numeric, Float
from sqlalchemy.orm import relationship
from database import Base

class ClinicSettings(Base):
    """Stores global clinic profile information."""
    __tablename__ = "clinic_settings"
    
    id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(150), nullable=False, default="ClinicTrack Pro")
    doctor_name = Column(String(150), nullable=True)
    phone = Column(String(50), nullable=True)
    address = Column(Text, nullable=True)
    logo_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Doctor(Base):
    """Represents doctors working in the clinic."""
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=True)
    specialization = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    visits = relationship("Visit", back_populates="doctor")


class Patient(Base):
    """Represents a clinic patient."""
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    phone = Column(String(20), nullable=True)
    blood_group = Column(String(10), nullable=True)
    allergies = Column(Text, nullable=True)
    address = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    visits = relationship("Visit", back_populates="patient", cascade="all, delete-orphan")


class Visit(Base):
    """Represents a clinical encounter mapping patients to doctors."""
    __tablename__ = "visits"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True)
    
    # Clinical info
    visit_type = Column(String(50), nullable=True)  # e.g., Consultation, Follow-up, Routine
    symptoms = Column(Text, nullable=True)
    diagnosis = Column(Text, nullable=True)
    prescription = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    
    # Vitals
    weight = Column(Float, nullable=True)           # In kg
    blood_pressure = Column(String(20), nullable=True) # e.g., "120/80"
    temperature = Column(Float, nullable=True)      # In Fahrenheit or Celsius
    
    # Billing & Logistics
    amount = Column(Numeric(10, 2), nullable=True, default=0.0)
    followup_date = Column(DateTime, nullable=True)
    visit_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    patient = relationship("Patient", back_populates="visits")
    doctor = relationship("Doctor", back_populates="visits")
