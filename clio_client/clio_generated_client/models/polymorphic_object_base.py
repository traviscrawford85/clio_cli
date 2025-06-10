from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymorphic_object_base_type import PolymorphicObjectBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymorphicObjectBase")


@_attrs_define
class PolymorphicObjectBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *PolymorphicObject*
        type_ (Union[Unset, PolymorphicObjectBaseType]): The type of the *PolymorphicObject*
        identifier (Union[Unset, str]): A string to identify the *PolymorphicObject*
        secondary_identifier (Union[Unset, str]): A secondary string to identify the *PolymorphicObject*
        tertiary_identifier (Union[Unset, str]): A tertiary string to identify the *PolymorphicObject*
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, PolymorphicObjectBaseType] = UNSET
    identifier: Union[Unset, str] = UNSET
    secondary_identifier: Union[Unset, str] = UNSET
    tertiary_identifier: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identifier = self.identifier

        secondary_identifier = self.secondary_identifier

        tertiary_identifier = self.tertiary_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if secondary_identifier is not UNSET:
            field_dict["secondary_identifier"] = secondary_identifier
        if tertiary_identifier is not UNSET:
            field_dict["tertiary_identifier"] = tertiary_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PolymorphicObjectBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PolymorphicObjectBaseType(_type_)

        identifier = d.pop("identifier", UNSET)

        secondary_identifier = d.pop("secondary_identifier", UNSET)

        tertiary_identifier = d.pop("tertiary_identifier", UNSET)

        polymorphic_object_base = cls(
            id=id,
            type_=type_,
            identifier=identifier,
            secondary_identifier=secondary_identifier,
            tertiary_identifier=tertiary_identifier,
        )

        polymorphic_object_base.additional_properties = d
        return polymorphic_object_base

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
