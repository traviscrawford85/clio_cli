# TaskTemplateCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascading** | **bool** | Determines if the TaskTemplate has a due date that is derived from another TaskTemplate. (Note that if false, no other cascading information will be checked) | [optional] 
**cascading_offset** | **int** | The amount of time that will differentiate the cascaded TaskTemplate from its parent. | [optional] 
**cascading_offset_polarity** | **str** | Determines whether or not the cascading_offset occurs before or after its parent. | [optional] 
**cascading_offset_type** | **str** | Determines the quantity of the cascading offset (e.g. CalendarDays, CalendarWeeks etc.) | [optional] 
**cascading_source** | [**TaskTemplateCreateRequestDataCascadingSource**](TaskTemplateCreateRequestDataCascadingSource.md) |  | [optional] 
**description** | **str** | Longer description of the TaskTemplate. This TaskTemplate supports rich text when the &#x60;description_text_type&#x60; field is set to &#x60;rich_text&#x60;. With supported tags such as &#x60;&lt;a&gt;&#x60;, &#x60;&lt;b&gt;&#x60;, &#x60;&lt;br&gt;&#x60;, &#x60;&lt;div&gt;&#x60;, &#x60;&lt;em&gt;&#x60;, &#x60;&lt;i&gt;&#x60; &#x60;&lt;li&gt;&#x60;, &#x60;&lt;ol&gt;&#x60;, &#x60;&lt;p&gt;&#x60;, &#x60;&lt;s&gt;&#x60;, &#x60;&lt;strong&gt;&#x60;, &#x60;&lt;u&gt;&#x60; and &#x60;&lt;ul&gt;&#x60;. This TaskTemplate also supports attributes such as &#x60;href&#x60;, &#x60;rel&#x60;, &#x60;type&#x60;, and &#x60;target&#x60;. | [optional] 
**description_text_type** | **str** | The type of text in the description field. | [optional] [default to 'plain_text']
**name** | **str** | Short name for the TaskTemplate. | 
**priority** | **str** | Priority of the task. | [optional] [default to 'Normal']
**private** | **bool** | Whether or not this TaskTemplate should be private. | [optional] 
**reminder_templates** | [**List[TaskTemplateCreateRequestDataReminderTemplatesInner]**](TaskTemplateCreateRequestDataReminderTemplatesInner.md) |  | [optional] 
**task_template_list** | [**TaskTemplateCreateRequestDataTaskTemplateList**](TaskTemplateCreateRequestDataTaskTemplateList.md) |  | [optional] 

## Example

```python
from clio_sdk.models.task_template_create_request_data import TaskTemplateCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of TaskTemplateCreateRequestData from a JSON string
task_template_create_request_data_instance = TaskTemplateCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(TaskTemplateCreateRequestData.to_json())

# convert the object into a dict
task_template_create_request_data_dict = task_template_create_request_data_instance.to_dict()
# create an instance of TaskTemplateCreateRequestData from a dict
task_template_create_request_data_from_dict = TaskTemplateCreateRequestData.from_dict(task_template_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


