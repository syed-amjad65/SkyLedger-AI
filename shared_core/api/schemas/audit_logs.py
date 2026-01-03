from pydantic import BaseModel
from typing import Dict


class AuditLogEntry(BaseModel):
    timestamp: str
    username: str
    action: str
    details: Dict