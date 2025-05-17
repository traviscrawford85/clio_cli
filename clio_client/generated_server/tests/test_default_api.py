# coding: utf-8

from fastapi.testclient import TestClient


from typing import Any, Dict  # noqa: F401
from openapi_server.models.account import Account  # noqa: F401
from openapi_server.models.account_balance_base import AccountBalanceBase  # noqa: F401
from openapi_server.models.account_base import AccountBase  # noqa: F401
from openapi_server.models.activity import Activity  # noqa: F401
from openapi_server.models.activity_base import ActivityBase  # noqa: F401
from openapi_server.models.activity_calendar_entry_base import ActivityCalendarEntryBase  # noqa: F401
from openapi_server.models.activity_description import ActivityDescription  # noqa: F401
from openapi_server.models.activity_description_base import ActivityDescriptionBase  # noqa: F401
from openapi_server.models.activity_description_rate_base import ActivityDescriptionRateBase  # noqa: F401
from openapi_server.models.activity_rate import ActivityRate  # noqa: F401
from openapi_server.models.activity_rate_base import ActivityRateBase  # noqa: F401
from openapi_server.models.activity_task_base import ActivityTaskBase  # noqa: F401
from openapi_server.models.activity_text_message_conversation_base import ActivityTextMessageConversationBase  # noqa: F401
from openapi_server.models.address import Address  # noqa: F401
from openapi_server.models.address_base import AddressBase  # noqa: F401
from openapi_server.models.allocation import Allocation  # noqa: F401
from openapi_server.models.allocation_base import AllocationBase  # noqa: F401
from openapi_server.models.attendee_base import AttendeeBase  # noqa: F401
from openapi_server.models.avatar_base import AvatarBase  # noqa: F401
from openapi_server.models.balance import Balance  # noqa: F401
from openapi_server.models.balance_base import BalanceBase  # noqa: F401
from openapi_server.models.bank_account import BankAccount  # noqa: F401
from openapi_server.models.bank_account_base import BankAccountBase  # noqa: F401
from openapi_server.models.bank_transaction import BankTransaction  # noqa: F401
from openapi_server.models.bank_transaction_base import BankTransactionBase  # noqa: F401
from openapi_server.models.bank_transfer import BankTransfer  # noqa: F401
from openapi_server.models.bank_transfer_base import BankTransferBase  # noqa: F401
from openapi_server.models.bill import Bill  # noqa: F401
from openapi_server.models.bill_base import BillBase  # noqa: F401
from openapi_server.models.bill_recipient import BillRecipient  # noqa: F401
from openapi_server.models.bill_recipient_base import BillRecipientBase  # noqa: F401
from openapi_server.models.bill_recipient_contact_base import BillRecipientContactBase  # noqa: F401
from openapi_server.models.bill_theme import BillTheme  # noqa: F401
from openapi_server.models.bill_theme_base import BillThemeBase  # noqa: F401
from openapi_server.models.billable_client import BillableClient  # noqa: F401
from openapi_server.models.billable_client_base import BillableClientBase  # noqa: F401
from openapi_server.models.billable_matter import BillableMatter  # noqa: F401
from openapi_server.models.billable_matter_base import BillableMatterBase  # noqa: F401
from openapi_server.models.billing_setting import BillingSetting  # noqa: F401
from openapi_server.models.billing_setting_base import BillingSettingBase  # noqa: F401
from openapi_server.models.calendar import Calendar  # noqa: F401
from openapi_server.models.calendar_base import CalendarBase  # noqa: F401
from openapi_server.models.calendar_entry import CalendarEntry  # noqa: F401
from openapi_server.models.calendar_entry_base import CalendarEntryBase  # noqa: F401
from openapi_server.models.calendar_entry_event_type_base import CalendarEntryEventTypeBase  # noqa: F401
from openapi_server.models.calendar_visibility import CalendarVisibility  # noqa: F401
from openapi_server.models.calendar_visibility_base import CalendarVisibilityBase  # noqa: F401
from openapi_server.models.cascading_task_template_base import CascadingTaskTemplateBase  # noqa: F401
from openapi_server.models.client import Client  # noqa: F401
from openapi_server.models.client_base import ClientBase  # noqa: F401
from openapi_server.models.client_portal_base import ClientPortalBase  # noqa: F401
from openapi_server.models.clio_creator_base import ClioCreatorBase  # noqa: F401
from openapi_server.models.clio_payments_link import ClioPaymentsLink  # noqa: F401
from openapi_server.models.clio_payments_link_base import ClioPaymentsLinkBase  # noqa: F401
from openapi_server.models.clio_payments_payment import ClioPaymentsPayment  # noqa: F401
from openapi_server.models.clio_payments_payment_base import ClioPaymentsPaymentBase  # noqa: F401
from openapi_server.models.comment import Comment  # noqa: F401
from openapi_server.models.comment_base import CommentBase  # noqa: F401
from openapi_server.models.communication import Communication  # noqa: F401
from openapi_server.models.communication_base import CommunicationBase  # noqa: F401
from openapi_server.models.communication_eml_file_base import CommunicationEmlFileBase  # noqa: F401
from openapi_server.models.conference_meeting_base import ConferenceMeetingBase  # noqa: F401
from openapi_server.models.contact import Contact  # noqa: F401
from openapi_server.models.contact_base import ContactBase  # noqa: F401
from openapi_server.models.contingency_fee_base import ContingencyFeeBase  # noqa: F401
from openapi_server.models.conversation import Conversation  # noqa: F401
from openapi_server.models.conversation_base import ConversationBase  # noqa: F401
from openapi_server.models.conversation_membership import ConversationMembership  # noqa: F401
from openapi_server.models.conversation_membership_base import ConversationMembershipBase  # noqa: F401
from openapi_server.models.conversation_message import ConversationMessage  # noqa: F401
from openapi_server.models.conversation_message_base import ConversationMessageBase  # noqa: F401
from openapi_server.models.credit_memo import CreditMemo  # noqa: F401
from openapi_server.models.credit_memo_base import CreditMemoBase  # noqa: F401
from openapi_server.models.currency import Currency  # noqa: F401
from openapi_server.models.currency_base import CurrencyBase  # noqa: F401
from openapi_server.models.custom_action import CustomAction  # noqa: F401
from openapi_server.models.custom_action_base import CustomActionBase  # noqa: F401
from openapi_server.models.custom_field import CustomField  # noqa: F401
from openapi_server.models.custom_field_base import CustomFieldBase  # noqa: F401
from openapi_server.models.custom_field_matter_selection import CustomFieldMatterSelection  # noqa: F401
from openapi_server.models.custom_field_matter_selection_base import CustomFieldMatterSelectionBase  # noqa: F401
from openapi_server.models.custom_field_set import CustomFieldSet  # noqa: F401
from openapi_server.models.custom_field_set_association_base import CustomFieldSetAssociationBase  # noqa: F401
from openapi_server.models.custom_field_set_base import CustomFieldSetBase  # noqa: F401
from openapi_server.models.custom_field_value import CustomFieldValue  # noqa: F401
from openapi_server.models.custom_field_value_base import CustomFieldValueBase  # noqa: F401
from openapi_server.models.damage import Damage  # noqa: F401
from openapi_server.models.damage_base import DamageBase  # noqa: F401
from openapi_server.models.discount_base import DiscountBase  # noqa: F401
from openapi_server.models.document import Document  # noqa: F401
from openapi_server.models.document_archive import DocumentArchive  # noqa: F401
from openapi_server.models.document_archive_base import DocumentArchiveBase  # noqa: F401
from openapi_server.models.document_automation import DocumentAutomation  # noqa: F401
from openapi_server.models.document_automation_base import DocumentAutomationBase  # noqa: F401
from openapi_server.models.document_base import DocumentBase  # noqa: F401
from openapi_server.models.document_category import DocumentCategory  # noqa: F401
from openapi_server.models.document_category_base import DocumentCategoryBase  # noqa: F401
from openapi_server.models.document_template import DocumentTemplate  # noqa: F401
from openapi_server.models.document_template_base import DocumentTemplateBase  # noqa: F401
from openapi_server.models.document_version import DocumentVersion  # noqa: F401
from openapi_server.models.document_version_base import DocumentVersionBase  # noqa: F401
from openapi_server.models.email_address import EmailAddress  # noqa: F401
from openapi_server.models.email_address_base import EmailAddressBase  # noqa: F401
from openapi_server.models.error_detail import ErrorDetail  # noqa: F401
from openapi_server.models.event import Event  # noqa: F401
from openapi_server.models.event_base import EventBase  # noqa: F401
from openapi_server.models.event_metrics import EventMetrics  # noqa: F401
from openapi_server.models.event_metrics_base import EventMetricsBase  # noqa: F401
from openapi_server.models.evergreen_retainer_base import EvergreenRetainerBase  # noqa: F401
from openapi_server.models.expense_category import ExpenseCategory  # noqa: F401
from openapi_server.models.expense_category_base import ExpenseCategoryBase  # noqa: F401
from openapi_server.models.external_property_base import ExternalPropertyBase  # noqa: F401
from openapi_server.models.folder import Folder  # noqa: F401
from openapi_server.models.folder_base import FolderBase  # noqa: F401
from openapi_server.models.grant import Grant  # noqa: F401
from openapi_server.models.grant_base import GrantBase  # noqa: F401
from openapi_server.models.grant_funding_source import GrantFundingSource  # noqa: F401
from openapi_server.models.grant_funding_source_base import GrantFundingSourceBase  # noqa: F401
from openapi_server.models.group import Group  # noqa: F401
from openapi_server.models.group_base import GroupBase  # noqa: F401
from openapi_server.models.ids_response import IdsResponse  # noqa: F401
from openapi_server.models.instant_messenger_base import InstantMessengerBase  # noqa: F401
from openapi_server.models.interest import Interest  # noqa: F401
from openapi_server.models.interest_base import InterestBase  # noqa: F401
from openapi_server.models.interest_charge import InterestCharge  # noqa: F401
from openapi_server.models.interest_charge_base import InterestChargeBase  # noqa: F401
from openapi_server.models.item import Item  # noqa: F401
from openapi_server.models.item_base import ItemBase  # noqa: F401
from openapi_server.models.job_title_base import JobTitleBase  # noqa: F401
from openapi_server.models.jurisdiction import Jurisdiction  # noqa: F401
from openapi_server.models.jurisdiction_base import JurisdictionBase  # noqa: F401
from openapi_server.models.jurisdictions_to_trigger import JurisdictionsToTrigger  # noqa: F401
from openapi_server.models.jurisdictions_to_trigger_base import JurisdictionsToTriggerBase  # noqa: F401
from openapi_server.models.lauk_civil_certificated_rate import LaukCivilCertificatedRate  # noqa: F401
from openapi_server.models.lauk_civil_certificated_rate_base import LaukCivilCertificatedRateBase  # noqa: F401
from openapi_server.models.lauk_civil_controlled_rate import LaukCivilControlledRate  # noqa: F401
from openapi_server.models.lauk_civil_controlled_rate_base import LaukCivilControlledRateBase  # noqa: F401
from openapi_server.models.lauk_criminal_controlled_rate import LaukCriminalControlledRate  # noqa: F401
from openapi_server.models.lauk_criminal_controlled_rate_base import LaukCriminalControlledRateBase  # noqa: F401
from openapi_server.models.lauk_expense_category import LaukExpenseCategory  # noqa: F401
from openapi_server.models.lauk_expense_category_base import LaukExpenseCategoryBase  # noqa: F401
from openapi_server.models.legal_aid_uk_activity_base import LegalAidUkActivityBase  # noqa: F401
from openapi_server.models.legal_aid_uk_bill_base import LegalAidUkBillBase  # noqa: F401
from openapi_server.models.legal_aid_uk_contact_base import LegalAidUkContactBase  # noqa: F401
from openapi_server.models.legal_aid_uk_matter_base import LegalAidUkMatterBase  # noqa: F401
from openapi_server.models.lien_base import LienBase  # noqa: F401
from openapi_server.models.line_item import LineItem  # noqa: F401
from openapi_server.models.line_item_base import LineItemBase  # noqa: F401
from openapi_server.models.line_item_totals_base import LineItemTotalsBase  # noqa: F401
from openapi_server.models.linked_folder_base import LinkedFolderBase  # noqa: F401
from openapi_server.models.log_entry import LogEntry  # noqa: F401
from openapi_server.models.log_entry_base import LogEntryBase  # noqa: F401
from openapi_server.models.matter import Matter  # noqa: F401
from openapi_server.models.matter_balance_base import MatterBalanceBase  # noqa: F401
from openapi_server.models.matter_base import MatterBase  # noqa: F401
from openapi_server.models.matter_bill_recipient import MatterBillRecipient  # noqa: F401
from openapi_server.models.matter_bill_recipient_base import MatterBillRecipientBase  # noqa: F401
from openapi_server.models.matter_budget_base import MatterBudgetBase  # noqa: F401
from openapi_server.models.matter_contacts import MatterContacts  # noqa: F401
from openapi_server.models.matter_contacts_base import MatterContactsBase  # noqa: F401
from openapi_server.models.matter_custom_rate import MatterCustomRate  # noqa: F401
from openapi_server.models.matter_custom_rate_base import MatterCustomRateBase  # noqa: F401
from openapi_server.models.matter_docket import MatterDocket  # noqa: F401
from openapi_server.models.matter_docket_base import MatterDocketBase  # noqa: F401
from openapi_server.models.matter_stage import MatterStage  # noqa: F401
from openapi_server.models.matter_stage_base import MatterStageBase  # noqa: F401
from openapi_server.models.medical_bill import MedicalBill  # noqa: F401
from openapi_server.models.medical_bill_base import MedicalBillBase  # noqa: F401
from openapi_server.models.medical_record import MedicalRecord  # noqa: F401
from openapi_server.models.medical_record_base import MedicalRecordBase  # noqa: F401
from openapi_server.models.medical_records_request import MedicalRecordsRequest  # noqa: F401
from openapi_server.models.medical_records_request_base import MedicalRecordsRequestBase  # noqa: F401
from openapi_server.models.multipart import Multipart  # noqa: F401
from openapi_server.models.multipart_base import MultipartBase  # noqa: F401
from openapi_server.models.multipart_header_base import MultipartHeaderBase  # noqa: F401
from openapi_server.models.my_event import MyEvent  # noqa: F401
from openapi_server.models.note import Note  # noqa: F401
from openapi_server.models.note_base import NoteBase  # noqa: F401
from openapi_server.models.notification_event_subscriber_base import NotificationEventSubscriberBase  # noqa: F401
from openapi_server.models.notification_method_base import NotificationMethodBase  # noqa: F401
from openapi_server.models.outstanding_client_balance import OutstandingClientBalance  # noqa: F401
from openapi_server.models.outstanding_client_balance_base import OutstandingClientBalanceBase  # noqa: F401
from openapi_server.models.participant import Participant  # noqa: F401
from openapi_server.models.participant_base import ParticipantBase  # noqa: F401
from openapi_server.models.payment import Payment  # noqa: F401
from openapi_server.models.payment_base import PaymentBase  # noqa: F401
from openapi_server.models.payment_profile_base import PaymentProfileBase  # noqa: F401
from openapi_server.models.phone_number import PhoneNumber  # noqa: F401
from openapi_server.models.phone_number_base import PhoneNumberBase  # noqa: F401
from openapi_server.models.picklist_option import PicklistOption  # noqa: F401
from openapi_server.models.picklist_option_base import PicklistOptionBase  # noqa: F401
from openapi_server.models.polymorphic_custom_rate import PolymorphicCustomRate  # noqa: F401
from openapi_server.models.polymorphic_custom_rate_activity_description_base import PolymorphicCustomRateActivityDescriptionBase  # noqa: F401
from openapi_server.models.polymorphic_custom_rate_base import PolymorphicCustomRateBase  # noqa: F401
from openapi_server.models.polymorphic_custom_rate_group_base import PolymorphicCustomRateGroupBase  # noqa: F401
from openapi_server.models.polymorphic_custom_rate_user_base import PolymorphicCustomRateUserBase  # noqa: F401
from openapi_server.models.polymorphic_object_base import PolymorphicObjectBase  # noqa: F401
from openapi_server.models.practice_area import PracticeArea  # noqa: F401
from openapi_server.models.practice_area_base import PracticeAreaBase  # noqa: F401
from openapi_server.models.related_contacts import RelatedContacts  # noqa: F401
from openapi_server.models.related_contacts_base import RelatedContactsBase  # noqa: F401
from openapi_server.models.relationship import Relationship  # noqa: F401
from openapi_server.models.relationship_base import RelationshipBase  # noqa: F401
from openapi_server.models.reminder import Reminder  # noqa: F401
from openapi_server.models.reminder_base import ReminderBase  # noqa: F401
from openapi_server.models.reminder_template_base import ReminderTemplateBase  # noqa: F401
from openapi_server.models.report import Report  # noqa: F401
from openapi_server.models.report_base import ReportBase  # noqa: F401
from openapi_server.models.report_preset import ReportPreset  # noqa: F401
from openapi_server.models.report_preset_base import ReportPresetBase  # noqa: F401
from openapi_server.models.report_schedule import ReportSchedule  # noqa: F401
from openapi_server.models.report_schedule_base import ReportScheduleBase  # noqa: F401
from openapi_server.models.service_type import ServiceType  # noqa: F401
from openapi_server.models.service_type_base import ServiceTypeBase  # noqa: F401
from openapi_server.models.split_invoice_base import SplitInvoiceBase  # noqa: F401
from openapi_server.models.split_invoice_payer_base import SplitInvoicePayerBase  # noqa: F401
from openapi_server.models.task import Task  # noqa: F401
from openapi_server.models.task_base import TaskBase  # noqa: F401
from openapi_server.models.task_template import TaskTemplate  # noqa: F401
from openapi_server.models.task_template_base import TaskTemplateBase  # noqa: F401
from openapi_server.models.task_template_list import TaskTemplateList  # noqa: F401
from openapi_server.models.task_template_list_base import TaskTemplateListBase  # noqa: F401
from openapi_server.models.task_template_list_instace_base import TaskTemplateListInstaceBase  # noqa: F401
from openapi_server.models.task_type import TaskType  # noqa: F401
from openapi_server.models.task_type_base import TaskTypeBase  # noqa: F401
from openapi_server.models.text_snippet import TextSnippet  # noqa: F401
from openapi_server.models.text_snippet_base import TextSnippetBase  # noqa: F401
from openapi_server.models.timer import Timer  # noqa: F401
from openapi_server.models.timer_base import TimerBase  # noqa: F401
from openapi_server.models.trust_line_item import TrustLineItem  # noqa: F401
from openapi_server.models.trust_line_item_base import TrustLineItemBase  # noqa: F401
from openapi_server.models.trust_request import TrustRequest  # noqa: F401
from openapi_server.models.trust_request_base import TrustRequestBase  # noqa: F401
from openapi_server.models.user import User  # noqa: F401
from openapi_server.models.user_base import UserBase  # noqa: F401
from openapi_server.models.utbms_code import UtbmsCode  # noqa: F401
from openapi_server.models.utbms_code_base import UtbmsCodeBase  # noqa: F401
from openapi_server.models.utbms_set import UtbmsSet  # noqa: F401
from openapi_server.models.utbms_set_base import UtbmsSetBase  # noqa: F401
from openapi_server.models.web_site_base import WebSiteBase  # noqa: F401
from openapi_server.models.webhook import Webhook  # noqa: F401
from openapi_server.models.webhook_base import WebhookBase  # noqa: F401


def test_generated_account_base_json_get(client: TestClient):
    """Test case for generated_account_base_json_get

    Generated endpoint for Account_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/account_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_account_json_get(client: TestClient):
    """Test case for generated_account_json_get

    Generated endpoint for Account
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/account.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_accountbalance_base_json_get(client: TestClient):
    """Test case for generated_accountbalance_base_json_get

    Generated endpoint for AccountBalance_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/accountbalance_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activity_base_json_get(client: TestClient):
    """Test case for generated_activity_base_json_get

    Generated endpoint for Activity_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activity_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activity_calendarentry_base_json_get(client: TestClient):
    """Test case for generated_activity_calendarentry_base_json_get

    Generated endpoint for Activity_CalendarEntry_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activity_calendarentry_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activity_json_get(client: TestClient):
    """Test case for generated_activity_json_get

    Generated endpoint for Activity
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activity.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activity_task_base_json_get(client: TestClient):
    """Test case for generated_activity_task_base_json_get

    Generated endpoint for Activity_Task_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activity_task_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activity_textmessageconversation_base_json_get(client: TestClient):
    """Test case for generated_activity_textmessageconversation_base_json_get

    Generated endpoint for Activity_TextMessageConversation_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activity_textmessageconversation_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activitydescription_base_json_get(client: TestClient):
    """Test case for generated_activitydescription_base_json_get

    Generated endpoint for ActivityDescription_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activitydescription_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activitydescription_json_get(client: TestClient):
    """Test case for generated_activitydescription_json_get

    Generated endpoint for ActivityDescription
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activitydescription.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activitydescriptionrate_base_json_get(client: TestClient):
    """Test case for generated_activitydescriptionrate_base_json_get

    Generated endpoint for ActivityDescriptionRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activitydescriptionrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activityrate_base_json_get(client: TestClient):
    """Test case for generated_activityrate_base_json_get

    Generated endpoint for ActivityRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activityrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_activityrate_json_get(client: TestClient):
    """Test case for generated_activityrate_json_get

    Generated endpoint for ActivityRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/activityrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_address_base_json_get(client: TestClient):
    """Test case for generated_address_base_json_get

    Generated endpoint for Address_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/address_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_address_json_get(client: TestClient):
    """Test case for generated_address_json_get

    Generated endpoint for Address
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/address.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_allocation_base_json_get(client: TestClient):
    """Test case for generated_allocation_base_json_get

    Generated endpoint for Allocation_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/allocation_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_allocation_json_get(client: TestClient):
    """Test case for generated_allocation_json_get

    Generated endpoint for Allocation
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/allocation.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_attendee_base_json_get(client: TestClient):
    """Test case for generated_attendee_base_json_get

    Generated endpoint for Attendee_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/attendee_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_avatar_base_json_get(client: TestClient):
    """Test case for generated_avatar_base_json_get

    Generated endpoint for Avatar_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/avatar_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_balance_base_json_get(client: TestClient):
    """Test case for generated_balance_base_json_get

    Generated endpoint for Balance_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/balance_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_balance_json_get(client: TestClient):
    """Test case for generated_balance_json_get

    Generated endpoint for Balance
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/balance.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_bankaccount_base_json_get(client: TestClient):
    """Test case for generated_bankaccount_base_json_get

    Generated endpoint for BankAccount_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/bankaccount_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_bankaccount_json_get(client: TestClient):
    """Test case for generated_bankaccount_json_get

    Generated endpoint for BankAccount
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/bankaccount.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_banktransaction_base_json_get(client: TestClient):
    """Test case for generated_banktransaction_base_json_get

    Generated endpoint for BankTransaction_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/banktransaction_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_banktransaction_json_get(client: TestClient):
    """Test case for generated_banktransaction_json_get

    Generated endpoint for BankTransaction
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/banktransaction.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_banktransfer_base_json_get(client: TestClient):
    """Test case for generated_banktransfer_base_json_get

    Generated endpoint for BankTransfer_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/banktransfer_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_banktransfer_json_get(client: TestClient):
    """Test case for generated_banktransfer_json_get

    Generated endpoint for BankTransfer
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/banktransfer.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_bill_base_json_get(client: TestClient):
    """Test case for generated_bill_base_json_get

    Generated endpoint for Bill_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/bill_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_bill_json_get(client: TestClient):
    """Test case for generated_bill_json_get

    Generated endpoint for Bill
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/bill.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billableclient_base_json_get(client: TestClient):
    """Test case for generated_billableclient_base_json_get

    Generated endpoint for BillableClient_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billableclient_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billableclient_json_get(client: TestClient):
    """Test case for generated_billableclient_json_get

    Generated endpoint for BillableClient
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billableclient.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billablematter_base_json_get(client: TestClient):
    """Test case for generated_billablematter_base_json_get

    Generated endpoint for BillableMatter_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billablematter_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billablematter_json_get(client: TestClient):
    """Test case for generated_billablematter_json_get

    Generated endpoint for BillableMatter
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billablematter.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billingsetting_base_json_get(client: TestClient):
    """Test case for generated_billingsetting_base_json_get

    Generated endpoint for BillingSetting_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billingsetting_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billingsetting_json_get(client: TestClient):
    """Test case for generated_billingsetting_json_get

    Generated endpoint for BillingSetting
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billingsetting.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billrecipient_base_json_get(client: TestClient):
    """Test case for generated_billrecipient_base_json_get

    Generated endpoint for BillRecipient_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billrecipient_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billrecipient_contact_base_json_get(client: TestClient):
    """Test case for generated_billrecipient_contact_base_json_get

    Generated endpoint for BillRecipient_Contact_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billrecipient_contact_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billrecipient_json_get(client: TestClient):
    """Test case for generated_billrecipient_json_get

    Generated endpoint for BillRecipient
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billrecipient.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billtheme_base_json_get(client: TestClient):
    """Test case for generated_billtheme_base_json_get

    Generated endpoint for BillTheme_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billtheme_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_billtheme_json_get(client: TestClient):
    """Test case for generated_billtheme_json_get

    Generated endpoint for BillTheme
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/billtheme.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendar_base_json_get(client: TestClient):
    """Test case for generated_calendar_base_json_get

    Generated endpoint for Calendar_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendar_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendar_json_get(client: TestClient):
    """Test case for generated_calendar_json_get

    Generated endpoint for Calendar
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendar.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendarentry_base_json_get(client: TestClient):
    """Test case for generated_calendarentry_base_json_get

    Generated endpoint for CalendarEntry_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendarentry_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendarentry_json_get(client: TestClient):
    """Test case for generated_calendarentry_json_get

    Generated endpoint for CalendarEntry
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendarentry.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendarentryeventtype_base_json_get(client: TestClient):
    """Test case for generated_calendarentryeventtype_base_json_get

    Generated endpoint for CalendarEntryEventType_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendarentryeventtype_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendarvisibility_base_json_get(client: TestClient):
    """Test case for generated_calendarvisibility_base_json_get

    Generated endpoint for CalendarVisibility_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendarvisibility_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_calendarvisibility_json_get(client: TestClient):
    """Test case for generated_calendarvisibility_json_get

    Generated endpoint for CalendarVisibility
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/calendarvisibility.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cascadingtask_base_json_get(client: TestClient):
    """Test case for generated_cascadingtask_base_json_get

    Generated endpoint for CascadingTask_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cascadingtask_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cascadingtasktemplate_base_json_get(client: TestClient):
    """Test case for generated_cascadingtasktemplate_base_json_get

    Generated endpoint for CascadingTaskTemplate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cascadingtasktemplate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_client_base_json_get(client: TestClient):
    """Test case for generated_client_base_json_get

    Generated endpoint for Client_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/client_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_client_json_get(client: TestClient):
    """Test case for generated_client_json_get

    Generated endpoint for Client
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/client.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_clientportal_base_json_get(client: TestClient):
    """Test case for generated_clientportal_base_json_get

    Generated endpoint for ClientPortal_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/clientportal_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cliocreator_base_json_get(client: TestClient):
    """Test case for generated_cliocreator_base_json_get

    Generated endpoint for ClioCreator_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cliocreator_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cliopaymentslink_base_json_get(client: TestClient):
    """Test case for generated_cliopaymentslink_base_json_get

    Generated endpoint for ClioPaymentsLink_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cliopaymentslink_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cliopaymentslink_json_get(client: TestClient):
    """Test case for generated_cliopaymentslink_json_get

    Generated endpoint for ClioPaymentsLink
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cliopaymentslink.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cliopaymentspayment_base_json_get(client: TestClient):
    """Test case for generated_cliopaymentspayment_base_json_get

    Generated endpoint for ClioPaymentsPayment_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cliopaymentspayment_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_cliopaymentspayment_json_get(client: TestClient):
    """Test case for generated_cliopaymentspayment_json_get

    Generated endpoint for ClioPaymentsPayment
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/cliopaymentspayment.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_comment_base_json_get(client: TestClient):
    """Test case for generated_comment_base_json_get

    Generated endpoint for Comment_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/comment_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_comment_json_get(client: TestClient):
    """Test case for generated_comment_json_get

    Generated endpoint for Comment
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/comment.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_communication_base_json_get(client: TestClient):
    """Test case for generated_communication_base_json_get

    Generated endpoint for Communication_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/communication_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_communication_json_get(client: TestClient):
    """Test case for generated_communication_json_get

    Generated endpoint for Communication
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/communication.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_communicationemlfile_base_json_get(client: TestClient):
    """Test case for generated_communicationemlfile_base_json_get

    Generated endpoint for CommunicationEmlFile_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/communicationemlfile_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conferencemeeting_base_json_get(client: TestClient):
    """Test case for generated_conferencemeeting_base_json_get

    Generated endpoint for ConferenceMeeting_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conferencemeeting_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_contact_base_json_get(client: TestClient):
    """Test case for generated_contact_base_json_get

    Generated endpoint for Contact_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/contact_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_contact_json_get(client: TestClient):
    """Test case for generated_contact_json_get

    Generated endpoint for Contact
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/contact.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_contingencyfee_base_json_get(client: TestClient):
    """Test case for generated_contingencyfee_base_json_get

    Generated endpoint for ContingencyFee_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/contingencyfee_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversation_base_json_get(client: TestClient):
    """Test case for generated_conversation_base_json_get

    Generated endpoint for Conversation_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversation_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversation_json_get(client: TestClient):
    """Test case for generated_conversation_json_get

    Generated endpoint for Conversation
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversation.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversationmembership_base_json_get(client: TestClient):
    """Test case for generated_conversationmembership_base_json_get

    Generated endpoint for ConversationMembership_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversationmembership_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversationmembership_json_get(client: TestClient):
    """Test case for generated_conversationmembership_json_get

    Generated endpoint for ConversationMembership
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversationmembership.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversationmessage_base_json_get(client: TestClient):
    """Test case for generated_conversationmessage_base_json_get

    Generated endpoint for ConversationMessage_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversationmessage_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_conversationmessage_json_get(client: TestClient):
    """Test case for generated_conversationmessage_json_get

    Generated endpoint for ConversationMessage
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/conversationmessage.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_creditmemo_base_json_get(client: TestClient):
    """Test case for generated_creditmemo_base_json_get

    Generated endpoint for CreditMemo_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/creditmemo_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_creditmemo_json_get(client: TestClient):
    """Test case for generated_creditmemo_json_get

    Generated endpoint for CreditMemo
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/creditmemo.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_currency_base_json_get(client: TestClient):
    """Test case for generated_currency_base_json_get

    Generated endpoint for Currency_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/currency_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_currency_json_get(client: TestClient):
    """Test case for generated_currency_json_get

    Generated endpoint for Currency
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/currency.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customaction_base_json_get(client: TestClient):
    """Test case for generated_customaction_base_json_get

    Generated endpoint for CustomAction_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customaction_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customaction_json_get(client: TestClient):
    """Test case for generated_customaction_json_get

    Generated endpoint for CustomAction
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customaction.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfield_base_json_get(client: TestClient):
    """Test case for generated_customfield_base_json_get

    Generated endpoint for CustomField_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfield_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfield_json_get(client: TestClient):
    """Test case for generated_customfield_json_get

    Generated endpoint for CustomField
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfield.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldmatterselection_base_json_get(client: TestClient):
    """Test case for generated_customfieldmatterselection_base_json_get

    Generated endpoint for CustomFieldMatterSelection_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldmatterselection_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldmatterselection_json_get(client: TestClient):
    """Test case for generated_customfieldmatterselection_json_get

    Generated endpoint for CustomFieldMatterSelection
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldmatterselection.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldset_base_json_get(client: TestClient):
    """Test case for generated_customfieldset_base_json_get

    Generated endpoint for CustomFieldSet_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldset_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldset_json_get(client: TestClient):
    """Test case for generated_customfieldset_json_get

    Generated endpoint for CustomFieldSet
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldset.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldsetassociation_base_json_get(client: TestClient):
    """Test case for generated_customfieldsetassociation_base_json_get

    Generated endpoint for CustomFieldSetAssociation_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldsetassociation_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldvalue_base_json_get(client: TestClient):
    """Test case for generated_customfieldvalue_base_json_get

    Generated endpoint for CustomFieldValue_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldvalue_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_customfieldvalue_json_get(client: TestClient):
    """Test case for generated_customfieldvalue_json_get

    Generated endpoint for CustomFieldValue
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/customfieldvalue.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_damage_base_json_get(client: TestClient):
    """Test case for generated_damage_base_json_get

    Generated endpoint for Damage_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/damage_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_damage_json_get(client: TestClient):
    """Test case for generated_damage_json_get

    Generated endpoint for Damage
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/damage.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_discount_base_json_get(client: TestClient):
    """Test case for generated_discount_base_json_get

    Generated endpoint for Discount_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/discount_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_document_base_json_get(client: TestClient):
    """Test case for generated_document_base_json_get

    Generated endpoint for Document_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/document_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_document_json_get(client: TestClient):
    """Test case for generated_document_json_get

    Generated endpoint for Document
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/document.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentarchive_base_json_get(client: TestClient):
    """Test case for generated_documentarchive_base_json_get

    Generated endpoint for DocumentArchive_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentarchive_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentarchive_json_get(client: TestClient):
    """Test case for generated_documentarchive_json_get

    Generated endpoint for DocumentArchive
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentarchive.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentautomation_base_json_get(client: TestClient):
    """Test case for generated_documentautomation_base_json_get

    Generated endpoint for DocumentAutomation_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentautomation_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentautomation_json_get(client: TestClient):
    """Test case for generated_documentautomation_json_get

    Generated endpoint for DocumentAutomation
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentautomation.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentcategory_base_json_get(client: TestClient):
    """Test case for generated_documentcategory_base_json_get

    Generated endpoint for DocumentCategory_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentcategory_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentcategory_json_get(client: TestClient):
    """Test case for generated_documentcategory_json_get

    Generated endpoint for DocumentCategory
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentcategory.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documenttemplate_base_json_get(client: TestClient):
    """Test case for generated_documenttemplate_base_json_get

    Generated endpoint for DocumentTemplate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documenttemplate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documenttemplate_json_get(client: TestClient):
    """Test case for generated_documenttemplate_json_get

    Generated endpoint for DocumentTemplate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documenttemplate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentversion_base_json_get(client: TestClient):
    """Test case for generated_documentversion_base_json_get

    Generated endpoint for DocumentVersion_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentversion_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_documentversion_json_get(client: TestClient):
    """Test case for generated_documentversion_json_get

    Generated endpoint for DocumentVersion
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/documentversion.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_emailaddress_base_json_get(client: TestClient):
    """Test case for generated_emailaddress_base_json_get

    Generated endpoint for EmailAddress_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/emailaddress_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_emailaddress_json_get(client: TestClient):
    """Test case for generated_emailaddress_json_get

    Generated endpoint for EmailAddress
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/emailaddress.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_errordetail_json_get(client: TestClient):
    """Test case for generated_errordetail_json_get

    Generated endpoint for ErrorDetail
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/errordetail.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_event_base_json_get(client: TestClient):
    """Test case for generated_event_base_json_get

    Generated endpoint for Event_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/event_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_event_json_get(client: TestClient):
    """Test case for generated_event_json_get

    Generated endpoint for Event
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/event.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_eventmetrics_base_json_get(client: TestClient):
    """Test case for generated_eventmetrics_base_json_get

    Generated endpoint for EventMetrics_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/eventmetrics_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_eventmetrics_json_get(client: TestClient):
    """Test case for generated_eventmetrics_json_get

    Generated endpoint for EventMetrics
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/eventmetrics.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_evergreenretainer_base_json_get(client: TestClient):
    """Test case for generated_evergreenretainer_base_json_get

    Generated endpoint for EvergreenRetainer_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/evergreenretainer_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_expensecategory_base_json_get(client: TestClient):
    """Test case for generated_expensecategory_base_json_get

    Generated endpoint for ExpenseCategory_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/expensecategory_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_expensecategory_json_get(client: TestClient):
    """Test case for generated_expensecategory_json_get

    Generated endpoint for ExpenseCategory
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/expensecategory.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_externalproperty_base_json_get(client: TestClient):
    """Test case for generated_externalproperty_base_json_get

    Generated endpoint for ExternalProperty_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/externalproperty_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_folder_base_json_get(client: TestClient):
    """Test case for generated_folder_base_json_get

    Generated endpoint for Folder_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/folder_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_folder_json_get(client: TestClient):
    """Test case for generated_folder_json_get

    Generated endpoint for Folder
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/folder.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_grant_base_json_get(client: TestClient):
    """Test case for generated_grant_base_json_get

    Generated endpoint for Grant_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/grant_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_grant_json_get(client: TestClient):
    """Test case for generated_grant_json_get

    Generated endpoint for Grant
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/grant.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_grantfundingsource_base_json_get(client: TestClient):
    """Test case for generated_grantfundingsource_base_json_get

    Generated endpoint for GrantFundingSource_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/grantfundingsource_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_grantfundingsource_json_get(client: TestClient):
    """Test case for generated_grantfundingsource_json_get

    Generated endpoint for GrantFundingSource
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/grantfundingsource.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_group_base_json_get(client: TestClient):
    """Test case for generated_group_base_json_get

    Generated endpoint for Group_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/group_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_group_json_get(client: TestClient):
    """Test case for generated_group_json_get

    Generated endpoint for Group
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/group.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_idsresponse_json_get(client: TestClient):
    """Test case for generated_idsresponse_json_get

    Generated endpoint for IdsResponse
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/idsresponse.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_instantmessenger_base_json_get(client: TestClient):
    """Test case for generated_instantmessenger_base_json_get

    Generated endpoint for InstantMessenger_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/instantmessenger_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_interest_base_json_get(client: TestClient):
    """Test case for generated_interest_base_json_get

    Generated endpoint for Interest_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/interest_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_interest_json_get(client: TestClient):
    """Test case for generated_interest_json_get

    Generated endpoint for Interest
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/interest.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_interestcharge_base_json_get(client: TestClient):
    """Test case for generated_interestcharge_base_json_get

    Generated endpoint for InterestCharge_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/interestcharge_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_interestcharge_json_get(client: TestClient):
    """Test case for generated_interestcharge_json_get

    Generated endpoint for InterestCharge
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/interestcharge.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_item_base_json_get(client: TestClient):
    """Test case for generated_item_base_json_get

    Generated endpoint for Item_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/item_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_item_json_get(client: TestClient):
    """Test case for generated_item_json_get

    Generated endpoint for Item
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/item.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_jobtitle_base_json_get(client: TestClient):
    """Test case for generated_jobtitle_base_json_get

    Generated endpoint for JobTitle_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/jobtitle_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_jurisdiction_base_json_get(client: TestClient):
    """Test case for generated_jurisdiction_base_json_get

    Generated endpoint for Jurisdiction_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/jurisdiction_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_jurisdiction_json_get(client: TestClient):
    """Test case for generated_jurisdiction_json_get

    Generated endpoint for Jurisdiction
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/jurisdiction.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_jurisdictionstotrigger_base_json_get(client: TestClient):
    """Test case for generated_jurisdictionstotrigger_base_json_get

    Generated endpoint for JurisdictionsToTrigger_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/jurisdictionstotrigger_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_jurisdictionstotrigger_json_get(client: TestClient):
    """Test case for generated_jurisdictionstotrigger_json_get

    Generated endpoint for JurisdictionsToTrigger
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/jurisdictionstotrigger.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcivilcertificatedrate_base_json_get(client: TestClient):
    """Test case for generated_laukcivilcertificatedrate_base_json_get

    Generated endpoint for LaukCivilCertificatedRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcivilcertificatedrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcivilcertificatedrate_json_get(client: TestClient):
    """Test case for generated_laukcivilcertificatedrate_json_get

    Generated endpoint for LaukCivilCertificatedRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcivilcertificatedrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcivilcontrolledrate_base_json_get(client: TestClient):
    """Test case for generated_laukcivilcontrolledrate_base_json_get

    Generated endpoint for LaukCivilControlledRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcivilcontrolledrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcivilcontrolledrate_json_get(client: TestClient):
    """Test case for generated_laukcivilcontrolledrate_json_get

    Generated endpoint for LaukCivilControlledRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcivilcontrolledrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcriminalcontrolledrate_base_json_get(client: TestClient):
    """Test case for generated_laukcriminalcontrolledrate_base_json_get

    Generated endpoint for LaukCriminalControlledRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcriminalcontrolledrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukcriminalcontrolledrate_json_get(client: TestClient):
    """Test case for generated_laukcriminalcontrolledrate_json_get

    Generated endpoint for LaukCriminalControlledRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukcriminalcontrolledrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukexpensecategory_base_json_get(client: TestClient):
    """Test case for generated_laukexpensecategory_base_json_get

    Generated endpoint for LaukExpenseCategory_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukexpensecategory_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_laukexpensecategory_json_get(client: TestClient):
    """Test case for generated_laukexpensecategory_json_get

    Generated endpoint for LaukExpenseCategory
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/laukexpensecategory.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_legalaidukactivity_base_json_get(client: TestClient):
    """Test case for generated_legalaidukactivity_base_json_get

    Generated endpoint for LegalAidUkActivity_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/legalaidukactivity_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_legalaidukbill_base_json_get(client: TestClient):
    """Test case for generated_legalaidukbill_base_json_get

    Generated endpoint for LegalAidUkBill_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/legalaidukbill_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_legalaidukcontact_base_json_get(client: TestClient):
    """Test case for generated_legalaidukcontact_base_json_get

    Generated endpoint for LegalAidUkContact_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/legalaidukcontact_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_legalaidukmatter_base_json_get(client: TestClient):
    """Test case for generated_legalaidukmatter_base_json_get

    Generated endpoint for LegalAidUkMatter_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/legalaidukmatter_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_lien_base_json_get(client: TestClient):
    """Test case for generated_lien_base_json_get

    Generated endpoint for Lien_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/lien_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_lineitem_base_json_get(client: TestClient):
    """Test case for generated_lineitem_base_json_get

    Generated endpoint for LineItem_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/lineitem_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_lineitem_json_get(client: TestClient):
    """Test case for generated_lineitem_json_get

    Generated endpoint for LineItem
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/lineitem.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_lineitemtotals_base_json_get(client: TestClient):
    """Test case for generated_lineitemtotals_base_json_get

    Generated endpoint for LineItemTotals_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/lineitemtotals_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_linkedfolder_base_json_get(client: TestClient):
    """Test case for generated_linkedfolder_base_json_get

    Generated endpoint for LinkedFolder_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/linkedfolder_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_logentry_base_json_get(client: TestClient):
    """Test case for generated_logentry_base_json_get

    Generated endpoint for LogEntry_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/logentry_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_logentry_json_get(client: TestClient):
    """Test case for generated_logentry_json_get

    Generated endpoint for LogEntry
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/logentry.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matter_base_json_get(client: TestClient):
    """Test case for generated_matter_base_json_get

    Generated endpoint for Matter_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matter_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matter_json_get(client: TestClient):
    """Test case for generated_matter_json_get

    Generated endpoint for Matter
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matter.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterbalance_base_json_get(client: TestClient):
    """Test case for generated_matterbalance_base_json_get

    Generated endpoint for MatterBalance_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterbalance_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterbillrecipient_base_json_get(client: TestClient):
    """Test case for generated_matterbillrecipient_base_json_get

    Generated endpoint for MatterBillRecipient_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterbillrecipient_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterbillrecipient_json_get(client: TestClient):
    """Test case for generated_matterbillrecipient_json_get

    Generated endpoint for MatterBillRecipient
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterbillrecipient.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterbudget_base_json_get(client: TestClient):
    """Test case for generated_matterbudget_base_json_get

    Generated endpoint for MatterBudget_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterbudget_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_mattercontacts_base_json_get(client: TestClient):
    """Test case for generated_mattercontacts_base_json_get

    Generated endpoint for MatterContacts_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/mattercontacts_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_mattercontacts_json_get(client: TestClient):
    """Test case for generated_mattercontacts_json_get

    Generated endpoint for MatterContacts
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/mattercontacts.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_mattercustomrate_base_json_get(client: TestClient):
    """Test case for generated_mattercustomrate_base_json_get

    Generated endpoint for MatterCustomRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/mattercustomrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_mattercustomrate_json_get(client: TestClient):
    """Test case for generated_mattercustomrate_json_get

    Generated endpoint for MatterCustomRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/mattercustomrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterdocket_base_json_get(client: TestClient):
    """Test case for generated_matterdocket_base_json_get

    Generated endpoint for MatterDocket_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterdocket_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterdocket_json_get(client: TestClient):
    """Test case for generated_matterdocket_json_get

    Generated endpoint for MatterDocket
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterdocket.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterstage_base_json_get(client: TestClient):
    """Test case for generated_matterstage_base_json_get

    Generated endpoint for MatterStage_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterstage_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_matterstage_json_get(client: TestClient):
    """Test case for generated_matterstage_json_get

    Generated endpoint for MatterStage
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/matterstage.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalbill_base_json_get(client: TestClient):
    """Test case for generated_medicalbill_base_json_get

    Generated endpoint for MedicalBill_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalbill_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalbill_json_get(client: TestClient):
    """Test case for generated_medicalbill_json_get

    Generated endpoint for MedicalBill
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalbill.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalrecord_base_json_get(client: TestClient):
    """Test case for generated_medicalrecord_base_json_get

    Generated endpoint for MedicalRecord_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalrecord_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalrecord_json_get(client: TestClient):
    """Test case for generated_medicalrecord_json_get

    Generated endpoint for MedicalRecord
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalrecord.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalrecordsrequest_base_json_get(client: TestClient):
    """Test case for generated_medicalrecordsrequest_base_json_get

    Generated endpoint for MedicalRecordsRequest_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalrecordsrequest_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_medicalrecordsrequest_json_get(client: TestClient):
    """Test case for generated_medicalrecordsrequest_json_get

    Generated endpoint for MedicalRecordsRequest
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/medicalrecordsrequest.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_multipart_base_json_get(client: TestClient):
    """Test case for generated_multipart_base_json_get

    Generated endpoint for Multipart_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/multipart_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_multipart_json_get(client: TestClient):
    """Test case for generated_multipart_json_get

    Generated endpoint for Multipart
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/multipart.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_multipartheader_base_json_get(client: TestClient):
    """Test case for generated_multipartheader_base_json_get

    Generated endpoint for MultipartHeader_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/multipartheader_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_myevent_base_json_get(client: TestClient):
    """Test case for generated_myevent_base_json_get

    Generated endpoint for MyEvent_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/myevent_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_myevent_json_get(client: TestClient):
    """Test case for generated_myevent_json_get

    Generated endpoint for MyEvent
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/myevent.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_note_base_json_get(client: TestClient):
    """Test case for generated_note_base_json_get

    Generated endpoint for Note_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/note_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_note_json_get(client: TestClient):
    """Test case for generated_note_json_get

    Generated endpoint for Note
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/note.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_notificationeventsubscriber_base_json_get(client: TestClient):
    """Test case for generated_notificationeventsubscriber_base_json_get

    Generated endpoint for NotificationEventSubscriber_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/notificationeventsubscriber_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_notificationmethod_base_json_get(client: TestClient):
    """Test case for generated_notificationmethod_base_json_get

    Generated endpoint for NotificationMethod_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/notificationmethod_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_outstandingclientbalance_base_json_get(client: TestClient):
    """Test case for generated_outstandingclientbalance_base_json_get

    Generated endpoint for OutstandingClientBalance_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/outstandingclientbalance_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_outstandingclientbalance_json_get(client: TestClient):
    """Test case for generated_outstandingclientbalance_json_get

    Generated endpoint for OutstandingClientBalance
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/outstandingclientbalance.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_participant_base_json_get(client: TestClient):
    """Test case for generated_participant_base_json_get

    Generated endpoint for Participant_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/participant_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_participant_json_get(client: TestClient):
    """Test case for generated_participant_json_get

    Generated endpoint for Participant
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/participant.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_payment_base_json_get(client: TestClient):
    """Test case for generated_payment_base_json_get

    Generated endpoint for Payment_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/payment_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_payment_json_get(client: TestClient):
    """Test case for generated_payment_json_get

    Generated endpoint for Payment
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/payment.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_paymentprofile_base_json_get(client: TestClient):
    """Test case for generated_paymentprofile_base_json_get

    Generated endpoint for PaymentProfile_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/paymentprofile_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_phonenumber_base_json_get(client: TestClient):
    """Test case for generated_phonenumber_base_json_get

    Generated endpoint for PhoneNumber_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/phonenumber_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_phonenumber_json_get(client: TestClient):
    """Test case for generated_phonenumber_json_get

    Generated endpoint for PhoneNumber
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/phonenumber.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_picklistoption_base_json_get(client: TestClient):
    """Test case for generated_picklistoption_base_json_get

    Generated endpoint for PicklistOption_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/picklistoption_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_picklistoption_json_get(client: TestClient):
    """Test case for generated_picklistoption_json_get

    Generated endpoint for PicklistOption
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/picklistoption.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphiccustomrate_activitydescription_base_json_get(client: TestClient):
    """Test case for generated_polymorphiccustomrate_activitydescription_base_json_get

    Generated endpoint for PolymorphicCustomRate_ActivityDescription_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphiccustomrate_activitydescription_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphiccustomrate_base_json_get(client: TestClient):
    """Test case for generated_polymorphiccustomrate_base_json_get

    Generated endpoint for PolymorphicCustomRate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphiccustomrate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphiccustomrate_group_base_json_get(client: TestClient):
    """Test case for generated_polymorphiccustomrate_group_base_json_get

    Generated endpoint for PolymorphicCustomRate_Group_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphiccustomrate_group_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphiccustomrate_json_get(client: TestClient):
    """Test case for generated_polymorphiccustomrate_json_get

    Generated endpoint for PolymorphicCustomRate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphiccustomrate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphiccustomrate_user_base_json_get(client: TestClient):
    """Test case for generated_polymorphiccustomrate_user_base_json_get

    Generated endpoint for PolymorphicCustomRate_User_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphiccustomrate_user_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_polymorphicobject_base_json_get(client: TestClient):
    """Test case for generated_polymorphicobject_base_json_get

    Generated endpoint for PolymorphicObject_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/polymorphicobject_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_practicearea_base_json_get(client: TestClient):
    """Test case for generated_practicearea_base_json_get

    Generated endpoint for PracticeArea_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/practicearea_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_practicearea_json_get(client: TestClient):
    """Test case for generated_practicearea_json_get

    Generated endpoint for PracticeArea
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/practicearea.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_relatedcontacts_base_json_get(client: TestClient):
    """Test case for generated_relatedcontacts_base_json_get

    Generated endpoint for RelatedContacts_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/relatedcontacts_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_relatedcontacts_json_get(client: TestClient):
    """Test case for generated_relatedcontacts_json_get

    Generated endpoint for RelatedContacts
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/relatedcontacts.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_relationship_base_json_get(client: TestClient):
    """Test case for generated_relationship_base_json_get

    Generated endpoint for Relationship_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/relationship_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_relationship_json_get(client: TestClient):
    """Test case for generated_relationship_json_get

    Generated endpoint for Relationship
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/relationship.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reminder_base_json_get(client: TestClient):
    """Test case for generated_reminder_base_json_get

    Generated endpoint for Reminder_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reminder_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reminder_json_get(client: TestClient):
    """Test case for generated_reminder_json_get

    Generated endpoint for Reminder
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reminder.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_remindertemplate_base_json_get(client: TestClient):
    """Test case for generated_remindertemplate_base_json_get

    Generated endpoint for ReminderTemplate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/remindertemplate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_report_base_json_get(client: TestClient):
    """Test case for generated_report_base_json_get

    Generated endpoint for Report_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/report_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_report_json_get(client: TestClient):
    """Test case for generated_report_json_get

    Generated endpoint for Report
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/report.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reportpreset_base_json_get(client: TestClient):
    """Test case for generated_reportpreset_base_json_get

    Generated endpoint for ReportPreset_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reportpreset_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reportpreset_json_get(client: TestClient):
    """Test case for generated_reportpreset_json_get

    Generated endpoint for ReportPreset
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reportpreset.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reportschedule_base_json_get(client: TestClient):
    """Test case for generated_reportschedule_base_json_get

    Generated endpoint for ReportSchedule_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reportschedule_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_reportschedule_json_get(client: TestClient):
    """Test case for generated_reportschedule_json_get

    Generated endpoint for ReportSchedule
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/reportschedule.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_servicetype_base_json_get(client: TestClient):
    """Test case for generated_servicetype_base_json_get

    Generated endpoint for ServiceType_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/servicetype_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_servicetype_json_get(client: TestClient):
    """Test case for generated_servicetype_json_get

    Generated endpoint for ServiceType
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/servicetype.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_splitinvoice_base_json_get(client: TestClient):
    """Test case for generated_splitinvoice_base_json_get

    Generated endpoint for SplitInvoice_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/splitinvoice_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_splitinvoicepayer_base_json_get(client: TestClient):
    """Test case for generated_splitinvoicepayer_base_json_get

    Generated endpoint for SplitInvoicePayer_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/splitinvoicepayer_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_task_base_json_get(client: TestClient):
    """Test case for generated_task_base_json_get

    Generated endpoint for Task_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/task_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_task_json_get(client: TestClient):
    """Test case for generated_task_json_get

    Generated endpoint for Task
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/task.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktemplate_base_json_get(client: TestClient):
    """Test case for generated_tasktemplate_base_json_get

    Generated endpoint for TaskTemplate_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktemplate_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktemplate_json_get(client: TestClient):
    """Test case for generated_tasktemplate_json_get

    Generated endpoint for TaskTemplate
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktemplate.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktemplatelist_base_json_get(client: TestClient):
    """Test case for generated_tasktemplatelist_base_json_get

    Generated endpoint for TaskTemplateList_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktemplatelist_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktemplatelist_json_get(client: TestClient):
    """Test case for generated_tasktemplatelist_json_get

    Generated endpoint for TaskTemplateList
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktemplatelist.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktemplatelistinstace_base_json_get(client: TestClient):
    """Test case for generated_tasktemplatelistinstace_base_json_get

    Generated endpoint for TaskTemplateListInstace_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktemplatelistinstace_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktype_base_json_get(client: TestClient):
    """Test case for generated_tasktype_base_json_get

    Generated endpoint for TaskType_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktype_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_tasktype_json_get(client: TestClient):
    """Test case for generated_tasktype_json_get

    Generated endpoint for TaskType
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/tasktype.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_textsnippet_base_json_get(client: TestClient):
    """Test case for generated_textsnippet_base_json_get

    Generated endpoint for TextSnippet_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/textsnippet_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_textsnippet_json_get(client: TestClient):
    """Test case for generated_textsnippet_json_get

    Generated endpoint for TextSnippet
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/textsnippet.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_timer_base_json_get(client: TestClient):
    """Test case for generated_timer_base_json_get

    Generated endpoint for Timer_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/timer_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_timer_json_get(client: TestClient):
    """Test case for generated_timer_json_get

    Generated endpoint for Timer
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/timer.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_trustlineitem_base_json_get(client: TestClient):
    """Test case for generated_trustlineitem_base_json_get

    Generated endpoint for TrustLineItem_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/trustlineitem_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_trustlineitem_json_get(client: TestClient):
    """Test case for generated_trustlineitem_json_get

    Generated endpoint for TrustLineItem
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/trustlineitem.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_trustrequest_base_json_get(client: TestClient):
    """Test case for generated_trustrequest_base_json_get

    Generated endpoint for TrustRequest_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/trustrequest_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_trustrequest_json_get(client: TestClient):
    """Test case for generated_trustrequest_json_get

    Generated endpoint for TrustRequest
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/trustrequest.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_unredactedparticipant_base_json_get(client: TestClient):
    """Test case for generated_unredactedparticipant_base_json_get

    Generated endpoint for UnredactedParticipant_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/unredactedparticipant_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_user_base_json_get(client: TestClient):
    """Test case for generated_user_base_json_get

    Generated endpoint for User_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/user_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_user_json_get(client: TestClient):
    """Test case for generated_user_json_get

    Generated endpoint for User
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/user.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_utbmscode_base_json_get(client: TestClient):
    """Test case for generated_utbmscode_base_json_get

    Generated endpoint for UtbmsCode_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/utbmscode_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_utbmscode_json_get(client: TestClient):
    """Test case for generated_utbmscode_json_get

    Generated endpoint for UtbmsCode
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/utbmscode.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_utbmsset_base_json_get(client: TestClient):
    """Test case for generated_utbmsset_base_json_get

    Generated endpoint for UtbmsSet_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/utbmsset_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_utbmsset_json_get(client: TestClient):
    """Test case for generated_utbmsset_json_get

    Generated endpoint for UtbmsSet
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/utbmsset.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_webhook_base_json_get(client: TestClient):
    """Test case for generated_webhook_base_json_get

    Generated endpoint for Webhook_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/webhook_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_webhook_json_get(client: TestClient):
    """Test case for generated_webhook_json_get

    Generated endpoint for Webhook
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/webhook.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_generated_website_base_json_get(client: TestClient):
    """Test case for generated_website_base_json_get

    Generated endpoint for WebSite_base
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/generated/website_base.json",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

