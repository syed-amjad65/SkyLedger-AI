# app/schemas/anomaly.py
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class AnomalyRequest(BaseModel):
    campaign: str = Field(..., example="WinterSale2025")
    events_checked: int = Field(1000, ge=0, example=1000)

class AnomalyResponse(BaseModel):
    campaign: str
    events_checked: int
    anomalies_detected: int
    flags: List[str]
    generated_at: datetime
