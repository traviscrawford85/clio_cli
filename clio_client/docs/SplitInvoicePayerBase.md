# SplitInvoicePayerBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *SplitInvoicePayer* | [optional] 
**contact_id** | **int** | The ID of the payer for the split invoice. | [optional] 
**matter_id** | **int** | The ID of the Matter that has split invoicing enabled. | [optional] 
**send_to_bill_recipients** | **bool** | Boolean to indicate if the sent bills should include bill recipients by default. | [optional] 
**split_portion** | **float** | The percentage of the bill that the payer is responsible for. | [optional] 
**etag** | **str** | ETag for the *SplitInvoicePayer* | [optional] 
**created_at** | **datetime** | The time the *SplitInvoicePayer* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *SplitInvoicePayer* was last updated (as a ISO-8601 timestamp) | [optional] 

## Example

```python
from clio_sdk.models.split_invoice_payer_base import SplitInvoicePayerBase

# TODO update the JSON string below
json = "{}"
# create an instance of SplitInvoicePayerBase from a JSON string
split_invoice_payer_base_instance = SplitInvoicePayerBase.from_json(json)
# print the JSON string representation of the object
print(SplitInvoicePayerBase.to_json())

# convert the object into a dict
split_invoice_payer_base_dict = split_invoice_payer_base_instance.to_dict()
# create an instance of SplitInvoicePayerBase from a dict
split_invoice_payer_base_from_dict = SplitInvoicePayerBase.from_dict(split_invoice_payer_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


