from enum import Enum


class TaskTemplatecreateFilesBodyDataReminderTemplatesItemNotificationType(str, Enum):
    EMAIL = "Email"
    POPUP = "Popup"

    def __str__(self) -> str:
        return str(self.value)
