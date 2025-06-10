from enum import Enum


class BillingSettingBaseSecondaryTaxRule(str, Enum):
    POST = "Post"
    PRE = "Pre"

    def __str__(self) -> str:
        return str(self.value)
