# LogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *LogEntry* | [optional] 
**etag** | **str** | ETag for the *LogEntry* | [optional] 
**type** | **str** | The type of the *LogEntry* | [optional] 
**accessed_at** | **datetime** | The time the item was last accessed (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *LogEntry* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *LogEntry* was last updated (as a ISO-8601 timestamp) | [optional] 
**item** | [**PolymorphicObjectBase**](PolymorphicObjectBase.md) |  | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from clio_sdk.models.log_entry import LogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LogEntry from a JSON string
log_entry_instance = LogEntry.from_json(json)
# print the JSON string representation of the object
print(LogEntry.to_json())

# convert the object into a dict
log_entry_dict = log_entry_instance.to_dict()
# create an instance of LogEntry from a dict
log_entry_from_dict = LogEntry.from_dict(log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


