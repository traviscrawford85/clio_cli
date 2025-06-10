from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountBalanceBase")


@_attrs_define
class AccountBalanceBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *AccountBalance*
        balance (Union[Unset, float]): The current balance of the bank account available to the matter or contact
        type_ (Union[Unset, str]): The bank account type. Either Operating or Trust
        name (Union[Unset, str]): The name of the bank account
        currency_id (Union[Unset, int]): The currency ID of the bank account
    """

    id: Union[Unset, int] = UNSET
    balance: Union[Unset, float] = UNSET
    type_: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    currency_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        balance = self.balance

        type_ = self.type_

        name = self.name

        currency_id = self.currency_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if balance is not UNSET:
            field_dict["balance"] = balance
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        balance = d.pop("balance", UNSET)

        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        account_balance_base = cls(
            id=id,
            balance=balance,
            type_=type_,
            name=name,
            currency_id=currency_id,
        )

        account_balance_base.additional_properties = d
        return account_balance_base

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
