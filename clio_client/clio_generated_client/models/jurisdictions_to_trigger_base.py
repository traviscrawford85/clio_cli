import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="JurisdictionsToTriggerBase")


@_attrs_define
class JurisdictionsToTriggerBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *JurisdictionsToTrigger*
        etag (Union[Unset, str]): ETag for the *JurisdictionsToTrigger*
        system_id (Union[Unset, int]): Server id
        description (Union[Unset, str]): A detailed description of the *JurisdictionsToTrigger*
        do_not_recalculate (Union[Unset, bool]): Whether the associated dates should not be recalculated
        is_served (Union[Unset, bool]): Whether the user must select a Date Offset (Service Type)
        is_requirements_required (Union[Unset, bool]): Whether the trigger has requirements
        created_at (Union[Unset, datetime.datetime]): The time the *JurisdictionsToTrigger* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *JurisdictionsToTrigger* was last updated (as a
            ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    system_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    do_not_recalculate: Union[Unset, bool] = UNSET
    is_served: Union[Unset, bool] = UNSET
    is_requirements_required: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        system_id = self.system_id

        description = self.description

        do_not_recalculate = self.do_not_recalculate

        is_served = self.is_served

        is_requirements_required = self.is_requirements_required

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
        if system_id is not UNSET:
            field_dict["system_id"] = system_id
        if description is not UNSET:
            field_dict["description"] = description
        if do_not_recalculate is not UNSET:
            field_dict["do_not_recalculate"] = do_not_recalculate
        if is_served is not UNSET:
            field_dict["is_served"] = is_served
        if is_requirements_required is not UNSET:
            field_dict["is_requirements_required"] = is_requirements_required
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

        system_id = d.pop("system_id", UNSET)

        description = d.pop("description", UNSET)

        do_not_recalculate = d.pop("do_not_recalculate", UNSET)

        is_served = d.pop("is_served", UNSET)

        is_requirements_required = d.pop("is_requirements_required", UNSET)

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

        jurisdictions_to_trigger_base = cls(
            id=id,
            etag=etag,
            system_id=system_id,
            description=description,
            do_not_recalculate=do_not_recalculate,
            is_served=is_served,
            is_requirements_required=is_requirements_required,
            created_at=created_at,
            updated_at=updated_at,
        )

        jurisdictions_to_trigger_base.additional_properties = d
        return jurisdictions_to_trigger_base

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
