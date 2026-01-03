# app/main.py
from fastapi import FastAPI

# Routers
from app.routers.flight_manager import router as flight_router
from app.routers.inventory import router as inventory_router
from app.routers.forecast import router as forecast_router
from app.routers.anomaly import router as anomaly_router
from app.routers.predictive_maintenance import router as pm_router
from app.routers.icu import router as icu_router
app = FastAPI(title="SkyLedger-AI (Demo Mode)")

# Register routers once
app.include_router(flight_router)
app.include_router(inventory_router)
app.include_router(forecast_router)
app.include_router(anomaly_router)
app.include_router(pm_router)
app.include_router(icu_router)
