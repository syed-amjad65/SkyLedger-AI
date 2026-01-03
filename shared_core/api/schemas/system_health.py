from pydantic import BaseModel
from typing import Dict, Any


class SystemHealthResponse(BaseModel):
    timestamp: str
    uptime_seconds: int
    api_health: Dict[str, int]
    module_health: Dict[str, Dict[str, str]]
    system_resources: Dict[str, float]
    user_stats: Dict[str, Any]