import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.activitycreate_files_body_data_tax_setting import ActivitycreateFilesBodyDataTaxSetting
from ..models.activitycreate_files_body_data_type import ActivitycreateFilesBodyDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activitycreate_files_body_data_activity_description import (
        ActivitycreateFilesBodyDataActivityDescription,
    )
    from ..models.activitycreate_files_body_data_calendar_entry import ActivitycreateFilesBodyDataCalendarEntry
    from ..models.activitycreate_files_body_data_client_portal import ActivitycreateFilesBodyDataClientPortal
    from ..models.activitycreate_files_body_data_communication import ActivitycreateFilesBodyDataCommunication
    from ..models.activitycreate_files_body_data_contact_note import ActivitycreateFilesBodyDataContactNote
    from ..models.activitycreate_files_body_data_expense_category import ActivitycreateFilesBodyDataExpenseCategory
    from ..models.activitycreate_files_body_data_matter import ActivitycreateFilesBodyDataMatter
    from ..models.activitycreate_files_body_data_matter_note import ActivitycreateFilesBodyDataMatterNote
    from ..models.activitycreate_files_body_data_task import ActivitycreateFilesBodyDataTask
    from ..models.activitycreate_files_body_data_text_message_conversation import (
        ActivitycreateFilesBodyDataTextMessageConversation,
    )
    from ..models.activitycreate_files_body_data_user import ActivitycreateFilesBodyDataUser
    from ..models.activitycreate_files_body_data_utbms_expense import ActivitycreateFilesBodyDataUtbmsExpense
    from ..models.activitycreate_files_body_data_vendor import ActivitycreateFilesBodyDataVendor


T = TypeVar("T", bound="ActivitycreateFilesBodyData")


@_attrs_define
class ActivitycreateFilesBodyData:
    """
    Attributes:
        date (datetime.date): The date the Activity was performed. (Expects an ISO-8601 date).
        type_ (ActivitycreateFilesBodyDataType): The type of the Activity.
        activity_description (Union[Unset, ActivitycreateFilesBodyDataActivityDescription]):
        calendar_entry (Union[Unset, ActivitycreateFilesBodyDataCalendarEntry]):
        client_portal (Union[Unset, ActivitycreateFilesBodyDataClientPortal]):
        communication (Union[Unset, ActivitycreateFilesBodyDataCommunication]):
        contact_note (Union[Unset, ActivitycreateFilesBodyDataContactNote]):
        expense_category (Union[Unset, ActivitycreateFilesBodyDataExpenseCategory]):
        matter (Union[Unset, ActivitycreateFilesBodyDataMatter]):
        matter_note (Union[Unset, ActivitycreateFilesBodyDataMatterNote]):
        no_charge (Union[Unset, bool]): Whether the non-billable *Activity* will be shown on the bill.
        non_billable (Union[Unset, bool]): Whether or not this Activity is prevented from appearing as a line item in a
            bill.
            Only valid for non-billed TimeEntries, and with the exception of the Activity having no_charge set to true.
        note (Union[Unset, str]): A custom note to describe what the Activity is for.
        price (Union[Unset, float]): For an ExpenseEntry, HardCostEntry, and SoftCostEntry, it is the expense amount.

            [Support Link for ExpenseEntry](https://help.clio.com/hc/en-us/articles/9289745356571-Expenses)

            [Support Link for HardCostEntry and SoftCostEntry](https://help.clio.com/hc/en-
            us/articles/9289745356571-Expenses#enable-hard-and-soft-cost-expenses-0-0)

            For a TimeEntry, it is the hourly or flat amount. When updating a TimeEntry,
            if the price is not given or the user does not have the permission to view the rate,
            and its activity description, matter and/or user is changed,
            the price is reset according to the rate defined for the activity description, matter, client or user.

            [Support Link for Rates Hierarchy](https://help.clio.com/hc/en-us/articles/9289801180187-Rates-and-Rate-
            Hierarchies-)

            [Support Link for Billing Rate Visibility](https://help.clio.com/hc/en-us/articles/9285360193819-Permissions-
            and-Billing-Rates#billing-rate-visibility-0-3)
        quantity (Union[Unset, float]): The field is applicable to TimeEntry, ExpenseEntry, and SoftCostEntry.

            **Version <= 4.0.3:**
            The number of hours the TimeEntry took.

            **Latest version:**
            The number of seconds the TimeEntry took.
        reference (Union[Unset, str]): A check reference for a HardCostEntry.
        start_timer (Union[Unset, bool]): Whether or not a timer should be started for this Activity. Only valid for
            non-FlatRate, non-billed TimeEntries.
        task (Union[Unset, ActivitycreateFilesBodyDataTask]):
        tax_setting (Union[Unset, ActivitycreateFilesBodyDataTaxSetting]): The option denoting whether primary tax,
            secondary tax, or both is applied to an expense entry.
        text_message_conversation (Union[Unset, ActivitycreateFilesBodyDataTextMessageConversation]):
        user (Union[Unset, ActivitycreateFilesBodyDataUser]):
        utbms_expense (Union[Unset, ActivitycreateFilesBodyDataUtbmsExpense]):
        vendor (Union[Unset, ActivitycreateFilesBodyDataVendor]):
    """

    date: datetime.date
    type_: ActivitycreateFilesBodyDataType
    activity_description: Union[Unset, "ActivitycreateFilesBodyDataActivityDescription"] = UNSET
    calendar_entry: Union[Unset, "ActivitycreateFilesBodyDataCalendarEntry"] = UNSET
    client_portal: Union[Unset, "ActivitycreateFilesBodyDataClientPortal"] = UNSET
    communication: Union[Unset, "ActivitycreateFilesBodyDataCommunication"] = UNSET
    contact_note: Union[Unset, "ActivitycreateFilesBodyDataContactNote"] = UNSET
    expense_category: Union[Unset, "ActivitycreateFilesBodyDataExpenseCategory"] = UNSET
    matter: Union[Unset, "ActivitycreateFilesBodyDataMatter"] = UNSET
    matter_note: Union[Unset, "ActivitycreateFilesBodyDataMatterNote"] = UNSET
    no_charge: Union[Unset, bool] = UNSET
    non_billable: Union[Unset, bool] = UNSET
    note: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    quantity: Union[Unset, float] = UNSET
    reference: Union[Unset, str] = UNSET
    start_timer: Union[Unset, bool] = UNSET
    task: Union[Unset, "ActivitycreateFilesBodyDataTask"] = UNSET
    tax_setting: Union[Unset, ActivitycreateFilesBodyDataTaxSetting] = UNSET
    text_message_conversation: Union[Unset, "ActivitycreateFilesBodyDataTextMessageConversation"] = UNSET
    user: Union[Unset, "ActivitycreateFilesBodyDataUser"] = UNSET
    utbms_expense: Union[Unset, "ActivitycreateFilesBodyDataUtbmsExpense"] = UNSET
    vendor: Union[Unset, "ActivitycreateFilesBodyDataVendor"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        type_ = self.type_.value

        activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_description, Unset):
            activity_description = self.activity_description.to_dict()

        calendar_entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calendar_entry, Unset):
            calendar_entry = self.calendar_entry.to_dict()

        client_portal: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client_portal, Unset):
            client_portal = self.client_portal.to_dict()

        communication: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.communication, Unset):
            communication = self.communication.to_dict()

        contact_note: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact_note, Unset):
            contact_note = self.contact_note.to_dict()

        expense_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.expense_category, Unset):
            expense_category = self.expense_category.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        matter_note: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter_note, Unset):
            matter_note = self.matter_note.to_dict()

        no_charge = self.no_charge

        non_billable = self.non_billable

        note = self.note

        price = self.price

        quantity = self.quantity

        reference = self.reference

        start_timer = self.start_timer

        task: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.task, Unset):
            task = self.task.to_dict()

        tax_setting: Union[Unset, str] = UNSET
        if not isinstance(self.tax_setting, Unset):
            tax_setting = self.tax_setting.value

        text_message_conversation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.text_message_conversation, Unset):
            text_message_conversation = self.text_message_conversation.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        utbms_expense: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utbms_expense, Unset):
            utbms_expense = self.utbms_expense.to_dict()

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "type": type_,
            }
        )
        if activity_description is not UNSET:
            field_dict["activity_description"] = activity_description
        if calendar_entry is not UNSET:
            field_dict["calendar_entry"] = calendar_entry
        if client_portal is not UNSET:
            field_dict["client_portal"] = client_portal
        if communication is not UNSET:
            field_dict["communication"] = communication
        if contact_note is not UNSET:
            field_dict["contact_note"] = contact_note
        if expense_category is not UNSET:
            field_dict["expense_category"] = expense_category
        if matter is not UNSET:
            field_dict["matter"] = matter
        if matter_note is not UNSET:
            field_dict["matter_note"] = matter_note
        if no_charge is not UNSET:
            field_dict["no_charge"] = no_charge
        if non_billable is not UNSET:
            field_dict["non_billable"] = non_billable
        if note is not UNSET:
            field_dict["note"] = note
        if price is not UNSET:
            field_dict["price"] = price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if reference is not UNSET:
            field_dict["reference"] = reference
        if start_timer is not UNSET:
            field_dict["start_timer"] = start_timer
        if task is not UNSET:
            field_dict["task"] = task
        if tax_setting is not UNSET:
            field_dict["tax_setting"] = tax_setting
        if text_message_conversation is not UNSET:
            field_dict["text_message_conversation"] = text_message_conversation
        if user is not UNSET:
            field_dict["user"] = user
        if utbms_expense is not UNSET:
            field_dict["utbms_expense"] = utbms_expense
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activitycreate_files_body_data_activity_description import (
            ActivitycreateFilesBodyDataActivityDescription,
        )
        from ..models.activitycreate_files_body_data_calendar_entry import ActivitycreateFilesBodyDataCalendarEntry
        from ..models.activitycreate_files_body_data_client_portal import ActivitycreateFilesBodyDataClientPortal
        from ..models.activitycreate_files_body_data_communication import ActivitycreateFilesBodyDataCommunication
        from ..models.activitycreate_files_body_data_contact_note import ActivitycreateFilesBodyDataContactNote
        from ..models.activitycreate_files_body_data_expense_category import ActivitycreateFilesBodyDataExpenseCategory
        from ..models.activitycreate_files_body_data_matter import ActivitycreateFilesBodyDataMatter
        from ..models.activitycreate_files_body_data_matter_note import ActivitycreateFilesBodyDataMatterNote
        from ..models.activitycreate_files_body_data_task import ActivitycreateFilesBodyDataTask
        from ..models.activitycreate_files_body_data_text_message_conversation import (
            ActivitycreateFilesBodyDataTextMessageConversation,
        )
        from ..models.activitycreate_files_body_data_user import ActivitycreateFilesBodyDataUser
        from ..models.activitycreate_files_body_data_utbms_expense import ActivitycreateFilesBodyDataUtbmsExpense
        from ..models.activitycreate_files_body_data_vendor import ActivitycreateFilesBodyDataVendor

        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        type_ = ActivitycreateFilesBodyDataType(d.pop("type"))

        _activity_description = d.pop("activity_description", UNSET)
        activity_description: Union[Unset, ActivitycreateFilesBodyDataActivityDescription]
        if isinstance(_activity_description, Unset):
            activity_description = UNSET
        else:
            activity_description = ActivitycreateFilesBodyDataActivityDescription.from_dict(_activity_description)

        _calendar_entry = d.pop("calendar_entry", UNSET)
        calendar_entry: Union[Unset, ActivitycreateFilesBodyDataCalendarEntry]
        if isinstance(_calendar_entry, Unset):
            calendar_entry = UNSET
        else:
            calendar_entry = ActivitycreateFilesBodyDataCalendarEntry.from_dict(_calendar_entry)

        _client_portal = d.pop("client_portal", UNSET)
        client_portal: Union[Unset, ActivitycreateFilesBodyDataClientPortal]
        if isinstance(_client_portal, Unset):
            client_portal = UNSET
        else:
            client_portal = ActivitycreateFilesBodyDataClientPortal.from_dict(_client_portal)

        _communication = d.pop("communication", UNSET)
        communication: Union[Unset, ActivitycreateFilesBodyDataCommunication]
        if isinstance(_communication, Unset):
            communication = UNSET
        else:
            communication = ActivitycreateFilesBodyDataCommunication.from_dict(_communication)

        _contact_note = d.pop("contact_note", UNSET)
        contact_note: Union[Unset, ActivitycreateFilesBodyDataContactNote]
        if isinstance(_contact_note, Unset):
            contact_note = UNSET
        else:
            contact_note = ActivitycreateFilesBodyDataContactNote.from_dict(_contact_note)

        _expense_category = d.pop("expense_category", UNSET)
        expense_category: Union[Unset, ActivitycreateFilesBodyDataExpenseCategory]
        if isinstance(_expense_category, Unset):
            expense_category = UNSET
        else:
            expense_category = ActivitycreateFilesBodyDataExpenseCategory.from_dict(_expense_category)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, ActivitycreateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = ActivitycreateFilesBodyDataMatter.from_dict(_matter)

        _matter_note = d.pop("matter_note", UNSET)
        matter_note: Union[Unset, ActivitycreateFilesBodyDataMatterNote]
        if isinstance(_matter_note, Unset):
            matter_note = UNSET
        else:
            matter_note = ActivitycreateFilesBodyDataMatterNote.from_dict(_matter_note)

        no_charge = d.pop("no_charge", UNSET)

        non_billable = d.pop("non_billable", UNSET)

        note = d.pop("note", UNSET)

        price = d.pop("price", UNSET)

        quantity = d.pop("quantity", UNSET)

        reference = d.pop("reference", UNSET)

        start_timer = d.pop("start_timer", UNSET)

        _task = d.pop("task", UNSET)
        task: Union[Unset, ActivitycreateFilesBodyDataTask]
        if isinstance(_task, Unset):
            task = UNSET
        else:
            task = ActivitycreateFilesBodyDataTask.from_dict(_task)

        _tax_setting = d.pop("tax_setting", UNSET)
        tax_setting: Union[Unset, ActivitycreateFilesBodyDataTaxSetting]
        if isinstance(_tax_setting, Unset):
            tax_setting = UNSET
        else:
            tax_setting = ActivitycreateFilesBodyDataTaxSetting(_tax_setting)

        _text_message_conversation = d.pop("text_message_conversation", UNSET)
        text_message_conversation: Union[Unset, ActivitycreateFilesBodyDataTextMessageConversation]
        if isinstance(_text_message_conversation, Unset):
            text_message_conversation = UNSET
        else:
            text_message_conversation = ActivitycreateFilesBodyDataTextMessageConversation.from_dict(
                _text_message_conversation
            )

        _user = d.pop("user", UNSET)
        user: Union[Unset, ActivitycreateFilesBodyDataUser]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = ActivitycreateFilesBodyDataUser.from_dict(_user)

        _utbms_expense = d.pop("utbms_expense", UNSET)
        utbms_expense: Union[Unset, ActivitycreateFilesBodyDataUtbmsExpense]
        if isinstance(_utbms_expense, Unset):
            utbms_expense = UNSET
        else:
            utbms_expense = ActivitycreateFilesBodyDataUtbmsExpense.from_dict(_utbms_expense)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, ActivitycreateFilesBodyDataVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = ActivitycreateFilesBodyDataVendor.from_dict(_vendor)

        activitycreate_files_body_data = cls(
            date=date,
            type_=type_,
            activity_description=activity_description,
            calendar_entry=calendar_entry,
            client_portal=client_portal,
            communication=communication,
            contact_note=contact_note,
            expense_category=expense_category,
            matter=matter,
            matter_note=matter_note,
            no_charge=no_charge,
            non_billable=non_billable,
            note=note,
            price=price,
            quantity=quantity,
            reference=reference,
            start_timer=start_timer,
            task=task,
            tax_setting=tax_setting,
            text_message_conversation=text_message_conversation,
            user=user,
            utbms_expense=utbms_expense,
            vendor=vendor,
        )

        activitycreate_files_body_data.additional_properties = d
        return activitycreate_files_body_data

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
