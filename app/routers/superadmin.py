from fastapi import APIRouter, Depends, HTTPException
from app.core.security import require_superadmin
from app.schemas.user_management import (
    CreateUserRequest,
    UpdateRoleRequest,
    UserResponse,
)
from app.services.user_management import (
    list_users,
    create_user,
    update_user_role,
    delete_user,
)

router = APIRouter(
    prefix="/superadmin",
    tags=["SuperAdmin"],
)


@router.get("/users", response_model=list[UserResponse])
def get_all_users(current_user=Depends(require_superadmin())):
    return list_users()


@router.post("/users", response_model=UserResponse)
def add_user(request: CreateUserRequest, current_user=Depends(require_superadmin())):
    user = create_user(request.username, request.password, request.role)
    if user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return user


@router.put("/users/{username}", response_model=UserResponse)
def change_role(username: str, request: UpdateRoleRequest, current_user=Depends(require_superadmin())):
    user = update_user_role(username, request.role)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{username}")
def remove_user(username: str, current_user=Depends(require_superadmin())):
    result = delete_user(username)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}