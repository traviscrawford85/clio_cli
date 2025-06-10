from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemupdateFilesBodyDataDiscount")


@_attrs_define
class LineItemupdateFilesBodyDataDiscount:
    """
    Attributes:
        rate (Union[Unset, float]): Discount rate for the LineItem.
        type_ (Union[Unset, bool]): Discount type. This should be set to one of: 'percentage' or 'money'.
    """

    rate: Union[Unset, float] = UNSET
    type_: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        type_ = d.pop("type", UNSET)

        line_itemupdate_files_body_data_discount = cls(
            rate=rate,
            type_=type_,
        )

        line_itemupdate_files_body_data_discount.additional_properties = d
        return line_itemupdate_files_body_data_discount

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
