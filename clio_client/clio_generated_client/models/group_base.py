import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.group_base_type import GroupBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupBase")


@_attrs_define
class GroupBase:
    """
    Attributes:
        client_connect_user (Union[Unset, bool]): Whether or not the Group is a UserGroup for a Clio Connect User
        etag (Union[Unset, str]): ETag for the *Group*
        id (Union[Unset, int]): Unique identifier for the *Group*
        name (Union[Unset, str]): The name of the *Group*
        type_ (Union[Unset, GroupBaseType]): The type of the *Group*
        updated_at (Union[Unset, datetime.datetime]): The time the *Group* was last updated (as a ISO-8601 timestamp)
    """

    client_connect_user: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    type_: Union[Unset, GroupBaseType] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_connect_user = self.client_connect_user

        etag = self.etag

        id = self.id

        name = self.name

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_connect_user is not UNSET:
            field_dict["client_connect_user"] = client_connect_user
        if etag is not UNSET:
            field_dict["etag"] = etag
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client_connect_user = d.pop("client_connect_user", UNSET)

        etag = d.pop("etag", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, GroupBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = GroupBaseType(_type_)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        group_base = cls(
            client_connect_user=client_connect_user,
            etag=etag,
            id=id,
            name=name,
            type_=type_,
            updated_at=updated_at,
        )

        group_base.additional_properties = d
        return group_base

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
