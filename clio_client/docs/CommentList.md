# CommentList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Comment]**](Comment.md) | Comment List Response | 

## Example

```python
from clio_sdk.models.comment_list import CommentList

# TODO update the JSON string below
json = "{}"
# create an instance of CommentList from a JSON string
comment_list_instance = CommentList.from_json(json)
# print the JSON string representation of the object
print(CommentList.to_json())

# convert the object into a dict
comment_list_dict = comment_list_instance.to_dict()
# create an instance of CommentList from a dict
comment_list_from_dict = CommentList.from_dict(comment_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


