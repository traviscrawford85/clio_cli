import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.bank_account_base_type import BankAccountBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_base import UserBase


T = TypeVar("T", bound="BankAccount")


@_attrs_define
class BankAccount:
    """
    Attributes:
        account_number (Union[Unset, str]): The account number for *BankAccount*
        balance (Union[Unset, float]): The current balance of the *BankAccount*
        bank_transactions_count (Union[Unset, int]): The number of bank transactions associated with the account.
        clio_payment_page_link (Union[Unset, str]): Link to Single Payment Page which allows to transfer funds without
            logging in.
        clio_payment_page_qr_code (Union[Unset, str]): A QR code that links to a Single Payment Page which allows to
            transfer funds without logging in.
        clio_payments_enabled (Union[Unset, bool]): Whether the bank account is connected to Clio Payments
        controlled_account (Union[Unset, bool]): Whether is a controlled account
        created_at (Union[Unset, datetime.datetime]): The time the *BankAccount* was created (as a ISO-8601 timestamp)
        currency (Union[Unset, str]): The currency type of the *BankAccount*
        currency_symbol (Union[Unset, str]): The currency symbol of the *BankAccount*
        currency_id (Union[Unset, float]): The currency ID of the *BankAccount*
        default_account (Union[Unset, bool]): Whether it is the default account
        domicile_branch (Union[Unset, str]): The name of the branch where the account was opened
        etag (Union[Unset, str]): ETag for the *BankAccount*
        general_ledger_number (Union[Unset, str]): General ledger number
        holder (Union[Unset, str]): The name of the person or business that owns the *BankAccount*
        id (Union[Unset, int]): Unique identifier for the *BankAccount*
        institution (Union[Unset, str]): The financial institution where the *BankAccount* is registered
        name (Union[Unset, str]): The name of the *BankAccount*
        swift (Union[Unset, str]): A unique identification code for the financial institution
        transit_number (Union[Unset, str]): Transit number for the bank account branch
        type_ (Union[Unset, BankAccountBaseType]): The type of the *BankAccount*
        updated_at (Union[Unset, datetime.datetime]): The time the *BankAccount* was last updated (as a ISO-8601
            timestamp)
        user (Union[Unset, UserBase]):
    """

    account_number: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    bank_transactions_count: Union[Unset, int] = UNSET
    clio_payment_page_link: Union[Unset, str] = UNSET
    clio_payment_page_qr_code: Union[Unset, str] = UNSET
    clio_payments_enabled: Union[Unset, bool] = UNSET
    controlled_account: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_symbol: Union[Unset, str] = UNSET
    currency_id: Union[Unset, float] = UNSET
    default_account: Union[Unset, bool] = UNSET
    domicile_branch: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    general_ledger_number: Union[Unset, str] = UNSET
    holder: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    institution: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    swift: Union[Unset, str] = UNSET
    transit_number: Union[Unset, str] = UNSET
    type_: Union[Unset, BankAccountBaseType] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_number = self.account_number

        balance = self.balance

        bank_transactions_count = self.bank_transactions_count

        clio_payment_page_link = self.clio_payment_page_link

        clio_payment_page_qr_code = self.clio_payment_page_qr_code

        clio_payments_enabled = self.clio_payments_enabled

        controlled_account = self.controlled_account

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        currency = self.currency

        currency_symbol = self.currency_symbol

        currency_id = self.currency_id

        default_account = self.default_account

        domicile_branch = self.domicile_branch

        etag = self.etag

        general_ledger_number = self.general_ledger_number

        holder = self.holder

        id = self.id

        institution = self.institution

        name = self.name

        swift = self.swift

        transit_number = self.transit_number

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if balance is not UNSET:
            field_dict["balance"] = balance
        if bank_transactions_count is not UNSET:
            field_dict["bank_transactions_count"] = bank_transactions_count
        if clio_payment_page_link is not UNSET:
            field_dict["clio_payment_page_link"] = clio_payment_page_link
        if clio_payment_page_qr_code is not UNSET:
            field_dict["clio_payment_page_qr_code"] = clio_payment_page_qr_code
        if clio_payments_enabled is not UNSET:
            field_dict["clio_payments_enabled"] = clio_payments_enabled
        if controlled_account is not UNSET:
            field_dict["controlled_account"] = controlled_account
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if default_account is not UNSET:
            field_dict["default_account"] = default_account
        if domicile_branch is not UNSET:
            field_dict["domicile_branch"] = domicile_branch
        if etag is not UNSET:
            field_dict["etag"] = etag
        if general_ledger_number is not UNSET:
            field_dict["general_ledger_number"] = general_ledger_number
        if holder is not UNSET:
            field_dict["holder"] = holder
        if id is not UNSET:
            field_dict["id"] = id
        if institution is not UNSET:
            field_dict["institution"] = institution
        if name is not UNSET:
            field_dict["name"] = name
        if swift is not UNSET:
            field_dict["swift"] = swift
        if transit_number is not UNSET:
            field_dict["transit_number"] = transit_number
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_base import UserBase

        d = dict(src_dict)
        account_number = d.pop("account_number", UNSET)

        balance = d.pop("balance", UNSET)

        bank_transactions_count = d.pop("bank_transactions_count", UNSET)

        clio_payment_page_link = d.pop("clio_payment_page_link", UNSET)

        clio_payment_page_qr_code = d.pop("clio_payment_page_qr_code", UNSET)

        clio_payments_enabled = d.pop("clio_payments_enabled", UNSET)

        controlled_account = d.pop("controlled_account", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        currency = d.pop("currency", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        default_account = d.pop("default_account", UNSET)

        domicile_branch = d.pop("domicile_branch", UNSET)

        etag = d.pop("etag", UNSET)

        general_ledger_number = d.pop("general_ledger_number", UNSET)

        holder = d.pop("holder", UNSET)

        id = d.pop("id", UNSET)

        institution = d.pop("institution", UNSET)

        name = d.pop("name", UNSET)

        swift = d.pop("swift", UNSET)

        transit_number = d.pop("transit_number", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BankAccountBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BankAccountBaseType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        bank_account = cls(
            account_number=account_number,
            balance=balance,
            bank_transactions_count=bank_transactions_count,
            clio_payment_page_link=clio_payment_page_link,
            clio_payment_page_qr_code=clio_payment_page_qr_code,
            clio_payments_enabled=clio_payments_enabled,
            controlled_account=controlled_account,
            created_at=created_at,
            currency=currency,
            currency_symbol=currency_symbol,
            currency_id=currency_id,
            default_account=default_account,
            domicile_branch=domicile_branch,
            etag=etag,
            general_ledger_number=general_ledger_number,
            holder=holder,
            id=id,
            institution=institution,
            name=name,
            swift=swift,
            transit_number=transit_number,
            type_=type_,
            updated_at=updated_at,
            user=user,
        )

        bank_account.additional_properties = d
        return bank_account

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
