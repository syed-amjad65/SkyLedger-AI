from fastapi import APIRouter

from app.schemas.cx_analytics import (
    AnomalyRequest,
    AnomalyResponse,
    EventValidationRequest,
    EventValidationResponse,
)
from app.services.cx_analytics import detect_anomalies, validate_event_sequence

router = APIRouter(
    prefix="/cx",
    tags=["CX Analytics"],
)


@router.post("/anomaly", response_model=AnomalyResponse)
def anomaly_detection(request: AnomalyRequest):
    result = detect_anomalies(request.events, request.expected_events)

    return AnomalyResponse(
        campaign=request.campaign,
        missing_events=result["missing_events"],
        unexpected_events=result["unexpected_events"],
        anomaly_score=result["anomaly_score"],
        status=result["status"],
    )


@router.post("/validate-events", response_model=EventValidationResponse)
def validate_events(request: EventValidationRequest):
    issues = validate_event_sequence(request.events)

    return EventValidationResponse(
        session_id=request.session_id,
        valid=len(issues) == 0,
        issues=issues,
    )