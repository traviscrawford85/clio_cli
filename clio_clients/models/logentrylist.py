# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.logentry import LogEntry


class LogEntryList(BaseModel):
    data: List[LogEntry] = Field(..., description="LogEntry List Response")
