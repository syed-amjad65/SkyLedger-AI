from app.services.system_health import get_system_health_summary


def test_system_health_keys():
    health = get_system_health_summary()
    assert "timestamp" in health
    assert "uptime_seconds" in health
    assert "api_health" in health
    assert "module_health" in health
    assert "system_resources" in health
    assert "user_stats" in health

    assert isinstance(health["uptime_seconds"], int)
    assert isinstance(health["system_resources"], dict)
