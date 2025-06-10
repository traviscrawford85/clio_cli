from enum import Enum


class ClioCreatorBaseType(str, Enum):
    CLIENTUSER = "ClientUser"
    MANAGEUSER = "ManageUser"

    def __str__(self) -> str:
        return str(self.value)
