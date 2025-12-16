from pydantic import BaseModel, Field
from typing import List


class AnomalyRequest(BaseModel):
    campaign: str = Field(..., description="Campaign or funnel being analyzed")
    events: List[str] = Field(..., description="List of events received")
    expected_events: List[str] = Field(..., description="List of expected events")


class AnomalyResponse(BaseModel):
    campaign: str
    missing_events: List[str]
    unexpected_events: List[str]
    anomaly_score: float
    status: str


class EventValidationRequest(BaseModel):
    session_id: str = Field(..., description="User session identifier")
    events: List[str] = Field(..., description="Events captured in the session")


class EventValidationResponse(BaseModel):
    session_id: str
    valid: bool
    issues: List[str]