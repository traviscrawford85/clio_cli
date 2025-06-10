import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.billing_setting_base_secondary_tax_rule import BillingSettingBaseSecondaryTaxRule
from ..types import UNSET, Unset

T = TypeVar("T", bound="BillingSettingBase")


@_attrs_define
class BillingSettingBase:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *BillingSetting*
        etag (Union[Unset, str]): ETag for the *BillingSetting*
        rounded_duration (Union[Unset, float]): Rounded equivalent of duration submitted
        rounding (Union[Unset, int]): Minute increment for time rounding
        use_decimal_rounding (Union[Unset, bool]): Round time to two decimal places
        currency (Union[Unset, str]): Current user setting of currency
        currency_sign (Union[Unset, str]): The sign of the current currency
        tax_rate (Union[Unset, float]): Rate applied for primary tax on invoices using this BillingSetting
        tax_name (Union[Unset, str]): Name shown for primary tax on invoices using this BillingSetting
        apply_tax_by_default (Union[Unset, bool]): Used to determine if primary tax should be applied to invoices by
            default
        time_on_flat_rate_contingency_matters_is_non_billable (Union[Unset, bool]): Used to determine if hourly time
            entries on flat rate or contingency fee matters should be non-billable by default
        use_secondary_tax (Union[Unset, bool]): Used to determine if secondary tax applies to invoices using this
            BillingSetting
        secondary_tax_rate (Union[Unset, float]): Rate applied for secondary tax on invoices using this BillingSetting
        secondary_tax_rule (Union[Unset, BillingSettingBaseSecondaryTaxRule]): Used to determine if secondary tax should
            be applied separately or additionally to primary tax
        secondary_tax_name (Union[Unset, str]): Name shown for secondary tax on invoices using this BillingSetting
        notify_after_bill_created (Union[Unset, bool]): Flag to indicate if users should have the option to notify other
            users when generating a bill
        use_utbms_codes (Union[Unset, bool]): Controls usage of UTBMS codes, allowing creation of coded time entries and
            expenses
        created_at (Union[Unset, datetime.datetime]): The time the *BillingSetting* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *BillingSetting* was last updated (as a ISO-8601
            timestamp)
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    rounded_duration: Union[Unset, float] = UNSET
    rounding: Union[Unset, int] = UNSET
    use_decimal_rounding: Union[Unset, bool] = UNSET
    currency: Union[Unset, str] = UNSET
    currency_sign: Union[Unset, str] = UNSET
    tax_rate: Union[Unset, float] = UNSET
    tax_name: Union[Unset, str] = UNSET
    apply_tax_by_default: Union[Unset, bool] = UNSET
    time_on_flat_rate_contingency_matters_is_non_billable: Union[Unset, bool] = UNSET
    use_secondary_tax: Union[Unset, bool] = UNSET
    secondary_tax_rate: Union[Unset, float] = UNSET
    secondary_tax_rule: Union[Unset, BillingSettingBaseSecondaryTaxRule] = UNSET
    secondary_tax_name: Union[Unset, str] = UNSET
    notify_after_bill_created: Union[Unset, bool] = UNSET
    use_utbms_codes: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        rounded_duration = self.rounded_duration

        rounding = self.rounding

        use_decimal_rounding = self.use_decimal_rounding

        currency = self.currency

        currency_sign = self.currency_sign

        tax_rate = self.tax_rate

        tax_name = self.tax_name

        apply_tax_by_default = self.apply_tax_by_default

        time_on_flat_rate_contingency_matters_is_non_billable = (
            self.time_on_flat_rate_contingency_matters_is_non_billable
        )

        use_secondary_tax = self.use_secondary_tax

        secondary_tax_rate = self.secondary_tax_rate

        secondary_tax_rule: Union[Unset, str] = UNSET
        if not isinstance(self.secondary_tax_rule, Unset):
            secondary_tax_rule = self.secondary_tax_rule.value

        secondary_tax_name = self.secondary_tax_name

        notify_after_bill_created = self.notify_after_bill_created

        use_utbms_codes = self.use_utbms_codes

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
        if rounded_duration is not UNSET:
            field_dict["rounded_duration"] = rounded_duration
        if rounding is not UNSET:
            field_dict["rounding"] = rounding
        if use_decimal_rounding is not UNSET:
            field_dict["use_decimal_rounding"] = use_decimal_rounding
        if currency is not UNSET:
            field_dict["currency"] = currency
        if currency_sign is not UNSET:
            field_dict["currency_sign"] = currency_sign
        if tax_rate is not UNSET:
            field_dict["tax_rate"] = tax_rate
        if tax_name is not UNSET:
            field_dict["tax_name"] = tax_name
        if apply_tax_by_default is not UNSET:
            field_dict["apply_tax_by_default"] = apply_tax_by_default
        if time_on_flat_rate_contingency_matters_is_non_billable is not UNSET:
            field_dict["time_on_flat_rate_contingency_matters_is_non_billable"] = (
                time_on_flat_rate_contingency_matters_is_non_billable
            )
        if use_secondary_tax is not UNSET:
            field_dict["use_secondary_tax"] = use_secondary_tax
        if secondary_tax_rate is not UNSET:
            field_dict["secondary_tax_rate"] = secondary_tax_rate
        if secondary_tax_rule is not UNSET:
            field_dict["secondary_tax_rule"] = secondary_tax_rule
        if secondary_tax_name is not UNSET:
            field_dict["secondary_tax_name"] = secondary_tax_name
        if notify_after_bill_created is not UNSET:
            field_dict["notify_after_bill_created"] = notify_after_bill_created
        if use_utbms_codes is not UNSET:
            field_dict["use_utbms_codes"] = use_utbms_codes
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

        rounded_duration = d.pop("rounded_duration", UNSET)

        rounding = d.pop("rounding", UNSET)

        use_decimal_rounding = d.pop("use_decimal_rounding", UNSET)

        currency = d.pop("currency", UNSET)

        currency_sign = d.pop("currency_sign", UNSET)

        tax_rate = d.pop("tax_rate", UNSET)

        tax_name = d.pop("tax_name", UNSET)

        apply_tax_by_default = d.pop("apply_tax_by_default", UNSET)

        time_on_flat_rate_contingency_matters_is_non_billable = d.pop(
            "time_on_flat_rate_contingency_matters_is_non_billable", UNSET
        )

        use_secondary_tax = d.pop("use_secondary_tax", UNSET)

        secondary_tax_rate = d.pop("secondary_tax_rate", UNSET)

        _secondary_tax_rule = d.pop("secondary_tax_rule", UNSET)
        secondary_tax_rule: Union[Unset, BillingSettingBaseSecondaryTaxRule]
        if isinstance(_secondary_tax_rule, Unset):
            secondary_tax_rule = UNSET
        else:
            secondary_tax_rule = BillingSettingBaseSecondaryTaxRule(_secondary_tax_rule)

        secondary_tax_name = d.pop("secondary_tax_name", UNSET)

        notify_after_bill_created = d.pop("notify_after_bill_created", UNSET)

        use_utbms_codes = d.pop("use_utbms_codes", UNSET)

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

        billing_setting_base = cls(
            id=id,
            etag=etag,
            rounded_duration=rounded_duration,
            rounding=rounding,
            use_decimal_rounding=use_decimal_rounding,
            currency=currency,
            currency_sign=currency_sign,
            tax_rate=tax_rate,
            tax_name=tax_name,
            apply_tax_by_default=apply_tax_by_default,
            time_on_flat_rate_contingency_matters_is_non_billable=time_on_flat_rate_contingency_matters_is_non_billable,
            use_secondary_tax=use_secondary_tax,
            secondary_tax_rate=secondary_tax_rate,
            secondary_tax_rule=secondary_tax_rule,
            secondary_tax_name=secondary_tax_name,
            notify_after_bill_created=notify_after_bill_created,
            use_utbms_codes=use_utbms_codes,
            created_at=created_at,
            updated_at=updated_at,
        )

        billing_setting_base.additional_properties = d
        return billing_setting_base

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
