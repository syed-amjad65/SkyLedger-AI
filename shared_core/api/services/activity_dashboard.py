from app.routers.auth import fake_users_db
from app.services.audit_logs import audit_log_store


def get_activity_summary():
    total_users = len(fake_users_db)
    total_logs = len(audit_log_store)

    # Last 10 actions
    recent_actions = audit_log_store[-10:]

    # Role distribution
    role_counts = {}
    for user in fake_users_db.values():
        role = user["role"]
        role_counts[role] = role_counts.get(role, 0) + 1

    return {
        "total_users": total_users,
        "total_audit_logs": total_logs,
        "role_distribution": role_counts,
        "recent_actions": recent_actions,
        "modules": [
            "Predictive Maintenance",
            "CX Analytics",
            "Dashboard Metrics",
            "Data Ingestion",
            "Asset Metadata",
            "Authentication",
            "RBAC",
            "User Management",
            "Audit Logs",
        ],
    }