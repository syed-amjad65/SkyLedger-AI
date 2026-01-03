# Simple in-memory audit log store
audit_log_store = []

# app/services/audit_logs.py
"""
Database-backed audit logging service for SkyLedger-AI.
Stores audit logs in the audit_logs table using SQLAlchemy ORM.
"""

from typing import Dict, List, Any
from sqlalchemy.orm import Session
from app.services.db import SessionLocal
from app.models import AuditLog
import json
from datetime import datetime


def _get_db() -> Session:
    return SessionLocal()


def log_event_db(username: str, action: str, details: Dict | None = None) -> Dict[str, Any]:
    """
    Insert a new audit log entry into the database.
    """
    db = _get_db()
    try:
        entry = AuditLog(
            username=username,
            action=action,
            details=json.dumps(details or {}),
        )
        db.add(entry)
        db.commit()
        db.refresh(entry)

        return {
            "id": entry.id,
            "timestamp": entry.timestamp.isoformat() if entry.timestamp else datetime.utcnow().isoformat(),
            "username": entry.username,
            "action": entry.action,
            "details": details or {},
        }
    finally:
        db.close()


def get_all_logs() -> List[Dict[str, Any]]:
    """
    Return all audit logs in ascending order.
    """
    db = _get_db()
    try:
        rows = db.query(AuditLog).order_by(AuditLog.id.asc()).all()
        return [
            {
                "id": r.id,
                "timestamp": r.timestamp.isoformat() if r.timestamp else None,
                "username": r.username,
                "action": r.action,
                "details": json.loads(r.details) if r.details else {},
            }
            for r in rows
        ]
    finally:
        db.close()


def get_logs_by_user(username: str) -> List[Dict[str, Any]]:
    """
    Return all logs created by a specific user.
    """
    db = _get_db()
    try:
        rows = db.query(AuditLog).filter(AuditLog.username == username).all()
        return [
            {
                "id": r.id,
                "timestamp": r.timestamp.isoformat() if r.timestamp else None,
                "username": r.username,
                "action": r.action,
                "details": json.loads(r.details) if r.details else {},
            }
            for r in rows
        ]
    finally:
        db.close()


def get_logs_by_action(action: str) -> List[Dict[str, Any]]:
    """
    Return all logs matching a specific action.
    """
    db = _get_db()
    try:
        rows = db.query(AuditLog).filter(AuditLog.action == action).all()
        return [
            {
                "id": r.id,
                "timestamp": r.timestamp.isoformat() if r.timestamp else None,
                "username": r.username,
                "action": r.action,
                "details": json.loads(r.details) if r.details else {},
            }
            for r in rows
        ]
    finally:
        db.close()
def add_audit_log(entry: dict):
    audit_log_store.append(entry)

