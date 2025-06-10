from enum import Enum


class CommunicationBaseType(str, Enum):
    EMAILCOMMUNICATION = "EmailCommunication"
    PHONECOMMUNICATION = "PhoneCommunication"

    def __str__(self) -> str:
        return str(self.value)
