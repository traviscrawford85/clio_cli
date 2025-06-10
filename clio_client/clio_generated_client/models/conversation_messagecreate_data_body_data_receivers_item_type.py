from enum import Enum


class ConversationMessagecreateDataBodyDataReceiversItemType(str, Enum):
    CONTACT = "Contact"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
