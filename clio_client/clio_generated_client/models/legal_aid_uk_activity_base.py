from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalAidUkActivityBase")


@_attrs_define
class LegalAidUkActivityBase:
    """
    Attributes:
        activity_sub_category (Union[Unset, str]): Activity sub-category
        advocacy (Union[Unset, int]): Advocacy
        base_rate (Union[Unset, float]): Base rate
        bolt_ons (Union[Unset, str]): Bolt ons
        bolt_ons_summary (Union[Unset, str]): Bolt ons summary
        court (Union[Unset, int]): Court
        eligible_for_sqm (Union[Unset, bool]): Eligible for SQM
        expert (Union[Unset, int]): Expert
        form_of_civil_legal_service (Union[Unset, int]): Form of civil legal service
        id (Union[Unset, int]): Unique identifier for the *LegalAidUkActivity*
        is_custom_rate (Union[Unset, bool]): Flag to indicate if rate was manually entered by user
        json_key (Union[Unset, str]): Lookup key that references JSON data
        region (Union[Unset, int]): Region
        tax_exclusive (Union[Unset, bool]): Flag to indicate if tax is exclusive
        uplift (Union[Unset, float]): Uplift percentage applied to activity rate
        user_type (Union[Unset, int]): User type
    """

    activity_sub_category: Union[Unset, str] = UNSET
    advocacy: Union[Unset, int] = UNSET
    base_rate: Union[Unset, float] = UNSET
    bolt_ons: Union[Unset, str] = UNSET
    bolt_ons_summary: Union[Unset, str] = UNSET
    court: Union[Unset, int] = UNSET
    eligible_for_sqm: Union[Unset, bool] = UNSET
    expert: Union[Unset, int] = UNSET
    form_of_civil_legal_service: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    is_custom_rate: Union[Unset, bool] = UNSET
    json_key: Union[Unset, str] = UNSET
    region: Union[Unset, int] = UNSET
    tax_exclusive: Union[Unset, bool] = UNSET
    uplift: Union[Unset, float] = UNSET
    user_type: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_sub_category = self.activity_sub_category

        advocacy = self.advocacy

        base_rate = self.base_rate

        bolt_ons = self.bolt_ons

        bolt_ons_summary = self.bolt_ons_summary

        court = self.court

        eligible_for_sqm = self.eligible_for_sqm

        expert = self.expert

        form_of_civil_legal_service = self.form_of_civil_legal_service

        id = self.id

        is_custom_rate = self.is_custom_rate

        json_key = self.json_key

        region = self.region

        tax_exclusive = self.tax_exclusive

        uplift = self.uplift

        user_type = self.user_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activity_sub_category is not UNSET:
            field_dict["activity_sub_category"] = activity_sub_category
        if advocacy is not UNSET:
            field_dict["advocacy"] = advocacy
        if base_rate is not UNSET:
            field_dict["base_rate"] = base_rate
        if bolt_ons is not UNSET:
            field_dict["bolt_ons"] = bolt_ons
        if bolt_ons_summary is not UNSET:
            field_dict["bolt_ons_summary"] = bolt_ons_summary
        if court is not UNSET:
            field_dict["court"] = court
        if eligible_for_sqm is not UNSET:
            field_dict["eligible_for_sqm"] = eligible_for_sqm
        if expert is not UNSET:
            field_dict["expert"] = expert
        if form_of_civil_legal_service is not UNSET:
            field_dict["form_of_civil_legal_service"] = form_of_civil_legal_service
        if id is not UNSET:
            field_dict["id"] = id
        if is_custom_rate is not UNSET:
            field_dict["is_custom_rate"] = is_custom_rate
        if json_key is not UNSET:
            field_dict["json_key"] = json_key
        if region is not UNSET:
            field_dict["region"] = region
        if tax_exclusive is not UNSET:
            field_dict["tax_exclusive"] = tax_exclusive
        if uplift is not UNSET:
            field_dict["uplift"] = uplift
        if user_type is not UNSET:
            field_dict["user_type"] = user_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        activity_sub_category = d.pop("activity_sub_category", UNSET)

        advocacy = d.pop("advocacy", UNSET)

        base_rate = d.pop("base_rate", UNSET)

        bolt_ons = d.pop("bolt_ons", UNSET)

        bolt_ons_summary = d.pop("bolt_ons_summary", UNSET)

        court = d.pop("court", UNSET)

        eligible_for_sqm = d.pop("eligible_for_sqm", UNSET)

        expert = d.pop("expert", UNSET)

        form_of_civil_legal_service = d.pop("form_of_civil_legal_service", UNSET)

        id = d.pop("id", UNSET)

        is_custom_rate = d.pop("is_custom_rate", UNSET)

        json_key = d.pop("json_key", UNSET)

        region = d.pop("region", UNSET)

        tax_exclusive = d.pop("tax_exclusive", UNSET)

        uplift = d.pop("uplift", UNSET)

        user_type = d.pop("user_type", UNSET)

        legal_aid_uk_activity_base = cls(
            activity_sub_category=activity_sub_category,
            advocacy=advocacy,
            base_rate=base_rate,
            bolt_ons=bolt_ons,
            bolt_ons_summary=bolt_ons_summary,
            court=court,
            eligible_for_sqm=eligible_for_sqm,
            expert=expert,
            form_of_civil_legal_service=form_of_civil_legal_service,
            id=id,
            is_custom_rate=is_custom_rate,
            json_key=json_key,
            region=region,
            tax_exclusive=tax_exclusive,
            uplift=uplift,
            user_type=user_type,
        )

        legal_aid_uk_activity_base.additional_properties = d
        return legal_aid_uk_activity_base

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
