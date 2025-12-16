from fastapi import APIRouter, Depends
from app.core.security import require_superadmin

router = APIRouter(
    prefix="/superadmin",
    tags=["SuperAdmin"],
)


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
        ],
        "message": "SuperAdmin access verified"
    }