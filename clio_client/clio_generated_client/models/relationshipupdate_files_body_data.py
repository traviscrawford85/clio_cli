from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.relationshipupdate_files_body_data_contact import RelationshipupdateFilesBodyDataContact
    from ..models.relationshipupdate_files_body_data_matter import RelationshipupdateFilesBodyDataMatter


T = TypeVar("T", bound="RelationshipupdateFilesBodyData")


@_attrs_define
class RelationshipupdateFilesBodyData:
    """
    Attributes:
        contact (Union[Unset, RelationshipupdateFilesBodyDataContact]):
        description (Union[Unset, str]): Describe the relationship between a Contact and a Matter.
        matter (Union[Unset, RelationshipupdateFilesBodyDataMatter]):
    """

    contact: Union[Unset, "RelationshipupdateFilesBodyDataContact"] = UNSET
    description: Union[Unset, str] = UNSET
    matter: Union[Unset, "RelationshipupdateFilesBodyDataMatter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        description = self.description

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact is not UNSET:
            field_dict["contact"] = contact
        if description is not UNSET:
            field_dict["description"] = description
        if matter is not UNSET:
            field_dict["matter"] = matter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.relationshipupdate_files_body_data_contact import RelationshipupdateFilesBodyDataContact
        from ..models.relationshipupdate_files_body_data_matter import RelationshipupdateFilesBodyDataMatter

        d = dict(src_dict)
        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, RelationshipupdateFilesBodyDataContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = RelationshipupdateFilesBodyDataContact.from_dict(_contact)

        description = d.pop("description", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, RelationshipupdateFilesBodyDataMatter]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = RelationshipupdateFilesBodyDataMatter.from_dict(_matter)

        relationshipupdate_files_body_data = cls(
            contact=contact,
            description=description,
            matter=matter,
        )

        relationshipupdate_files_body_data.additional_properties = d
        return relationshipupdate_files_body_data

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
