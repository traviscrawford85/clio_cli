import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document_archivecreate_files_body_data import DocumentArchivecreateFilesBodyData


T = TypeVar("T", bound="DocumentArchivecreateFilesBody")


@_attrs_define
class DocumentArchivecreateFilesBody:
    """
    Attributes:
        data (DocumentArchivecreateFilesBodyData):
    """

    data: "DocumentArchivecreateFilesBodyData"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        data = (None, json.dumps(self.data.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_archivecreate_files_body_data import DocumentArchivecreateFilesBodyData

        d = dict(src_dict)
        data = DocumentArchivecreateFilesBodyData.from_dict(d.pop("data"))

        document_archivecreate_files_body = cls(
            data=data,
        )

        document_archivecreate_files_body.additional_properties = d
        return document_archivecreate_files_body

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
