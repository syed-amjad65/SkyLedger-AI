import time
from datetime import datetime
from typing import Dict

import psutil

from app.routers.auth import fake_users_db
from app.services.audit_logs import audit_log_store

# Track when the app started (for uptime)
APP_START_TIME = datetime.utcnow()


def _get_uptime_seconds() -> int:
    now = datetime.utcnow()
    delta = now - APP_START_TIME
    return int(delta.total_seconds())


def _get_api_counters() -> Dict[str, int]:
    # For now, we approximate using audit logs length as "activity"
    total_requests = len(audit_log_store)
    total_errors = len([log for log in audit_log_store if "error" in log["action"].lower()])
    return {
        "total_requests": total_requests,
        "total_errors": total_errors,
    }


def _get_module_health() -> Dict[str, Dict[str, str]]:
    # For now, all modules are "healthy" unless you want to simulate issues
    modules = [
        "Predictive Maintenance",
        "CX Analytics",
        "Dashboard Metrics",
        "Data Ingestion",
        "Asset Metadata",
        "Authentication",
        "RBAC",
        "User Management",
        "Audit Logs",
        "Activity Dashboard",
        "System Health",
    ]

    module_health = {}
    for module in modules:
        module_health[module] = {
            "status": "healthy",
            "last_check": datetime.utcnow().isoformat(),
            "details": "Module reachable and operating normally",
        }

    return module_health


def _get_system_resources() -> Dict[str, float]:
    cpu_percent = psutil.cpu_percent(interval=0.2)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "cpu_percent": cpu_percent,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
    }


def get_system_health_summary():
    api_counters = _get_api_counters()
    module_health = _get_module_health()
    system_resources = _get_system_resources()

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "uptime_seconds": _get_uptime_seconds(),
        "api_health": {
            "total_requests": api_counters["total_requests"],
            "total_errors": api_counters["total_errors"],
        },
        "module_health": module_health,
        "system_resources": system_resources,
        "user_stats": {
            "total_users": len(fake_users_db),
            "roles": {
                role: sum(1 for u in fake_users_db.values() if u["role"] == role)
                for role in {u["role"] for u in fake_users_db.values()}
            } if fake_users_db else {},
        },
    }