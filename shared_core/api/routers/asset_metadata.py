from fastapi import APIRouter, Depends, HTTPException
from app.schemas.asset_metadata import AssetMetadata, CampaignMetadata
from app.services.asset_metadata import get_all_assets, get_asset_by_id, get_all_campaigns
from app.core.security import require_any_role

router = APIRouter(
    prefix="/metadata",
    tags=["Asset Metadata"],
)

# ✅ Only ADMIN can view all assets
@router.get("/assets", response_model=list[AssetMetadata])
def list_assets(current_user=Depends(require_any_role(["admin"]))):
    return get_all_assets()

# ✅ Only ADMIN can view a single asset
@router.get("/assets/{asset_id}", response_model=AssetMetadata)
def get_asset(asset_id: str, current_user=Depends(require_any_role(["admin"]))):
    asset = get_asset_by_id(asset_id)
    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

# ✅ Only ANALYST can view campaign metadata
@router.get("/campaigns", response_model=list[CampaignMetadata])
def list_campaigns(current_user=Depends(require_any_role(["analyst"]))):
    return get_all_campaigns()
