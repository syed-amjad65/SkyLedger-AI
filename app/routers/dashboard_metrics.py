from fastapi import APIRouter
from typing import List

from app.schemas.dashboard_metrics import (
    AssetHealthSummary,
    CXSummary,
    PlatformOverview,
)
from app.services.dashboard_metrics import (
    generate_asset_health_summary,
    generate_cx_summary,
    generate_platform_overview,
)

router = APIRouter(
    prefix="/metrics",
    tags=["Dashboard Metrics"],
)


@router.get("/asset-health", response_model=List[AssetHealthSummary])
def asset_health():
    return generate_asset_health_summary()


@router.get("/cx-summary", response_model=List[CXSummary])
def cx_summary():
    return generate_cx_summary()


@router.get("/overview", response_model=PlatformOverview)
def overview():
    return generate_platform_overview()