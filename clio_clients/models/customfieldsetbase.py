# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.parenttype.parenttype import ParentType


class CustomFieldSetBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *CustomFieldSet* was created (as a ISO-8601 timestamp)",
    )
    displayed: Optional[bool] = Field(
        None,
        description="Whether or not the *CustomFieldSet* should be displayed by default.",
    )
    etag: Optional[str] = Field(None, description="ETag for the *CustomFieldSet*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *CustomFieldSet*"
    )
    name: Optional[str] = Field(None, description="The name of the custom field set.")
    parent_type: Optional[ParentType] = Field(
        None, description="Type of object the *CustomFieldSet* is for."
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *CustomFieldSet* was last updated (as a ISO-8601 timestamp)",
    )
