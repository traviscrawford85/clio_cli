# NoteCreateRequestData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**NoteCreateRequestDataContact**](NoteCreateRequestDataContact.md) |  | 
**var_date** | **date** | Date for the Note. (Expects an ISO-8601 date). | [optional] 
**detail** | **str** | Note body in text. This Note supports rich text when setting the &#x60;detail_text_type&#x60; field to &#x60;rich_text&#x60;. With supported tags such as &#x60;&lt;a&gt;&#x60;, &#x60;&lt;b&gt;&#x60;, &#x60;&lt;br&gt;&#x60;, &#x60;&lt;div&gt;&#x60;, &#x60;&lt;em&gt;&#x60;, &#x60;&lt;i&gt;&#x60; &#x60;&lt;li&gt;&#x60;, &#x60;&lt;ol&gt;&#x60;, &#x60;&lt;p&gt;&#x60;, &#x60;&lt;s&gt;&#x60;, &#x60;&lt;strong&gt;&#x60;, &#x60;&lt;u&gt;&#x60; and &#x60;&lt;ul&gt;&#x60;. This Note also supports attributes such as &#x60;href&#x60;, &#x60;rel&#x60;, &#x60;type&#x60;, and &#x60;target&#x60;. | [optional] 
**detail_text_type** | **str** | The type of text in the detail field. | [optional] [default to 'plain_text']
**matter** | [**NoteCreateRequestDataMatter**](NoteCreateRequestDataMatter.md) |  | 
**notification_event_subscribers** | [**List[NoteCreateRequestDataNotificationEventSubscribersInner]**](NoteCreateRequestDataNotificationEventSubscribersInner.md) |  | [optional] 
**subject** | **str** | Note subject. | [optional] 
**type** | **str** | Note type. | 

## Example

```python
from clio_sdk.models.note_create_request_data import NoteCreateRequestData

# TODO update the JSON string below
json = "{}"
# create an instance of NoteCreateRequestData from a JSON string
note_create_request_data_instance = NoteCreateRequestData.from_json(json)
# print the JSON string representation of the object
print(NoteCreateRequestData.to_json())

# convert the object into a dict
note_create_request_data_dict = note_create_request_data_instance.to_dict()
# create an instance of NoteCreateRequestData from a dict
note_create_request_data_from_dict = NoteCreateRequestData.from_dict(note_create_request_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


