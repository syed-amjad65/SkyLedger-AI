def baseline_forecast(route: str, horizon_days: int) -> list:
    """Simple baseline forecast. Replace later with time-series model."""
    base = [120, 135, 150, 160]
    return base[:min(len(base), horizon_days)]
