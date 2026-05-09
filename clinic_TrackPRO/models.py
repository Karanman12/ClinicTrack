"""
models.py — ORM models for ClinicTrack

Defines Patient and Visit tables with a one-to-many relationship:
  Patient (1) ──▶ (many) Visits
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Patient(Base):
    """Represents a patient registered at the clinic."""

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(10), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # One patient can have many visits (newest first by default)
    visits = relationship(
        "Visit",
        back_populates="patient",
        order_by="Visit.visit_date.desc()",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.name}')>"


class Visit(Base):
    """Represents a single clinic visit for a patient."""

    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    symptoms = Column(Text, nullable=False)
    prescription = Column(Text, nullable=False)
    notes = Column(Text, default="")
    amount = Column(Integer, nullable=True)
    visit_date = Column(DateTime, default=datetime.utcnow)

    # Back-reference to the parent patient
    patient = relationship("Patient", back_populates="visits")

    def __repr__(self):
        return f"<Visit(id={self.id}, date='{self.visit_date}')>"


class Settings(Base):
    """Stores clinic configuration and doctor information."""

    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    clinic_name = Column(String(150), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    degree = Column(String(50), nullable=True)
    phone = Column(String(15), nullable=True)
    address = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Settings(id={self.id}, clinic='{self.clinic_name}')>"
