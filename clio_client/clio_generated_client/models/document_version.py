import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clio_creator_base import ClioCreatorBase
    from ..models.multipart import Multipart
    from ..models.multipart_header_base import MultipartHeaderBase


T = TypeVar("T", bound="DocumentVersion")


@_attrs_define
class DocumentVersion:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *DocumentVersion*
        document_id (Union[Unset, int]): The ID of the parent document.
        etag (Union[Unset, str]): ETag for the *DocumentVersion*
        uuid (Union[Unset, str]): UUID associated with the DocumentVersion. UUID is required to mark a document fully
            uploaded.
        created_at (Union[Unset, datetime.datetime]): The time the *DocumentVersion* was created (as a ISO-8601
            timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *DocumentVersion* was last updated (as a ISO-8601
            timestamp)
        filename (Union[Unset, str]): The uploaded file name of the DocumentVersion.
        size (Union[Unset, int]): The size of the DocumentVersion in bytes.
        version_number (Union[Unset, int]): The ordered number of when this DocumentVersion was uploaded.
        content_type (Union[Unset, str]): A standard MIME type describing the format of the object data.
        received_at (Union[Unset, datetime.datetime]): The time the DocumentVersion was received (as an ISO-8601
            timestamp)
        put_url (Union[Unset, str]): A signed URL for uploading the file in a single operation. It expires in 10
            minutes. If the document is fully uploaded, the field is empty.
        fully_uploaded (Union[Unset, bool]): True if the DocumentVersion is uploaded. False if the DocumentVersion is
            being uploaded.
        creator (Union[Unset, ClioCreatorBase]):
        put_headers (Union[Unset, list['MultipartHeaderBase']]): MultipartHeader
        multiparts (Union[Unset, list['Multipart']]): Multipart
    """

    id: Union[Unset, int] = UNSET
    document_id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    filename: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    version_number: Union[Unset, int] = UNSET
    content_type: Union[Unset, str] = UNSET
    received_at: Union[Unset, datetime.datetime] = UNSET
    put_url: Union[Unset, str] = UNSET
    fully_uploaded: Union[Unset, bool] = UNSET
    creator: Union[Unset, "ClioCreatorBase"] = UNSET
    put_headers: Union[Unset, list["MultipartHeaderBase"]] = UNSET
    multiparts: Union[Unset, list["Multipart"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        etag = self.etag

        uuid = self.uuid

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        filename = self.filename

        size = self.size

        version_number = self.version_number

        content_type = self.content_type

        received_at: Union[Unset, str] = UNSET
        if not isinstance(self.received_at, Unset):
            received_at = self.received_at.isoformat()

        put_url = self.put_url

        fully_uploaded = self.fully_uploaded

        creator: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        put_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.put_headers, Unset):
            put_headers = []
            for put_headers_item_data in self.put_headers:
                put_headers_item = put_headers_item_data.to_dict()
                put_headers.append(put_headers_item)

        multiparts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.multiparts, Unset):
            multiparts = []
            for multiparts_item_data in self.multiparts:
                multiparts_item = multiparts_item_data.to_dict()
                multiparts.append(multiparts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size is not UNSET:
            field_dict["size"] = size
        if version_number is not UNSET:
            field_dict["version_number"] = version_number
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if put_url is not UNSET:
            field_dict["put_url"] = put_url
        if fully_uploaded is not UNSET:
            field_dict["fully_uploaded"] = fully_uploaded
        if creator is not UNSET:
            field_dict["creator"] = creator
        if put_headers is not UNSET:
            field_dict["put_headers"] = put_headers
        if multiparts is not UNSET:
            field_dict["multiparts"] = multiparts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clio_creator_base import ClioCreatorBase
        from ..models.multipart import Multipart
        from ..models.multipart_header_base import MultipartHeaderBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        document_id = d.pop("document_id", UNSET)

        etag = d.pop("etag", UNSET)

        uuid = d.pop("uuid", UNSET)

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

        filename = d.pop("filename", UNSET)

        size = d.pop("size", UNSET)

        version_number = d.pop("version_number", UNSET)

        content_type = d.pop("content_type", UNSET)

        _received_at = d.pop("received_at", UNSET)
        received_at: Union[Unset, datetime.datetime]
        if isinstance(_received_at, Unset):
            received_at = UNSET
        else:
            received_at = isoparse(_received_at)

        put_url = d.pop("put_url", UNSET)

        fully_uploaded = d.pop("fully_uploaded", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: Union[Unset, ClioCreatorBase]
        if isinstance(_creator, Unset):
            creator = UNSET
        else:
            creator = ClioCreatorBase.from_dict(_creator)

        put_headers = []
        _put_headers = d.pop("put_headers", UNSET)
        for put_headers_item_data in _put_headers or []:
            put_headers_item = MultipartHeaderBase.from_dict(put_headers_item_data)

            put_headers.append(put_headers_item)

        multiparts = []
        _multiparts = d.pop("multiparts", UNSET)
        for multiparts_item_data in _multiparts or []:
            multiparts_item = Multipart.from_dict(multiparts_item_data)

            multiparts.append(multiparts_item)

        document_version = cls(
            id=id,
            document_id=document_id,
            etag=etag,
            uuid=uuid,
            created_at=created_at,
            updated_at=updated_at,
            filename=filename,
            size=size,
            version_number=version_number,
            content_type=content_type,
            received_at=received_at,
            put_url=put_url,
            fully_uploaded=fully_uploaded,
            creator=creator,
            put_headers=put_headers,
            multiparts=multiparts,
        )

        document_version.additional_properties = d
        return document_version

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
