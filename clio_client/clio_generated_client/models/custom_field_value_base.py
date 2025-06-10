import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_field_value_base_field_type import CustomFieldValueBaseFieldType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomFieldValueBase")


@_attrs_define
class CustomFieldValueBase:
    """
    Attributes:
        id (Union[Unset, str]): Unique identifier for the *CustomFieldValue*
        etag (Union[Unset, str]): ETag for the *CustomFieldValue*
        field_name (Union[Unset, str]): The name of the custom field
        created_at (Union[Unset, datetime.datetime]): The time the *CustomFieldValue* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CustomFieldValue* was last updated (as a ISO-8601
            timestamp)
        field_type (Union[Unset, CustomFieldValueBaseFieldType]): The type of the *CustomFieldValue*
        field_required (Union[Unset, bool]): Whether the *CustomFieldValue* requires a value
        field_displayed (Union[Unset, bool]): Whether the *CustomFieldValue* is displayed by default
        field_display_order (Union[Unset, int]): The display position of the *CustomFieldValue*
        value (Union[Unset, str]): The value of the *CustomFieldValue*
        soft_deleted (Union[Unset, bool]): Whether the value is associated with a deleted custom field
    """

    id: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    field_type: Union[Unset, CustomFieldValueBaseFieldType] = UNSET
    field_required: Union[Unset, bool] = UNSET
    field_displayed: Union[Unset, bool] = UNSET
    field_display_order: Union[Unset, int] = UNSET
    value: Union[Unset, str] = UNSET
    soft_deleted: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        field_name = self.field_name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_type: Union[Unset, str] = UNSET
        if not isinstance(self.field_type, Unset):
            field_type = self.field_type.value

        field_required = self.field_required

        field_displayed = self.field_displayed

        field_display_order = self.field_display_order

        value = self.value

        soft_deleted = self.soft_deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if field_name is not UNSET:
            field_dict["field_name"] = field_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if field_required is not UNSET:
            field_dict["field_required"] = field_required
        if field_displayed is not UNSET:
            field_dict["field_displayed"] = field_displayed
        if field_display_order is not UNSET:
            field_dict["field_display_order"] = field_display_order
        if value is not UNSET:
            field_dict["value"] = value
        if soft_deleted is not UNSET:
            field_dict["soft_deleted"] = soft_deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        field_name = d.pop("field_name", UNSET)

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

        _field_type = d.pop("field_type", UNSET)
        field_type: Union[Unset, CustomFieldValueBaseFieldType]
        if isinstance(_field_type, Unset):
            field_type = UNSET
        else:
            field_type = CustomFieldValueBaseFieldType(_field_type)

        field_required = d.pop("field_required", UNSET)

        field_displayed = d.pop("field_displayed", UNSET)

        field_display_order = d.pop("field_display_order", UNSET)

        value = d.pop("value", UNSET)

        soft_deleted = d.pop("soft_deleted", UNSET)

        custom_field_value_base = cls(
            id=id,
            etag=etag,
            field_name=field_name,
            created_at=created_at,
            updated_at=updated_at,
            field_type=field_type,
            field_required=field_required,
            field_displayed=field_displayed,
            field_display_order=field_display_order,
            value=value,
            soft_deleted=soft_deleted,
        )

        custom_field_value_base.additional_properties = d
        return custom_field_value_base

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
