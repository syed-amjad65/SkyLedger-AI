from app.services.forecast import baseline_forecast
from app.services.inventory import allocate_seats
from app.services.analytics import validate_events

def test_baseline_forecast_lengths():
    assert len(baseline_forecast("DXB-LHR", 2)) == 2
    assert len(baseline_forecast("DXB-LHR", 7)) == 4

def test_allocate_seats_sum():
    alloc = allocate_seats(180)
    assert sum(alloc.values()) == 180

def test_validate_events_flags():
    result = validate_events("WinterSale2025", 1000)
    assert result["anomalies_detected"] == 3
    assert len(result["flags"]) == 3
