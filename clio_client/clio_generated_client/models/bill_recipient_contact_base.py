from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bill_recipient_contact_base_type import BillRecipientContactBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillRecipientContactBase")


@_attrs_define
class BillRecipientContactBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Contact*
        name (Union[Unset, str]): The full name of the *Contact*
        first_name (Union[Unset, str]): First name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        last_name (Union[Unset, str]): Last name of the Person
        type_ (Union[Unset, BillRecipientContactBaseType]): The type of the *Contact*
        primary_email_address (Union[Unset, str]): The primary email address associated with this *Contact*.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    type_: Union[Unset, BillRecipientContactBaseType] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        primary_email_address = self.primary_email_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, BillRecipientContactBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = BillRecipientContactBaseType(_type_)

        primary_email_address = d.pop("primary_email_address", UNSET)

        bill_recipient_contact_base = cls(
            id=id,
            name=name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            type_=type_,
            primary_email_address=primary_email_address,
        )

        bill_recipient_contact_base.additional_properties = d
        return bill_recipient_contact_base

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
