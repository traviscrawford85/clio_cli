# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.bankaccount import BankAccount


class BankAccountList(BaseModel):
    data: List[BankAccount] = Field(..., description="BankAccount List Response")
