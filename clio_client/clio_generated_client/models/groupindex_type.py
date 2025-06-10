from enum import Enum


class GroupindexType(str, Enum):
    ACCOUNTGROUP = "AccountGroup"
    ADHOCGROUP = "AdhocGroup"
    USERGROUP = "UserGroup"

    def __str__(self) -> str:
        return str(self.value)
