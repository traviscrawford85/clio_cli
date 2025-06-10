from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discount_base_type import DiscountBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscountBase")


@_attrs_define
class DiscountBase:
    """
    Attributes:
        rate (Union[Unset, float]): The rate of the *Discount%*
        type_ (Union[Unset, DiscountBaseType]): The type of *Discount* being applied in your *Discount* rate.
        note (Union[Unset, str]): A note for your *Discount*
        early_payment_rate (Union[Unset, int]): The % discount that will be applied if your *Discount* is paid within
            the early payment period.
        early_payment_period (Union[Unset, int]): The number of days for your *Discount* period. If your bill is paid
            within this time, apply your *Discount* rate to the bill.
    """

    rate: Union[Unset, float] = UNSET
    type_: Union[Unset, DiscountBaseType] = UNSET
    note: Union[Unset, str] = UNSET
    early_payment_rate: Union[Unset, int] = UNSET
    early_payment_period: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        note = self.note

        early_payment_rate = self.early_payment_rate

        early_payment_period = self.early_payment_period

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_
        if note is not UNSET:
            field_dict["note"] = note
        if early_payment_rate is not UNSET:
            field_dict["early_payment_rate"] = early_payment_rate
        if early_payment_period is not UNSET:
            field_dict["early_payment_period"] = early_payment_period

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DiscountBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DiscountBaseType(_type_)

        note = d.pop("note", UNSET)

        early_payment_rate = d.pop("early_payment_rate", UNSET)

        early_payment_period = d.pop("early_payment_period", UNSET)

        discount_base = cls(
            rate=rate,
            type_=type_,
            note=note,
            early_payment_rate=early_payment_rate,
            early_payment_period=early_payment_period,
        )

        discount_base.additional_properties = d
        return discount_base

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
