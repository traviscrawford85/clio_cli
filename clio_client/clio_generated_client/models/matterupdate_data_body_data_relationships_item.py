from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matterupdate_data_body_data_relationships_item_contact import (
        MatterupdateDataBodyDataRelationshipsItemContact,
    )


T = TypeVar("T", bound="MatterupdateDataBodyDataRelationshipsItem")


@_attrs_define
class MatterupdateDataBodyDataRelationshipsItem:
    """
    Attributes:
        description (Union[Unset, str]): Describe the relationship between a Contact and a Matter.
        contact (Union[Unset, MatterupdateDataBodyDataRelationshipsItemContact]):
        id (Union[Unset, int]): The unique identifier for a single Relationship associated with the Matter. The keyword
            `null` is not valid for this field.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated Relationship is present, the Relationship is deleted from the Matter.
    """

    description: Union[Unset, str] = UNSET
    contact: Union[Unset, "MatterupdateDataBodyDataRelationshipsItemContact"] = UNSET
    id: Union[Unset, int] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        id = self.id

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if contact is not UNSET:
            field_dict["contact"] = contact
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matterupdate_data_body_data_relationships_item_contact import (
            MatterupdateDataBodyDataRelationshipsItemContact,
        )

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, MatterupdateDataBodyDataRelationshipsItemContact]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = MatterupdateDataBodyDataRelationshipsItemContact.from_dict(_contact)

        id = d.pop("id", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        matterupdate_data_body_data_relationships_item = cls(
            description=description,
            contact=contact,
            id=id,
            field_destroy=field_destroy,
        )

        matterupdate_data_body_data_relationships_item.additional_properties = d
        return matterupdate_data_body_data_relationships_item

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
