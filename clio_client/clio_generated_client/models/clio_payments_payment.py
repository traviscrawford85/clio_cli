import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.clio_payments_payment_base_state import ClioPaymentsPaymentBaseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_base import AllocationBase
    from ..models.bank_account_base import BankAccountBase
    from ..models.bank_transaction_base import BankTransactionBase
    from ..models.bill_base import BillBase
    from ..models.clio_payments_link_base import ClioPaymentsLinkBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="ClioPaymentsPayment")


@_attrs_define
class ClioPaymentsPayment:
    """
    Attributes:
        amount (Union[Unset, float]): The amount of the payment.
        confirmation_number (Union[Unset, str]): The confirmation number of the payment.
        created_at (Union[Unset, datetime.datetime]): The time the *ClioPaymentsPayment* was created (as a ISO-8601
            timestamp)
        currency (Union[Unset, str]): The currency the payment was processed in.
        deposit_as_revenue (Union[Unset, bool]): Whether the payment was deposited as revenue.
        description (Union[Unset, str]): The description of the payment.
        email_address (Union[Unset, str]): The email address of the client.
        id (Union[Unset, int]): Unique identifier for the *ClioPaymentsPayment*
        state (Union[Unset, ClioPaymentsPaymentBaseState]): The state of the payment (authorized, completed, failed,
            etc).
        updated_at (Union[Unset, datetime.datetime]): The time the *ClioPaymentsPayment* was last updated (as a ISO-8601
            timestamp)
        bank_transaction (Union[Unset, BankTransactionBase]):
        clio_payments_link (Union[Unset, ClioPaymentsLinkBase]):
        contact (Union[Unset, ContactBase]):
        destination_account (Union[Unset, BankAccountBase]):
        user (Union[Unset, UserBase]):
        allocations (Union[Unset, list['AllocationBase']]): Allocation
        bills (Union[Unset, list['BillBase']]): Bill
        matters (Union[Unset, list['MatterBase']]): Matter
    """

    amount: Union[Unset, float] = UNSET
    confirmation_number: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    deposit_as_revenue: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    state: Union[Unset, ClioPaymentsPaymentBaseState] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    bank_transaction: Union[Unset, "BankTransactionBase"] = UNSET
    clio_payments_link: Union[Unset, "ClioPaymentsLinkBase"] = UNSET
    contact: Union[Unset, "ContactBase"] = UNSET
    destination_account: Union[Unset, "BankAccountBase"] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    allocations: Union[Unset, list["AllocationBase"]] = UNSET
    bills: Union[Unset, list["BillBase"]] = UNSET
    matters: Union[Unset, list["MatterBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        confirmation_number = self.confirmation_number

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        currency = self.currency

        deposit_as_revenue = self.deposit_as_revenue

        description = self.description

        email_address = self.email_address

        id = self.id

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        bank_transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_transaction, Unset):
            bank_transaction = self.bank_transaction.to_dict()

        clio_payments_link: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clio_payments_link, Unset):
            clio_payments_link = self.clio_payments_link.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        destination_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.destination_account, Unset):
            destination_account = self.destination_account.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        allocations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allocations, Unset):
            allocations = []
            for allocations_item_data in self.allocations:
                allocations_item = allocations_item_data.to_dict()
                allocations.append(allocations_item)

        bills: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.bills, Unset):
            bills = []
            for bills_item_data in self.bills:
                bills_item = bills_item_data.to_dict()
                bills.append(bills_item)

        matters: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.matters, Unset):
            matters = []
            for matters_item_data in self.matters:
                matters_item = matters_item_data.to_dict()
                matters.append(matters_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if confirmation_number is not UNSET:
            field_dict["confirmation_number"] = confirmation_number
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if deposit_as_revenue is not UNSET:
            field_dict["deposit_as_revenue"] = deposit_as_revenue
        if description is not UNSET:
            field_dict["description"] = description
        if email_address is not UNSET:
            field_dict["email_address"] = email_address
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bank_transaction is not UNSET:
            field_dict["bank_transaction"] = bank_transaction
        if clio_payments_link is not UNSET:
            field_dict["clio_payments_link"] = clio_payments_link
        if contact is not UNSET:
            field_dict["contact"] = contact
        if destination_account is not UNSET:
            field_dict["destination_account"] = destination_account
        if user is not UNSET:
            field_dict["user"] = user
        if allocations is not UNSET:
            field_dict["allocations"] = allocations
        if bills is not UNSET:
            field_dict["bills"] = bills
        if matters is not UNSET:
            field_dict["matters"] = matters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_base import AllocationBase
        from ..models.bank_account_base import BankAccountBase
        from ..models.bank_transaction_base import BankTransactionBase
        from ..models.bill_base import BillBase
        from ..models.clio_payments_link_base import ClioPaymentsLinkBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        confirmation_number = d.pop("confirmation_number", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        currency = d.pop("currency", UNSET)

        deposit_as_revenue = d.pop("deposit_as_revenue", UNSET)

        description = d.pop("description", UNSET)

        email_address = d.pop("email_address", UNSET)

        id = d.pop("id", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, ClioPaymentsPaymentBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = ClioPaymentsPaymentBaseState(_state)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _bank_transaction = d.pop("bank_transaction", UNSET)
        bank_transaction: Union[Unset, BankTransactionBase]
        if isinstance(_bank_transaction, Unset):
            bank_transaction = UNSET
        else:
            bank_transaction = BankTransactionBase.from_dict(_bank_transaction)

        _clio_payments_link = d.pop("clio_payments_link", UNSET)
        clio_payments_link: Union[Unset, ClioPaymentsLinkBase]
        if isinstance(_clio_payments_link, Unset):
            clio_payments_link = UNSET
        else:
            clio_payments_link = ClioPaymentsLinkBase.from_dict(_clio_payments_link)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactBase]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactBase.from_dict(_contact)

        _destination_account = d.pop("destination_account", UNSET)
        destination_account: Union[Unset, BankAccountBase]
        if isinstance(_destination_account, Unset):
            destination_account = UNSET
        else:
            destination_account = BankAccountBase.from_dict(_destination_account)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        allocations = []
        _allocations = d.pop("allocations", UNSET)
        for allocations_item_data in _allocations or []:
            allocations_item = AllocationBase.from_dict(allocations_item_data)

            allocations.append(allocations_item)

        bills = []
        _bills = d.pop("bills", UNSET)
        for bills_item_data in _bills or []:
            bills_item = BillBase.from_dict(bills_item_data)

            bills.append(bills_item)

        matters = []
        _matters = d.pop("matters", UNSET)
        for matters_item_data in _matters or []:
            matters_item = MatterBase.from_dict(matters_item_data)

            matters.append(matters_item)

        clio_payments_payment = cls(
            amount=amount,
            confirmation_number=confirmation_number,
            created_at=created_at,
            currency=currency,
            deposit_as_revenue=deposit_as_revenue,
            description=description,
            email_address=email_address,
            id=id,
            state=state,
            updated_at=updated_at,
            bank_transaction=bank_transaction,
            clio_payments_link=clio_payments_link,
            contact=contact,
            destination_account=destination_account,
            user=user,
            allocations=allocations,
            bills=bills,
            matters=matters,
        )

        clio_payments_payment.additional_properties = d
        return clio_payments_payment

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
