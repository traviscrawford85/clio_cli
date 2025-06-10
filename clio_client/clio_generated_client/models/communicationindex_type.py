from enum import Enum


class CommunicationindexType(str, Enum):
    EMAILCOMMUNICATION = "EmailCommunication"
    PHONECOMMUNICATION = "PhoneCommunication"

    def __str__(self) -> str:
        return str(self.value)
