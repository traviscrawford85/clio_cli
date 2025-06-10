# GitHub Copilot Instructions for clio_clients/models

## Purpose

This folder is the authoritative source for all Pydantic models representing Clio API resources. These models are used in a dynamic OpenAPI client to power a Textual CLI app for Clio data visualization and interaction.

## Responsibilities

Copilot, you are responsible for:

- Ensuring **imports are correct and all references are resolvable**, especially nested or recursive models.
- Generating missing nested models from example JSONs or the OpenAPI schema (e.g openapi_sdk.yaml).
- Applying `model_rebuild()` where necessary to resolve forward references.
- Refactoring and cleaning model definitions proactively to ensure they are syntactically valid and type-safe.
- Keeping field names **exactly aligned with the Clio API JSON** keys.
- Using proper `Optional`, `List`, and union types to represent optional and array fields.
- Organizing and splitting models across files if they become too large or tightly coupled.

## Example

```python
from pydantic import BaseModel
from typing import Optional, List
from clio_clients.models.contact import Contact

class Matter(BaseModel):
    id: int
    description: Optional[str]
    status: Optional[str]
    client: Optional[Contact]

Matter.model_rebuild()
```

## Goals

- All models should validate against real Clio API responses.

- The dynamic OpenAPI client should be able to use model_validate() on response payloads without failure.

- The CLI should display fetched entities (e.g., Tasks, Contacts, Matters) using these models without error.

Thank you for helping keep Clio models robust and usable!
