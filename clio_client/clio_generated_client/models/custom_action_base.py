import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.custom_action_base_ui_reference import CustomActionBaseUiReference
from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomActionBase")


@_attrs_define
class CustomActionBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *CustomAction*
        etag (Union[Unset, str]): ETag for the *CustomAction*
        created_at (Union[Unset, datetime.datetime]): The time the *CustomAction* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *CustomAction* was last updated (as a ISO-8601
            timestamp)
        label (Union[Unset, str]): Text label to be displayed on the custom link.
        target_url (Union[Unset, str]): Target URL which will be opened in a new tab when the user clicks the custom
            link.
        ui_reference (Union[Unset, CustomActionBaseUiReference]): UI reference location within Clio where the link will
            be displayed.
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    label: Union[Unset, str] = UNSET
    target_url: Union[Unset, str] = UNSET
    ui_reference: Union[Unset, CustomActionBaseUiReference] = UNSET
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

        label = self.label

        target_url = self.target_url

        ui_reference: Union[Unset, str] = UNSET
        if not isinstance(self.ui_reference, Unset):
            ui_reference = self.ui_reference.value

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
        if label is not UNSET:
            field_dict["label"] = label
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if ui_reference is not UNSET:
            field_dict["ui_reference"] = ui_reference

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

        label = d.pop("label", UNSET)

        target_url = d.pop("target_url", UNSET)

        _ui_reference = d.pop("ui_reference", UNSET)
        ui_reference: Union[Unset, CustomActionBaseUiReference]
        if isinstance(_ui_reference, Unset):
            ui_reference = UNSET
        else:
            ui_reference = CustomActionBaseUiReference(_ui_reference)

        custom_action_base = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            label=label,
            target_url=target_url,
            ui_reference=ui_reference,
        )

        custom_action_base.additional_properties = d
        return custom_action_base

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
