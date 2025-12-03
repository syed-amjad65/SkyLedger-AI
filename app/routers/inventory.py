from fastapi import APIRouter
from app.schemas import InventoryResponse

router = APIRouter()

@router.get("", response_model=InventoryResponse, tags=["Inventory"])
def get_inventory():
    return InventoryResponse(
        route="DXB-LHR",
        total_seats=180,
        allocated={"economy": 120, "business": 50, "first": 10},
        overbooking_strategy="5% buffer",
    )
