# PracticeAreaBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *PracticeArea* | [optional] 
**etag** | **str** | ETag for the *PracticeArea* | [optional] 
**created_at** | **datetime** | The time the *PracticeArea* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *PracticeArea* was last updated (as a ISO-8601 timestamp) | [optional] 
**name** | **str** | The name of the *PracticeArea* | [optional] 
**category** | **str** | The practice area category associated with the *PracticeArea*  | [optional] 
**code** | **str** | The code of the *PracticeArea* | [optional] 

## Example

```python
from clio_sdk.models.practice_area_base import PracticeAreaBase

# TODO update the JSON string below
json = "{}"
# create an instance of PracticeAreaBase from a JSON string
practice_area_base_instance = PracticeAreaBase.from_json(json)
# print the JSON string representation of the object
print(PracticeAreaBase.to_json())

# convert the object into a dict
practice_area_base_dict = practice_area_base_instance.to_dict()
# create an instance of PracticeAreaBase from a dict
practice_area_base_from_dict = PracticeAreaBase.from_dict(practice_area_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


