from fastapi import FastAPI
from app.routers import health, predictive_maintenance

app = FastAPI(
    title="SkyLedger AI",
    description="Multi-industry operational intelligence platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "SkyLedger AI API is running"}

# Register routers
app.include_router(health.router)
app.include_router(predictive_maintenance.router)