from enum import Enum


class ReminderTemplateBaseNotificationType(str, Enum):
    EMAIL = "Email"
    POPUP = "Popup"

    def __str__(self) -> str:
        return str(self.value)
