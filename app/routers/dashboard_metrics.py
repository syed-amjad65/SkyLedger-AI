from fastapi import APIRouter, Depends
from app.schemas.dashboard_metrics import DashboardRequest, DashboardResponse
from app.services.dashboard_metrics import generate_dashboard_metrics
from app.core.security import require_any_role

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Metrics"],
)

# ✅ Analysts, Admins, and SuperAdmins can access dashboards
@router.post("/", response_model=DashboardResponse)
def dashboard_metrics(request: DashboardRequest, current_user=Depends(require_any_role(["analyst", "admin", "superadmin"]))):
    return generate_dashboard_metrics(request)

@router.get("/asset-health", response_model=List[AssetHealthSummary])
def asset_health():
    return generate_asset_health_summary()


@router.get("/cx-summary", response_model=List[CXSummary])
def cx_summary():
    return generate_cx_summary()


@router.get("/overview", response_model=PlatformOverview)
def overview():
    return generate_platform_overview()