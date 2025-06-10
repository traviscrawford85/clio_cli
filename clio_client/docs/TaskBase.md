# TaskBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Task* | [optional] 
**etag** | **str** | ETag for the *Task* | [optional] 
**name** | **str** | The name of the *Task* | [optional] 
**status** | **str** | Status of the *Task*. (Note that users without advanced tasks can only have either complete or pending) | [optional] 
**description** | **str** | A detailed description of the *Task*. This Task supports rich text when setting the field &#x60;description_text_type&#x60; to &#x60;rich_text&#x60;. With supported tags such as &#x60;&lt;a&gt;&#x60;, &#x60;&lt;b&gt;&#x60;, &#x60;&lt;br&gt;&#x60;, &#x60;&lt;div&gt;&#x60;, &#x60;&lt;em&gt;&#x60;, &#x60;&lt;i&gt;&#x60; &#x60;&lt;li&gt;&#x60;, &#x60;&lt;ol&gt;&#x60;, &#x60;&lt;p&gt;&#x60;, &#x60;&lt;s&gt;&#x60;, &#x60;&lt;strong&gt;&#x60;, &#x60;&lt;u&gt;&#x60; and &#x60;&lt;ul&gt;&#x60;. This Task also supports attributes such as &#x60;href&#x60;, &#x60;rel&#x60;, &#x60;type&#x60;, and &#x60;target&#x60;. | [optional] 
**description_text_type** | **str** | The text type of the *Task* | [optional] 
**priority** | **str** | The priority of the *Task* | [optional] 
**due_at** | **date** | The date the *Task* is due (as a ISO-8601 date) | [optional] 
**permission** | **str** | The permission of the *Task* | [optional] 
**completed_at** | **datetime** | The time the *Task* was completed (as a ISO-8601 timestamp) | [optional] 
**notify_completion** | **bool** | Whether to notify the assigner of the task&#39;s completion | [optional] 
**statute_of_limitations** | **bool** | Whether the task is a statute of limitations | [optional] 
**time_estimated** | **int** | Time the *Task* should take to complete | [optional] 
**created_at** | **datetime** | The time the *Task* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Task* was last updated (as a ISO-8601 timestamp) | [optional] 
**time_entries_count** | **int** | The number of time entries associated with this task | [optional] 

## Example

```python
from clio_sdk.models.task_base import TaskBase

# TODO update the JSON string below
json = "{}"
# create an instance of TaskBase from a JSON string
task_base_instance = TaskBase.from_json(json)
# print the JSON string representation of the object
print(TaskBase.to_json())

# convert the object into a dict
task_base_dict = task_base_instance.to_dict()
# create an instance of TaskBase from a dict
task_base_from_dict = TaskBase.from_dict(task_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


