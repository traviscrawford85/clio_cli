# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class MedicalRecordBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *MedicalRecord* was created (as a ISO-8601 timestamp)",
    )
    document_id: Optional[int] = Field(
        None, description="The id of the document associated with the Medical Record"
    )
    end_date: Optional[str] = Field(
        None, description="End date for *MedicalRecord* (as a ISO-8601 date)"
    )
    etag: Optional[str] = Field(None, description="ETag for the *MedicalRecord*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *MedicalRecord*"
    )
    start_date: Optional[str] = Field(
        None, description="Start date for *MedicalRecord* (as a ISO-8601 date)"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *MedicalRecord* was last updated (as a ISO-8601 timestamp)",
    )
