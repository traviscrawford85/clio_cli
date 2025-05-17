# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

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


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def generated_account_base_json_get(
        self,
    ) -> AccountBase:
        ...


    async def generated_account_json_get(
        self,
    ) -> Account:
        ...


    async def generated_accountbalance_base_json_get(
        self,
    ) -> AccountBalanceBase:
        ...


    async def generated_activity_base_json_get(
        self,
    ) -> ActivityBase:
        ...


    async def generated_activity_calendarentry_base_json_get(
        self,
    ) -> ActivityCalendarEntryBase:
        ...


    async def generated_activity_json_get(
        self,
    ) -> Activity:
        ...


    async def generated_activity_task_base_json_get(
        self,
    ) -> ActivityTaskBase:
        ...


    async def generated_activity_textmessageconversation_base_json_get(
        self,
    ) -> ActivityTextMessageConversationBase:
        ...


    async def generated_activitydescription_base_json_get(
        self,
    ) -> ActivityDescriptionBase:
        ...


    async def generated_activitydescription_json_get(
        self,
    ) -> ActivityDescription:
        ...


    async def generated_activitydescriptionrate_base_json_get(
        self,
    ) -> ActivityDescriptionRateBase:
        ...


    async def generated_activityrate_base_json_get(
        self,
    ) -> ActivityRateBase:
        ...


    async def generated_activityrate_json_get(
        self,
    ) -> ActivityRate:
        ...


    async def generated_address_base_json_get(
        self,
    ) -> AddressBase:
        ...


    async def generated_address_json_get(
        self,
    ) -> Address:
        ...


    async def generated_allocation_base_json_get(
        self,
    ) -> AllocationBase:
        ...


    async def generated_allocation_json_get(
        self,
    ) -> Allocation:
        ...


    async def generated_attendee_base_json_get(
        self,
    ) -> AttendeeBase:
        ...


    async def generated_avatar_base_json_get(
        self,
    ) -> AvatarBase:
        ...


    async def generated_balance_base_json_get(
        self,
    ) -> BalanceBase:
        ...


    async def generated_balance_json_get(
        self,
    ) -> Balance:
        ...


    async def generated_bankaccount_base_json_get(
        self,
    ) -> BankAccountBase:
        ...


    async def generated_bankaccount_json_get(
        self,
    ) -> BankAccount:
        ...


    async def generated_banktransaction_base_json_get(
        self,
    ) -> BankTransactionBase:
        ...


    async def generated_banktransaction_json_get(
        self,
    ) -> BankTransaction:
        ...


    async def generated_banktransfer_base_json_get(
        self,
    ) -> BankTransferBase:
        ...


    async def generated_banktransfer_json_get(
        self,
    ) -> BankTransfer:
        ...


    async def generated_bill_base_json_get(
        self,
    ) -> BillBase:
        ...


    async def generated_bill_json_get(
        self,
    ) -> Bill:
        ...


    async def generated_billableclient_base_json_get(
        self,
    ) -> BillableClientBase:
        ...


    async def generated_billableclient_json_get(
        self,
    ) -> BillableClient:
        ...


    async def generated_billablematter_base_json_get(
        self,
    ) -> BillableMatterBase:
        ...


    async def generated_billablematter_json_get(
        self,
    ) -> BillableMatter:
        ...


    async def generated_billingsetting_base_json_get(
        self,
    ) -> BillingSettingBase:
        ...


    async def generated_billingsetting_json_get(
        self,
    ) -> BillingSetting:
        ...


    async def generated_billrecipient_base_json_get(
        self,
    ) -> BillRecipientBase:
        ...


    async def generated_billrecipient_contact_base_json_get(
        self,
    ) -> BillRecipientContactBase:
        ...


    async def generated_billrecipient_json_get(
        self,
    ) -> BillRecipient:
        ...


    async def generated_billtheme_base_json_get(
        self,
    ) -> BillThemeBase:
        ...


    async def generated_billtheme_json_get(
        self,
    ) -> BillTheme:
        ...


    async def generated_calendar_base_json_get(
        self,
    ) -> CalendarBase:
        ...


    async def generated_calendar_json_get(
        self,
    ) -> Calendar:
        ...


    async def generated_calendarentry_base_json_get(
        self,
    ) -> CalendarEntryBase:
        ...


    async def generated_calendarentry_json_get(
        self,
    ) -> CalendarEntry:
        ...


    async def generated_calendarentryeventtype_base_json_get(
        self,
    ) -> CalendarEntryEventTypeBase:
        ...


    async def generated_calendarvisibility_base_json_get(
        self,
    ) -> CalendarVisibilityBase:
        ...


    async def generated_calendarvisibility_json_get(
        self,
    ) -> CalendarVisibility:
        ...


    async def generated_cascadingtask_base_json_get(
        self,
    ) -> object:
        ...


    async def generated_cascadingtasktemplate_base_json_get(
        self,
    ) -> CascadingTaskTemplateBase:
        ...


    async def generated_client_base_json_get(
        self,
    ) -> ClientBase:
        ...


    async def generated_client_json_get(
        self,
    ) -> Client:
        ...


    async def generated_clientportal_base_json_get(
        self,
    ) -> ClientPortalBase:
        ...


    async def generated_cliocreator_base_json_get(
        self,
    ) -> ClioCreatorBase:
        ...


    async def generated_cliopaymentslink_base_json_get(
        self,
    ) -> ClioPaymentsLinkBase:
        ...


    async def generated_cliopaymentslink_json_get(
        self,
    ) -> ClioPaymentsLink:
        ...


    async def generated_cliopaymentspayment_base_json_get(
        self,
    ) -> ClioPaymentsPaymentBase:
        ...


    async def generated_cliopaymentspayment_json_get(
        self,
    ) -> ClioPaymentsPayment:
        ...


    async def generated_comment_base_json_get(
        self,
    ) -> CommentBase:
        ...


    async def generated_comment_json_get(
        self,
    ) -> Comment:
        ...


    async def generated_communication_base_json_get(
        self,
    ) -> CommunicationBase:
        ...


    async def generated_communication_json_get(
        self,
    ) -> Communication:
        ...


    async def generated_communicationemlfile_base_json_get(
        self,
    ) -> CommunicationEmlFileBase:
        ...


    async def generated_conferencemeeting_base_json_get(
        self,
    ) -> ConferenceMeetingBase:
        ...


    async def generated_contact_base_json_get(
        self,
    ) -> ContactBase:
        ...


    async def generated_contact_json_get(
        self,
    ) -> Contact:
        ...


    async def generated_contingencyfee_base_json_get(
        self,
    ) -> ContingencyFeeBase:
        ...


    async def generated_conversation_base_json_get(
        self,
    ) -> ConversationBase:
        ...


    async def generated_conversation_json_get(
        self,
    ) -> Conversation:
        ...


    async def generated_conversationmembership_base_json_get(
        self,
    ) -> ConversationMembershipBase:
        ...


    async def generated_conversationmembership_json_get(
        self,
    ) -> ConversationMembership:
        ...


    async def generated_conversationmessage_base_json_get(
        self,
    ) -> ConversationMessageBase:
        ...


    async def generated_conversationmessage_json_get(
        self,
    ) -> ConversationMessage:
        ...


    async def generated_creditmemo_base_json_get(
        self,
    ) -> CreditMemoBase:
        ...


    async def generated_creditmemo_json_get(
        self,
    ) -> CreditMemo:
        ...


    async def generated_currency_base_json_get(
        self,
    ) -> CurrencyBase:
        ...


    async def generated_currency_json_get(
        self,
    ) -> Currency:
        ...


    async def generated_customaction_base_json_get(
        self,
    ) -> CustomActionBase:
        ...


    async def generated_customaction_json_get(
        self,
    ) -> CustomAction:
        ...


    async def generated_customfield_base_json_get(
        self,
    ) -> CustomFieldBase:
        ...


    async def generated_customfield_json_get(
        self,
    ) -> CustomField:
        ...


    async def generated_customfieldmatterselection_base_json_get(
        self,
    ) -> CustomFieldMatterSelectionBase:
        ...


    async def generated_customfieldmatterselection_json_get(
        self,
    ) -> CustomFieldMatterSelection:
        ...


    async def generated_customfieldset_base_json_get(
        self,
    ) -> CustomFieldSetBase:
        ...


    async def generated_customfieldset_json_get(
        self,
    ) -> CustomFieldSet:
        ...


    async def generated_customfieldsetassociation_base_json_get(
        self,
    ) -> CustomFieldSetAssociationBase:
        ...


    async def generated_customfieldvalue_base_json_get(
        self,
    ) -> CustomFieldValueBase:
        ...


    async def generated_customfieldvalue_json_get(
        self,
    ) -> CustomFieldValue:
        ...


    async def generated_damage_base_json_get(
        self,
    ) -> DamageBase:
        ...


    async def generated_damage_json_get(
        self,
    ) -> Damage:
        ...


    async def generated_discount_base_json_get(
        self,
    ) -> DiscountBase:
        ...


    async def generated_document_base_json_get(
        self,
    ) -> DocumentBase:
        ...


    async def generated_document_json_get(
        self,
    ) -> Document:
        ...


    async def generated_documentarchive_base_json_get(
        self,
    ) -> DocumentArchiveBase:
        ...


    async def generated_documentarchive_json_get(
        self,
    ) -> DocumentArchive:
        ...


    async def generated_documentautomation_base_json_get(
        self,
    ) -> DocumentAutomationBase:
        ...


    async def generated_documentautomation_json_get(
        self,
    ) -> DocumentAutomation:
        ...


    async def generated_documentcategory_base_json_get(
        self,
    ) -> DocumentCategoryBase:
        ...


    async def generated_documentcategory_json_get(
        self,
    ) -> DocumentCategory:
        ...


    async def generated_documenttemplate_base_json_get(
        self,
    ) -> DocumentTemplateBase:
        ...


    async def generated_documenttemplate_json_get(
        self,
    ) -> DocumentTemplate:
        ...


    async def generated_documentversion_base_json_get(
        self,
    ) -> DocumentVersionBase:
        ...


    async def generated_documentversion_json_get(
        self,
    ) -> DocumentVersion:
        ...


    async def generated_emailaddress_base_json_get(
        self,
    ) -> EmailAddressBase:
        ...


    async def generated_emailaddress_json_get(
        self,
    ) -> EmailAddress:
        ...


    async def generated_errordetail_json_get(
        self,
    ) -> ErrorDetail:
        ...


    async def generated_event_base_json_get(
        self,
    ) -> EventBase:
        ...


    async def generated_event_json_get(
        self,
    ) -> Event:
        ...


    async def generated_eventmetrics_base_json_get(
        self,
    ) -> EventMetricsBase:
        ...


    async def generated_eventmetrics_json_get(
        self,
    ) -> EventMetrics:
        ...


    async def generated_evergreenretainer_base_json_get(
        self,
    ) -> EvergreenRetainerBase:
        ...


    async def generated_expensecategory_base_json_get(
        self,
    ) -> ExpenseCategoryBase:
        ...


    async def generated_expensecategory_json_get(
        self,
    ) -> ExpenseCategory:
        ...


    async def generated_externalproperty_base_json_get(
        self,
    ) -> ExternalPropertyBase:
        ...


    async def generated_folder_base_json_get(
        self,
    ) -> FolderBase:
        ...


    async def generated_folder_json_get(
        self,
    ) -> Folder:
        ...


    async def generated_grant_base_json_get(
        self,
    ) -> GrantBase:
        ...


    async def generated_grant_json_get(
        self,
    ) -> Grant:
        ...


    async def generated_grantfundingsource_base_json_get(
        self,
    ) -> GrantFundingSourceBase:
        ...


    async def generated_grantfundingsource_json_get(
        self,
    ) -> GrantFundingSource:
        ...


    async def generated_group_base_json_get(
        self,
    ) -> GroupBase:
        ...


    async def generated_group_json_get(
        self,
    ) -> Group:
        ...


    async def generated_idsresponse_json_get(
        self,
    ) -> IdsResponse:
        ...


    async def generated_instantmessenger_base_json_get(
        self,
    ) -> InstantMessengerBase:
        ...


    async def generated_interest_base_json_get(
        self,
    ) -> InterestBase:
        ...


    async def generated_interest_json_get(
        self,
    ) -> Interest:
        ...


    async def generated_interestcharge_base_json_get(
        self,
    ) -> InterestChargeBase:
        ...


    async def generated_interestcharge_json_get(
        self,
    ) -> InterestCharge:
        ...


    async def generated_item_base_json_get(
        self,
    ) -> ItemBase:
        ...


    async def generated_item_json_get(
        self,
    ) -> Item:
        ...


    async def generated_jobtitle_base_json_get(
        self,
    ) -> JobTitleBase:
        ...


    async def generated_jurisdiction_base_json_get(
        self,
    ) -> JurisdictionBase:
        ...


    async def generated_jurisdiction_json_get(
        self,
    ) -> Jurisdiction:
        ...


    async def generated_jurisdictionstotrigger_base_json_get(
        self,
    ) -> JurisdictionsToTriggerBase:
        ...


    async def generated_jurisdictionstotrigger_json_get(
        self,
    ) -> JurisdictionsToTrigger:
        ...


    async def generated_laukcivilcertificatedrate_base_json_get(
        self,
    ) -> LaukCivilCertificatedRateBase:
        ...


    async def generated_laukcivilcertificatedrate_json_get(
        self,
    ) -> LaukCivilCertificatedRate:
        ...


    async def generated_laukcivilcontrolledrate_base_json_get(
        self,
    ) -> LaukCivilControlledRateBase:
        ...


    async def generated_laukcivilcontrolledrate_json_get(
        self,
    ) -> LaukCivilControlledRate:
        ...


    async def generated_laukcriminalcontrolledrate_base_json_get(
        self,
    ) -> LaukCriminalControlledRateBase:
        ...


    async def generated_laukcriminalcontrolledrate_json_get(
        self,
    ) -> LaukCriminalControlledRate:
        ...


    async def generated_laukexpensecategory_base_json_get(
        self,
    ) -> LaukExpenseCategoryBase:
        ...


    async def generated_laukexpensecategory_json_get(
        self,
    ) -> LaukExpenseCategory:
        ...


    async def generated_legalaidukactivity_base_json_get(
        self,
    ) -> LegalAidUkActivityBase:
        ...


    async def generated_legalaidukbill_base_json_get(
        self,
    ) -> LegalAidUkBillBase:
        ...


    async def generated_legalaidukcontact_base_json_get(
        self,
    ) -> LegalAidUkContactBase:
        ...


    async def generated_legalaidukmatter_base_json_get(
        self,
    ) -> LegalAidUkMatterBase:
        ...


    async def generated_lien_base_json_get(
        self,
    ) -> LienBase:
        ...


    async def generated_lineitem_base_json_get(
        self,
    ) -> LineItemBase:
        ...


    async def generated_lineitem_json_get(
        self,
    ) -> LineItem:
        ...


    async def generated_lineitemtotals_base_json_get(
        self,
    ) -> LineItemTotalsBase:
        ...


    async def generated_linkedfolder_base_json_get(
        self,
    ) -> LinkedFolderBase:
        ...


    async def generated_logentry_base_json_get(
        self,
    ) -> LogEntryBase:
        ...


    async def generated_logentry_json_get(
        self,
    ) -> LogEntry:
        ...


    async def generated_matter_base_json_get(
        self,
    ) -> MatterBase:
        ...


    async def generated_matter_json_get(
        self,
    ) -> Matter:
        ...


    async def generated_matterbalance_base_json_get(
        self,
    ) -> MatterBalanceBase:
        ...


    async def generated_matterbillrecipient_base_json_get(
        self,
    ) -> MatterBillRecipientBase:
        ...


    async def generated_matterbillrecipient_json_get(
        self,
    ) -> MatterBillRecipient:
        ...


    async def generated_matterbudget_base_json_get(
        self,
    ) -> MatterBudgetBase:
        ...


    async def generated_mattercontacts_base_json_get(
        self,
    ) -> MatterContactsBase:
        ...


    async def generated_mattercontacts_json_get(
        self,
    ) -> MatterContacts:
        ...


    async def generated_mattercustomrate_base_json_get(
        self,
    ) -> MatterCustomRateBase:
        ...


    async def generated_mattercustomrate_json_get(
        self,
    ) -> MatterCustomRate:
        ...


    async def generated_matterdocket_base_json_get(
        self,
    ) -> MatterDocketBase:
        ...


    async def generated_matterdocket_json_get(
        self,
    ) -> MatterDocket:
        ...


    async def generated_matterstage_base_json_get(
        self,
    ) -> MatterStageBase:
        ...


    async def generated_matterstage_json_get(
        self,
    ) -> MatterStage:
        ...


    async def generated_medicalbill_base_json_get(
        self,
    ) -> MedicalBillBase:
        ...


    async def generated_medicalbill_json_get(
        self,
    ) -> MedicalBill:
        ...


    async def generated_medicalrecord_base_json_get(
        self,
    ) -> MedicalRecordBase:
        ...


    async def generated_medicalrecord_json_get(
        self,
    ) -> MedicalRecord:
        ...


    async def generated_medicalrecordsrequest_base_json_get(
        self,
    ) -> MedicalRecordsRequestBase:
        ...


    async def generated_medicalrecordsrequest_json_get(
        self,
    ) -> MedicalRecordsRequest:
        ...


    async def generated_multipart_base_json_get(
        self,
    ) -> MultipartBase:
        ...


    async def generated_multipart_json_get(
        self,
    ) -> Multipart:
        ...


    async def generated_multipartheader_base_json_get(
        self,
    ) -> MultipartHeaderBase:
        ...


    async def generated_myevent_base_json_get(
        self,
    ) -> object:
        ...


    async def generated_myevent_json_get(
        self,
    ) -> MyEvent:
        ...


    async def generated_note_base_json_get(
        self,
    ) -> NoteBase:
        ...


    async def generated_note_json_get(
        self,
    ) -> Note:
        ...


    async def generated_notificationeventsubscriber_base_json_get(
        self,
    ) -> NotificationEventSubscriberBase:
        ...


    async def generated_notificationmethod_base_json_get(
        self,
    ) -> NotificationMethodBase:
        ...


    async def generated_outstandingclientbalance_base_json_get(
        self,
    ) -> OutstandingClientBalanceBase:
        ...


    async def generated_outstandingclientbalance_json_get(
        self,
    ) -> OutstandingClientBalance:
        ...


    async def generated_participant_base_json_get(
        self,
    ) -> ParticipantBase:
        ...


    async def generated_participant_json_get(
        self,
    ) -> Participant:
        ...


    async def generated_payment_base_json_get(
        self,
    ) -> PaymentBase:
        ...


    async def generated_payment_json_get(
        self,
    ) -> Payment:
        ...


    async def generated_paymentprofile_base_json_get(
        self,
    ) -> PaymentProfileBase:
        ...


    async def generated_phonenumber_base_json_get(
        self,
    ) -> PhoneNumberBase:
        ...


    async def generated_phonenumber_json_get(
        self,
    ) -> PhoneNumber:
        ...


    async def generated_picklistoption_base_json_get(
        self,
    ) -> PicklistOptionBase:
        ...


    async def generated_picklistoption_json_get(
        self,
    ) -> PicklistOption:
        ...


    async def generated_polymorphiccustomrate_activitydescription_base_json_get(
        self,
    ) -> PolymorphicCustomRateActivityDescriptionBase:
        ...


    async def generated_polymorphiccustomrate_base_json_get(
        self,
    ) -> PolymorphicCustomRateBase:
        ...


    async def generated_polymorphiccustomrate_group_base_json_get(
        self,
    ) -> PolymorphicCustomRateGroupBase:
        ...


    async def generated_polymorphiccustomrate_json_get(
        self,
    ) -> PolymorphicCustomRate:
        ...


    async def generated_polymorphiccustomrate_user_base_json_get(
        self,
    ) -> PolymorphicCustomRateUserBase:
        ...


    async def generated_polymorphicobject_base_json_get(
        self,
    ) -> PolymorphicObjectBase:
        ...


    async def generated_practicearea_base_json_get(
        self,
    ) -> PracticeAreaBase:
        ...


    async def generated_practicearea_json_get(
        self,
    ) -> PracticeArea:
        ...


    async def generated_relatedcontacts_base_json_get(
        self,
    ) -> RelatedContactsBase:
        ...


    async def generated_relatedcontacts_json_get(
        self,
    ) -> RelatedContacts:
        ...


    async def generated_relationship_base_json_get(
        self,
    ) -> RelationshipBase:
        ...


    async def generated_relationship_json_get(
        self,
    ) -> Relationship:
        ...


    async def generated_reminder_base_json_get(
        self,
    ) -> ReminderBase:
        ...


    async def generated_reminder_json_get(
        self,
    ) -> Reminder:
        ...


    async def generated_remindertemplate_base_json_get(
        self,
    ) -> ReminderTemplateBase:
        ...


    async def generated_report_base_json_get(
        self,
    ) -> ReportBase:
        ...


    async def generated_report_json_get(
        self,
    ) -> Report:
        ...


    async def generated_reportpreset_base_json_get(
        self,
    ) -> ReportPresetBase:
        ...


    async def generated_reportpreset_json_get(
        self,
    ) -> ReportPreset:
        ...


    async def generated_reportschedule_base_json_get(
        self,
    ) -> ReportScheduleBase:
        ...


    async def generated_reportschedule_json_get(
        self,
    ) -> ReportSchedule:
        ...


    async def generated_servicetype_base_json_get(
        self,
    ) -> ServiceTypeBase:
        ...


    async def generated_servicetype_json_get(
        self,
    ) -> ServiceType:
        ...


    async def generated_splitinvoice_base_json_get(
        self,
    ) -> SplitInvoiceBase:
        ...


    async def generated_splitinvoicepayer_base_json_get(
        self,
    ) -> SplitInvoicePayerBase:
        ...


    async def generated_task_base_json_get(
        self,
    ) -> TaskBase:
        ...


    async def generated_task_json_get(
        self,
    ) -> Task:
        ...


    async def generated_tasktemplate_base_json_get(
        self,
    ) -> TaskTemplateBase:
        ...


    async def generated_tasktemplate_json_get(
        self,
    ) -> TaskTemplate:
        ...


    async def generated_tasktemplatelist_base_json_get(
        self,
    ) -> TaskTemplateListBase:
        ...


    async def generated_tasktemplatelist_json_get(
        self,
    ) -> TaskTemplateList:
        ...


    async def generated_tasktemplatelistinstace_base_json_get(
        self,
    ) -> TaskTemplateListInstaceBase:
        ...


    async def generated_tasktype_base_json_get(
        self,
    ) -> TaskTypeBase:
        ...


    async def generated_tasktype_json_get(
        self,
    ) -> TaskType:
        ...


    async def generated_textsnippet_base_json_get(
        self,
    ) -> TextSnippetBase:
        ...


    async def generated_textsnippet_json_get(
        self,
    ) -> TextSnippet:
        ...


    async def generated_timer_base_json_get(
        self,
    ) -> TimerBase:
        ...


    async def generated_timer_json_get(
        self,
    ) -> Timer:
        ...


    async def generated_trustlineitem_base_json_get(
        self,
    ) -> TrustLineItemBase:
        ...


    async def generated_trustlineitem_json_get(
        self,
    ) -> TrustLineItem:
        ...


    async def generated_trustrequest_base_json_get(
        self,
    ) -> TrustRequestBase:
        ...


    async def generated_trustrequest_json_get(
        self,
    ) -> TrustRequest:
        ...


    async def generated_unredactedparticipant_base_json_get(
        self,
    ) -> object:
        ...


    async def generated_user_base_json_get(
        self,
    ) -> UserBase:
        ...


    async def generated_user_json_get(
        self,
    ) -> User:
        ...


    async def generated_utbmscode_base_json_get(
        self,
    ) -> UtbmsCodeBase:
        ...


    async def generated_utbmscode_json_get(
        self,
    ) -> UtbmsCode:
        ...


    async def generated_utbmsset_base_json_get(
        self,
    ) -> UtbmsSetBase:
        ...


    async def generated_utbmsset_json_get(
        self,
    ) -> UtbmsSet:
        ...


    async def generated_webhook_base_json_get(
        self,
    ) -> WebhookBase:
        ...


    async def generated_webhook_json_get(
        self,
    ) -> Webhook:
        ...


    async def generated_website_base_json_get(
        self,
    ) -> WebSiteBase:
        ...
