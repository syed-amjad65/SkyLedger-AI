from pydantic import BaseModel
from typing import Dict, List, Any


class ActivityDashboardResponse(BaseModel):
    total_users: int
    total_audit_logs: int
    role_distribution: Dict[str, int]
    recent_actions: List[Dict[str, Any]]
    modules: List[str]