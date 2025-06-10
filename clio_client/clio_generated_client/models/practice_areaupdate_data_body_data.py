from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.practice_areaupdate_data_body_data_category import PracticeAreaupdateDataBodyDataCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="PracticeAreaupdateDataBodyData")


@_attrs_define
class PracticeAreaupdateDataBodyData:
    """
    Attributes:
        category (Union[Unset, PracticeAreaupdateDataBodyDataCategory]): The practice area category associated with the
            *PracticeArea*. The friendly display values corresponding to the enum strings:
            * Administrative
            * Admiralty / Maritime
            * Anti-Trust / Competition
            * Appellate
            * Banking / Finance
            * Bankruptcy
            * Business Formation / Compliance
            * Civil Litigation
            * Civil Rights / Constitutional
            * Collections & Debt
            * Commercial / Sale of Goods
            * Commercial Litigation
            * Construction
            * Consumer Protection
            * Contracts
            * Corporate Litigation
            * Criminal
            * Disability / Social Security
            * Education
            * Elder
            * Employment / Labor
            * Energy / Environmental
            * Ethics
            * Family
            * Food / Drug
            * General Practice
            * Government
            * Healthcare
            * Immigration
            * In-House Counsel
            * Insurance
            * Intellectual Property
            * International
            * Juvenile
            * Legal Aid
            * Mediation / Arbitration
            * Medical Malpractice
            * Military
            * Multi-Practice
            * Non-Profit / Pro Bono
            * Other
            * Personal Injury
            * Privacy / Information Security
            * Private Client
            * Product Liability
            * Real Estate
            * Science / Technology
            * Securities / Mergers & Acquisitions
            * Small Claims
            * Sports / Entertainment / Gaming
            * Tax
            * Telecommunications
            * Traffic Offenses
            * Transportation
            * Tribal
            * Trusts
            * Wills & Estates
            * Worker's Compensation
        code (Union[Unset, str]): The code attached to the PracticeArea.
        name (Union[Unset, str]): Name of the PracticeArea.
    """

    category: Union[Unset, PracticeAreaupdateDataBodyDataCategory] = UNSET
    code: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        code = self.code

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if code is not UNSET:
            field_dict["code"] = code
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _category = d.pop("category", UNSET)
        category: Union[Unset, PracticeAreaupdateDataBodyDataCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = PracticeAreaupdateDataBodyDataCategory(_category)

        code = d.pop("code", UNSET)

        name = d.pop("name", UNSET)

        practice_areaupdate_data_body_data = cls(
            category=category,
            code=code,
            name=name,
        )

        practice_areaupdate_data_body_data.additional_properties = d
        return practice_areaupdate_data_body_data

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
