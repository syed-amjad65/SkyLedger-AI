from app.services.audit_logs import audit_log_store, log_event, get_all_logs, get_logs_by_user, get_logs_by_action


def setup_function():
    # clear in-memory store before each test
    audit_log_store.clear()


def test_log_and_query():
    # log events
    log_event("alice", "create_user", {"username": "bob"})
    log_event("alice", "delete_user", {"username": "charlie"})
    log_event("dave", "create_user", {"username": "eve"})

    all_logs = get_all_logs()
    assert len(all_logs) == 3

    alice_logs = get_logs_by_user("alice")
    assert len(alice_logs) == 2
    assert all(log["username"] == "alice" for log in alice_logs)

    create_logs = get_logs_by_action("create_user")
    assert len(create_logs) == 2
    assert all(log["action"] == "create_user" for log in create_logs)
