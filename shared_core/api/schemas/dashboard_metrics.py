from pydantic import BaseModel
from typing import List, Dict, Any

class DashboardRequest(BaseModel):
    metrics: List[str]
    filters: Dict[str, Any] = {}

class DashboardResponse(BaseModel):
    results: Dict[str, Any]
    generated_at: str

from pydantic import BaseModel
from typing import List


class MetricPoint(BaseModel):
    label: str
    value: float


class AssetHealthSummary(BaseModel):
    asset_id: str
    average_risk: float
    highest_risk: float
    status: str


class CXSummary(BaseModel):
    campaign: str
    anomaly_score: float
    status: str


class PlatformOverview(BaseModel):
    system_status: str
    total_assets: int
    high_risk_assets: int
    active_campaigns: int
    critical_campaigns: int
from pydantic import BaseModel
from typing import Dict, Any

class CXSummary(BaseModel):
    total_events: int
    anomalies_detected: int
    top_issue: str
    summary_details: Dict[str, Any] = {}
from pydantic import BaseModel
from typing import Dict, Any

class PlatformOverview(BaseModel):
    total_users: int
    active_users: int
    total_assets: int
    healthy_assets: int
    critical_assets: int
    summary: Dict[str, Any] = {}

