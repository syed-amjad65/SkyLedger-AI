from typing import List
from app.schemas.dashboard_metrics import (
    MetricPoint,
    AssetHealthSummary,
    CXSummary,
    PlatformOverview,
)


def generate_asset_health_summary() -> List[AssetHealthSummary]:
    # Dummy data for dashboard
    return [
        AssetHealthSummary(
            asset_id="A320-AP-BNB",
            average_risk=0.42,
            highest_risk=0.78,
            status="medium",
        ),
        AssetHealthSummary(
            asset_id="B777-AP-XYZ",
            average_risk=0.25,
            highest_risk=0.40,
            status="low",
        ),
    ]


def generate_cx_summary() -> List[CXSummary]:
    return [
        CXSummary(
            campaign="Winter Sale",
            anomaly_score=0.12,
            status="healthy",
        ),
        CXSummary(
            campaign="Holiday Promo",
            anomaly_score=0.45,
            status="minor_issues",
        ),
    ]


def generate_platform_overview() -> PlatformOverview:
    return PlatformOverview(
        system_status="operational",
        total_assets=12,
        high_risk_assets=3,
        active_campaigns=5,
        critical_campaigns=1,
    )