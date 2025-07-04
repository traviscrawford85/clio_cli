# Webhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Webhook* | [optional] 
**etag** | **str** | ETag for the *Webhook* | [optional] 
**url** | **str** | The &#x60;https&#x60; URL to send the data to when the events are triggered | [optional] 
**fields** | **str** | Fields to be included in the webhook request | [optional] 
**shared_secret** | **str** | A shared secret used to create a signature for the payload | [optional] 
**model** | **str** | What kind of records the webhook is for | [optional] 
**status** | **str** | The current status of the webhook. | [optional] 
**events** | **List[str]** | The events your webhook is subscribed to. | [optional] 
**expires_at** | **datetime** | The time webhook will expire (as a ISO-8601 timestamp) | [optional] 
**created_at** | **datetime** | The time the *Webhook* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Webhook* was last updated (as a ISO-8601 timestamp) | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 

## Example

```python
from clio_sdk.models.webhook import Webhook

# TODO update the JSON string below
json = "{}"
# create an instance of Webhook from a JSON string
webhook_instance = Webhook.from_json(json)
# print the JSON string representation of the object
print(Webhook.to_json())

# convert the object into a dict
webhook_dict = webhook_instance.to_dict()
# create an instance of Webhook from a dict
webhook_from_dict = Webhook.from_dict(webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


