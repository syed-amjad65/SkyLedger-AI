# app/routers/inventory.py
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/inventory", tags=["inventory"])

@router.get("/{route}", summary="Get inventory allocation for a route")
def get_inventory(route: str, total_seats: int = 180, overbooking_pct: float = 0.05):
    allocated = {
        "economy": int(total_seats * (1 - overbooking_pct) * 0.7),
        "business": int(total_seats * (1 - overbooking_pct) * 0.2),
        "first": int(total_seats * (1 - overbooking_pct) * 0.1),
    }
    return {
        "route": route,
        "total_seats": total_seats,
        "allocated": allocated,
        "overbooking_strategy": f"{int(overbooking_pct*100)}% overbooking",
        "generated_at": datetime.utcnow().isoformat(),
    }
