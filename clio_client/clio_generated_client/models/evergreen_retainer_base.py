import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EvergreenRetainerBase")


@_attrs_define
class EvergreenRetainerBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *EvergreenRetainer*
        created_at (Union[Unset, datetime.datetime]): The time the *EvergreenRetainer* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *EvergreenRetainer* was last updated (as a ISO-8601
            timestamp)
        etag (Union[Unset, str]): ETag for the *EvergreenRetainer*
        minimum_threshold (Union[Unset, float]): The trust balance threshold for the associated Matter. When the balance
            falls below the threshold, the retainer's associated recipients (firm users) will receive a notification.
    """

    id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    etag: Union[Unset, str] = UNSET
    minimum_threshold: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        etag = self.etag

        minimum_threshold = self.minimum_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if etag is not UNSET:
            field_dict["etag"] = etag
        if minimum_threshold is not UNSET:
            field_dict["minimum_threshold"] = minimum_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

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

        etag = d.pop("etag", UNSET)

        minimum_threshold = d.pop("minimum_threshold", UNSET)

        evergreen_retainer_base = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            etag=etag,
            minimum_threshold=minimum_threshold,
        )

        evergreen_retainer_base.additional_properties = d
        return evergreen_retainer_base

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
