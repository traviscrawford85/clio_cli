import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_automation_base_export_formats import DocumentAutomationBaseExportFormats
from ..models.document_automation_base_state import DocumentAutomationBaseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_base import DocumentBase
    from ..models.document_template_base import DocumentTemplateBase
    from ..models.matter_base import MatterBase


T = TypeVar("T", bound="DocumentAutomation")


@_attrs_define
class DocumentAutomation:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *DocumentAutomation*
        etag (Union[Unset, str]): ETag for the *DocumentAutomation*
        state (Union[Unset, DocumentAutomationBaseState]): A text description of what the automation is currently doing
        export_formats (Union[Unset, DocumentAutomationBaseExportFormats]): An array of what formats were requested
        filename (Union[Unset, str]): The name of the file being generated.
        created_at (Union[Unset, datetime.datetime]): The time the *DocumentAutomation* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *DocumentAutomation* was last updated (as a ISO-8601
            timestamp)
        matter (Union[Unset, MatterBase]):
        document_template (Union[Unset, DocumentTemplateBase]):
        documents (Union[Unset, list['DocumentBase']]): Document
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    state: Union[Unset, DocumentAutomationBaseState] = UNSET
    export_formats: Union[Unset, DocumentAutomationBaseExportFormats] = UNSET
    filename: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    matter: Union[Unset, "MatterBase"] = UNSET
    document_template: Union[Unset, "DocumentTemplateBase"] = UNSET
    documents: Union[Unset, list["DocumentBase"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        export_formats: Union[Unset, str] = UNSET
        if not isinstance(self.export_formats, Unset):
            export_formats = self.export_formats.value

        filename = self.filename

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        matter: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.matter, Unset):
            matter = self.matter.to_dict()

        document_template: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_template, Unset):
            document_template = self.document_template.to_dict()

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if state is not UNSET:
            field_dict["state"] = state
        if export_formats is not UNSET:
            field_dict["export_formats"] = export_formats
        if filename is not UNSET:
            field_dict["filename"] = filename
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if matter is not UNSET:
            field_dict["matter"] = matter
        if document_template is not UNSET:
            field_dict["document_template"] = document_template
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_base import DocumentBase
        from ..models.document_template_base import DocumentTemplateBase
        from ..models.matter_base import MatterBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, DocumentAutomationBaseState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = DocumentAutomationBaseState(_state)

        _export_formats = d.pop("export_formats", UNSET)
        export_formats: Union[Unset, DocumentAutomationBaseExportFormats]
        if isinstance(_export_formats, Unset):
            export_formats = UNSET
        else:
            export_formats = DocumentAutomationBaseExportFormats(_export_formats)

        filename = d.pop("filename", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        _matter = d.pop("matter", UNSET)
        matter: Union[Unset, MatterBase]
        if isinstance(_matter, Unset):
            matter = UNSET
        else:
            matter = MatterBase.from_dict(_matter)

        _document_template = d.pop("document_template", UNSET)
        document_template: Union[Unset, DocumentTemplateBase]
        if isinstance(_document_template, Unset):
            document_template = UNSET
        else:
            document_template = DocumentTemplateBase.from_dict(_document_template)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = DocumentBase.from_dict(documents_item_data)

            documents.append(documents_item)

        document_automation = cls(
            id=id,
            etag=etag,
            state=state,
            export_formats=export_formats,
            filename=filename,
            created_at=created_at,
            updated_at=updated_at,
            matter=matter,
            document_template=document_template,
            documents=documents,
        )

        document_automation.additional_properties = d
        return document_automation

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
