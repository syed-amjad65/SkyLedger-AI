from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime

class ForecastRequest(BaseModel):
    route: str = Field(..., example="DXB-LHR")
    horizon_days: int = Field(14, ge=1, le=90, example=14)

class ForecastResponse(BaseModel):
    route: str
    forecasted_demand: List[int]
    method: str
    generated_at: datetime

class InventoryRequest(BaseModel):
    route: str = Field(..., example="DXB-LHR")
    total_seats: int = Field(180, ge=1, example=180)
    overbooking_pct: float = Field(0.05, ge=0.0, le=0.2, example=0.05)

class InventoryResponse(BaseModel):
    route: str
    total_seats: int
    allocated: Dict[str, int]
    overbooking_strategy: str
    generated_at: datetime

class AnomalyRequest(BaseModel):
    campaign: str = Field(..., example="WinterSale2025")
    events_checked: int = Field(1000, ge=0, example=1000)

class AnomalyResponse(BaseModel):
    campaign: str
    events_checked: int
    anomalies_detected: int
    flags: List[str]
    generated_at: datetime
