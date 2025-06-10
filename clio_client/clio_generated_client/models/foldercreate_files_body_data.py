from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.foldercreate_files_body_data_document_category import FoldercreateFilesBodyDataDocumentCategory
    from ..models.foldercreate_files_body_data_external_properties_item import (
        FoldercreateFilesBodyDataExternalPropertiesItem,
    )
    from ..models.foldercreate_files_body_data_parent import FoldercreateFilesBodyDataParent


T = TypeVar("T", bound="FoldercreateFilesBodyData")


@_attrs_define
class FoldercreateFilesBodyData:
    """
    Attributes:
        name (str): Name of the Folder
        parent (FoldercreateFilesBodyDataParent):
        document_category (Union[Unset, FoldercreateFilesBodyDataDocumentCategory]):
        external_properties (Union[Unset, list['FoldercreateFilesBodyDataExternalPropertiesItem']]):
        restore (Union[Unset, bool]): Whether or not a trashed Folder should be restored.
    """

    name: str
    parent: "FoldercreateFilesBodyDataParent"
    document_category: Union[Unset, "FoldercreateFilesBodyDataDocumentCategory"] = UNSET
    external_properties: Union[Unset, list["FoldercreateFilesBodyDataExternalPropertiesItem"]] = UNSET
    restore: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        parent = self.parent.to_dict()

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        restore = self.restore

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parent": parent,
            }
        )
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if restore is not UNSET:
            field_dict["restore"] = restore

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.foldercreate_files_body_data_document_category import FoldercreateFilesBodyDataDocumentCategory
        from ..models.foldercreate_files_body_data_external_properties_item import (
            FoldercreateFilesBodyDataExternalPropertiesItem,
        )
        from ..models.foldercreate_files_body_data_parent import FoldercreateFilesBodyDataParent

        d = dict(src_dict)
        name = d.pop("name")

        parent = FoldercreateFilesBodyDataParent.from_dict(d.pop("parent"))

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, FoldercreateFilesBodyDataDocumentCategory]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = FoldercreateFilesBodyDataDocumentCategory.from_dict(_document_category)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = FoldercreateFilesBodyDataExternalPropertiesItem.from_dict(
                external_properties_item_data
            )

            external_properties.append(external_properties_item)

        restore = d.pop("restore", UNSET)

        foldercreate_files_body_data = cls(
            name=name,
            parent=parent,
            document_category=document_category,
            external_properties=external_properties,
            restore=restore,
        )

        foldercreate_files_body_data.additional_properties = d
        return foldercreate_files_body_data

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
