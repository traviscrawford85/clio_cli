import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documentcopy_data_body_data_document_category import DocumentcopyDataBodyDataDocumentCategory
    from ..models.documentcopy_data_body_data_external_properties_item import (
        DocumentcopyDataBodyDataExternalPropertiesItem,
    )
    from ..models.documentcopy_data_body_data_parent import DocumentcopyDataBodyDataParent


T = TypeVar("T", bound="DocumentcopyDataBodyData")


@_attrs_define
class DocumentcopyDataBodyData:
    """
    Attributes:
        parent (DocumentcopyDataBodyDataParent):
        communication_id (Union[Unset, int]): Related communication record.
        document_category (Union[Unset, DocumentcopyDataBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['DocumentcopyDataBodyDataExternalPropertiesItem']]):
        filename (Union[Unset, str]): Name of the original file. Default: 'name'.
        name (Union[Unset, str]): Document name.
        received_at (Union[Unset, datetime.datetime]): Date and time the document was received (Expects an ISO-8601
            timestamp).
    """

    parent: "DocumentcopyDataBodyDataParent"
    communication_id: Union[Unset, int] = UNSET
    document_category: Union[Unset, "DocumentcopyDataBodyDataDocumentCategory"] = UNSET
    external_properties: Union[Unset, list["DocumentcopyDataBodyDataExternalPropertiesItem"]] = UNSET
    filename: Union[Unset, str] = "name"
    name: Union[Unset, str] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent = self.parent.to_dict()

        communication_id = self.communication_id

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        filename = self.filename

        name = self.name

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "parent": parent,
            }
        )
        if communication_id is not UNSET:
            field_dict["communication_id"] = communication_id
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name
        if received_at is not UNSET:
            field_dict["received_at"] = received_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documentcopy_data_body_data_document_category import DocumentcopyDataBodyDataDocumentCategory
        from ..models.documentcopy_data_body_data_external_properties_item import (
            DocumentcopyDataBodyDataExternalPropertiesItem,
        )
        from ..models.documentcopy_data_body_data_parent import DocumentcopyDataBodyDataParent

        d = dict(src_dict)
        parent = DocumentcopyDataBodyDataParent.from_dict(d.pop("parent"))

        communication_id = d.pop("communication_id", UNSET)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentcopyDataBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentcopyDataBodyDataDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = DocumentcopyDataBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        filename = d.pop("filename", UNSET)

        name = d.pop("name", UNSET)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        documentcopy_data_body_data = cls(
            parent=parent,
            communication_id=communication_id,
            document_category=document_category,
            external_properties=external_properties,
            filename=filename,
            name=name,
            received_at=received_at,
        )

        documentcopy_data_body_data.additional_properties = d
        return documentcopy_data_body_data

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
