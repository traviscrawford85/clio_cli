# FolderUpdateRequestDataParent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the parent object. | [optional] 
**type** | **str** | Type of parent object: * \&quot;Folder\&quot; represents a specified folder on Clio by folder id. It if specified when you add / move an item to a folder. * \&quot;Contact\&quot; represents a contact folder on Clio identified by contact id. It is specified when you add / move an item to a contact folder. A contact folder will be created for the specified contact if none exists already. * \&quot;Matter\&quot; represents a matter folder on Clio identified by matter id. It is specified when you add / move an item to a matter folder.  | [optional] 

## Example

```python
from clio_sdk.models.folder_update_request_data_parent import FolderUpdateRequestDataParent

# TODO update the JSON string below
json = "{}"
# create an instance of FolderUpdateRequestDataParent from a JSON string
folder_update_request_data_parent_instance = FolderUpdateRequestDataParent.from_json(json)
# print the JSON string representation of the object
print(FolderUpdateRequestDataParent.to_json())

# convert the object into a dict
folder_update_request_data_parent_dict = folder_update_request_data_parent_instance.to_dict()
# create an instance of FolderUpdateRequestDataParent from a dict
folder_update_request_data_parent_from_dict = FolderUpdateRequestDataParent.from_dict(folder_update_request_data_parent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


