# app/schemas/inventory.py
from pydantic import BaseModel, Field
from typing import Dict
from datetime import datetime

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
