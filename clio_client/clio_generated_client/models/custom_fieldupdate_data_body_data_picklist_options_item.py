from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldupdateDataBodyDataPicklistOptionsItem")


@_attrs_define
class CustomFieldupdateDataBodyDataPicklistOptionsItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single PicklistOption associated with the CustomField. The
            keyword `null` is not valid for this field. Not required for creating new PicklistOptions, but required for
            updating or deleting existing ones.
        option (Union[Unset, str]): The option value.
        field_deleted (Union[Unset, bool]): Whether or not the PicklistOption should be deleted.
    """

    id: Union[Unset, int] = UNSET
    option: Union[Unset, str] = UNSET
    field_deleted: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        option = self.option

        field_deleted = self.field_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if option is not UNSET:
            field_dict["option"] = option
        if field_deleted is not UNSET:
            field_dict["_deleted"] = field_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        option = d.pop("option", UNSET)

        field_deleted = d.pop("_deleted", UNSET)

        custom_fieldupdate_data_body_data_picklist_options_item = cls(
            id=id,
            option=option,
            field_deleted=field_deleted,
        )

        custom_fieldupdate_data_body_data_picklist_options_item.additional_properties = d
        return custom_fieldupdate_data_body_data_picklist_options_item

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
