from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.documentupdate_data_body_data_parent_type import DocumentupdateDataBodyDataParentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentupdateDataBodyDataParent")


@_attrs_define
class DocumentupdateDataBodyDataParent:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier of the parent object.
        type_ (Union[Unset, DocumentupdateDataBodyDataParentType]): Type of parent object:
            * "Document" represents an existing Clio document. It is specified when you provide a new revision (or document
            version) to an existing document.
            * "Folder" represents a specified folder on Clio by folder id. It if specified when you add / move an item to a
            folder.
            * "Contact" represents a contact folder on Clio identified by contact id. It is specified when you add / move an
            item to a contact folder. A contact folder will be created for the specified contact if none exists already.
            * "Matter" represents a matter folder on Clio identified by matter id. It is specified when you add / move an
            item to a matter folder.
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, DocumentupdateDataBodyDataParentType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentupdateDataBodyDataParentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentupdateDataBodyDataParentType(_type_)

        documentupdate_data_body_data_parent = cls(
            id=id,
            type_=type_,
        )

        documentupdate_data_body_data_parent.additional_properties = d
        return documentupdate_data_body_data_parent

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
