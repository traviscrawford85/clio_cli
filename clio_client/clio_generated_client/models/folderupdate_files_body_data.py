from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.folderupdate_files_body_data_document_category import FolderupdateFilesBodyDataDocumentCategory
    from ..models.folderupdate_files_body_data_external_properties_item import (
        FolderupdateFilesBodyDataExternalPropertiesItem,
    )
    from ..models.folderupdate_files_body_data_parent import FolderupdateFilesBodyDataParent


T = TypeVar("T", bound="FolderupdateFilesBodyData")


@_attrs_define
class FolderupdateFilesBodyData:
    """
    Attributes:
        document_category (Union[Unset, FolderupdateFilesBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['FolderupdateFilesBodyDataExternalPropertiesItem']]):
        name (Union[Unset, str]): Name of the Folder
        parent (Union[Unset, FolderupdateFilesBodyDataParent]):
        restore (Union[Unset, bool]): Whether or not a trashed Folder should be restored.
    """

    document_category: Union[Unset, "FolderupdateFilesBodyDataDocumentCategory"] = UNSET
    external_properties: Union[Unset, list["FolderupdateFilesBodyDataExternalPropertiesItem"]] = UNSET
    name: Union[Unset, str] = UNSET
    parent: Union[Unset, "FolderupdateFilesBodyDataParent"] = UNSET
    restore: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        name = self.name

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        restore = self.restore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if restore is not UNSET:
            field_dict["restore"] = restore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folderupdate_files_body_data_document_category import FolderupdateFilesBodyDataDocumentCategory
        from ..models.folderupdate_files_body_data_external_properties_item import (
            FolderupdateFilesBodyDataExternalPropertiesItem,
        )
        from ..models.folderupdate_files_body_data_parent import FolderupdateFilesBodyDataParent

        d = dict(src_dict)
        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, FolderupdateFilesBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = FolderupdateFilesBodyDataDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = FolderupdateFilesBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, FolderupdateFilesBodyDataParent]
        if isinstance(_parent, Unset):
            parent = UNSET
        else:
            parent = FolderupdateFilesBodyDataParent.from_dict(_parent)

        restore = d.pop("restore", UNSET)

        folderupdate_files_body_data = cls(
            document_category=document_category,
            external_properties=external_properties,
            name=name,
            parent=parent,
            restore=restore,
        )

        folderupdate_files_body_data.additional_properties = d
        return folderupdate_files_body_data

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
