import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.contactupdate_files_body_data_type import ContactupdateFilesBodyDataType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contactupdate_files_body_data_addresses_item import ContactupdateFilesBodyDataAddressesItem
    from ..models.contactupdate_files_body_data_avatar import ContactupdateFilesBodyDataAvatar
    from ..models.contactupdate_files_body_data_co_counsel_rate import ContactupdateFilesBodyDataCoCounselRate
    from ..models.contactupdate_files_body_data_company import ContactupdateFilesBodyDataCompany
    from ..models.contactupdate_files_body_data_currency import ContactupdateFilesBodyDataCurrency
    from ..models.contactupdate_files_body_data_custom_field_set_associations_item import (
        ContactupdateFilesBodyDataCustomFieldSetAssociationsItem,
    )
    from ..models.contactupdate_files_body_data_custom_field_values_item import (
        ContactupdateFilesBodyDataCustomFieldValuesItem,
    )
    from ..models.contactupdate_files_body_data_email_addresses_item import ContactupdateFilesBodyDataEmailAddressesItem
    from ..models.contactupdate_files_body_data_instant_messengers_item import (
        ContactupdateFilesBodyDataInstantMessengersItem,
    )
    from ..models.contactupdate_files_body_data_phone_numbers_item import ContactupdateFilesBodyDataPhoneNumbersItem
    from ..models.contactupdate_files_body_data_web_sites_item import ContactupdateFilesBodyDataWebSitesItem


T = TypeVar("T", bound="ContactupdateFilesBodyData")


@_attrs_define
class ContactupdateFilesBodyData:
    """
    Attributes:
        addresses (Union[Unset, list['ContactupdateFilesBodyDataAddressesItem']]):
        avatar (Union[Unset, ContactupdateFilesBodyDataAvatar]):
        clio_connect_email (Union[Unset, str]): Notifications will be sent to this email when a resource is shared.
        co_counsel_rate (Union[Unset, ContactupdateFilesBodyDataCoCounselRate]):
        company (Union[Unset, ContactupdateFilesBodyDataCompany]):
        currency (Union[Unset, ContactupdateFilesBodyDataCurrency]): The Currency the contact is associated with.
        custom_field_set_associations (Union[Unset, list['ContactupdateFilesBodyDataCustomFieldSetAssociationsItem']]):
        custom_field_values (Union[Unset, list['ContactupdateFilesBodyDataCustomFieldValuesItem']]):
        date_of_birth (Union[Unset, datetime.date]): Date of birth of the Contact.
        email_addresses (Union[Unset, list['ContactupdateFilesBodyDataEmailAddressesItem']]):
        first_name (Union[Unset, str]): First name of the Contact.
        instant_messengers (Union[Unset, list['ContactupdateFilesBodyDataInstantMessengersItem']]):
        last_name (Union[Unset, str]): Last name of the Contact.
        ledes_client_id (Union[Unset, str]): LEDES client id of the Contact.
        middle_name (Union[Unset, str]): Middle name of the Contact.
        name (Union[Unset, str]): Full name of the Contact. For requirements, see [Contact
            Name](https://docs.developers.clio.com/api-reference/#section/Contact-Name).
        phone_numbers (Union[Unset, list['ContactupdateFilesBodyDataPhoneNumbersItem']]):
        prefix (Union[Unset, str]): Personal title of the Contact.
        sales_tax_number (Union[Unset, str]): A contact's sales tax number will appear on invoices generated for the
            Contact.
        title (Union[Unset, str]): Professional title of the Contact.
        type_ (Union[Unset, ContactupdateFilesBodyDataType]): Type of the Contact.
        web_sites (Union[Unset, list['ContactupdateFilesBodyDataWebSitesItem']]):
    """

    addresses: Union[Unset, list["ContactupdateFilesBodyDataAddressesItem"]] = UNSET
    avatar: Union[Unset, "ContactupdateFilesBodyDataAvatar"] = UNSET
    clio_connect_email: Union[Unset, str] = UNSET
    co_counsel_rate: Union[Unset, "ContactupdateFilesBodyDataCoCounselRate"] = UNSET
    company: Union[Unset, "ContactupdateFilesBodyDataCompany"] = UNSET
    currency: Union[Unset, "ContactupdateFilesBodyDataCurrency"] = UNSET
    custom_field_set_associations: Union[Unset, list["ContactupdateFilesBodyDataCustomFieldSetAssociationsItem"]] = (
        UNSET
    )
    custom_field_values: Union[Unset, list["ContactupdateFilesBodyDataCustomFieldValuesItem"]] = UNSET
    date_of_birth: Union[Unset, datetime.date] = UNSET
    email_addresses: Union[Unset, list["ContactupdateFilesBodyDataEmailAddressesItem"]] = UNSET
    first_name: Union[Unset, str] = UNSET
    instant_messengers: Union[Unset, list["ContactupdateFilesBodyDataInstantMessengersItem"]] = UNSET
    last_name: Union[Unset, str] = UNSET
    ledes_client_id: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    phone_numbers: Union[Unset, list["ContactupdateFilesBodyDataPhoneNumbersItem"]] = UNSET
    prefix: Union[Unset, str] = UNSET
    sales_tax_number: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, ContactupdateFilesBodyDataType] = UNSET
    web_sites: Union[Unset, list["ContactupdateFilesBodyDataWebSitesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.addresses, Unset):
            addresses = []
            for addresses_item_data in self.addresses:
                addresses_item = addresses_item_data.to_dict()
                addresses.append(addresses_item)

        avatar: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.avatar, Unset):
            avatar = self.avatar.to_dict()

        clio_connect_email = self.clio_connect_email

        co_counsel_rate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.co_counsel_rate, Unset):
            co_counsel_rate = self.co_counsel_rate.to_dict()

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        currency: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.currency, Unset):
            currency = self.currency.to_dict()

        custom_field_set_associations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_set_associations, Unset):
            custom_field_set_associations = []
            for custom_field_set_associations_item_data in self.custom_field_set_associations:
                custom_field_set_associations_item = custom_field_set_associations_item_data.to_dict()
                custom_field_set_associations.append(custom_field_set_associations_item)

        custom_field_values: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.custom_field_values, Unset):
            custom_field_values = []
            for custom_field_values_item_data in self.custom_field_values:
                custom_field_values_item = custom_field_values_item_data.to_dict()
                custom_field_values.append(custom_field_values_item)

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        email_addresses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = []
            for email_addresses_item_data in self.email_addresses:
                email_addresses_item = email_addresses_item_data.to_dict()
                email_addresses.append(email_addresses_item)

        first_name = self.first_name

        instant_messengers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.instant_messengers, Unset):
            instant_messengers = []
            for instant_messengers_item_data in self.instant_messengers:
                instant_messengers_item = instant_messengers_item_data.to_dict()
                instant_messengers.append(instant_messengers_item)

        last_name = self.last_name

        ledes_client_id = self.ledes_client_id

        middle_name = self.middle_name

        name = self.name

        phone_numbers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.phone_numbers, Unset):
            phone_numbers = []
            for phone_numbers_item_data in self.phone_numbers:
                phone_numbers_item = phone_numbers_item_data.to_dict()
                phone_numbers.append(phone_numbers_item)

        prefix = self.prefix

        sales_tax_number = self.sales_tax_number

        title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        web_sites: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.web_sites, Unset):
            web_sites = []
            for web_sites_item_data in self.web_sites:
                web_sites_item = web_sites_item_data.to_dict()
                web_sites.append(web_sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if clio_connect_email is not UNSET:
            field_dict["clio_connect_email"] = clio_connect_email
        if co_counsel_rate is not UNSET:
            field_dict["co_counsel_rate"] = co_counsel_rate
        if company is not UNSET:
            field_dict["company"] = company
        if currency is not UNSET:
            field_dict["currency"] = currency
        if custom_field_set_associations is not UNSET:
            field_dict["custom_field_set_associations"] = custom_field_set_associations
        if custom_field_values is not UNSET:
            field_dict["custom_field_values"] = custom_field_values
        if date_of_birth is not UNSET:
            field_dict["date_of_birth"] = date_of_birth
        if email_addresses is not UNSET:
            field_dict["email_addresses"] = email_addresses
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if instant_messengers is not UNSET:
            field_dict["instant_messengers"] = instant_messengers
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if ledes_client_id is not UNSET:
            field_dict["ledes_client_id"] = ledes_client_id
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if name is not UNSET:
            field_dict["name"] = name
        if phone_numbers is not UNSET:
            field_dict["phone_numbers"] = phone_numbers
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if sales_tax_number is not UNSET:
            field_dict["sales_tax_number"] = sales_tax_number
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if web_sites is not UNSET:
            field_dict["web_sites"] = web_sites

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contactupdate_files_body_data_addresses_item import ContactupdateFilesBodyDataAddressesItem
        from ..models.contactupdate_files_body_data_avatar import ContactupdateFilesBodyDataAvatar
        from ..models.contactupdate_files_body_data_co_counsel_rate import ContactupdateFilesBodyDataCoCounselRate
        from ..models.contactupdate_files_body_data_company import ContactupdateFilesBodyDataCompany
        from ..models.contactupdate_files_body_data_currency import ContactupdateFilesBodyDataCurrency
        from ..models.contactupdate_files_body_data_custom_field_set_associations_item import (
            ContactupdateFilesBodyDataCustomFieldSetAssociationsItem,
        )
        from ..models.contactupdate_files_body_data_custom_field_values_item import (
            ContactupdateFilesBodyDataCustomFieldValuesItem,
        )
        from ..models.contactupdate_files_body_data_email_addresses_item import (
            ContactupdateFilesBodyDataEmailAddressesItem,
        )
        from ..models.contactupdate_files_body_data_instant_messengers_item import (
            ContactupdateFilesBodyDataInstantMessengersItem,
        )
        from ..models.contactupdate_files_body_data_phone_numbers_item import ContactupdateFilesBodyDataPhoneNumbersItem
        from ..models.contactupdate_files_body_data_web_sites_item import ContactupdateFilesBodyDataWebSitesItem

        d = dict(src_dict)
        addresses = []
        _addresses = d.pop("addresses", UNSET)
        for addresses_item_data in _addresses or []:
            addresses_item = ContactupdateFilesBodyDataAddressesItem.from_dict(addresses_item_data)

            addresses.append(addresses_item)

        _avatar = d.pop("avatar", UNSET)
        avatar: Union[Unset, ContactupdateFilesBodyDataAvatar]
        if isinstance(_avatar, Unset):
            avatar = UNSET
        else:
            avatar = ContactupdateFilesBodyDataAvatar.from_dict(_avatar)

        clio_connect_email = d.pop("clio_connect_email", UNSET)

        _co_counsel_rate = d.pop("co_counsel_rate", UNSET)
        co_counsel_rate: Union[Unset, ContactupdateFilesBodyDataCoCounselRate]
        if isinstance(_co_counsel_rate, Unset):
            co_counsel_rate = UNSET
        else:
            co_counsel_rate = ContactupdateFilesBodyDataCoCounselRate.from_dict(_co_counsel_rate)

        _company = d.pop("company", UNSET)
        company: Union[Unset, ContactupdateFilesBodyDataCompany]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = ContactupdateFilesBodyDataCompany.from_dict(_company)

        _currency = d.pop("currency", UNSET)
        currency: Union[Unset, ContactupdateFilesBodyDataCurrency]
        if isinstance(_currency, Unset):
            currency = UNSET
        else:
            currency = ContactupdateFilesBodyDataCurrency.from_dict(_currency)

        custom_field_set_associations = []
        _custom_field_set_associations = d.pop("custom_field_set_associations", UNSET)
        for custom_field_set_associations_item_data in _custom_field_set_associations or []:
            custom_field_set_associations_item = ContactupdateFilesBodyDataCustomFieldSetAssociationsItem.from_dict(
                custom_field_set_associations_item_data
            )

            custom_field_set_associations.append(custom_field_set_associations_item)

        custom_field_values = []
        _custom_field_values = d.pop("custom_field_values", UNSET)
        for custom_field_values_item_data in _custom_field_values or []:
            custom_field_values_item = ContactupdateFilesBodyDataCustomFieldValuesItem.from_dict(
                custom_field_values_item_data
            )

            custom_field_values.append(custom_field_values_item)

        _date_of_birth = d.pop("date_of_birth", UNSET)
        date_of_birth: Union[Unset, datetime.date]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth).date()

        email_addresses = []
        _email_addresses = d.pop("email_addresses", UNSET)
        for email_addresses_item_data in _email_addresses or []:
            email_addresses_item = ContactupdateFilesBodyDataEmailAddressesItem.from_dict(email_addresses_item_data)

            email_addresses.append(email_addresses_item)

        first_name = d.pop("first_name", UNSET)

        instant_messengers = []
        _instant_messengers = d.pop("instant_messengers", UNSET)
        for instant_messengers_item_data in _instant_messengers or []:
            instant_messengers_item = ContactupdateFilesBodyDataInstantMessengersItem.from_dict(
                instant_messengers_item_data
            )

            instant_messengers.append(instant_messengers_item)

        last_name = d.pop("last_name", UNSET)

        ledes_client_id = d.pop("ledes_client_id", UNSET)

        middle_name = d.pop("middle_name", UNSET)

        name = d.pop("name", UNSET)

        phone_numbers = []
        _phone_numbers = d.pop("phone_numbers", UNSET)
        for phone_numbers_item_data in _phone_numbers or []:
            phone_numbers_item = ContactupdateFilesBodyDataPhoneNumbersItem.from_dict(phone_numbers_item_data)

            phone_numbers.append(phone_numbers_item)

        prefix = d.pop("prefix", UNSET)

        sales_tax_number = d.pop("sales_tax_number", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ContactupdateFilesBodyDataType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ContactupdateFilesBodyDataType(_type_)

        web_sites = []
        _web_sites = d.pop("web_sites", UNSET)
        for web_sites_item_data in _web_sites or []:
            web_sites_item = ContactupdateFilesBodyDataWebSitesItem.from_dict(web_sites_item_data)

            web_sites.append(web_sites_item)

        contactupdate_files_body_data = cls(
            addresses=addresses,
            avatar=avatar,
            clio_connect_email=clio_connect_email,
            co_counsel_rate=co_counsel_rate,
            company=company,
            currency=currency,
            custom_field_set_associations=custom_field_set_associations,
            custom_field_values=custom_field_values,
            date_of_birth=date_of_birth,
            email_addresses=email_addresses,
            first_name=first_name,
            instant_messengers=instant_messengers,
            last_name=last_name,
            ledes_client_id=ledes_client_id,
            middle_name=middle_name,
            name=name,
            phone_numbers=phone_numbers,
            prefix=prefix,
            sales_tax_number=sales_tax_number,
            title=title,
            type_=type_,
            web_sites=web_sites,
        )

        contactupdate_files_body_data.additional_properties = d
        return contactupdate_files_body_data

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
