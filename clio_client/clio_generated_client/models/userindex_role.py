from enum import Enum


class UserindexRole(str, Enum):
    ACCOUNTS = "accounts"
    ADMIN = "admin"
    BILLING = "billing"
    REPORTS = "reports"

    def __str__(self) -> str:
        return str(self.value)
