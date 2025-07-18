# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.secondarytaxrule.secondarytaxrule import SecondaryTaxRule


class BillingSettingBase(BaseModel):
    apply_tax_by_default: Optional[bool] = Field(
        None,
        description="Used to determine if primary tax should be applied to invoices by default",
    )
    created_at: Optional[str] = Field(
        None,
        description="The time the *BillingSetting* was created (as a ISO-8601 timestamp)",
    )
    currency: Optional[str] = Field(
        None, description="Current user setting of currency"
    )
    currency_sign: Optional[str] = Field(
        None, description="The sign of the current currency"
    )
    etag: Optional[str] = Field(None, description="ETag for the *BillingSetting*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *BillingSetting*"
    )
    notify_after_bill_created: Optional[bool] = Field(
        None,
        description="Flag to indicate if users should have the option to notify other users when generating a bill",
    )
    rounded_duration: Optional[float] = Field(
        None, description="Rounded equivalent of duration submitted"
    )
    rounding: Optional[int] = Field(
        None, description="Minute increment for time rounding"
    )
    secondary_tax_name: Optional[str] = Field(
        None,
        description="Name shown for secondary tax on invoices using this BillingSetting",
    )
    secondary_tax_rate: Optional[float] = Field(
        None,
        description="Rate applied for secondary tax on invoices using this BillingSetting",
    )
    secondary_tax_rule: Optional[SecondaryTaxRule] = Field(
        None,
        description="Used to determine if secondary tax should be applied separately or additionally to primary tax",
    )
    tax_name: Optional[str] = Field(
        None,
        description="Name shown for primary tax on invoices using this BillingSetting",
    )
    tax_rate: Optional[float] = Field(
        None,
        description="Rate applied for primary tax on invoices using this BillingSetting",
    )
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = Field(
        None,
        description="Used to determine if hourly time entries on flat rate or contingency fee matters should be non-billable by default",
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *BillingSetting* was last updated (as a ISO-8601 timestamp)",
    )
    use_decimal_rounding: Optional[bool] = Field(
        None, description="Round time to two decimal places"
    )
    use_secondary_tax: Optional[bool] = Field(
        None,
        description="Used to determine if secondary tax applies to invoices using this BillingSetting",
    )
    use_utbms_codes: Optional[bool] = Field(
        None,
        description="Controls usage of UTBMS codes, allowing creation of coded time entries and expenses",
    )
