from enum import Enum


class GroupBaseType(str, Enum):
    ACCOUNTGROUP = "AccountGroup"
    ADHOCGROUP = "AdhocGroup"
    TEAMGROUP = "TeamGroup"
    USERGROUP = "UserGroup"

    def __str__(self) -> str:
        return str(self.value)
