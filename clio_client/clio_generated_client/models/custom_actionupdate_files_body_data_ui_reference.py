from enum import Enum


class CustomActionupdateFilesBodyDataUiReference(str, Enum):
    ACTIVITIESSHOW = "activities/show"
    CONTACTSSHOW = "contacts/show"
    DOCUMENTSSHOW = "documents/show"
    FOLDERSSHOW = "folders/show"
    MATTERSSHOW = "matters/show"

    def __str__(self) -> str:
        return str(self.value)
