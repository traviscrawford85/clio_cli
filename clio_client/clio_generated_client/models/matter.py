import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.matter_base_billing_method import MatterBaseBillingMethod
from ..models.matter_base_status import MatterBaseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balance_base import AccountBalanceBase
    from ..models.contact_base import ContactBase
    from ..models.contingency_fee_base import ContingencyFeeBase
    from ..models.custom_field_set_association_base import CustomFieldSetAssociationBase
    from ..models.custom_field_value import CustomFieldValue
    from ..models.evergreen_retainer_base import EvergreenRetainerBase
    from ..models.folder_base import FolderBase
    from ..models.group_base import GroupBase
    from ..models.legal_aid_uk_matter_base import LegalAidUkMatterBase
    from ..models.matter_base_currency import MatterBaseCurrency
    from ..models.matter_bill_recipient import MatterBillRecipient
    from ..models.matter_budget_base import MatterBudgetBase
    from ..models.matter_custom_rate import MatterCustomRate
    from ..models.matter_stage_base import MatterStageBase
    from ..models.practice_area_base import PracticeAreaBase
    from ..models.relationship_base import RelationshipBase
    from ..models.split_invoice_payer_base import SplitInvoicePayerBase
    from ..models.task_base import TaskBase
    from ..models.task_template_list_instace_base import TaskTemplateListInstaceBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Matter")


@_attrs_define
class Matter:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Matter*
        etag (Union[Unset, str]): ETag for the *Matter*
        number (Union[Unset, int]): The number given to the *Matter* within an account
        display_number (Union[Unset, str]): The reference and label of the *Matter*. Depending on the account's
            manual_matter_numbering setting, this is either read only (generated) or customizable.
        custom_number (Union[Unset, str]): User defined custom number of the *Matter*
        currency (Union[Unset, MatterBaseCurrency]): Currency of the matter
        description (Union[Unset, str]): The detailed description of the *Matter*
        status (Union[Unset, MatterBaseStatus]): The current status of the *Matter*
        location (Union[Unset, str]): The location of the *Matter*
        client_reference (Union[Unset, str]): Client Reference string for external uses
        client_id (Union[Unset, int]): Client ID
        billable (Union[Unset, bool]): Whether this matter is billable
        maildrop_address (Union[Unset, str]): A unique Maildrop email address for the matter
        billing_method (Union[Unset, MatterBaseBillingMethod]): Billing method of this matter
        open_date (Union[Unset, datetime.date]): The date the matter was set to open (as a ISO-8601 date)
        close_date (Union[Unset, datetime.date]): The date the matter was set to closed (as a ISO-8601 date)
        pending_date (Union[Unset, datetime.date]): The date the matter was set to pending (as a ISO-8601 date)
        created_at (Union[Unset, datetime.datetime]): The time the *Matter* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Matter* was last updated (as a ISO-8601 timestamp)
        shared (Union[Unset, bool]): Whether the matter is currently shared with Clio Connect
        has_tasks (Union[Unset, bool]): Whether or not the matter has any tasks.
        last_activity_date (Union[Unset, datetime.date]): The greatest date out of all of the activities on the matter
            (as a ISO-8601 date)
        matter_stage_updated_at (Union[Unset, datetime.datetime]): The date the matter stage was last updated (as a
            ISO-8601 date)
        client (Union[Unset, ContactBase]):
        contingency_fee (Union[Unset, ContingencyFeeBase]):
        custom_rate (Union[Unset, MatterCustomRate]):
        evergreen_retainer (Union[Unset, EvergreenRetainerBase]):
        folder (Union[Unset, FolderBase]):
        group (Union[Unset, GroupBase]):
        matter_budget (Union[Unset, MatterBudgetBase]):
        matter_stage (Union[Unset, MatterStageBase]):
        originating_attorney (Union[Unset, UserBase]):
        practice_area (Union[Unset, PracticeAreaBase]):
        responsible_attorney (Union[Unset, UserBase]):
        responsible_staff (Union[Unset, UserBase]):
        statute_of_limitations (Union[Unset, TaskBase]):
        user (Union[Unset, UserBase]):
        legal_aid_uk_matter (Union[Unset, LegalAidUkMatterBase]):
        account_balances (Union[Unset, list['AccountBalanceBase']]): AccountBalance
        custom_field_values (Union[Unset, list['CustomFieldValue']]): CustomFieldValue
        custom_field_set_associations (Union[Unset, list['CustomFieldSetAssociationBase']]): CustomFieldSetAssociation
        matter_bill_recipients (Union[Unset, list['MatterBillRecipient']]): MatterBillRecipient
        relationships (Union[Unset, list['RelationshipBase']]): Relationship
        task_template_list_instances (Union[Unset, list['TaskTemplateListInstaceBase']]): TaskTemplateListInstace
        split_invoice_payers (Union[Unset, list['SplitInvoicePayerBase']]): SplitInvoicePayer
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    display_number: Union[Unset, str] = UNSET
    custom_number: Union[Unset, str] = UNSET
    currency: Union[Unset, "MatterBaseCurrency"] = UNSET
    description: Union[Unset, str] = UNSET
    status: Union[Unset, MatterBaseStatus] = UNSET
    location: Union[Unset, str] = UNSET
    client_reference: Union[Unset, str] = UNSET
    client_id: Union[Unset, int] = UNSET
    billable: Union[Unset, bool] = UNSET
    maildrop_address: Union[Unset, str] = UNSET
    billing_method: Union[Unset, MatterBaseBillingMethod] = UNSET
    open_date: Union[Unset, datetime.date] = UNSET
    close_date: Union[Unset, datetime.date] = UNSET
    pending_date: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    shared: Union[Unset, bool] = UNSET
    has_tasks: Union[Unset, bool] = UNSET
    last_activity_date: Union[Unset, datetime.date] = UNSET
    matter_stage_updated_at: Union[Unset, datetime.datetime] = UNSET
    client: Union[Unset, "ContactBase"] = UNSET
    contingency_fee: Union[Unset, "ContingencyFeeBase"] = UNSET
    custom_rate: Union[Unset, "MatterCustomRate"] = UNSET
    evergreen_retainer: Union[Unset, "EvergreenRetainerBase"] = UNSET
    folder: Union[Unset, "FolderBase"] = UNSET
    group: Union[Unset, "GroupBase"] = UNSET
    matter_budget: Union[Unset, "MatterBudgetBase"] = UNSET
    matter_stage: Union[Unset, "MatterStageBase"] = UNSET
    originating_attorney: Union[Unset, "UserBase"] = UNSET
    practice_area: Union[Unset, "PracticeAreaBase"] = UNSET
    responsible_attorney: Union[Unset, "UserBase"] = UNSET
    responsible_staff: Union[Unset, "UserBase"] = UNSET
    statute_of_limitations: Union[Unset, "TaskBase"] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    legal_aid_uk_matter: Union[Unset, "LegalAidUkMatterBase"] = UNSET
    account_balances: Union[Unset, list["AccountBalanceBase"]] = UNSET
    custom_field_values: Union[Unset, list["CustomFieldValue"]] = UNSET
    custom_field_set_associations: Union[Unset, list["CustomFieldSetAssociationBase"]] = UNSET
    matter_bill_recipients: Union[Unset, list["MatterBillRecipient"]] = UNSET
    relationships: Union[Unset, list["RelationshipBase"]] = UNSET
    task_template_list_instances: Union[Unset, list["TaskTemplateListInstaceBase"]] = UNSET
    split_invoice_payers: Union[Unset, list["SplitInvoicePayerBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        number = self.number

        display_number = self.display_number

        custom_number = self.custom_number

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        description = self.description

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        location = self.location

        client_reference = self.client_reference

        client_id = self.client_id

        billable = self.billable

        maildrop_address = self.maildrop_address

        billing_method: Union[Unset, str] = UNSET
        if not isinstance(self.billing_method, Unset):
            billing_method = self.billing_method.value

        open_date: Union[Unset, str] = UNSET
        if not isinstance(self.open_date, Unset):
            open_date = self.open_date.isoformat()

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        pending_date: Union[Unset, str] = UNSET
        if not isinstance(self.pending_date, Unset):
            pending_date = self.pending_date.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        shared = self.shared

        has_tasks = self.has_tasks

        last_activity_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_activity_date, Unset):
            last_activity_date = self.last_activity_date.isoformat()

        matter_stage_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.matter_stage_updated_at, Unset):
            matter_stage_updated_at = self.matter_stage_updated_at.isoformat()

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        contingency_fee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contingency_fee, Unset):
            contingency_fee = self.contingency_fee.to_dict()

        custom_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_rate, Unset):
            custom_rate = self.custom_rate.to_dict()

        evergreen_retainer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.evergreen_retainer, Unset):
            evergreen_retainer = self.evergreen_retainer.to_dict()

        folder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        matter_budget: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_budget, Unset):
            matter_budget = self.matter_budget.to_dict()

        matter_stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_stage, Unset):
            matter_stage = self.matter_stage.to_dict()

        originating_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.originating_attorney, Unset):
            originating_attorney = self.originating_attorney.to_dict()

        practice_area: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.practice_area, Unset):
            practice_area = self.practice_area.to_dict()

        responsible_attorney: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_attorney, Unset):
            responsible_attorney = self.responsible_attorney.to_dict()

        responsible_staff: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.responsible_staff, Unset):
            responsible_staff = self.responsible_staff.to_dict()

        statute_of_limitations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statute_of_limitations, Unset):
            statute_of_limitations = self.statute_of_limitations.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        legal_aid_uk_matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal_aid_uk_matter, Unset):
            legal_aid_uk_matter = self.legal_aid_uk_matter.to_dict()

        account_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_balances, Unset):
            account_balances = []
            for account_balances_item_data in self.account_balances:
                account_balances_item = account_balances_item_data.to_dict()
                account_balances.append(account_balances_item)

        custom_field_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_values, Unset):
            custom_field_values = []
            for custom_field_values_item_data in self.custom_field_values:
                custom_field_values_item = custom_field_values_item_data.to_dict()
                custom_field_values.append(custom_field_values_item)

        custom_field_set_associations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_set_associations, Unset):
            custom_field_set_associations = []
            for custom_field_set_associations_item_data in self.custom_field_set_associations:
                custom_field_set_associations_item = custom_field_set_associations_item_data.to_dict()
                custom_field_set_associations.append(custom_field_set_associations_item)

        matter_bill_recipients: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matter_bill_recipients, Unset):
            matter_bill_recipients = []
            for matter_bill_recipients_item_data in self.matter_bill_recipients:
                matter_bill_recipients_item = matter_bill_recipients_item_data.to_dict()
                matter_bill_recipients.append(matter_bill_recipients_item)

        relationships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()
                relationships.append(relationships_item)

        task_template_list_instances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.task_template_list_instances, Unset):
            task_template_list_instances = []
            for task_template_list_instances_item_data in self.task_template_list_instances:
                task_template_list_instances_item = task_template_list_instances_item_data.to_dict()
                task_template_list_instances.append(task_template_list_instances_item)

        split_invoice_payers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.split_invoice_payers, Unset):
            split_invoice_payers = []
            for split_invoice_payers_item_data in self.split_invoice_payers:
                split_invoice_payers_item = split_invoice_payers_item_data.to_dict()
                split_invoice_payers.append(split_invoice_payers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if number is not UNSET:
            field_dict["number"] = number
        if display_number is not UNSET:
            field_dict["display_number"] = display_number
        if custom_number is not UNSET:
            field_dict["custom_number"] = custom_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if location is not UNSET:
            field_dict["location"] = location
        if client_reference is not UNSET:
            field_dict["client_reference"] = client_reference
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if billable is not UNSET:
            field_dict["billable"] = billable
        if maildrop_address is not UNSET:
            field_dict["maildrop_address"] = maildrop_address
        if billing_method is not UNSET:
            field_dict["billing_method"] = billing_method
        if open_date is not UNSET:
            field_dict["open_date"] = open_date
        if close_date is not UNSET:
            field_dict["close_date"] = close_date
        if pending_date is not UNSET:
            field_dict["pending_date"] = pending_date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if shared is not UNSET:
            field_dict["shared"] = shared
        if has_tasks is not UNSET:
            field_dict["has_tasks"] = has_tasks
        if last_activity_date is not UNSET:
            field_dict["last_activity_date"] = last_activity_date
        if matter_stage_updated_at is not UNSET:
            field_dict["matter_stage_updated_at"] = matter_stage_updated_at
        if client is not UNSET:
            field_dict["client"] = client
        if contingency_fee is not UNSET:
            field_dict["contingency_fee"] = contingency_fee
        if custom_rate is not UNSET:
            field_dict["custom_rate"] = custom_rate
        if evergreen_retainer is not UNSET:
            field_dict["evergreen_retainer"] = evergreen_retainer
        if folder is not UNSET:
            field_dict["folder"] = folder
        if group is not UNSET:
            field_dict["group"] = group
        if matter_budget is not UNSET:
            field_dict["matter_budget"] = matter_budget
        if matter_stage is not UNSET:
            field_dict["matter_stage"] = matter_stage
        if originating_attorney is not UNSET:
            field_dict["originating_attorney"] = originating_attorney
        if practice_area is not UNSET:
            field_dict["practice_area"] = practice_area
        if responsible_attorney is not UNSET:
            field_dict["responsible_attorney"] = responsible_attorney
        if responsible_staff is not UNSET:
            field_dict["responsible_staff"] = responsible_staff
        if statute_of_limitations is not UNSET:
            field_dict["statute_of_limitations"] = statute_of_limitations
        if user is not UNSET:
            field_dict["user"] = user
        if legal_aid_uk_matter is not UNSET:
            field_dict["legal_aid_uk_matter"] = legal_aid_uk_matter
        if account_balances is not UNSET:
            field_dict["account_balances"] = account_balances
        if custom_field_values is not UNSET:
            field_dict["custom_field_values"] = custom_field_values
        if custom_field_set_associations is not UNSET:
            field_dict["custom_field_set_associations"] = custom_field_set_associations
        if matter_bill_recipients is not UNSET:
            field_dict["matter_bill_recipients"] = matter_bill_recipients
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if task_template_list_instances is not UNSET:
            field_dict["task_template_list_instances"] = task_template_list_instances
        if split_invoice_payers is not UNSET:
            field_dict["split_invoice_payers"] = split_invoice_payers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_balance_base import AccountBalanceBase
        from ..models.contact_base import ContactBase
        from ..models.contingency_fee_base import ContingencyFeeBase
        from ..models.custom_field_set_association_base import CustomFieldSetAssociationBase
        from ..models.custom_field_value import CustomFieldValue
        from ..models.evergreen_retainer_base import EvergreenRetainerBase
        from ..models.folder_base import FolderBase
        from ..models.group_base import GroupBase
        from ..models.legal_aid_uk_matter_base import LegalAidUkMatterBase
        from ..models.matter_base_currency import MatterBaseCurrency
        from ..models.matter_bill_recipient import MatterBillRecipient
        from ..models.matter_budget_base import MatterBudgetBase
        from ..models.matter_custom_rate import MatterCustomRate
        from ..models.matter_stage_base import MatterStageBase
        from ..models.practice_area_base import PracticeAreaBase
        from ..models.relationship_base import RelationshipBase
        from ..models.split_invoice_payer_base import SplitInvoicePayerBase
        from ..models.task_base import TaskBase
        from ..models.task_template_list_instace_base import TaskTemplateListInstaceBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        number = d.pop("number", UNSET)

        display_number = d.pop("display_number", UNSET)

        custom_number = d.pop("custom_number", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, MatterBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = MatterBaseCurrency.from_dict(_currency)

        description = d.pop("description", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MatterBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatterBaseStatus(_status)

        location = d.pop("location", UNSET)

        client_reference = d.pop("client_reference", UNSET)

        client_id = d.pop("client_id", UNSET)

        billable = d.pop("billable", UNSET)

        maildrop_address = d.pop("maildrop_address", UNSET)

        _billing_method = d.pop("billing_method", UNSET)
        billing_method: Union[Unset, MatterBaseBillingMethod]
        if isinstance(_billing_method, Unset):
            billing_method = UNSET
        else:
            billing_method = MatterBaseBillingMethod(_billing_method)

        _open_date = d.pop("open_date", UNSET)
        open_date: Union[Unset, datetime.date]
        if isinstance(_open_date, Unset):
            open_date = UNSET
        else:
            open_date = isoparse(_open_date).date()

        _close_date = d.pop("close_date", UNSET)
        close_date: Union[Unset, datetime.date]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date).date()

        _pending_date = d.pop("pending_date", UNSET)
        pending_date: Union[Unset, datetime.date]
        if isinstance(_pending_date, Unset):
            pending_date = UNSET
        else:
            pending_date = isoparse(_pending_date).date()

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        shared = d.pop("shared", UNSET)

        has_tasks = d.pop("has_tasks", UNSET)

        _last_activity_date = d.pop("last_activity_date", UNSET)
        last_activity_date: Union[Unset, datetime.date]
        if isinstance(_last_activity_date, Unset):
            last_activity_date = UNSET
        else:
            last_activity_date = isoparse(_last_activity_date).date()

        _matter_stage_updated_at = d.pop("matter_stage_updated_at", UNSET)
        matter_stage_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_matter_stage_updated_at, Unset):
            matter_stage_updated_at = UNSET
        else:
            matter_stage_updated_at = isoparse(_matter_stage_updated_at)

        _client = d.pop("client", UNSET)
        client: Union[Unset, ContactBase]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ContactBase.from_dict(_client)

        _contingency_fee = d.pop("contingency_fee", UNSET)
        contingency_fee: Union[Unset, ContingencyFeeBase]
        if isinstance(_contingency_fee, Unset):
            contingency_fee = UNSET
        else:
            contingency_fee = ContingencyFeeBase.from_dict(_contingency_fee)

        _custom_rate = d.pop("custom_rate", UNSET)
        custom_rate: Union[Unset, MatterCustomRate]
        if isinstance(_custom_rate, Unset):
            custom_rate = UNSET
        else:
            custom_rate = MatterCustomRate.from_dict(_custom_rate)

        _evergreen_retainer = d.pop("evergreen_retainer", UNSET)
        evergreen_retainer: Union[Unset, EvergreenRetainerBase]
        if isinstance(_evergreen_retainer, Unset):
            evergreen_retainer = UNSET
        else:
            evergreen_retainer = EvergreenRetainerBase.from_dict(_evergreen_retainer)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, FolderBase]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = FolderBase.from_dict(_folder)

        _group = d.pop("group", UNSET)
        group: Union[Unset, GroupBase]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GroupBase.from_dict(_group)

        _matter_budget = d.pop("matter_budget", UNSET)
        matter_budget: Union[Unset, MatterBudgetBase]
        if isinstance(_matter_budget, Unset):
            matter_budget = UNSET
        else:
            matter_budget = MatterBudgetBase.from_dict(_matter_budget)

        _matter_stage = d.pop("matter_stage", UNSET)
        matter_stage: Union[Unset, MatterStageBase]
        if isinstance(_matter_stage, Unset):
            matter_stage = UNSET
        else:
            matter_stage = MatterStageBase.from_dict(_matter_stage)

        _originating_attorney = d.pop("originating_attorney", UNSET)
        originating_attorney: Union[Unset, UserBase]
        if isinstance(_originating_attorney, Unset):
            originating_attorney = UNSET
        else:
            originating_attorney = UserBase.from_dict(_originating_attorney)

        _practice_area = d.pop("practice_area", UNSET)
        practice_area: Union[Unset, PracticeAreaBase]
        if isinstance(_practice_area, Unset):
            practice_area = UNSET
        else:
            practice_area = PracticeAreaBase.from_dict(_practice_area)

        _responsible_attorney = d.pop("responsible_attorney", UNSET)
        responsible_attorney: Union[Unset, UserBase]
        if isinstance(_responsible_attorney, Unset):
            responsible_attorney = UNSET
        else:
            responsible_attorney = UserBase.from_dict(_responsible_attorney)

        _responsible_staff = d.pop("responsible_staff", UNSET)
        responsible_staff: Union[Unset, UserBase]
        if isinstance(_responsible_staff, Unset):
            responsible_staff = UNSET
        else:
            responsible_staff = UserBase.from_dict(_responsible_staff)

        _statute_of_limitations = d.pop("statute_of_limitations", UNSET)
        statute_of_limitations: Union[Unset, TaskBase]
        if isinstance(_statute_of_limitations, Unset):
            statute_of_limitations = UNSET
        else:
            statute_of_limitations = TaskBase.from_dict(_statute_of_limitations)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        _legal_aid_uk_matter = d.pop("legal_aid_uk_matter", UNSET)
        legal_aid_uk_matter: Union[Unset, LegalAidUkMatterBase]
        if isinstance(_legal_aid_uk_matter, Unset):
            legal_aid_uk_matter = UNSET
        else:
            legal_aid_uk_matter = LegalAidUkMatterBase.from_dict(_legal_aid_uk_matter)

        account_balances = []
        _account_balances = d.pop("account_balances", UNSET)
        for account_balances_item_data in _account_balances or []:
            account_balances_item = AccountBalanceBase.from_dict(account_balances_item_data)

            account_balances.append(account_balances_item)

        custom_field_values = []
        _custom_field_values = d.pop("custom_field_values", UNSET)
        for custom_field_values_item_data in _custom_field_values or []:
            custom_field_values_item = CustomFieldValue.from_dict(custom_field_values_item_data)

            custom_field_values.append(custom_field_values_item)

        custom_field_set_associations = []
        _custom_field_set_associations = d.pop("custom_field_set_associations", UNSET)
        for custom_field_set_associations_item_data in _custom_field_set_associations or []:
            custom_field_set_associations_item = CustomFieldSetAssociationBase.from_dict(
                custom_field_set_associations_item_data
            )

            custom_field_set_associations.append(custom_field_set_associations_item)

        matter_bill_recipients = []
        _matter_bill_recipients = d.pop("matter_bill_recipients", UNSET)
        for matter_bill_recipients_item_data in _matter_bill_recipients or []:
            matter_bill_recipients_item = MatterBillRecipient.from_dict(matter_bill_recipients_item_data)

            matter_bill_recipients.append(matter_bill_recipients_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = RelationshipBase.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        task_template_list_instances = []
        _task_template_list_instances = d.pop("task_template_list_instances", UNSET)
        for task_template_list_instances_item_data in _task_template_list_instances or []:
            task_template_list_instances_item = TaskTemplateListInstaceBase.from_dict(
                task_template_list_instances_item_data
            )

            task_template_list_instances.append(task_template_list_instances_item)

        split_invoice_payers = []
        _split_invoice_payers = d.pop("split_invoice_payers", UNSET)
        for split_invoice_payers_item_data in _split_invoice_payers or []:
            split_invoice_payers_item = SplitInvoicePayerBase.from_dict(split_invoice_payers_item_data)

            split_invoice_payers.append(split_invoice_payers_item)

        matter = cls(
            id=id,
            etag=etag,
            number=number,
            display_number=display_number,
            custom_number=custom_number,
            currency=currency,
            description=description,
            status=status,
            location=location,
            client_reference=client_reference,
            client_id=client_id,
            billable=billable,
            maildrop_address=maildrop_address,
            billing_method=billing_method,
            open_date=open_date,
            close_date=close_date,
            pending_date=pending_date,
            created_at=created_at,
            updated_at=updated_at,
            shared=shared,
            has_tasks=has_tasks,
            last_activity_date=last_activity_date,
            matter_stage_updated_at=matter_stage_updated_at,
            client=client,
            contingency_fee=contingency_fee,
            custom_rate=custom_rate,
            evergreen_retainer=evergreen_retainer,
            folder=folder,
            group=group,
            matter_budget=matter_budget,
            matter_stage=matter_stage,
            originating_attorney=originating_attorney,
            practice_area=practice_area,
            responsible_attorney=responsible_attorney,
            responsible_staff=responsible_staff,
            statute_of_limitations=statute_of_limitations,
            user=user,
            legal_aid_uk_matter=legal_aid_uk_matter,
            account_balances=account_balances,
            custom_field_values=custom_field_values,
            custom_field_set_associations=custom_field_set_associations,
            matter_bill_recipients=matter_bill_recipients,
            relationships=relationships,
            task_template_list_instances=task_template_list_instances,
            split_invoice_payers=split_invoice_payers,
        )

        matter.additional_properties = d
        return matter

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
