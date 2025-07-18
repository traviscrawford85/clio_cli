# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.mattercontacts import MatterContacts


class MatterContactsList(BaseModel):
    data: List[MatterContacts] = Field(..., description="MatterContacts List Response")
