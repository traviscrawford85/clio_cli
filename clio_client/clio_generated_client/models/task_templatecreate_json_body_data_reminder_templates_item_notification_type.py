from enum import Enum


class TaskTemplatecreateJsonBodyDataReminderTemplatesItemNotificationType(str, Enum):
    EMAIL = "Email"
    POPUP = "Popup"

    def __str__(self) -> str:
        return str(self.value)
