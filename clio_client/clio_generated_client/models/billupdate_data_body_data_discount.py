from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.billupdate_data_body_data_discount_type import BillupdateDataBodyDataDiscountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillupdateDataBodyDataDiscount")


@_attrs_define
class BillupdateDataBodyDataDiscount:
    """
    Attributes:
        rate (Union[Unset, float]): Discount amount for the Bill. This can either be a percentage or monetary value,
            this is determined by the `discount[type]`.
        type_ (Union[Unset, BillupdateDataBodyDataDiscountType]): The type of discount you are applying to your Bill
            with the `discount[rate]`.
        note (Union[Unset, str]): A note for your Bill's discount.
    """

    rate: Union[Unset, float] = UNSET
    type_: Union[Unset, BillupdateDataBodyDataDiscountType] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BillupdateDataBodyDataDiscountType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillupdateDataBodyDataDiscountType(_type_)

        note = d.pop("note", UNSET)

        billupdate_data_body_data_discount = cls(
            rate=rate,
            type_=type_,
            note=note,
        )

        billupdate_data_body_data_discount.additional_properties = d
        return billupdate_data_body_data_discount

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
