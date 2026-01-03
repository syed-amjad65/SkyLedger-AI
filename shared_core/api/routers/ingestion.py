from fastapi import APIRouter, Depends
from app.schemas.ingestion import IngestionRequest, IngestionResponse
from app.services.ingestion import ingest_data
from app.core.security import require_any_role

router = APIRouter(
    prefix="/ingestion",
    tags=["Data Ingestion"],
)

# ✅ Only ADMIN or SUPERADMIN can ingest data
@router.post("/", response_model=IngestionResponse)
def ingest(request: IngestionRequest, current_user=Depends(require_any_role(["admin", "superadmin"]))):
    return ingest_data(request.dict())
