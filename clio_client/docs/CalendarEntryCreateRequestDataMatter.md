# CalendarEntryCreateRequestDataMatter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier for a single Matter associated with the CalendarEntry. Use the keyword &#x60;null&#x60; to specify no association. | [optional] 

## Example

```python
from clio_sdk.models.calendar_entry_create_request_data_matter import CalendarEntryCreateRequestDataMatter

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEntryCreateRequestDataMatter from a JSON string
calendar_entry_create_request_data_matter_instance = CalendarEntryCreateRequestDataMatter.from_json(json)
# print the JSON string representation of the object
print(CalendarEntryCreateRequestDataMatter.to_json())

# convert the object into a dict
calendar_entry_create_request_data_matter_dict = calendar_entry_create_request_data_matter_instance.to_dict()
# create an instance of CalendarEntryCreateRequestDataMatter from a dict
calendar_entry_create_request_data_matter_from_dict = CalendarEntryCreateRequestDataMatter.from_dict(calendar_entry_create_request_data_matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


