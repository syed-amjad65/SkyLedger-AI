from fastapi import APIRouter
from app.schemas import AnomalyResponse

router = APIRouter()

@router.get("", response_model=AnomalyResponse, tags=["Anomaly"])
def get_anomaly():
    return AnomalyResponse(
        campaign="WinterSale2025",
        events_checked=1000,
        anomalies_detected=3,
        flags=["missing_conversion", "duplicate_event", "timestamp_gap"],
    )
