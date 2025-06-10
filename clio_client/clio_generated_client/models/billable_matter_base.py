from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillableMatterBase")


@_attrs_define
class BillableMatterBase:
    """
    Attributes:
        currency_code (Union[Unset, str]): The currency code
        currency_id (Union[Unset, int]): The currency ID
        id (Union[Unset, int]): Unique identifier for the *BillableMatter*
        unbilled_hours (Union[Unset, float]): The unbilled number of hours for the matter
        unbilled_amount (Union[Unset, float]): The unbilled amount for the matter
        amount_in_trust (Union[Unset, float]): The trust amount available for the matter
        display_number (Union[Unset, str]): The reference to the matter
    """

    currency_code: Union[Unset, str] = UNSET
    currency_id: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    unbilled_hours: Union[Unset, float] = UNSET
    unbilled_amount: Union[Unset, float] = UNSET
    amount_in_trust: Union[Unset, float] = UNSET
    display_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_code = self.currency_code

        currency_id = self.currency_id

        id = self.id

        unbilled_hours = self.unbilled_hours

        unbilled_amount = self.unbilled_amount

        amount_in_trust = self.amount_in_trust

        display_number = self.display_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if id is not UNSET:
            field_dict["id"] = id
        if unbilled_hours is not UNSET:
            field_dict["unbilled_hours"] = unbilled_hours
        if unbilled_amount is not UNSET:
            field_dict["unbilled_amount"] = unbilled_amount
        if amount_in_trust is not UNSET:
            field_dict["amount_in_trust"] = amount_in_trust
        if display_number is not UNSET:
            field_dict["display_number"] = display_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_code = d.pop("currency_code", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        id = d.pop("id", UNSET)

        unbilled_hours = d.pop("unbilled_hours", UNSET)

        unbilled_amount = d.pop("unbilled_amount", UNSET)

        amount_in_trust = d.pop("amount_in_trust", UNSET)

        display_number = d.pop("display_number", UNSET)

        billable_matter_base = cls(
            currency_code=currency_code,
            currency_id=currency_id,
            id=id,
            unbilled_hours=unbilled_hours,
            unbilled_amount=unbilled_amount,
            amount_in_trust=amount_in_trust,
            display_number=display_number,
        )

        billable_matter_base.additional_properties = d
        return billable_matter_base

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
