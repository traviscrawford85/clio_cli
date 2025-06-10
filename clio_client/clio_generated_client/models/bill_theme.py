import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BillTheme")


@_attrs_define
class BillTheme:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BillTheme*
        etag (Union[Unset, str]): ETag for the *BillTheme*
        created_at (Union[Unset, datetime.datetime]): The time the *BillTheme* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *BillTheme* was last updated (as a ISO-8601
            timestamp)
        account_id (Union[Unset, int]): The account number the *BillTheme* belongs to
        default (Union[Unset, bool]): Whether the *BillTheme* is the default for its account
        name (Union[Unset, str]): The name of the *BillTheme*
        config (Union[Unset, str]): The configuration of the *BillTheme*
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    account_id: Union[Unset, int] = UNSET
    default: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    config: Union[Unset, str] = UNSET
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

        account_id = self.account_id

        default = self.default

        name = self.name

        config = self.config

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
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if default is not UNSET:
            field_dict["default"] = default
        if name is not UNSET:
            field_dict["name"] = name
        if config is not UNSET:
            field_dict["config"] = config

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

        account_id = d.pop("account_id", UNSET)

        default = d.pop("default", UNSET)

        name = d.pop("name", UNSET)

        config = d.pop("config", UNSET)

        bill_theme = cls(
            id=id,
            etag=etag,
            created_at=created_at,
            updated_at=updated_at,
            account_id=account_id,
            default=default,
            name=name,
            config=config,
        )

        bill_theme.additional_properties = d
        return bill_theme

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
