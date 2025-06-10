from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.matter_custom_rate_base_type import MatterCustomRateBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymorphic_custom_rate import PolymorphicCustomRate


T = TypeVar("T", bound="MatterCustomRate")


@_attrs_define
class MatterCustomRate:
    """
    Attributes:
        type_ (Union[Unset, MatterCustomRateBaseType]): The type of the *MatterCustomRate*
        on_invoice (Union[Unset, bool]): Specifies if the matter's associated activity is posted or on a bill.
        rates (Union[Unset, list['PolymorphicCustomRate']]): PolymorphicCustomRate
    """

    type_: Union[Unset, MatterCustomRateBaseType] = UNSET
    on_invoice: Union[Unset, bool] = UNSET
    rates: Union[Unset, list["PolymorphicCustomRate"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        on_invoice = self.on_invoice

        rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.rates, Unset):
            rates = []
            for rates_item_data in self.rates:
                rates_item = rates_item_data.to_dict()
                rates.append(rates_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if on_invoice is not UNSET:
            field_dict["on_invoice"] = on_invoice
        if rates is not UNSET:
            field_dict["rates"] = rates

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymorphic_custom_rate import PolymorphicCustomRate

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MatterCustomRateBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MatterCustomRateBaseType(_type_)

        on_invoice = d.pop("on_invoice", UNSET)

        rates = []
        _rates = d.pop("rates", UNSET)
        for rates_item_data in _rates or []:
            rates_item = PolymorphicCustomRate.from_dict(rates_item_data)

            rates.append(rates_item)

        matter_custom_rate = cls(
            type_=type_,
            on_invoice=on_invoice,
            rates=rates,
        )

        matter_custom_rate.additional_properties = d
        return matter_custom_rate

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
