# app/services/auth.py
from passlib.context import CryptContext
from typing import Dict

# Use a PBKDF2 scheme which does not have bcrypt's 72-byte limit.
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Simple in-memory fake users DB for development/demo.
# Store hashed passwords using the chosen pwd_context.
# Keep initial demo passwords short and safe.
fake_users_db: Dict[str, Dict] = {
    "superadmin": {
        "username": "superadmin",
        "hashed_password": pwd_context.hash("superadmin123"),
        "role": "superadmin",
    },
    "admin": {
        "username": "admin",
        "hashed_password": pwd_context.hash("admin123"),
        "role": "admin",
    },
    "analyst": {
        "username": "analyst",
        "hashed_password": pwd_context.hash("analyst123"),
        "role": "analyst",
    },
}


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a stored hash.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_user(username: str):
    """
    Return user dict from fake_users_db or None.
    """
    return fake_users_db.get(username)


def authenticate_user(username: str, password: str):
    """
    Simple authentication helper for demo/testing.
    Returns user dict on success, None on failure.
    """
    user = get_user(username)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return user
