import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.communication_base_type import CommunicationBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base import ActivityBase
    from ..models.communication_eml_file_base import CommunicationEmlFileBase
    from ..models.document_base import DocumentBase
    from ..models.external_property_base import ExternalPropertyBase
    from ..models.matter_base import MatterBase
    from ..models.notification_event_subscriber_base import NotificationEventSubscriberBase
    from ..models.participant import Participant
    from ..models.user_base import UserBase


T = TypeVar("T", bound="Communication")


@_attrs_define
class Communication:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Communication*
        etag (Union[Unset, str]): ETag for the *Communication*
        subject (Union[Unset, str]): The subject line of the *Communication*
        body (Union[Unset, str]): The main content of the *Communication*
        type_ (Union[Unset, CommunicationBaseType]): The type of the *Communication*
        date (Union[Unset, datetime.date]): The date of the *Communication* (as a ISO-8601 datestamp)
        time_entries_count (Union[Unset, int]): The number of time_entries associated with the *Communication*
        created_at (Union[Unset, datetime.datetime]): The time the *Communication* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Communication* was last updated (as a ISO-8601
            timestamp)
        received_at (Union[Unset, datetime.datetime]): The date-time of the *Communication* (in ISO-8601 format)
        user (Union[Unset, UserBase]):
        matter (Union[Unset, MatterBase]):
        communication_eml_file (Union[Unset, CommunicationEmlFileBase]):
        senders (Union[Unset, list['Participant']]): Participant
        receivers (Union[Unset, list['Participant']]): Participant
        external_properties (Union[Unset, list['ExternalPropertyBase']]): ExternalProperty
        time_entries (Union[Unset, list['ActivityBase']]): Activity
        documents (Union[Unset, list['DocumentBase']]): Document
        notification_event_subscribers (Union[Unset, list['NotificationEventSubscriberBase']]):
            NotificationEventSubscriber
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    body: Union[Unset, str] = UNSET
    type_: Union[Unset, CommunicationBaseType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    time_entries_count: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    user: Union[Unset, "UserBase"] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    communication_eml_file: Union[Unset, "CommunicationEmlFileBase"] = UNSET
    senders: Union[Unset, list["Participant"]] = UNSET
    receivers: Union[Unset, list["Participant"]] = UNSET
    external_properties: Union[Unset, list["ExternalPropertyBase"]] = UNSET
    time_entries: Union[Unset, list["ActivityBase"]] = UNSET
    documents: Union[Unset, list["DocumentBase"]] = UNSET
    notification_event_subscribers: Union[Unset, list["NotificationEventSubscriberBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        subject = self.subject

        body = self.body

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        time_entries_count = self.time_entries_count

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        communication_eml_file: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.communication_eml_file, Unset):
            communication_eml_file = self.communication_eml_file.to_dict()

        senders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.senders, Unset):
            senders = []
            for senders_item_data in self.senders:
                senders_item = senders_item_data.to_dict()
                senders.append(senders_item)

        receivers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.receivers, Unset):
            receivers = []
            for receivers_item_data in self.receivers:
                receivers_item = receivers_item_data.to_dict()
                receivers.append(receivers_item)

        external_properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.external_properties, Unset):
            external_properties = []
            for external_properties_item_data in self.external_properties:
                external_properties_item = external_properties_item_data.to_dict()
                external_properties.append(external_properties_item)

        time_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.time_entries, Unset):
            time_entries = []
            for time_entries_item_data in self.time_entries:
                time_entries_item = time_entries_item_data.to_dict()
                time_entries.append(time_entries_item)

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

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
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body
        if type_ is not UNSET:
            field_dict["type"] = type_
        if date is not UNSET:
            field_dict["date"] = date
        if time_entries_count is not UNSET:
            field_dict["time_entries_count"] = time_entries_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if user is not UNSET:
            field_dict["user"] = user
        if matter is not UNSET:
            field_dict["matter"] = matter
        if communication_eml_file is not UNSET:
            field_dict["communication_eml_file"] = communication_eml_file
        if senders is not UNSET:
            field_dict["senders"] = senders
        if receivers is not UNSET:
            field_dict["receivers"] = receivers
        if external_properties is not UNSET:
            field_dict["external_properties"] = external_properties
        if time_entries is not UNSET:
            field_dict["time_entries"] = time_entries
        if documents is not UNSET:
            field_dict["documents"] = documents
        if notification_event_subscribers is not UNSET:
            field_dict["notification_event_subscribers"] = notification_event_subscribers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_base import ActivityBase
        from ..models.communication_eml_file_base import CommunicationEmlFileBase
        from ..models.document_base import DocumentBase
        from ..models.external_property_base import ExternalPropertyBase
        from ..models.matter_base import MatterBase
        from ..models.notification_event_subscriber_base import NotificationEventSubscriberBase
        from ..models.participant import Participant
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, CommunicationBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CommunicationBaseType(_type_)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        time_entries_count = d.pop("time_entries_count", UNSET)

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

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        _user = d.pop("user", UNSET)
        user: Union[Unset, UserBase]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UserBase.from_dict(_user)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _communication_eml_file = d.pop("communication_eml_file", UNSET)
        communication_eml_file: Union[Unset, CommunicationEmlFileBase]
        if isinstance(_communication_eml_file, Unset):
            communication_eml_file = UNSET
        else:
            communication_eml_file = CommunicationEmlFileBase.from_dict(_communication_eml_file)

        senders = []
        _senders = d.pop("senders", UNSET)
        for senders_item_data in _senders or []:
            senders_item = Participant.from_dict(senders_item_data)

            senders.append(senders_item)

        receivers = []
        _receivers = d.pop("receivers", UNSET)
        for receivers_item_data in _receivers or []:
            receivers_item = Participant.from_dict(receivers_item_data)

            receivers.append(receivers_item)

        external_properties = []
        _external_properties = d.pop("external_properties", UNSET)
        for external_properties_item_data in _external_properties or []:
            external_properties_item = ExternalPropertyBase.from_dict(external_properties_item_data)

            external_properties.append(external_properties_item)

        time_entries = []
        _time_entries = d.pop("time_entries", UNSET)
        for time_entries_item_data in _time_entries or []:
            time_entries_item = ActivityBase.from_dict(time_entries_item_data)

            time_entries.append(time_entries_item)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentBase.from_dict(documents_item_data)

            documents.append(documents_item)

        notification_event_subscribers = []
        _notification_event_subscribers = d.pop("notification_event_subscribers", UNSET)
        for notification_event_subscribers_item_data in _notification_event_subscribers or []:
            notification_event_subscribers_item = NotificationEventSubscriberBase.from_dict(
                notification_event_subscribers_item_data
            )

            notification_event_subscribers.append(notification_event_subscribers_item)

        communication = cls(
            id=id,
            etag=etag,
            subject=subject,
            body=body,
            type_=type_,
            date=date,
            time_entries_count=time_entries_count,
            created_at=created_at,
            updated_at=updated_at,
            received_at=received_at,
            user=user,
            matter=matter,
            communication_eml_file=communication_eml_file,
            senders=senders,
            receivers=receivers,
            external_properties=external_properties,
            time_entries=time_entries,
            documents=documents,
            notification_event_subscribers=notification_event_subscribers,
        )

        communication.additional_properties = d
        return communication

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
