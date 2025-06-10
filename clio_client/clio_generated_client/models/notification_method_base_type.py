from enum import Enum


class NotificationMethodBaseType(str, Enum):
    EMAIL = "Email"
    POPUP = "Popup"
    SMS = "SMS"

    def __str__(self) -> str:
        return str(self.value)
