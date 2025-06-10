# TaskCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignee** | [**TaskCreateRequestDataAssignee**](TaskCreateRequestDataAssignee.md) |  | 
**cascading** | **bool** | Determines if the Task has a due date that is derived from another Task. (Note that if false, no other cascading information will be checked) | [optional] 
**cascading_offset** | **int** | The amount of time that will differentiate the cascaded Task from its parent. | [optional] 
**cascading_offset_polarity** | **str** | Determines whether or not the cascading_offset occurs before or after its parent. | [optional] 
**cascading_offset_type** | **str** | Determines the quantity of the cascading offset (e.g. CalendarDays, CalendarWeeks etc.) | [optional] 
**cascading_source** | **int** | The parent Task that is used to determine the due_at property of the cascaded Task | [optional] 
**description** | **str** | Longer description of the Task. This Task supports rich text when the &#x60;description_text_type&#x60; field is set to &#x60;rich_text&#x60;. With supported tags such as &#x60;&lt;a&gt;&#x60;, &#x60;&lt;b&gt;&#x60;, &#x60;&lt;br&gt;&#x60;, &#x60;&lt;div&gt;&#x60;, &#x60;&lt;em&gt;&#x60;, &#x60;&lt;i&gt;&#x60; &#x60;&lt;li&gt;&#x60;, &#x60;&lt;ol&gt;&#x60;, &#x60;&lt;p&gt;&#x60;, &#x60;&lt;s&gt;&#x60;, &#x60;&lt;strong&gt;&#x60;, &#x60;&lt;u&gt;&#x60; and &#x60;&lt;ul&gt;&#x60;. This Task also supports attributes such as &#x60;href&#x60;, &#x60;rel&#x60;, &#x60;type&#x60;, and &#x60;target&#x60;. | 
**description_text_type** | **str** | The type of text in the description field. | [optional] [default to 'plain_text']
**due_at** | **datetime** | Date when the Task must be completed by. (Expects an ISO-8601 date). | [optional] 
**matter** | [**TaskCreateRequestDataMatter**](TaskCreateRequestDataMatter.md) |  | [optional] 
**name** | **str** | Name of the Task. | 
**notify_assignee** | **bool** | Whether or not the Task should notify the assignee on creation. | [optional] 
**notify_completion** | **bool** | Whether or not the Task should notify the assigner on completion. | [optional] 
**permission** | **str** | Permission of the Task. Defaults to &#x60;public&#x60; | [optional] [default to 'public']
**priority** | **str** | Priority of the Task. | [optional] [default to 'Normal']
**status** | **str** | Task status. Users without advanced tasks are allowed to select &#x60;Complete&#x60; or &#x60;Pending&#x60; only. | [optional] [default to 'pending']
**statute_of_limitations** | **bool** | Whether or not the Task should be a statute of limitations. | [optional] 
**task_type** | [**TaskCreateRequestDataTaskType**](TaskCreateRequestDataTaskType.md) |  | [optional] 
**time_estimated** | **int** | Time the Task should take to complete. | [optional] 

## Example

```python
from clio_sdk.models.task_create_request_data import TaskCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskCreateRequestData from a JSON string
task_create_request_data_instance = TaskCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskCreateRequestData.to_json())

# convert the object into a dict
task_create_request_data_dict = task_create_request_data_instance.to_dict()
# create an instance of TaskCreateRequestData from a dict
task_create_request_data_from_dict = TaskCreateRequestData.from_dict(task_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


