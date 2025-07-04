# LaukExpenseCategoryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificated** | **bool** | Certificated boolean identifier for expense | [optional] 
**civil** | **bool** | Civil boolean identifier for expense | [optional] 
**created_at** | **datetime** | The time the *LaukExpenseCategory* was created (as a ISO-8601 timestamp) | [optional] 
**criminal** | **bool** | Criminal boolean identifier for expense | [optional] 
**etag** | **str** | ETag for the *LaukExpenseCategory* | [optional] 
**id** | **int** | Unique identifier for the *LaukExpenseCategory* | [optional] 
**key** | **str** | Unique key | [optional] 
**name** | **str** | Expense name | [optional] 
**rate** | **float** | Determines rate based on region param | [optional] 
**updated_at** | **datetime** | The time the *LaukExpenseCategory* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from clio_sdk.models.lauk_expense_category_base import LaukExpenseCategoryBase

# TODO update the JSON string below
json = "{}"
# create an instance of LaukExpenseCategoryBase from a JSON string
lauk_expense_category_base_instance = LaukExpenseCategoryBase.from_json(json)
# print the JSON string representation of the object
print(LaukExpenseCategoryBase.to_json())

# convert the object into a dict
lauk_expense_category_base_dict = lauk_expense_category_base_instance.to_dict()
# create an instance of LaukExpenseCategoryBase from a dict
lauk_expense_category_base_from_dict = LaukExpenseCategoryBase.from_dict(lauk_expense_category_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


