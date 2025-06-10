from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentupdateDataBodyDataMultipartsItem")


@_attrs_define
class DocumentupdateDataBodyDataMultipartsItem:
    """
    Attributes:
        part_number (Union[Unset, int]): The part number of multipart upload. It must be an integer between 1 to 10,000,
            inclusive.

            Multipart upload supports upload a single file as a set of parts.
            Each part is a contiguous portion of the data.
            A `part_number` uniquely identifies a part and also defines its position within the document being uploaded.
            Each part must be at least 5 MB in size, except the last part.
            There is no minimum size limit on the last part.

            The URLs of multipart upload are returned in the field, `put_url`, with the corresponding `multipart`

            The API handles maximum 50 `multiparts` in one request. If the upload is split to more than 50 parts,
            make a PUT request with `fully_uploaded` equal to `false`, and another set of part numbers.
        content_length (Union[Unset, str]): The size of the part of the upload file in bytes.
        content_md5 (Union[Unset, str]): The base64-encoded 128-bit MD5 digest of the part data. This header can be used
            as a message integrity check to verify that the part data is the same data that was originally sent. Although it
            is optional, we recommend using the Content-MD5 mechanism as an end-to-end integrity check.
    """

    part_number: Union[Unset, int] = UNSET
    content_length: Union[Unset, str] = UNSET
    content_md5: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        part_number = self.part_number

        content_length = self.content_length

        content_md5 = self.content_md5

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if part_number is not UNSET:
            field_dict["part_number"] = part_number
        if content_length is not UNSET:
            field_dict["content_length"] = content_length
        if content_md5 is not UNSET:
            field_dict["content_md5"] = content_md5

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        part_number = d.pop("part_number", UNSET)

        content_length = d.pop("content_length", UNSET)

        content_md5 = d.pop("content_md5", UNSET)

        documentupdate_data_body_data_multiparts_item = cls(
            part_number=part_number,
            content_length=content_length,
            content_md5=content_md5,
        )

        documentupdate_data_body_data_multiparts_item.additional_properties = d
        return documentupdate_data_body_data_multiparts_item

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
