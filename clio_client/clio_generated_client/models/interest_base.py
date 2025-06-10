from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interest_base_type import InterestBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterestBase")


@_attrs_define
class InterestBase:
    """
    Attributes:
        balance (Union[Unset, float]): Interest balance for the object
        period (Union[Unset, int]): Number of days that represent the frequency which your *Interest%* will be applied
        rate (Union[Unset, float]): Rate for the *Interest%*
        total (Union[Unset, float]): Interest total for the object
        type_ (Union[Unset, InterestBaseType]): Type of *Interest%* being applied
    """

    balance: Union[Unset, float] = UNSET
    period: Union[Unset, int] = UNSET
    rate: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    type_: Union[Unset, InterestBaseType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        period = self.period

        rate = self.rate

        total = self.total

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if period is not UNSET:
            field_dict["period"] = period
        if rate is not UNSET:
            field_dict["rate"] = rate
        if total is not UNSET:
            field_dict["total"] = total
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        period = d.pop("period", UNSET)

        rate = d.pop("rate", UNSET)

        total = d.pop("total", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, InterestBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InterestBaseType(_type_)

        interest_base = cls(
            balance=balance,
            period=period,
            rate=rate,
            total=total,
            type_=type_,
        )

        interest_base.additional_properties = d
        return interest_base

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
