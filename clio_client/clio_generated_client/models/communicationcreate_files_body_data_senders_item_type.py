from enum import Enum


class CommunicationcreateFilesBodyDataSendersItemType(str, Enum):
    CONTACT = "Contact"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
