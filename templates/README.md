# Clio SDK

An async Python client SDK generated from Clio's OpenAPI spec.

## Features
- Fully async `httpx` client
- Pydantic request/response models
- Automatic retries and pagination
- Grouped service interfaces and implementations
- CLI-extensible with Jinja templates

## Install
```bash
pip install .
```

## Usage
```python
from clio_sdk import ClioSDK

sdk = ClioSDK(base_url="https://api.clio.com", token="your-token")
matters = await sdk.matters.list_matters()
```