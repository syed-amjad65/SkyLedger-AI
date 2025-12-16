from datetime import datetime

# ✅ In-memory audit log store (can be replaced with DB later)
audit_log_store = []


def log_event(username: str, action: str, details: dict | None = None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "username": username,
        "action": action,
        "details": details or {},
    }
    audit_log_store.append(entry)
    return entry


def get_all_logs():
    return audit_log_store


def get_logs_by_user(username: str):
    return [log for log in audit_log_store if log["username"] == username]


def get_logs_by_action(action: str):
    return [log for log in audit_log_store if log["action"] == action]