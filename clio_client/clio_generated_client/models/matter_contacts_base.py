import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.matter_contacts_base_type import MatterContactsBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatterContactsBase")


@_attrs_define
class MatterContactsBase:
    """
    Attributes:
        contact_created_at (Union[Unset, datetime.datetime]): Timestamp of the time the contact was created
        contact_updated_at (Union[Unset, datetime.datetime]): Timestamp of the time the contact was created
        created_at (Union[Unset, datetime.datetime]): The time the *MatterContacts* was created (as a ISO-8601
            timestamp)
        description (Union[Unset, str]): Description of the matter
        etag (Union[Unset, str]): ETag for the *MatterContacts*
        first_name (Union[Unset, str]): First name of the Person
        id (Union[Unset, int]): Unique identifier for the *MatterContacts*
        initials (Union[Unset, str]): The initials of the *MatterContacts*
        is_client (Union[Unset, bool]): Whether or not the MatterContacts is a client
        last_name (Union[Unset, str]): Last name of the Person
        matter_id (Union[Unset, int]): ID of the matter
        matter_number (Union[Unset, str]): Number of the matter
        middle_name (Union[Unset, str]): Middle name of the Person
        name (Union[Unset, str]): The full name of the *MatterContacts*
        prefix (Union[Unset, str]): The prefix of the *MatterContacts* (Mr, Mrs, etc)
        primary_email_address (Union[Unset, str]): The primary email address associated with this *MatterContacts*.
        primary_phone_number (Union[Unset, str]): The primary phone number associated with this *MatterContacts*.
        relationship_name (Union[Unset, str]): The description of the relation between the contact and the matter, or
            "Client" if the user is the client.
        secondary_email_address (Union[Unset, str]): The secondary email address of the contact
        secondary_phone_number (Union[Unset, str]): The secondary phone number of the contact
        title (Union[Unset, str]): The designated title of the *MatterContacts*
        type_ (Union[Unset, MatterContactsBaseType]): The type of the *MatterContacts*
        updated_at (Union[Unset, datetime.datetime]): The time the *MatterContacts* was last updated (as a ISO-8601
            timestamp)
        client_connect_user_id (Union[Unset, int]): The client connect ID of the contacts associated user
    """

    contact_created_at: Union[Unset, datetime.datetime] = UNSET
    contact_updated_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    initials: Union[Unset, str] = UNSET
    is_client: Union[Unset, bool] = UNSET
    last_name: Union[Unset, str] = UNSET
    matter_id: Union[Unset, int] = UNSET
    matter_number: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    relationship_name: Union[Unset, str] = UNSET
    secondary_email_address: Union[Unset, str] = UNSET
    secondary_phone_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, MatterContactsBaseType] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    client_connect_user_id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contact_created_at: Union[Unset, str] = UNSET
        if not isinstance(self.contact_created_at, Unset):
            contact_created_at = self.contact_created_at.isoformat()

        contact_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.contact_updated_at, Unset):
            contact_updated_at = self.contact_updated_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        description = self.description

        etag = self.etag

        first_name = self.first_name

        id = self.id

        initials = self.initials

        is_client = self.is_client

        last_name = self.last_name

        matter_id = self.matter_id

        matter_number = self.matter_number

        middle_name = self.middle_name

        name = self.name

        prefix = self.prefix

        primary_email_address = self.primary_email_address

        primary_phone_number = self.primary_phone_number

        relationship_name = self.relationship_name

        secondary_email_address = self.secondary_email_address

        secondary_phone_number = self.secondary_phone_number

        title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        client_connect_user_id = self.client_connect_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_created_at is not UNSET:
            field_dict["contact_created_at"] = contact_created_at
        if contact_updated_at is not UNSET:
            field_dict["contact_updated_at"] = contact_updated_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if etag is not UNSET:
            field_dict["etag"] = etag
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if initials is not UNSET:
            field_dict["initials"] = initials
        if is_client is not UNSET:
            field_dict["is_client"] = is_client
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if matter_id is not UNSET:
            field_dict["matter_id"] = matter_id
        if matter_number is not UNSET:
            field_dict["matter_number"] = matter_number
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if name is not UNSET:
            field_dict["name"] = name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address
        if primary_phone_number is not UNSET:
            field_dict["primary_phone_number"] = primary_phone_number
        if relationship_name is not UNSET:
            field_dict["relationship_name"] = relationship_name
        if secondary_email_address is not UNSET:
            field_dict["secondary_email_address"] = secondary_email_address
        if secondary_phone_number is not UNSET:
            field_dict["secondary_phone_number"] = secondary_phone_number
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _contact_created_at = d.pop("contact_created_at", UNSET)
        contact_created_at: Union[Unset, datetime.datetime]
        if isinstance(_contact_created_at, Unset):
            contact_created_at = UNSET
        else:
            contact_created_at = isoparse(_contact_created_at)

        _contact_updated_at = d.pop("contact_updated_at", UNSET)
        contact_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_contact_updated_at, Unset):
            contact_updated_at = UNSET
        else:
            contact_updated_at = isoparse(_contact_updated_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        description = d.pop("description", UNSET)

        etag = d.pop("etag", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        initials = d.pop("initials", UNSET)

        is_client = d.pop("is_client", UNSET)

        last_name = d.pop("last_name", UNSET)

        matter_id = d.pop("matter_id", UNSET)

        matter_number = d.pop("matter_number", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        name = d.pop("name", UNSET)

        prefix = d.pop("prefix", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        relationship_name = d.pop("relationship_name", UNSET)

        secondary_email_address = d.pop("secondary_email_address", UNSET)

        secondary_phone_number = d.pop("secondary_phone_number", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MatterContactsBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MatterContactsBaseType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        client_connect_user_id = d.pop("client_connect_user_id", UNSET)

        matter_contacts_base = cls(
            contact_created_at=contact_created_at,
            contact_updated_at=contact_updated_at,
            created_at=created_at,
            description=description,
            etag=etag,
            first_name=first_name,
            id=id,
            initials=initials,
            is_client=is_client,
            last_name=last_name,
            matter_id=matter_id,
            matter_number=matter_number,
            middle_name=middle_name,
            name=name,
            prefix=prefix,
            primary_email_address=primary_email_address,
            primary_phone_number=primary_phone_number,
            relationship_name=relationship_name,
            secondary_email_address=secondary_email_address,
            secondary_phone_number=secondary_phone_number,
            title=title,
            type_=type_,
            updated_at=updated_at,
            client_connect_user_id=client_connect_user_id,
        )

        matter_contacts_base.additional_properties = d
        return matter_contacts_base

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
