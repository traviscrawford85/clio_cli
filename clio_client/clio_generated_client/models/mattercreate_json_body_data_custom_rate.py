from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mattercreate_json_body_data_custom_rate_type import MattercreateJsonBodyDataCustomRateType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mattercreate_json_body_data_custom_rate_rates_item import MattercreateJsonBodyDataCustomRateRatesItem


T = TypeVar("T", bound="MattercreateJsonBodyDataCustomRate")


@_attrs_define
class MattercreateJsonBodyDataCustomRate:
    """
    Attributes:
        type_ (MattercreateJsonBodyDataCustomRateType): The type of custom rate for the Matter.
        rates (Union[Unset, list['MattercreateJsonBodyDataCustomRateRatesItem']]):
    """

    type_: MattercreateJsonBodyDataCustomRateType
    rates: Union[Unset, list["MattercreateJsonBodyDataCustomRateRatesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_json_body_data_custom_rate_rates_item import (
            MattercreateJsonBodyDataCustomRateRatesItem,
        )

        d = dict(src_dict)
        type_ = MattercreateJsonBodyDataCustomRateType(d.pop("type"))

        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = MattercreateJsonBodyDataCustomRateRatesItem.from_dict(rates_item_data)

            rates.append(rates_item)

        mattercreate_json_body_data_custom_rate = cls(
            type_=type_,
            rates=rates,
        )

        mattercreate_json_body_data_custom_rate.additional_properties = d
        return mattercreate_json_body_data_custom_rate

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
