from fastapi import APIRouter, HTTPException

from app.schemas.asset_metadata import AssetMetadata, CampaignMetadata
from app.services.asset_metadata import (
    get_all_assets,
    get_asset_by_id,
    get_all_campaigns,
)

router = APIRouter(
    prefix="/metadata",
    tags=["Asset Metadata"],
)


@router.get("/assets", response_model=list[AssetMetadata])
def list_assets():
    return get_all_assets()


@router.get("/assets/{asset_id}", response_model=AssetMetadata)
def get_asset(asset_id: str):
    asset = get_asset_by_id(asset_id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset


@router.get("/campaigns", response_model=list[CampaignMetadata])
def list_campaigns():
    return get_all_campaigns()