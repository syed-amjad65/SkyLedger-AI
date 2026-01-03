# app/routers/flight_manager.py
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/flights", tags=["flights"])

# Demo in-memory data
demo_flights = {
    "EK2025": {"flight_id": "EK2025", "route": "DXB-LHR", "seats": 180, "status": "scheduled"},
    "PK300": {"flight_id": "PK300", "route": "KHI-ISB", "seats": 150, "status": "boarding"},
}

@router.get("/", summary="List all flights")
def list_flights():
    return list(demo_flights.values())

@router.get("/{flight_id}", summary="Get flight by ID")
def get_flight(flight_id: str):
    flight = demo_flights.get(flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight
