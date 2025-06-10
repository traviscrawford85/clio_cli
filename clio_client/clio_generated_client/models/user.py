import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.user_base_subscription_type import UserBaseSubscriptionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_base import AccountBase
    from ..models.activity_description_base import ActivityDescriptionBase
    from ..models.avatar_base import AvatarBase
    from ..models.contact_base import ContactBase
    from ..models.group_base import GroupBase
    from ..models.job_title_base import JobTitleBase
    from ..models.notification_method_base import NotificationMethodBase


T = TypeVar("T", bound="User")


@_attrs_define
class User:
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
        default_activity_description (Union[Unset, ActivityDescriptionBase]):
        notification_methods (Union[Unset, list['NotificationMethodBase']]): NotificationMethod
        account (Union[Unset, AccountBase]):
        avatar (Union[Unset, AvatarBase]):
        contact (Union[Unset, ContactBase]):
        job_title (Union[Unset, JobTitleBase]):
        groups (Union[Unset, list['GroupBase']]): Group
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
    default_activity_description: Union[Unset, "ActivityDescriptionBase"] = UNSET
    notification_methods: Union[Unset, list["NotificationMethodBase"]] = UNSET
    account: Union[Unset, "AccountBase"] = UNSET
    avatar: Union[Unset, "AvatarBase"] = UNSET
    contact: Union[Unset, "ContactBase"] = UNSET
    job_title: Union[Unset, "JobTitleBase"] = UNSET
    groups: Union[Unset, list["GroupBase"]] = UNSET
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

        default_activity_description: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_activity_description, Unset):
            default_activity_description = self.default_activity_description.to_dict()

        notification_methods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_methods, Unset):
            notification_methods = []
            for notification_methods_item_data in self.notification_methods:
                notification_methods_item = notification_methods_item_data.to_dict()
                notification_methods.append(notification_methods_item)

        account: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        job_title: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.job_title, Unset):
            job_title = self.job_title.to_dict()

        groups: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

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
        if default_activity_description is not UNSET:
            field_dict["default_activity_description"] = default_activity_description
        if notification_methods is not UNSET:
            field_dict["notification_methods"] = notification_methods
        if account is not UNSET:
            field_dict["account"] = account
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if contact is not UNSET:
            field_dict["contact"] = contact
        if job_title is not UNSET:
            field_dict["job_title"] = job_title
        if groups is not UNSET:
            field_dict["groups"] = groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_base import AccountBase
        from ..models.activity_description_base import ActivityDescriptionBase
        from ..models.avatar_base import AvatarBase
        from ..models.contact_base import ContactBase
        from ..models.group_base import GroupBase
        from ..models.job_title_base import JobTitleBase
        from ..models.notification_method_base import NotificationMethodBase

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

        _default_activity_description = d.pop("default_activity_description", UNSET)
        default_activity_description: Union[Unset, ActivityDescriptionBase]
        if isinstance(_default_activity_description, Unset):
            default_activity_description = UNSET
        else:
            default_activity_description = ActivityDescriptionBase.from_dict(_default_activity_description)

        notification_methods = []
        _notification_methods = d.pop("notification_methods", UNSET)
        for notification_methods_item_data in _notification_methods or []:
            notification_methods_item = NotificationMethodBase.from_dict(notification_methods_item_data)

            notification_methods.append(notification_methods_item)

        _account = d.pop("account", UNSET)
        account: Union[Unset, AccountBase]
        if isinstance(_account, Unset):
            account = UNSET
        else:
            account = AccountBase.from_dict(_account)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, AvatarBase]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = AvatarBase.from_dict(_avatar)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactBase]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactBase.from_dict(_contact)

        _job_title = d.pop("job_title", UNSET)
        job_title: Union[Unset, JobTitleBase]
        if isinstance(_job_title, Unset):
            job_title = UNSET
        else:
            job_title = JobTitleBase.from_dict(_job_title)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = GroupBase.from_dict(groups_item_data)

            groups.append(groups_item)

        user = cls(
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
            default_activity_description=default_activity_description,
            notification_methods=notification_methods,
            account=account,
            avatar=avatar,
            contact=contact,
            job_title=job_title,
            groups=groups,
        )

        user.additional_properties = d
        return user

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
