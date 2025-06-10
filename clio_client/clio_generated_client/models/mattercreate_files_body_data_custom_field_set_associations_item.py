from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mattercreate_files_body_data_custom_field_set_associations_item_custom_field_set import (
        MattercreateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet,
    )


T = TypeVar("T", bound="MattercreateFilesBodyDataCustomFieldSetAssociationsItem")


@_attrs_define
class MattercreateFilesBodyDataCustomFieldSetAssociationsItem:
    """
    Attributes:
        custom_field_set (MattercreateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet):
        display_order (Union[Unset, int]): The order to display the CustomFieldSet in a Matter. If not specified, it is
            added as the last CustomFieldSet of the Matter.
    """

    custom_field_set: "MattercreateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet"
    display_order: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_field_set = self.custom_field_set.to_dict()

        display_order = self.display_order

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "custom_field_set": custom_field_set,
            }
        )
        if display_order is not UNSET:
            field_dict["display_order"] = display_order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mattercreate_files_body_data_custom_field_set_associations_item_custom_field_set import (
            MattercreateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet,
        )

        d = dict(src_dict)
        custom_field_set = MattercreateFilesBodyDataCustomFieldSetAssociationsItemCustomFieldSet.from_dict(
            d.pop("custom_field_set")
        )

        display_order = d.pop("display_order", UNSET)

        mattercreate_files_body_data_custom_field_set_associations_item = cls(
            custom_field_set=custom_field_set,
            display_order=display_order,
        )

        mattercreate_files_body_data_custom_field_set_associations_item.additional_properties = d
        return mattercreate_files_body_data_custom_field_set_associations_item

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
