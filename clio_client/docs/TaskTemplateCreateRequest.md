# TaskTemplateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskTemplateCreateRequestData**](TaskTemplateCreateRequestData.md) |  | 

## Example

```python
from clio_sdk.models.task_template_create_request import TaskTemplateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCreateRequest from a JSON string
task_template_create_request_instance = TaskTemplateCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCreateRequest.to_json())

# convert the object into a dict
task_template_create_request_dict = task_template_create_request_instance.to_dict()
# create an instance of TaskTemplateCreateRequest from a dict
task_template_create_request_from_dict = TaskTemplateCreateRequest.from_dict(task_template_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


