
from datetime import date, datetime
from typing import Any, List, Optional

from pydantic import BaseModel


class CustomFieldValueExtended(BaseModel):
    pass

class CustomFieldExtended(BaseModel):
    pass

class AccountBalance_base(BaseModel):
    balance: float = None
    id: int = None
    name: str = None
    type: str = None
class Account_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    state: str = None
    updated_at: str = None
class Activity(BaseModel):
    pass

class ActivityDescription(BaseModel):
    pass

class ActivityDescriptionRate_base(BaseModel):
    amount: float = None
    hierarchy: str = None
    non_billable_amount: float = None
    type: str = None
class ActivityDescription_List(BaseModel):
    data: List[ActivityDescription]
class ActivityDescription_Show(BaseModel):
    data: ActivityDescription
class ActivityDescription_base(BaseModel):
    accessible_to_user: bool = None
    category_type: str = None
    created_at: str = None
    default: bool = None
    etag: str = None
    id: int = None
    name: str = None
    type: str = None
    updated_at: str = None
    utbms_activity_id: int = None
    utbms_task_id: int = None
    utbms_task_name: str = None
    visible_to_co_counsel: bool = None
    xero_service_code: str = None
class ActivityRate(BaseModel):
    pass

class ActivityRate_List(BaseModel):
    data: List[ActivityRate]
class ActivityRate_Show(BaseModel):
    data: ActivityRate
class ActivityRate_base(BaseModel):
    co_counsel_contact_id: int = None
    contact_id: int = None
    created_at: str = None
    etag: str = None
    flat_rate: bool = None
    id: int = None
    rate: float = None
    updated_at: str = None
class Activity_CalendarEntry_base(BaseModel):
    calendar_owner_id: int = None
    etag: str = None
    id: str = None
class Activity_List(BaseModel):
    data: List[Activity]
class Activity_Show(BaseModel):
    data: dict
class Activity_Task_base(BaseModel):
    etag: str = None
    id: int = None
class Activity_TextMessageConversation_base(BaseModel):
    etag: str = None
    id: int = None
class Activity_base(BaseModel):
    billed: bool = None
    contingency_fee: bool = None
    created_at: str = None
    date: str = None
    etag: str = None
    flat_rate: bool = None
    id: int = None
    no_charge: bool = None
    non_billable: bool = None
    non_billable_total: float = None
    note: str = None
    on_bill: bool = None
    price: float = None
    quantity: float = None
    quantity_in_hours: float = None
    quantity_redacted: bool = None
    reference: str = None
    rounded_quantity: float = None
    rounded_quantity_in_hours: float = None
    tax_setting: str = None
    total: float = None
    type: str = None
    updated_at: str = None
class Address_base(BaseModel):
    city: str = None
    country: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    postal_code: str = None
    primary: bool = None
    province: str = None
    street: str = None
    updated_at: str = None
class Allocation(BaseModel):
    pass

class Allocation_List(BaseModel):
    data: List[Allocation]
class Allocation_Show(BaseModel):
    data: Allocation
class Allocation_base(BaseModel):
    amount: float = None
    created_at: str = None
    date: str = None
    description: str = None
    destroyable: bool = None
    etag: str = None
    has_online_payment: bool = None
    id: int = None
    interest: bool = None
    payment_type: str = None
    updated_at: str = None
    voided_at: str = None
class Attendee_base(BaseModel):
    created_at: str = None
    email: str = None
    enabled: bool = None
    etag: str = None
    id: int = None
    name: str = None
    type: str = None
    updated_at: str = None
class Avatar_base(BaseModel):
    _destroy: bool = None
    created_at: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
    url: str = None
class Balance_base(BaseModel):
    amount: float = None
    due: float = None
    id: int = None
    interest_amount: float = None
    type: str = None
class BankAccount(BaseModel):
    pass

class BankAccount_List(BaseModel):
    data: List[BankAccount]
class BankAccount_Show(BaseModel):
    data: BankAccount
class BankAccount_base(BaseModel):
    account_number: str = None
    balance: float = None
    bank_transactions_count: int = None
    clio_payment_page_link: str = None
    clio_payment_page_qr_code: str = None
    clio_payments_enabled: bool = None
    controlled_account: bool = None
    created_at: str = None
    currency: str = None
    default_account: bool = None
    domicile_branch: str = None
    etag: str = None
    general_ledger_number: str = None
    holder: str = None
    id: int = None
    institution: str = None
    name: str = None
    swift: str = None
    transit_number: str = None
    type: str = None
    updated_at: str = None
class BankTransaction(BaseModel):
    pass

class BankTransaction_List(BaseModel):
    data: List[BankTransaction]
class BankTransaction_Show(BaseModel):
    data: BankTransaction
class BankTransaction_base(BaseModel):
    amount: float = None
    bank_account_id: int = None
    clio_payments_transaction: bool = None
    confirmation: str = None
    created_at: str = None
    currency: str = None
    current_account_balance: float = None
    date: str = None
    description: str = None
    etag: str = None
    exchange_rate: float = None
    funds_in: float = None
    funds_out: float = None
    id: int = None
    read_only_confirmation: bool = None
    source: str = None
    transaction_type: str = None
    type: str = None
    updated_at: str = None
class BankTransfer(BaseModel):
    pass

class BankTransfer_Show(BaseModel):
    data: BankTransfer
class BankTransfer_base(BaseModel):
    amount: float = None
    created_at: str = None
    date: str = None
    description: str = None
    etag: str = None
    id: int = None
    primary_authorizer: str = None
    secondary_authorizer: str = None
    updated_at: str = None
class Bill(BaseModel):
    pass

class BillTheme(BaseModel):
    pass

class BillTheme_List(BaseModel):
    data: List[BillTheme]
class BillTheme_Show(BaseModel):
    data: BillTheme
class BillTheme_base(BaseModel):
    account_id: int = None
    config: str = None
    created_at: str = None
    default: bool = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class Bill_List(BaseModel):
    data: List[Bill]
class Bill_Show(BaseModel):
    data: Bill
class Bill_base(BaseModel):
    available_state_transitions: str = None
    balance: float = None
    can_update: bool = None
    created_at: str = None
    credits_issued: float = None
    discount_services_only: str = None
    due: float = None
    due_at: str = None
    end_at: str = None
    etag: str = None
    id: int = None
    issued_at: str = None
    kind: str = None
    last_sent_at: str = None
    memo: str = None
    number: str = None
    paid: float = None
    paid_at: str = None
    pending: float = None
    purchase_order: str = None
    secondary_tax_rate: float = None
    secondary_tax_sum: float = None
    secondary_taxable_sub_total: int = None
    services_secondary_tax: float = None
    services_secondary_taxable_sub_total: int = None
    services_sub_total: float = None
    services_tax: float = None
    services_taxable_sub_total: int = None
    shared: bool = None
    start_at: str = None
    state: str = None
    sub_total: float = None
    subject: str = None
    tax_rate: float = None
    tax_sum: float = None
    taxable_sub_total: int = None
    total: float = None
    total_tax: float = None
    type: str = None
    updated_at: str = None
class BillableClient(BaseModel):
    pass

class BillableClient_List(BaseModel):
    data: List[BillableClient]
class BillableClient_base(BaseModel):
    amount_in_trust: float = None
    billable_matters_count: int = None
    id: int = None
    name: str = None
    unbilled_amount: float = None
    unbilled_hours: float = None
class BillableMatter(BaseModel):
    pass

class BillableMatter_List(BaseModel):
    data: List[BillableMatter]
class BillableMatter_Show(BaseModel):
    data: BillableMatter
class BillableMatter_base(BaseModel):
    amount_in_trust: float = None
    display_number: str = None
    id: int = None
    unbilled_amount: float = None
    unbilled_hours: float = None
class BillingSetting(BaseModel):
    pass

class BillingSetting_Show(BaseModel):
    data: BillingSetting
class BillingSetting_base(BaseModel):
    apply_tax_by_default: bool = None
    created_at: str = None
    currency: str = None
    currency_sign: str = None
    etag: str = None
    id: int = None
    notify_after_bill_created: bool = None
    rounded_duration: float = None
    rounding: int = None
    secondary_tax_name: str = None
    secondary_tax_rate: float = None
    secondary_tax_rule: str = None
    tax_name: str = None
    tax_rate: float = None
    time_on_flat_rate_contingency_matters_is_non_billable: bool = None
    updated_at: str = None
    use_decimal_rounding: bool = None
    use_secondary_tax: bool = None
    use_utbms_codes: bool = None
class Calendar(BaseModel):
    pass

class CalendarEntry(BaseModel):
    pass

class CalendarEntryEventType(BaseModel):
    pass

class CalendarEntryEventType_base(BaseModel):
    color: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class CalendarEntry_List(BaseModel):
    data: List[CalendarEntry]
class CalendarEntry_Show(BaseModel):
    data: CalendarEntry
class CalendarEntry_base(BaseModel):
    all_day: bool = None
    calendar_owner_id: int = None
    court_rule: bool = None
    created_at: str = None
    description: str = None
    end_at: str = None
    etag: str = None
    id: str = None
    location: str = None
    parent_calendar_entry_id: int = None
    permission: str = None
    recurrence_rule: str = None
    start_at: str = None
    start_at_time_zone: str = None
    summary: str = None
    time_entries_count: int = None
    updated_at: str = None
class CalendarVisibility(BaseModel):
    pass

class CalendarVisibility_List(BaseModel):
    data: List[CalendarVisibility]
class CalendarVisibility_Show(BaseModel):
    data: CalendarVisibility
class CalendarVisibility_base(BaseModel):
    color: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    light_color: str = None
    name: str = None
    updated_at: str = None
    visible: bool = None
class Calendar_List(BaseModel):
    data: List[Calendar]
class Calendar_Show(BaseModel):
    data: Calendar
class Calendar_base(BaseModel):
    color: str = None
    court_rules_default_calendar: bool = None
    created_at: str = None
    etag: str = None
    id: int = None
    light_color: str = None
    name: str = None
    permission: str = None
    source: str = None
    type: str = None
    updated_at: str = None
    visible: bool = None
class CascadingTaskTemplate_base(BaseModel):
    id: int = None
    name: str = None
class Client(BaseModel):
    pass

class ClientPortal_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    unread_count: int = None
    unread_notifiable_count: int = None
    updated_at: str = None
class Client_Show(BaseModel):
    data: dict
class Client_base(BaseModel):
    client_connect_user_id: int = None
    created_at: str = None
    date_of_birth: str = None
    first_name: str = None
    id: int = None
    initials: str = None
    is_matter_client: bool = None
    last_name: str = None
    middle_name: str = None
    name: str = None
    prefix: str = None
    primary_email_address: str = None
    primary_phone_number: str = None
    title: str = None
    type: str = None
    updated_at: str = None
class ClioCreator_base(BaseModel):
    account_owner: bool = None
    clio_connect: bool = None
    court_rules_default_attendee: bool = None
    created_at: str = None
    default_calendar_id: int = None
    email: str = None
    enabled: bool = None
    etag: str = None
    first_name: str = None
    id: int = None
    initials: str = None
    last_name: str = None
    name: str = None
    phone_number: str = None
    rate: float = None
    roles: List[str] = None
    subscription_type: str = None
    time_zone: str = None
    type: str = None
    updated_at: str = None
class ClioPaymentsLink(BaseModel):
    pass

class ClioPaymentsLink_List(BaseModel):
    data: List[ClioPaymentsLink]
class ClioPaymentsLink_Show(BaseModel):
    data: ClioPaymentsLink
class ClioPaymentsLink_base(BaseModel):
    active: bool = None
    amount: float = None
    created_at: str = None
    currency: str = None
    description: str = None
    email_address: str = None
    etag: str = None
    expires_at: str = None
    id: int = None
    is_allocated_as_revenue: bool = None
    redirect_url: str = None
    url: str = None
class ClioPaymentsPayment(BaseModel):
    pass

class ClioPaymentsPayment_List(BaseModel):
    data: List[ClioPaymentsPayment]
class ClioPaymentsPayment_Show(BaseModel):
    data: ClioPaymentsPayment
class ClioPaymentsPayment_base(BaseModel):
    amount: float = None
    confirmation_number: str = None
    created_at: str = None
    currency: str = None
    deposit_as_revenue: bool = None
    description: str = None
    email_address: str = None
    id: int = None
    state: str = None
    updated_at: str = None
class Comment(BaseModel):
    pass

class Comment_List(BaseModel):
    data: List[Comment]
class Comment_Show(BaseModel):
    data: Comment
class Comment_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    message: str = None
    updated_at: str = None
class Communication(BaseModel):
    pass

class CommunicationEmlFile_base(BaseModel):
    id: int = None
class Communication_List(BaseModel):
    data: List[Communication]
class Communication_Show(BaseModel):
    data: Communication
class Communication_base(BaseModel):
    body: str = None
    created_at: str = None
    date: str = None
    etag: str = None
    id: int = None
    received_at: str = None
    subject: str = None
    time_entries_count: int = None
    type: str = None
    updated_at: str = None
class ConferenceMeeting_base(BaseModel):
    conference_id: int = None
    conference_password: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    join_url: str = None
    source_id: int = None
    type: str = None
    updated_at: str = None
class Contact(BaseModel):
    pass

class Contact_List(BaseModel):
    data: List[Contact]
class Contact_Show(BaseModel):
    data: dict
class Contact_base(BaseModel):
    client_connect_user_id: int = None
    clio_connect_email: str = None
    created_at: str = None
    date_of_birth: str = None
    etag: str = None
    first_name: str = None
    has_clio_for_clients_permission: bool = None
    id: int = None
    initials: str = None
    is_bill_recipient: bool = None
    is_client: bool = None
    is_clio_for_client_user: bool = None
    is_co_counsel: bool = None
    last_name: str = None
    ledes_client_id: str = None
    locked_clio_connect_email: bool = None
    middle_name: str = None
    name: str = None
    prefix: str = None
    primary_email_address: str = None
    primary_phone_number: str = None
    sales_tax_number: str = None
    secondary_email_address: str = None
    secondary_phone_number: str = None
    title: str = None
    type: str = None
    updated_at: str = None
class ContingencyFee_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    show_contingency_award: bool = None
    ed_at: str = None
class Conversation(BaseModel):
    pass

class ConversationMembership(BaseModel):
    pass

class ConversationMembership_base(BaseModel):
    archived: bool = None
    created_at: str = None
    etag: str = None
    id: int = None
    read: bool = None
    updated_at: str = None
class ConversationMessage(BaseModel):
    pass

class ConversationMessage_List(BaseModel):
    data: List[ConversationMessage]
class ConversationMessage_Show(BaseModel):
    data: ConversationMessage
class ConversationMessage_base(BaseModel):
    body: str = None
    created_at: str = None
    date: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class Conversation_List(BaseModel):
    data: List[Conversation]
class Conversation_Show(BaseModel):
    data: Conversation
class Conversation_base(BaseModel):
    archived: bool = None
    created_at: str = None
    current_user_is_member: bool = None
    etag: str = None
    id: int = None
    message_count: int = None
    read: bool = None
    read_only: bool = None
    subject: str = None
    time_entries_count: int = None
    updated_at: str = None
class CreditMemo(BaseModel):
    pass

class CreditMemo_List(BaseModel):
    data: List[CreditMemo]
class CreditMemo_Show(BaseModel):
    data: CreditMemo
class CreditMemo_base(BaseModel):
    amount: float = None
    created_at: str = None
    date: str = None
    description: str = None
    discount: bool = None
    etag: str = None
    id: int = None
    updated_at: str = None
    voided_at: str = None
class Currency(BaseModel):
    pass

class Currency_List(BaseModel):
    data: List[Currency]
class Currency_base(BaseModel):
    code: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    sign: str = None
    updated_at: str = None
class CustomAction(BaseModel):
    pass

class CustomAction_List(BaseModel):
    data: List[CustomAction]
class CustomAction_Show(BaseModel):
    data: CustomAction
class CustomAction_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    label: str = None
    target_url: str = None
    ui_reference: str = None
    updated_at: str = None
class CustomField(BaseModel):
    pass

class CustomFieldMatterSelection_base(BaseModel):
    display_number: str = None
    id: int = None
class CustomFieldSet(BaseModel):
    pass

class CustomFieldSetAssociation_base(BaseModel):
    created_at: str = None
    display_order: int = None
    etag: str = None
    id: int = None
    updated_at: str = None
class CustomFieldSet_List(BaseModel):
    data: List[CustomFieldSet]
class CustomFieldSet_Show(BaseModel):
    data: CustomFieldSet
class CustomFieldSet_base(BaseModel):
    created_at: str = None
    displayed: bool = None
    etag: str = None
    id: int = None
    name: str = None
    parent_type: str = None
    updated_at: str = None
class CustomFieldValue(BaseModel):
    pass

class CustomFieldValue_base(BaseModel):
    created_at: str = None
    etag: str = None
    field_display_order: int = None
    field_displayed: bool = None
    field_name: str = None
    field_required: bool = None
    field_type: str = None
    id: str = None
    soft_deleted: bool = None
    updated_at: str = None
    value: str = None
class CustomField_List(BaseModel):
    data: List[CustomField]
class CustomField_Show(BaseModel):
    data: CustomField
class CustomField_base(BaseModel):
    created_at: str = None
    deleted: bool = None
    display_order: int = None
    displayed: bool = None
    etag: str = None
    field_type: str = None
    id: int = None
    name: str = None
    parent_type: str = None
    required: bool = None
    updated_at: str = None
class Damage(BaseModel):
    pass

class Damage_List(BaseModel):
    data: List[Damage]
class Damage_Show(BaseModel):
    data: Damage
class Damage_base(BaseModel):
    amount: float = None
    created_at: str = None
    damage_type: str = None
    description: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class Discount_base(BaseModel):
    early_payment_period: int = None
    early_payment_rate: int = None
    note: str = None
    rate: float = None
    type: str = None
class Document(BaseModel):
    pass

class DocumentArchive(BaseModel):
    pass

class DocumentArchive_Show(BaseModel):
    data: DocumentArchive
class DocumentArchive_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    message: str = None
    progress: float = None
    size: int = None
    state: str = None
    updated_at: str = None
class DocumentAutomation(BaseModel):
    pass

class DocumentAutomation_List(BaseModel):
    data: List[DocumentAutomation]
class DocumentAutomation_Show(BaseModel):
    data: DocumentAutomation
class DocumentAutomation_base(BaseModel):
    created_at: str = None
    etag: str = None
    export_formats: str = None
    filename: str = None
    id: int = None
    state: str = None
    updated_at: str = None
class DocumentCategory(BaseModel):
    pass

class DocumentCategory_List(BaseModel):
    data: List[DocumentCategory]
class DocumentCategory_Show(BaseModel):
    data: DocumentCategory
class DocumentCategory_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class DocumentTemplate(BaseModel):
    pass

class DocumentTemplate_List(BaseModel):
    data: List[DocumentTemplate]
class DocumentTemplate_Show(BaseModel):
    data: DocumentTemplate
class DocumentTemplate_base(BaseModel):
    content_type: str = None
    created_at: str = None
    etag: str = None
    filename: str = None
    id: int = None
    size: int = None
    updated_at: str = None
class DocumentVersion(BaseModel):
    pass

class DocumentVersion_List(BaseModel):
    data: List[DocumentVersion]
class DocumentVersion_base(BaseModel):
    content_type: str = None
    created_at: str = None
    document_id: int = None
    etag: str = None
    filename: str = None
    fully_uploaded: bool = None
    id: int = None
    put_url: str = None
    received_at: str = None
    size: int = None
    updated_at: str = None
    uuid: str = None
    version_number: int = None
class Document_List(BaseModel):
    data: List[Document]
class Document_Show(BaseModel):
    data: dict
class Document_base(BaseModel):
    content_type: str = None
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    filename: str = None
    id: int = None
    locked: bool = None
    name: str = None
    received_at: str = None
    size: int = None
    type: str = None
    updated_at: str = None
class EmailAddress_base(BaseModel):
    address: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    primary: bool = None
    updated_at: str = None
class Error(BaseModel):
    error: ErrorDetail
class ErrorDetail(BaseModel):
    message: str    type: str
class EventMetrics(BaseModel):
    pass

class EventMetrics_Show(BaseModel):
    data: EventMetrics
class EventMetrics_base(BaseModel):
    unread_client_portal_messages: int = None
    unread_mobile_events: int = None
    unread_secure_messages: int = None
    unread_text_messages: int = None
    unread_web_events: int = None
class Event_base(BaseModel):
    description: str = None
    description_url: str = None
    etag: str = None
    icon: str = None
    id: int = None
    message: str = None
    mobile_icon: str = None
    occurred_at: str = None
    primary_detail: str = None
    primary_detail_url: str = None
    secondary_detail: str = None
    secondary_detail_url: str = None
    subject_id: int = None
    subject_type: str = None
    title: str = None
    title_url: str = None
class EvergreenRetainer_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    minimum_threshold: float = None
    updated_at: str = None
class ExpenseCategory(BaseModel):
    pass

class ExpenseCategory_List(BaseModel):
    data: List[ExpenseCategory]
class ExpenseCategory_Show(BaseModel):
    data: ExpenseCategory
class ExpenseCategory_base(BaseModel):
    accessible_to_user: bool = None
    created_at: str = None
    entry_type: str = None
    etag: str = None
    id: int = None
    name: str = None
    rate: int = None
    tax_setting: str = None
    updated_at: str = None
    xero_expense_code: str = None
class ExternalProperty_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
    value: str = None
class Folder(BaseModel):
    pass

class Folder_List(BaseModel):
    data: List[Folder]
class Folder_Show(BaseModel):
    data: Folder
class Folder_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    locked: bool = None
    name: str = None
    root: bool = None
    type: str = None
    updated_at: str = None
class Grant(BaseModel):
    pass

class GrantFundingSource(BaseModel):
    pass

class GrantFundingSource_List(BaseModel):
    data: List[GrantFundingSource]
class GrantFundingSource_Show(BaseModel):
    data: GrantFundingSource
class GrantFundingSource_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class Grant_List(BaseModel):
    data: List[Grant]
class Grant_Show(BaseModel):
    data: Grant
class Grant_base(BaseModel):
    balance: str = None
    created_at: str = None
    etag: str = None
    funding_code: str = None
    funding_code_and_name: str = None
    funding_source_name: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class Group(BaseModel):
    pass

class Group_List(BaseModel):
    data: List[Group]
class Group_Show(BaseModel):
    data: Group
class Group_base(BaseModel):
    client_connect_user: bool = None
    etag: str = None
    id: int = None
    name: str = None
    type: str = None
    updated_at: str = None
class InstantMessenger_base(BaseModel):
    address: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class InterestCharge(BaseModel):
    pass

class InterestCharge_List(BaseModel):
    data: List[InterestCharge]
class InterestCharge_base(BaseModel):
    created_at: str = None
    date: str = None
    description: str = None
    etag: str = None
    id: int = None
    total: float = None
    updated_at: str = None
class Interest_base(BaseModel):
    balance: float = None
    period: int = None
    rate: float = None
    total: float = None
    type: str = None
class Item(BaseModel):
    pass

class Item_List(BaseModel):
    data: List[Item]
class Item_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    locked: bool = None
    name: str = None
    type: str = None
    updated_at: str = None
class JobTitle_base(BaseModel):
    etag: str = None
    id: int = None
    initials: str = None
    name: str = None
class Jurisdiction(BaseModel):
    pass

class Jurisdiction_List(BaseModel):
    data: List[Jurisdiction]
class Jurisdiction_Show(BaseModel):
    data: Jurisdiction
class Jurisdiction_base(BaseModel):
    created_at: str = None
    default: bool = None
    description: str = None
    display_timezone: str = None
    etag: str = None
    id: int = None
    is_local_timezone: bool = None
    system_id: int = None
    updated_at: str = None
    valid_subscription: bool = None
class JurisdictionsToTrigger(BaseModel):
    pass

class JurisdictionsToTrigger_List(BaseModel):
    data: List[JurisdictionsToTrigger]
class JurisdictionsToTrigger_Show(BaseModel):
    data: JurisdictionsToTrigger
class JurisdictionsToTrigger_base(BaseModel):
    created_at: str = None
    description: str = None
    do_not_recalculate: bool = None
    etag: str = None
    id: int = None
    is_requirements_required: bool = None
    is_served: bool = None
    system_id: int = None
    updated_at: str = None
class LaukCivilCertificatedRate(BaseModel):
    pass

class LaukCivilCertificatedRate_List(BaseModel):
    data: List[LaukCivilCertificatedRate]
class LaukCivilCertificatedRate_base(BaseModel):
    activity: str = None
    activity_sub_category: str = None
    activity_type: str = None
    attended_several_hearings_for_multiple_clients: bool = None
    category_of_law: str = None
    change_of_solicitor: bool = None
    court: str = None
    created_at: str = None
    eligible_for_sqm: bool = None
    etag: str = None
    exceptional: float = None
    exceptional_warning: str = None
    fee: float = None
    fee_scheme: str = None
    first_conducting_solicitor: bool = None
    id: int = None
    key: str = None
    number_of_clients: str = None
    party: str = None
    post_transfer_clients_represented: str = None
    rate_type: str = None
    region: str = None
    session_type: str = None
    updated_at: str = None
    user_type: str = None
class LaukCivilControlledRate(BaseModel):
    pass

class LaukCivilControlledRate_List(BaseModel):
    data: List[LaukCivilControlledRate]
class LaukCivilControlledRate_base(BaseModel):
    activity: str = None
    activity_type: str = None
    category_of_law: str = None
    created_at: str = None
    etag: str = None
    exceptional: float = None
    fee: float = None
    fee_scheme: str = None
    id: int = None
    key: str = None
    rate_type: str = None
    region: str = None
    updated_at: str = None
class LaukCriminalControlledRate(BaseModel):
    pass

class LaukCriminalControlledRate_List(BaseModel):
    data: List[LaukCriminalControlledRate]
class LaukCriminalControlledRate_base(BaseModel):
    activity: str = None
    activity_type: str = None
    category_of_law: str = None
    counsel: str = None
    court: str = None
    created_at: str = None
    etag: str = None
    exceptional: float = None
    fee: float = None
    fee_scheme: str = None
    id: int = None
    key: str = None
    post_sept_22_exceptional: float = None
    post_sept_22_fee: float = None
    rate_type: str = None
    region: str = None
    solicitor_type: str = None
    updated_at: str = None
class LaukExpenseCategory(BaseModel):
    pass

class LaukExpenseCategory_List(BaseModel):
    data: List[LaukExpenseCategory]
class LaukExpenseCategory_base(BaseModel):
    certificated: bool = None
    civil: bool = None
    created_at: str = None
    criminal: bool = None
    etag: str = None
    id: int = None
    key: str = None
    name: str = None
    rate: float = None
    updated_at: str = None
class LegalAidUkBill_base(BaseModel):
    additional_travel_payment: bool = None
    adjourned_hearing_fee: str = None
    advice_time: int = None
    advocacy_costs: float = None
    bill_type: int = None
    case_concluded: str = None
    case_stage_level: int = None
    cla_exemption_code: str = None
    cla_reference: str = None
    cmrh_oral: int = None
    cmrh_telephone: int = None
    cost_of_counsel: str = None
    costs_are_those_of: int = None
    court_location: str = None
    date_of_claim: str = None
    designated_accredited_representative: int = None
    detention_travel_and_waiting_costs: str = None
    disbursements_vat: float = None
    exceptional_case_funding_reference: str = None
    exemption_criteria_satisfied: int = None
    follow_on_work: int = None
    ho_interview: int = None
    ho_ucn: int = None
    id: int = None
    independent_medical_reports_claimed: str = None
    jr_form_filling: str = None
    maat_id: str = None
    meetings_attended: int = None
    mht_ref_no: str = None
    net_disbursements: float = None
    net_profit_costs: float = None
    niat_disbursement_prior_authority_number: str = None
    number_of_attendances: int = None
    outcome_for_the_client: int = None
    prior_authority_reference: str = None
    profit_costs_ex_vat: int = None
    representation_order_date: str = None
    stage_reached: int = None
    substantive_hearing: int = None
    travel_and_waiting_costs: float = None
    travel_time: int = None
    value_of_costs: str = None
    waiting_time: int = None
class Lien_base(BaseModel):
    amount: float = None
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    lien_type: str = None
    mark_as_lien: bool = None
    updated_at: str = None
class LineItem(BaseModel):
    pass

class LineItemTotals_base(BaseModel):
    discount_percent: float = None
    price: float = None
    quantity: float = None
    sub_total: float = None
    total: float = None
class LineItem_List(BaseModel):
    data: List[LineItem]
class LineItem_Show(BaseModel):
    data: LineItem
class LineItem_base(BaseModel):
    created_at: str = None
    date: str = None
    description: str = None
    etag: str = None
    group_ordering: int = None
    id: int = None
    kind: str = None
    note: str = None
    price: float = None
    quantity: float = None
    secondary_tax: float = None
    secondary_taxable: bool = None
    sub_total: float = None
    tax: float = None
    taxable: bool = None
    total: float = None
    type: str = None
    updated_at: str = None
class LinkedFolder_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    locked: bool = None
    name: str = None
    root: bool = None
    type: str = None
    updated_at: str = None
class LogEntry(BaseModel):
    pass

class LogEntry_List(BaseModel):
    data: List[LogEntry]
class LogEntry_base(BaseModel):
    accessed_at: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    type: str = None
    updated_at: str = None
class Matter(BaseModel):
    pass

class MatterBalance_base(BaseModel):
    amount: float = None
    id: int = None
class MatterBillRecipient(BaseModel):
    pass

class MatterBillRecipient_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class MatterBudget_base(BaseModel):
    budget: float = None
    created_at: str = None
    etag: str = None
    id: int = None
    include_expenses: bool = None
    notification_threshold: int = None
    notify_users: bool = None
    updated_at: str = None
class MatterContacts(BaseModel):
    pass

class MatterContacts_List(BaseModel):
    data: List[MatterContacts]
class MatterContacts_base(BaseModel):
    client_connect_user_id: int = None
    contact_created_at: str = None
    contact_updated_at: str = None
    created_at: str = None
    description: str = None
    etag: str = None
    first_name: str = None
    id: int = None
    initials: str = None
    is_client: bool = None
    last_name: str = None
    matter_id: int = None
    matter_number: str = None
    middle_name: str = None
    name: str = None
    prefix: str = None
    primary_email_address: str = None
    primary_phone_number: str = None
    relationship_name: str = None
    secondary_email_address: str = None
    secondary_phone_number: str = None
    title: str = None
    type: str = None
    updated_at: str = None
class MatterCreatedWebhookEvent(BaseModel):
    event: str = None
    payload: dict = None
    timestamp: str = None
class MatterCustomRate(BaseModel):
    pass

class MatterCustomRate_base(BaseModel):
    on_invoice: bool = None
    type: str = None
class MatterDocket(BaseModel):
    pass

class MatterDocket_List(BaseModel):
    data: List[MatterDocket]
class MatterDocket_Show(BaseModel):
    data: MatterDocket
class MatterDocket_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    start_date: str = None
    start_time: str = None
    status: str = None
    updated_at: str = None
class MatterStage(BaseModel):
    pass

class MatterStage_List(BaseModel):
    data: List[MatterStage]
class MatterStage_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    order: int = None
    practice_area_id: str = None
    updated_at: str = None
class Matter_List(BaseModel):
    data: List[Matter]
class Matter_Show(BaseModel):
    data: dict
class Matter_base(BaseModel):
    billable: bool = None
    billing_method: str = None
    client_id: int = None
    client_reference: str = None
    close_date: str = None
    created_at: str = None
    custom_number: str = None
    description: str = None
    display_number: str = None
    etag: str = None
    has_tasks: bool = None
    id: int = None
    last_activity_date: str = None
    location: str = None
    maildrop_address: str = None
    matter_stage_updated_at: str = None
    number: int = None
    open_date: str = None
    pending_date: str = None
    shared: bool = None
    status: str = None
    updated_at: str = None
class MedicalBill(BaseModel):
    pass

class MedicalBill_Show(BaseModel):
    data: MedicalBill
class MedicalBill_base(BaseModel):
    adjustment: float = None
    amount: float = None
    bill_date: str = None
    bill_received_date: str = None
    created_at: str = None
    damage_type: str = None
    document_id: int = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class MedicalRecord(BaseModel):
    pass

class MedicalRecord_Show(BaseModel):
    data: MedicalRecord
class MedicalRecord_base(BaseModel):
    created_at: str = None
    document_id: int = None
    end_date: str = None
    etag: str = None
    id: int = None
    start_date: str = None
    updated_at: str = None
class MedicalRecordsRequest(BaseModel):
    pass

class MedicalRecordsRequest_List(BaseModel):
    data: List[MedicalRecordsRequest]
class MedicalRecordsRequest_Show(BaseModel):
    data: MedicalRecordsRequest
class MedicalRecordsRequest_base(BaseModel):
    bills_follow_up_date: str = None
    bills_request_date: str = None
    bills_status: str = None
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    in_treatment: bool = None
    records_follow_up_date: str = None
    records_request_date: str = None
    records_status: str = None
    treatment_end_date: str = None
    treatment_start_date: str = None
    updated_at: str = None
class Multipart(BaseModel):
    pass

class MultipartHeader_base(BaseModel):
    name: str = None
    value: str = None
class Multipart_base(BaseModel):
    part_number: int = None
    put_url: str = None
class MyEvent(BaseModel):
    pass

class MyEvent_List(BaseModel):
    data: List[MyEvent]
class MyEvent_Show(BaseModel):
    data: MyEvent
class MyEvent_base(BaseModel):
    pass

class Note(BaseModel):
    pass

class Note_List(BaseModel):
    data: List[Note]
class Note_Show(BaseModel):
    data: Note
class Note_base(BaseModel):
    created_at: str = None
    date: str = None
    detail: str = None
    etag: str = None
    id: int = None
    subject: str = None
    time_entries_count: int = None
    type: str = None
    updated_at: str = None
class NotificationEventSubscriber_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
    user_id: int = None
class NotificationMethod_base(BaseModel):
    created_at: str = None
    email_address: str = None
    etag: str = None
    id: int = None
    is_default_email_address: bool = None
    type: str = None
    updated_at: str = None
class OutstandingClientBalance(BaseModel):
    pass

class OutstandingClientBalance_List(BaseModel):
    data: List[OutstandingClientBalance]
class OutstandingClientBalance_base(BaseModel):
    associated_matter_ids: List[int] = None
    created_at: str = None
    etag: str = None
    id: int = None
    last_payment_date: str = None
    last_shared_date: str = None
    newest_issued_bill_due_date: str = None
    pending_payments_total: float = None
    reminders_enabled: bool = None
    total_outstanding_balance: float = None
    updated_at: str = None
class Participant(BaseModel):
    pass

class Participant_base(BaseModel):
    created_at: str = None
    enabled: bool = None
    etag: str = None
    id: int = None
    identifier: str = None
    initials: str = None
    job_title_name: str = None
    name: str = None
    secondary_identifier: str = None
    type: str = None
    updated_at: str = None
class PaymentProfile_base(BaseModel):
    billing_setting_id: int = None
    created_at: str = None
    discount_period: int = None
    discount_rate: float = None
    etag: str = None
    id: int = None
    interest_period: int = None
    interest_rate: float = None
    interest_type: str = None
    name: str = None
    terms: int = None
    updated_at: str = None
class PhoneNumber_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    number: str = None
    primary: bool = None
    updated_at: str = None
class PicklistOption(BaseModel):
    pass

class PicklistOption_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    option: str = None
    updated_at: str = None
class PolymorphicCustomRate(BaseModel):
    pass

class PolymorphicCustomRate_ActivityDescription_base(BaseModel):
    etag: str = None
    id: int = None
    name: str = None
class PolymorphicCustomRate_Group_base(BaseModel):
    etag: str = None
    id: int = None
    name: str = None
class PolymorphicCustomRate_User_base(BaseModel):
    enabled: bool = None
    etag: str = None
    id: int = None
    name: str = None
class PolymorphicCustomRate_base(BaseModel):
    award: float = None
    created_at: str = None
    date: str = None
    etag: str = None
    id: int = None
    note: str = None
    rate: float = None
    updated_at: str = None
class PolymorphicObject_base(BaseModel):
    id: int = None
    identifier: str = None
    secondary_identifier: str = None
    tertiary_identifier: str = None
    type: str = None
class PracticeArea(BaseModel):
    pass

class PracticeArea_List(BaseModel):
    data: List[PracticeArea]
class PracticeArea_Show(BaseModel):
    data: PracticeArea
class PracticeArea_base(BaseModel):
    category: str = None
    code: str = None
    created_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class RelatedContacts(BaseModel):
    pass

class RelatedContacts_List(BaseModel):
    data: List[RelatedContacts]
class RelatedContacts_base(BaseModel):
    client_connect_user_id: int = None
    contact_id: int = None
    created_at: str = None
    first_name: str = None
    id: int = None
    initials: str = None
    is_matter_client: bool = None
    last_name: str = None
    middle_name: str = None
    name: str = None
    prefix: str = None
    primary_email_address: str = None
    primary_phone_number: str = None
    title: str = None
    type: str = None
    updated_at: str = None
class Relationship(BaseModel):
    pass

class Relationship_List(BaseModel):
    data: List[Relationship]
class Relationship_Show(BaseModel):
    data: Relationship
class Relationship_base(BaseModel):
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class Reminder(BaseModel):
    pass

class ReminderTemplate_base(BaseModel):
    created_at: str = None
    duration: int = None
    etag: str = None
    id: int = None
    notification_type: str = None
    updated_at: str = None
class Reminder_List(BaseModel):
    data: List[Reminder]
class Reminder_Show(BaseModel):
    data: Reminder
class Reminder_base(BaseModel):
    created_at: str = None
    duration: int = None
    etag: str = None
    id: int = None
    next_delivery_at: str = None
    state: str = None
    updated_at: str = None
class Report(BaseModel):
    pass

class ReportPreset(BaseModel):
    pass

class ReportPreset_List(BaseModel):
    data: List[ReportPreset]
class ReportPreset_Show(BaseModel):
    data: ReportPreset
class ReportPreset_base(BaseModel):
    category: str = None
    created_at: str = None
    etag: str = None
    format: str = None
    id: int = None
    kind: str = None
    last_generated_at: str = None
    name: str = None
    options: str = None
    updated_at: str = None
class ReportSchedule(BaseModel):
    pass

class ReportSchedule_List(BaseModel):
    data: List[ReportSchedule]
class ReportSchedule_Show(BaseModel):
    data: ReportSchedule
class ReportSchedule_base(BaseModel):
    created_at: str = None
    day_of_month: int = None
    days_of_week: List[int] = None
    effective_from: str = None
    etag: str = None
    every_no_of_months: int = None
    frequency: str = None
    id: int = None
    next_scheduled_date: str = None
    report_preset_id: int = None
    status: str = None
    status_updated_at: str = None
    time_of_day: str = None
    time_zone: str = None
    updated_at: str = None
class Report_List(BaseModel):
    data: List[Report]
class Report_Show(BaseModel):
    data: Report
class Report_base(BaseModel):
    category: str = None
    created_at: str = None
    etag: str = None
    format: str = None
    id: int = None
    kind: str = None
    name: str = None
    progress: int = None
    source: str = None
    state: str = None
    updated_at: str = None
class ServiceType(BaseModel):
    pass

class ServiceType_List(BaseModel):
    data: List[ServiceType]
class ServiceType_Show(BaseModel):
    data: ServiceType
class ServiceType_base(BaseModel):
    created_at: str = None
    default: bool = None
    description: str = None
    etag: str = None
    id: int = None
    system_id: int = None
    updated_at: str = None
class StatuteOfLimitationsComputeRequest(BaseModel):
    date_of_incident: str
class StatuteOfLimitationsComputeResponse(BaseModel):
    due_at: str
class Task(BaseModel):
    pass

class TaskTemplate(BaseModel):
    pass

class TaskTemplateList(BaseModel):
    pass

class TaskTemplateListInstance_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class TaskTemplateList_List(BaseModel):
    data: List[TaskTemplateList]
class TaskTemplateList_Show(BaseModel):
    data: TaskTemplateList
class TaskTemplateList_base(BaseModel):
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    name: str = None
    templates_count: int = None
    updated_at: str = None
class TaskTemplate_Show(BaseModel):
    data: TaskTemplate
class TaskTemplate_base(BaseModel):
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    name: str = None
    priority: str = None
    private: bool = None
    updated_at: str = None
class TaskType(BaseModel):
    pass

class TaskType_List(BaseModel):
    data: List[TaskType]
class TaskType_Show(BaseModel):
    data: TaskType
class TaskType_base(BaseModel):
    created_at: str = None
    deleted_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class Task_List(BaseModel):
    data: List[Task]
class Task_Show(BaseModel):
    data: dict
class Task_base(BaseModel):
    completed_at: str = None
    created_at: str = None
    description: str = None
    due_at: str = None
    etag: str = None
    id: int = None
    name: str = None
    notify_completion: bool = None
    permission: str = None
    priority: str = None
    status: str = None
    statute_of_limitations: bool = None
    time_entries_count: int = None
    time_estimated: int = None
    updated_at: str = None
class TextSnippet(BaseModel):
    pass

class TextSnippet_List(BaseModel):
    data: List[TextSnippet]
class TextSnippet_Show(BaseModel):
    data: TextSnippet
class TextSnippet_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    phrase: str = None
    snippet: str = None
    updated_at: str = None
    whole_word: bool = None
class Timer(BaseModel):
    pass

class Timer_Show(BaseModel):
    data: Timer
class Timer_base(BaseModel):
    created_at: str = None
    elapsed_time: float = None
    etag: str = None
    id: int = None
    start_time: str = None
    updated_at: str = None
class TrustLineItem(BaseModel):
    pass

class TrustLineItem_List(BaseModel):
    data: List[TrustLineItem]
class TrustLineItem_Show(BaseModel):
    data: TrustLineItem
class TrustLineItem_base(BaseModel):
    created_at: str = None
    date: str = None
    etag: str = None
    id: int = None
    note: str = None
    total: float = None
    updated_at: str = None
class TrustRequest(BaseModel):
    pass

class TrustRequest_Show(BaseModel):
    data: TrustRequest
class TrustRequest_base(BaseModel):
    created_at: str = None
    etag: str = None
    id: int = None
    updated_at: str = None
class UnredactedParticipant_base(BaseModel):
    pass

class User(BaseModel):
    pass

class User_List(BaseModel):
    data: List[User]
class User_Show(BaseModel):
    data: dict
class User_base(BaseModel):
    account_owner: bool = None
    clio_connect: bool = None
    court_rules_default_attendee: bool = None
    created_at: str = None
    default_calendar_id: int = None
    email: str = None
    enabled: bool = None
    etag: str = None
    first_name: str = None
    id: int = None
    initials: str = None
    last_name: str = None
    name: str = None
    phone_number: str = None
    rate: float = None
    roles: List[str] = None
    subscription_type: str = None
    time_zone: str = None
    updated_at: str = None
class UtbmsCode(BaseModel):
    pass

class UtbmsCode_List(BaseModel):
    data: List[UtbmsCode]
class UtbmsCode_Show(BaseModel):
    data: UtbmsCode
class UtbmsCode_base(BaseModel):
    code: str = None
    created_at: str = None
    description: str = None
    etag: str = None
    id: int = None
    name: str = None
    type: str = None
    updated_at: str = None
    utbms_set_id: int = None
class UtbmsSet(BaseModel):
    pass

class UtbmsSet_List(BaseModel):
    data: List[UtbmsSet]
class UtbmsSet_base(BaseModel):
    created_at: str = None
    enabled: bool = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class WebSite_base(BaseModel):
    address: str = None
    created_at: str = None
    default_web_site: bool = None
    etag: str = None
    id: int = None
    name: str = None
    updated_at: str = None
class Webhook(BaseModel):
    pass

class Webhook_List(BaseModel):
    data: List[Webhook]
class Webhook_Show(BaseModel):
    data: Webhook
class Webhook_base(BaseModel):
    created_at: str = None
    etag: str = None
    events: List[str] = None
    expires_at: str = None
    fields: str = None
    id: int = None
    model: str = None
    shared_secret: str = None
    status: str = None
    updated_at: str = None
    url: str = None
