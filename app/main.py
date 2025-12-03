from app.services.forecast import baseline_forecast
from app.services.inventory import allocate_seats
from app.services.analytics import validate_events

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
    demand = baseline_forecast(req.route, req.horizon_days)
    return ForecastResponse(
        route=req.route,
        forecasted_demand=demand,
        method="EMSR-b",
        generated_at=datetime.utcnow()
    )


@app.post("/inventory", response_model=InventoryResponse)
def inventory(req: InventoryRequest):
    allocated = allocate_seats(req.total_seats)
    return InventoryResponse(
        route=req.route,
        total_seats=req.total_seats,
        allocated=allocated,
        overbooking_strategy=f"{int(req.overbooking_pct*100)}% buffer",
        generated_at=datetime.utcnow()
    )


@app.post("/anomaly", response_model=AnomalyResponse)
def anomaly(req: AnomalyRequest):
    result = validate_events(req.campaign, req.events_checked)
    return AnomalyResponse(
        campaign=result["campaign"],
        events_checked=result["events_checked"],
        anomalies_detected=result["anomalies_detected"],
        flags=result["flags"],
        generated_at=datetime.utcnow()
    )

