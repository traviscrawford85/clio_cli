import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalAidUkMatterBase")


@_attrs_define
class LegalAidUkMatterBase:
    """
    Attributes:
        access_point (Union[Unset, str]): Access point
        laa_office_number (Union[Unset, str]): LAA office number
        ait_hearing_centre (Union[Unset, int]): AIT hearing centre
        attended_several_hearings_acting_for_multiple_clients (Union[Unset, bool]): Attended several hearings acting for
            multiple clients
        bill_ho_ucn (Union[Unset, str]): Bill HO UCN
        bill_number_of_attendances (Union[Unset, int]): Bill number of attendances
        bill_outcome_for_the_client_code (Union[Unset, int]): Bill outcome for the client code
        bill_stage_reached_code (Union[Unset, int]): Bill stage reached code
        case_reference (Union[Unset, str]): Case reference
        case_start_date (Union[Unset, datetime.date]): Case start date
        category (Union[Unset, int]): Category
        category_as_string (Union[Unset, str]): Category as string
        certificate_effective_date (Union[Unset, datetime.date]): Certificate effective date
        certificate_expiration_date (Union[Unset, datetime.date]): Certificate expiration date
        certificate_number (Union[Unset, str]): Certificate number
        certificate_scope (Union[Unset, str]): Certificate scope
        certification_type (Union[Unset, int]): Certification type
        change_of_solicitor (Union[Unset, bool]): Change of solicitor
        client_equal_opportunity_monitoring (Union[Unset, str]): Client equal opportunity monitoring
        client_type (Union[Unset, int]): Client type
        clr_start_date (Union[Unset, datetime.date]): CLR start date
        clr_total_profit_costs (Union[Unset, str]): CLR total profit costs
        cost_limit (Union[Unset, str]): Cost limit
        counsel (Union[Unset, int]): Counsel
        court (Union[Unset, int]): Court
        court_id (Union[Unset, int]): Court ID
        court_id_code (Union[Unset, str]): Court ID code
        created_at (Union[Unset, datetime.datetime]): The time the *LegalAidUkMatter* was created (as a ISO-8601
            timestamp)
        delivery_location (Union[Unset, str]): Delivery location
        dscc_number (Union[Unset, str]): DSCC number
        duty_solicitor (Union[Unset, bool]): Duty solicitor
        etag (Union[Unset, str]): ETag for the *LegalAidUkMatter*
        exceptional_case_funding_reference (Union[Unset, str]): Exceptional case funding reference
        expense_limit (Union[Unset, str]): Expense limit
        fee_scheme (Union[Unset, int]): Fee scheme
        first_conducting_solicitor (Union[Unset, bool]): First conducting solicitor
        id (Union[Unset, int]): Unique identifier for the *LegalAidUkMatter*
        irc_surgery (Union[Unset, str]): Irc surgery
        legacy_case (Union[Unset, str]): Legacy case
        legal_representation_number (Union[Unset, str]): Legal representation number
        lh_total_disbursements (Union[Unset, str]): LH total disbursements
        lh_start_date (Union[Unset, str]): LH start date
        lh_total_profit_costs (Union[Unset, str]): LH total profit costs
        linked_matter_id (Union[Unset, int]): Linked matter ID
        local_authority_number (Union[Unset, str]): Local authority number
        maat_id (Union[Unset, str]): MAAT ID
        matter_type (Union[Unset, int]): Matter type
        matter_type_code (Union[Unset, str]): Matter type code
        matter_type_1 (Union[Unset, int]): Matter type 1
        matter_type_1_code (Union[Unset, str]): Matter type 1 code
        matter_type_1_title (Union[Unset, str]): Matter type 1 title
        matter_type_2 (Union[Unset, int]): Matter type 2
        matter_type_2_code (Union[Unset, str]): Matter type 2 code
        matter_type_2_title (Union[Unset, str]): Matter type 2 title
        matter_types_combined (Union[Unset, str]): Matter types combined
        number_of_clients_seen_at_surgery (Union[Unset, int]): Number of clients seen at surgery
        number_of_clients (Union[Unset, int]): Number of clients
        party (Union[Unset, int]): Party
        police_station (Union[Unset, str]): Police station
        post_transfer_clients_represented (Union[Unset, int]): Post transfer clients represented
        postal_application_accepted (Union[Unset, str]): Postal application accepted
        prior_authority_reference (Union[Unset, str]): Priory authority reference
        prison_id (Union[Unset, int]): Prison ID
        prison_law_prior_approval_number (Union[Unset, str]): Prison law prior approval number
        procurement_area (Union[Unset, str]): Procurement area
        region (Union[Unset, int]): Region
        related_claims_number (Union[Unset, str]): Related claims number
        representation_order_date (Union[Unset, datetime.date]): Representation order date
        schedule_reference_number (Union[Unset, str]): Schedule reference number
        scheme_id (Union[Unset, str]): Scheme ID
        session_type (Union[Unset, int]): Session type
        solicitor_type (Union[Unset, int]): Solicitor type
        standard_fee_category (Union[Unset, int]): Standard fee category
        surgery_clients_resulting_in_a_legal_help_matter_opened (Union[Unset, int]): Surgery clients resulting in a
            legal help matter opened
        surgery_clients (Union[Unset, int]): Surgery clients
        surgery_date (Union[Unset, datetime.date]): Surgery date
        transfer_date (Union[Unset, datetime.date]): Transfer date
        type_of_advice (Union[Unset, int]): Type of advice
        type_of_service (Union[Unset, str]): Type of service
        ucn (Union[Unset, str]): UCN
        ufn (Union[Unset, str]): UFN
        undesignated_area_court (Union[Unset, bool]): Undesignated area court
        updated_at (Union[Unset, datetime.datetime]): The time the *LegalAidUkMatter* was last updated (as a ISO-8601
            timestamp)
        user_type (Union[Unset, int]): User type
        youth_court (Union[Unset, bool]): Youth court
    """

    access_point: Union[Unset, str] = UNSET
    laa_office_number: Union[Unset, str] = UNSET
    ait_hearing_centre: Union[Unset, int] = UNSET
    attended_several_hearings_acting_for_multiple_clients: Union[Unset, bool] = UNSET
    bill_ho_ucn: Union[Unset, str] = UNSET
    bill_number_of_attendances: Union[Unset, int] = UNSET
    bill_outcome_for_the_client_code: Union[Unset, int] = UNSET
    bill_stage_reached_code: Union[Unset, int] = UNSET
    case_reference: Union[Unset, str] = UNSET
    case_start_date: Union[Unset, datetime.date] = UNSET
    category: Union[Unset, int] = UNSET
    category_as_string: Union[Unset, str] = UNSET
    certificate_effective_date: Union[Unset, datetime.date] = UNSET
    certificate_expiration_date: Union[Unset, datetime.date] = UNSET
    certificate_number: Union[Unset, str] = UNSET
    certificate_scope: Union[Unset, str] = UNSET
    certification_type: Union[Unset, int] = UNSET
    change_of_solicitor: Union[Unset, bool] = UNSET
    client_equal_opportunity_monitoring: Union[Unset, str] = UNSET
    client_type: Union[Unset, int] = UNSET
    clr_start_date: Union[Unset, datetime.date] = UNSET
    clr_total_profit_costs: Union[Unset, str] = UNSET
    cost_limit: Union[Unset, str] = UNSET
    counsel: Union[Unset, int] = UNSET
    court: Union[Unset, int] = UNSET
    court_id: Union[Unset, int] = UNSET
    court_id_code: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    delivery_location: Union[Unset, str] = UNSET
    dscc_number: Union[Unset, str] = UNSET
    duty_solicitor: Union[Unset, bool] = UNSET
    etag: Union[Unset, str] = UNSET
    exceptional_case_funding_reference: Union[Unset, str] = UNSET
    expense_limit: Union[Unset, str] = UNSET
    fee_scheme: Union[Unset, int] = UNSET
    first_conducting_solicitor: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    irc_surgery: Union[Unset, str] = UNSET
    legacy_case: Union[Unset, str] = UNSET
    legal_representation_number: Union[Unset, str] = UNSET
    lh_total_disbursements: Union[Unset, str] = UNSET
    lh_start_date: Union[Unset, str] = UNSET
    lh_total_profit_costs: Union[Unset, str] = UNSET
    linked_matter_id: Union[Unset, int] = UNSET
    local_authority_number: Union[Unset, str] = UNSET
    maat_id: Union[Unset, str] = UNSET
    matter_type: Union[Unset, int] = UNSET
    matter_type_code: Union[Unset, str] = UNSET
    matter_type_1: Union[Unset, int] = UNSET
    matter_type_1_code: Union[Unset, str] = UNSET
    matter_type_1_title: Union[Unset, str] = UNSET
    matter_type_2: Union[Unset, int] = UNSET
    matter_type_2_code: Union[Unset, str] = UNSET
    matter_type_2_title: Union[Unset, str] = UNSET
    matter_types_combined: Union[Unset, str] = UNSET
    number_of_clients_seen_at_surgery: Union[Unset, int] = UNSET
    number_of_clients: Union[Unset, int] = UNSET
    party: Union[Unset, int] = UNSET
    police_station: Union[Unset, str] = UNSET
    post_transfer_clients_represented: Union[Unset, int] = UNSET
    postal_application_accepted: Union[Unset, str] = UNSET
    prior_authority_reference: Union[Unset, str] = UNSET
    prison_id: Union[Unset, int] = UNSET
    prison_law_prior_approval_number: Union[Unset, str] = UNSET
    procurement_area: Union[Unset, str] = UNSET
    region: Union[Unset, int] = UNSET
    related_claims_number: Union[Unset, str] = UNSET
    representation_order_date: Union[Unset, datetime.date] = UNSET
    schedule_reference_number: Union[Unset, str] = UNSET
    scheme_id: Union[Unset, str] = UNSET
    session_type: Union[Unset, int] = UNSET
    solicitor_type: Union[Unset, int] = UNSET
    standard_fee_category: Union[Unset, int] = UNSET
    surgery_clients_resulting_in_a_legal_help_matter_opened: Union[Unset, int] = UNSET
    surgery_clients: Union[Unset, int] = UNSET
    surgery_date: Union[Unset, datetime.date] = UNSET
    transfer_date: Union[Unset, datetime.date] = UNSET
    type_of_advice: Union[Unset, int] = UNSET
    type_of_service: Union[Unset, str] = UNSET
    ucn: Union[Unset, str] = UNSET
    ufn: Union[Unset, str] = UNSET
    undesignated_area_court: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    user_type: Union[Unset, int] = UNSET
    youth_court: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_point = self.access_point

        laa_office_number = self.laa_office_number

        ait_hearing_centre = self.ait_hearing_centre

        attended_several_hearings_acting_for_multiple_clients = (
            self.attended_several_hearings_acting_for_multiple_clients
        )

        bill_ho_ucn = self.bill_ho_ucn

        bill_number_of_attendances = self.bill_number_of_attendances

        bill_outcome_for_the_client_code = self.bill_outcome_for_the_client_code

        bill_stage_reached_code = self.bill_stage_reached_code

        case_reference = self.case_reference

        case_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.case_start_date, Unset):
            case_start_date = self.case_start_date.isoformat()

        category = self.category

        category_as_string = self.category_as_string

        certificate_effective_date: Union[Unset, str] = UNSET
        if not isinstance(self.certificate_effective_date, Unset):
            certificate_effective_date = self.certificate_effective_date.isoformat()

        certificate_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.certificate_expiration_date, Unset):
            certificate_expiration_date = self.certificate_expiration_date.isoformat()

        certificate_number = self.certificate_number

        certificate_scope = self.certificate_scope

        certification_type = self.certification_type

        change_of_solicitor = self.change_of_solicitor

        client_equal_opportunity_monitoring = self.client_equal_opportunity_monitoring

        client_type = self.client_type

        clr_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.clr_start_date, Unset):
            clr_start_date = self.clr_start_date.isoformat()

        clr_total_profit_costs = self.clr_total_profit_costs

        cost_limit = self.cost_limit

        counsel = self.counsel

        court = self.court

        court_id = self.court_id

        court_id_code = self.court_id_code

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        delivery_location = self.delivery_location

        dscc_number = self.dscc_number

        duty_solicitor = self.duty_solicitor

        etag = self.etag

        exceptional_case_funding_reference = self.exceptional_case_funding_reference

        expense_limit = self.expense_limit

        fee_scheme = self.fee_scheme

        first_conducting_solicitor = self.first_conducting_solicitor

        id = self.id

        irc_surgery = self.irc_surgery

        legacy_case = self.legacy_case

        legal_representation_number = self.legal_representation_number

        lh_total_disbursements = self.lh_total_disbursements

        lh_start_date = self.lh_start_date

        lh_total_profit_costs = self.lh_total_profit_costs

        linked_matter_id = self.linked_matter_id

        local_authority_number = self.local_authority_number

        maat_id = self.maat_id

        matter_type = self.matter_type

        matter_type_code = self.matter_type_code

        matter_type_1 = self.matter_type_1

        matter_type_1_code = self.matter_type_1_code

        matter_type_1_title = self.matter_type_1_title

        matter_type_2 = self.matter_type_2

        matter_type_2_code = self.matter_type_2_code

        matter_type_2_title = self.matter_type_2_title

        matter_types_combined = self.matter_types_combined

        number_of_clients_seen_at_surgery = self.number_of_clients_seen_at_surgery

        number_of_clients = self.number_of_clients

        party = self.party

        police_station = self.police_station

        post_transfer_clients_represented = self.post_transfer_clients_represented

        postal_application_accepted = self.postal_application_accepted

        prior_authority_reference = self.prior_authority_reference

        prison_id = self.prison_id

        prison_law_prior_approval_number = self.prison_law_prior_approval_number

        procurement_area = self.procurement_area

        region = self.region

        related_claims_number = self.related_claims_number

        representation_order_date: Union[Unset, str] = UNSET
        if not isinstance(self.representation_order_date, Unset):
            representation_order_date = self.representation_order_date.isoformat()

        schedule_reference_number = self.schedule_reference_number

        scheme_id = self.scheme_id

        session_type = self.session_type

        solicitor_type = self.solicitor_type

        standard_fee_category = self.standard_fee_category

        surgery_clients_resulting_in_a_legal_help_matter_opened = (
            self.surgery_clients_resulting_in_a_legal_help_matter_opened
        )

        surgery_clients = self.surgery_clients

        surgery_date: Union[Unset, str] = UNSET
        if not isinstance(self.surgery_date, Unset):
            surgery_date = self.surgery_date.isoformat()

        transfer_date: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_date, Unset):
            transfer_date = self.transfer_date.isoformat()

        type_of_advice = self.type_of_advice

        type_of_service = self.type_of_service

        ucn = self.ucn

        ufn = self.ufn

        undesignated_area_court = self.undesignated_area_court

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        user_type = self.user_type

        youth_court = self.youth_court

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_point is not UNSET:
            field_dict["access_point"] = access_point
        if laa_office_number is not UNSET:
            field_dict["laa_office_number"] = laa_office_number
        if ait_hearing_centre is not UNSET:
            field_dict["ait_hearing_centre"] = ait_hearing_centre
        if attended_several_hearings_acting_for_multiple_clients is not UNSET:
            field_dict["attended_several_hearings_acting_for_multiple_clients"] = (
                attended_several_hearings_acting_for_multiple_clients
            )
        if bill_ho_ucn is not UNSET:
            field_dict["bill_ho_ucn"] = bill_ho_ucn
        if bill_number_of_attendances is not UNSET:
            field_dict["bill_number_of_attendances"] = bill_number_of_attendances
        if bill_outcome_for_the_client_code is not UNSET:
            field_dict["bill_outcome_for_the_client_code"] = bill_outcome_for_the_client_code
        if bill_stage_reached_code is not UNSET:
            field_dict["bill_stage_reached_code"] = bill_stage_reached_code
        if case_reference is not UNSET:
            field_dict["case_reference"] = case_reference
        if case_start_date is not UNSET:
            field_dict["case_start_date"] = case_start_date
        if category is not UNSET:
            field_dict["category"] = category
        if category_as_string is not UNSET:
            field_dict["category_as_string"] = category_as_string
        if certificate_effective_date is not UNSET:
            field_dict["certificate_effective_date"] = certificate_effective_date
        if certificate_expiration_date is not UNSET:
            field_dict["certificate_expiration_date"] = certificate_expiration_date
        if certificate_number is not UNSET:
            field_dict["certificate_number"] = certificate_number
        if certificate_scope is not UNSET:
            field_dict["certificate_scope"] = certificate_scope
        if certification_type is not UNSET:
            field_dict["certification_type"] = certification_type
        if change_of_solicitor is not UNSET:
            field_dict["change_of_solicitor"] = change_of_solicitor
        if client_equal_opportunity_monitoring is not UNSET:
            field_dict["client_equal_opportunity_monitoring"] = client_equal_opportunity_monitoring
        if client_type is not UNSET:
            field_dict["client_type"] = client_type
        if clr_start_date is not UNSET:
            field_dict["clr_start_date"] = clr_start_date
        if clr_total_profit_costs is not UNSET:
            field_dict["clr_total_profit_costs"] = clr_total_profit_costs
        if cost_limit is not UNSET:
            field_dict["cost_limit"] = cost_limit
        if counsel is not UNSET:
            field_dict["counsel"] = counsel
        if court is not UNSET:
            field_dict["court"] = court
        if court_id is not UNSET:
            field_dict["court_id"] = court_id
        if court_id_code is not UNSET:
            field_dict["court_id_code"] = court_id_code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if delivery_location is not UNSET:
            field_dict["delivery_location"] = delivery_location
        if dscc_number is not UNSET:
            field_dict["dscc_number"] = dscc_number
        if duty_solicitor is not UNSET:
            field_dict["duty_solicitor"] = duty_solicitor
        if etag is not UNSET:
            field_dict["etag"] = etag
        if exceptional_case_funding_reference is not UNSET:
            field_dict["exceptional_case_funding_reference"] = exceptional_case_funding_reference
        if expense_limit is not UNSET:
            field_dict["expense_limit"] = expense_limit
        if fee_scheme is not UNSET:
            field_dict["fee_scheme"] = fee_scheme
        if first_conducting_solicitor is not UNSET:
            field_dict["first_conducting_solicitor"] = first_conducting_solicitor
        if id is not UNSET:
            field_dict["id"] = id
        if irc_surgery is not UNSET:
            field_dict["irc_surgery"] = irc_surgery
        if legacy_case is not UNSET:
            field_dict["legacy_case"] = legacy_case
        if legal_representation_number is not UNSET:
            field_dict["legal_representation_number"] = legal_representation_number
        if lh_total_disbursements is not UNSET:
            field_dict["lh_total_disbursements"] = lh_total_disbursements
        if lh_start_date is not UNSET:
            field_dict["lh_start_date"] = lh_start_date
        if lh_total_profit_costs is not UNSET:
            field_dict["lh_total_profit_costs"] = lh_total_profit_costs
        if linked_matter_id is not UNSET:
            field_dict["linked_matter_id"] = linked_matter_id
        if local_authority_number is not UNSET:
            field_dict["local_authority_number"] = local_authority_number
        if maat_id is not UNSET:
            field_dict["maat_id"] = maat_id
        if matter_type is not UNSET:
            field_dict["matter_type"] = matter_type
        if matter_type_code is not UNSET:
            field_dict["matter_type_code"] = matter_type_code
        if matter_type_1 is not UNSET:
            field_dict["matter_type_1"] = matter_type_1
        if matter_type_1_code is not UNSET:
            field_dict["matter_type_1_code"] = matter_type_1_code
        if matter_type_1_title is not UNSET:
            field_dict["matter_type_1_title"] = matter_type_1_title
        if matter_type_2 is not UNSET:
            field_dict["matter_type_2"] = matter_type_2
        if matter_type_2_code is not UNSET:
            field_dict["matter_type_2_code"] = matter_type_2_code
        if matter_type_2_title is not UNSET:
            field_dict["matter_type_2_title"] = matter_type_2_title
        if matter_types_combined is not UNSET:
            field_dict["matter_types_combined"] = matter_types_combined
        if number_of_clients_seen_at_surgery is not UNSET:
            field_dict["number_of_clients_seen_at_surgery"] = number_of_clients_seen_at_surgery
        if number_of_clients is not UNSET:
            field_dict["number_of_clients"] = number_of_clients
        if party is not UNSET:
            field_dict["party"] = party
        if police_station is not UNSET:
            field_dict["police_station"] = police_station
        if post_transfer_clients_represented is not UNSET:
            field_dict["post_transfer_clients_represented"] = post_transfer_clients_represented
        if postal_application_accepted is not UNSET:
            field_dict["postal_application_accepted"] = postal_application_accepted
        if prior_authority_reference is not UNSET:
            field_dict["prior_authority_reference"] = prior_authority_reference
        if prison_id is not UNSET:
            field_dict["prison_id"] = prison_id
        if prison_law_prior_approval_number is not UNSET:
            field_dict["prison_law_prior_approval_number"] = prison_law_prior_approval_number
        if procurement_area is not UNSET:
            field_dict["procurement_area"] = procurement_area
        if region is not UNSET:
            field_dict["region"] = region
        if related_claims_number is not UNSET:
            field_dict["related_claims_number"] = related_claims_number
        if representation_order_date is not UNSET:
            field_dict["representation_order_date"] = representation_order_date
        if schedule_reference_number is not UNSET:
            field_dict["schedule_reference_number"] = schedule_reference_number
        if scheme_id is not UNSET:
            field_dict["scheme_id"] = scheme_id
        if session_type is not UNSET:
            field_dict["session_type"] = session_type
        if solicitor_type is not UNSET:
            field_dict["solicitor_type"] = solicitor_type
        if standard_fee_category is not UNSET:
            field_dict["standard_fee_category"] = standard_fee_category
        if surgery_clients_resulting_in_a_legal_help_matter_opened is not UNSET:
            field_dict["surgery_clients_resulting_in_a_legal_help_matter_opened"] = (
                surgery_clients_resulting_in_a_legal_help_matter_opened
            )
        if surgery_clients is not UNSET:
            field_dict["surgery_clients"] = surgery_clients
        if surgery_date is not UNSET:
            field_dict["surgery_date"] = surgery_date
        if transfer_date is not UNSET:
            field_dict["transfer_date"] = transfer_date
        if type_of_advice is not UNSET:
            field_dict["type_of_advice"] = type_of_advice
        if type_of_service is not UNSET:
            field_dict["type_of_service"] = type_of_service
        if ucn is not UNSET:
            field_dict["ucn"] = ucn
        if ufn is not UNSET:
            field_dict["ufn"] = ufn
        if undesignated_area_court is not UNSET:
            field_dict["undesignated_area_court"] = undesignated_area_court
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_type is not UNSET:
            field_dict["user_type"] = user_type
        if youth_court is not UNSET:
            field_dict["youth_court"] = youth_court

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_point = d.pop("access_point", UNSET)

        laa_office_number = d.pop("laa_office_number", UNSET)

        ait_hearing_centre = d.pop("ait_hearing_centre", UNSET)

        attended_several_hearings_acting_for_multiple_clients = d.pop(
            "attended_several_hearings_acting_for_multiple_clients", UNSET
        )

        bill_ho_ucn = d.pop("bill_ho_ucn", UNSET)

        bill_number_of_attendances = d.pop("bill_number_of_attendances", UNSET)

        bill_outcome_for_the_client_code = d.pop("bill_outcome_for_the_client_code", UNSET)

        bill_stage_reached_code = d.pop("bill_stage_reached_code", UNSET)

        case_reference = d.pop("case_reference", UNSET)

        _case_start_date = d.pop("case_start_date", UNSET)
        case_start_date: Union[Unset, datetime.date]
        if isinstance(_case_start_date, Unset):
            case_start_date = UNSET
        else:
            case_start_date = isoparse(_case_start_date).date()

        category = d.pop("category", UNSET)

        category_as_string = d.pop("category_as_string", UNSET)

        _certificate_effective_date = d.pop("certificate_effective_date", UNSET)
        certificate_effective_date: Union[Unset, datetime.date]
        if isinstance(_certificate_effective_date, Unset):
            certificate_effective_date = UNSET
        else:
            certificate_effective_date = isoparse(_certificate_effective_date).date()

        _certificate_expiration_date = d.pop("certificate_expiration_date", UNSET)
        certificate_expiration_date: Union[Unset, datetime.date]
        if isinstance(_certificate_expiration_date, Unset):
            certificate_expiration_date = UNSET
        else:
            certificate_expiration_date = isoparse(_certificate_expiration_date).date()

        certificate_number = d.pop("certificate_number", UNSET)

        certificate_scope = d.pop("certificate_scope", UNSET)

        certification_type = d.pop("certification_type", UNSET)

        change_of_solicitor = d.pop("change_of_solicitor", UNSET)

        client_equal_opportunity_monitoring = d.pop("client_equal_opportunity_monitoring", UNSET)

        client_type = d.pop("client_type", UNSET)

        _clr_start_date = d.pop("clr_start_date", UNSET)
        clr_start_date: Union[Unset, datetime.date]
        if isinstance(_clr_start_date, Unset):
            clr_start_date = UNSET
        else:
            clr_start_date = isoparse(_clr_start_date).date()

        clr_total_profit_costs = d.pop("clr_total_profit_costs", UNSET)

        cost_limit = d.pop("cost_limit", UNSET)

        counsel = d.pop("counsel", UNSET)

        court = d.pop("court", UNSET)

        court_id = d.pop("court_id", UNSET)

        court_id_code = d.pop("court_id_code", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        delivery_location = d.pop("delivery_location", UNSET)

        dscc_number = d.pop("dscc_number", UNSET)

        duty_solicitor = d.pop("duty_solicitor", UNSET)

        etag = d.pop("etag", UNSET)

        exceptional_case_funding_reference = d.pop("exceptional_case_funding_reference", UNSET)

        expense_limit = d.pop("expense_limit", UNSET)

        fee_scheme = d.pop("fee_scheme", UNSET)

        first_conducting_solicitor = d.pop("first_conducting_solicitor", UNSET)

        id = d.pop("id", UNSET)

        irc_surgery = d.pop("irc_surgery", UNSET)

        legacy_case = d.pop("legacy_case", UNSET)

        legal_representation_number = d.pop("legal_representation_number", UNSET)

        lh_total_disbursements = d.pop("lh_total_disbursements", UNSET)

        lh_start_date = d.pop("lh_start_date", UNSET)

        lh_total_profit_costs = d.pop("lh_total_profit_costs", UNSET)

        linked_matter_id = d.pop("linked_matter_id", UNSET)

        local_authority_number = d.pop("local_authority_number", UNSET)

        maat_id = d.pop("maat_id", UNSET)

        matter_type = d.pop("matter_type", UNSET)

        matter_type_code = d.pop("matter_type_code", UNSET)

        matter_type_1 = d.pop("matter_type_1", UNSET)

        matter_type_1_code = d.pop("matter_type_1_code", UNSET)

        matter_type_1_title = d.pop("matter_type_1_title", UNSET)

        matter_type_2 = d.pop("matter_type_2", UNSET)

        matter_type_2_code = d.pop("matter_type_2_code", UNSET)

        matter_type_2_title = d.pop("matter_type_2_title", UNSET)

        matter_types_combined = d.pop("matter_types_combined", UNSET)

        number_of_clients_seen_at_surgery = d.pop("number_of_clients_seen_at_surgery", UNSET)

        number_of_clients = d.pop("number_of_clients", UNSET)

        party = d.pop("party", UNSET)

        police_station = d.pop("police_station", UNSET)

        post_transfer_clients_represented = d.pop("post_transfer_clients_represented", UNSET)

        postal_application_accepted = d.pop("postal_application_accepted", UNSET)

        prior_authority_reference = d.pop("prior_authority_reference", UNSET)

        prison_id = d.pop("prison_id", UNSET)

        prison_law_prior_approval_number = d.pop("prison_law_prior_approval_number", UNSET)

        procurement_area = d.pop("procurement_area", UNSET)

        region = d.pop("region", UNSET)

        related_claims_number = d.pop("related_claims_number", UNSET)

        _representation_order_date = d.pop("representation_order_date", UNSET)
        representation_order_date: Union[Unset, datetime.date]
        if isinstance(_representation_order_date, Unset):
            representation_order_date = UNSET
        else:
            representation_order_date = isoparse(_representation_order_date).date()

        schedule_reference_number = d.pop("schedule_reference_number", UNSET)

        scheme_id = d.pop("scheme_id", UNSET)

        session_type = d.pop("session_type", UNSET)

        solicitor_type = d.pop("solicitor_type", UNSET)

        standard_fee_category = d.pop("standard_fee_category", UNSET)

        surgery_clients_resulting_in_a_legal_help_matter_opened = d.pop(
            "surgery_clients_resulting_in_a_legal_help_matter_opened", UNSET
        )

        surgery_clients = d.pop("surgery_clients", UNSET)

        _surgery_date = d.pop("surgery_date", UNSET)
        surgery_date: Union[Unset, datetime.date]
        if isinstance(_surgery_date, Unset):
            surgery_date = UNSET
        else:
            surgery_date = isoparse(_surgery_date).date()

        _transfer_date = d.pop("transfer_date", UNSET)
        transfer_date: Union[Unset, datetime.date]
        if isinstance(_transfer_date, Unset):
            transfer_date = UNSET
        else:
            transfer_date = isoparse(_transfer_date).date()

        type_of_advice = d.pop("type_of_advice", UNSET)

        type_of_service = d.pop("type_of_service", UNSET)

        ucn = d.pop("ucn", UNSET)

        ufn = d.pop("ufn", UNSET)

        undesignated_area_court = d.pop("undesignated_area_court", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        user_type = d.pop("user_type", UNSET)

        youth_court = d.pop("youth_court", UNSET)

        legal_aid_uk_matter_base = cls(
            access_point=access_point,
            laa_office_number=laa_office_number,
            ait_hearing_centre=ait_hearing_centre,
            attended_several_hearings_acting_for_multiple_clients=attended_several_hearings_acting_for_multiple_clients,
            bill_ho_ucn=bill_ho_ucn,
            bill_number_of_attendances=bill_number_of_attendances,
            bill_outcome_for_the_client_code=bill_outcome_for_the_client_code,
            bill_stage_reached_code=bill_stage_reached_code,
            case_reference=case_reference,
            case_start_date=case_start_date,
            category=category,
            category_as_string=category_as_string,
            certificate_effective_date=certificate_effective_date,
            certificate_expiration_date=certificate_expiration_date,
            certificate_number=certificate_number,
            certificate_scope=certificate_scope,
            certification_type=certification_type,
            change_of_solicitor=change_of_solicitor,
            client_equal_opportunity_monitoring=client_equal_opportunity_monitoring,
            client_type=client_type,
            clr_start_date=clr_start_date,
            clr_total_profit_costs=clr_total_profit_costs,
            cost_limit=cost_limit,
            counsel=counsel,
            court=court,
            court_id=court_id,
            court_id_code=court_id_code,
            created_at=created_at,
            delivery_location=delivery_location,
            dscc_number=dscc_number,
            duty_solicitor=duty_solicitor,
            etag=etag,
            exceptional_case_funding_reference=exceptional_case_funding_reference,
            expense_limit=expense_limit,
            fee_scheme=fee_scheme,
            first_conducting_solicitor=first_conducting_solicitor,
            id=id,
            irc_surgery=irc_surgery,
            legacy_case=legacy_case,
            legal_representation_number=legal_representation_number,
            lh_total_disbursements=lh_total_disbursements,
            lh_start_date=lh_start_date,
            lh_total_profit_costs=lh_total_profit_costs,
            linked_matter_id=linked_matter_id,
            local_authority_number=local_authority_number,
            maat_id=maat_id,
            matter_type=matter_type,
            matter_type_code=matter_type_code,
            matter_type_1=matter_type_1,
            matter_type_1_code=matter_type_1_code,
            matter_type_1_title=matter_type_1_title,
            matter_type_2=matter_type_2,
            matter_type_2_code=matter_type_2_code,
            matter_type_2_title=matter_type_2_title,
            matter_types_combined=matter_types_combined,
            number_of_clients_seen_at_surgery=number_of_clients_seen_at_surgery,
            number_of_clients=number_of_clients,
            party=party,
            police_station=police_station,
            post_transfer_clients_represented=post_transfer_clients_represented,
            postal_application_accepted=postal_application_accepted,
            prior_authority_reference=prior_authority_reference,
            prison_id=prison_id,
            prison_law_prior_approval_number=prison_law_prior_approval_number,
            procurement_area=procurement_area,
            region=region,
            related_claims_number=related_claims_number,
            representation_order_date=representation_order_date,
            schedule_reference_number=schedule_reference_number,
            scheme_id=scheme_id,
            session_type=session_type,
            solicitor_type=solicitor_type,
            standard_fee_category=standard_fee_category,
            surgery_clients_resulting_in_a_legal_help_matter_opened=surgery_clients_resulting_in_a_legal_help_matter_opened,
            surgery_clients=surgery_clients,
            surgery_date=surgery_date,
            transfer_date=transfer_date,
            type_of_advice=type_of_advice,
            type_of_service=type_of_service,
            ucn=ucn,
            ufn=ufn,
            undesignated_area_court=undesignated_area_court,
            updated_at=updated_at,
            user_type=user_type,
            youth_court=youth_court,
        )

        legal_aid_uk_matter_base.additional_properties = d
        return legal_aid_uk_matter_base

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
