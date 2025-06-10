
### PATCH: Clio Integration Update

**File: `clio_clients/clio_dynamic_client.py`**
```python
import os
from clio_clients.tasks_client import ClioTaskClient

class ClioDynamicClient:
    ...
    def task_client(self) -> ClioTaskClient:
        return ClioTaskClient(
            token=self.headers["Authorization"].replace("Bearer ", ""),
            base_url=self.base_url,
        )

    async def get_task(self, id: int):
        client = self.task_client()
        return await client.get_task(id)

    async def update_task(self, id: int, payload: dict):
        client = self.task_client()
        return await client.update_task(id, payload)
```

**File: `clio_dashboard/clio_app.py`**
```python
# Add update_task method to expose it to the views if needed
class DashboardApp(App):
    ...
    async def update_task(self, task_id: int, payload: dict):
        return await self.client.update_task(task_id, payload)
```
