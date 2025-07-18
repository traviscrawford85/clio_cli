# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.state4 import State4


class ReminderBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *Reminder* was created (as a ISO-8601 timestamp)",
    )
    duration: Optional[int] = Field(
        None, description="Time in minutes to remind user before the subject"
    )
    etag: Optional[str] = Field(None, description="ETag for the *Reminder*")
    id: Optional[int] = Field(None, description="Unique identifier for the *Reminder*")
    next_delivery_at: Optional[str] = Field(
        None,
        description="The time the *Reminder* will be delivered (as a ISO-8601 timestamp)",
    )
    state: Optional[State4] = Field(
        None, description="The current state of the *Reminder*"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *Reminder* was last updated (as a ISO-8601 timestamp)",
    )
