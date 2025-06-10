import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LaukCivilCertificatedRateBase")


@_attrs_define
class LaukCivilCertificatedRateBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *LaukCivilCertificatedRate*
        activity (Union[Unset, str]): Activity of the *LaukCivilCertificatedRate*
        activity_sub_category (Union[Unset, str]): Activity sub-category
        activity_type (Union[Unset, str]): Activity type
        attended_several_hearings_for_multiple_clients (Union[Unset, bool]): Multiple hearings for multiple clients
            indicator
        category_of_law (Union[Unset, str]): Category of law
        created_at (Union[Unset, datetime.datetime]): The time the *LaukCivilCertificatedRate* was created (as a
            ISO-8601 timestamp)
        change_of_solicitor (Union[Unset, bool]): Change of solicitor indicator
        court (Union[Unset, str]): Court associated
        eligible_for_sqm (Union[Unset, bool]): SQM eligibility (Legal Aid England and Wales)
        exceptional (Union[Unset, float]): Fee applied for high activity count
        exceptional_warning (Union[Unset, str]): Warning for exceptional status
        etag (Union[Unset, str]): ETag for the *LaukCivilCertificatedRate*
        fee (Union[Unset, float]): Fee amount
        fee_scheme (Union[Unset, str]): Fee scheme
        first_conducting_solicitor (Union[Unset, bool]): First conducting solicitor indicator
        key (Union[Unset, str]): Unique key
        number_of_clients (Union[Unset, str]): Number of clients
        party (Union[Unset, str]): Associated party
        post_transfer_clients_represented (Union[Unset, str]): Post-transfer clients represented
        rate_type (Union[Unset, str]): Rate type
        region (Union[Unset, str]): Region
        session_type (Union[Unset, str]): Session type
        user_type (Union[Unset, str]): User type
        updated_at (Union[Unset, datetime.datetime]): The time the *LaukCivilCertificatedRate* was last updated (as a
            ISO-8601 timestamp)
    """

    id: Union[Unset, int] = UNSET
    activity: Union[Unset, str] = UNSET
    activity_sub_category: Union[Unset, str] = UNSET
    activity_type: Union[Unset, str] = UNSET
    attended_several_hearings_for_multiple_clients: Union[Unset, bool] = UNSET
    category_of_law: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    change_of_solicitor: Union[Unset, bool] = UNSET
    court: Union[Unset, str] = UNSET
    eligible_for_sqm: Union[Unset, bool] = UNSET
    exceptional: Union[Unset, float] = UNSET
    exceptional_warning: Union[Unset, str] = UNSET
    etag: Union[Unset, str] = UNSET
    fee: Union[Unset, float] = UNSET
    fee_scheme: Union[Unset, str] = UNSET
    first_conducting_solicitor: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    number_of_clients: Union[Unset, str] = UNSET
    party: Union[Unset, str] = UNSET
    post_transfer_clients_represented: Union[Unset, str] = UNSET
    rate_type: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    session_type: Union[Unset, str] = UNSET
    user_type: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity = self.activity

        activity_sub_category = self.activity_sub_category

        activity_type = self.activity_type

        attended_several_hearings_for_multiple_clients = self.attended_several_hearings_for_multiple_clients

        category_of_law = self.category_of_law

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        change_of_solicitor = self.change_of_solicitor

        court = self.court

        eligible_for_sqm = self.eligible_for_sqm

        exceptional = self.exceptional

        exceptional_warning = self.exceptional_warning

        etag = self.etag

        fee = self.fee

        fee_scheme = self.fee_scheme

        first_conducting_solicitor = self.first_conducting_solicitor

        key = self.key

        number_of_clients = self.number_of_clients

        party = self.party

        post_transfer_clients_represented = self.post_transfer_clients_represented

        rate_type = self.rate_type

        region = self.region

        session_type = self.session_type

        user_type = self.user_type

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if activity is not UNSET:
            field_dict["activity"] = activity
        if activity_sub_category is not UNSET:
            field_dict["activity_sub_category"] = activity_sub_category
        if activity_type is not UNSET:
            field_dict["activity_type"] = activity_type
        if attended_several_hearings_for_multiple_clients is not UNSET:
            field_dict["attended_several_hearings_for_multiple_clients"] = (
                attended_several_hearings_for_multiple_clients
            )
        if category_of_law is not UNSET:
            field_dict["category_of_law"] = category_of_law
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if change_of_solicitor is not UNSET:
            field_dict["change_of_solicitor"] = change_of_solicitor
        if court is not UNSET:
            field_dict["court"] = court
        if eligible_for_sqm is not UNSET:
            field_dict["eligible_for_sqm"] = eligible_for_sqm
        if exceptional is not UNSET:
            field_dict["exceptional"] = exceptional
        if exceptional_warning is not UNSET:
            field_dict["exceptional_warning"] = exceptional_warning
        if etag is not UNSET:
            field_dict["etag"] = etag
        if fee is not UNSET:
            field_dict["fee"] = fee
        if fee_scheme is not UNSET:
            field_dict["fee_scheme"] = fee_scheme
        if first_conducting_solicitor is not UNSET:
            field_dict["first_conducting_solicitor"] = first_conducting_solicitor
        if key is not UNSET:
            field_dict["key"] = key
        if number_of_clients is not UNSET:
            field_dict["number_of_clients"] = number_of_clients
        if party is not UNSET:
            field_dict["party"] = party
        if post_transfer_clients_represented is not UNSET:
            field_dict["post_transfer_clients_represented"] = post_transfer_clients_represented
        if rate_type is not UNSET:
            field_dict["rate_type"] = rate_type
        if region is not UNSET:
            field_dict["region"] = region
        if session_type is not UNSET:
            field_dict["session_type"] = session_type
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        activity = d.pop("activity", UNSET)

        activity_sub_category = d.pop("activity_sub_category", UNSET)

        activity_type = d.pop("activity_type", UNSET)

        attended_several_hearings_for_multiple_clients = d.pop("attended_several_hearings_for_multiple_clients", UNSET)

        category_of_law = d.pop("category_of_law", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        change_of_solicitor = d.pop("change_of_solicitor", UNSET)

        court = d.pop("court", UNSET)

        eligible_for_sqm = d.pop("eligible_for_sqm", UNSET)

        exceptional = d.pop("exceptional", UNSET)

        exceptional_warning = d.pop("exceptional_warning", UNSET)

        etag = d.pop("etag", UNSET)

        fee = d.pop("fee", UNSET)

        fee_scheme = d.pop("fee_scheme", UNSET)

        first_conducting_solicitor = d.pop("first_conducting_solicitor", UNSET)

        key = d.pop("key", UNSET)

        number_of_clients = d.pop("number_of_clients", UNSET)

        party = d.pop("party", UNSET)

        post_transfer_clients_represented = d.pop("post_transfer_clients_represented", UNSET)

        rate_type = d.pop("rate_type", UNSET)

        region = d.pop("region", UNSET)

        session_type = d.pop("session_type", UNSET)

        user_type = d.pop("user_type", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        lauk_civil_certificated_rate_base = cls(
            id=id,
            activity=activity,
            activity_sub_category=activity_sub_category,
            activity_type=activity_type,
            attended_several_hearings_for_multiple_clients=attended_several_hearings_for_multiple_clients,
            category_of_law=category_of_law,
            created_at=created_at,
            change_of_solicitor=change_of_solicitor,
            court=court,
            eligible_for_sqm=eligible_for_sqm,
            exceptional=exceptional,
            exceptional_warning=exceptional_warning,
            etag=etag,
            fee=fee,
            fee_scheme=fee_scheme,
            first_conducting_solicitor=first_conducting_solicitor,
            key=key,
            number_of_clients=number_of_clients,
            party=party,
            post_transfer_clients_represented=post_transfer_clients_represented,
            rate_type=rate_type,
            region=region,
            session_type=session_type,
            user_type=user_type,
            updated_at=updated_at,
        )

        lauk_civil_certificated_rate_base.additional_properties = d
        return lauk_civil_certificated_rate_base

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
