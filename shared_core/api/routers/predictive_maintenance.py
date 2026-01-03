# app/routers/predictive_maintenance.py
from fastapi import APIRouter
from datetime import timedelta

router = APIRouter(prefix="/predictive-maintenance", tags=["predictive_maintenance"])

@router.get("/forecast", summary="Forecast maintenance risk by asset and date range")
def forecast_maintenance(asset_id: str, start_date: str, end_date: str):
    # Parse dates lightly (YYYY-MM-DD expected)
    from datetime import date
    s = date.fromisoformat(start_date)
    e = date.fromisoformat(end_date)
    days = (e - s).days + 1

    points = []
    for i in range(days):
        d = s + timedelta(days=i)
        score = round(0.2 + 0.02 * i, 2)  # simple upward trend
        level = "low" if score < 0.33 else "medium" if score < 0.66 else "high"
        points.append({"date": d.isoformat(), "risk_score": score, "risk_level": level})

    return {
        "asset_id": asset_id,
        "start_date": s.isoformat(),
        "end_date": e.isoformat(),
        "points": points,
        "version": "v0.1-dummy",
    }
