from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ContactcreateJsonBodyDataCustomFieldSetAssociationsItemCustomFieldSet")


@_attrs_define
class ContactcreateJsonBodyDataCustomFieldSetAssociationsItemCustomFieldSet:
    """
    Attributes:
        id (int): The unique identifier for a single CustomFieldSet associated with the CustomFieldSetAssociation. The
            keyword `null` is not valid for this field.
    """

    id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        contactcreate_json_body_data_custom_field_set_associations_item_custom_field_set = cls(
            id=id,
        )

        contactcreate_json_body_data_custom_field_set_associations_item_custom_field_set.additional_properties = d
        return contactcreate_json_body_data_custom_field_set_associations_item_custom_field_set

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
