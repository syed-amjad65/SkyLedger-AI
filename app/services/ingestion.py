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