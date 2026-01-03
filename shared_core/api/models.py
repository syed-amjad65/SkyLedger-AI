# app/models.py
"""
SQLAlchemy ORM models for SkyLedger-AI.
Defines tables for Users, Audit Logs, Flights, Adjustments, ICU Beds.
"""

from datetime import datetime, date
from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Text
from sqlalchemy.sql import func
from app.services.db import Base  # unified Base via shim

# --- Identity and audit ---

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    role = Column(String(50), nullable=False)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    username = Column(String(150), nullable=False)
    action = Column(String(150), nullable=False)
    details = Column(Text, nullable=True)

# --- Aviation RM ---

class Flight(Base):
    __tablename__ = "flights"
    id = Column(String(64), primary_key=True, index=True)  # e.g., AUH-LHR-2026-01-15
    route_code = Column(String(16), index=True)
    departure_date = Column(Date, index=True)
    capacity = Column(Integer)
    bookings = Column(Integer, default=0)
    revenue = Column(Float, default=0.0)
    pos = Column(String(4))          # point of sale
    od = Column(String(16))          # origin-destination

class Adjustment(Base):
    __tablename__ = "adjustments"
    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(String(64), index=True)
    type = Column(String(32))        # overbooking, decrement, closure
    value = Column(Float)
    note = Column(String(256))
    created_by = Column(String(64))
    created_at = Column(DateTime, default=datetime.utcnow)

# --- Healthcare ICU ---

class ICUBed(Base):
    __tablename__ = "icu_beds"
    id = Column(Integer, primary_key=True, index=True)
    hospital_id = Column(String(32), index=True)
    ward = Column(String(64))
    bed_number = Column(String(16), index=True)
    status = Column(String(16), default="free")  # free/occupied/maintenance
    patient_id = Column(String(64))
    assigned_at = Column(DateTime)
    released_at = Column(DateTime)
