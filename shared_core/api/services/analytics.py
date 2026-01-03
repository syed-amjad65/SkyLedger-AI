def validate_events(campaign: str, events_checked: int) -> dict:
    """Basic anomaly detection stub. Add schema checks later."""
    flags = ["missing_conversion", "duplicate_event", "timestamp_gap"]
    return {
        "campaign": campaign,
        "events_checked": events_checked,
        "anomalies_detected": len(flags),
        "flags": flags
    }
