import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_field_base_field_type import CustomFieldBaseFieldType
from ..models.custom_field_base_parent_type import CustomFieldBaseParentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldBase")


@_attrs_define
class CustomFieldBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *CustomField*
        etag (Union[Unset, str]): ETag for the *CustomField*
        created_at (Union[Unset, datetime.datetime]): The time the *CustomField* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CustomField* was last updated (as a ISO-8601
            timestamp)
        name (Union[Unset, str]): The name of the *CustomField*
        parent_type (Union[Unset, CustomFieldBaseParentType]): Type of object the *CustomField* is for
        field_type (Union[Unset, CustomFieldBaseFieldType]): Field type of the *CustomField*
        displayed (Union[Unset, bool]): Whether the *CustomField* is displayed by default
        deleted (Union[Unset, bool]): Whether the *CustomField* is deleted for future use
        required (Union[Unset, bool]): Whether the *CustomField* requires a value
        display_order (Union[Unset, int]): The display position of the *CustomField*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    parent_type: Union[Unset, CustomFieldBaseParentType] = UNSET
    field_type: Union[Unset, CustomFieldBaseFieldType] = UNSET
    displayed: Union[Unset, bool] = UNSET
    deleted: Union[Unset, bool] = UNSET
    required: Union[Unset, bool] = UNSET
    display_order: Union[Unset, int] = UNSET
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

        name = self.name

        parent_type: Union[Unset, str] = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        displayed = self.displayed

        deleted = self.deleted

        required = self.required

        display_order = self.display_order

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
        if name is not UNSET:
            field_dict["name"] = name
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if displayed is not UNSET:
            field_dict["displayed"] = displayed
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if required is not UNSET:
            field_dict["required"] = required
        if display_order is not UNSET:
            field_dict["display_order"] = display_order

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

        name = d.pop("name", UNSET)

        _parent_type = d.pop("parent_type", UNSET)
        parent_type: Union[Unset, CustomFieldBaseParentType]
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = CustomFieldBaseParentType(_parent_type)

        _field_type = d.pop("field_type", UNSET)
        field_type: Union[Unset, CustomFieldBaseFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = CustomFieldBaseFieldType(_field_type)

        displayed = d.pop("displayed", UNSET)

        deleted = d.pop("deleted", UNSET)

        required = d.pop("required", UNSET)

        display_order = d.pop("display_order", UNSET)

        custom_field_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            parent_type=parent_type,
            field_type=field_type,
            displayed=displayed,
            deleted=deleted,
            required=required,
            display_order=display_order,
        )

        custom_field_base.additional_properties = d
        return custom_field_base

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
