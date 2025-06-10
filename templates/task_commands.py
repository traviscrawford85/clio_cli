"""
This file defines the commands interface for creating and modifying task-related data in Clio.

It wraps low-level clio_client operations (e.g., taskcreate.sync_detailed) and exposes a simpler,
developer-friendly function like `create_task()` that accepts an SDK-level model.

Copilot Prompt:
- Wrap the clio_client function for task creation.
- Accept a `clio_sdk.models.task.Task` as input, adapt it into a clio_client JSON body using an adapter.
- Call the clio_client function, check for successful responses, and return the SDK-level model.
- If errors occur, raise helpful exceptions to aid debugging.
- This module should only contain "write" or "mutating" operations (POST, PUT, PATCH, DELETE).
"""


from clio_client.models.taskcreate_json_body import TaskcreateJsonBody
from clio_client.tasks.taskcreate import sync_detailed as raw_create_task
from clio_sdk.adapters.task import from_taskshow
from clio_sdk.generated_models.task import Task


def create_task(task: Task) -> Task:
    json_body = TaskcreateJsonBody(
        description=task.description,
        status=task.status,
        priority=task.priority,
        due_date=task.due_date,
        matter_id=task.matter_id,
        assignee_id=task.assignee_id,
    )
    resp = raw_create_task(client=get_client(), body=json_body)
    if resp.status_code == 201:
        return from_taskshow(resp.parsed)
    raise Exception(f"Task creation failed: {resp.status_code}")
