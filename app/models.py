# app/models.py
"""
SQLAlchemy ORM models for SkyLedger-AI.
Defines the database tables for Users and Audit Logs.
"""

from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.services.db import Base


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
