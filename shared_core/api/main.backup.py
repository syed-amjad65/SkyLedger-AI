from fastapi import FastAPI

app = FastAPI(title="SkyLedger-AI API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
@app.get("/forecast")
def forecast():
    return {
        "route": "DXB-LHR",
        "forecasted_demand": [120, 135, 150, 160],
        "method": "EMSR-b"
    }

@app.get("/inventory")
def inventory():
    return {
        "route": "DXB-LHR",
        "total_seats": 180,
        "allocated": {"economy": 120, "business": 50, "first": 10},
        "overbooking_strategy": "5% buffer"
    }

@app.get("/anomaly")
def anomaly():
    return {
        "campaign": "WinterSale2025",
        "events_checked": 1000,
        "anomalies_detected": 3,
        "flags": ["missing_conversion", "duplicate_event", "timestamp_gap"]
    }
