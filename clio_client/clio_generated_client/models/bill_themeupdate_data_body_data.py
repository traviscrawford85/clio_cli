from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillThemeupdateDataBodyData")


@_attrs_define
class BillThemeupdateDataBodyData:
    """
    Attributes:
        config (Union[Unset, str]): A string containing settings for the BillTheme.
            Values set in this string will apply to any bill using this BillTheme, unless overridden by the bill.

            Available settings within this string:
            - "show": Values set under this key determine how/if sections will appear on a bill.
            - "text": Values set under this key determine what will display if the section is shown.
            - "css": Values set under this key determine CSS rules for sections on a bill.

            Available settings under "show":
            - "client_account": Can be set to "hidden", "details", or "summary" to control the display and content of this
            section.
            - "client_account_details_balance_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "client_account_include_matter_transfers": Can be set to true/false to toggle displaying this section.
            - "client_account_matter_date_text_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_matter_details_description_text_header_alignment": Can be set to "center", "left", or "right"
            to control the alignment of this section.
            - "client_account_matter_title_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_matter_type_text_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_only_bill_matters": Can be set to true/false to toggle displaying this section.
            - "client_account_other_matters": Can be set to true/false to toggle displaying this section.
            - "client_account_payments_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_receipts_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_account_summary_balance_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "client_justification": Can be set to "center", "left", or "right" to control the justification of this
            section.
            - "client_operating_account_omit_balance": Can be set to true/false to toggle displaying this section.
            - "clio_payments_amount_body_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_amount_header_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "clio_payments_date_body_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_date_header_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_note_body_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_note_header_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_reference_body_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "clio_payments_reference_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "clio_payments_status_body_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "clio_payments_status_header_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "draft_watermark": Can be set to true/false to toggle displaying a draft watermark. Will only affect bills in
            draft.
            - "envelope_friendly": Can be set to true/false to toggle size styling for the bill.
            - "firm_address": Can be set to true/false to toggle displaying this section.
            - "firm_justification": Can be set to "center", "left", or "right" to control the justification of this section.
            - "firm_title": Can be set to true/false to toggle displaying this section.
            - "footer_invoice_memo": Can be set to true/false to toggle displaying this section.
            - "footer_invoice_payable": Can be set to true/false to toggle displaying this section.
            - "footer_justification": Can be set to "center", "left", or "right" to control the justification of this
            section.
            - "footer_page_numbers": Can be set to true/false to toggle displaying this section.
            - "header_invoice_issued_date": Can be set to true/false to toggle displaying this section.
            - "header_invoice_number": Can be set to true/false to toggle displaying this section.
            - "header_on_first_page": Can be set to true/false to toggle displaying this section.
            - "interest_date": Can be set to true/false to toggle displaying this section.
            - "interest_date_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "interest_date_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "interest_description": Can be set to true/false to toggle displaying this section.
            - "interest_details_description": Can be set to true/false to toggle displaying this section.
            - "interest_details_description_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "interest_details_description_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "interest_details_description_new_line": Can be set to true/false to toggle displaying a interest descriptions
            on a new line.
            - "interest_headings_order": Should be set to an array that contains the values: ["interest_type","
            interest_date", "interest_details_description", "interest_total"] in the order you would like the sections to
            display on your bills.
            - "interest_total": Can be set to true/false to toggle displaying this section.
            - "interest_total_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "interest_total_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "interest_totals_subtotal": Can be set to true/false to toggle displaying this section.
            - "interest_type": Can be set to true/false to toggle displaying this section.
            - "interest_type_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "interest_type_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "invoice_information_due_date": Can be set to true/false to toggle displaying this section.
            - "invoice_information_invoice_number": Can be set to true/false to toggle displaying this section.
            - "invoice_information_issue_date": Can be set to true/false to toggle displaying this section.
            - "invoice_title": Can be set to true/false to toggle displaying this section.
            - "logo": Can be set to true/false to toggle displaying this section.
            - "logo_justification": Can be set to "center", "left", or "right" to control the justification of this section.
            - "matter_attorney_display": Can be set to "name" or "initials" to control the content shown in this section.
            - "matter_attorney_initials": Can be set to true/false to toggle displaying this section.
            - "matter_attorney_initials_body_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "matter_attorney_initials_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_attorney_initials_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_attorney_initials_products": Can be set to true/false to toggle displaying this section.
            - "matter_attorney_summary_position_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_attorney_summary_time_keeper_header_alignment": Can be set to "center", "left", or "right" to control
            the alignment of this section.
            - "matter_client_ref": Can be set to true/false to toggle displaying this section.
            - "matter_date": Can be set to true/false to toggle displaying this section.
            - "matter_date_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_date_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_date_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_date_products": Can be set to true/false to toggle displaying this section.
            - "matter_date_trust": Can be set to true/false to toggle displaying this section.
            - "matter_description": Can be set to true/false to toggle displaying this section.
            - "matter_details_description": Can be set to true/false to toggle displaying this section.
            - "matter_details_description_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_details_description_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_details_description_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_details_description_new_line": Can be set to true/false to toggle displaying a matter descriptions on
            a new line.
            - "matter_details_description_products": Can be set to true/false to toggle displaying this section.
            - "matter_details_description_trust": Can be set to true/false to toggle displaying this section.
            - "matter_heading_justification": Can be set to "center", "left", or "right" to control the justification of
            this section.
            - "matter_headings_order": Should be set to an array that contains the values: ["matter_type",
            "matter_attorney_initials", "matter_date", "matter_details_description", "matter_quantity", "matter_rate",
            "matter_line_item_discount", "matter_total", "matter_total_with_tax", "matter_tax"]
            in the order you would like the sections to display on your bills.
            - "matter_headings_order_expenses": Should be set to an array that contains the values: ["matter_type",
            "matter_attorney_initials", "matter_date", "matter_details_description", "matter_quantity", "matter_rate",
            "matter_line_item_discount", "matter_total", "matter_total_with_tax", "matter_tax"]
            in the order you would like the sections to display on your bills.
            - "matter_headings_order_products": Should be set to an array that contains the values: ["matter_type",
            "matter_attorney_initials", "matter_date", "matter_details_description", "matter_quantity", "matter_rate",
            "matter_line_item_discount", "matter_total", "matter_total_with_tax", "matter_tax"]
            in the order you would like the sections to display on your bills.
            - "matter_headings_order_trust": Should be set to an array that contains the values: ["matter_date",
            "matter_details_description", "matter_total"] in the order you would like the sections to display on your bills.
            - "matter_individual_payments": Can be set to true/false to toggle displaying this section.
            - "matter_line_item_discount": Can be set to true/false to toggle displaying this section.
            - "matter_line_item_discount_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_line_item_discount_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_line_item_discount_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_line_item_discount_products": Can be set to true/false to toggle displaying this section.
            - "matter_line_item_discount_text_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "matter_line_items_activity_descriptions": Can be set to true/false to toggle displaying this section.
            - "matter_number": Can be set to true/false to toggle displaying this section.
            - "matter_quantity": Can be set to true/false to toggle displaying this section.
            - "matter_quantity_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_quantity_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_quantity_header_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "matter_quantity_products": Can be set to true/false to toggle displaying this section.
            - "matter_quantity_text_header_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "matter_rate": Can be set to true/false to toggle displaying this section.
            - "matter_rate_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_rate_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_rate_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_rate_products": Can be set to true/false to toggle displaying this section.
            - "matter_rate_text_header_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "matter_separate_line_items": Can be set to true/false to toggle displaying this section.
            - "matter_show_amount_with_percentage": Can be set to true/false to toggle displaying this section.
            - "matter_tax_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_tax_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_total": Can be set to true/false to toggle displaying this section.
            - "matter_total_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_total_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_total_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_total_products": Can be set to true/false to toggle displaying this section.
            - "matter_total_text_header_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "matter_total_trust": Can be set to true/false to toggle displaying this section.
            - "matter_total_with_tax_body_alignment": Can be set to "center", "left", or "right" to control the alignment of
            this section.
            - "matter_total_with_tax_header_alignment": Can be set to "center", "left", or "right" to control the alignment
            of this section.
            - "matter_totals_subtotal": Can be set to true/false to toggle displaying this section.
            - "matter_totals_subtotal_line_item_discount": Can be set to true/false to toggle displaying this section.
            - "matter_type": Can be set to true/false to toggle displaying this section.
            - "matter_type_body_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_type_expenses": Can be set to true/false to toggle displaying this section.
            - "matter_type_header_alignment": Can be set to "center", "left", or "right" to control the alignment of this
            section.
            - "matter_type_products": Can be set to true/false to toggle displaying this section.
            - "payment_profile_discount": Can be set to true/false to toggle displaying this section. Even if set to true,
            this section will not be shown if the bill does not have an early payment discount.
            - "payment_profile_grace_period": Can be set to true/false to toggle displaying this section. Even if set to
            true, this section will not be shown if the bill does not have a grace period.
            - "payment_profile_interest": Can be set to true/false to toggle displaying this section. Even if set to true,
            this section will not be shown if the bill does not have a recurring interest charge.
            - "payment_profile_no_grace_period": Can be set to true/false to toggle displaying this section. Even if set to
            true, this section will not be shown if the bill has a grace period.
            - "show_clio_payments": Can be set to true/false to toggle displaying this section.
            - "soa_title": Can be set to true/false to toggle displaying this section.
            - "statement_of_accounts": Can be set to true/false to toggle displaying this section.
            - "statement_of_accounts_amount_due_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "statement_of_accounts_amount_due_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "statement_of_accounts_balance_due_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "statement_of_accounts_balance_due_header_alignment": Can be set to "center", "left", or "right" to control
            the alignment of this section.
            - "statement_of_accounts_details": Can be set to true/false to toggle displaying this section.
            - "statement_of_accounts_due_on_body_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "statement_of_accounts_due_on_header_alignment": Can be set to "center", "left", or "right" to control the
            alignment of this section.
            - "statement_of_accounts_include_trust": Can be set to true/false to toggle displaying this section.
            - "statement_of_accounts_invoice_number_body_alignment": Can be set to "center", "left", or "right" to control
            the alignment of this section.
            - "statement_of_accounts_invoice_number_header_alignment": Can be set to "center", "left", or "right" to control
            the alignment of this section.
            - "statement_of_accounts_note": Can be set to true/false to toggle displaying this section. Even if set to true,
            this section will not be shown if "statement_of_accounts_summary" is "hidden".
            - "statement_of_accounts_payments_received_body_alignment": Can be set to "center", "left", or "right" to
            control the alignment of this section.
            - "statement_of_accounts_payments_received_header_alignment": Can be set to "center", "left", or "right" to
            control the alignment of this section.
            - "statement_of_accounts_summary": Can be set to "hidden", "above", or "below" to control the location of this
            section. This will determine if the statements of account section on the bill is displayed, and if it displays
            above or below the line items.
            - "statement_of_accounts_summary_detail": Can be set to "simple", "with_payment", or "with_account_balance" to
            control the values shown in this section.
            - "statement_of_accounts_summary_only_bill_matters": Can be set to true/false to control the values shown in
            this section.
            - "void_watermark": Can be set to true/false to toggle displaying a void watermark. Will only affect bills that
            have been void.


            Available settings under "text", each of these can be set to the text you would like to display when they are
            shown, some of these fields allow substituting values with codes wrapped in curly braces:
            - "address_email"
            - "address_fax"
            - "address_phone"
            - "vat_number_au"
            - "vat_number_eu"
            - "attorney_summary_position"
            - "attorney_summary_time_keeper"
            - "client_account_account"
            - "client_account_balance"
            - "client_account_payments"
            - "client_account_receipts"
            - "client_account_total_balance"
            - "clio_payments_amount"
            - "clio_payments_date"
            - "clio_payments_note"
            - "clio_payments_reference"
            - "clio_payments_status"
            - "clio_payments_title"
            - "clio_payments_total"
            - "discount_early_payment_balance_owing_text"
            - "discount_early_payment_end_date_text"
            - "discount_early_payment_text"
            - "discount_early_payment_total_text"
            - "footer_invoice_memo"
              - {{billing_setting_memo}}" can be used to reference your billing settings memo.
              - {{bill_memo}} can be used to reference your bills memo.
            - "footer_invoice_payable"
              - {{firm_name}} can be used to reference your firms name.
            - "footer_page"
            - "footer_page_of"
            - "grand_total_text"
              - {{same_as_total_heading}} can be used to reference the value in "text" => "matter_total_text"
            - "interest_date_text"
            - "interest_details_description_text"
            - "interest_subtotal_text"
            - "interest_text"
            - "interest_title_text"
            - "interest_total_text"
            - "interest_type_text"
            - "invoice_client_sales_tax_text"
            - "invoice_due_date_text"
            - "invoice_information_due_date_receipt_text"
            - "invoice_issued_date_text"
            - "invoice_lc"
            - "invoice_number_text"
            - "invoice_purchase_order_text"
            - "invoice_title"
            - "matter_attorney_initials_text"
            - "matter_balance_owing_text"
            - "matter_client_ref"
              - {{client_ref_num}}" can be used to reference the matters client reference.
            - "matter_credit_note_text"
            - "matter_date_text"
            - "matter_details_description_text"
            - "matter_discount_text"
            - "matter_expense_subtotal_text"
            - "matter_expense_text"
            - "matter_expense_title_text"
            - "matter_grand_total_text"
              - {{same_as_total_heading}} can be used to reference the value in "text" => "matter_total_text"
            - "matter_line_item_discount_expenses_text"
            - "matter_line_item_discount_products_text"client_address_custom"
            - "matter_line_item_discount_subtotal_text"
            - "matter_line_item_discount_text"
            - "matter_non_billable_expenses_title_text"
            - "matter_non_billable_grouped_title_text"
            - "matter_non_billable_products_title_text"
            - "matter_non_billable_services_title_text"
            - "matter_payment_text"
            - "matter_product_subtotal_text"
            - "matter_product_text"
            - "matter_product_title_text"
            - "matter_quantity_expenses_text"
            - "matter_quantity_products_text"
            - "matter_quantity_subtotal_text"
            - "matter_quantity_text"
            - "matter_quantity_total_text"
            - "matter_rate_expenses_text"
            - "matter_rate_products_text"
            - "matter_rate_text"
            - "matter_refund_text"
            - "matter_service_subtotal_text"
            - "matter_service_text"
            - "matter_service_title_text"
            - "matter_subtotal_text"
            - "matter_tax_text"
            - "matter_title"
            - "matter_total_text"
            - "matter_total_with_tax_text"
            - "matter_trust_line_items_title_text"
            - "matter_trust_text"
            - "matter_type_text"
            - "payment_profile"
            - "payment_profile_discount"
              - {{discount_rate}} can be used to reference the bills discount rate.
              - {{interest_rate}} can be used to reference the bills interest rate.
              - {{interest_type}} can be used to reference the bills interest type.
              - {{grace_period}} can be used to reference the grace period for the bill.
              - {{discount_period}} can be used to reference the discount period for the bill.
              - {{interest_period}} can be used to reference the interest period for the bill.
            - "payment_profile_grace_period"
              - {{discount_rate}} can be used to reference the bills discount rate.
              - {{interest_rate}} can be used to reference the bills interest rate.
              - {{interest_type}} can be used to reference the bills interest type.
              - {{grace_period}} can be used to reference the grace period for the bill.
              - {{discount_period}} can be used to reference the discount period for the bill.
              - {{interest_period}} can be used to reference the interest period for the bill.
            - "payment_profile_interest"
              - {{discount_rate}} can be used to reference the bills discount rate.
              - {{interest_rate}} can be used to reference the bills interest rate.
              - {{interest_type}} can be used to reference the bills interest type.
              - {{grace_period}} can be used to reference the grace period for the bill.
              - {{discount_period}} can be used to reference the discount period for the bill.
              - {{interest_period}} can be used to reference the interest period for the bill.
            - "payment_profile_no_grace_period"
              - {{discount_rate}} can be used to reference the bills discount rate.
              - {{interest_rate}} can be used to reference the bills interest rate.
              - {{interest_type}} can be used to reference the bills interest type.
              - {{grace_period}} can be used to reference the grace period for the bill.
              - {{discount_period}} can be used to reference the discount period for the bill.
              - {{interest_period}} can be used to reference the interest period for the bill.
            - "remittance_checks"
            - "remittance_checks_label"
            - "remittance_checks_title"
            - "remittance_note"
              - {{bill_number}} can be used to reference the bills number.
            - "remittance_note_soa"
            - "remittance_title"
            - "remittance_wire_bank_account"
            - "remittance_wire_bank_account_label"
            - "remittance_wire_bank_name"
            - "remittance_wire_bank_name_label"
            - "remittance_wire_bank_routing"
            - "remittance_wire_bank_routing_label"
            - "remittance_wire_bank_swift"
            - "remittance_wire_bank_swift_label"
            - "remittance_wire_title"
            - "soa_title"
            - "statement_of_accounts_amount"
            - "statement_of_accounts_amount_in_trust"
            - "statement_of_accounts_amount_on_account"
            - "statement_of_accounts_balance"
            - "statement_of_accounts_current_invoice"
            - "statement_of_accounts_details_title"
            - "statement_of_accounts_due_on"
            - "statement_of_accounts_invoice_number"
            - "statement_of_accounts_new_charges"
            - "statement_of_accounts_note"
              - {{firm_name}} can be used to reference your firms name.
            - "statement_of_accounts_original_invoice_number"
            - "statement_of_accounts_other_interest_invoices"
            - "statement_of_accounts_other_invoices"
            - "statement_of_accounts_outstanding_balance"
            - "statement_of_accounts_detailed_outstanding_balance"
            - "statement_of_accounts_payments"
            - "statement_of_accounts_summary_title"
            - "statement_of_accounts_total_balance"
            - "statement_of_accounts_total_credit"
            - "statement_of_accounts_total_outstanding_balance"
            - "statement_of_accounts_detailed_total_outstanding_balance"
            - "trust_request_adjustments_title_text"
            - "trust_request_lc"
            - "trust_request_number_text"
            - "trust_request_title"
            - "trust_request_total_text"


            Available settings under "css", each of these has nested values that can be set to apply CSS rules to bills:
            - "client"
              - "color": Color used in the client section. Value is in 'Hex'.
              - "font-family": Font used in client section.
              - "font-size": Font size in client section. Value is in 'em'.
            - "client_address"
              - "margin-bottom": Bottom margin size for the client address. Value is in 'em'.
            - "firm_title"
              - "margin-bottom": Bottom margin height for the bills firm title. Value is in 'em'.
              - "color": Color for the bills firm title section. Value is in 'Hex'.
              - "font-family": Font used for text in the firm title.
              - "font-size": Font size for the bills firm title. Value is in 'em'.
              - "border-color": Border color property for the firm title on a bill. Value is in 'Hex'.
              - "border-style": Border style property for the firm title on a bill. Accepts standard CSS options for
            'border-style' property.
              - "border-width": Border width property for table rows on a bill. Accepts standard CSS options for 'border-
            width' property.
              - "background-color": Background color for the firm title on a bill. Value is in 'Hex'.
            - "header"
              - "margin-bottom": Bottom margin size for the bill header. Value is in 'em'.
            - "inside_margins"
              - "font-family": Primary font used on the bill.
              - "font-size": Primary font size used for bill.
              - "color": Primary font used on the bill, default is "Arial".
            - "invoice_title"
              - "color": Color used in the invoice title section. Value is in 'Hex'.
              - "font-family": Font used in invoice title section.
              - "font-size": Font size in invoice title section. Value is in 'em'.
            - "logo_img"
              - "height": Height for the bills logo image. Value is in 'em'.
              - "margin-top": Top margin height for the bills logo image. Value is in 'em'.
              - "margin-bottom": Bottom margin height for the bills logo image. Value is in 'em'.
            - "matter_description"
              - "margin-top": Top margin size for matter description section. Value is in 'em'.
              - "color": Color used in the matter description section. Value is in 'Hex'.
              - "font-family": Font used in matter description section.
              - "font-size": Font size in matter description section. Value is in 'em'.
            - "matter_number"
              - "color": Color used in the matter number section. Value is in 'Hex'.
              - "font-family": Font used in matter number section.
              - "font-size": Font size in matter number section. Value is in 'em'.
            - "page_margins"
              - "margin-left": Left margin size for the bill. Value is in 'em'.
              - "margin-right": Right margin size for the bill. Value is in 'em'.
              - "margin-top": Top margin size for the bill. Value is in 'em'.
              - "margin-bottom": Bottom margin size for the bill. Value is in 'em'.
              - "size": Size property for the bill, default is "US-Letter".
            - "remittance_title"
              - "color": Color used in the remittance title section. Value is in 'Hex'.
              - "font-family": Font used in remittance title section.
              - "font-size": Font size in remittance title section. Value is in 'em'.
              - "background-color": Background color for the remittance title section on a bill. Value is in 'Hex'.
              - "border-color": Border color property for the remittance title section on a bill. Value is in 'Hex'.
              - "border-style": Border style property for the remittance title section on a bill. Accepts standard CSS
            options for 'border-style' property.
              - "border-width": Border width property for the remittance title section on a bill. Accepts standard CSS
            options for 'border-width' property.
            - "statement_of_accounts_title"
              - "color": Color used in the statement of accounts section. Value is in 'Hex'.
              - "font-family": Font used in statement of accounts section.
              - "font-size": Font size in statement of accounts section. Value is in 'em'.
              - "background-color": Background color for the statement of accounts section on a bill. Value is in 'Hex'.
              - "border-color": Border color property for the statement of accounts section on a bill. Value is in 'Hex'.
              - "border-style": Border style property for the statement of accounts section on a bill. Accepts standard CSS
            options for 'border-style' property.
              - "border-width": Border width property for the statement of accounts section on a bill. Accepts standard CSS
            options for 'border-width' property.
            - "table_even_line"
              - "background-color": Background color for even table rows. Value is in 'Hex'.
            - "table_h4"
              - "background-color": Background color for table headers. Value is in 'Hex'.
            - "table_line"
              - "border-bottom-width": Bottom border width for table rows. Value is in 'px'.
              - "border-bottom-style": Bottom border style property for table rows on a bill. Accepts standard CSS options
            for 'border-style' property.
              - "border-bottom-color": Bottom border color property for table rows on a bill. Value is in 'Hex'.
            - "table_odd_line"
              - "background-color": Background color for odd table rows. Value is in 'Hex'.


            A config with samples of each type of option is shown below:
            ```
              config = {
                "show": {
                    "statement_of_accounts_summary": "left"
                    "statement_of_accounts_note": true,
                    "footer_invoice_payable": true,
                    "footer_invoice_memo": true,
                    "payment_profile_no_grace_period": true,
                    "payment_profile_grace_period": true,
                    "payment_profile_discount": true,
                    "payment_profile_interest": true,
                    "interest_headings_order": ["interest_type"," interest_date", "interest_details_description",
            "interest_total"]
                  },
                "text": {
                    "statement_of_accounts_note": "Please make all amounts payable to: {{firm_name}}",
                    "footer_invoice_payable": "Please make all amounts payable to: {{firm_name}}",
                    "footer_invoice_memo": "{{bill_memo}}",
                    "payment_profile_no_grace_period": "Payment is due upon receipt.",
                    "payment_profile_grace_period": "Please pay within {{grace_period}}.",
                    "payment_profile_discount": "{{discount_rate}}% discount will be applied if payment is received within
            {{discount_period}}.",
                    "payment_profile_interest": "{{interest_rate}}% {{interest_type}} annual interest will be charged every
            {{interest_period}}.",
                  },
                "css": {
                  "statement_of_accounts_title": {
                    "color": "#00cc00",
                    "font-family": "Times New Roman",
                    "font-size": "0.875em",
                    "background-color": "#ccff99",
                    "border-color": "#0033ff",
                    "border-style": "dotted",
                    "border-width": "thick"
                  },
                  "remittance_title": {
                    "color": "#00ff00",
                    "background-color": "None",
                    "border-color": "#0033cc",
                    "border-width": "medium",
                    "border-style": "dotted",
                    "font-family": "Arial",
                    "font-size": "1.5em"
                  }
                }
              }
            ```
        name (Union[Unset, str]): Name of the BillTheme.
    """

    config: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        config = d.pop("config", UNSET)

        name = d.pop("name", UNSET)

        bill_themeupdate_data_body_data = cls(
            config=config,
            name=name,
        )

        bill_themeupdate_data_body_data.additional_properties = d
        return bill_themeupdate_data_body_data

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
