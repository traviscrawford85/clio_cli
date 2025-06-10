# Copilot Instruction:
# This folder contains all Pydantic models auto-generated or hand-refined from Clio's OpenAPI schema.
# These models are used dynamically in a Textual CLI app via a runtime OpenAPI client.
# As the models custodian, ensure:
# - All nested objects are explicitly defined and correctly imported.
# - Forward references are properly resolved (e.g., via `model_rebuild()`).
# - Optional and recursive fields follow Pydantic typing (e.g., `Optional[List[Model]]`).
# - Model field names match Clio's JSON schema exactly.
# - If a model references another model (e.g., Contact inside Matter), import and use that model.
# - You may proactively refactor and organize models for correctness, including moving or renaming.
# - Validate via `model_validate(data)` or `**data` unpacking in client calls.

# Example usage in dynamic client:
#    from clio_clients.models.matter import Matter
#    Matter.model_rebuild()
#    matter = Matter.model_validate(response_data)
