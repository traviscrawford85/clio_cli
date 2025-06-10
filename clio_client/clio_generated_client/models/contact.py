import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.contact_base_type import ContactBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account_balance_base import AccountBalanceBase
    from ..models.activity_rate_base import ActivityRateBase
    from ..models.address_base import AddressBase
    from ..models.avatar_base import AvatarBase
    from ..models.contact_base import ContactBase
    from ..models.contact_base_currency import ContactBaseCurrency
    from ..models.custom_field_set_association_base import CustomFieldSetAssociationBase
    from ..models.custom_field_value import CustomFieldValue
    from ..models.email_address_base import EmailAddressBase
    from ..models.folder_base import FolderBase
    from ..models.instant_messenger_base import InstantMessengerBase
    from ..models.legal_aid_uk_contact_base import LegalAidUkContactBase
    from ..models.notification_method_base import NotificationMethodBase
    from ..models.payment_profile_base import PaymentProfileBase
    from ..models.phone_number_base import PhoneNumberBase
    from ..models.web_site_base import WebSiteBase


T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        id (Union[Unset, int]): Unique identifier for the *Contact*
        etag (Union[Unset, str]): ETag for the *Contact*
        name (Union[Unset, str]): The full name of the *Contact*
        first_name (Union[Unset, str]): First name of the Person
        middle_name (Union[Unset, str]): Middle name of the Person
        last_name (Union[Unset, str]): Last name of the Person
        date_of_birth (Union[Unset, datetime.date]): Date of birth
        type_ (Union[Unset, ContactBaseType]): The type of the *Contact*
        created_at (Union[Unset, datetime.datetime]): The time the *Contact* was created (as a ISO-8601 timestamp)
        updated_at (Union[Unset, datetime.datetime]): The time the *Contact* was last updated (as a ISO-8601 timestamp)
        prefix (Union[Unset, str]): The prefix of the *Contact* (Mr, Mrs, etc)
        title (Union[Unset, str]): The designated title of the *Contact*
        initials (Union[Unset, str]): The initials of the *Contact*
        clio_connect_email (Union[Unset, str]): Clio Connect email if the *Contact* is a ClioConnect User
        locked_clio_connect_email (Union[Unset, bool]): A boolean indicating if the ability to modify this *Contacts
            Clio connect email is locked.
        client_connect_user_id (Union[Unset, int]): The ID for the Clio Connect user associated with this *Contact*
        primary_email_address (Union[Unset, str]): The primary email address associated with this *Contact*.
        secondary_email_address (Union[Unset, str]): The secondary email address associated with this *Contact*.
        primary_phone_number (Union[Unset, str]): The primary phone number associated with this *Contact*.
        secondary_phone_number (Union[Unset, str]): The secondary phone number of the *Contact*.
        ledes_client_id (Union[Unset, str]): LEDES client id of the Contact
        has_clio_for_clients_permission (Union[Unset, bool]): True if at least one resource has been shared with the
            contact using Clio for Clients.
        is_client (Union[Unset, bool]): Whether or not the Contact is a client
        is_clio_for_client_user (Union[Unset, bool]): Whether or not this contact has client_login and client_user (can
            be created due to addition to client portal or client_share_permissions)
        is_co_counsel (Union[Unset, bool]): Whether or not the Contact has matters shared as co-counsel
        is_bill_recipient (Union[Unset, bool]): Whether the Contact is a bill recipient on at least one matter.
        sales_tax_number (Union[Unset, str]): The sales tax number of the *Contact*
        currency (Union[Unset, ContactBaseCurrency]): Currency of the *Contact*
        activity_rates (Union[Unset, list['ActivityRateBase']]): ActivityRate
        addresses (Union[Unset, list['AddressBase']]): Address
        custom_field_values (Union[Unset, list['CustomFieldValue']]): CustomFieldValue
        custom_field_set_associations (Union[Unset, list['CustomFieldSetAssociationBase']]): CustomFieldSetAssociation
        email_addresses (Union[Unset, list['EmailAddressBase']]): EmailAddress
        instant_messengers (Union[Unset, list['InstantMessengerBase']]): InstantMessenger
        phone_numbers (Union[Unset, list['PhoneNumberBase']]): PhoneNumber
        web_sites (Union[Unset, list['WebSiteBase']]): WebSite
        notification_methods (Union[Unset, list['NotificationMethodBase']]): NotificationMethod
        account_balances (Union[Unset, list['AccountBalanceBase']]): AccountBalance
        related_contacts (Union[Unset, list['ContactBase']]): Contact
        primary_work_address (Union[Unset, AddressBase]):
        primary_address (Union[Unset, AddressBase]):
        secondary_address (Union[Unset, AddressBase]):
        company (Union[Unset, ContactBase]):
        avatar (Union[Unset, AvatarBase]):
        payment_profile (Union[Unset, PaymentProfileBase]):
        folder (Union[Unset, FolderBase]):
        co_counsel_rate (Union[Unset, ActivityRateBase]):
        primary_web_site (Union[Unset, WebSiteBase]):
        legal_aid_uk_contact (Union[Unset, LegalAidUkContactBase]):
    """

    id: Union[Unset, int] = UNSET
    etag: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    type_: Union[Unset, ContactBaseType] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    prefix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    initials: Union[Unset, str] = UNSET
    clio_connect_email: Union[Unset, str] = UNSET
    locked_clio_connect_email: Union[Unset, bool] = UNSET
    client_connect_user_id: Union[Unset, int] = UNSET
    primary_email_address: Union[Unset, str] = UNSET
    secondary_email_address: Union[Unset, str] = UNSET
    primary_phone_number: Union[Unset, str] = UNSET
    secondary_phone_number: Union[Unset, str] = UNSET
    ledes_client_id: Union[Unset, str] = UNSET
    has_clio_for_clients_permission: Union[Unset, bool] = UNSET
    is_client: Union[Unset, bool] = UNSET
    is_clio_for_client_user: Union[Unset, bool] = UNSET
    is_co_counsel: Union[Unset, bool] = UNSET
    is_bill_recipient: Union[Unset, bool] = UNSET
    sales_tax_number: Union[Unset, str] = UNSET
    currency: Union[Unset, "ContactBaseCurrency"] = UNSET
    activity_rates: Union[Unset, list["ActivityRateBase"]] = UNSET
    addresses: Union[Unset, list["AddressBase"]] = UNSET
    custom_field_values: Union[Unset, list["CustomFieldValue"]] = UNSET
    custom_field_set_associations: Union[Unset, list["CustomFieldSetAssociationBase"]] = UNSET
    email_addresses: Union[Unset, list["EmailAddressBase"]] = UNSET
    instant_messengers: Union[Unset, list["InstantMessengerBase"]] = UNSET
    phone_numbers: Union[Unset, list["PhoneNumberBase"]] = UNSET
    web_sites: Union[Unset, list["WebSiteBase"]] = UNSET
    notification_methods: Union[Unset, list["NotificationMethodBase"]] = UNSET
    account_balances: Union[Unset, list["AccountBalanceBase"]] = UNSET
    related_contacts: Union[Unset, list["ContactBase"]] = UNSET
    primary_work_address: Union[Unset, "AddressBase"] = UNSET
    primary_address: Union[Unset, "AddressBase"] = UNSET
    secondary_address: Union[Unset, "AddressBase"] = UNSET
    company: Union[Unset, "ContactBase"] = UNSET
    avatar: Union[Unset, "AvatarBase"] = UNSET
    payment_profile: Union[Unset, "PaymentProfileBase"] = UNSET
    folder: Union[Unset, "FolderBase"] = UNSET
    co_counsel_rate: Union[Unset, "ActivityRateBase"] = UNSET
    primary_web_site: Union[Unset, "WebSiteBase"] = UNSET
    legal_aid_uk_contact: Union[Unset, "LegalAidUkContactBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        etag = self.etag

        name = self.name

        first_name = self.first_name

        middle_name = self.middle_name

        last_name = self.last_name

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        prefix = self.prefix

        title = self.title

        initials = self.initials

        clio_connect_email = self.clio_connect_email

        locked_clio_connect_email = self.locked_clio_connect_email

        client_connect_user_id = self.client_connect_user_id

        primary_email_address = self.primary_email_address

        secondary_email_address = self.secondary_email_address

        primary_phone_number = self.primary_phone_number

        secondary_phone_number = self.secondary_phone_number

        ledes_client_id = self.ledes_client_id

        has_clio_for_clients_permission = self.has_clio_for_clients_permission

        is_client = self.is_client

        is_clio_for_client_user = self.is_clio_for_client_user

        is_co_counsel = self.is_co_counsel

        is_bill_recipient = self.is_bill_recipient

        sales_tax_number = self.sales_tax_number

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        activity_rates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.activity_rates, Unset):
            activity_rates = []
            for activity_rates_item_data in self.activity_rates:
                activity_rates_item = activity_rates_item_data.to_dict()
                activity_rates.append(activity_rates_item)

        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        custom_field_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_values, Unset):
            custom_field_values = []
            for custom_field_values_item_data in self.custom_field_values:
                custom_field_values_item = custom_field_values_item_data.to_dict()
                custom_field_values.append(custom_field_values_item)

        custom_field_set_associations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_set_associations, Unset):
            custom_field_set_associations = []
            for custom_field_set_associations_item_data in self.custom_field_set_associations:
                custom_field_set_associations_item = custom_field_set_associations_item_data.to_dict()
                custom_field_set_associations.append(custom_field_set_associations_item)

        email_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = []
            for email_addresses_item_data in self.email_addresses:
                email_addresses_item = email_addresses_item_data.to_dict()
                email_addresses.append(email_addresses_item)

        instant_messengers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instant_messengers, Unset):
            instant_messengers = []
            for instant_messengers_item_data in self.instant_messengers:
                instant_messengers_item = instant_messengers_item_data.to_dict()
                instant_messengers.append(instant_messengers_item)

        phone_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        web_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.web_sites, Unset):
            web_sites = []
            for web_sites_item_data in self.web_sites:
                web_sites_item = web_sites_item_data.to_dict()
                web_sites.append(web_sites_item)

        notification_methods: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notification_methods, Unset):
            notification_methods = []
            for notification_methods_item_data in self.notification_methods:
                notification_methods_item = notification_methods_item_data.to_dict()
                notification_methods.append(notification_methods_item)

        account_balances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.account_balances, Unset):
            account_balances = []
            for account_balances_item_data in self.account_balances:
                account_balances_item = account_balances_item_data.to_dict()
                account_balances.append(account_balances_item)

        related_contacts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.related_contacts, Unset):
            related_contacts = []
            for related_contacts_item_data in self.related_contacts:
                related_contacts_item = related_contacts_item_data.to_dict()
                related_contacts.append(related_contacts_item)

        primary_work_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_work_address, Unset):
            primary_work_address = self.primary_work_address.to_dict()

        primary_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_address, Unset):
            primary_address = self.primary_address.to_dict()

        secondary_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.secondary_address, Unset):
            secondary_address = self.secondary_address.to_dict()

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        payment_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_profile, Unset):
            payment_profile = self.payment_profile.to_dict()

        folder: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.folder, Unset):
            folder = self.folder.to_dict()

        co_counsel_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.co_counsel_rate, Unset):
            co_counsel_rate = self.co_counsel_rate.to_dict()

        primary_web_site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.primary_web_site, Unset):
            primary_web_site = self.primary_web_site.to_dict()

        legal_aid_uk_contact: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.legal_aid_uk_contact, Unset):
            legal_aid_uk_contact = self.legal_aid_uk_contact.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if etag is not UNSET:
            field_dict["etag"] = etag
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if type_ is not UNSET:
            field_dict["type"] = type_
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if title is not UNSET:
            field_dict["title"] = title
        if initials is not UNSET:
            field_dict["initials"] = initials
        if clio_connect_email is not UNSET:
            field_dict["clio_connect_email"] = clio_connect_email
        if locked_clio_connect_email is not UNSET:
            field_dict["locked_clio_connect_email"] = locked_clio_connect_email
        if client_connect_user_id is not UNSET:
            field_dict["client_connect_user_id"] = client_connect_user_id
        if primary_email_address is not UNSET:
            field_dict["primary_email_address"] = primary_email_address
        if secondary_email_address is not UNSET:
            field_dict["secondary_email_address"] = secondary_email_address
        if primary_phone_number is not UNSET:
            field_dict["primary_phone_number"] = primary_phone_number
        if secondary_phone_number is not UNSET:
            field_dict["secondary_phone_number"] = secondary_phone_number
        if ledes_client_id is not UNSET:
            field_dict["ledes_client_id"] = ledes_client_id
        if has_clio_for_clients_permission is not UNSET:
            field_dict["has_clio_for_clients_permission"] = has_clio_for_clients_permission
        if is_client is not UNSET:
            field_dict["is_client"] = is_client
        if is_clio_for_client_user is not UNSET:
            field_dict["is_clio_for_client_user"] = is_clio_for_client_user
        if is_co_counsel is not UNSET:
            field_dict["is_co_counsel"] = is_co_counsel
        if is_bill_recipient is not UNSET:
            field_dict["is_bill_recipient"] = is_bill_recipient
        if sales_tax_number is not UNSET:
            field_dict["sales_tax_number"] = sales_tax_number
        if currency is not UNSET:
            field_dict["currency"] = currency
        if activity_rates is not UNSET:
            field_dict["activity_rates"] = activity_rates
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if custom_field_values is not UNSET:
            field_dict["custom_field_values"] = custom_field_values
        if custom_field_set_associations is not UNSET:
            field_dict["custom_field_set_associations"] = custom_field_set_associations
        if email_addresses is not UNSET:
            field_dict["email_addresses"] = email_addresses
        if instant_messengers is not UNSET:
            field_dict["instant_messengers"] = instant_messengers
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if web_sites is not UNSET:
            field_dict["web_sites"] = web_sites
        if notification_methods is not UNSET:
            field_dict["notification_methods"] = notification_methods
        if account_balances is not UNSET:
            field_dict["account_balances"] = account_balances
        if related_contacts is not UNSET:
            field_dict["related_contacts"] = related_contacts
        if primary_work_address is not UNSET:
            field_dict["primary_work_address"] = primary_work_address
        if primary_address is not UNSET:
            field_dict["primary_address"] = primary_address
        if secondary_address is not UNSET:
            field_dict["secondary_address"] = secondary_address
        if company is not UNSET:
            field_dict["company"] = company
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if payment_profile is not UNSET:
            field_dict["payment_profile"] = payment_profile
        if folder is not UNSET:
            field_dict["folder"] = folder
        if co_counsel_rate is not UNSET:
            field_dict["co_counsel_rate"] = co_counsel_rate
        if primary_web_site is not UNSET:
            field_dict["primary_web_site"] = primary_web_site
        if legal_aid_uk_contact is not UNSET:
            field_dict["legal_aid_uk_contact"] = legal_aid_uk_contact

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_balance_base import AccountBalanceBase
        from ..models.activity_rate_base import ActivityRateBase
        from ..models.address_base import AddressBase
        from ..models.avatar_base import AvatarBase
        from ..models.contact_base import ContactBase
        from ..models.contact_base_currency import ContactBaseCurrency
        from ..models.custom_field_set_association_base import CustomFieldSetAssociationBase
        from ..models.custom_field_value import CustomFieldValue
        from ..models.email_address_base import EmailAddressBase
        from ..models.folder_base import FolderBase
        from ..models.instant_messenger_base import InstantMessengerBase
        from ..models.legal_aid_uk_contact_base import LegalAidUkContactBase
        from ..models.notification_method_base import NotificationMethodBase
        from ..models.payment_profile_base import PaymentProfileBase
        from ..models.phone_number_base import PhoneNumberBase
        from ..models.web_site_base import WebSiteBase

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        etag = d.pop("etag", UNSET)

        name = d.pop("name", UNSET)

        first_name = d.pop("first_name", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ContactBaseType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContactBaseType(_type_)

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

        prefix = d.pop("prefix", UNSET)

        title = d.pop("title", UNSET)

        initials = d.pop("initials", UNSET)

        clio_connect_email = d.pop("clio_connect_email", UNSET)

        locked_clio_connect_email = d.pop("locked_clio_connect_email", UNSET)

        client_connect_user_id = d.pop("client_connect_user_id", UNSET)

        primary_email_address = d.pop("primary_email_address", UNSET)

        secondary_email_address = d.pop("secondary_email_address", UNSET)

        primary_phone_number = d.pop("primary_phone_number", UNSET)

        secondary_phone_number = d.pop("secondary_phone_number", UNSET)

        ledes_client_id = d.pop("ledes_client_id", UNSET)

        has_clio_for_clients_permission = d.pop("has_clio_for_clients_permission", UNSET)

        is_client = d.pop("is_client", UNSET)

        is_clio_for_client_user = d.pop("is_clio_for_client_user", UNSET)

        is_co_counsel = d.pop("is_co_counsel", UNSET)

        is_bill_recipient = d.pop("is_bill_recipient", UNSET)

        sales_tax_number = d.pop("sales_tax_number", UNSET)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ContactBaseCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ContactBaseCurrency.from_dict(_currency)

        activity_rates = []
        _activity_rates = d.pop("activity_rates", UNSET)
        for activity_rates_item_data in _activity_rates or []:
            activity_rates_item = ActivityRateBase.from_dict(activity_rates_item_data)

            activity_rates.append(activity_rates_item)

        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = AddressBase.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        custom_field_values = []
        _custom_field_values = d.pop("custom_field_values", UNSET)
        for custom_field_values_item_data in _custom_field_values or []:
            custom_field_values_item = CustomFieldValue.from_dict(custom_field_values_item_data)

            custom_field_values.append(custom_field_values_item)

        custom_field_set_associations = []
        _custom_field_set_associations = d.pop("custom_field_set_associations", UNSET)
        for custom_field_set_associations_item_data in _custom_field_set_associations or []:
            custom_field_set_associations_item = CustomFieldSetAssociationBase.from_dict(
                custom_field_set_associations_item_data
            )

            custom_field_set_associations.append(custom_field_set_associations_item)

        email_addresses = []
        _email_addresses = d.pop("email_addresses", UNSET)
        for email_addresses_item_data in _email_addresses or []:
            email_addresses_item = EmailAddressBase.from_dict(email_addresses_item_data)

            email_addresses.append(email_addresses_item)

        instant_messengers = []
        _instant_messengers = d.pop("instant_messengers", UNSET)
        for instant_messengers_item_data in _instant_messengers or []:
            instant_messengers_item = InstantMessengerBase.from_dict(instant_messengers_item_data)

            instant_messengers.append(instant_messengers_item)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = PhoneNumberBase.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        web_sites = []
        _web_sites = d.pop("web_sites", UNSET)
        for web_sites_item_data in _web_sites or []:
            web_sites_item = WebSiteBase.from_dict(web_sites_item_data)

            web_sites.append(web_sites_item)

        notification_methods = []
        _notification_methods = d.pop("notification_methods", UNSET)
        for notification_methods_item_data in _notification_methods or []:
            notification_methods_item = NotificationMethodBase.from_dict(notification_methods_item_data)

            notification_methods.append(notification_methods_item)

        account_balances = []
        _account_balances = d.pop("account_balances", UNSET)
        for account_balances_item_data in _account_balances or []:
            account_balances_item = AccountBalanceBase.from_dict(account_balances_item_data)

            account_balances.append(account_balances_item)

        related_contacts = []
        _related_contacts = d.pop("related_contacts", UNSET)
        for related_contacts_item_data in _related_contacts or []:
            related_contacts_item = ContactBase.from_dict(related_contacts_item_data)

            related_contacts.append(related_contacts_item)

        _primary_work_address = d.pop("primary_work_address", UNSET)
        primary_work_address: Union[Unset, AddressBase]
        if isinstance(_primary_work_address, Unset):
            primary_work_address = UNSET
        else:
            primary_work_address = AddressBase.from_dict(_primary_work_address)

        _primary_address = d.pop("primary_address", UNSET)
        primary_address: Union[Unset, AddressBase]
        if isinstance(_primary_address, Unset):
            primary_address = UNSET
        else:
            primary_address = AddressBase.from_dict(_primary_address)

        _secondary_address = d.pop("secondary_address", UNSET)
        secondary_address: Union[Unset, AddressBase]
        if isinstance(_secondary_address, Unset):
            secondary_address = UNSET
        else:
            secondary_address = AddressBase.from_dict(_secondary_address)

        _company = d.pop("company", UNSET)
        company: Union[Unset, ContactBase]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = ContactBase.from_dict(_company)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, AvatarBase]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = AvatarBase.from_dict(_avatar)

        _payment_profile = d.pop("payment_profile", UNSET)
        payment_profile: Union[Unset, PaymentProfileBase]
        if isinstance(_payment_profile, Unset):
            payment_profile = UNSET
        else:
            payment_profile = PaymentProfileBase.from_dict(_payment_profile)

        _folder = d.pop("folder", UNSET)
        folder: Union[Unset, FolderBase]
        if isinstance(_folder, Unset):
            folder = UNSET
        else:
            folder = FolderBase.from_dict(_folder)

        _co_counsel_rate = d.pop("co_counsel_rate", UNSET)
        co_counsel_rate: Union[Unset, ActivityRateBase]
        if isinstance(_co_counsel_rate, Unset):
            co_counsel_rate = UNSET
        else:
            co_counsel_rate = ActivityRateBase.from_dict(_co_counsel_rate)

        _primary_web_site = d.pop("primary_web_site", UNSET)
        primary_web_site: Union[Unset, WebSiteBase]
        if isinstance(_primary_web_site, Unset):
            primary_web_site = UNSET
        else:
            primary_web_site = WebSiteBase.from_dict(_primary_web_site)

        _legal_aid_uk_contact = d.pop("legal_aid_uk_contact", UNSET)
        legal_aid_uk_contact: Union[Unset, LegalAidUkContactBase]
        if isinstance(_legal_aid_uk_contact, Unset):
            legal_aid_uk_contact = UNSET
        else:
            legal_aid_uk_contact = LegalAidUkContactBase.from_dict(_legal_aid_uk_contact)

        contact = cls(
            id=id,
            etag=etag,
            name=name,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            type_=type_,
            created_at=created_at,
            updated_at=updated_at,
            prefix=prefix,
            title=title,
            initials=initials,
            clio_connect_email=clio_connect_email,
            locked_clio_connect_email=locked_clio_connect_email,
            client_connect_user_id=client_connect_user_id,
            primary_email_address=primary_email_address,
            secondary_email_address=secondary_email_address,
            primary_phone_number=primary_phone_number,
            secondary_phone_number=secondary_phone_number,
            ledes_client_id=ledes_client_id,
            has_clio_for_clients_permission=has_clio_for_clients_permission,
            is_client=is_client,
            is_clio_for_client_user=is_clio_for_client_user,
            is_co_counsel=is_co_counsel,
            is_bill_recipient=is_bill_recipient,
            sales_tax_number=sales_tax_number,
            currency=currency,
            activity_rates=activity_rates,
            addresses=addresses,
            custom_field_values=custom_field_values,
            custom_field_set_associations=custom_field_set_associations,
            email_addresses=email_addresses,
            instant_messengers=instant_messengers,
            phone_numbers=phone_numbers,
            web_sites=web_sites,
            notification_methods=notification_methods,
            account_balances=account_balances,
            related_contacts=related_contacts,
            primary_work_address=primary_work_address,
            primary_address=primary_address,
            secondary_address=secondary_address,
            company=company,
            avatar=avatar,
            payment_profile=payment_profile,
            folder=folder,
            co_counsel_rate=co_counsel_rate,
            primary_web_site=primary_web_site,
            legal_aid_uk_contact=legal_aid_uk_contact,
        )

        contact.additional_properties = d
        return contact

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
