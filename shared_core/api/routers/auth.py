from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

from app.schemas.user import Token
from app.core.security import SECRET_KEY  # ✅ use SAME key as security.py

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

# ✅ Password hashing context (you can start with plain passwords if you want)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ✅ In-memory user store (simple roles for now)
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",  # plain-text for now
        "role": "admin",
    },
    "analyst": {
        "username": "analyst",
        "password": "analyst123",
        "role": "analyst",
    },
    "superadmin": {
        "username": "superadmin",
        "password": "superadmin123",
        "role": "superadmin",
    },
}


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return None
    if password != user["password"]:
        return None
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Login endpoint for Swagger and clients.
    Accepts form data: username, password.
    Returns: access_token (JWT) + token_type.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(
        data={"sub": user["username"], "role": user["role"]}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
