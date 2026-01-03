# app/routers/forecast.py
from fastapi import APIRouter
from datetime import datetime
from typing import List

router = APIRouter(prefix="/forecast", tags=["forecast"])

@router.get("/{route}", summary="Get demand forecast for a route")
def get_forecast(route: str, horizon_days: int = 14):
    # Demo rising demand pattern
    forecasted: List[int] = [100 + i * 5 for i in range(horizon_days)]
    return {
        "route": route,
        "forecasted_demand": forecasted,
        "method": "demo_linear_trend",
        "generated_at": datetime.utcnow().isoformat(),
    }
