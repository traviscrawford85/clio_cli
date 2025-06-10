from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClioPaymentsLinkcreateJsonBodyDataDestinationContact")


@_attrs_define
class ClioPaymentsLinkcreateJsonBodyDataDestinationContact:
    """
    Attributes:
        id (Union[Unset, int]): Only applicable for a direct payment. The contact that the payment will be associated
            with. If not defined, and the payment is collecting an unallocated balance, then the payment can be associated
            with a contact manually within Manage after it has been made.
    """

    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        clio_payments_linkcreate_json_body_data_destination_contact = cls(
            id=id,
        )

        clio_payments_linkcreate_json_body_data_destination_contact.additional_properties = d
        return clio_payments_linkcreate_json_body_data_destination_contact

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
