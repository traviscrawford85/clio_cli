import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_category_base import DocumentCategoryBase
    from ..models.user_base import UserBase


T = TypeVar("T", bound="DocumentTemplate")


@_attrs_define
class DocumentTemplate:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *DocumentTemplate*
        etag (Union[Unset, str]): ETag for the *DocumentTemplate*
        size (Union[Unset, int]): The size in bytes of the template
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data.
        filename (Union[Unset, str]): The name of the original file that was uploaded
        created_at (Union[Unset, datetime.datetime]): The time the *DocumentTemplate* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *DocumentTemplate* was last updated (as a ISO-8601
            timestamp)
        document_category (Union[Unset, DocumentCategoryBase]):
        last_modified_by (Union[Unset, UserBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    document_category: Union[Unset, "DocumentCategoryBase"] = UNSET
    last_modified_by: Union[Unset, "UserBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        size = self.size

        content_type = self.content_type

        filename = self.filename

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        document_category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document_category, Unset):
            document_category = self.document_category.to_dict()

        last_modified_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_modified_by, Unset):
            last_modified_by = self.last_modified_by.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if size is not UNSET:
            field_dict["size"] = size
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if filename is not UNSET:
            field_dict["filename"] = filename
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if document_category is not UNSET:
            field_dict["document_category"] = document_category
        if last_modified_by is not UNSET:
            field_dict["last_modified_by"] = last_modified_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_category_base import DocumentCategoryBase
        from ..models.user_base import UserBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        size = d.pop("size", UNSET)

        content_type = d.pop("content_type", UNSET)

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

        _document_category = d.pop("document_category", UNSET)
        document_category: Union[Unset, DocumentCategoryBase]
        if isinstance(_document_category, Unset):
            document_category = UNSET
        else:
            document_category = DocumentCategoryBase.from_dict(_document_category)

        _last_modified_by = d.pop("last_modified_by", UNSET)
        last_modified_by: Union[Unset, UserBase]
        if isinstance(_last_modified_by, Unset):
            last_modified_by = UNSET
        else:
            last_modified_by = UserBase.from_dict(_last_modified_by)

        document_template = cls(
            id=id,
            etag=etag,
            size=size,
            content_type=content_type,
            filename=filename,
            created_at=created_at,
            updated_at=updated_at,
            document_category=document_category,
            last_modified_by=last_modified_by,
        )

        document_template.additional_properties = d
        return document_template

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
