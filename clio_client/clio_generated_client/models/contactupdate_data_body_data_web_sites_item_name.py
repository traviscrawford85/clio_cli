from enum import Enum


class ContactupdateDataBodyDataWebSitesItemName(str, Enum):
    FACEBOOK = "Facebook"
    INSTANT_MESSENGER = "Instant Messenger"
    LINKEDIN = "LinkedIn"
    OTHER = "Other"
    PERSONAL = "Personal"
    TWITTER = "Twitter"
    WORK = "Work"

    def __str__(self) -> str:
        return str(self.value)
