
"""
    Clio API Documentation

    # Developer Support and Feedback * Clio takes the availability and stability of our API seriously; please report any **degradations** or **breakages** to Clio's API Support team at [api@clio.com](mailto:api@clio.com). * For business and partnership inquiries, contact our API Partnerships team at [api.partnerships@clio.com](mailto:api.partnerships@clio.com). * For best practices and tips from the Clio development community, join the conversation in the [Clio Developer Slack Channel](https://join.slack.com/t/clio-public/shared_invite/zt-1bd5nfbiv-WloZR3ZjepoUTv28SI1ezw).  A community-driven [Clio Developers Stack Overflow Group](https://stackoverflow.com/questions/tagged/clio-api) also exists where you can connect and ask questions from other Clio API users. # Getting Started > **Note:** The API is available in four distinct data regions: Australia (au.app.clio.com), Canada (ca.app.clio.com), EU (eu.app.clio.com) and US (app.clio.com). > > Likewise, the developer portal is available at region-specific links for the [Australia](https://au.developers.clio.com), [Canada](https://ca.developers.clio.com), [EU](https://eu.developers.clio.com), and [US](https://developers.clio.com) regions. > > This document assumes the US region is being used (app.clio.com). If you're building in one of the other regions, you should adapt the links and examples as necessary.  To start building on the Clio API, you’ll need a Clio account – you can review our [Developer Handbook](https://docs.developers.clio.com/) and follow the steps to sign up for an account.  Once you have an account, you can [create a developer application](https://docs.developers.clio.com/api-docs/applications) from the [Developer Portal](https://developers.clio.com) and start building! # Authorization with OAuth 2.0 See our [Authorization documentation →](https://docs.developers.clio.com/api-docs/authorization) # Permissions See our [Permissions documentation →](https://docs.developers.clio.com/api-docs/permissions) # Fields See our [Fields documentation →](https://docs.developers.clio.com/api-docs/fields) # Rate Limiting See our [Rate Limits documentation →](https://docs.developers.clio.com/api-docs/rate-limits) # Paging See our [Pagination documentation →](https://docs.developers.clio.com/api-docs/paging) # ETags See our [ETags documentation →](https://docs.developers.clio.com/api-docs/etags) # Minor Versions API v4 supports multiple minor versions. Versions are of the form '4.X.Y'. To request a specific version, you can use an `X-API-VERSION` header in your request, with the header value set to the API version you're requesting. If this header is omitted, it will be treated as a request for the default API version. If the header is present but invalid, it will return a `410 Gone` response. If the header is present and valid, but it is no longer supported, it will return a `410 Gone` response.  An `X-API-VERSION` will be included in all successful responses, with the value being set to the API version used.  You can find our [API Versioning Policy and Guidelines](https://docs.developers.clio.com/api-docs/api-versioning-policy) in our documentation hub.  The [API Changelog](https://docs.developers.clio.com/api-docs/api-changelog) explains each version's changes in further detail. - 4.0.4    Update `quantity` field to return values in seconds rather than hours for Activities  - 4.0.5    * Remove `matter_balances` field from Bills   * Standardize status/state enum values   * Add a Document association to completed DocumentAutomations   * Add rate visibility handling for Activity's price and total  - 4.0.6    Remove `document_versions` collection field from Documents  - 4.0.7    Change secure link format  - 4.0.8    * `Activity` hours are redacted in the response based on the activity hours visibility setting for the user   * Add `quantity_redacted` field to activities  - 4.0.9    **This is the default version**    Contacts are filtered and redacted in the response based on the new 'Contacts Visibility' user permission setting.  - 4.0.10    Fixed validation of `type` query parameter when querying Notes   

    The version of the OpenAPI document: v4
    Contact: api@clio.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing_extensions import Self


class MatterContactsBase(BaseModel):
    """
    MatterContactsBase
    """ # noqa: E501
    contact_created_at: Optional[datetime] = Field(default=None, description="Timestamp of the time the contact was created")
    contact_updated_at: Optional[datetime] = Field(default=None, description="Timestamp of the time the contact was created")
    created_at: Optional[datetime] = Field(default=None, description="The time the *MatterContacts* was created (as a ISO-8601 timestamp)")
    description: Optional[StrictStr] = Field(default=None, description="Description of the matter")
    etag: Optional[StrictStr] = Field(default=None, description="ETag for the *MatterContacts*")
    first_name: Optional[StrictStr] = Field(default=None, description="First name of the Person")
    id: Optional[StrictInt] = Field(default=None, description="Unique identifier for the *MatterContacts*")
    initials: Optional[StrictStr] = Field(default=None, description="The initials of the *MatterContacts*")
    is_client: Optional[StrictBool] = Field(default=None, description="Whether or not the MatterContacts is a client")
    last_name: Optional[StrictStr] = Field(default=None, description="Last name of the Person")
    matter_id: Optional[StrictInt] = Field(default=None, description="ID of the matter")
    matter_number: Optional[StrictStr] = Field(default=None, description="Number of the matter")
    middle_name: Optional[StrictStr] = Field(default=None, description="Middle name of the Person")
    name: Optional[StrictStr] = Field(default=None, description="The full name of the *MatterContacts*")
    prefix: Optional[StrictStr] = Field(default=None, description="The prefix of the *MatterContacts* (Mr, Mrs, etc)")
    primary_email_address: Optional[StrictStr] = Field(default=None, description="The primary email address associated with this *MatterContacts*.")
    primary_phone_number: Optional[StrictStr] = Field(default=None, description="The primary phone number associated with this *MatterContacts*.")
    relationship_name: Optional[StrictStr] = Field(default=None, description="The description of the relation between the contact and the matter, or \"Client\" if the user is the client.")
    secondary_email_address: Optional[StrictStr] = Field(default=None, description="The secondary email address of the contact")
    secondary_phone_number: Optional[StrictStr] = Field(default=None, description="The secondary phone number of the contact")
    title: Optional[StrictStr] = Field(default=None, description="The designated title of the *MatterContacts*")
    type: Optional[StrictStr] = Field(default=None, description="The type of the *MatterContacts*")
    updated_at: Optional[datetime] = Field(default=None, description="The time the *MatterContacts* was last updated (as a ISO-8601 timestamp)")
    client_connect_user_id: Optional[StrictInt] = Field(default=None, description="The client connect ID of the contacts associated user")
    __properties: ClassVar[List[str]] = ["contact_created_at", "contact_updated_at", "created_at", "description", "etag", "first_name", "id", "initials", "is_client", "last_name", "matter_id", "matter_number", "middle_name", "name", "prefix", "primary_email_address", "primary_phone_number", "relationship_name", "secondary_email_address", "secondary_phone_number", "title", "type", "updated_at", "client_connect_user_id"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Company', 'Person']):
            raise ValueError("must be one of enum values ('Company', 'Person')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of MatterContactsBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatterContactsBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact_created_at": obj.get("contact_created_at"),
            "contact_updated_at": obj.get("contact_updated_at"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "etag": obj.get("etag"),
            "first_name": obj.get("first_name"),
            "id": obj.get("id"),
            "initials": obj.get("initials"),
            "is_client": obj.get("is_client"),
            "last_name": obj.get("last_name"),
            "matter_id": obj.get("matter_id"),
            "matter_number": obj.get("matter_number"),
            "middle_name": obj.get("middle_name"),
            "name": obj.get("name"),
            "prefix": obj.get("prefix"),
            "primary_email_address": obj.get("primary_email_address"),
            "primary_phone_number": obj.get("primary_phone_number"),
            "relationship_name": obj.get("relationship_name"),
            "secondary_email_address": obj.get("secondary_email_address"),
            "secondary_phone_number": obj.get("secondary_phone_number"),
            "title": obj.get("title"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "client_connect_user_id": obj.get("client_connect_user_id")
        })
        return _obj


