
async def list_matters(self, limit=5) -> List[Matter]:
    logger.debug("Fetching matters")
    raw = await self.call("Matter#index", query_params={"limit": limit})
    logger.debug("Raw matters response: %s", raw)
    return [Matter.model_validate(item) for item in raw["data"]]

async def list_tasks(self, limit=5) -> List[Task]:
    logger.debug("Fetching tasks")
    raw = await self.call("Task#index", query_params={"limit": limit})
    logger.debug("Raw tasks response: %s", raw)
    return [Task.model_validate(item) for item in raw["data"]]

async def list_contacts(self, limit=5) -> List[Contact]:
    logger.debug("Fetching contacts")
    raw = await self.call("Contact#index", query_params={"limit": limit})
    logger.debug("Raw contacts response: %s", raw)
    return [Contact.model_validate(item) for item in raw["data"]]
