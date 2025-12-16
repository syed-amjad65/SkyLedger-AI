from fastapi import APIRouter, Depends
from app.schemas.cx_analytics import AnomalyRequest, AnomalyResponse
from app.services.cx_analytics import detect_anomaly
from app.core.security import require_role

router = APIRouter(
    prefix="/cx",
    tags=["CX Analytics"],
)


# ✅ Only ANALYST can run anomaly detection
@router.post("/anomaly", response_model=AnomalyResponse)
def anomaly_detection(request: AnomalyRequest, current_user=Depends(require_role("analyst"))):
    return detect_anomaly(request)