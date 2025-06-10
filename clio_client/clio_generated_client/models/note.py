import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.note_base_detail_text_type import NoteBaseDetailTextType
from ..models.note_base_type import NoteBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.contact_base import ContactBase
    from ..models.matter_base import MatterBase
    from ..models.notification_event_subscriber_base import NotificationEventSubscriberBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Note")


@_attrs_define
class Note:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Note*
        etag (Union[Unset, str]): ETag for the *Note*
        type_ (Union[Unset, NoteBaseType]): The type of the *Note*
        subject (Union[Unset, str]): The subject of the *Note*
        detail (Union[Unset, str]): The text body of the *Note*. This Note supports rich text when setting the field
            `detail_text_type` to `rich_text`. With supported tags such as `<a>`, `<b>`, `<br>`, `<div>`, `<em>`, `<i>`
            `<li>`, `<ol>`, `<p>`, `<s>`, `<strong>`, `<u>` and `<ul>`. This Note also supports attributes such as `href`,
            `rel`, `type`, and `target`.
        detail_text_type (Union[Unset, NoteBaseDetailTextType]): The text type of the *Note*
        date (Union[Unset, datetime.date]): The date the *Note* is for (as a ISO-8601 date)
        created_at (Union[Unset, datetime.datetime]): The time the *Note* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Note* was last updated (as a ISO-8601 timestamp)
        time_entries_count (Union[Unset, int]): The number of time_entries associated with the *Note*
        matter (Union[Unset, MatterBase]):
        contact (Union[Unset, ContactBase]):
        author (Union[Unset, UserBase]):
        time_entries (Union[Unset, list['ActivityBase']]): Activity
        notification_event_subscribers (Union[Unset, list['NotificationEventSubscriberBase']]):
            NotificationEventSubscriber
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    type_: Union[Unset, NoteBaseType] = UNSET
    subject: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    detail_text_type: Union[Unset, NoteBaseDetailTextType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    contact: Union[Unset, "ContactBase"] = UNSET
    author: Union[Unset, "UserBase"] = UNSET
    time_entries: Union[Unset, list["ActivityBase"]] = UNSET
    notification_event_subscribers: Union[Unset, list["NotificationEventSubscriberBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        subject = self.subject

        detail = self.detail

        detail_text_type: Union[Unset, str] = UNSET
        if not isinstance(self.detail_text_type, Unset):
            detail_text_type = self.detail_text_type.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        time_entries_count = self.time_entries_count

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact, Unset):
            contact = self.contact.to_dict()

        author: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.author, Unset):
            author = self.author.to_dict()

        time_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

        notification_event_subscribers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_event_subscribers, Unset):
            notification_event_subscribers = []
            for notification_event_subscribers_item_data in self.notification_event_subscribers:
                notification_event_subscribers_item = notification_event_subscribers_item_data.to_dict()
                notification_event_subscribers.append(notification_event_subscribers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subject is not UNSET:
            field_dict["subject"] = subject
        if detail is not UNSET:
            field_dict["detail"] = detail
        if detail_text_type is not UNSET:
            field_dict["detail_text_type"] = detail_text_type
        if date is not UNSET:
            field_dict["date"] = date
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if matter is not UNSET:
            field_dict["matter"] = matter
        if contact is not UNSET:
            field_dict["contact"] = contact
        if author is not UNSET:
            field_dict["author"] = author
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.contact_base import ContactBase
        from ..models.matter_base import MatterBase
        from ..models.notification_event_subscriber_base import NotificationEventSubscriberBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, NoteBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = NoteBaseType(_type_)

        subject = d.pop("subject", UNSET)

        detail = d.pop("detail", UNSET)

        _detail_text_type = d.pop("detail_text_type", UNSET)
        detail_text_type: Union[Unset, NoteBaseDetailTextType]
        if isinstance(_detail_text_type, Unset):
            detail_text_type = UNSET
        else:
            detail_text_type = NoteBaseDetailTextType(_detail_text_type)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

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

        time_entries_count = d.pop("time_entries_count", UNSET)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _contact = d.pop("contact", UNSET)
        contact: Union[Unset, ContactBase]
        if isinstance(_contact, Unset):
            contact = UNSET
        else:
            contact = ContactBase.from_dict(_contact)

        _author = d.pop("author", UNSET)
        author: Union[Unset, UserBase]
        if isinstance(_author, Unset):
            author = UNSET
        else:
            author = UserBase.from_dict(_author)

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = NotificationEventSubscriberBase.from_dict(
                notification_event_subscribers_item_data
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        note = cls(
            id=id,
            etag=etag,
            type_=type_,
            subject=subject,
            detail=detail,
            detail_text_type=detail_text_type,
            date=date,
            created_at=created_at,
            updated_at=updated_at,
            time_entries_count=time_entries_count,
            matter=matter,
            contact=contact,
            author=author,
            time_entries=time_entries,
            notification_event_subscribers=notification_event_subscribers,
        )

        note.additional_properties = d
        return note

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
