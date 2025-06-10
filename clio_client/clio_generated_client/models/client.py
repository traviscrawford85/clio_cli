import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.client_base_type import ClientBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_base import AddressBase
    from ..models.avatar_base import AvatarBase
    from ..models.contact_base import ContactBase
    from ..models.email_address_base import EmailAddressBase
    from ..models.phone_number_base import PhoneNumberBase
    from ..models.web_site_base import WebSiteBase


T = TypeVar("T", bound="Client")


@_attrs_define
class Client:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Client*
        name (Union[Unset, str]): The full name of the *Client*
        first_name (Union[Unset, str]): First name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        last_name (Union[Unset, str]): Last name of the Person
        type_ (Union[Unset, ClientBaseType]): The type of the *Client*
        created_at (Union[Unset, datetime.datetime]): The time the *Client* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Client* was last updated (as a ISO-8601 timestamp)
        prefix (Union[Unset, str]): The prefix of the *Client* (Mr, Mrs, etc)
        title (Union[Unset, str]): The designated title of the *Client*
        initials (Union[Unset, str]): The initials of the *Client*
        is_matter_client (Union[Unset, bool]): Whether or not the Client is also the client of the matter
        primary_email_address (Union[Unset, str]): The primary email address of client
        primary_phone_number (Union[Unset, str]): The primary phone number of client
        client_connect_user_id (Union[Unset, int]): The client connect ID of the contacts associated user
        date_of_birth (Union[Unset, datetime.date]): Date of Birth
        avatar (Union[Unset, AvatarBase]):
        company (Union[Unset, ContactBase]):
        addresses (Union[Unset, list['AddressBase']]): Address
        email_addresses (Union[Unset, list['EmailAddressBase']]): EmailAddress
        phone_numbers (Union[Unset, list['PhoneNumberBase']]): PhoneNumber
        web_sites (Union[Unset, list['WebSiteBase']]): WebSite
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    type_: Union[Unset, ClientBaseType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    prefix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    is_matter_client: Union[Unset, bool] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    client_connect_user_id: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    avatar: Union[Unset, "AvatarBase"] = UNSET
    company: Union[Unset, "ContactBase"] = UNSET
    addresses: Union[Unset, list["AddressBase"]] = UNSET
    email_addresses: Union[Unset, list["EmailAddressBase"]] = UNSET
    phone_numbers: Union[Unset, list["PhoneNumberBase"]] = UNSET
    web_sites: Union[Unset, list["WebSiteBase"]] = UNSET
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

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        email_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = []
            for email_addresses_item_data in self.email_addresses:
                email_addresses_item = email_addresses_item_data.to_dict()
                email_addresses.append(email_addresses_item)

        phone_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        web_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.web_sites, Unset):
            web_sites = []
            for web_sites_item_data in self.web_sites:
                web_sites_item = web_sites_item_data.to_dict()
                web_sites.append(web_sites_item)

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
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if company is not UNSET:
            field_dict["company"] = company
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if email_addresses is not UNSET:
            field_dict["email_addresses"] = email_addresses
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if web_sites is not UNSET:
            field_dict["web_sites"] = web_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_base import AddressBase
        from ..models.avatar_base import AvatarBase
        from ..models.contact_base import ContactBase
        from ..models.email_address_base import EmailAddressBase
        from ..models.phone_number_base import PhoneNumberBase
        from ..models.web_site_base import WebSiteBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ClientBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ClientBaseType(_type_)

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

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, AvatarBase]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = AvatarBase.from_dict(_avatar)

        _company = d.pop("company", UNSET)
        company: Union[Unset, ContactBase]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = ContactBase.from_dict(_company)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = AddressBase.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        email_addresses = []
        _email_addresses = d.pop("email_addresses", UNSET)
        for email_addresses_item_data in _email_addresses or []:
            email_addresses_item = EmailAddressBase.from_dict(email_addresses_item_data)

            email_addresses.append(email_addresses_item)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = PhoneNumberBase.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        web_sites = []
        _web_sites = d.pop("web_sites", UNSET)
        for web_sites_item_data in _web_sites or []:
            web_sites_item = WebSiteBase.from_dict(web_sites_item_data)

            web_sites.append(web_sites_item)

        client = cls(
            id=id,
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
            date_of_birth=date_of_birth,
            avatar=avatar,
            company=company,
            addresses=addresses,
            email_addresses=email_addresses,
            phone_numbers=phone_numbers,
            web_sites=web_sites,
        )

        client.additional_properties = d
        return client

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
