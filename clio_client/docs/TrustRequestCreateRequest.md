# TrustRequestCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TrustRequestCreateRequestData**](TrustRequestCreateRequestData.md) |  | 

## Example

```python
from clio_sdk.models.trust_request_create_request import TrustRequestCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrustRequestCreateRequest from a JSON string
trust_request_create_request_instance = TrustRequestCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TrustRequestCreateRequest.to_json())

# convert the object into a dict
trust_request_create_request_dict = trust_request_create_request_instance.to_dict()
# create an instance of TrustRequestCreateRequest from a dict
trust_request_create_request_from_dict = TrustRequestCreateRequest.from_dict(trust_request_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


