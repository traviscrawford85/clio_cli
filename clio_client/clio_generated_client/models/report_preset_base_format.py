from enum import Enum


class ReportPresetBaseFormat(str, Enum):
    CSV = "csv"
    HTML = "html"
    JSON = "json"
    PDF = "pdf"
    XLSX = "xlsx"
    ZIP = "zip"

    def __str__(self) -> str:
        return str(self.value)
