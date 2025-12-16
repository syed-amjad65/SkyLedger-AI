from typing import List, Dict

def detect_anomalies(events: List[str], expected_events: List[str]) -> Dict:
    missing = [e for e in expected_events if e not in events]
    unexpected = [e for e in events if e not in expected_events]

    # Simple scoring logic
    score = (len(missing) + len(unexpected)) / max(len(expected_events), 1)

    if score == 0:
        status = "healthy"
    elif score < 0.3:
        status = "minor_issues"
    else:
        status = "critical"

    return {
        "missing_events": missing,
        "unexpected_events": unexpected,
        "anomaly_score": round(score, 2),
        "status": status,
    }


def validate_event_sequence(events: List[str]) -> List[str]:
    issues = []

    if not events:
        issues.append("no_events_received")
        return issues

    if events[0] != "page_view":
        issues.append("missing_initial_page_view")

    if "purchase" in events and "add_to_cart" not in events:
        issues.append("purchase_without_cart")

    return issues