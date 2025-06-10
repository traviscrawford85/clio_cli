import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grant_funding_source_base import GrantFundingSourceBase


T = TypeVar("T", bound="Grant")


@_attrs_define
class Grant:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Grant*
        etag (Union[Unset, str]): ETag for the *Grant*
        name (Union[Unset, str]): The name of the *Grant*
        funding_code (Union[Unset, str]): Funding code of the grant
        funding_code_and_name (Union[Unset, str]): Funding code and name of the grant
        funding_source_name (Union[Unset, str]): Name of the funding source of the grant
        created_at (Union[Unset, datetime.datetime]): The time the *Grant* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Grant* was last updated (as a ISO-8601 timestamp)
        balance (Union[Unset, str]): Balance of the grant
        start_date (Union[Unset, datetime.date]): Start date of the grant
        end_date (Union[Unset, datetime.date]): End date of the grant
        grant_funding_source (Union[Unset, GrantFundingSourceBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    funding_code: Union[Unset, str] = UNSET
    funding_code_and_name: Union[Unset, str] = UNSET
    funding_source_name: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    balance: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[Unset, datetime.date] = UNSET
    grant_funding_source: Union[Unset, "GrantFundingSourceBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        funding_code = self.funding_code

        funding_code_and_name = self.funding_code_and_name

        funding_source_name = self.funding_source_name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        balance = self.balance

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        grant_funding_source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grant_funding_source, Unset):
            grant_funding_source = self.grant_funding_source.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if funding_code is not UNSET:
            field_dict["funding_code"] = funding_code
        if funding_code_and_name is not UNSET:
            field_dict["funding_code_and_name"] = funding_code_and_name
        if funding_source_name is not UNSET:
            field_dict["funding_source_name"] = funding_source_name
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if balance is not UNSET:
            field_dict["balance"] = balance
        if start_date is not UNSET:
            field_dict["start_date"] = start_date
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if grant_funding_source is not UNSET:
            field_dict["grant_funding_source"] = grant_funding_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grant_funding_source_base import GrantFundingSourceBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        funding_code = d.pop("funding_code", UNSET)

        funding_code_and_name = d.pop("funding_code_and_name", UNSET)

        funding_source_name = d.pop("funding_source_name", UNSET)

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

        balance = d.pop("balance", UNSET)

        _start_date = d.pop("start_date", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        _end_date = d.pop("end_date", UNSET)
        end_date: Union[Unset, datetime.date]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date).date()

        _grant_funding_source = d.pop("grant_funding_source", UNSET)
        grant_funding_source: Union[Unset, GrantFundingSourceBase]
        if isinstance(_grant_funding_source, Unset):
            grant_funding_source = UNSET
        else:
            grant_funding_source = GrantFundingSourceBase.from_dict(_grant_funding_source)

        grant = cls(
            id=id,
            etag=etag,
            name=name,
            funding_code=funding_code,
            funding_code_and_name=funding_code_and_name,
            funding_source_name=funding_source_name,
            created_at=created_at,
            updated_at=updated_at,
            balance=balance,
            start_date=start_date,
            end_date=end_date,
            grant_funding_source=grant_funding_source,
        )

        grant.additional_properties = d
        return grant

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
