# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type23 import Type23


class NotificationMethodBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *NotificationMethod* was created (as a ISO-8601 timestamp)",
    )
    email_address: Optional[str] = Field(
        None,
        description="Email address to send the notification to (only for email type)",
    )
    etag: Optional[str] = Field(None, description="ETag for the *NotificationMethod*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *NotificationMethod*"
    )
    is_default_email_address: Optional[bool] = Field(
        None,
        description="A boolean that is returned only on notification method objects that are relevant e.g. Email notification or Alternative Email",
    )
    type: Optional[Type23] = Field(
        None, description="Human readable description of the type of notification"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *NotificationMethod* was last updated (as a ISO-8601 timestamp)",
    )
