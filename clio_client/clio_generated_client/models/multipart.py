from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multipart_header_base import MultipartHeaderBase


T = TypeVar("T", bound="Multipart")


@_attrs_define
class Multipart:
    """
    Attributes:
        part_number (Union[Unset, int]): Unique identifier of a part which defines its position within the document
            being uploaded.
        put_url (Union[Unset, str]): A signed URL for uploading the file part. It expires in 10 minutes.
        put_headers (Union[Unset, list['MultipartHeaderBase']]): MultipartHeader
    """

    part_number: Union[Unset, int] = UNSET
    put_url: Union[Unset, str] = UNSET
    put_headers: Union[Unset, list["MultipartHeaderBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        put_url = self.put_url

        put_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.put_headers, Unset):
            put_headers = []
            for put_headers_item_data in self.put_headers:
                put_headers_item = put_headers_item_data.to_dict()
                put_headers.append(put_headers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if put_url is not UNSET:
            field_dict["put_url"] = put_url
        if put_headers is not UNSET:
            field_dict["put_headers"] = put_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.multipart_header_base import MultipartHeaderBase

        d = dict(src_dict)
        part_number = d.pop("part_number", UNSET)

        put_url = d.pop("put_url", UNSET)

        put_headers = []
        _put_headers = d.pop("put_headers", UNSET)
        for put_headers_item_data in _put_headers or []:
            put_headers_item = MultipartHeaderBase.from_dict(put_headers_item_data)

            put_headers.append(put_headers_item)

        multipart = cls(
            part_number=part_number,
            put_url=put_url,
            put_headers=put_headers,
        )

        multipart.additional_properties = d
        return multipart

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
