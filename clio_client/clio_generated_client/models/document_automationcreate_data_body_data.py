from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_automationcreate_data_body_data_formats_item import (
    DocumentAutomationcreateDataBodyDataFormatsItem,
)

if TYPE_CHECKING:
    from ..models.document_automationcreate_data_body_data_document_template import (
        DocumentAutomationcreateDataBodyDataDocumentTemplate,
    )
    from ..models.document_automationcreate_data_body_data_matter import DocumentAutomationcreateDataBodyDataMatter


T = TypeVar("T", bound="DocumentAutomationcreateDataBodyData")


@_attrs_define
class DocumentAutomationcreateDataBodyData:
    """
    Attributes:
        document_template (DocumentAutomationcreateDataBodyDataDocumentTemplate):
        filename (str): The filename the generated document should have.
        formats (list[DocumentAutomationcreateDataBodyDataFormatsItem]): The formats the document should be generated
            as. It can either be generated as a PDF and/or in whatever type the document template is.
        matter (DocumentAutomationcreateDataBodyDataMatter):
    """

    document_template: "DocumentAutomationcreateDataBodyDataDocumentTemplate"
    filename: str
    formats: list[DocumentAutomationcreateDataBodyDataFormatsItem]
    matter: "DocumentAutomationcreateDataBodyDataMatter"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_template = self.document_template.to_dict()

        filename = self.filename

        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.value
            formats.append(formats_item)

        matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "document_template": document_template,
                "filename": filename,
                "formats": formats,
                "matter": matter,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_automationcreate_data_body_data_document_template import (
            DocumentAutomationcreateDataBodyDataDocumentTemplate,
        )
        from ..models.document_automationcreate_data_body_data_matter import DocumentAutomationcreateDataBodyDataMatter

        d = dict(src_dict)
        document_template = DocumentAutomationcreateDataBodyDataDocumentTemplate.from_dict(d.pop("document_template"))

        filename = d.pop("filename")

        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = DocumentAutomationcreateDataBodyDataFormatsItem(formats_item_data)

            formats.append(formats_item)

        matter = DocumentAutomationcreateDataBodyDataMatter.from_dict(d.pop("matter"))

        document_automationcreate_data_body_data = cls(
            document_template=document_template,
            filename=filename,
            formats=formats,
            matter=matter,
        )

        document_automationcreate_data_body_data.additional_properties = d
        return document_automationcreate_data_body_data

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
