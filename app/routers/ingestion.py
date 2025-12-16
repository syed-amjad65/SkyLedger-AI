from fastapi import APIRouter

from app.schemas.ingestion import IngestionRequest, IngestionResponse
from app.services.ingestion import validate_records, process_records

router = APIRouter(
    prefix="/ingest",
    tags=["Data Ingestion"],
)


@router.post("/json", response_model=IngestionResponse)
def ingest_json(request: IngestionRequest):
    issues = validate_records(request.records)
    processed = process_records(request.records)

    status = "success" if len(issues) == 0 else "partial_success"

    return IngestionResponse(
        source=request.source,
        total_records=len(request.records),
        processed_records=processed,
        status=status,
        issues=issues,
    )