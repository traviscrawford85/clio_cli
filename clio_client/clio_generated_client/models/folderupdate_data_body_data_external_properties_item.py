from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FolderupdateDataBodyDataExternalPropertiesItem")


@_attrs_define
class FolderupdateDataBodyDataExternalPropertiesItem:
    """
    Attributes:
        id (Union[Unset, int]): The unique identifier for a single ExternalProperty associated with the Folder. The
            keyword `null` is not valid for this field.
        name (Union[Unset, str]): The ExternalProperty name. Note: **there is a limit of 5 external_properties per
            Folder**
        value (Union[Unset, str]): The ExternalProperty value.
        field_destroy (Union[Unset, bool]): The destroy flag. If the flag is set to `true` and the unique identifier of
            the associated ExternalProperty is present, the ExternalProperty is deleted from the Folder.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    field_destroy: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        value = self.value

        field_destroy = self.field_destroy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value
        if field_destroy is not UNSET:
            field_dict["_destroy"] = field_destroy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        field_destroy = d.pop("_destroy", UNSET)

        folderupdate_data_body_data_external_properties_item = cls(
            id=id,
            name=name,
            value=value,
            field_destroy=field_destroy,
        )

        folderupdate_data_body_data_external_properties_item.additional_properties = d
        return folderupdate_data_body_data_external_properties_item

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
