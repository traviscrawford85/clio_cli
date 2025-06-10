from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultipartBase")


@_attrs_define
class MultipartBase:
    """
    Attributes:
        part_number (Union[Unset, int]): Unique identifier of a part which defines its position within the document
            being uploaded.
        put_url (Union[Unset, str]): A signed URL for uploading the file part. It expires in 10 minutes.
    """

    part_number: Union[Unset, int] = UNSET
    put_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        put_url = self.put_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if put_url is not UNSET:
            field_dict["put_url"] = put_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        part_number = d.pop("part_number", UNSET)

        put_url = d.pop("put_url", UNSET)

        multipart_base = cls(
            part_number=part_number,
            put_url=put_url,
        )

        multipart_base.additional_properties = d
        return multipart_base

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
