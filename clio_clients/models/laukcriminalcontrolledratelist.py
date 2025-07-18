# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.laukcriminalcontrolledrate import LaukCriminalControlledRate


class LaukCriminalControlledRateList(BaseModel):
    data: List[LaukCriminalControlledRate] = Field(
        ..., description="LaukCriminalControlledRate List Response"
    )
