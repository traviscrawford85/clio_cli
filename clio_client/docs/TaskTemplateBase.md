# TaskTemplateBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *TaskTemplate* | [optional] 
**etag** | **str** | ETag for the *TaskTemplate* | [optional] 
**name** | **str** | The name of the *TaskTemplate* | [optional] 
**description** | **str** | The text body of the *TaskTemplate*. This TaskTemplate supports rich text when setting the field &#x60;detail_text_type&#x60; to &#x60;rich_text&#x60;. With supported tags such as &#x60;&lt;a&gt;&#x60;, &#x60;&lt;b&gt;&#x60;, &#x60;&lt;br&gt;&#x60;, &#x60;&lt;div&gt;&#x60;, &#x60;&lt;em&gt;&#x60;, &#x60;&lt;i&gt;&#x60; &#x60;&lt;li&gt;&#x60;, &#x60;&lt;ol&gt;&#x60;, &#x60;&lt;p&gt;&#x60;, &#x60;&lt;s&gt;&#x60;, &#x60;&lt;strong&gt;&#x60;, &#x60;&lt;u&gt;&#x60; and &#x60;&lt;ul&gt;&#x60;. This TaskTemplate also supports attributes such as &#x60;href&#x60;, &#x60;rel&#x60;, &#x60;type&#x60;, and &#x60;target&#x60;. | [optional] 
**description_text_type** | **str** | The type of text in the description field. | [optional] 
**priority** | **str** | *TaskTemplate* priority | [optional] 
**private** | **bool** | Whether the *TaskTemplate* is private. | [optional] 
**created_at** | **datetime** | The time the *TaskTemplate* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *TaskTemplate* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from clio_sdk.models.task_template_base import TaskTemplateBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateBase from a JSON string
task_template_base_instance = TaskTemplateBase.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateBase.to_json())

# convert the object into a dict
task_template_base_dict = task_template_base_instance.to_dict()
# create an instance of TaskTemplateBase from a dict
task_template_base_from_dict = TaskTemplateBase.from_dict(task_template_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


