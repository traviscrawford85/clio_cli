from enum import Enum


class ReportBaseCategory(str, Enum):
    BILLING = "billing"
    CLIENT = "client"
    COMPLIANCE = "compliance"
    FINANCIAL = "financial"
    MATTER = "matter"
    ONLINE_PAYMENTS = "online_payments"
    PRODUCTIVITY = "productivity"
    REVENUE = "revenue"
    TASK = "task"

    def __str__(self) -> str:
        return str(self.value)
