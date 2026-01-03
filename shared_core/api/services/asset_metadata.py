from typing import List
from app.schemas.asset_metadata import AssetMetadata, CampaignMetadata


def get_all_assets() -> List[AssetMetadata]:
    return [
        AssetMetadata(
            asset_id="A320-AP-BNB",
            asset_type="Aircraft",
            manufacturer="Airbus",
            year_of_manufacture=2012,
            cycles=18500,
            status="active",
        ),
        AssetMetadata(
            asset_id="B777-AP-XYZ",
            asset_type="Aircraft",
            manufacturer="Boeing",
            year_of_manufacture=2015,
            cycles=12200,
            status="active",
        ),
    ]


def get_asset_by_id(asset_id: str) -> AssetMetadata | None:
    for asset in get_all_assets():
        if asset.asset_id == asset_id:
            return asset
    return None


def get_all_campaigns() -> List[CampaignMetadata]:
    return [
        CampaignMetadata(
            campaign="Winter Sale",
            expected_events=["page_view", "add_to_cart", "purchase"],
            owner="Digital Marketing",
            status="active",
        ),
        CampaignMetadata(
            campaign="Holiday Promo",
            expected_events=["page_view", "signup", "purchase"],
            owner="Growth Team",
            status="paused",
        ),
    ]