from fastapi import FastAPI

app = FastAPI(
    title="SkyLedger AI",
    description="Multi-industry operational intelligence platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "SkyLedger AI API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}