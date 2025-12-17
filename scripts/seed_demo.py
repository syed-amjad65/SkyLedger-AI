# scripts/seed_demo.py
"""
Seed script for SkyLedger-AI demo database.
Creates tables and inserts demo users and a few audit logs.
Run: python scripts/seed_demo.py
"""

from app.services.db import engine, Base
from app.services.user_management import create_user
from app.services.audit_logs import log_event_db
import os


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created.")


def seed_users():
    # Create demo users (passwords are short for demo only)
    create_user("superadmin", "superadmin123", "superadmin", actor="system")
    create_user("admin", "admin123", "admin", actor="system")
    create_user("analyst", "analyst123", "analyst", actor="system")
    print("✅ Demo users seeded.")


def seed_logs():
    log_event_db("system", "seed", {"message": "initial seed"})
    log_event_db("superadmin", "login", {"success": True})
    print("✅ Demo audit logs seeded.")


if __name__ == "__main__":
    print("🚀 Starting SkyLedger-AI database seed...")
    create_tables()
    seed_users()
    seed_logs()
    print("✅ Seeding complete.")
    print("📦 Database file:", os.getenv("DATABASE_URL", "sqlite:///./skyledger.db"))
