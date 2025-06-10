import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.participant_base_type import ParticipantBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantBase")


@_attrs_define
class ParticipantBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Participant*
        etag (Union[Unset, str]): ETag for the *Participant*
        created_at (Union[Unset, datetime.datetime]): The time the *Participant* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Participant* was last updated (as a ISO-8601
            timestamp)
        type_ (Union[Unset, ParticipantBaseType]): The type of the Participant. Person and Company are subtypes of
            Contact
        identifier (Union[Unset, str]): A string to identify the *Participant*
        secondary_identifier (Union[Unset, str]): A secondary string to identify the *Participant*
        enabled (Union[Unset, bool]): The enabled state of the *Participant* record. Always 'null' if *Participant* type
            is Contact
        name (Union[Unset, str]): The name of the *Participant* record
        initials (Union[Unset, str]): A  string with the participant initials
        job_title_name (Union[Unset, str]): the job title name of the participant if they are a firm user and have one
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    type_: Union[Unset, ParticipantBaseType] = UNSET
    identifier: Union[Unset, str] = UNSET
    secondary_identifier: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    job_title_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        identifier = self.identifier

        secondary_identifier = self.secondary_identifier

        enabled = self.enabled

        name = self.name

        initials = self.initials

        job_title_name = self.job_title_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if secondary_identifier is not UNSET:
            field_dict["secondary_identifier"] = secondary_identifier
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if initials is not UNSET:
            field_dict["initials"] = initials
        if job_title_name is not UNSET:
            field_dict["job_title_name"] = job_title_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

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

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ParticipantBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ParticipantBaseType(_type_)

        identifier = d.pop("identifier", UNSET)

        secondary_identifier = d.pop("secondary_identifier", UNSET)

        enabled = d.pop("enabled", UNSET)

        name = d.pop("name", UNSET)

        initials = d.pop("initials", UNSET)

        job_title_name = d.pop("job_title_name", UNSET)

        participant_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            type_=type_,
            identifier=identifier,
            secondary_identifier=secondary_identifier,
            enabled=enabled,
            name=name,
            initials=initials,
            job_title_name=job_title_name,
        )

        participant_base.additional_properties = d
        return participant_base

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
