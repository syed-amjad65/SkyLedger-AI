# app/services/user_management.py
"""
Database-backed user management service for SkyLedger-AI.
Handles CRUD operations for users using SQLAlchemy ORM.
"""

from typing import Optional, Dict, Any, List
from sqlalchemy.orm import Session
from app.services.db import SessionLocal
from app.models import User
from app.services.auth import pwd_context
from app.services.audit_logs import log_event_db


def _get_db() -> Session:
    return SessionLocal()


def list_users() -> List[Dict[str, Any]]:
    db = _get_db()
    try:
        users = db.query(User).all()
        return [{"username": u.username, "role": u.role} for u in users]
    finally:
        db.close()


def create_user(username: str, password: str, role: str, actor: str = "system") -> Optional[Dict[str, Any]]:
    db = _get_db()
    try:
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            return None

        hashed = pwd_context.hash(password)
        user = User(username=username, hashed_password=hashed, role=role)
        db.add(user)
        db.commit()
        db.refresh(user)

        log_event_db(actor, "create_user", {"username": username, "role": role})

        return {"username": user.username, "role": user.role}
    finally:
        db.close()


def update_user_role(username: str, new_role: str, actor: str = "system") -> Optional[Dict[str, Any]]:
    db = _get_db()
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None

        old_role = user.role
        user.role = new_role
        db.commit()
        db.refresh(user)

        log_event_db(actor, "update_role", {"username": username, "old_role": old_role, "new_role": new_role})

        return {"username": user.username, "role": user.role}
    finally:
        db.close()


def delete_user(username: str, actor: str = "system") -> Optional[bool]:
    db = _get_db()
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return None

        role = user.role
        db.delete(user)
        db.commit()

        log_event_db(actor, "delete_user", {"username": username, "role": role})

        return True
    finally:
        db.close()
