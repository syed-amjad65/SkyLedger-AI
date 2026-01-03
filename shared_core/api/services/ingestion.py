from typing import List, Dict


def validate_records(records: List[Dict]) -> List[str]:
    issues = []

    for idx, record in enumerate(records):
        if "id" not in record:
            issues.append(f"Record {idx} missing 'id' field")
        if "timestamp" not in record:
            issues.append(f"Record {idx} missing 'timestamp' field")

    return issues


def process_records(records: List[Dict]) -> int:
    # Dummy ETL: pretend we processed all valid records
    return len(records)
from typing import Dict, Any

def ingest_data(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Dummy ingestion logic.
    Replace with real ingestion pipeline later.
    """
    # Simulate ingestion success
    return {
        "status": "success",
        "records_received": len(payload.get("records", [])),
        "message": "Data ingested successfully"
    }
