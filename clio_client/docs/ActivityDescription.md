# ActivityDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *ActivityDescription* | [optional] 
**etag** | **str** | ETag for the *ActivityDescription* | [optional] 
**name** | **str** | The name of the *ActivityDescription* | [optional] 
**visible_to_co_counsel** | **bool** | A toggle that determines if a co-counsel user of the firm can have access to this activity description | [optional] 
**created_at** | **datetime** | The time the *ActivityDescription* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *ActivityDescription* was last updated (as a ISO-8601 timestamp) | [optional] 
**default** | **bool** | Whether it is the user&#39;s default activity description | [optional] 
**type** | **str** | The type of the *ActivityDescription* | [optional] 
**utbms_activity_id** | **int** | The UTBMS activity id if the *ActivityDescription* is a UTBMS activity description | [optional] 
**utbms_task_name** | **str** | The UTBMS activity task name if attached to a UTBMS activity description | [optional] 
**utbms_task_id** | **int** | The UTBMS activity task id if attached to a UTBMS activity description | [optional] 
**xero_service_code** | **str** | Custom Xero service code for this activity description | [optional] 
**accessible_to_user** | **bool** | Determines if activity description is accessible to user | [optional] 
**category_type** | **str** | Activity category rate type. Either hourly or flat fee | [optional] 
**currency** | [**CurrencyBase**](CurrencyBase.md) |  | [optional] 
**groups** | [**List[GroupBase]**](GroupBase.md) | Group | [optional] 
**rate** | [**ActivityDescriptionRateBase**](ActivityDescriptionRateBase.md) |  | [optional] 
**utbms_task** | [**UtbmsCodeBase**](UtbmsCodeBase.md) |  | [optional] 
**utbms_activity** | [**UtbmsCodeBase**](UtbmsCodeBase.md) |  | [optional] 

## Example

```python
from clio_sdk.models.activity_description import ActivityDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityDescription from a JSON string
activity_description_instance = ActivityDescription.from_json(json)
# print the JSON string representation of the object
print(ActivityDescription.to_json())

# convert the object into a dict
activity_description_dict = activity_description_instance.to_dict()
# create an instance of ActivityDescription from a dict
activity_description_from_dict = ActivityDescription.from_dict(activity_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


