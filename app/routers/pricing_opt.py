from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/pricing", tags=["pricing"])

@router.get("/elasticity/{route_code}/{fare_class}")
def get_elasticity(route_code: str, fare_class: str, db: Session = Depends(get_db)):
    # Placeholder values
    return {"route_code": route_code, "fare_class": fare_class, "elasticity": -1.2, "confidence": 0.72}

@router.post("/recommendation")
def recommend_price(payload: dict, db: Session = Depends(get_db)):
    route = payload.get("route_code")
    fare = payload.get("fare_class")
    current = float(payload.get("current_price", 100))
    elasticity = -1.2  # demo value
    rec = current * (1 - 0.05 if elasticity < -1.0 else 0.0)
    return {
        "route_code": route,
        "fare_class": fare,
        "current_price": current,
        "recommended_price": round(rec, 2),
        "rationale": "Elasticity-based adjustment"
    }
