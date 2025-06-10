import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.contact_base_type import ContactBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_base_currency import ContactBaseCurrency


T = TypeVar("T", bound="ContactBase")


@_attrs_define
class ContactBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Contact*
        etag (Union[Unset, str]): ETag for the *Contact*
        name (Union[Unset, str]): The full name of the *Contact*
        first_name (Union[Unset, str]): First name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        last_name (Union[Unset, str]): Last name of the Person
        date_of_birth (Union[Unset, datetime.date]): Date of birth
        type_ (Union[Unset, ContactBaseType]): The type of the *Contact*
        created_at (Union[Unset, datetime.datetime]): The time the *Contact* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Contact* was last updated (as a ISO-8601 timestamp)
        prefix (Union[Unset, str]): The prefix of the *Contact* (Mr, Mrs, etc)
        title (Union[Unset, str]): The designated title of the *Contact*
        initials (Union[Unset, str]): The initials of the *Contact*
        clio_connect_email (Union[Unset, str]): Clio Connect email if the *Contact* is a ClioConnect User
        locked_clio_connect_email (Union[Unset, bool]): A boolean indicating if the ability to modify this *Contacts
            Clio connect email is locked.
        client_connect_user_id (Union[Unset, int]): The ID for the Clio Connect user associated with this *Contact*
        primary_email_address (Union[Unset, str]): The primary email address associated with this *Contact*.
        secondary_email_address (Union[Unset, str]): The secondary email address associated with this *Contact*.
        primary_phone_number (Union[Unset, str]): The primary phone number associated with this *Contact*.
        secondary_phone_number (Union[Unset, str]): The secondary phone number of the *Contact*.
        ledes_client_id (Union[Unset, str]): LEDES client id of the Contact
        has_clio_for_clients_permission (Union[Unset, bool]): True if at least one resource has been shared with the
            contact using Clio for Clients.
        is_client (Union[Unset, bool]): Whether or not the Contact is a client
        is_clio_for_client_user (Union[Unset, bool]): Whether or not this contact has client_login and client_user (can
            be created due to addition to client portal or client_share_permissions)
        is_co_counsel (Union[Unset, bool]): Whether or not the Contact has matters shared as co-counsel
        is_bill_recipient (Union[Unset, bool]): Whether the Contact is a bill recipient on at least one matter.
        sales_tax_number (Union[Unset, str]): The sales tax number of the *Contact*
        currency (Union[Unset, ContactBaseCurrency]): Currency of the *Contact*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    type_: Union[Unset, ContactBaseType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    prefix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    clio_connect_email: Union[Unset, str] = UNSET
    locked_clio_connect_email: Union[Unset, bool] = UNSET
    client_connect_user_id: Union[Unset, int] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    secondary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    secondary_phone_number: Union[Unset, str] = UNSET
    ledes_client_id: Union[Unset, str] = UNSET
    has_clio_for_clients_permission: Union[Unset, bool] = UNSET
    is_client: Union[Unset, bool] = UNSET
    is_clio_for_client_user: Union[Unset, bool] = UNSET
    is_co_counsel: Union[Unset, bool] = UNSET
    is_bill_recipient: Union[Unset, bool] = UNSET
    sales_tax_number: Union[Unset, str] = UNSET
    currency: Union[Unset, "ContactBaseCurrency"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

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

        clio_connect_email = self.clio_connect_email

        locked_clio_connect_email = self.locked_clio_connect_email

        client_connect_user_id = self.client_connect_user_id

        primary_email_address = self.primary_email_address

        secondary_email_address = self.secondary_email_address

        primary_phone_number = self.primary_phone_number

        secondary_phone_number = self.secondary_phone_number

        ledes_client_id = self.ledes_client_id

        has_clio_for_clients_permission = self.has_clio_for_clients_permission

        is_client = self.is_client

        is_clio_for_client_user = self.is_clio_for_client_user

        is_co_counsel = self.is_co_counsel

        is_bill_recipient = self.is_bill_recipient

        sales_tax_number = self.sales_tax_number

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
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
        if clio_connect_email is not UNSET:
            field_dict["clio_connect_email"] = clio_connect_email
        if locked_clio_connect_email is not UNSET:
            field_dict["locked_clio_connect_email"] = locked_clio_connect_email
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address
        if secondary_email_address is not UNSET:
            field_dict["secondary_email_address"] = secondary_email_address
        if primary_phone_number is not UNSET:
            field_dict["primary_phone_number"] = primary_phone_number
        if secondary_phone_number is not UNSET:
            field_dict["secondary_phone_number"] = secondary_phone_number
        if ledes_client_id is not UNSET:
            field_dict["ledes_client_id"] = ledes_client_id
        if has_clio_for_clients_permission is not UNSET:
            field_dict["has_clio_for_clients_permission"] = has_clio_for_clients_permission
        if is_client is not UNSET:
            field_dict["is_client"] = is_client
        if is_clio_for_client_user is not UNSET:
            field_dict["is_clio_for_client_user"] = is_clio_for_client_user
        if is_co_counsel is not UNSET:
            field_dict["is_co_counsel"] = is_co_counsel
        if is_bill_recipient is not UNSET:
            field_dict["is_bill_recipient"] = is_bill_recipient
        if sales_tax_number is not UNSET:
            field_dict["sales_tax_number"] = sales_tax_number
        if currency is not UNSET:
            field_dict["currency"] = currency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_base_currency import ContactBaseCurrency

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ContactBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContactBaseType(_type_)

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

        clio_connect_email = d.pop("clio_connect_email", UNSET)

        locked_clio_connect_email = d.pop("locked_clio_connect_email", UNSET)

        client_connect_user_id = d.pop("client_connect_user_id", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        secondary_email_address = d.pop("secondary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        secondary_phone_number = d.pop("secondary_phone_number", UNSET)

        ledes_client_id = d.pop("ledes_client_id", UNSET)

        has_clio_for_clients_permission = d.pop("has_clio_for_clients_permission", UNSET)

        is_client = d.pop("is_client", UNSET)

        is_clio_for_client_user = d.pop("is_clio_for_client_user", UNSET)

        is_co_counsel = d.pop("is_co_counsel", UNSET)

        is_bill_recipient = d.pop("is_bill_recipient", UNSET)

        sales_tax_number = d.pop("sales_tax_number", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ContactBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ContactBaseCurrency.from_dict(_currency)

        contact_base = cls(
            id=id,
            etag=etag,
            name=name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            prefix=prefix,
            title=title,
            initials=initials,
            clio_connect_email=clio_connect_email,
            locked_clio_connect_email=locked_clio_connect_email,
            client_connect_user_id=client_connect_user_id,
            primary_email_address=primary_email_address,
            secondary_email_address=secondary_email_address,
            primary_phone_number=primary_phone_number,
            secondary_phone_number=secondary_phone_number,
            ledes_client_id=ledes_client_id,
            has_clio_for_clients_permission=has_clio_for_clients_permission,
            is_client=is_client,
            is_clio_for_client_user=is_clio_for_client_user,
            is_co_counsel=is_co_counsel,
            is_bill_recipient=is_bill_recipient,
            sales_tax_number=sales_tax_number,
            currency=currency,
        )

        contact_base.additional_properties = d
        return contact_base

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
