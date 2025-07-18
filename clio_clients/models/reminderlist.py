# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.reminder import Reminder


class ReminderList(BaseModel):
    data: List[Reminder] = Field(..., description="Reminder List Response")
