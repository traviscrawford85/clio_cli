import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LegalAidUkBillBase")


@_attrs_define
class LegalAidUkBillBase:
    """
    Attributes:
        additional_travel_payment (Union[Unset, bool]): Additional travel payment, for Legal Aid England and Wales
        adjourned_hearing_fee (Union[Unset, str]): Adjourned hearing fee
        advocacy_costs (Union[Unset, float]): Advocacy costs
        advice_time (Union[Unset, int]): Advice time
        bill_type (Union[Unset, int]): Bill type
        case_concluded (Union[Unset, datetime.date]): Case concluded
        case_stage_level (Union[Unset, int]): Case stage level
        cla_exemption_code (Union[Unset, str]): CLA exemption code
        cla_reference (Union[Unset, str]): CLA reference
        cmrh_oral (Union[Unset, int]): CMRH oral
        cmrh_telephone (Union[Unset, int]): CMRH telephone
        cost_of_counsel (Union[Unset, str]): Cost of counsel
        costs_are_those_of (Union[Unset, int]): Costs are those of
        court_location (Union[Unset, str]): Court location (HPCDS matters)
        date_of_claim (Union[Unset, datetime.date]): Date of claim
        designated_accredited_representative (Union[Unset, int]): Designated accredited representative
        detention_travel_and_waiting_costs (Union[Unset, str]): Detention travel & waiting costs ex VAT
        disbursements_vat (Union[Unset, float]): Disbursements VAT
        exceptional_case_funding_reference (Union[Unset, str]): Exceptional case funding reference
        exemption_criteria_satisfied (Union[Unset, int]): Exemption criteria satisfied
        follow_on_work (Union[Unset, int]): Follow on work
        ho_interview (Union[Unset, int]): HO interview
        ho_ucn (Union[Unset, int]): HO UCN
        id (Union[Unset, int]): Unique identifier for the *LegalAidUkBill*
        independent_medical_reports_claimed (Union[Unset, str]): Independent medical reports claimed
        jr_form_filling (Union[Unset, str]): JR/Form filling ex VAT, for Legal Aid England and Wales
        maat_id (Union[Unset, str]): MAAT ID
        meetings_attended (Union[Unset, int]): Meetings attended
        mht_ref_no (Union[Unset, str]): MHT reference number
        net_disbursements (Union[Unset, float]): Net disbursements
        net_profit_costs (Union[Unset, float]): Net profit cost
        niat_disbursement_prior_authority_number (Union[Unset, str]): NIAT disbursement prior authority number
        number_of_attendances (Union[Unset, int]): Number of attendances
        outcome_for_the_client (Union[Unset, int]): Outcome for the client
        profit_costs_ex_vat (Union[Unset, int]): Profit costs ex VAT
        prior_authority_reference (Union[Unset, str]): Prior authority reference number
        representation_order_date (Union[Unset, datetime.date]): Representation order date
        stage_reached (Union[Unset, int]): Stage reached
        substantive_hearing (Union[Unset, int]): Substantive hearing
        travel_and_waiting_costs (Union[Unset, float]): Travel & waiting costs
        travel_time (Union[Unset, int]): Travel time
        value_of_costs (Union[Unset, str]): Value of costs
        waiting_time (Union[Unset, int]): Waiting time
    """

    additional_travel_payment: Union[Unset, bool] = UNSET
    adjourned_hearing_fee: Union[Unset, str] = UNSET
    advocacy_costs: Union[Unset, float] = UNSET
    advice_time: Union[Unset, int] = UNSET
    bill_type: Union[Unset, int] = UNSET
    case_concluded: Union[Unset, datetime.date] = UNSET
    case_stage_level: Union[Unset, int] = UNSET
    cla_exemption_code: Union[Unset, str] = UNSET
    cla_reference: Union[Unset, str] = UNSET
    cmrh_oral: Union[Unset, int] = UNSET
    cmrh_telephone: Union[Unset, int] = UNSET
    cost_of_counsel: Union[Unset, str] = UNSET
    costs_are_those_of: Union[Unset, int] = UNSET
    court_location: Union[Unset, str] = UNSET
    date_of_claim: Union[Unset, datetime.date] = UNSET
    designated_accredited_representative: Union[Unset, int] = UNSET
    detention_travel_and_waiting_costs: Union[Unset, str] = UNSET
    disbursements_vat: Union[Unset, float] = UNSET
    exceptional_case_funding_reference: Union[Unset, str] = UNSET
    exemption_criteria_satisfied: Union[Unset, int] = UNSET
    follow_on_work: Union[Unset, int] = UNSET
    ho_interview: Union[Unset, int] = UNSET
    ho_ucn: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    independent_medical_reports_claimed: Union[Unset, str] = UNSET
    jr_form_filling: Union[Unset, str] = UNSET
    maat_id: Union[Unset, str] = UNSET
    meetings_attended: Union[Unset, int] = UNSET
    mht_ref_no: Union[Unset, str] = UNSET
    net_disbursements: Union[Unset, float] = UNSET
    net_profit_costs: Union[Unset, float] = UNSET
    niat_disbursement_prior_authority_number: Union[Unset, str] = UNSET
    number_of_attendances: Union[Unset, int] = UNSET
    outcome_for_the_client: Union[Unset, int] = UNSET
    profit_costs_ex_vat: Union[Unset, int] = UNSET
    prior_authority_reference: Union[Unset, str] = UNSET
    representation_order_date: Union[Unset, datetime.date] = UNSET
    stage_reached: Union[Unset, int] = UNSET
    substantive_hearing: Union[Unset, int] = UNSET
    travel_and_waiting_costs: Union[Unset, float] = UNSET
    travel_time: Union[Unset, int] = UNSET
    value_of_costs: Union[Unset, str] = UNSET
    waiting_time: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        additional_travel_payment = self.additional_travel_payment

        adjourned_hearing_fee = self.adjourned_hearing_fee

        advocacy_costs = self.advocacy_costs

        advice_time = self.advice_time

        bill_type = self.bill_type

        case_concluded: Union[Unset, str] = UNSET
        if not isinstance(self.case_concluded, Unset):
            case_concluded = self.case_concluded.isoformat()

        case_stage_level = self.case_stage_level

        cla_exemption_code = self.cla_exemption_code

        cla_reference = self.cla_reference

        cmrh_oral = self.cmrh_oral

        cmrh_telephone = self.cmrh_telephone

        cost_of_counsel = self.cost_of_counsel

        costs_are_those_of = self.costs_are_those_of

        court_location = self.court_location

        date_of_claim: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_claim, Unset):
            date_of_claim = self.date_of_claim.isoformat()

        designated_accredited_representative = self.designated_accredited_representative

        detention_travel_and_waiting_costs = self.detention_travel_and_waiting_costs

        disbursements_vat = self.disbursements_vat

        exceptional_case_funding_reference = self.exceptional_case_funding_reference

        exemption_criteria_satisfied = self.exemption_criteria_satisfied

        follow_on_work = self.follow_on_work

        ho_interview = self.ho_interview

        ho_ucn = self.ho_ucn

        id = self.id

        independent_medical_reports_claimed = self.independent_medical_reports_claimed

        jr_form_filling = self.jr_form_filling

        maat_id = self.maat_id

        meetings_attended = self.meetings_attended

        mht_ref_no = self.mht_ref_no

        net_disbursements = self.net_disbursements

        net_profit_costs = self.net_profit_costs

        niat_disbursement_prior_authority_number = self.niat_disbursement_prior_authority_number

        number_of_attendances = self.number_of_attendances

        outcome_for_the_client = self.outcome_for_the_client

        profit_costs_ex_vat = self.profit_costs_ex_vat

        prior_authority_reference = self.prior_authority_reference

        representation_order_date: Union[Unset, str] = UNSET
        if not isinstance(self.representation_order_date, Unset):
            representation_order_date = self.representation_order_date.isoformat()

        stage_reached = self.stage_reached

        substantive_hearing = self.substantive_hearing

        travel_and_waiting_costs = self.travel_and_waiting_costs

        travel_time = self.travel_time

        value_of_costs = self.value_of_costs

        waiting_time = self.waiting_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if additional_travel_payment is not UNSET:
            field_dict["additional_travel_payment"] = additional_travel_payment
        if adjourned_hearing_fee is not UNSET:
            field_dict["adjourned_hearing_fee"] = adjourned_hearing_fee
        if advocacy_costs is not UNSET:
            field_dict["advocacy_costs"] = advocacy_costs
        if advice_time is not UNSET:
            field_dict["advice_time"] = advice_time
        if bill_type is not UNSET:
            field_dict["bill_type"] = bill_type
        if case_concluded is not UNSET:
            field_dict["case_concluded"] = case_concluded
        if case_stage_level is not UNSET:
            field_dict["case_stage_level"] = case_stage_level
        if cla_exemption_code is not UNSET:
            field_dict["cla_exemption_code"] = cla_exemption_code
        if cla_reference is not UNSET:
            field_dict["cla_reference"] = cla_reference
        if cmrh_oral is not UNSET:
            field_dict["cmrh_oral"] = cmrh_oral
        if cmrh_telephone is not UNSET:
            field_dict["cmrh_telephone"] = cmrh_telephone
        if cost_of_counsel is not UNSET:
            field_dict["cost_of_counsel"] = cost_of_counsel
        if costs_are_those_of is not UNSET:
            field_dict["costs_are_those_of"] = costs_are_those_of
        if court_location is not UNSET:
            field_dict["court_location"] = court_location
        if date_of_claim is not UNSET:
            field_dict["date_of_claim"] = date_of_claim
        if designated_accredited_representative is not UNSET:
            field_dict["designated_accredited_representative"] = designated_accredited_representative
        if detention_travel_and_waiting_costs is not UNSET:
            field_dict["detention_travel_and_waiting_costs"] = detention_travel_and_waiting_costs
        if disbursements_vat is not UNSET:
            field_dict["disbursements_vat"] = disbursements_vat
        if exceptional_case_funding_reference is not UNSET:
            field_dict["exceptional_case_funding_reference"] = exceptional_case_funding_reference
        if exemption_criteria_satisfied is not UNSET:
            field_dict["exemption_criteria_satisfied"] = exemption_criteria_satisfied
        if follow_on_work is not UNSET:
            field_dict["follow_on_work"] = follow_on_work
        if ho_interview is not UNSET:
            field_dict["ho_interview"] = ho_interview
        if ho_ucn is not UNSET:
            field_dict["ho_ucn"] = ho_ucn
        if id is not UNSET:
            field_dict["id"] = id
        if independent_medical_reports_claimed is not UNSET:
            field_dict["independent_medical_reports_claimed"] = independent_medical_reports_claimed
        if jr_form_filling is not UNSET:
            field_dict["jr_form_filling"] = jr_form_filling
        if maat_id is not UNSET:
            field_dict["maat_id"] = maat_id
        if meetings_attended is not UNSET:
            field_dict["meetings_attended"] = meetings_attended
        if mht_ref_no is not UNSET:
            field_dict["mht_ref_no"] = mht_ref_no
        if net_disbursements is not UNSET:
            field_dict["net_disbursements"] = net_disbursements
        if net_profit_costs is not UNSET:
            field_dict["net_profit_costs"] = net_profit_costs
        if niat_disbursement_prior_authority_number is not UNSET:
            field_dict["niat_disbursement_prior_authority_number"] = niat_disbursement_prior_authority_number
        if number_of_attendances is not UNSET:
            field_dict["number_of_attendances"] = number_of_attendances
        if outcome_for_the_client is not UNSET:
            field_dict["outcome_for_the_client"] = outcome_for_the_client
        if profit_costs_ex_vat is not UNSET:
            field_dict["profit_costs_ex_vat"] = profit_costs_ex_vat
        if prior_authority_reference is not UNSET:
            field_dict["prior_authority_reference"] = prior_authority_reference
        if representation_order_date is not UNSET:
            field_dict["representation_order_date"] = representation_order_date
        if stage_reached is not UNSET:
            field_dict["stage_reached"] = stage_reached
        if substantive_hearing is not UNSET:
            field_dict["substantive_hearing"] = substantive_hearing
        if travel_and_waiting_costs is not UNSET:
            field_dict["travel_and_waiting_costs"] = travel_and_waiting_costs
        if travel_time is not UNSET:
            field_dict["travel_time"] = travel_time
        if value_of_costs is not UNSET:
            field_dict["value_of_costs"] = value_of_costs
        if waiting_time is not UNSET:
            field_dict["waiting_time"] = waiting_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        additional_travel_payment = d.pop("additional_travel_payment", UNSET)

        adjourned_hearing_fee = d.pop("adjourned_hearing_fee", UNSET)

        advocacy_costs = d.pop("advocacy_costs", UNSET)

        advice_time = d.pop("advice_time", UNSET)

        bill_type = d.pop("bill_type", UNSET)

        _case_concluded = d.pop("case_concluded", UNSET)
        case_concluded: Union[Unset, datetime.date]
        if isinstance(_case_concluded, Unset):
            case_concluded = UNSET
        else:
            case_concluded = isoparse(_case_concluded).date()

        case_stage_level = d.pop("case_stage_level", UNSET)

        cla_exemption_code = d.pop("cla_exemption_code", UNSET)

        cla_reference = d.pop("cla_reference", UNSET)

        cmrh_oral = d.pop("cmrh_oral", UNSET)

        cmrh_telephone = d.pop("cmrh_telephone", UNSET)

        cost_of_counsel = d.pop("cost_of_counsel", UNSET)

        costs_are_those_of = d.pop("costs_are_those_of", UNSET)

        court_location = d.pop("court_location", UNSET)

        _date_of_claim = d.pop("date_of_claim", UNSET)
        date_of_claim: Union[Unset, datetime.date]
        if isinstance(_date_of_claim, Unset):
            date_of_claim = UNSET
        else:
            date_of_claim = isoparse(_date_of_claim).date()

        designated_accredited_representative = d.pop("designated_accredited_representative", UNSET)

        detention_travel_and_waiting_costs = d.pop("detention_travel_and_waiting_costs", UNSET)

        disbursements_vat = d.pop("disbursements_vat", UNSET)

        exceptional_case_funding_reference = d.pop("exceptional_case_funding_reference", UNSET)

        exemption_criteria_satisfied = d.pop("exemption_criteria_satisfied", UNSET)

        follow_on_work = d.pop("follow_on_work", UNSET)

        ho_interview = d.pop("ho_interview", UNSET)

        ho_ucn = d.pop("ho_ucn", UNSET)

        id = d.pop("id", UNSET)

        independent_medical_reports_claimed = d.pop("independent_medical_reports_claimed", UNSET)

        jr_form_filling = d.pop("jr_form_filling", UNSET)

        maat_id = d.pop("maat_id", UNSET)

        meetings_attended = d.pop("meetings_attended", UNSET)

        mht_ref_no = d.pop("mht_ref_no", UNSET)

        net_disbursements = d.pop("net_disbursements", UNSET)

        net_profit_costs = d.pop("net_profit_costs", UNSET)

        niat_disbursement_prior_authority_number = d.pop("niat_disbursement_prior_authority_number", UNSET)

        number_of_attendances = d.pop("number_of_attendances", UNSET)

        outcome_for_the_client = d.pop("outcome_for_the_client", UNSET)

        profit_costs_ex_vat = d.pop("profit_costs_ex_vat", UNSET)

        prior_authority_reference = d.pop("prior_authority_reference", UNSET)

        _representation_order_date = d.pop("representation_order_date", UNSET)
        representation_order_date: Union[Unset, datetime.date]
        if isinstance(_representation_order_date, Unset):
            representation_order_date = UNSET
        else:
            representation_order_date = isoparse(_representation_order_date).date()

        stage_reached = d.pop("stage_reached", UNSET)

        substantive_hearing = d.pop("substantive_hearing", UNSET)

        travel_and_waiting_costs = d.pop("travel_and_waiting_costs", UNSET)

        travel_time = d.pop("travel_time", UNSET)

        value_of_costs = d.pop("value_of_costs", UNSET)

        waiting_time = d.pop("waiting_time", UNSET)

        legal_aid_uk_bill_base = cls(
            additional_travel_payment=additional_travel_payment,
            adjourned_hearing_fee=adjourned_hearing_fee,
            advocacy_costs=advocacy_costs,
            advice_time=advice_time,
            bill_type=bill_type,
            case_concluded=case_concluded,
            case_stage_level=case_stage_level,
            cla_exemption_code=cla_exemption_code,
            cla_reference=cla_reference,
            cmrh_oral=cmrh_oral,
            cmrh_telephone=cmrh_telephone,
            cost_of_counsel=cost_of_counsel,
            costs_are_those_of=costs_are_those_of,
            court_location=court_location,
            date_of_claim=date_of_claim,
            designated_accredited_representative=designated_accredited_representative,
            detention_travel_and_waiting_costs=detention_travel_and_waiting_costs,
            disbursements_vat=disbursements_vat,
            exceptional_case_funding_reference=exceptional_case_funding_reference,
            exemption_criteria_satisfied=exemption_criteria_satisfied,
            follow_on_work=follow_on_work,
            ho_interview=ho_interview,
            ho_ucn=ho_ucn,
            id=id,
            independent_medical_reports_claimed=independent_medical_reports_claimed,
            jr_form_filling=jr_form_filling,
            maat_id=maat_id,
            meetings_attended=meetings_attended,
            mht_ref_no=mht_ref_no,
            net_disbursements=net_disbursements,
            net_profit_costs=net_profit_costs,
            niat_disbursement_prior_authority_number=niat_disbursement_prior_authority_number,
            number_of_attendances=number_of_attendances,
            outcome_for_the_client=outcome_for_the_client,
            profit_costs_ex_vat=profit_costs_ex_vat,
            prior_authority_reference=prior_authority_reference,
            representation_order_date=representation_order_date,
            stage_reached=stage_reached,
            substantive_hearing=substantive_hearing,
            travel_and_waiting_costs=travel_and_waiting_costs,
            travel_time=travel_time,
            value_of_costs=value_of_costs,
            waiting_time=waiting_time,
        )

        legal_aid_uk_bill_base.additional_properties = d
        return legal_aid_uk_bill_base

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
