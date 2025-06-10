from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.balance_base_type import BalanceBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BalanceBase")


@_attrs_define
class BalanceBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Balance*
        amount (Union[Unset, float]): The amount for this Balance.
        type_ (Union[Unset, BalanceBaseType]): The type of Balance this data is for.
        interest_amount (Union[Unset, float]): The interest amount for this Balance.
        due (Union[Unset, float]): The amount due for this Balance, factoring in applicable discounts.
    """

    id: Union[Unset, int] = UNSET
    amount: Union[Unset, float] = UNSET
    type_: Union[Unset, BalanceBaseType] = UNSET
    interest_amount: Union[Unset, float] = UNSET
    due: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        interest_amount = self.interest_amount

        due = self.due

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if type_ is not UNSET:
            field_dict["type"] = type_
        if interest_amount is not UNSET:
            field_dict["interest_amount"] = interest_amount
        if due is not UNSET:
            field_dict["due"] = due

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BalanceBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BalanceBaseType(_type_)

        interest_amount = d.pop("interest_amount", UNSET)

        due = d.pop("due", UNSET)

        balance_base = cls(
            id=id,
            amount=amount,
            type_=type_,
            interest_amount=interest_amount,
            due=due,
        )

        balance_base.additional_properties = d
        return balance_base

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
