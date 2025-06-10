from enum import Enum


class LineItemBaseType(str, Enum):
    ACTIVITYLINEITEM = "ActivityLineItem"
    LINEITEM = "LineItem"
    NOCHARGELINEITEM = "NoChargeLineItem"
    SUMMARYLINEITEM = "SummaryLineItem"

    def __str__(self) -> str:
        return str(self.value)
