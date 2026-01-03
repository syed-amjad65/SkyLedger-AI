# app/routers/anomaly.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/anomaly", tags=["anomaly"])

@router.get("/{campaign}", summary="Detect anomalies for a campaign")
def get_anomaly(campaign: str, events_checked: int = 1000):
    anomalies = min(events_checked // 100, 50)
    flags = []
    if anomalies > 0:
        flags.append("spike")
    if events_checked > 500:
        flags.append("volume_high")
    return {
        "campaign": campaign,
        "events_checked": events_checked,
        "anomalies_detected": anomalies,
        "flags": flags,
        "generated_at": datetime.utcnow().isoformat(),
    }
