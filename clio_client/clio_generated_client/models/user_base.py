import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_base_subscription_type import UserBaseSubscriptionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBase")


@_attrs_define
class UserBase:
    """
    Attributes:
        account_owner (Union[Unset, bool]): Whether the *User* is the owner of the account
        clio_connect (Union[Unset, bool]): Whether the *User* is a Clio Connect user
        court_rules_default_attendee (Union[Unset, bool]): Whether the *User* is a default attendee for court rules
            events
        created_at (Union[Unset, datetime.datetime]): The time the *User* was created (as a ISO-8601 timestamp)
        default_calendar_id (Union[Unset, int]): Default calendar id for *User*.
        email (Union[Unset, str]): The email of the *User*
        enabled (Union[Unset, bool]): Whether the *User* is allowed to log in
        etag (Union[Unset, str]): ETag for the *User*
        first_name (Union[Unset, str]): The first name of the *User*
        id (Union[Unset, int]): Unique identifier for the *User*
        initials (Union[Unset, str]): The initials of the *User*
        last_name (Union[Unset, str]): The last name of the *User*
        name (Union[Unset, str]): The full name of the *User*
        phone_number (Union[Unset, str]): The primary phone number for the *User*.
        rate (Union[Unset, float]): Default user activity rate for *User*.
        roles (Union[Unset, list[str]]): An array of roles assigned to this *User*
        subscription_type (Union[Unset, UserBaseSubscriptionType]): The subscription type of the *User*
        time_zone (Union[Unset, str]): The selected time zone of the *User*
        updated_at (Union[Unset, datetime.datetime]): The time the *User* was last updated (as a ISO-8601 timestamp)
    """

    account_owner: Union[Unset, bool] = UNSET
    clio_connect: Union[Unset, bool] = UNSET
    court_rules_default_attendee: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    default_calendar_id: Union[Unset, int] = UNSET
    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    initials: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    rate: Union[Unset, float] = UNSET
    roles: Union[Unset, list[str]] = UNSET
    subscription_type: Union[Unset, UserBaseSubscriptionType] = UNSET
    time_zone: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_owner = self.account_owner

        clio_connect = self.clio_connect

        court_rules_default_attendee = self.court_rules_default_attendee

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        default_calendar_id = self.default_calendar_id

        email = self.email

        enabled = self.enabled

        etag = self.etag

        first_name = self.first_name

        id = self.id

        initials = self.initials

        last_name = self.last_name

        name = self.name

        phone_number = self.phone_number

        rate = self.rate

        roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = self.roles

        subscription_type: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_type, Unset):
            subscription_type = self.subscription_type.value

        time_zone = self.time_zone

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_owner is not UNSET:
            field_dict["account_owner"] = account_owner
        if clio_connect is not UNSET:
            field_dict["clio_connect"] = clio_connect
        if court_rules_default_attendee is not UNSET:
            field_dict["court_rules_default_attendee"] = court_rules_default_attendee
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_calendar_id is not UNSET:
            field_dict["default_calendar_id"] = default_calendar_id
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if etag is not UNSET:
            field_dict["etag"] = etag
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if initials is not UNSET:
            field_dict["initials"] = initials
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if name is not UNSET:
            field_dict["name"] = name
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if rate is not UNSET:
            field_dict["rate"] = rate
        if roles is not UNSET:
            field_dict["roles"] = roles
        if subscription_type is not UNSET:
            field_dict["subscription_type"] = subscription_type
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_owner = d.pop("account_owner", UNSET)

        clio_connect = d.pop("clio_connect", UNSET)

        court_rules_default_attendee = d.pop("court_rules_default_attendee", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        default_calendar_id = d.pop("default_calendar_id", UNSET)

        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        etag = d.pop("etag", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        initials = d.pop("initials", UNSET)

        last_name = d.pop("last_name", UNSET)

        name = d.pop("name", UNSET)

        phone_number = d.pop("phone_number", UNSET)

        rate = d.pop("rate", UNSET)

        roles = cast(list[str], d.pop("roles", UNSET))

        _subscription_type = d.pop("subscription_type", UNSET)
        subscription_type: Union[Unset, UserBaseSubscriptionType]
        if isinstance(_subscription_type, Unset):
            subscription_type = UNSET
        else:
            subscription_type = UserBaseSubscriptionType(_subscription_type)

        time_zone = d.pop("time_zone", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_base = cls(
            account_owner=account_owner,
            clio_connect=clio_connect,
            court_rules_default_attendee=court_rules_default_attendee,
            created_at=created_at,
            default_calendar_id=default_calendar_id,
            email=email,
            enabled=enabled,
            etag=etag,
            first_name=first_name,
            id=id,
            initials=initials,
            last_name=last_name,
            name=name,
            phone_number=phone_number,
            rate=rate,
            roles=roles,
            subscription_type=subscription_type,
            time_zone=time_zone,
            updated_at=updated_at,
        )

        user_base.additional_properties = d
        return user_base

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
