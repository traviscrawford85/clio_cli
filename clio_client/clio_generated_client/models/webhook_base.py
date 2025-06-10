import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.webhook_base_events_item import WebhookBaseEventsItem
from ..models.webhook_base_model import WebhookBaseModel
from ..models.webhook_base_status import WebhookBaseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookBase")


@_attrs_define
class WebhookBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Webhook*
        etag (Union[Unset, str]): ETag for the *Webhook*
        url (Union[Unset, str]): The `https` URL to send the data to when the events are triggered
        fields (Union[Unset, str]): Fields to be included in the webhook request
        shared_secret (Union[Unset, str]): A shared secret used to create a signature for the payload
        model (Union[Unset, WebhookBaseModel]): What kind of records the webhook is for
        status (Union[Unset, WebhookBaseStatus]): The current status of the webhook.
        events (Union[Unset, list[WebhookBaseEventsItem]]): The events your webhook is subscribed to.
        expires_at (Union[Unset, datetime.datetime]): The time webhook will expire (as a ISO-8601 timestamp)
        created_at (Union[Unset, datetime.datetime]): The time the *Webhook* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Webhook* was last updated (as a ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    fields: Union[Unset, str] = UNSET
    shared_secret: Union[Unset, str] = UNSET
    model: Union[Unset, WebhookBaseModel] = UNSET
    status: Union[Unset, WebhookBaseStatus] = UNSET
    events: Union[Unset, list[WebhookBaseEventsItem]] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        url = self.url

        fields = self.fields

        shared_secret = self.shared_secret

        model: Union[Unset, str] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        events: Union[Unset, list[str]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if url is not UNSET:
            field_dict["url"] = url
        if fields is not UNSET:
            field_dict["fields"] = fields
        if shared_secret is not UNSET:
            field_dict["shared_secret"] = shared_secret
        if model is not UNSET:
            field_dict["model"] = model
        if status is not UNSET:
            field_dict["status"] = status
        if events is not UNSET:
            field_dict["events"] = events
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        url = d.pop("url", UNSET)

        fields = d.pop("fields", UNSET)

        shared_secret = d.pop("shared_secret", UNSET)

        _model = d.pop("model", UNSET)
        model: Union[Unset, WebhookBaseModel]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = WebhookBaseModel(_model)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WebhookBaseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookBaseStatus(_status)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WebhookBaseEventsItem(events_item_data)

            events.append(events_item)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

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

        webhook_base = cls(
            id=id,
            etag=etag,
            url=url,
            fields=fields,
            shared_secret=shared_secret,
            model=model,
            status=status,
            events=events,
            expires_at=expires_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhook_base.additional_properties = d
        return webhook_base

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
