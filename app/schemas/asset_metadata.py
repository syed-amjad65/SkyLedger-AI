from pydantic import BaseModel
from typing import List


class AssetMetadata(BaseModel):
    asset_id: str
    asset_type: str
    manufacturer: str
    year_of_manufacture: int
    cycles: int
    status: str


class CampaignMetadata(BaseModel):
    campaign: str
    expected_events: List[str]
    owner: str
    status: str