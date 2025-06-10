from enum import Enum


class BillBaseKind(str, Enum):
    AGGREGATE_ALL = "aggregate_all"
    AGGREGATE_EXPENSES = "aggregate_expenses"
    AGGREGATE_SERVICES = "aggregate_services"
    AGGREGATE_SPLIT = "aggregate_split"
    REVENUE_KIND = "revenue_kind"
    SUMMARY_KIND = "summary_kind"
    TRUST_KIND = "trust_kind"

    def __str__(self) -> str:
        return str(self.value)
