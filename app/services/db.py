# app/services/db.py
"""
Database session and engine setup for SkyLedger-AI.

Default: SQLite file at ./skyledger.db
Override with environment variable DATABASE_URL (e.g., postgresql://user:pass@host/dbname).
"""

from typing import Generator
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from sqlalchemy.engine import Engine

# Read DB URL from environment, fallback to local SQLite file for demo
from app.core.config import settings
DATABASE_URL: str = settings.DATABASE_URL

# Only pass check_same_thread for SQLite engines
_connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

# Create engine. echo=False to avoid noisy SQL logs; set True for debugging
engine: Engine = create_engine(DATABASE_URL, connect_args=_connect_args, echo=False)

# Session factory and scoped session for thread safety in web servers
SessionFactory = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,   # ✅ prevents DetachedInstanceError
    bind=engine
)

SessionLocal = scoped_session(SessionFactory)

# Base class for ORM models
Base = declarative_base()


def get_db() -> Generator:
    """
    Dependency generator for FastAPI endpoints.

    Usage in FastAPI:
        from app.services.db import get_db
        def endpoint(db = Depends(get_db)):
            # db is a SQLAlchemy Session
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
