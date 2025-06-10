# SplitInvoiceBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *SplitInvoice* | [optional] 
**bill_id** | **int** | The ID of the bill that was split. | [optional] 
**linked_invoices_display_numbers** | **List[str]** | Display numbers of all invoices split with this one. | [optional] 
**linked_invoices_ids** | **List[int]** | IDs of all invoices split with this one. | [optional] 
**split_connection_id** | **str** | UUID to determine which invoices are split together. | [optional] 
**split_portion** | **float** | The percentage of the bill that the payer is responsible for. | [optional] 
**etag** | **str** | ETag for the *SplitInvoice* | [optional] 
**created_at** | **datetime** | The time the *SplitInvoice* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *SplitInvoice* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from clio_sdk.models.split_invoice_base import SplitInvoiceBase

# TODO update the JSON string below
json = "{}"
# create an instance of SplitInvoiceBase from a JSON string
split_invoice_base_instance = SplitInvoiceBase.from_json(json)
# print the JSON string representation of the object
print(SplitInvoiceBase.to_json())

# convert the object into a dict
split_invoice_base_dict = split_invoice_base_instance.to_dict()
# create an instance of SplitInvoiceBase from a dict
split_invoice_base_from_dict = SplitInvoiceBase.from_dict(split_invoice_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


