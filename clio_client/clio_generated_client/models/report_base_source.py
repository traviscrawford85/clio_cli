from enum import Enum


class ReportBaseSource(str, Enum):
    PRESETS = "presets"
    REPORTS = "reports"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
