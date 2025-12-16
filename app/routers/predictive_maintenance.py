from fastapi import APIRouter

from app.schemas.predictive_maintenance import (
    MaintenanceForecastRequest,
    MaintenanceForecastResponse,
)
from app.services.predictive_maintenance import generate_dummy_risk_curve

router = APIRouter(
    prefix="/predictive-maintenance",
    tags=["Predictive Maintenance"],
)


@router.post("/forecast", response_model=MaintenanceForecastResponse)
def forecast_maintenance(request: MaintenanceForecastRequest):
    """
    Returns a dummy maintenance risk forecast for a given asset over a date range.
    """
    points = generate_dummy_risk_curve(request.start_date, request.end_date)

    return MaintenanceForecastResponse(
        asset_id=request.asset_id,
        start_date=request.start_date,
        end_date=request.end_date,
        points=points,
    )