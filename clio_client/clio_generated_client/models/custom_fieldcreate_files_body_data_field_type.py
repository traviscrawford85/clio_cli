from enum import Enum


class CustomFieldcreateFilesBodyDataFieldType(str, Enum):
    CHECKBOX = "checkbox"
    CONTACT = "contact"
    CURRENCY = "currency"
    DATE = "date"
    EMAIL = "email"
    MATTER = "matter"
    NUMERIC = "numeric"
    PICKLIST = "picklist"
    TEXT_AREA = "text_area"
    TEXT_LINE = "text_line"
    TIME = "time"
    URL = "url"

    def __str__(self) -> str:
        return str(self.value)
