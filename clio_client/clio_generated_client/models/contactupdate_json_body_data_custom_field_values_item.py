from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactupdate_json_body_data_custom_field_values_item_custom_field import (
        ContactupdateJsonBodyDataCustomFieldValuesItemCustomField,
    )


T = TypeVar("T", bound="ContactupdateJsonBodyDataCustomFieldValuesItem")


@_attrs_define
class ContactupdateJsonBodyDataCustomFieldValuesItem:
    """
    Attributes:
        value (Union[Unset, str]): The value of the CustomFieldValue.
        custom_field (Union[Unset, ContactupdateJsonBodyDataCustomFieldValuesItemCustomField]):
        id (Union[Unset, int]): The unique identifier for a single CustomFieldValue associated with the Contact. The
            keyword `null` is not valid for this field.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated CustomFieldValue is present, the CustomFieldValue is deleted from the Contact.
    """

    value: Union[Unset, str] = UNSET
    custom_field: Union[Unset, "ContactupdateJsonBodyDataCustomFieldValuesItemCustomField"] = UNSET
    id: Union[Unset, int] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        custom_field: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_field, Unset):
            custom_field = self.custom_field.to_dict()

        id = self.id

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if value is not UNSET:
            field_dict["value"] = value
        if custom_field is not UNSET:
            field_dict["custom_field"] = custom_field
        if id is not UNSET:
            field_dict["id"] = id
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactupdate_json_body_data_custom_field_values_item_custom_field import (
            ContactupdateJsonBodyDataCustomFieldValuesItemCustomField,
        )

        d = dict(src_dict)
        value = d.pop("value", UNSET)

        _custom_field = d.pop("custom_field", UNSET)
        custom_field: Union[Unset, ContactupdateJsonBodyDataCustomFieldValuesItemCustomField]
        if isinstance(_custom_field, Unset):
            custom_field = UNSET
        else:
            custom_field = ContactupdateJsonBodyDataCustomFieldValuesItemCustomField.from_dict(_custom_field)

        id = d.pop("id", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        contactupdate_json_body_data_custom_field_values_item = cls(
            value=value,
            custom_field=custom_field,
            id=id,
            field_destroy=field_destroy,
        )

        contactupdate_json_body_data_custom_field_values_item.additional_properties = d
        return contactupdate_json_body_data_custom_field_values_item

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
