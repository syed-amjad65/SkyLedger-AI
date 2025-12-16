from fastapi import FastAPI
from app.routers import (
    health,
    predictive_maintenance,
    cx_analytics,
    dashboard_metrics,
    ingestion,
    asset_metadata,
    auth,
    superadmin,   # ✅ NEW: SuperAdmin router
)

app = FastAPI(
    title="SkyLedger AI",
    description="Multi-industry operational intelligence platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {"message": "SkyLedger AI API is running"}


# ✅ Register routers in clean, professional order
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(superadmin.router)          # ✅ SuperAdmin endpoints
app.include_router(predictive_maintenance.router)
app.include_router(cx_analytics.router)
app.include_router(dashboard_metrics.router)
app.include_router(ingestion.router)
app.include_router(asset_metadata.router)