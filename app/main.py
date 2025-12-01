from fastapi import FastAPI

app = FastAPI(title="SkyLedger-AI API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/hello")
def hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}