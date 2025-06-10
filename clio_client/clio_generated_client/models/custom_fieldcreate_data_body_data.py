from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.custom_fieldcreate_data_body_data_field_type import CustomFieldcreateDataBodyDataFieldType
from ..models.custom_fieldcreate_data_body_data_parent_type import CustomFieldcreateDataBodyDataParentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_fieldcreate_data_body_data_picklist_options_item import (
        CustomFieldcreateDataBodyDataPicklistOptionsItem,
    )


T = TypeVar("T", bound="CustomFieldcreateDataBodyData")


@_attrs_define
class CustomFieldcreateDataBodyData:
    """
    Attributes:
        field_type (CustomFieldcreateDataBodyDataFieldType): Field type of the CustomField.
        name (str): CustomField name.
        parent_type (CustomFieldcreateDataBodyDataParentType): Type of object the CustomField is for.
        display_order (Union[Unset, int]): The display position of the CustomField.
        displayed (Union[Unset, bool]): Whether or not the CustomField should be displayed by default. Default: True.
        picklist_options (Union[Unset, list['CustomFieldcreateDataBodyDataPicklistOptionsItem']]):
        required (Union[Unset, bool]): Whether or not the CustomField should require a value. Default: False.
    """

    field_type: CustomFieldcreateDataBodyDataFieldType
    name: str
    parent_type: CustomFieldcreateDataBodyDataParentType
    display_order: Union[Unset, int] = UNSET
    displayed: Union[Unset, bool] = True
    picklist_options: Union[Unset, list["CustomFieldcreateDataBodyDataPicklistOptionsItem"]] = UNSET
    required: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_type = self.field_type.value

        name = self.name

        parent_type = self.parent_type.value

        display_order = self.display_order

        displayed = self.displayed

        picklist_options: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.picklist_options, Unset):
            picklist_options = []
            for picklist_options_item_data in self.picklist_options:
                picklist_options_item = picklist_options_item_data.to_dict()
                picklist_options.append(picklist_options_item)

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_type": field_type,
                "name": name,
                "parent_type": parent_type,
            }
        )
        if display_order is not UNSET:
            field_dict["display_order"] = display_order
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if picklist_options is not UNSET:
            field_dict["picklist_options"] = picklist_options
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_fieldcreate_data_body_data_picklist_options_item import (
            CustomFieldcreateDataBodyDataPicklistOptionsItem,
        )

        d = dict(src_dict)
        field_type = CustomFieldcreateDataBodyDataFieldType(d.pop("field_type"))

        name = d.pop("name")

        parent_type = CustomFieldcreateDataBodyDataParentType(d.pop("parent_type"))

        display_order = d.pop("display_order", UNSET)

        displayed = d.pop("displayed", UNSET)

        picklist_options = []
        _picklist_options = d.pop("picklist_options", UNSET)
        for picklist_options_item_data in _picklist_options or []:
            picklist_options_item = CustomFieldcreateDataBodyDataPicklistOptionsItem.from_dict(
                picklist_options_item_data
            )

            picklist_options.append(picklist_options_item)

        required = d.pop("required", UNSET)

        custom_fieldcreate_data_body_data = cls(
            field_type=field_type,
            name=name,
            parent_type=parent_type,
            display_order=display_order,
            displayed=displayed,
            picklist_options=picklist_options,
            required=required,
        )

        custom_fieldcreate_data_body_data.additional_properties = d
        return custom_fieldcreate_data_body_data

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
