from enum import Enum


class TaskTemplatecreateDataBodyDataDescriptionTextType(str, Enum):
    PLAIN_TEXT = "plain_text"
    RICH_TEXT = "rich_text"

    def __str__(self) -> str:
        return str(self.value)
