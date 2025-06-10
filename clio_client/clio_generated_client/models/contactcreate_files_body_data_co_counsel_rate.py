from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactcreateFilesBodyDataCoCounselRate")


@_attrs_define
class ContactcreateFilesBodyDataCoCounselRate:
    """
    Attributes:
        rate (Union[Unset, float]): Billing rate if the Contact is a co-counsel.

            Note: this value can only be provided during PATCH requests. It cannot be provided at the time a Contact is
            created (i.e. POST requests).
    """

    rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate = self.rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        rate = d.pop("rate", UNSET)

        contactcreate_files_body_data_co_counsel_rate = cls(
            rate=rate,
        )

        contactcreate_files_body_data_co_counsel_rate.additional_properties = d
        return contactcreate_files_body_data_co_counsel_rate

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
