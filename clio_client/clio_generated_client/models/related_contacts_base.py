import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.related_contacts_base_type import RelatedContactsBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RelatedContactsBase")


@_attrs_define
class RelatedContactsBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *RelatedContacts*
        contact_id (Union[Unset, int]): The id of the *RelatedContacts*
        name (Union[Unset, str]): The full name of the *RelatedContacts*
        first_name (Union[Unset, str]): First name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        last_name (Union[Unset, str]): Last name of the Person
        type_ (Union[Unset, RelatedContactsBaseType]): The type of the *RelatedContacts*
        created_at (Union[Unset, datetime.datetime]): The time the *RelatedContacts* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *RelatedContacts* was last updated (as a ISO-8601
            timestamp)
        prefix (Union[Unset, str]): The prefix of the *RelatedContacts* (Mr, Mrs, etc)
        title (Union[Unset, str]): The designated title of the *RelatedContacts*
        initials (Union[Unset, str]): The initials of the *RelatedContacts*
        is_matter_client (Union[Unset, bool]): Whether or not the RelatedContacts is also the client of the matter
        primary_email_address (Union[Unset, str]): The primary email address of related contact
        primary_phone_number (Union[Unset, str]): The primary phone number of related contact
        client_connect_user_id (Union[Unset, int]): The client connect ID of the contacts associated user
    """

    id: Union[Unset, int] = UNSET
    contact_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    type_: Union[Unset, RelatedContactsBaseType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    prefix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    is_matter_client: Union[Unset, bool] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    client_connect_user_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contact_id = self.contact_id

        name = self.name

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        prefix = self.prefix

        title = self.title

        initials = self.initials

        is_matter_client = self.is_matter_client

        primary_email_address = self.primary_email_address

        primary_phone_number = self.primary_phone_number

        client_connect_user_id = self.client_connect_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if title is not UNSET:
            field_dict["title"] = title
        if initials is not UNSET:
            field_dict["initials"] = initials
        if is_matter_client is not UNSET:
            field_dict["is_matter_client"] = is_matter_client
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address
        if primary_phone_number is not UNSET:
            field_dict["primary_phone_number"] = primary_phone_number
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        contact_id = d.pop("contact_id", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, RelatedContactsBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RelatedContactsBaseType(_type_)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        prefix = d.pop("prefix", UNSET)

        title = d.pop("title", UNSET)

        initials = d.pop("initials", UNSET)

        is_matter_client = d.pop("is_matter_client", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        client_connect_user_id = d.pop("client_connect_user_id", UNSET)

        related_contacts_base = cls(
            id=id,
            contact_id=contact_id,
            name=name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            prefix=prefix,
            title=title,
            initials=initials,
            is_matter_client=is_matter_client,
            primary_email_address=primary_email_address,
            primary_phone_number=primary_phone_number,
            client_connect_user_id=client_connect_user_id,
        )

        related_contacts_base.additional_properties = d
        return related_contacts_base

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
