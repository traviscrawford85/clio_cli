# FolderUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FolderUpdateRequestData**](FolderUpdateRequestData.md) |  | 

## Example

```python
from clio_sdk.models.folder_update_request import FolderUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateRequest from a JSON string
folder_update_request_instance = FolderUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateRequest.to_json())

# convert the object into a dict
folder_update_request_dict = folder_update_request_instance.to_dict()
# create an instance of FolderUpdateRequest from a dict
folder_update_request_from_dict = FolderUpdateRequest.from_dict(folder_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


