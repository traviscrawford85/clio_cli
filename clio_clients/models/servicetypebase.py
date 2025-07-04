# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ServiceTypeBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *ServiceType* was created (as a ISO-8601 timestamp)",
    )
    default: Optional[bool] = Field(
        None, description="Whether *ServiceType* is default for the current user"
    )
    description: Optional[str] = Field(
        None, description="A detailed description of the *ServiceType*"
    )
    etag: Optional[str] = Field(None, description="ETag for the *ServiceType*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *ServiceType*"
    )
    system_id: Optional[int] = Field(None, description="Server ID")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *ServiceType* was last updated (as a ISO-8601 timestamp)",
    )
