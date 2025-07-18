# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.bill import Bill


class BillList(BaseModel):
    data: List[Bill] = Field(..., description="Bill List Response")
