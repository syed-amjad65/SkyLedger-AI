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