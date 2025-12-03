import json
from datetime import datetime
from pathlib import Path

LEDGER_PATH = Path("logs/ledger.jsonl")

def log_event(endpoint: str, request: dict, response_summary: dict) -> None:
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "endpoint": endpoint,
        "request": request,
        "response": response_summary
    }
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
