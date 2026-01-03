# app/api/routes_health.py

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/ping")
def health_ping():
    """
    Simple health check endpoint to verify the API is running.
    """
    return {"status": "ok", "service": "SkyLedger-AI"}
