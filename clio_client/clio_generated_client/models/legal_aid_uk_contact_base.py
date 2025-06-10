from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalAidUkContactBase")


@_attrs_define
class LegalAidUkContactBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *LegalAidUkContact*
        disability (Union[Unset, int]): The disability of the LegalAidUkContact
        disability_code (Union[Unset, str]): The disability code of the LegalAidUkContact
        ethnicity (Union[Unset, int]): The ethnicity of the LegalAidUkContact
        ethnicity_title (Union[Unset, str]): The ethnicity title of the LegalAidUkContact
        financially_eligible (Union[Unset, bool]): The financial eligibility of the LegalAidUkContact
        gender (Union[Unset, int]): The gender of the LegalAidUkContact
        gender_title (Union[Unset, str]): The gender title of the LegalAidUkContact
        national_insurance_number (Union[Unset, str]): National Insurance Number
    """

    id: Union[Unset, int] = UNSET
    disability: Union[Unset, int] = UNSET
    disability_code: Union[Unset, str] = UNSET
    ethnicity: Union[Unset, int] = UNSET
    ethnicity_title: Union[Unset, str] = UNSET
    financially_eligible: Union[Unset, bool] = UNSET
    gender: Union[Unset, int] = UNSET
    gender_title: Union[Unset, str] = UNSET
    national_insurance_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        disability = self.disability

        disability_code = self.disability_code

        ethnicity = self.ethnicity

        ethnicity_title = self.ethnicity_title

        financially_eligible = self.financially_eligible

        gender = self.gender

        gender_title = self.gender_title

        national_insurance_number = self.national_insurance_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if disability is not UNSET:
            field_dict["disability"] = disability
        if disability_code is not UNSET:
            field_dict["disability_code"] = disability_code
        if ethnicity is not UNSET:
            field_dict["ethnicity"] = ethnicity
        if ethnicity_title is not UNSET:
            field_dict["ethnicity_title"] = ethnicity_title
        if financially_eligible is not UNSET:
            field_dict["financially_eligible"] = financially_eligible
        if gender is not UNSET:
            field_dict["gender"] = gender
        if gender_title is not UNSET:
            field_dict["gender_title"] = gender_title
        if national_insurance_number is not UNSET:
            field_dict["national_insurance_number"] = national_insurance_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        disability = d.pop("disability", UNSET)

        disability_code = d.pop("disability_code", UNSET)

        ethnicity = d.pop("ethnicity", UNSET)

        ethnicity_title = d.pop("ethnicity_title", UNSET)

        financially_eligible = d.pop("financially_eligible", UNSET)

        gender = d.pop("gender", UNSET)

        gender_title = d.pop("gender_title", UNSET)

        national_insurance_number = d.pop("national_insurance_number", UNSET)

        legal_aid_uk_contact_base = cls(
            id=id,
            disability=disability,
            disability_code=disability_code,
            ethnicity=ethnicity,
            ethnicity_title=ethnicity_title,
            financially_eligible=financially_eligible,
            gender=gender,
            gender_title=gender_title,
            national_insurance_number=national_insurance_number,
        )

        legal_aid_uk_contact_base.additional_properties = d
        return legal_aid_uk_contact_base

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
