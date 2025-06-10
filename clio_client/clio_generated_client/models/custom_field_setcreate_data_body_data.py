from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_field_setcreate_data_body_data_parent_type import CustomFieldSetcreateDataBodyDataParentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldSetcreateDataBodyData")


@_attrs_define
class CustomFieldSetcreateDataBodyData:
    """
    Attributes:
        name (str): CustomFieldSet name.
        displayed (Union[Unset, bool]): Whether or not the CustomFieldSet should be displayed by default.
        parent_type (Union[Unset, CustomFieldSetcreateDataBodyDataParentType]): Type of object the CustomFieldSet is
            for.
    """

    name: str
    displayed: Union[Unset, bool] = UNSET
    parent_type: Union[Unset, CustomFieldSetcreateDataBodyDataParentType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        displayed = self.displayed

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        displayed = d.pop("displayed", UNSET)

        _parent_type = d.pop("parent_type", UNSET)
        parent_type: Union[Unset, CustomFieldSetcreateDataBodyDataParentType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = CustomFieldSetcreateDataBodyDataParentType(_parent_type)

        custom_field_setcreate_data_body_data = cls(
            name=name,
            displayed=displayed,
            parent_type=parent_type,
        )

        custom_field_setcreate_data_body_data.additional_properties = d
        return custom_field_setcreate_data_body_data

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
