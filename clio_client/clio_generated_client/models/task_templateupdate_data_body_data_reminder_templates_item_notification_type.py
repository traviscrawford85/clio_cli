from enum import Enum


class TaskTemplateupdateDataBodyDataReminderTemplatesItemNotificationType(str, Enum):
    EMAIL = "Email"
    POPUP = "Popup"

    def __str__(self) -> str:
        return str(self.value)
