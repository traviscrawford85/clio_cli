import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documentupdate_json_body_data_document_category import DocumentupdateJsonBodyDataDocumentCategory
    from ..models.documentupdate_json_body_data_external_properties_item import (
        DocumentupdateJsonBodyDataExternalPropertiesItem,
    )
    from ..models.documentupdate_json_body_data_multiparts_item import DocumentupdateJsonBodyDataMultipartsItem
    from ..models.documentupdate_json_body_data_parent import DocumentupdateJsonBodyDataParent


T = TypeVar("T", bound="DocumentupdateJsonBodyData")


@_attrs_define
class DocumentupdateJsonBodyData:
    """
    Attributes:
        communication_id (Union[Unset, int]): Related communication record.
        copy_version (Union[Unset, bool]): Indicates whether to create a new version with the updated filename on
            rename. This is intended to handle cases where the document extension has been changed; if the document
            extension has not changed, no new version will be created.
        document_category (Union[Unset, DocumentupdateJsonBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['DocumentupdateJsonBodyDataExternalPropertiesItem']]):
        fully_uploaded (Union[Unset, bool]): Indicates whether document is uploaded.

            When marking the document fully uploaded, it arises errors when:
            * The file is not successfully uploaded.
            * Not all the file parts are uploaded.
            * The document is already marked as fully uploaded.
        multiparts (Union[Unset, list['DocumentupdateJsonBodyDataMultipartsItem']]):
        name (Union[Unset, str]): Document name.
        parent (Union[Unset, DocumentupdateJsonBodyDataParent]):
        received_at (Union[Unset, datetime.datetime]): Date and time the document was received (Expects an ISO-8601
            timestamp).
        restore (Union[Unset, bool]): Whether or not a trashed Document should be restored.
        uuid (Union[Unset, str]): UUID associated with the document version. UUID is required to mark a document fully
            uploaded.
    """

    communication_id: Union[Unset, int] = UNSET
    copy_version: Union[Unset, bool] = UNSET
    document_category: Union[Unset, "DocumentupdateJsonBodyDataDocumentCategory"] = UNSET
    external_properties: Union[Unset, list["DocumentupdateJsonBodyDataExternalPropertiesItem"]] = UNSET
    fully_uploaded: Union[Unset, bool] = UNSET
    multiparts: Union[Unset, list["DocumentupdateJsonBodyDataMultipartsItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    parent: Union[Unset, "DocumentupdateJsonBodyDataParent"] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    restore: Union[Unset, bool] = UNSET
    uuid: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        communication_id = self.communication_id

        copy_version = self.copy_version

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        fully_uploaded = self.fully_uploaded

        multiparts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.multiparts, Unset):
            multiparts = []
            for multiparts_item_data in self.multiparts:
                multiparts_item = multiparts_item_data.to_dict()
                multiparts.append(multiparts_item)

        name = self.name

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        restore = self.restore

        uuid = self.uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if communication_id is not UNSET:
            field_dict["communication_id"] = communication_id
        if copy_version is not UNSET:
            field_dict["copy_version"] = copy_version
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if fully_uploaded is not UNSET:
            field_dict["fully_uploaded"] = fully_uploaded
        if multiparts is not UNSET:
            field_dict["multiparts"] = multiparts
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if restore is not UNSET:
            field_dict["restore"] = restore
        if uuid is not UNSET:
            field_dict["uuid"] = uuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.documentupdate_json_body_data_document_category import DocumentupdateJsonBodyDataDocumentCategory
        from ..models.documentupdate_json_body_data_external_properties_item import (
            DocumentupdateJsonBodyDataExternalPropertiesItem,
        )
        from ..models.documentupdate_json_body_data_multiparts_item import DocumentupdateJsonBodyDataMultipartsItem
        from ..models.documentupdate_json_body_data_parent import DocumentupdateJsonBodyDataParent

        d = dict(src_dict)
        communication_id = d.pop("communication_id", UNSET)

        copy_version = d.pop("copy_version", UNSET)

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentupdateJsonBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentupdateJsonBodyDataDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = DocumentupdateJsonBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        fully_uploaded = d.pop("fully_uploaded", UNSET)

        multiparts = []
        _multiparts = d.pop("multiparts", UNSET)
        for multiparts_item_data in _multiparts or []:
            multiparts_item = DocumentupdateJsonBodyDataMultipartsItem.from_dict(multiparts_item_data)

            multiparts.append(multiparts_item)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, DocumentupdateJsonBodyDataParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = DocumentupdateJsonBodyDataParent.from_dict(_parent)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        restore = d.pop("restore", UNSET)

        uuid = d.pop("uuid", UNSET)

        documentupdate_json_body_data = cls(
            communication_id=communication_id,
            copy_version=copy_version,
            document_category=document_category,
            external_properties=external_properties,
            fully_uploaded=fully_uploaded,
            multiparts=multiparts,
            name=name,
            parent=parent,
            received_at=received_at,
            restore=restore,
            uuid=uuid,
        )

        documentupdate_json_body_data.additional_properties = d
        return documentupdate_json_body_data

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
