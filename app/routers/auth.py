from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import TokenResponse
from app.services.auth import authenticate_user, create_access_token
from app.core.security import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    # ✅ Token now includes role
    token = create_access_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return TokenResponse(access_token=token)


@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return current_user