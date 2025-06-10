from enum import Enum


class ActivitycreateDataBodyDataTaxSetting(str, Enum):
    NO_TAX = "no_tax"
    TAX_1_AND_TAX_2 = "tax_1_and_tax_2"
    TAX_1_ONLY = "tax_1_only"
    TAX_2_ONLY = "tax_2_only"

    def __str__(self) -> str:
        return str(self.value)
