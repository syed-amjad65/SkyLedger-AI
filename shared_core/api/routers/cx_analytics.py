from fastapi import APIRouter
from app.schemas.cx_analytics import CXAnalyticsRequest, CXAnalyticsResponse
from app.services.cx_analytics import detect_anomalies

router = APIRouter(prefix="/cx", tags=["CX Analytics"])

@router.post("/analyze", response_model=CXAnalyticsResponse)
def analyze_cx(request: CXAnalyticsRequest):
    result = detect_anomalies(request.events, request.expected_events)
    return result
