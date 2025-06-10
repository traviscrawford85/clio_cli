import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documentcreate_json_body_data_document_category import DocumentcreateJsonBodyDataDocumentCategory
    from ..models.documentcreate_json_body_data_external_properties_item import (
        DocumentcreateJsonBodyDataExternalPropertiesItem,
    )
    from ..models.documentcreate_json_body_data_multiparts_item import DocumentcreateJsonBodyDataMultipartsItem
    from ..models.documentcreate_json_body_data_parent import DocumentcreateJsonBodyDataParent


T = TypeVar("T", bound="DocumentcreateJsonBodyData")


@_attrs_define
class DocumentcreateJsonBodyData:
    """
    Attributes:
        name (str): Document name.
        parent (DocumentcreateJsonBodyDataParent):
        communication_id (Union[Unset, int]): Related communication record.
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data. If the field is
            not specified, it is determined by the file extension.
        document_category (Union[Unset, DocumentcreateJsonBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['DocumentcreateJsonBodyDataExternalPropertiesItem']]):
        filename (Union[Unset, str]): Name of the original file. Default: 'name'.
        multiparts (Union[Unset, list['DocumentcreateJsonBodyDataMultipartsItem']]):
        received_at (Union[Unset, datetime.datetime]): Date and time the document was received (Expects an ISO-8601
            timestamp).
    """

    name: str
    parent: "DocumentcreateJsonBodyDataParent"
    communication_id: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    document_category: Union[Unset, "DocumentcreateJsonBodyDataDocumentCategory"] = UNSET
    external_properties: Union[Unset, list["DocumentcreateJsonBodyDataExternalPropertiesItem"]] = UNSET
    filename: Union[Unset, str] = "name"
    multiparts: Union[Unset, list["DocumentcreateJsonBodyDataMultipartsItem"]] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent = self.parent.to_dict()

        communication_id = self.communication_id

        content_type = self.content_type

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

        multiparts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.multiparts, Unset):
            multiparts = []
            for multiparts_item_data in self.multiparts:
                multiparts_item = multiparts_item_data.to_dict()
                multiparts.append(multiparts_item)

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parent": parent,
            }
        )
        if communication_id is not UNSET:
            field_dict["communication_id"] = communication_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if filename is not UNSET:
            field_dict["filename"] = filename
        if multiparts is not UNSET:
            field_dict["multiparts"] = multiparts
        if received_at is not UNSET:
            field_dict["received_at"] = received_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documentcreate_json_body_data_document_category import DocumentcreateJsonBodyDataDocumentCategory
        from ..models.documentcreate_json_body_data_external_properties_item import (
            DocumentcreateJsonBodyDataExternalPropertiesItem,
        )
        from ..models.documentcreate_json_body_data_multiparts_item import DocumentcreateJsonBodyDataMultipartsItem
        from ..models.documentcreate_json_body_data_parent import DocumentcreateJsonBodyDataParent

        d = dict(src_dict)
        name = d.pop("name")

        parent = DocumentcreateJsonBodyDataParent.from_dict(d.pop("parent"))

        communication_id = d.pop("communication_id", UNSET)

        content_type = d.pop("content_type", UNSET)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentcreateJsonBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentcreateJsonBodyDataDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = DocumentcreateJsonBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        filename = d.pop("filename", UNSET)

        multiparts = []
        _multiparts = d.pop("multiparts", UNSET)
        for multiparts_item_data in _multiparts or []:
            multiparts_item = DocumentcreateJsonBodyDataMultipartsItem.from_dict(multiparts_item_data)

            multiparts.append(multiparts_item)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        documentcreate_json_body_data = cls(
            name=name,
            parent=parent,
            communication_id=communication_id,
            content_type=content_type,
            document_category=document_category,
            external_properties=external_properties,
            filename=filename,
            multiparts=multiparts,
            received_at=received_at,
        )

        documentcreate_json_body_data.additional_properties = d
        return documentcreate_json_body_data

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
