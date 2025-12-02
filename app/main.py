from fastapi import FastAPI, Query
from typing import Dict
from datetime import datetime
from app.schemas import (
    ForecastRequest, ForecastResponse,
    InventoryRequest, InventoryResponse,
    AnomalyRequest, AnomalyResponse
)

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="SkyLedger-AI API", version="0.1.0",description="Airline & Digital Analytics API")

@app.get("/health", response_model=Dict[str, str])
def health():
    return {"status": "ok"}

@app.get("/hello", response_model=Dict[str, str])
def hello(name: str = Query("World", min_length=1, example="Syed")):
    return {"message": f"Hello {name}, SkyLedger-AI"}

class ForecastResponse(BaseModel):
    route: str
    forecasted_demand: List[int]
    method: str

class InventoryResponse(BaseModel):
    route: str
    total_seats: int
    allocated: Dict[str, int]
    overbooking_strategy: str

class AnomalyResponse(BaseModel):
    campaign: str
    events_checked: int
    anomalies_detected: int
    flags: List[str]
@app.post("/forecast", response_model=ForecastResponse)
def forecast(req: ForecastRequest):
    demand = [120, 135, 150, 160][:min(4, req.horizon_days)]
    return ForecastResponse(
        route=req.route,
        forecasted_demand=demand,
        method="EMSR-b",
        generated_at=datetime.utcnow()
    )


@app.post("/inventory", response_model=InventoryResponse)
def inventory(req: InventoryRequest):
    allocated = {"economy": 120, "business": 50, "first": 10}
    return InventoryResponse(
        route=req.route,
        total_seats=req.total_seats,
        allocated=allocated,
        overbooking_strategy=f"{int(req.overbooking_pct*100)}% buffer",
        generated_at=datetime.utcnow()
    )


@app.post("/anomaly", response_model=AnomalyResponse)
def anomaly(req: AnomalyRequest):
    flags = ["missing_conversion", "duplicate_event", "timestamp_gap"]
    return AnomalyResponse(
        campaign=req.campaign,
        events_checked=req.events_checked,
        anomalies_detected=len(flags),
        flags=flags,
        generated_at=datetime.utcnow()
    )

