# app/services/db.py
"""
Compatibility shim: re-export Base, engine, SessionLocal, get_db from app.database
so legacy imports continue to work with a single source of truth.
"""
from app.database import Base, engine, SessionLocal, get_db

__all__ = ["Base", "engine", "SessionLocal", "get_db"]
