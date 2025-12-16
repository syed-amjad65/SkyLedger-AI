from fastapi import APIRouter, Depends, HTTPException
from app.core.security import require_superadmin
from app.schemas.user_management import (
    CreateUserRequest,
    UpdateRoleRequest,
    UserResponse,
)
from app.schemas.audit_logs import AuditLogEntry
from app.services.user_management import (
    list_users,
    create_user,
    update_user_role,
    delete_user,
)
from app.services.audit_logs import (
    get_all_logs,
    get_logs_by_user,
    get_logs_by_action,
)

router = APIRouter(
    prefix="/superadmin",
    tags=["SuperAdmin"],
)


# ✅ System overview (you can keep or adjust this)
@router.get("/system-overview")
def system_overview(current_user=Depends(require_superadmin())):
    return {
        "status": "OK",
        "modules": [
            "Predictive Maintenance",
            "CX Analytics",
            "Dashboard Metrics",
            "Data Ingestion",
            "Asset Metadata",
            "Authentication",
            "RBAC",
            "User Management",
            "Audit Logs",
        ],
        "message": "SuperAdmin access verified"
    }


# ✅ User management endpoints
@router.get("/users", response_model=list[UserResponse])
def get_all_users(current_user=Depends(require_superadmin())):
    return list_users()


@router.post("/users", response_model=UserResponse)
def add_user(request: CreateUserRequest, current_user=Depends(require_superadmin())):
    user = create_user(
        username=request.username,
        password=request.password,
        role=request.role,
        actor=current_user["username"],
    )
    if user is None:
        raise HTTPException(status_code=400, detail="User already exists")
    return user


@router.put("/users/{username}", response_model=UserResponse)
def change_role(username: str, request: UpdateRoleRequest, current_user=Depends(require_superadmin())):
    user = update_user_role(
        username=username,
        new_role=request.role,
        actor=current_user["username"],
    )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{username}")
def remove_user(username: str, current_user=Depends(require_superadmin())):
    result = delete_user(username, actor=current_user["username"])
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


# ✅ Audit log endpoints (SuperAdmin only)
@router.get("/audit/logs", response_model=list[AuditLogEntry])
def view_all_logs(current_user=Depends(require_superadmin())):
    return get_all_logs()


@router.get("/audit/logs/user/{username}", response_model=list[AuditLogEntry])
def view_logs_by_user(username: str, current_user=Depends(require_superadmin())):
    return get_logs_by_user(username)


@router.get("/audit/logs/action/{action}", response_model=list[AuditLogEntry])
def view_logs_by_action(action: str, current_user=Depends(require_superadmin())):
    return get_logs_by_action(action)