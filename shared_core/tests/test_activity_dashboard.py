from app.services.activity_dashboard import get_activity_summary


def test_activity_summary_structure():
    summary = get_activity_summary()
    assert "total_users" in summary
    assert "total_audit_logs" in summary
    assert "role_distribution" in summary
    assert "recent_actions" in summary
    assert "modules" in summary

    assert isinstance(summary["total_users"], int)
    assert isinstance(summary["total_audit_logs"], int)
    assert isinstance(summary["modules"], list)
