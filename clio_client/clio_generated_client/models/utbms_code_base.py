import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.utbms_code_base_type import UtbmsCodeBaseType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UtbmsCodeBase")


@_attrs_define
class UtbmsCodeBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *UtbmsCode*
        etag (Union[Unset, str]): ETag for the *UtbmsCode*
        name (Union[Unset, str]): The name of the *UtbmsCode*
        code (Union[Unset, str]): The UTBMS code for the *UtbmsCode*
        description (Union[Unset, str]): The UTBMS description for the *UtbmsCode*
        type_ (Union[Unset, UtbmsCodeBaseType]): The type of the *UtbmsCode*
        utbms_set_id (Union[Unset, int]): Set id for the *UtbmsCode*
        created_at (Union[Unset, datetime.datetime]): The time the *UtbmsCode* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *UtbmsCode* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    type_: Union[Unset, UtbmsCodeBaseType] = UNSET
    utbms_set_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        code = self.code

        description = self.description

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        utbms_set_id = self.utbms_set_id

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
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if description is not UNSET:
            field_dict["description"] = description
        if type_ is not UNSET:
            field_dict["type"] = type_
        if utbms_set_id is not UNSET:
            field_dict["utbms_set_id"] = utbms_set_id
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

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        description = d.pop("description", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, UtbmsCodeBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UtbmsCodeBaseType(_type_)

        utbms_set_id = d.pop("utbms_set_id", UNSET)

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

        utbms_code_base = cls(
            id=id,
            etag=etag,
            name=name,
            code=code,
            description=description,
            type_=type_,
            utbms_set_id=utbms_set_id,
            created_at=created_at,
            updated_at=updated_at,
        )

        utbms_code_base.additional_properties = d
        return utbms_code_base

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
