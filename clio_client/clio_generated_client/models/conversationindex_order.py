from enum import Enum


class ConversationindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    LAST_MESSAGE_IDASC = "last_message_id(asc)"
    LAST_MESSAGE_IDDESC = "last_message_id(desc)"
    MATTER_IDASC = "matter_id(asc)"
    MATTER_IDDESC = "matter_id(desc)"

    def __str__(self) -> str:
        return str(self.value)
