# app/routers/icu.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/icu", tags=["icu"])

# Demo in-memory ICU beds
demo_icu = {
    "KHI-General": {"hospital": "KHI-General", "beds_total": 40, "beds_free": 12, "occupancy_pct": 0.7},
    "DXB-Central": {"hospital": "DXB-Central", "beds_total": 60, "beds_free": 18, "occupancy_pct": 0.7},
    "KHI-Central": {"hospital": "KHI-Central", "beds_total": 50, "beds_free": 20, "occupancy_pct": 0.6},
}

@router.get("/", summary="List ICU capacity across hospitals")
def list_icu():
    return list(demo_icu.values())

@router.get("/{hospital}", summary="Get ICU capacity for a hospital")
def get_icu(hospital: str = "KHI-General"):
    data = demo_icu.get(hospital)
    if not data:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return data
