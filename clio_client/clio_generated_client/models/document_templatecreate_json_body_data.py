from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_templatecreate_json_body_data_document_category import (
        DocumentTemplatecreateJsonBodyDataDocumentCategory,
    )


T = TypeVar("T", bound="DocumentTemplatecreateJsonBodyData")


@_attrs_define
class DocumentTemplatecreateJsonBodyData:
    """
    Attributes:
        file (str): A file that contains the DocumentTemplate. The file can be uploaded through a form as
            application/x-www-form-urlencoded or multipart/form-data request.
            Alternatively, the file can be converted to a BASE64-encoded string and serialized to JSON.
        document_category (Union[Unset, DocumentTemplatecreateJsonBodyDataDocumentCategory]):
        filename (Union[Unset, str]): The name of the file. The field is required when the file is BASE64-encoded
            string.
    """

    file: str
    document_category: Union[Unset, "DocumentTemplatecreateJsonBodyDataDocumentCategory"] = UNSET
    filename: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if filename is not UNSET:
            field_dict["filename"] = filename

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_templatecreate_json_body_data_document_category import (
            DocumentTemplatecreateJsonBodyDataDocumentCategory,
        )

        d = dict(src_dict)
        file = d.pop("file")

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentTemplatecreateJsonBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentTemplatecreateJsonBodyDataDocumentCategory.from_dict(_document_category)

        filename = d.pop("filename", UNSET)

        document_templatecreate_json_body_data = cls(
            file=file,
            document_category=document_category,
            filename=filename,
        )

        document_templatecreate_json_body_data.additional_properties = d
        return document_templatecreate_json_body_data

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
