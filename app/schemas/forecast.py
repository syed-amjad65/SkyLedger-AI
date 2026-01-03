# app/schemas/forecast.py
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class ForecastRequest(BaseModel):
    route: str = Field(..., example="DXB-LHR")
    horizon_days: int = Field(14, ge=1, le=90, example=14)

class ForecastResponse(BaseModel):
    route: str
    forecasted_demand: List[int]
    method: str
    generated_at: datetime
