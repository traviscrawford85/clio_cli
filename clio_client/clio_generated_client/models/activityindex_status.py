from enum import Enum


class ActivityindexStatus(str, Enum):
    BILLABLE = "billable"
    BILLED = "billed"
    DRAFT = "draft"
    NON_BILLABLE = "non_billable"
    UNBILLED = "unbilled"
    WRITTEN_OFF = "written_off"

    def __str__(self) -> str:
        return str(self.value)
