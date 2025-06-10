import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allocation_base import AllocationBase
    from ..models.bank_account_base import BankAccountBase
    from ..models.bill_base import BillBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="BankTransaction")


@_attrs_define
class BankTransaction:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BankTransaction*
        type_ (Union[Unset, str]): The type of the *BankTransaction*
        etag (Union[Unset, str]): ETag for the *BankTransaction*
        created_at (Union[Unset, datetime.datetime]): The time the *BankTransaction* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *BankTransaction* was last updated (as a ISO-8601
            timestamp)
        bank_account_id (Union[Unset, int]): The associated bank account.
        source (Union[Unset, str]): Where the transaction came from.
        confirmation (Union[Unset, str]): The reference code for the transaction.
        date (Union[Unset, datetime.date]): The date of the transaction.
        amount (Union[Unset, float]): The amount of the transaction.
        currency (Union[Unset, str]): The currency of the transaction.
        currency_id (Union[Unset, int]): The id of the currency of the transaction.
        description (Union[Unset, str]): The description of the transaction.
        exchange_rate (Union[Unset, float]): The exchange rate of the transaction.
        transaction_type (Union[Unset, str]): What kind of transaction.
        funds_in (Union[Unset, float]): The amount of funds received in this transaction.
        funds_out (Union[Unset, float]): The amount of funds withdrawn in this transaction.
        clio_payments_transaction (Union[Unset, bool]): Whether the transaction was created through online payments.
        current_account_balance (Union[Unset, float]): The current account balance.
        read_only_confirmation (Union[Unset, bool]): Whether the transaction's reference code is read-only.
        client (Union[Unset, ContactBase]):
        matter (Union[Unset, MatterBase]):
        bank_account (Union[Unset, BankAccountBase]):
        bill (Union[Unset, BillBase]):
        allocation (Union[Unset, AllocationBase]):
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    bank_account_id: Union[Unset, int] = UNSET
    source: Union[Unset, str] = UNSET
    confirmation: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    amount: Union[Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    exchange_rate: Union[Unset, float] = UNSET
    transaction_type: Union[Unset, str] = UNSET
    funds_in: Union[Unset, float] = UNSET
    funds_out: Union[Unset, float] = UNSET
    clio_payments_transaction: Union[Unset, bool] = UNSET
    current_account_balance: Union[Unset, float] = UNSET
    read_only_confirmation: Union[Unset, bool] = UNSET
    client: Union[Unset, "ContactBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    bank_account: Union[Unset, "BankAccountBase"] = UNSET
    bill: Union[Unset, "BillBase"] = UNSET
    allocation: Union[Unset, "AllocationBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        bank_account_id = self.bank_account_id

        source = self.source

        confirmation = self.confirmation

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        currency = self.currency

        currency_id = self.currency_id

        description = self.description

        exchange_rate = self.exchange_rate

        transaction_type = self.transaction_type

        funds_in = self.funds_in

        funds_out = self.funds_out

        clio_payments_transaction = self.clio_payments_transaction

        current_account_balance = self.current_account_balance

        read_only_confirmation = self.read_only_confirmation

        client: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        bank_account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_account, Unset):
            bank_account = self.bank_account.to_dict()

        bill: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill, Unset):
            bill = self.bill.to_dict()

        allocation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.allocation, Unset):
            allocation = self.allocation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if bank_account_id is not UNSET:
            field_dict["bank_account_id"] = bank_account_id
        if source is not UNSET:
            field_dict["source"] = source
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if description is not UNSET:
            field_dict["description"] = description
        if exchange_rate is not UNSET:
            field_dict["exchange_rate"] = exchange_rate
        if transaction_type is not UNSET:
            field_dict["transaction_type"] = transaction_type
        if funds_in is not UNSET:
            field_dict["funds_in"] = funds_in
        if funds_out is not UNSET:
            field_dict["funds_out"] = funds_out
        if clio_payments_transaction is not UNSET:
            field_dict["clio_payments_transaction"] = clio_payments_transaction
        if current_account_balance is not UNSET:
            field_dict["current_account_balance"] = current_account_balance
        if read_only_confirmation is not UNSET:
            field_dict["read_only_confirmation"] = read_only_confirmation
        if client is not UNSET:
            field_dict["client"] = client
        if matter is not UNSET:
            field_dict["matter"] = matter
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if bill is not UNSET:
            field_dict["bill"] = bill
        if allocation is not UNSET:
            field_dict["allocation"] = allocation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_base import AllocationBase
        from ..models.bank_account_base import BankAccountBase
        from ..models.bill_base import BillBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        etag = d.pop("etag", UNSET)

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

        bank_account_id = d.pop("bank_account_id", UNSET)

        source = d.pop("source", UNSET)

        confirmation = d.pop("confirmation", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        amount = d.pop("amount", UNSET)

        currency = d.pop("currency", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        description = d.pop("description", UNSET)

        exchange_rate = d.pop("exchange_rate", UNSET)

        transaction_type = d.pop("transaction_type", UNSET)

        funds_in = d.pop("funds_in", UNSET)

        funds_out = d.pop("funds_out", UNSET)

        clio_payments_transaction = d.pop("clio_payments_transaction", UNSET)

        current_account_balance = d.pop("current_account_balance", UNSET)

        read_only_confirmation = d.pop("read_only_confirmation", UNSET)

        _client = d.pop("client", UNSET)
        client: Union[Unset, ContactBase]
        if isinstance(_client, Unset):
            client = UNSET
        else:
            client = ContactBase.from_dict(_client)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _bank_account = d.pop("bank_account", UNSET)
        bank_account: Union[Unset, BankAccountBase]
        if isinstance(_bank_account, Unset):
            bank_account = UNSET
        else:
            bank_account = BankAccountBase.from_dict(_bank_account)

        _bill = d.pop("bill", UNSET)
        bill: Union[Unset, BillBase]
        if isinstance(_bill, Unset):
            bill = UNSET
        else:
            bill = BillBase.from_dict(_bill)

        _allocation = d.pop("allocation", UNSET)
        allocation: Union[Unset, AllocationBase]
        if isinstance(_allocation, Unset):
            allocation = UNSET
        else:
            allocation = AllocationBase.from_dict(_allocation)

        bank_transaction = cls(
            id=id,
            type_=type_,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            bank_account_id=bank_account_id,
            source=source,
            confirmation=confirmation,
            date=date,
            amount=amount,
            currency=currency,
            currency_id=currency_id,
            description=description,
            exchange_rate=exchange_rate,
            transaction_type=transaction_type,
            funds_in=funds_in,
            funds_out=funds_out,
            clio_payments_transaction=clio_payments_transaction,
            current_account_balance=current_account_balance,
            read_only_confirmation=read_only_confirmation,
            client=client,
            matter=matter,
            bank_account=bank_account,
            bill=bill,
            allocation=allocation,
        )

        bank_transaction.additional_properties = d
        return bank_transaction

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
