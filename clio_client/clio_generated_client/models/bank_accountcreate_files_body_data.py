from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bank_accountcreate_files_body_data_type import BankAccountcreateFilesBodyDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BankAccountcreateFilesBodyData")


@_attrs_define
class BankAccountcreateFilesBodyData:
    """
    Attributes:
        currency (str): Currency the BankAccount is in.
        type_ (BankAccountcreateFilesBodyDataType): Type of BankAccount.
        account_number (Union[Unset, str]): Account number for the BankAccount.
        balance (Union[Unset, float]): BankAccount balance.
        controlled_account (Union[Unset, bool]): Whether is a controlled account.
        default_account (Union[Unset, bool]): Whether or not the BankAccount should be the default account.
        domicile_branch (Union[Unset, str]): Branch where the BankAccount was opened.
        general_ledger_number (Union[Unset, str]): General ledger number used for the Law Society of Alberta.
        holder (Union[Unset, str]): BankAccount holder.
        institution (Union[Unset, str]): Financial institution.
        name (Union[Unset, str]): BankAccount name.
        swift (Union[Unset, str]): Identification code for the financial institution.
        transit_number (Union[Unset, str]): Transit number for the BankAccount branch.
    """

    currency: str
    type_: BankAccountcreateFilesBodyDataType
    account_number: Union[Unset, str] = UNSET
    balance: Union[Unset, float] = UNSET
    controlled_account: Union[Unset, bool] = UNSET
    default_account: Union[Unset, bool] = UNSET
    domicile_branch: Union[Unset, str] = UNSET
    general_ledger_number: Union[Unset, str] = UNSET
    holder: Union[Unset, str] = UNSET
    institution: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    swift: Union[Unset, str] = UNSET
    transit_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        type_ = self.type_.value

        account_number = self.account_number

        balance = self.balance

        controlled_account = self.controlled_account

        default_account = self.default_account

        domicile_branch = self.domicile_branch

        general_ledger_number = self.general_ledger_number

        holder = self.holder

        institution = self.institution

        name = self.name

        swift = self.swift

        transit_number = self.transit_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "type": type_,
            }
        )
        if account_number is not UNSET:
            field_dict["account_number"] = account_number
        if balance is not UNSET:
            field_dict["balance"] = balance
        if controlled_account is not UNSET:
            field_dict["controlled_account"] = controlled_account
        if default_account is not UNSET:
            field_dict["default_account"] = default_account
        if domicile_branch is not UNSET:
            field_dict["domicile_branch"] = domicile_branch
        if general_ledger_number is not UNSET:
            field_dict["general_ledger_number"] = general_ledger_number
        if holder is not UNSET:
            field_dict["holder"] = holder
        if institution is not UNSET:
            field_dict["institution"] = institution
        if name is not UNSET:
            field_dict["name"] = name
        if swift is not UNSET:
            field_dict["swift"] = swift
        if transit_number is not UNSET:
            field_dict["transit_number"] = transit_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency")

        type_ = BankAccountcreateFilesBodyDataType(d.pop("type"))

        account_number = d.pop("account_number", UNSET)

        balance = d.pop("balance", UNSET)

        controlled_account = d.pop("controlled_account", UNSET)

        default_account = d.pop("default_account", UNSET)

        domicile_branch = d.pop("domicile_branch", UNSET)

        general_ledger_number = d.pop("general_ledger_number", UNSET)

        holder = d.pop("holder", UNSET)

        institution = d.pop("institution", UNSET)

        name = d.pop("name", UNSET)

        swift = d.pop("swift", UNSET)

        transit_number = d.pop("transit_number", UNSET)

        bank_accountcreate_files_body_data = cls(
            currency=currency,
            type_=type_,
            account_number=account_number,
            balance=balance,
            controlled_account=controlled_account,
            default_account=default_account,
            domicile_branch=domicile_branch,
            general_ledger_number=general_ledger_number,
            holder=holder,
            institution=institution,
            name=name,
            swift=swift,
            transit_number=transit_number,
        )

        bank_accountcreate_files_body_data.additional_properties = d
        return bank_accountcreate_files_body_data

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
