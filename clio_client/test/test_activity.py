
"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clio_sdk.models.activity import Activity


class TestActivity(unittest.TestCase):
    """Activity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Activity:
        """Test Activity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Activity`
        """
        model = Activity()
        if include_optional:
            return Activity(
                id = 56,
                etag = '',
                type = 'TimeEntry',
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                quantity_in_hours = 1.337,
                rounded_quantity_in_hours = 1.337,
                quantity = 1.337,
                rounded_quantity = 1.337,
                quantity_redacted = True,
                price = 1.337,
                note = '',
                flat_rate = True,
                billed = True,
                on_bill = True,
                total = 1.337,
                contingency_fee = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                reference = '',
                non_billable = True,
                non_billable_total = 1.337,
                no_charge = True,
                tax_setting = 'no_tax',
                currency = clio_sdk.models.currency_base.Currency_base(
                    id = 56, 
                    etag = '', 
                    code = '', 
                    sign = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                activity_description = clio_sdk.models.activity_description_base.ActivityDescription_base(
                    id = 56, 
                    etag = '', 
                    name = '', 
                    visible_to_co_counsel = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default = True, 
                    type = '', 
                    utbms_activity_id = 56, 
                    utbms_task_name = '', 
                    utbms_task_id = 56, 
                    xero_service_code = '', 
                    accessible_to_user = True, 
                    category_type = '', 
                    currency = clio_sdk.models.currency.currency(), ),
                expense_category = clio_sdk.models.expense_category_base.ExpenseCategory_base(
                    id = 56, 
                    etag = '', 
                    name = '', 
                    rate = 56, 
                    entry_type = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    xero_expense_code = '', 
                    accessible_to_user = True, 
                    tax_setting = '', 
                    currency = clio_sdk.models.currency.currency(), ),
                bill = clio_sdk.models.bill_base.Bill_base(
                    id = 56, 
                    etag = '', 
                    number = '', 
                    issued_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    due_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    tax_rate = 1.337, 
                    secondary_tax_rate = 1.337, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    subject = '', 
                    purchase_order = '', 
                    type = 'MatterBill', 
                    memo = '', 
                    start_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    end_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    balance = 1.337, 
                    state = 'draft', 
                    kind = 'revenue_kind', 
                    total = 1.337, 
                    paid = 1.337, 
                    paid_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    pending = 1.337, 
                    due = 1.337, 
                    discount_services_only = '', 
                    can_update = True, 
                    credits_issued = 1.337, 
                    shared = True, 
                    last_sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    services_secondary_tax = 1.337, 
                    services_sub_total = 1.337, 
                    services_tax = 1.337, 
                    services_taxable_sub_total = 56, 
                    services_secondary_taxable_sub_total = 56, 
                    taxable_sub_total = 56, 
                    secondary_taxable_sub_total = 56, 
                    sub_total = 1.337, 
                    tax_sum = 1.337, 
                    secondary_tax_sum = 1.337, 
                    total_tax = 1.337, 
                    available_state_transitions = [
                        'awaiting_approval'
                        ], ),
                communication = clio_sdk.models.communication_base.Communication_base(
                    id = 56, 
                    etag = '', 
                    subject = '', 
                    body = '', 
                    type = 'EmailCommunication', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    time_entries_count = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                client_portal = clio_sdk.models.client_portal_base.ClientPortal_base(
                    id = 56, 
                    etag = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    unread_count = 56, 
                    unread_notifiable_count = 56, ),
                matter = clio_sdk.models.matter_base.Matter_base(
                    id = 56, 
                    etag = '', 
                    number = 56, 
                    display_number = '', 
                    custom_number = '', 
                    currency = clio_sdk.models.currency.currency(), 
                    description = '', 
                    status = 'Pending', 
                    location = '', 
                    client_reference = '', 
                    client_id = 56, 
                    billable = True, 
                    maildrop_address = '', 
                    billing_method = 'flat', 
                    open_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    close_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    pending_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    shared = True, 
                    has_tasks = True, 
                    last_activity_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    matter_stage_updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                matter_note = clio_sdk.models.note_base.Note_base(
                    id = 56, 
                    etag = '', 
                    type = 'Matter', 
                    subject = '', 
                    detail = '', 
                    detail_text_type = 'plain_text', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_entries_count = 56, ),
                contact_note = clio_sdk.models.note_base.Note_base(
                    id = 56, 
                    etag = '', 
                    type = 'Matter', 
                    subject = '', 
                    detail = '', 
                    detail_text_type = 'plain_text', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    time_entries_count = 56, ),
                subject = clio_sdk.models.polymorphic_object_base.PolymorphicObject_base(
                    id = 56, 
                    type = 'Task', 
                    identifier = '', 
                    secondary_identifier = '', 
                    tertiary_identifier = '', ),
                timer = clio_sdk.models.timer_base.Timer_base(
                    id = 56, 
                    etag = '', 
                    start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    elapsed_time = 1.337, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                user = clio_sdk.models.user_base.User_base(
                    account_owner = True, 
                    clio_connect = True, 
                    court_rules_default_attendee = True, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    default_calendar_id = 56, 
                    email = '', 
                    enabled = True, 
                    etag = '', 
                    first_name = '', 
                    id = 56, 
                    initials = '', 
                    last_name = '', 
                    name = '', 
                    phone_number = '', 
                    rate = 1.337, 
                    roles = [
                        ''
                        ], 
                    subscription_type = 'Attorney', 
                    time_zone = '', 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                utbms_expense = clio_sdk.models.utbms_code_base.UtbmsCode_base(
                    id = 56, 
                    etag = '', 
                    name = '', 
                    code = '', 
                    description = '', 
                    type = 'UtbmsTask', 
                    utbms_set_id = 56, 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                vendor = clio_sdk.models.contact_base.Contact_base(
                    id = 56, 
                    etag = '', 
                    name = '', 
                    first_name = '', 
                    middle_name = '', 
                    last_name = '', 
                    date_of_birth = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    type = 'Company', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    prefix = '', 
                    title = '', 
                    initials = '', 
                    clio_connect_email = '', 
                    locked_clio_connect_email = True, 
                    client_connect_user_id = 56, 
                    primary_email_address = '', 
                    secondary_email_address = '', 
                    primary_phone_number = '', 
                    secondary_phone_number = '', 
                    ledes_client_id = '', 
                    has_clio_for_clients_permission = True, 
                    is_client = True, 
                    is_clio_for_client_user = True, 
                    is_co_counsel = True, 
                    is_bill_recipient = True, 
                    sales_tax_number = '', 
                    currency = clio_sdk.models.currency.currency(), ),
                calendar_entry = clio_sdk.models.activity_calendar_entry_base.Activity_CalendarEntry_base(
                    id = '', 
                    etag = '', 
                    calendar_owner_id = 56, ),
                task = clio_sdk.models.activity_task_base.Activity_Task_base(
                    id = 56, 
                    etag = '', ),
                text_message_conversation = clio_sdk.models.activity_text_message_conversation_base.Activity_TextMessageConversation_base(
                    id = 56, 
                    etag = '', ),
                document_version = clio_sdk.models.document_version_base.DocumentVersion_base(
                    id = 56, 
                    document_id = 56, 
                    etag = '', 
                    uuid = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    filename = '', 
                    size = 56, 
                    version_number = 56, 
                    content_type = '', 
                    received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    put_url = '', 
                    fully_uploaded = True, ),
                legal_aid_uk_activity = clio_sdk.models.legal_aid_uk_activity_base.LegalAidUkActivity_base(
                    activity_sub_category = '', 
                    advocacy = 56, 
                    base_rate = 1.337, 
                    bolt_ons = '', 
                    bolt_ons_summary = '', 
                    court = 56, 
                    eligible_for_sqm = True, 
                    expert = 56, 
                    form_of_civil_legal_service = 56, 
                    id = 56, 
                    is_custom_rate = True, 
                    json_key = '', 
                    region = 56, 
                    tax_exclusive = True, 
                    uplift = 1.337, 
                    user_type = 56, )
            )
        else:
            return Activity(
        )
        """

    def testActivity(self):
        """Test Activity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
