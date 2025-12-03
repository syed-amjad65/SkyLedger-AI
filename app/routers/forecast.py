from fastapi import APIRouter
from app.schemas import ForecastResponse

router = APIRouter()

@router.get("", response_model=ForecastResponse, tags=["Forecast"])
def get_forecast():
    return ForecastResponse(
        route="DXB-LHR",
        forecasted_demand=[120, 135, 150, 160],
        method="EMSR-b",
    )
