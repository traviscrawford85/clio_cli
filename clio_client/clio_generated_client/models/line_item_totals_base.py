from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LineItemTotalsBase")


@_attrs_define
class LineItemTotalsBase:
    """
    Attributes:
        quantity (Union[Unset, float]): Sum of quantity for included line items.
        price (Union[Unset, float]): Sum of price for included line items.
        discount_percent (Union[Unset, float]): Sum of discount as percentage for included line items.
        total (Union[Unset, float]): Sum of total for included line items.
        sub_total (Union[Unset, float]): Sum of total before discount and tax is applied.
    """

    quantity: Union[Unset, float] = UNSET
    price: Union[Unset, float] = UNSET
    discount_percent: Union[Unset, float] = UNSET
    total: Union[Unset, float] = UNSET
    sub_total: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        quantity = self.quantity

        price = self.price

        discount_percent = self.discount_percent

        total = self.total

        sub_total = self.sub_total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if price is not UNSET:
            field_dict["price"] = price
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if total is not UNSET:
            field_dict["total"] = total
        if sub_total is not UNSET:
            field_dict["sub_total"] = sub_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        quantity = d.pop("quantity", UNSET)

        price = d.pop("price", UNSET)

        discount_percent = d.pop("discount_percent", UNSET)

        total = d.pop("total", UNSET)

        sub_total = d.pop("sub_total", UNSET)

        line_item_totals_base = cls(
            quantity=quantity,
            price=price,
            discount_percent=discount_percent,
            total=total,
            sub_total=sub_total,
        )

        line_item_totals_base.additional_properties = d
        return line_item_totals_base

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
