# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from pydantic import BaseModel
from clio_clients.models.tasktemplatelist import TaskTemplateList


class TaskTemplateListShow(BaseModel):
    data: TaskTemplateList
