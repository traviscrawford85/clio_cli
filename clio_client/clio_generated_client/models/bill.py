import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bill_base_available_state_transitions_item import BillBaseAvailableStateTransitionsItem
from ..models.bill_base_kind import BillBaseKind
from ..models.bill_base_state import BillBaseState
from ..models.bill_base_type import BillBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_base import AddressBase
    from ..models.balance_base import BalanceBase
    from ..models.bank_account_base import BankAccountBase
    from ..models.bill_base import BillBase
    from ..models.bill_theme_base import BillThemeBase
    from ..models.billing_setting_base import BillingSettingBase
    from ..models.contact_base import ContactBase
    from ..models.currency_base import CurrencyBase
    from ..models.discount_base import DiscountBase
    from ..models.group_base import GroupBase
    from ..models.interest_base import InterestBase
    from ..models.legal_aid_uk_bill_base import LegalAidUkBillBase
    from ..models.matter_balance_base import MatterBalanceBase
    from ..models.matter_base import MatterBase
    from ..models.split_invoice_base import SplitInvoiceBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Bill")


@_attrs_define
class Bill:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Bill*
        etag (Union[Unset, str]): ETag for the *Bill*
        number (Union[Unset, str]): The *Bill* identifier (not necessarily numeric)'
        issued_at (Union[Unset, datetime.date]): The time the *Bill* was issued (as a ISO-8601 date)
        created_at (Union[Unset, datetime.datetime]): The time the *Bill* was created (as a ISO-8601 timestamp)
        due_at (Union[Unset, datetime.date]): The date the *Bill* is due (as a ISO-8601 date)
        tax_rate (Union[Unset, float]): The tax rate to the *Bill*
        secondary_tax_rate (Union[Unset, float]): A secondary tax rate applied to the *Bill*
        updated_at (Union[Unset, datetime.datetime]): The time the *Bill* was last updated (as a ISO-8601 timestamp)
        subject (Union[Unset, str]): The subject of the *Bill*
        purchase_order (Union[Unset, str]): The purchase order of the *Bill*
        type_ (Union[Unset, BillBaseType]): The type of the *Bill*
        memo (Union[Unset, str]): A memo for the *Bill*
        start_at (Union[Unset, datetime.date]): The time the billing period starts (as a ISO-8601 date)
        end_at (Union[Unset, datetime.date]): The time the billing period ends (as a ISO-8601 date)
        balance (Union[Unset, float]): The outstanding balance of the *Bill*
        state (Union[Unset, BillBaseState]): The billing state the *Bill* is in
        kind (Union[Unset, BillBaseKind]): The kind of the *Bill*
        total (Union[Unset, float]): The total with interest of the *Bill*
        paid (Union[Unset, float]): The total amount paid for the *Bill*
        paid_at (Union[Unset, datetime.datetime]): The date of the last payment on the *Bill*
        pending (Union[Unset, float]): The amount of pending credit card payments on the *Bill*
        due (Union[Unset, float]): The total amount of the *Bill* with interest and less discounts
        discount_services_only (Union[Unset, str]): The selected discount is applied to services only.
        can_update (Union[Unset, bool]): This value indicates if your *Bill*'s line items and information can be
            updated.
        credits_issued (Union[Unset, float]): The total credits issued for the *Bill*
        shared (Union[Unset, bool]): Whether the *Bill* is a shared
        last_sent_at (Union[Unset, datetime.datetime]): The last time the *Bill* was sent (as a ISO-8601 date)
        services_secondary_tax (Union[Unset, float]): The total secondary tax of the bill's line items of a service kind
        services_sub_total (Union[Unset, float]): The sub total of all the bill's line items of a service kind
        services_tax (Union[Unset, float]): The total tax of the bill's line items of a service kind
        services_taxable_sub_total (Union[Unset, int]): The services portion of the bill's primary tax
        services_secondary_taxable_sub_total (Union[Unset, int]): The services portion of the bill's secondary tax
        taxable_sub_total (Union[Unset, int]): The total taxable bill amount
        secondary_taxable_sub_total (Union[Unset, int]): The subtotal of the bill's secondary tax
        sub_total (Union[Unset, float]): Sub total for the *Bill*
        tax_sum (Union[Unset, float]): Sum of primary tax for the model
        secondary_tax_sum (Union[Unset, float]): Sum of secondary tax for the model
        total_tax (Union[Unset, float]): The total amount of tax for the bill.
        available_state_transitions (Union[Unset, list[BillBaseAvailableStateTransitionsItem]]): The available *Bill*
            state transitions.
        user (Union[Unset, UserBase]):
        client (Union[Unset, ContactBase]):
        discount (Union[Unset, DiscountBase]):
        interest (Union[Unset, InterestBase]):
        matters (Union[Unset, list['MatterBase']]): Matter
        group (Union[Unset, GroupBase]):
        bill_theme (Union[Unset, BillThemeBase]):
        original_bill (Union[Unset, BillBase]):
        destination_account (Union[Unset, BankAccountBase]):
        balances (Union[Unset, list['BalanceBase']]): Balance
        matter_totals (Union[Unset, list['MatterBalanceBase']]): MatterBalance
        currency (Union[Unset, CurrencyBase]):
        billing_setting (Union[Unset, BillingSettingBase]):
        client_addresses (Union[Unset, list['AddressBase']]): Address
        legal_aid_uk_bill (Union[Unset, LegalAidUkBillBase]):
        split_invoice (Union[Unset, SplitInvoiceBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    issued_at: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    due_at: Union[Unset, datetime.date] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    secondary_tax_rate: Union[Unset, float] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    subject: Union[Unset, str] = UNSET
    purchase_order: Union[Unset, str] = UNSET
    type_: Union[Unset, BillBaseType] = UNSET
    memo: Union[Unset, str] = UNSET
    start_at: Union[Unset, datetime.date] = UNSET
    end_at: Union[Unset, datetime.date] = UNSET
    balance: Union[Unset, float] = UNSET
    state: Union[Unset, BillBaseState] = UNSET
    kind: Union[Unset, BillBaseKind] = UNSET
    total: Union[Unset, float] = UNSET
    paid: Union[Unset, float] = UNSET
    paid_at: Union[Unset, datetime.datetime] = UNSET
    pending: Union[Unset, float] = UNSET
    due: Union[Unset, float] = UNSET
    discount_services_only: Union[Unset, str] = UNSET
    can_update: Union[Unset, bool] = UNSET
    credits_issued: Union[Unset, float] = UNSET
    shared: Union[Unset, bool] = UNSET
    last_sent_at: Union[Unset, datetime.datetime] = UNSET
    services_secondary_tax: Union[Unset, float] = UNSET
    services_sub_total: Union[Unset, float] = UNSET
    services_tax: Union[Unset, float] = UNSET
    services_taxable_sub_total: Union[Unset, int] = UNSET
    services_secondary_taxable_sub_total: Union[Unset, int] = UNSET
    taxable_sub_total: Union[Unset, int] = UNSET
    secondary_taxable_sub_total: Union[Unset, int] = UNSET
    sub_total: Union[Unset, float] = UNSET
    tax_sum: Union[Unset, float] = UNSET
    secondary_tax_sum: Union[Unset, float] = UNSET
    total_tax: Union[Unset, float] = UNSET
    available_state_transitions: Union[Unset, list[BillBaseAvailableStateTransitionsItem]] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    client: Union[Unset, "ContactBase"] = UNSET
    discount: Union[Unset, "DiscountBase"] = UNSET
    interest: Union[Unset, "InterestBase"] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    group: Union[Unset, "GroupBase"] = UNSET
    bill_theme: Union[Unset, "BillThemeBase"] = UNSET
    original_bill: Union[Unset, "BillBase"] = UNSET
    destination_account: Union[Unset, "BankAccountBase"] = UNSET
    balances: Union[Unset, list["BalanceBase"]] = UNSET
    matter_totals: Union[Unset, list["MatterBalanceBase"]] = UNSET
    currency: Union[Unset, "CurrencyBase"] = UNSET
    billing_setting: Union[Unset, "BillingSettingBase"] = UNSET
    client_addresses: Union[Unset, list["AddressBase"]] = UNSET
    legal_aid_uk_bill: Union[Unset, "LegalAidUkBillBase"] = UNSET
    split_invoice: Union[Unset, "SplitInvoiceBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        number = self.number

        issued_at: Union[Unset, str] = UNSET
        if not isinstance(self.issued_at, Unset):
            issued_at = self.issued_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        due_at: Union[Unset, str] = UNSET
        if not isinstance(self.due_at, Unset):
            due_at = self.due_at.isoformat()

        tax_rate = self.tax_rate

        secondary_tax_rate = self.secondary_tax_rate

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        subject = self.subject

        purchase_order = self.purchase_order

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        memo = self.memo

        start_at: Union[Unset, str] = UNSET
        if not isinstance(self.start_at, Unset):
            start_at = self.start_at.isoformat()

        end_at: Union[Unset, str] = UNSET
        if not isinstance(self.end_at, Unset):
            end_at = self.end_at.isoformat()

        balance = self.balance

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        kind: Union[Unset, str] = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        total = self.total

        paid = self.paid

        paid_at: Union[Unset, str] = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        pending = self.pending

        due = self.due

        discount_services_only = self.discount_services_only

        can_update = self.can_update

        credits_issued = self.credits_issued

        shared = self.shared

        last_sent_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_sent_at, Unset):
            last_sent_at = self.last_sent_at.isoformat()

        services_secondary_tax = self.services_secondary_tax

        services_sub_total = self.services_sub_total

        services_tax = self.services_tax

        services_taxable_sub_total = self.services_taxable_sub_total

        services_secondary_taxable_sub_total = self.services_secondary_taxable_sub_total

        taxable_sub_total = self.taxable_sub_total

        secondary_taxable_sub_total = self.secondary_taxable_sub_total

        sub_total = self.sub_total

        tax_sum = self.tax_sum

        secondary_tax_sum = self.secondary_tax_sum

        total_tax = self.total_tax

        available_state_transitions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.available_state_transitions, Unset):
            available_state_transitions = []
            for available_state_transitions_item_data in self.available_state_transitions:
                available_state_transitions_item = available_state_transitions_item_data.value
                available_state_transitions.append(available_state_transitions_item)

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        discount: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        interest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.interest, Unset):
            interest = self.interest.to_dict()

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        bill_theme: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill_theme, Unset):
            bill_theme = self.bill_theme.to_dict()

        original_bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.original_bill, Unset):
            original_bill = self.original_bill.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.balances, Unset):
            balances = []
            for balances_item_data in self.balances:
                balances_item = balances_item_data.to_dict()
                balances.append(balances_item)

        matter_totals: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matter_totals, Unset):
            matter_totals = []
            for matter_totals_item_data in self.matter_totals:
                matter_totals_item = matter_totals_item_data.to_dict()
                matter_totals.append(matter_totals_item)

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        billing_setting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.billing_setting, Unset):
            billing_setting = self.billing_setting.to_dict()

        client_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.client_addresses, Unset):
            client_addresses = []
            for client_addresses_item_data in self.client_addresses:
                client_addresses_item = client_addresses_item_data.to_dict()
                client_addresses.append(client_addresses_item)

        legal_aid_uk_bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal_aid_uk_bill, Unset):
            legal_aid_uk_bill = self.legal_aid_uk_bill.to_dict()

        split_invoice: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.split_invoice, Unset):
            split_invoice = self.split_invoice.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if number is not UNSET:
            field_dict["number"] = number
        if issued_at is not UNSET:
            field_dict["issued_at"] = issued_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if secondary_tax_rate is not UNSET:
            field_dict["secondary_tax_rate"] = secondary_tax_rate
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if subject is not UNSET:
            field_dict["subject"] = subject
        if purchase_order is not UNSET:
            field_dict["purchase_order"] = purchase_order
        if type_ is not UNSET:
            field_dict["type"] = type_
        if memo is not UNSET:
            field_dict["memo"] = memo
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if balance is not UNSET:
            field_dict["balance"] = balance
        if state is not UNSET:
            field_dict["state"] = state
        if kind is not UNSET:
            field_dict["kind"] = kind
        if total is not UNSET:
            field_dict["total"] = total
        if paid is not UNSET:
            field_dict["paid"] = paid
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if pending is not UNSET:
            field_dict["pending"] = pending
        if due is not UNSET:
            field_dict["due"] = due
        if discount_services_only is not UNSET:
            field_dict["discount_services_only"] = discount_services_only
        if can_update is not UNSET:
            field_dict["can_update"] = can_update
        if credits_issued is not UNSET:
            field_dict["credits_issued"] = credits_issued
        if shared is not UNSET:
            field_dict["shared"] = shared
        if last_sent_at is not UNSET:
            field_dict["last_sent_at"] = last_sent_at
        if services_secondary_tax is not UNSET:
            field_dict["services_secondary_tax"] = services_secondary_tax
        if services_sub_total is not UNSET:
            field_dict["services_sub_total"] = services_sub_total
        if services_tax is not UNSET:
            field_dict["services_tax"] = services_tax
        if services_taxable_sub_total is not UNSET:
            field_dict["services_taxable_sub_total"] = services_taxable_sub_total
        if services_secondary_taxable_sub_total is not UNSET:
            field_dict["services_secondary_taxable_sub_total"] = services_secondary_taxable_sub_total
        if taxable_sub_total is not UNSET:
            field_dict["taxable_sub_total"] = taxable_sub_total
        if secondary_taxable_sub_total is not UNSET:
            field_dict["secondary_taxable_sub_total"] = secondary_taxable_sub_total
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total
        if tax_sum is not UNSET:
            field_dict["tax_sum"] = tax_sum
        if secondary_tax_sum is not UNSET:
            field_dict["secondary_tax_sum"] = secondary_tax_sum
        if total_tax is not UNSET:
            field_dict["total_tax"] = total_tax
        if available_state_transitions is not UNSET:
            field_dict["available_state_transitions"] = available_state_transitions
        if user is not UNSET:
            field_dict["user"] = user
        if client is not UNSET:
            field_dict["client"] = client
        if discount is not UNSET:
            field_dict["discount"] = discount
        if interest is not UNSET:
            field_dict["interest"] = interest
        if matters is not UNSET:
            field_dict["matters"] = matters
        if group is not UNSET:
            field_dict["group"] = group
        if bill_theme is not UNSET:
            field_dict["bill_theme"] = bill_theme
        if original_bill is not UNSET:
            field_dict["original_bill"] = original_bill
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if balances is not UNSET:
            field_dict["balances"] = balances
        if matter_totals is not UNSET:
            field_dict["matter_totals"] = matter_totals
        if currency is not UNSET:
            field_dict["currency"] = currency
        if billing_setting is not UNSET:
            field_dict["billing_setting"] = billing_setting
        if client_addresses is not UNSET:
            field_dict["client_addresses"] = client_addresses
        if legal_aid_uk_bill is not UNSET:
            field_dict["legal_aid_uk_bill"] = legal_aid_uk_bill
        if split_invoice is not UNSET:
            field_dict["split_invoice"] = split_invoice

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_base import AddressBase
        from ..models.balance_base import BalanceBase
        from ..models.bank_account_base import BankAccountBase
        from ..models.bill_base import BillBase
        from ..models.bill_theme_base import BillThemeBase
        from ..models.billing_setting_base import BillingSettingBase
        from ..models.contact_base import ContactBase
        from ..models.currency_base import CurrencyBase
        from ..models.discount_base import DiscountBase
        from ..models.group_base import GroupBase
        from ..models.interest_base import InterestBase
        from ..models.legal_aid_uk_bill_base import LegalAidUkBillBase
        from ..models.matter_balance_base import MatterBalanceBase
        from ..models.matter_base import MatterBase
        from ..models.split_invoice_base import SplitInvoiceBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        number = d.pop("number", UNSET)

        _issued_at = d.pop("issued_at", UNSET)
        issued_at: Union[Unset, datetime.date]
        if isinstance(_issued_at, Unset):
            issued_at = UNSET
        else:
            issued_at = isoparse(_issued_at).date()

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _due_at = d.pop("due_at", UNSET)
        due_at: Union[Unset, datetime.date]
        if isinstance(_due_at, Unset):
            due_at = UNSET
        else:
            due_at = isoparse(_due_at).date()

        tax_rate = d.pop("tax_rate", UNSET)

        secondary_tax_rate = d.pop("secondary_tax_rate", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        subject = d.pop("subject", UNSET)

        purchase_order = d.pop("purchase_order", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BillBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillBaseType(_type_)

        memo = d.pop("memo", UNSET)

        _start_at = d.pop("start_at", UNSET)
        start_at: Union[Unset, datetime.date]
        if isinstance(_start_at, Unset):
            start_at = UNSET
        else:
            start_at = isoparse(_start_at).date()

        _end_at = d.pop("end_at", UNSET)
        end_at: Union[Unset, datetime.date]
        if isinstance(_end_at, Unset):
            end_at = UNSET
        else:
            end_at = isoparse(_end_at).date()

        balance = d.pop("balance", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BillBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BillBaseState(_state)

        _kind = d.pop("kind", UNSET)
        kind: Union[Unset, BillBaseKind]
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = BillBaseKind(_kind)

        total = d.pop("total", UNSET)

        paid = d.pop("paid", UNSET)

        _paid_at = d.pop("paid_at", UNSET)
        paid_at: Union[Unset, datetime.datetime]
        if isinstance(_paid_at, Unset):
            paid_at = UNSET
        else:
            paid_at = isoparse(_paid_at)

        pending = d.pop("pending", UNSET)

        due = d.pop("due", UNSET)

        discount_services_only = d.pop("discount_services_only", UNSET)

        can_update = d.pop("can_update", UNSET)

        credits_issued = d.pop("credits_issued", UNSET)

        shared = d.pop("shared", UNSET)

        _last_sent_at = d.pop("last_sent_at", UNSET)
        last_sent_at: Union[Unset, datetime.datetime]
        if isinstance(_last_sent_at, Unset):
            last_sent_at = UNSET
        else:
            last_sent_at = isoparse(_last_sent_at)

        services_secondary_tax = d.pop("services_secondary_tax", UNSET)

        services_sub_total = d.pop("services_sub_total", UNSET)

        services_tax = d.pop("services_tax", UNSET)

        services_taxable_sub_total = d.pop("services_taxable_sub_total", UNSET)

        services_secondary_taxable_sub_total = d.pop("services_secondary_taxable_sub_total", UNSET)

        taxable_sub_total = d.pop("taxable_sub_total", UNSET)

        secondary_taxable_sub_total = d.pop("secondary_taxable_sub_total", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        tax_sum = d.pop("tax_sum", UNSET)

        secondary_tax_sum = d.pop("secondary_tax_sum", UNSET)

        total_tax = d.pop("total_tax", UNSET)

        available_state_transitions = []
        _available_state_transitions = d.pop("available_state_transitions", UNSET)
        for available_state_transitions_item_data in _available_state_transitions or []:
            available_state_transitions_item = BillBaseAvailableStateTransitionsItem(
                available_state_transitions_item_data
            )

            available_state_transitions.append(available_state_transitions_item)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        _client = d.pop("client", UNSET)
        client: Union[Unset, ContactBase]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ContactBase.from_dict(_client)

        _discount = d.pop("discount", UNSET)
        discount: Union[Unset, DiscountBase]
        if isinstance(_discount, Unset):
            discount = UNSET
        else:
            discount = DiscountBase.from_dict(_discount)

        _interest = d.pop("interest", UNSET)
        interest: Union[Unset, InterestBase]
        if isinstance(_interest, Unset):
            interest = UNSET
        else:
            interest = InterestBase.from_dict(_interest)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        _group = d.pop("group", UNSET)
        group: Union[Unset, GroupBase]
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GroupBase.from_dict(_group)

        _bill_theme = d.pop("bill_theme", UNSET)
        bill_theme: Union[Unset, BillThemeBase]
        if isinstance(_bill_theme, Unset):
            bill_theme = UNSET
        else:
            bill_theme = BillThemeBase.from_dict(_bill_theme)

        _original_bill = d.pop("original_bill", UNSET)
        original_bill: Union[Unset, BillBase]
        if isinstance(_original_bill, Unset):
            original_bill = UNSET
        else:
            original_bill = BillBase.from_dict(_original_bill)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, BankAccountBase]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = BankAccountBase.from_dict(_destination_account)

        balances = []
        _balances = d.pop("balances", UNSET)
        for balances_item_data in _balances or []:
            balances_item = BalanceBase.from_dict(balances_item_data)

            balances.append(balances_item)

        matter_totals = []
        _matter_totals = d.pop("matter_totals", UNSET)
        for matter_totals_item_data in _matter_totals or []:
            matter_totals_item = MatterBalanceBase.from_dict(matter_totals_item_data)

            matter_totals.append(matter_totals_item)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, CurrencyBase]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = CurrencyBase.from_dict(_currency)

        _billing_setting = d.pop("billing_setting", UNSET)
        billing_setting: Union[Unset, BillingSettingBase]
        if isinstance(_billing_setting, Unset):
            billing_setting = UNSET
        else:
            billing_setting = BillingSettingBase.from_dict(_billing_setting)

        client_addresses = []
        _client_addresses = d.pop("client_addresses", UNSET)
        for client_addresses_item_data in _client_addresses or []:
            client_addresses_item = AddressBase.from_dict(client_addresses_item_data)

            client_addresses.append(client_addresses_item)

        _legal_aid_uk_bill = d.pop("legal_aid_uk_bill", UNSET)
        legal_aid_uk_bill: Union[Unset, LegalAidUkBillBase]
        if isinstance(_legal_aid_uk_bill, Unset):
            legal_aid_uk_bill = UNSET
        else:
            legal_aid_uk_bill = LegalAidUkBillBase.from_dict(_legal_aid_uk_bill)

        _split_invoice = d.pop("split_invoice", UNSET)
        split_invoice: Union[Unset, SplitInvoiceBase]
        if isinstance(_split_invoice, Unset):
            split_invoice = UNSET
        else:
            split_invoice = SplitInvoiceBase.from_dict(_split_invoice)

        bill = cls(
            id=id,
            etag=etag,
            number=number,
            issued_at=issued_at,
            created_at=created_at,
            due_at=due_at,
            tax_rate=tax_rate,
            secondary_tax_rate=secondary_tax_rate,
            updated_at=updated_at,
            subject=subject,
            purchase_order=purchase_order,
            type_=type_,
            memo=memo,
            start_at=start_at,
            end_at=end_at,
            balance=balance,
            state=state,
            kind=kind,
            total=total,
            paid=paid,
            paid_at=paid_at,
            pending=pending,
            due=due,
            discount_services_only=discount_services_only,
            can_update=can_update,
            credits_issued=credits_issued,
            shared=shared,
            last_sent_at=last_sent_at,
            services_secondary_tax=services_secondary_tax,
            services_sub_total=services_sub_total,
            services_tax=services_tax,
            services_taxable_sub_total=services_taxable_sub_total,
            services_secondary_taxable_sub_total=services_secondary_taxable_sub_total,
            taxable_sub_total=taxable_sub_total,
            secondary_taxable_sub_total=secondary_taxable_sub_total,
            sub_total=sub_total,
            tax_sum=tax_sum,
            secondary_tax_sum=secondary_tax_sum,
            total_tax=total_tax,
            available_state_transitions=available_state_transitions,
            user=user,
            client=client,
            discount=discount,
            interest=interest,
            matters=matters,
            group=group,
            bill_theme=bill_theme,
            original_bill=original_bill,
            destination_account=destination_account,
            balances=balances,
            matter_totals=matter_totals,
            currency=currency,
            billing_setting=billing_setting,
            client_addresses=client_addresses,
            legal_aid_uk_bill=legal_aid_uk_bill,
            split_invoice=split_invoice,
        )

        bill.additional_properties = d
        return bill

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
