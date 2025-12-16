from pydantic import BaseModel, Field
from typing import List, Optional


class IngestionRequest(BaseModel):
    source: str = Field(..., description="Name of the data source")
    records: List[dict] = Field(..., description="List of JSON records to ingest")


class IngestionResponse(BaseModel):
    source: str
    total_records: int
    processed_records: int
    status: str
    issues: Optional[List[str]] = []