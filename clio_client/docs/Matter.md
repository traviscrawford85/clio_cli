# Matter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the *Matter* | [optional] 
**etag** | **str** | ETag for the *Matter* | [optional] 
**number** | **int** | The number given to the *Matter* within an account | [optional] 
**display_number** | **str** | The reference and label of the *Matter*. Depending on the account&#39;s manual_matter_numbering setting, this is either read only (generated) or customizable. | [optional] 
**custom_number** | **str** | User defined custom number of the *Matter* | [optional] 
**currency** | [**CurrencyBase**](CurrencyBase.md) |  | [optional] 
**description** | **str** | The detailed description of the *Matter* | [optional] 
**status** | **str** | The current status of the *Matter* | [optional] 
**location** | **str** | The location of the *Matter* | [optional] 
**client_reference** | **str** | Client Reference string for external uses | [optional] 
**client_id** | **int** | Client ID | [optional] 
**billable** | **bool** | Whether this matter is billable | [optional] 
**maildrop_address** | **str** | A unique Maildrop email address for the matter | [optional] 
**billing_method** | **str** | Billing method of this matter | [optional] 
**open_date** | **date** | The date the matter was set to open (as a ISO-8601 date) | [optional] 
**close_date** | **date** | The date the matter was set to closed (as a ISO-8601 date) | [optional] 
**pending_date** | **date** | The date the matter was set to pending (as a ISO-8601 date) | [optional] 
**created_at** | **datetime** | The time the *Matter* was created (as a ISO-8601 timestamp) | [optional] 
**updated_at** | **datetime** | The time the *Matter* was last updated (as a ISO-8601 timestamp) | [optional] 
**shared** | **bool** | Whether the matter is currently shared with Clio Connect | [optional] 
**has_tasks** | **bool** | Whether or not the matter has any tasks. | [optional] 
**last_activity_date** | **date** | The greatest date out of all of the activities on the matter (as a ISO-8601 date) | [optional] 
**matter_stage_updated_at** | **datetime** | The date the matter stage was last updated (as a ISO-8601 date) | [optional] 
**client** | [**ContactBase**](ContactBase.md) |  | [optional] 
**contingency_fee** | [**ContingencyFeeBase**](ContingencyFeeBase.md) |  | [optional] 
**custom_rate** | [**MatterCustomRate**](MatterCustomRate.md) |  | [optional] 
**evergreen_retainer** | [**EvergreenRetainerBase**](EvergreenRetainerBase.md) |  | [optional] 
**folder** | [**FolderBase**](FolderBase.md) |  | [optional] 
**group** | [**GroupBase**](GroupBase.md) |  | [optional] 
**matter_budget** | [**MatterBudgetBase**](MatterBudgetBase.md) |  | [optional] 
**matter_stage** | [**MatterStageBase**](MatterStageBase.md) |  | [optional] 
**originating_attorney** | [**UserBase**](UserBase.md) |  | [optional] 
**practice_area** | [**PracticeAreaBase**](PracticeAreaBase.md) |  | [optional] 
**responsible_attorney** | [**UserBase**](UserBase.md) |  | [optional] 
**responsible_staff** | [**UserBase**](UserBase.md) |  | [optional] 
**statute_of_limitations** | [**TaskBase**](TaskBase.md) |  | [optional] 
**user** | [**UserBase**](UserBase.md) |  | [optional] 
**legal_aid_uk_matter** | [**LegalAidUkMatterBase**](LegalAidUkMatterBase.md) |  | [optional] 
**account_balances** | [**List[AccountBalanceBase]**](AccountBalanceBase.md) | AccountBalance | [optional] 
**custom_field_values** | [**List[CustomFieldValue]**](CustomFieldValue.md) | CustomFieldValue | [optional] 
**custom_field_set_associations** | [**List[CustomFieldSetAssociationBase]**](CustomFieldSetAssociationBase.md) | CustomFieldSetAssociation | [optional] 
**matter_bill_recipients** | [**List[MatterBillRecipient]**](MatterBillRecipient.md) | MatterBillRecipient | [optional] 
**relationships** | [**List[RelationshipBase]**](RelationshipBase.md) | Relationship | [optional] 
**task_template_list_instances** | [**List[TaskTemplateListInstaceBase]**](TaskTemplateListInstaceBase.md) | TaskTemplateListInstace | [optional] 
**split_invoice_payers** | [**List[SplitInvoicePayerBase]**](SplitInvoicePayerBase.md) | SplitInvoicePayer | [optional] 

## Example

```python
from clio_sdk.models.matter import Matter

# TODO update the JSON string below
json = "{}"
# create an instance of Matter from a JSON string
matter_instance = Matter.from_json(json)
# print the JSON string representation of the object
print(Matter.to_json())

# convert the object into a dict
matter_dict = matter_instance.to_dict()
# create an instance of Matter from a dict
matter_from_dict = Matter.from_dict(matter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


