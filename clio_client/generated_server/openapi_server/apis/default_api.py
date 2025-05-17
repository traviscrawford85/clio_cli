# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from typing import Any, Dict
from openapi_server.models.account import Account
from openapi_server.models.account_balance_base import AccountBalanceBase
from openapi_server.models.account_base import AccountBase
from openapi_server.models.activity import Activity
from openapi_server.models.activity_base import ActivityBase
from openapi_server.models.activity_calendar_entry_base import ActivityCalendarEntryBase
from openapi_server.models.activity_description import ActivityDescription
from openapi_server.models.activity_description_base import ActivityDescriptionBase
from openapi_server.models.activity_description_rate_base import ActivityDescriptionRateBase
from openapi_server.models.activity_rate import ActivityRate
from openapi_server.models.activity_rate_base import ActivityRateBase
from openapi_server.models.activity_task_base import ActivityTaskBase
from openapi_server.models.activity_text_message_conversation_base import ActivityTextMessageConversationBase
from openapi_server.models.address import Address
from openapi_server.models.address_base import AddressBase
from openapi_server.models.allocation import Allocation
from openapi_server.models.allocation_base import AllocationBase
from openapi_server.models.attendee_base import AttendeeBase
from openapi_server.models.avatar_base import AvatarBase
from openapi_server.models.balance import Balance
from openapi_server.models.balance_base import BalanceBase
from openapi_server.models.bank_account import BankAccount
from openapi_server.models.bank_account_base import BankAccountBase
from openapi_server.models.bank_transaction import BankTransaction
from openapi_server.models.bank_transaction_base import BankTransactionBase
from openapi_server.models.bank_transfer import BankTransfer
from openapi_server.models.bank_transfer_base import BankTransferBase
from openapi_server.models.bill import Bill
from openapi_server.models.bill_base import BillBase
from openapi_server.models.bill_recipient import BillRecipient
from openapi_server.models.bill_recipient_base import BillRecipientBase
from openapi_server.models.bill_recipient_contact_base import BillRecipientContactBase
from openapi_server.models.bill_theme import BillTheme
from openapi_server.models.bill_theme_base import BillThemeBase
from openapi_server.models.billable_client import BillableClient
from openapi_server.models.billable_client_base import BillableClientBase
from openapi_server.models.billable_matter import BillableMatter
from openapi_server.models.billable_matter_base import BillableMatterBase
from openapi_server.models.billing_setting import BillingSetting
from openapi_server.models.billing_setting_base import BillingSettingBase
from openapi_server.models.calendar import Calendar
from openapi_server.models.calendar_base import CalendarBase
from openapi_server.models.calendar_entry import CalendarEntry
from openapi_server.models.calendar_entry_base import CalendarEntryBase
from openapi_server.models.calendar_entry_event_type_base import CalendarEntryEventTypeBase
from openapi_server.models.calendar_visibility import CalendarVisibility
from openapi_server.models.calendar_visibility_base import CalendarVisibilityBase
from openapi_server.models.cascading_task_template_base import CascadingTaskTemplateBase
from openapi_server.models.client import Client
from openapi_server.models.client_base import ClientBase
from openapi_server.models.client_portal_base import ClientPortalBase
from openapi_server.models.clio_creator_base import ClioCreatorBase
from openapi_server.models.clio_payments_link import ClioPaymentsLink
from openapi_server.models.clio_payments_link_base import ClioPaymentsLinkBase
from openapi_server.models.clio_payments_payment import ClioPaymentsPayment
from openapi_server.models.clio_payments_payment_base import ClioPaymentsPaymentBase
from openapi_server.models.comment import Comment
from openapi_server.models.comment_base import CommentBase
from openapi_server.models.communication import Communication
from openapi_server.models.communication_base import CommunicationBase
from openapi_server.models.communication_eml_file_base import CommunicationEmlFileBase
from openapi_server.models.conference_meeting_base import ConferenceMeetingBase
from openapi_server.models.contact import Contact
from openapi_server.models.contact_base import ContactBase
from openapi_server.models.contingency_fee_base import ContingencyFeeBase
from openapi_server.models.conversation import Conversation
from openapi_server.models.conversation_base import ConversationBase
from openapi_server.models.conversation_membership import ConversationMembership
from openapi_server.models.conversation_membership_base import ConversationMembershipBase
from openapi_server.models.conversation_message import ConversationMessage
from openapi_server.models.conversation_message_base import ConversationMessageBase
from openapi_server.models.credit_memo import CreditMemo
from openapi_server.models.credit_memo_base import CreditMemoBase
from openapi_server.models.currency import Currency
from openapi_server.models.currency_base import CurrencyBase
from openapi_server.models.custom_action import CustomAction
from openapi_server.models.custom_action_base import CustomActionBase
from openapi_server.models.custom_field import CustomField
from openapi_server.models.custom_field_base import CustomFieldBase
from openapi_server.models.custom_field_matter_selection import CustomFieldMatterSelection
from openapi_server.models.custom_field_matter_selection_base import CustomFieldMatterSelectionBase
from openapi_server.models.custom_field_set import CustomFieldSet
from openapi_server.models.custom_field_set_association_base import CustomFieldSetAssociationBase
from openapi_server.models.custom_field_set_base import CustomFieldSetBase
from openapi_server.models.custom_field_value import CustomFieldValue
from openapi_server.models.custom_field_value_base import CustomFieldValueBase
from openapi_server.models.damage import Damage
from openapi_server.models.damage_base import DamageBase
from openapi_server.models.discount_base import DiscountBase
from openapi_server.models.document import Document
from openapi_server.models.document_archive import DocumentArchive
from openapi_server.models.document_archive_base import DocumentArchiveBase
from openapi_server.models.document_automation import DocumentAutomation
from openapi_server.models.document_automation_base import DocumentAutomationBase
from openapi_server.models.document_base import DocumentBase
from openapi_server.models.document_category import DocumentCategory
from openapi_server.models.document_category_base import DocumentCategoryBase
from openapi_server.models.document_template import DocumentTemplate
from openapi_server.models.document_template_base import DocumentTemplateBase
from openapi_server.models.document_version import DocumentVersion
from openapi_server.models.document_version_base import DocumentVersionBase
from openapi_server.models.email_address import EmailAddress
from openapi_server.models.email_address_base import EmailAddressBase
from openapi_server.models.error_detail import ErrorDetail
from openapi_server.models.event import Event
from openapi_server.models.event_base import EventBase
from openapi_server.models.event_metrics import EventMetrics
from openapi_server.models.event_metrics_base import EventMetricsBase
from openapi_server.models.evergreen_retainer_base import EvergreenRetainerBase
from openapi_server.models.expense_category import ExpenseCategory
from openapi_server.models.expense_category_base import ExpenseCategoryBase
from openapi_server.models.external_property_base import ExternalPropertyBase
from openapi_server.models.folder import Folder
from openapi_server.models.folder_base import FolderBase
from openapi_server.models.grant import Grant
from openapi_server.models.grant_base import GrantBase
from openapi_server.models.grant_funding_source import GrantFundingSource
from openapi_server.models.grant_funding_source_base import GrantFundingSourceBase
from openapi_server.models.group import Group
from openapi_server.models.group_base import GroupBase
from openapi_server.models.ids_response import IdsResponse
from openapi_server.models.instant_messenger_base import InstantMessengerBase
from openapi_server.models.interest import Interest
from openapi_server.models.interest_base import InterestBase
from openapi_server.models.interest_charge import InterestCharge
from openapi_server.models.interest_charge_base import InterestChargeBase
from openapi_server.models.item import Item
from openapi_server.models.item_base import ItemBase
from openapi_server.models.job_title_base import JobTitleBase
from openapi_server.models.jurisdiction import Jurisdiction
from openapi_server.models.jurisdiction_base import JurisdictionBase
from openapi_server.models.jurisdictions_to_trigger import JurisdictionsToTrigger
from openapi_server.models.jurisdictions_to_trigger_base import JurisdictionsToTriggerBase
from openapi_server.models.lauk_civil_certificated_rate import LaukCivilCertificatedRate
from openapi_server.models.lauk_civil_certificated_rate_base import LaukCivilCertificatedRateBase
from openapi_server.models.lauk_civil_controlled_rate import LaukCivilControlledRate
from openapi_server.models.lauk_civil_controlled_rate_base import LaukCivilControlledRateBase
from openapi_server.models.lauk_criminal_controlled_rate import LaukCriminalControlledRate
from openapi_server.models.lauk_criminal_controlled_rate_base import LaukCriminalControlledRateBase
from openapi_server.models.lauk_expense_category import LaukExpenseCategory
from openapi_server.models.lauk_expense_category_base import LaukExpenseCategoryBase
from openapi_server.models.legal_aid_uk_activity_base import LegalAidUkActivityBase
from openapi_server.models.legal_aid_uk_bill_base import LegalAidUkBillBase
from openapi_server.models.legal_aid_uk_contact_base import LegalAidUkContactBase
from openapi_server.models.legal_aid_uk_matter_base import LegalAidUkMatterBase
from openapi_server.models.lien_base import LienBase
from openapi_server.models.line_item import LineItem
from openapi_server.models.line_item_base import LineItemBase
from openapi_server.models.line_item_totals_base import LineItemTotalsBase
from openapi_server.models.linked_folder_base import LinkedFolderBase
from openapi_server.models.log_entry import LogEntry
from openapi_server.models.log_entry_base import LogEntryBase
from openapi_server.models.matter import Matter
from openapi_server.models.matter_balance_base import MatterBalanceBase
from openapi_server.models.matter_base import MatterBase
from openapi_server.models.matter_bill_recipient import MatterBillRecipient
from openapi_server.models.matter_bill_recipient_base import MatterBillRecipientBase
from openapi_server.models.matter_budget_base import MatterBudgetBase
from openapi_server.models.matter_contacts import MatterContacts
from openapi_server.models.matter_contacts_base import MatterContactsBase
from openapi_server.models.matter_custom_rate import MatterCustomRate
from openapi_server.models.matter_custom_rate_base import MatterCustomRateBase
from openapi_server.models.matter_docket import MatterDocket
from openapi_server.models.matter_docket_base import MatterDocketBase
from openapi_server.models.matter_stage import MatterStage
from openapi_server.models.matter_stage_base import MatterStageBase
from openapi_server.models.medical_bill import MedicalBill
from openapi_server.models.medical_bill_base import MedicalBillBase
from openapi_server.models.medical_record import MedicalRecord
from openapi_server.models.medical_record_base import MedicalRecordBase
from openapi_server.models.medical_records_request import MedicalRecordsRequest
from openapi_server.models.medical_records_request_base import MedicalRecordsRequestBase
from openapi_server.models.multipart import Multipart
from openapi_server.models.multipart_base import MultipartBase
from openapi_server.models.multipart_header_base import MultipartHeaderBase
from openapi_server.models.my_event import MyEvent
from openapi_server.models.note import Note
from openapi_server.models.note_base import NoteBase
from openapi_server.models.notification_event_subscriber_base import NotificationEventSubscriberBase
from openapi_server.models.notification_method_base import NotificationMethodBase
from openapi_server.models.outstanding_client_balance import OutstandingClientBalance
from openapi_server.models.outstanding_client_balance_base import OutstandingClientBalanceBase
from openapi_server.models.participant import Participant
from openapi_server.models.participant_base import ParticipantBase
from openapi_server.models.payment import Payment
from openapi_server.models.payment_base import PaymentBase
from openapi_server.models.payment_profile_base import PaymentProfileBase
from openapi_server.models.phone_number import PhoneNumber
from openapi_server.models.phone_number_base import PhoneNumberBase
from openapi_server.models.picklist_option import PicklistOption
from openapi_server.models.picklist_option_base import PicklistOptionBase
from openapi_server.models.polymorphic_custom_rate import PolymorphicCustomRate
from openapi_server.models.polymorphic_custom_rate_activity_description_base import PolymorphicCustomRateActivityDescriptionBase
from openapi_server.models.polymorphic_custom_rate_base import PolymorphicCustomRateBase
from openapi_server.models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase
from openapi_server.models.polymorphic_custom_rate_user_base import PolymorphicCustomRateUserBase
from openapi_server.models.polymorphic_object_base import PolymorphicObjectBase
from openapi_server.models.practice_area import PracticeArea
from openapi_server.models.practice_area_base import PracticeAreaBase
from openapi_server.models.related_contacts import RelatedContacts
from openapi_server.models.related_contacts_base import RelatedContactsBase
from openapi_server.models.relationship import Relationship
from openapi_server.models.relationship_base import RelationshipBase
from openapi_server.models.reminder import Reminder
from openapi_server.models.reminder_base import ReminderBase
from openapi_server.models.reminder_template_base import ReminderTemplateBase
from openapi_server.models.report import Report
from openapi_server.models.report_base import ReportBase
from openapi_server.models.report_preset import ReportPreset
from openapi_server.models.report_preset_base import ReportPresetBase
from openapi_server.models.report_schedule import ReportSchedule
from openapi_server.models.report_schedule_base import ReportScheduleBase
from openapi_server.models.service_type import ServiceType
from openapi_server.models.service_type_base import ServiceTypeBase
from openapi_server.models.split_invoice_base import SplitInvoiceBase
from openapi_server.models.split_invoice_payer_base import SplitInvoicePayerBase
from openapi_server.models.task import Task
from openapi_server.models.task_base import TaskBase
from openapi_server.models.task_template import TaskTemplate
from openapi_server.models.task_template_base import TaskTemplateBase
from openapi_server.models.task_template_list import TaskTemplateList
from openapi_server.models.task_template_list_base import TaskTemplateListBase
from openapi_server.models.task_template_list_instace_base import TaskTemplateListInstaceBase
from openapi_server.models.task_type import TaskType
from openapi_server.models.task_type_base import TaskTypeBase
from openapi_server.models.text_snippet import TextSnippet
from openapi_server.models.text_snippet_base import TextSnippetBase
from openapi_server.models.timer import Timer
from openapi_server.models.timer_base import TimerBase
from openapi_server.models.trust_line_item import TrustLineItem
from openapi_server.models.trust_line_item_base import TrustLineItemBase
from openapi_server.models.trust_request import TrustRequest
from openapi_server.models.trust_request_base import TrustRequestBase
from openapi_server.models.user import User
from openapi_server.models.user_base import UserBase
from openapi_server.models.utbms_code import UtbmsCode
from openapi_server.models.utbms_code_base import UtbmsCodeBase
from openapi_server.models.utbms_set import UtbmsSet
from openapi_server.models.utbms_set_base import UtbmsSetBase
from openapi_server.models.web_site_base import WebSiteBase
from openapi_server.models.webhook import Webhook
from openapi_server.models.webhook_base import WebhookBase


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/generated/account_base.json",
    responses={
        200: {"model": AccountBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Account_base",
    response_model_by_alias=True,
)
async def generated_account_base_json_get(
) -> AccountBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_account_base_json_get()


@router.get(
    "/generated/account.json",
    responses={
        200: {"model": Account, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Account",
    response_model_by_alias=True,
)
async def generated_account_json_get(
) -> Account:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_account_json_get()


@router.get(
    "/generated/accountbalance_base.json",
    responses={
        200: {"model": AccountBalanceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for AccountBalance_base",
    response_model_by_alias=True,
)
async def generated_accountbalance_base_json_get(
) -> AccountBalanceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_accountbalance_base_json_get()


@router.get(
    "/generated/activity_base.json",
    responses={
        200: {"model": ActivityBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Activity_base",
    response_model_by_alias=True,
)
async def generated_activity_base_json_get(
) -> ActivityBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activity_base_json_get()


@router.get(
    "/generated/activity_calendarentry_base.json",
    responses={
        200: {"model": ActivityCalendarEntryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Activity_CalendarEntry_base",
    response_model_by_alias=True,
)
async def generated_activity_calendarentry_base_json_get(
) -> ActivityCalendarEntryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activity_calendarentry_base_json_get()


@router.get(
    "/generated/activity.json",
    responses={
        200: {"model": Activity, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Activity",
    response_model_by_alias=True,
)
async def generated_activity_json_get(
) -> Activity:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activity_json_get()


@router.get(
    "/generated/activity_task_base.json",
    responses={
        200: {"model": ActivityTaskBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Activity_Task_base",
    response_model_by_alias=True,
)
async def generated_activity_task_base_json_get(
) -> ActivityTaskBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activity_task_base_json_get()


@router.get(
    "/generated/activity_textmessageconversation_base.json",
    responses={
        200: {"model": ActivityTextMessageConversationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Activity_TextMessageConversation_base",
    response_model_by_alias=True,
)
async def generated_activity_textmessageconversation_base_json_get(
) -> ActivityTextMessageConversationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activity_textmessageconversation_base_json_get()


@router.get(
    "/generated/activitydescription_base.json",
    responses={
        200: {"model": ActivityDescriptionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ActivityDescription_base",
    response_model_by_alias=True,
)
async def generated_activitydescription_base_json_get(
) -> ActivityDescriptionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activitydescription_base_json_get()


@router.get(
    "/generated/activitydescription.json",
    responses={
        200: {"model": ActivityDescription, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ActivityDescription",
    response_model_by_alias=True,
)
async def generated_activitydescription_json_get(
) -> ActivityDescription:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activitydescription_json_get()


@router.get(
    "/generated/activitydescriptionrate_base.json",
    responses={
        200: {"model": ActivityDescriptionRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ActivityDescriptionRate_base",
    response_model_by_alias=True,
)
async def generated_activitydescriptionrate_base_json_get(
) -> ActivityDescriptionRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activitydescriptionrate_base_json_get()


@router.get(
    "/generated/activityrate_base.json",
    responses={
        200: {"model": ActivityRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ActivityRate_base",
    response_model_by_alias=True,
)
async def generated_activityrate_base_json_get(
) -> ActivityRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activityrate_base_json_get()


@router.get(
    "/generated/activityrate.json",
    responses={
        200: {"model": ActivityRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ActivityRate",
    response_model_by_alias=True,
)
async def generated_activityrate_json_get(
) -> ActivityRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_activityrate_json_get()


@router.get(
    "/generated/address_base.json",
    responses={
        200: {"model": AddressBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Address_base",
    response_model_by_alias=True,
)
async def generated_address_base_json_get(
) -> AddressBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_address_base_json_get()


@router.get(
    "/generated/address.json",
    responses={
        200: {"model": Address, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Address",
    response_model_by_alias=True,
)
async def generated_address_json_get(
) -> Address:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_address_json_get()


@router.get(
    "/generated/allocation_base.json",
    responses={
        200: {"model": AllocationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Allocation_base",
    response_model_by_alias=True,
)
async def generated_allocation_base_json_get(
) -> AllocationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_allocation_base_json_get()


@router.get(
    "/generated/allocation.json",
    responses={
        200: {"model": Allocation, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Allocation",
    response_model_by_alias=True,
)
async def generated_allocation_json_get(
) -> Allocation:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_allocation_json_get()


@router.get(
    "/generated/attendee_base.json",
    responses={
        200: {"model": AttendeeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Attendee_base",
    response_model_by_alias=True,
)
async def generated_attendee_base_json_get(
) -> AttendeeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_attendee_base_json_get()


@router.get(
    "/generated/avatar_base.json",
    responses={
        200: {"model": AvatarBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Avatar_base",
    response_model_by_alias=True,
)
async def generated_avatar_base_json_get(
) -> AvatarBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_avatar_base_json_get()


@router.get(
    "/generated/balance_base.json",
    responses={
        200: {"model": BalanceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Balance_base",
    response_model_by_alias=True,
)
async def generated_balance_base_json_get(
) -> BalanceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_balance_base_json_get()


@router.get(
    "/generated/balance.json",
    responses={
        200: {"model": Balance, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Balance",
    response_model_by_alias=True,
)
async def generated_balance_json_get(
) -> Balance:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_balance_json_get()


@router.get(
    "/generated/bankaccount_base.json",
    responses={
        200: {"model": BankAccountBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankAccount_base",
    response_model_by_alias=True,
)
async def generated_bankaccount_base_json_get(
) -> BankAccountBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_bankaccount_base_json_get()


@router.get(
    "/generated/bankaccount.json",
    responses={
        200: {"model": BankAccount, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankAccount",
    response_model_by_alias=True,
)
async def generated_bankaccount_json_get(
) -> BankAccount:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_bankaccount_json_get()


@router.get(
    "/generated/banktransaction_base.json",
    responses={
        200: {"model": BankTransactionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankTransaction_base",
    response_model_by_alias=True,
)
async def generated_banktransaction_base_json_get(
) -> BankTransactionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_banktransaction_base_json_get()


@router.get(
    "/generated/banktransaction.json",
    responses={
        200: {"model": BankTransaction, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankTransaction",
    response_model_by_alias=True,
)
async def generated_banktransaction_json_get(
) -> BankTransaction:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_banktransaction_json_get()


@router.get(
    "/generated/banktransfer_base.json",
    responses={
        200: {"model": BankTransferBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankTransfer_base",
    response_model_by_alias=True,
)
async def generated_banktransfer_base_json_get(
) -> BankTransferBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_banktransfer_base_json_get()


@router.get(
    "/generated/banktransfer.json",
    responses={
        200: {"model": BankTransfer, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BankTransfer",
    response_model_by_alias=True,
)
async def generated_banktransfer_json_get(
) -> BankTransfer:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_banktransfer_json_get()


@router.get(
    "/generated/bill_base.json",
    responses={
        200: {"model": BillBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Bill_base",
    response_model_by_alias=True,
)
async def generated_bill_base_json_get(
) -> BillBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_bill_base_json_get()


@router.get(
    "/generated/bill.json",
    responses={
        200: {"model": Bill, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Bill",
    response_model_by_alias=True,
)
async def generated_bill_json_get(
) -> Bill:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_bill_json_get()


@router.get(
    "/generated/billableclient_base.json",
    responses={
        200: {"model": BillableClientBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillableClient_base",
    response_model_by_alias=True,
)
async def generated_billableclient_base_json_get(
) -> BillableClientBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billableclient_base_json_get()


@router.get(
    "/generated/billableclient.json",
    responses={
        200: {"model": BillableClient, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillableClient",
    response_model_by_alias=True,
)
async def generated_billableclient_json_get(
) -> BillableClient:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billableclient_json_get()


@router.get(
    "/generated/billablematter_base.json",
    responses={
        200: {"model": BillableMatterBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillableMatter_base",
    response_model_by_alias=True,
)
async def generated_billablematter_base_json_get(
) -> BillableMatterBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billablematter_base_json_get()


@router.get(
    "/generated/billablematter.json",
    responses={
        200: {"model": BillableMatter, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillableMatter",
    response_model_by_alias=True,
)
async def generated_billablematter_json_get(
) -> BillableMatter:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billablematter_json_get()


@router.get(
    "/generated/billingsetting_base.json",
    responses={
        200: {"model": BillingSettingBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillingSetting_base",
    response_model_by_alias=True,
)
async def generated_billingsetting_base_json_get(
) -> BillingSettingBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billingsetting_base_json_get()


@router.get(
    "/generated/billingsetting.json",
    responses={
        200: {"model": BillingSetting, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillingSetting",
    response_model_by_alias=True,
)
async def generated_billingsetting_json_get(
) -> BillingSetting:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billingsetting_json_get()


@router.get(
    "/generated/billrecipient_base.json",
    responses={
        200: {"model": BillRecipientBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillRecipient_base",
    response_model_by_alias=True,
)
async def generated_billrecipient_base_json_get(
) -> BillRecipientBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billrecipient_base_json_get()


@router.get(
    "/generated/billrecipient_contact_base.json",
    responses={
        200: {"model": BillRecipientContactBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillRecipient_Contact_base",
    response_model_by_alias=True,
)
async def generated_billrecipient_contact_base_json_get(
) -> BillRecipientContactBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billrecipient_contact_base_json_get()


@router.get(
    "/generated/billrecipient.json",
    responses={
        200: {"model": BillRecipient, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillRecipient",
    response_model_by_alias=True,
)
async def generated_billrecipient_json_get(
) -> BillRecipient:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billrecipient_json_get()


@router.get(
    "/generated/billtheme_base.json",
    responses={
        200: {"model": BillThemeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillTheme_base",
    response_model_by_alias=True,
)
async def generated_billtheme_base_json_get(
) -> BillThemeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billtheme_base_json_get()


@router.get(
    "/generated/billtheme.json",
    responses={
        200: {"model": BillTheme, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for BillTheme",
    response_model_by_alias=True,
)
async def generated_billtheme_json_get(
) -> BillTheme:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_billtheme_json_get()


@router.get(
    "/generated/calendar_base.json",
    responses={
        200: {"model": CalendarBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Calendar_base",
    response_model_by_alias=True,
)
async def generated_calendar_base_json_get(
) -> CalendarBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendar_base_json_get()


@router.get(
    "/generated/calendar.json",
    responses={
        200: {"model": Calendar, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Calendar",
    response_model_by_alias=True,
)
async def generated_calendar_json_get(
) -> Calendar:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendar_json_get()


@router.get(
    "/generated/calendarentry_base.json",
    responses={
        200: {"model": CalendarEntryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CalendarEntry_base",
    response_model_by_alias=True,
)
async def generated_calendarentry_base_json_get(
) -> CalendarEntryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendarentry_base_json_get()


@router.get(
    "/generated/calendarentry.json",
    responses={
        200: {"model": CalendarEntry, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CalendarEntry",
    response_model_by_alias=True,
)
async def generated_calendarentry_json_get(
) -> CalendarEntry:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendarentry_json_get()


@router.get(
    "/generated/calendarentryeventtype_base.json",
    responses={
        200: {"model": CalendarEntryEventTypeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CalendarEntryEventType_base",
    response_model_by_alias=True,
)
async def generated_calendarentryeventtype_base_json_get(
) -> CalendarEntryEventTypeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendarentryeventtype_base_json_get()


@router.get(
    "/generated/calendarvisibility_base.json",
    responses={
        200: {"model": CalendarVisibilityBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CalendarVisibility_base",
    response_model_by_alias=True,
)
async def generated_calendarvisibility_base_json_get(
) -> CalendarVisibilityBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendarvisibility_base_json_get()


@router.get(
    "/generated/calendarvisibility.json",
    responses={
        200: {"model": CalendarVisibility, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CalendarVisibility",
    response_model_by_alias=True,
)
async def generated_calendarvisibility_json_get(
) -> CalendarVisibility:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_calendarvisibility_json_get()


@router.get(
    "/generated/cascadingtask_base.json",
    responses={
        200: {"model": object, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CascadingTask_base",
    response_model_by_alias=True,
)
async def generated_cascadingtask_base_json_get(
) -> object:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cascadingtask_base_json_get()


@router.get(
    "/generated/cascadingtasktemplate_base.json",
    responses={
        200: {"model": CascadingTaskTemplateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CascadingTaskTemplate_base",
    response_model_by_alias=True,
)
async def generated_cascadingtasktemplate_base_json_get(
) -> CascadingTaskTemplateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cascadingtasktemplate_base_json_get()


@router.get(
    "/generated/client_base.json",
    responses={
        200: {"model": ClientBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Client_base",
    response_model_by_alias=True,
)
async def generated_client_base_json_get(
) -> ClientBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_client_base_json_get()


@router.get(
    "/generated/client.json",
    responses={
        200: {"model": Client, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Client",
    response_model_by_alias=True,
)
async def generated_client_json_get(
) -> Client:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_client_json_get()


@router.get(
    "/generated/clientportal_base.json",
    responses={
        200: {"model": ClientPortalBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClientPortal_base",
    response_model_by_alias=True,
)
async def generated_clientportal_base_json_get(
) -> ClientPortalBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_clientportal_base_json_get()


@router.get(
    "/generated/cliocreator_base.json",
    responses={
        200: {"model": ClioCreatorBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClioCreator_base",
    response_model_by_alias=True,
)
async def generated_cliocreator_base_json_get(
) -> ClioCreatorBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cliocreator_base_json_get()


@router.get(
    "/generated/cliopaymentslink_base.json",
    responses={
        200: {"model": ClioPaymentsLinkBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClioPaymentsLink_base",
    response_model_by_alias=True,
)
async def generated_cliopaymentslink_base_json_get(
) -> ClioPaymentsLinkBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cliopaymentslink_base_json_get()


@router.get(
    "/generated/cliopaymentslink.json",
    responses={
        200: {"model": ClioPaymentsLink, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClioPaymentsLink",
    response_model_by_alias=True,
)
async def generated_cliopaymentslink_json_get(
) -> ClioPaymentsLink:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cliopaymentslink_json_get()


@router.get(
    "/generated/cliopaymentspayment_base.json",
    responses={
        200: {"model": ClioPaymentsPaymentBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClioPaymentsPayment_base",
    response_model_by_alias=True,
)
async def generated_cliopaymentspayment_base_json_get(
) -> ClioPaymentsPaymentBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cliopaymentspayment_base_json_get()


@router.get(
    "/generated/cliopaymentspayment.json",
    responses={
        200: {"model": ClioPaymentsPayment, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ClioPaymentsPayment",
    response_model_by_alias=True,
)
async def generated_cliopaymentspayment_json_get(
) -> ClioPaymentsPayment:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_cliopaymentspayment_json_get()


@router.get(
    "/generated/comment_base.json",
    responses={
        200: {"model": CommentBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Comment_base",
    response_model_by_alias=True,
)
async def generated_comment_base_json_get(
) -> CommentBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_comment_base_json_get()


@router.get(
    "/generated/comment.json",
    responses={
        200: {"model": Comment, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Comment",
    response_model_by_alias=True,
)
async def generated_comment_json_get(
) -> Comment:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_comment_json_get()


@router.get(
    "/generated/communication_base.json",
    responses={
        200: {"model": CommunicationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Communication_base",
    response_model_by_alias=True,
)
async def generated_communication_base_json_get(
) -> CommunicationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_communication_base_json_get()


@router.get(
    "/generated/communication.json",
    responses={
        200: {"model": Communication, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Communication",
    response_model_by_alias=True,
)
async def generated_communication_json_get(
) -> Communication:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_communication_json_get()


@router.get(
    "/generated/communicationemlfile_base.json",
    responses={
        200: {"model": CommunicationEmlFileBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CommunicationEmlFile_base",
    response_model_by_alias=True,
)
async def generated_communicationemlfile_base_json_get(
) -> CommunicationEmlFileBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_communicationemlfile_base_json_get()


@router.get(
    "/generated/conferencemeeting_base.json",
    responses={
        200: {"model": ConferenceMeetingBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ConferenceMeeting_base",
    response_model_by_alias=True,
)
async def generated_conferencemeeting_base_json_get(
) -> ConferenceMeetingBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conferencemeeting_base_json_get()


@router.get(
    "/generated/contact_base.json",
    responses={
        200: {"model": ContactBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Contact_base",
    response_model_by_alias=True,
)
async def generated_contact_base_json_get(
) -> ContactBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_contact_base_json_get()


@router.get(
    "/generated/contact.json",
    responses={
        200: {"model": Contact, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Contact",
    response_model_by_alias=True,
)
async def generated_contact_json_get(
) -> Contact:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_contact_json_get()


@router.get(
    "/generated/contingencyfee_base.json",
    responses={
        200: {"model": ContingencyFeeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ContingencyFee_base",
    response_model_by_alias=True,
)
async def generated_contingencyfee_base_json_get(
) -> ContingencyFeeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_contingencyfee_base_json_get()


@router.get(
    "/generated/conversation_base.json",
    responses={
        200: {"model": ConversationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Conversation_base",
    response_model_by_alias=True,
)
async def generated_conversation_base_json_get(
) -> ConversationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversation_base_json_get()


@router.get(
    "/generated/conversation.json",
    responses={
        200: {"model": Conversation, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Conversation",
    response_model_by_alias=True,
)
async def generated_conversation_json_get(
) -> Conversation:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversation_json_get()


@router.get(
    "/generated/conversationmembership_base.json",
    responses={
        200: {"model": ConversationMembershipBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ConversationMembership_base",
    response_model_by_alias=True,
)
async def generated_conversationmembership_base_json_get(
) -> ConversationMembershipBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversationmembership_base_json_get()


@router.get(
    "/generated/conversationmembership.json",
    responses={
        200: {"model": ConversationMembership, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ConversationMembership",
    response_model_by_alias=True,
)
async def generated_conversationmembership_json_get(
) -> ConversationMembership:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversationmembership_json_get()


@router.get(
    "/generated/conversationmessage_base.json",
    responses={
        200: {"model": ConversationMessageBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ConversationMessage_base",
    response_model_by_alias=True,
)
async def generated_conversationmessage_base_json_get(
) -> ConversationMessageBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversationmessage_base_json_get()


@router.get(
    "/generated/conversationmessage.json",
    responses={
        200: {"model": ConversationMessage, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ConversationMessage",
    response_model_by_alias=True,
)
async def generated_conversationmessage_json_get(
) -> ConversationMessage:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_conversationmessage_json_get()


@router.get(
    "/generated/creditmemo_base.json",
    responses={
        200: {"model": CreditMemoBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CreditMemo_base",
    response_model_by_alias=True,
)
async def generated_creditmemo_base_json_get(
) -> CreditMemoBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_creditmemo_base_json_get()


@router.get(
    "/generated/creditmemo.json",
    responses={
        200: {"model": CreditMemo, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CreditMemo",
    response_model_by_alias=True,
)
async def generated_creditmemo_json_get(
) -> CreditMemo:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_creditmemo_json_get()


@router.get(
    "/generated/currency_base.json",
    responses={
        200: {"model": CurrencyBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Currency_base",
    response_model_by_alias=True,
)
async def generated_currency_base_json_get(
) -> CurrencyBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_currency_base_json_get()


@router.get(
    "/generated/currency.json",
    responses={
        200: {"model": Currency, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Currency",
    response_model_by_alias=True,
)
async def generated_currency_json_get(
) -> Currency:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_currency_json_get()


@router.get(
    "/generated/customaction_base.json",
    responses={
        200: {"model": CustomActionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomAction_base",
    response_model_by_alias=True,
)
async def generated_customaction_base_json_get(
) -> CustomActionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customaction_base_json_get()


@router.get(
    "/generated/customaction.json",
    responses={
        200: {"model": CustomAction, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomAction",
    response_model_by_alias=True,
)
async def generated_customaction_json_get(
) -> CustomAction:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customaction_json_get()


@router.get(
    "/generated/customfield_base.json",
    responses={
        200: {"model": CustomFieldBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomField_base",
    response_model_by_alias=True,
)
async def generated_customfield_base_json_get(
) -> CustomFieldBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfield_base_json_get()


@router.get(
    "/generated/customfield.json",
    responses={
        200: {"model": CustomField, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomField",
    response_model_by_alias=True,
)
async def generated_customfield_json_get(
) -> CustomField:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfield_json_get()


@router.get(
    "/generated/customfieldmatterselection_base.json",
    responses={
        200: {"model": CustomFieldMatterSelectionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldMatterSelection_base",
    response_model_by_alias=True,
)
async def generated_customfieldmatterselection_base_json_get(
) -> CustomFieldMatterSelectionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldmatterselection_base_json_get()


@router.get(
    "/generated/customfieldmatterselection.json",
    responses={
        200: {"model": CustomFieldMatterSelection, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldMatterSelection",
    response_model_by_alias=True,
)
async def generated_customfieldmatterselection_json_get(
) -> CustomFieldMatterSelection:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldmatterselection_json_get()


@router.get(
    "/generated/customfieldset_base.json",
    responses={
        200: {"model": CustomFieldSetBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldSet_base",
    response_model_by_alias=True,
)
async def generated_customfieldset_base_json_get(
) -> CustomFieldSetBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldset_base_json_get()


@router.get(
    "/generated/customfieldset.json",
    responses={
        200: {"model": CustomFieldSet, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldSet",
    response_model_by_alias=True,
)
async def generated_customfieldset_json_get(
) -> CustomFieldSet:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldset_json_get()


@router.get(
    "/generated/customfieldsetassociation_base.json",
    responses={
        200: {"model": CustomFieldSetAssociationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldSetAssociation_base",
    response_model_by_alias=True,
)
async def generated_customfieldsetassociation_base_json_get(
) -> CustomFieldSetAssociationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldsetassociation_base_json_get()


@router.get(
    "/generated/customfieldvalue_base.json",
    responses={
        200: {"model": CustomFieldValueBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldValue_base",
    response_model_by_alias=True,
)
async def generated_customfieldvalue_base_json_get(
) -> CustomFieldValueBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldvalue_base_json_get()


@router.get(
    "/generated/customfieldvalue.json",
    responses={
        200: {"model": CustomFieldValue, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for CustomFieldValue",
    response_model_by_alias=True,
)
async def generated_customfieldvalue_json_get(
) -> CustomFieldValue:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_customfieldvalue_json_get()


@router.get(
    "/generated/damage_base.json",
    responses={
        200: {"model": DamageBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Damage_base",
    response_model_by_alias=True,
)
async def generated_damage_base_json_get(
) -> DamageBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_damage_base_json_get()


@router.get(
    "/generated/damage.json",
    responses={
        200: {"model": Damage, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Damage",
    response_model_by_alias=True,
)
async def generated_damage_json_get(
) -> Damage:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_damage_json_get()


@router.get(
    "/generated/discount_base.json",
    responses={
        200: {"model": DiscountBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Discount_base",
    response_model_by_alias=True,
)
async def generated_discount_base_json_get(
) -> DiscountBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_discount_base_json_get()


@router.get(
    "/generated/document_base.json",
    responses={
        200: {"model": DocumentBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Document_base",
    response_model_by_alias=True,
)
async def generated_document_base_json_get(
) -> DocumentBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_document_base_json_get()


@router.get(
    "/generated/document.json",
    responses={
        200: {"model": Document, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Document",
    response_model_by_alias=True,
)
async def generated_document_json_get(
) -> Document:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_document_json_get()


@router.get(
    "/generated/documentarchive_base.json",
    responses={
        200: {"model": DocumentArchiveBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentArchive_base",
    response_model_by_alias=True,
)
async def generated_documentarchive_base_json_get(
) -> DocumentArchiveBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentarchive_base_json_get()


@router.get(
    "/generated/documentarchive.json",
    responses={
        200: {"model": DocumentArchive, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentArchive",
    response_model_by_alias=True,
)
async def generated_documentarchive_json_get(
) -> DocumentArchive:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentarchive_json_get()


@router.get(
    "/generated/documentautomation_base.json",
    responses={
        200: {"model": DocumentAutomationBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentAutomation_base",
    response_model_by_alias=True,
)
async def generated_documentautomation_base_json_get(
) -> DocumentAutomationBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentautomation_base_json_get()


@router.get(
    "/generated/documentautomation.json",
    responses={
        200: {"model": DocumentAutomation, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentAutomation",
    response_model_by_alias=True,
)
async def generated_documentautomation_json_get(
) -> DocumentAutomation:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentautomation_json_get()


@router.get(
    "/generated/documentcategory_base.json",
    responses={
        200: {"model": DocumentCategoryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentCategory_base",
    response_model_by_alias=True,
)
async def generated_documentcategory_base_json_get(
) -> DocumentCategoryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentcategory_base_json_get()


@router.get(
    "/generated/documentcategory.json",
    responses={
        200: {"model": DocumentCategory, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentCategory",
    response_model_by_alias=True,
)
async def generated_documentcategory_json_get(
) -> DocumentCategory:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentcategory_json_get()


@router.get(
    "/generated/documenttemplate_base.json",
    responses={
        200: {"model": DocumentTemplateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentTemplate_base",
    response_model_by_alias=True,
)
async def generated_documenttemplate_base_json_get(
) -> DocumentTemplateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documenttemplate_base_json_get()


@router.get(
    "/generated/documenttemplate.json",
    responses={
        200: {"model": DocumentTemplate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentTemplate",
    response_model_by_alias=True,
)
async def generated_documenttemplate_json_get(
) -> DocumentTemplate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documenttemplate_json_get()


@router.get(
    "/generated/documentversion_base.json",
    responses={
        200: {"model": DocumentVersionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentVersion_base",
    response_model_by_alias=True,
)
async def generated_documentversion_base_json_get(
) -> DocumentVersionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentversion_base_json_get()


@router.get(
    "/generated/documentversion.json",
    responses={
        200: {"model": DocumentVersion, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for DocumentVersion",
    response_model_by_alias=True,
)
async def generated_documentversion_json_get(
) -> DocumentVersion:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_documentversion_json_get()


@router.get(
    "/generated/emailaddress_base.json",
    responses={
        200: {"model": EmailAddressBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for EmailAddress_base",
    response_model_by_alias=True,
)
async def generated_emailaddress_base_json_get(
) -> EmailAddressBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_emailaddress_base_json_get()


@router.get(
    "/generated/emailaddress.json",
    responses={
        200: {"model": EmailAddress, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for EmailAddress",
    response_model_by_alias=True,
)
async def generated_emailaddress_json_get(
) -> EmailAddress:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_emailaddress_json_get()


@router.get(
    "/generated/errordetail.json",
    responses={
        200: {"model": ErrorDetail, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ErrorDetail",
    response_model_by_alias=True,
)
async def generated_errordetail_json_get(
) -> ErrorDetail:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_errordetail_json_get()


@router.get(
    "/generated/event_base.json",
    responses={
        200: {"model": EventBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Event_base",
    response_model_by_alias=True,
)
async def generated_event_base_json_get(
) -> EventBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_event_base_json_get()


@router.get(
    "/generated/event.json",
    responses={
        200: {"model": Event, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Event",
    response_model_by_alias=True,
)
async def generated_event_json_get(
) -> Event:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_event_json_get()


@router.get(
    "/generated/eventmetrics_base.json",
    responses={
        200: {"model": EventMetricsBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for EventMetrics_base",
    response_model_by_alias=True,
)
async def generated_eventmetrics_base_json_get(
) -> EventMetricsBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_eventmetrics_base_json_get()


@router.get(
    "/generated/eventmetrics.json",
    responses={
        200: {"model": EventMetrics, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for EventMetrics",
    response_model_by_alias=True,
)
async def generated_eventmetrics_json_get(
) -> EventMetrics:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_eventmetrics_json_get()


@router.get(
    "/generated/evergreenretainer_base.json",
    responses={
        200: {"model": EvergreenRetainerBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for EvergreenRetainer_base",
    response_model_by_alias=True,
)
async def generated_evergreenretainer_base_json_get(
) -> EvergreenRetainerBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_evergreenretainer_base_json_get()


@router.get(
    "/generated/expensecategory_base.json",
    responses={
        200: {"model": ExpenseCategoryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ExpenseCategory_base",
    response_model_by_alias=True,
)
async def generated_expensecategory_base_json_get(
) -> ExpenseCategoryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_expensecategory_base_json_get()


@router.get(
    "/generated/expensecategory.json",
    responses={
        200: {"model": ExpenseCategory, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ExpenseCategory",
    response_model_by_alias=True,
)
async def generated_expensecategory_json_get(
) -> ExpenseCategory:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_expensecategory_json_get()


@router.get(
    "/generated/externalproperty_base.json",
    responses={
        200: {"model": ExternalPropertyBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ExternalProperty_base",
    response_model_by_alias=True,
)
async def generated_externalproperty_base_json_get(
) -> ExternalPropertyBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_externalproperty_base_json_get()


@router.get(
    "/generated/folder_base.json",
    responses={
        200: {"model": FolderBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Folder_base",
    response_model_by_alias=True,
)
async def generated_folder_base_json_get(
) -> FolderBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_folder_base_json_get()


@router.get(
    "/generated/folder.json",
    responses={
        200: {"model": Folder, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Folder",
    response_model_by_alias=True,
)
async def generated_folder_json_get(
) -> Folder:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_folder_json_get()


@router.get(
    "/generated/grant_base.json",
    responses={
        200: {"model": GrantBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Grant_base",
    response_model_by_alias=True,
)
async def generated_grant_base_json_get(
) -> GrantBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_grant_base_json_get()


@router.get(
    "/generated/grant.json",
    responses={
        200: {"model": Grant, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Grant",
    response_model_by_alias=True,
)
async def generated_grant_json_get(
) -> Grant:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_grant_json_get()


@router.get(
    "/generated/grantfundingsource_base.json",
    responses={
        200: {"model": GrantFundingSourceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for GrantFundingSource_base",
    response_model_by_alias=True,
)
async def generated_grantfundingsource_base_json_get(
) -> GrantFundingSourceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_grantfundingsource_base_json_get()


@router.get(
    "/generated/grantfundingsource.json",
    responses={
        200: {"model": GrantFundingSource, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for GrantFundingSource",
    response_model_by_alias=True,
)
async def generated_grantfundingsource_json_get(
) -> GrantFundingSource:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_grantfundingsource_json_get()


@router.get(
    "/generated/group_base.json",
    responses={
        200: {"model": GroupBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Group_base",
    response_model_by_alias=True,
)
async def generated_group_base_json_get(
) -> GroupBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_group_base_json_get()


@router.get(
    "/generated/group.json",
    responses={
        200: {"model": Group, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Group",
    response_model_by_alias=True,
)
async def generated_group_json_get(
) -> Group:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_group_json_get()


@router.get(
    "/generated/idsresponse.json",
    responses={
        200: {"model": IdsResponse, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for IdsResponse",
    response_model_by_alias=True,
)
async def generated_idsresponse_json_get(
) -> IdsResponse:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_idsresponse_json_get()


@router.get(
    "/generated/instantmessenger_base.json",
    responses={
        200: {"model": InstantMessengerBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for InstantMessenger_base",
    response_model_by_alias=True,
)
async def generated_instantmessenger_base_json_get(
) -> InstantMessengerBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_instantmessenger_base_json_get()


@router.get(
    "/generated/interest_base.json",
    responses={
        200: {"model": InterestBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Interest_base",
    response_model_by_alias=True,
)
async def generated_interest_base_json_get(
) -> InterestBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_interest_base_json_get()


@router.get(
    "/generated/interest.json",
    responses={
        200: {"model": Interest, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Interest",
    response_model_by_alias=True,
)
async def generated_interest_json_get(
) -> Interest:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_interest_json_get()


@router.get(
    "/generated/interestcharge_base.json",
    responses={
        200: {"model": InterestChargeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for InterestCharge_base",
    response_model_by_alias=True,
)
async def generated_interestcharge_base_json_get(
) -> InterestChargeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_interestcharge_base_json_get()


@router.get(
    "/generated/interestcharge.json",
    responses={
        200: {"model": InterestCharge, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for InterestCharge",
    response_model_by_alias=True,
)
async def generated_interestcharge_json_get(
) -> InterestCharge:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_interestcharge_json_get()


@router.get(
    "/generated/item_base.json",
    responses={
        200: {"model": ItemBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Item_base",
    response_model_by_alias=True,
)
async def generated_item_base_json_get(
) -> ItemBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_item_base_json_get()


@router.get(
    "/generated/item.json",
    responses={
        200: {"model": Item, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Item",
    response_model_by_alias=True,
)
async def generated_item_json_get(
) -> Item:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_item_json_get()


@router.get(
    "/generated/jobtitle_base.json",
    responses={
        200: {"model": JobTitleBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for JobTitle_base",
    response_model_by_alias=True,
)
async def generated_jobtitle_base_json_get(
) -> JobTitleBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_jobtitle_base_json_get()


@router.get(
    "/generated/jurisdiction_base.json",
    responses={
        200: {"model": JurisdictionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Jurisdiction_base",
    response_model_by_alias=True,
)
async def generated_jurisdiction_base_json_get(
) -> JurisdictionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_jurisdiction_base_json_get()


@router.get(
    "/generated/jurisdiction.json",
    responses={
        200: {"model": Jurisdiction, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Jurisdiction",
    response_model_by_alias=True,
)
async def generated_jurisdiction_json_get(
) -> Jurisdiction:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_jurisdiction_json_get()


@router.get(
    "/generated/jurisdictionstotrigger_base.json",
    responses={
        200: {"model": JurisdictionsToTriggerBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for JurisdictionsToTrigger_base",
    response_model_by_alias=True,
)
async def generated_jurisdictionstotrigger_base_json_get(
) -> JurisdictionsToTriggerBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_jurisdictionstotrigger_base_json_get()


@router.get(
    "/generated/jurisdictionstotrigger.json",
    responses={
        200: {"model": JurisdictionsToTrigger, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for JurisdictionsToTrigger",
    response_model_by_alias=True,
)
async def generated_jurisdictionstotrigger_json_get(
) -> JurisdictionsToTrigger:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_jurisdictionstotrigger_json_get()


@router.get(
    "/generated/laukcivilcertificatedrate_base.json",
    responses={
        200: {"model": LaukCivilCertificatedRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCivilCertificatedRate_base",
    response_model_by_alias=True,
)
async def generated_laukcivilcertificatedrate_base_json_get(
) -> LaukCivilCertificatedRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcivilcertificatedrate_base_json_get()


@router.get(
    "/generated/laukcivilcertificatedrate.json",
    responses={
        200: {"model": LaukCivilCertificatedRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCivilCertificatedRate",
    response_model_by_alias=True,
)
async def generated_laukcivilcertificatedrate_json_get(
) -> LaukCivilCertificatedRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcivilcertificatedrate_json_get()


@router.get(
    "/generated/laukcivilcontrolledrate_base.json",
    responses={
        200: {"model": LaukCivilControlledRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCivilControlledRate_base",
    response_model_by_alias=True,
)
async def generated_laukcivilcontrolledrate_base_json_get(
) -> LaukCivilControlledRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcivilcontrolledrate_base_json_get()


@router.get(
    "/generated/laukcivilcontrolledrate.json",
    responses={
        200: {"model": LaukCivilControlledRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCivilControlledRate",
    response_model_by_alias=True,
)
async def generated_laukcivilcontrolledrate_json_get(
) -> LaukCivilControlledRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcivilcontrolledrate_json_get()


@router.get(
    "/generated/laukcriminalcontrolledrate_base.json",
    responses={
        200: {"model": LaukCriminalControlledRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCriminalControlledRate_base",
    response_model_by_alias=True,
)
async def generated_laukcriminalcontrolledrate_base_json_get(
) -> LaukCriminalControlledRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcriminalcontrolledrate_base_json_get()


@router.get(
    "/generated/laukcriminalcontrolledrate.json",
    responses={
        200: {"model": LaukCriminalControlledRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukCriminalControlledRate",
    response_model_by_alias=True,
)
async def generated_laukcriminalcontrolledrate_json_get(
) -> LaukCriminalControlledRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukcriminalcontrolledrate_json_get()


@router.get(
    "/generated/laukexpensecategory_base.json",
    responses={
        200: {"model": LaukExpenseCategoryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukExpenseCategory_base",
    response_model_by_alias=True,
)
async def generated_laukexpensecategory_base_json_get(
) -> LaukExpenseCategoryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukexpensecategory_base_json_get()


@router.get(
    "/generated/laukexpensecategory.json",
    responses={
        200: {"model": LaukExpenseCategory, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LaukExpenseCategory",
    response_model_by_alias=True,
)
async def generated_laukexpensecategory_json_get(
) -> LaukExpenseCategory:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_laukexpensecategory_json_get()


@router.get(
    "/generated/legalaidukactivity_base.json",
    responses={
        200: {"model": LegalAidUkActivityBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LegalAidUkActivity_base",
    response_model_by_alias=True,
)
async def generated_legalaidukactivity_base_json_get(
) -> LegalAidUkActivityBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_legalaidukactivity_base_json_get()


@router.get(
    "/generated/legalaidukbill_base.json",
    responses={
        200: {"model": LegalAidUkBillBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LegalAidUkBill_base",
    response_model_by_alias=True,
)
async def generated_legalaidukbill_base_json_get(
) -> LegalAidUkBillBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_legalaidukbill_base_json_get()


@router.get(
    "/generated/legalaidukcontact_base.json",
    responses={
        200: {"model": LegalAidUkContactBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LegalAidUkContact_base",
    response_model_by_alias=True,
)
async def generated_legalaidukcontact_base_json_get(
) -> LegalAidUkContactBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_legalaidukcontact_base_json_get()


@router.get(
    "/generated/legalaidukmatter_base.json",
    responses={
        200: {"model": LegalAidUkMatterBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LegalAidUkMatter_base",
    response_model_by_alias=True,
)
async def generated_legalaidukmatter_base_json_get(
) -> LegalAidUkMatterBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_legalaidukmatter_base_json_get()


@router.get(
    "/generated/lien_base.json",
    responses={
        200: {"model": LienBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Lien_base",
    response_model_by_alias=True,
)
async def generated_lien_base_json_get(
) -> LienBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_lien_base_json_get()


@router.get(
    "/generated/lineitem_base.json",
    responses={
        200: {"model": LineItemBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LineItem_base",
    response_model_by_alias=True,
)
async def generated_lineitem_base_json_get(
) -> LineItemBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_lineitem_base_json_get()


@router.get(
    "/generated/lineitem.json",
    responses={
        200: {"model": LineItem, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LineItem",
    response_model_by_alias=True,
)
async def generated_lineitem_json_get(
) -> LineItem:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_lineitem_json_get()


@router.get(
    "/generated/lineitemtotals_base.json",
    responses={
        200: {"model": LineItemTotalsBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LineItemTotals_base",
    response_model_by_alias=True,
)
async def generated_lineitemtotals_base_json_get(
) -> LineItemTotalsBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_lineitemtotals_base_json_get()


@router.get(
    "/generated/linkedfolder_base.json",
    responses={
        200: {"model": LinkedFolderBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LinkedFolder_base",
    response_model_by_alias=True,
)
async def generated_linkedfolder_base_json_get(
) -> LinkedFolderBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_linkedfolder_base_json_get()


@router.get(
    "/generated/logentry_base.json",
    responses={
        200: {"model": LogEntryBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LogEntry_base",
    response_model_by_alias=True,
)
async def generated_logentry_base_json_get(
) -> LogEntryBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_logentry_base_json_get()


@router.get(
    "/generated/logentry.json",
    responses={
        200: {"model": LogEntry, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for LogEntry",
    response_model_by_alias=True,
)
async def generated_logentry_json_get(
) -> LogEntry:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_logentry_json_get()


@router.get(
    "/generated/matter_base.json",
    responses={
        200: {"model": MatterBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Matter_base",
    response_model_by_alias=True,
)
async def generated_matter_base_json_get(
) -> MatterBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matter_base_json_get()


@router.get(
    "/generated/matter.json",
    responses={
        200: {"model": Matter, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Matter",
    response_model_by_alias=True,
)
async def generated_matter_json_get(
) -> Matter:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matter_json_get()


@router.get(
    "/generated/matterbalance_base.json",
    responses={
        200: {"model": MatterBalanceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterBalance_base",
    response_model_by_alias=True,
)
async def generated_matterbalance_base_json_get(
) -> MatterBalanceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterbalance_base_json_get()


@router.get(
    "/generated/matterbillrecipient_base.json",
    responses={
        200: {"model": MatterBillRecipientBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterBillRecipient_base",
    response_model_by_alias=True,
)
async def generated_matterbillrecipient_base_json_get(
) -> MatterBillRecipientBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterbillrecipient_base_json_get()


@router.get(
    "/generated/matterbillrecipient.json",
    responses={
        200: {"model": MatterBillRecipient, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterBillRecipient",
    response_model_by_alias=True,
)
async def generated_matterbillrecipient_json_get(
) -> MatterBillRecipient:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterbillrecipient_json_get()


@router.get(
    "/generated/matterbudget_base.json",
    responses={
        200: {"model": MatterBudgetBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterBudget_base",
    response_model_by_alias=True,
)
async def generated_matterbudget_base_json_get(
) -> MatterBudgetBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterbudget_base_json_get()


@router.get(
    "/generated/mattercontacts_base.json",
    responses={
        200: {"model": MatterContactsBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterContacts_base",
    response_model_by_alias=True,
)
async def generated_mattercontacts_base_json_get(
) -> MatterContactsBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_mattercontacts_base_json_get()


@router.get(
    "/generated/mattercontacts.json",
    responses={
        200: {"model": MatterContacts, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterContacts",
    response_model_by_alias=True,
)
async def generated_mattercontacts_json_get(
) -> MatterContacts:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_mattercontacts_json_get()


@router.get(
    "/generated/mattercustomrate_base.json",
    responses={
        200: {"model": MatterCustomRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterCustomRate_base",
    response_model_by_alias=True,
)
async def generated_mattercustomrate_base_json_get(
) -> MatterCustomRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_mattercustomrate_base_json_get()


@router.get(
    "/generated/mattercustomrate.json",
    responses={
        200: {"model": MatterCustomRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterCustomRate",
    response_model_by_alias=True,
)
async def generated_mattercustomrate_json_get(
) -> MatterCustomRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_mattercustomrate_json_get()


@router.get(
    "/generated/matterdocket_base.json",
    responses={
        200: {"model": MatterDocketBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterDocket_base",
    response_model_by_alias=True,
)
async def generated_matterdocket_base_json_get(
) -> MatterDocketBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterdocket_base_json_get()


@router.get(
    "/generated/matterdocket.json",
    responses={
        200: {"model": MatterDocket, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterDocket",
    response_model_by_alias=True,
)
async def generated_matterdocket_json_get(
) -> MatterDocket:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterdocket_json_get()


@router.get(
    "/generated/matterstage_base.json",
    responses={
        200: {"model": MatterStageBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterStage_base",
    response_model_by_alias=True,
)
async def generated_matterstage_base_json_get(
) -> MatterStageBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterstage_base_json_get()


@router.get(
    "/generated/matterstage.json",
    responses={
        200: {"model": MatterStage, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MatterStage",
    response_model_by_alias=True,
)
async def generated_matterstage_json_get(
) -> MatterStage:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_matterstage_json_get()


@router.get(
    "/generated/medicalbill_base.json",
    responses={
        200: {"model": MedicalBillBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalBill_base",
    response_model_by_alias=True,
)
async def generated_medicalbill_base_json_get(
) -> MedicalBillBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalbill_base_json_get()


@router.get(
    "/generated/medicalbill.json",
    responses={
        200: {"model": MedicalBill, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalBill",
    response_model_by_alias=True,
)
async def generated_medicalbill_json_get(
) -> MedicalBill:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalbill_json_get()


@router.get(
    "/generated/medicalrecord_base.json",
    responses={
        200: {"model": MedicalRecordBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalRecord_base",
    response_model_by_alias=True,
)
async def generated_medicalrecord_base_json_get(
) -> MedicalRecordBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalrecord_base_json_get()


@router.get(
    "/generated/medicalrecord.json",
    responses={
        200: {"model": MedicalRecord, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalRecord",
    response_model_by_alias=True,
)
async def generated_medicalrecord_json_get(
) -> MedicalRecord:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalrecord_json_get()


@router.get(
    "/generated/medicalrecordsrequest_base.json",
    responses={
        200: {"model": MedicalRecordsRequestBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalRecordsRequest_base",
    response_model_by_alias=True,
)
async def generated_medicalrecordsrequest_base_json_get(
) -> MedicalRecordsRequestBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalrecordsrequest_base_json_get()


@router.get(
    "/generated/medicalrecordsrequest.json",
    responses={
        200: {"model": MedicalRecordsRequest, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MedicalRecordsRequest",
    response_model_by_alias=True,
)
async def generated_medicalrecordsrequest_json_get(
) -> MedicalRecordsRequest:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_medicalrecordsrequest_json_get()


@router.get(
    "/generated/multipart_base.json",
    responses={
        200: {"model": MultipartBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Multipart_base",
    response_model_by_alias=True,
)
async def generated_multipart_base_json_get(
) -> MultipartBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_multipart_base_json_get()


@router.get(
    "/generated/multipart.json",
    responses={
        200: {"model": Multipart, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Multipart",
    response_model_by_alias=True,
)
async def generated_multipart_json_get(
) -> Multipart:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_multipart_json_get()


@router.get(
    "/generated/multipartheader_base.json",
    responses={
        200: {"model": MultipartHeaderBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MultipartHeader_base",
    response_model_by_alias=True,
)
async def generated_multipartheader_base_json_get(
) -> MultipartHeaderBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_multipartheader_base_json_get()


@router.get(
    "/generated/myevent_base.json",
    responses={
        200: {"model": object, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MyEvent_base",
    response_model_by_alias=True,
)
async def generated_myevent_base_json_get(
) -> object:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_myevent_base_json_get()


@router.get(
    "/generated/myevent.json",
    responses={
        200: {"model": MyEvent, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for MyEvent",
    response_model_by_alias=True,
)
async def generated_myevent_json_get(
) -> MyEvent:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_myevent_json_get()


@router.get(
    "/generated/note_base.json",
    responses={
        200: {"model": NoteBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Note_base",
    response_model_by_alias=True,
)
async def generated_note_base_json_get(
) -> NoteBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_note_base_json_get()


@router.get(
    "/generated/note.json",
    responses={
        200: {"model": Note, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Note",
    response_model_by_alias=True,
)
async def generated_note_json_get(
) -> Note:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_note_json_get()


@router.get(
    "/generated/notificationeventsubscriber_base.json",
    responses={
        200: {"model": NotificationEventSubscriberBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for NotificationEventSubscriber_base",
    response_model_by_alias=True,
)
async def generated_notificationeventsubscriber_base_json_get(
) -> NotificationEventSubscriberBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_notificationeventsubscriber_base_json_get()


@router.get(
    "/generated/notificationmethod_base.json",
    responses={
        200: {"model": NotificationMethodBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for NotificationMethod_base",
    response_model_by_alias=True,
)
async def generated_notificationmethod_base_json_get(
) -> NotificationMethodBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_notificationmethod_base_json_get()


@router.get(
    "/generated/outstandingclientbalance_base.json",
    responses={
        200: {"model": OutstandingClientBalanceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for OutstandingClientBalance_base",
    response_model_by_alias=True,
)
async def generated_outstandingclientbalance_base_json_get(
) -> OutstandingClientBalanceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_outstandingclientbalance_base_json_get()


@router.get(
    "/generated/outstandingclientbalance.json",
    responses={
        200: {"model": OutstandingClientBalance, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for OutstandingClientBalance",
    response_model_by_alias=True,
)
async def generated_outstandingclientbalance_json_get(
) -> OutstandingClientBalance:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_outstandingclientbalance_json_get()


@router.get(
    "/generated/participant_base.json",
    responses={
        200: {"model": ParticipantBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Participant_base",
    response_model_by_alias=True,
)
async def generated_participant_base_json_get(
) -> ParticipantBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_participant_base_json_get()


@router.get(
    "/generated/participant.json",
    responses={
        200: {"model": Participant, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Participant",
    response_model_by_alias=True,
)
async def generated_participant_json_get(
) -> Participant:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_participant_json_get()


@router.get(
    "/generated/payment_base.json",
    responses={
        200: {"model": PaymentBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Payment_base",
    response_model_by_alias=True,
)
async def generated_payment_base_json_get(
) -> PaymentBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_payment_base_json_get()


@router.get(
    "/generated/payment.json",
    responses={
        200: {"model": Payment, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Payment",
    response_model_by_alias=True,
)
async def generated_payment_json_get(
) -> Payment:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_payment_json_get()


@router.get(
    "/generated/paymentprofile_base.json",
    responses={
        200: {"model": PaymentProfileBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PaymentProfile_base",
    response_model_by_alias=True,
)
async def generated_paymentprofile_base_json_get(
) -> PaymentProfileBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_paymentprofile_base_json_get()


@router.get(
    "/generated/phonenumber_base.json",
    responses={
        200: {"model": PhoneNumberBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PhoneNumber_base",
    response_model_by_alias=True,
)
async def generated_phonenumber_base_json_get(
) -> PhoneNumberBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_phonenumber_base_json_get()


@router.get(
    "/generated/phonenumber.json",
    responses={
        200: {"model": PhoneNumber, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PhoneNumber",
    response_model_by_alias=True,
)
async def generated_phonenumber_json_get(
) -> PhoneNumber:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_phonenumber_json_get()


@router.get(
    "/generated/picklistoption_base.json",
    responses={
        200: {"model": PicklistOptionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PicklistOption_base",
    response_model_by_alias=True,
)
async def generated_picklistoption_base_json_get(
) -> PicklistOptionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_picklistoption_base_json_get()


@router.get(
    "/generated/picklistoption.json",
    responses={
        200: {"model": PicklistOption, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PicklistOption",
    response_model_by_alias=True,
)
async def generated_picklistoption_json_get(
) -> PicklistOption:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_picklistoption_json_get()


@router.get(
    "/generated/polymorphiccustomrate_activitydescription_base.json",
    responses={
        200: {"model": PolymorphicCustomRateActivityDescriptionBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicCustomRate_ActivityDescription_base",
    response_model_by_alias=True,
)
async def generated_polymorphiccustomrate_activitydescription_base_json_get(
) -> PolymorphicCustomRateActivityDescriptionBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphiccustomrate_activitydescription_base_json_get()


@router.get(
    "/generated/polymorphiccustomrate_base.json",
    responses={
        200: {"model": PolymorphicCustomRateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicCustomRate_base",
    response_model_by_alias=True,
)
async def generated_polymorphiccustomrate_base_json_get(
) -> PolymorphicCustomRateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphiccustomrate_base_json_get()


@router.get(
    "/generated/polymorphiccustomrate_group_base.json",
    responses={
        200: {"model": PolymorphicCustomRateGroupBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicCustomRate_Group_base",
    response_model_by_alias=True,
)
async def generated_polymorphiccustomrate_group_base_json_get(
) -> PolymorphicCustomRateGroupBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphiccustomrate_group_base_json_get()


@router.get(
    "/generated/polymorphiccustomrate.json",
    responses={
        200: {"model": PolymorphicCustomRate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicCustomRate",
    response_model_by_alias=True,
)
async def generated_polymorphiccustomrate_json_get(
) -> PolymorphicCustomRate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphiccustomrate_json_get()


@router.get(
    "/generated/polymorphiccustomrate_user_base.json",
    responses={
        200: {"model": PolymorphicCustomRateUserBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicCustomRate_User_base",
    response_model_by_alias=True,
)
async def generated_polymorphiccustomrate_user_base_json_get(
) -> PolymorphicCustomRateUserBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphiccustomrate_user_base_json_get()


@router.get(
    "/generated/polymorphicobject_base.json",
    responses={
        200: {"model": PolymorphicObjectBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PolymorphicObject_base",
    response_model_by_alias=True,
)
async def generated_polymorphicobject_base_json_get(
) -> PolymorphicObjectBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_polymorphicobject_base_json_get()


@router.get(
    "/generated/practicearea_base.json",
    responses={
        200: {"model": PracticeAreaBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PracticeArea_base",
    response_model_by_alias=True,
)
async def generated_practicearea_base_json_get(
) -> PracticeAreaBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_practicearea_base_json_get()


@router.get(
    "/generated/practicearea.json",
    responses={
        200: {"model": PracticeArea, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for PracticeArea",
    response_model_by_alias=True,
)
async def generated_practicearea_json_get(
) -> PracticeArea:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_practicearea_json_get()


@router.get(
    "/generated/relatedcontacts_base.json",
    responses={
        200: {"model": RelatedContactsBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for RelatedContacts_base",
    response_model_by_alias=True,
)
async def generated_relatedcontacts_base_json_get(
) -> RelatedContactsBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_relatedcontacts_base_json_get()


@router.get(
    "/generated/relatedcontacts.json",
    responses={
        200: {"model": RelatedContacts, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for RelatedContacts",
    response_model_by_alias=True,
)
async def generated_relatedcontacts_json_get(
) -> RelatedContacts:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_relatedcontacts_json_get()


@router.get(
    "/generated/relationship_base.json",
    responses={
        200: {"model": RelationshipBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Relationship_base",
    response_model_by_alias=True,
)
async def generated_relationship_base_json_get(
) -> RelationshipBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_relationship_base_json_get()


@router.get(
    "/generated/relationship.json",
    responses={
        200: {"model": Relationship, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Relationship",
    response_model_by_alias=True,
)
async def generated_relationship_json_get(
) -> Relationship:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_relationship_json_get()


@router.get(
    "/generated/reminder_base.json",
    responses={
        200: {"model": ReminderBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Reminder_base",
    response_model_by_alias=True,
)
async def generated_reminder_base_json_get(
) -> ReminderBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reminder_base_json_get()


@router.get(
    "/generated/reminder.json",
    responses={
        200: {"model": Reminder, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Reminder",
    response_model_by_alias=True,
)
async def generated_reminder_json_get(
) -> Reminder:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reminder_json_get()


@router.get(
    "/generated/remindertemplate_base.json",
    responses={
        200: {"model": ReminderTemplateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ReminderTemplate_base",
    response_model_by_alias=True,
)
async def generated_remindertemplate_base_json_get(
) -> ReminderTemplateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_remindertemplate_base_json_get()


@router.get(
    "/generated/report_base.json",
    responses={
        200: {"model": ReportBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Report_base",
    response_model_by_alias=True,
)
async def generated_report_base_json_get(
) -> ReportBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_report_base_json_get()


@router.get(
    "/generated/report.json",
    responses={
        200: {"model": Report, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Report",
    response_model_by_alias=True,
)
async def generated_report_json_get(
) -> Report:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_report_json_get()


@router.get(
    "/generated/reportpreset_base.json",
    responses={
        200: {"model": ReportPresetBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ReportPreset_base",
    response_model_by_alias=True,
)
async def generated_reportpreset_base_json_get(
) -> ReportPresetBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reportpreset_base_json_get()


@router.get(
    "/generated/reportpreset.json",
    responses={
        200: {"model": ReportPreset, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ReportPreset",
    response_model_by_alias=True,
)
async def generated_reportpreset_json_get(
) -> ReportPreset:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reportpreset_json_get()


@router.get(
    "/generated/reportschedule_base.json",
    responses={
        200: {"model": ReportScheduleBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ReportSchedule_base",
    response_model_by_alias=True,
)
async def generated_reportschedule_base_json_get(
) -> ReportScheduleBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reportschedule_base_json_get()


@router.get(
    "/generated/reportschedule.json",
    responses={
        200: {"model": ReportSchedule, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ReportSchedule",
    response_model_by_alias=True,
)
async def generated_reportschedule_json_get(
) -> ReportSchedule:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_reportschedule_json_get()


@router.get(
    "/generated/servicetype_base.json",
    responses={
        200: {"model": ServiceTypeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ServiceType_base",
    response_model_by_alias=True,
)
async def generated_servicetype_base_json_get(
) -> ServiceTypeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_servicetype_base_json_get()


@router.get(
    "/generated/servicetype.json",
    responses={
        200: {"model": ServiceType, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for ServiceType",
    response_model_by_alias=True,
)
async def generated_servicetype_json_get(
) -> ServiceType:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_servicetype_json_get()


@router.get(
    "/generated/splitinvoice_base.json",
    responses={
        200: {"model": SplitInvoiceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for SplitInvoice_base",
    response_model_by_alias=True,
)
async def generated_splitinvoice_base_json_get(
) -> SplitInvoiceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_splitinvoice_base_json_get()


@router.get(
    "/generated/splitinvoicepayer_base.json",
    responses={
        200: {"model": SplitInvoicePayerBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for SplitInvoicePayer_base",
    response_model_by_alias=True,
)
async def generated_splitinvoicepayer_base_json_get(
) -> SplitInvoicePayerBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_splitinvoicepayer_base_json_get()


@router.get(
    "/generated/task_base.json",
    responses={
        200: {"model": TaskBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Task_base",
    response_model_by_alias=True,
)
async def generated_task_base_json_get(
) -> TaskBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_task_base_json_get()


@router.get(
    "/generated/task.json",
    responses={
        200: {"model": Task, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Task",
    response_model_by_alias=True,
)
async def generated_task_json_get(
) -> Task:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_task_json_get()


@router.get(
    "/generated/tasktemplate_base.json",
    responses={
        200: {"model": TaskTemplateBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskTemplate_base",
    response_model_by_alias=True,
)
async def generated_tasktemplate_base_json_get(
) -> TaskTemplateBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktemplate_base_json_get()


@router.get(
    "/generated/tasktemplate.json",
    responses={
        200: {"model": TaskTemplate, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskTemplate",
    response_model_by_alias=True,
)
async def generated_tasktemplate_json_get(
) -> TaskTemplate:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktemplate_json_get()


@router.get(
    "/generated/tasktemplatelist_base.json",
    responses={
        200: {"model": TaskTemplateListBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskTemplateList_base",
    response_model_by_alias=True,
)
async def generated_tasktemplatelist_base_json_get(
) -> TaskTemplateListBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktemplatelist_base_json_get()


@router.get(
    "/generated/tasktemplatelist.json",
    responses={
        200: {"model": TaskTemplateList, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskTemplateList",
    response_model_by_alias=True,
)
async def generated_tasktemplatelist_json_get(
) -> TaskTemplateList:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktemplatelist_json_get()


@router.get(
    "/generated/tasktemplatelistinstace_base.json",
    responses={
        200: {"model": TaskTemplateListInstaceBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskTemplateListInstace_base",
    response_model_by_alias=True,
)
async def generated_tasktemplatelistinstace_base_json_get(
) -> TaskTemplateListInstaceBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktemplatelistinstace_base_json_get()


@router.get(
    "/generated/tasktype_base.json",
    responses={
        200: {"model": TaskTypeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskType_base",
    response_model_by_alias=True,
)
async def generated_tasktype_base_json_get(
) -> TaskTypeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktype_base_json_get()


@router.get(
    "/generated/tasktype.json",
    responses={
        200: {"model": TaskType, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TaskType",
    response_model_by_alias=True,
)
async def generated_tasktype_json_get(
) -> TaskType:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_tasktype_json_get()


@router.get(
    "/generated/textsnippet_base.json",
    responses={
        200: {"model": TextSnippetBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TextSnippet_base",
    response_model_by_alias=True,
)
async def generated_textsnippet_base_json_get(
) -> TextSnippetBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_textsnippet_base_json_get()


@router.get(
    "/generated/textsnippet.json",
    responses={
        200: {"model": TextSnippet, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TextSnippet",
    response_model_by_alias=True,
)
async def generated_textsnippet_json_get(
) -> TextSnippet:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_textsnippet_json_get()


@router.get(
    "/generated/timer_base.json",
    responses={
        200: {"model": TimerBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Timer_base",
    response_model_by_alias=True,
)
async def generated_timer_base_json_get(
) -> TimerBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_timer_base_json_get()


@router.get(
    "/generated/timer.json",
    responses={
        200: {"model": Timer, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Timer",
    response_model_by_alias=True,
)
async def generated_timer_json_get(
) -> Timer:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_timer_json_get()


@router.get(
    "/generated/trustlineitem_base.json",
    responses={
        200: {"model": TrustLineItemBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TrustLineItem_base",
    response_model_by_alias=True,
)
async def generated_trustlineitem_base_json_get(
) -> TrustLineItemBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_trustlineitem_base_json_get()


@router.get(
    "/generated/trustlineitem.json",
    responses={
        200: {"model": TrustLineItem, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TrustLineItem",
    response_model_by_alias=True,
)
async def generated_trustlineitem_json_get(
) -> TrustLineItem:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_trustlineitem_json_get()


@router.get(
    "/generated/trustrequest_base.json",
    responses={
        200: {"model": TrustRequestBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TrustRequest_base",
    response_model_by_alias=True,
)
async def generated_trustrequest_base_json_get(
) -> TrustRequestBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_trustrequest_base_json_get()


@router.get(
    "/generated/trustrequest.json",
    responses={
        200: {"model": TrustRequest, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for TrustRequest",
    response_model_by_alias=True,
)
async def generated_trustrequest_json_get(
) -> TrustRequest:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_trustrequest_json_get()


@router.get(
    "/generated/unredactedparticipant_base.json",
    responses={
        200: {"model": object, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for UnredactedParticipant_base",
    response_model_by_alias=True,
)
async def generated_unredactedparticipant_base_json_get(
) -> object:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_unredactedparticipant_base_json_get()


@router.get(
    "/generated/user_base.json",
    responses={
        200: {"model": UserBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for User_base",
    response_model_by_alias=True,
)
async def generated_user_base_json_get(
) -> UserBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_user_base_json_get()


@router.get(
    "/generated/user.json",
    responses={
        200: {"model": User, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for User",
    response_model_by_alias=True,
)
async def generated_user_json_get(
) -> User:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_user_json_get()


@router.get(
    "/generated/utbmscode_base.json",
    responses={
        200: {"model": UtbmsCodeBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for UtbmsCode_base",
    response_model_by_alias=True,
)
async def generated_utbmscode_base_json_get(
) -> UtbmsCodeBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_utbmscode_base_json_get()


@router.get(
    "/generated/utbmscode.json",
    responses={
        200: {"model": UtbmsCode, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for UtbmsCode",
    response_model_by_alias=True,
)
async def generated_utbmscode_json_get(
) -> UtbmsCode:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_utbmscode_json_get()


@router.get(
    "/generated/utbmsset_base.json",
    responses={
        200: {"model": UtbmsSetBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for UtbmsSet_base",
    response_model_by_alias=True,
)
async def generated_utbmsset_base_json_get(
) -> UtbmsSetBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_utbmsset_base_json_get()


@router.get(
    "/generated/utbmsset.json",
    responses={
        200: {"model": UtbmsSet, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for UtbmsSet",
    response_model_by_alias=True,
)
async def generated_utbmsset_json_get(
) -> UtbmsSet:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_utbmsset_json_get()


@router.get(
    "/generated/webhook_base.json",
    responses={
        200: {"model": WebhookBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Webhook_base",
    response_model_by_alias=True,
)
async def generated_webhook_base_json_get(
) -> WebhookBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_webhook_base_json_get()


@router.get(
    "/generated/webhook.json",
    responses={
        200: {"model": Webhook, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for Webhook",
    response_model_by_alias=True,
)
async def generated_webhook_json_get(
) -> Webhook:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_webhook_json_get()


@router.get(
    "/generated/website_base.json",
    responses={
        200: {"model": WebSiteBase, "description": "OK"},
    },
    tags=["default"],
    summary="Generated endpoint for WebSite_base",
    response_model_by_alias=True,
)
async def generated_website_base_json_get(
) -> WebSiteBase:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().generated_website_base_json_get()
