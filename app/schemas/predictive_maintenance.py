from pydantic import BaseModel, Field
from datetime import date
from typing import List


class MaintenanceForecastRequest(BaseModel):
    asset_id: str = Field(..., description="Unique ID of the aircraft, engine, or asset")
    start_date: date = Field(..., description="Start date for the forecast window")
    end_date: date = Field(..., description="End date for the forecast window")


class DailyRiskPoint(BaseModel):
    date: date
    risk_score: float
    risk_level: str


class MaintenanceForecastResponse(BaseModel):
    asset_id: str
    start_date: date
    end_date: date
    points: List[DailyRiskPoint]
    model_version: str = "v0.1-dummy"