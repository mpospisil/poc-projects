# coding: utf-8

"""
    Connection Rest API 1.2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_weld_ci_basic_types import CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes
from connection_restapi_client_poc.models.idea_rs_connections_data_weld_type_code_ci_basic_types import IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_weld_check_method_hkci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldCheckMethodHKCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_weld_position_snipci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldPositionSNIPCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_welding_type_snipci_basic_types import IdeaStatiCaConnectionBasicTypesDataWeldingTypeSNIPCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    joined_item_name: Optional[StrictStr] = Field(default=None, alias="joinedItemName")
    designed_thickness: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="designedThickness")
    thickness: Optional[Union[StrictFloat, StrictInt]] = None
    leg_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="legSize")
    max_equivalent_stress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxEquivalentStress")
    equivalent_stress_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="equivalentStressResistance")
    sigma_perpendicular: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sigmaPerpendicular")
    sigma_perpendicular_max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sigmaPerpendicularMax")
    sigma_perpendicular_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sigmaPerpendicularResistance")
    unity_check_stress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckStress")
    unity_check_weld: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckWeld")
    unity_check_base_metal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckBaseMetal")
    material_name: Optional[StrictStr] = Field(default=None, alias="materialName")
    weld_type2: Optional[IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes] = Field(default=None, alias="weldType2")
    weld_with_contact: Optional[StrictBool] = Field(default=None, alias="weldWithContact")
    items: Optional[List[StrictInt]] = None
    struct_items: Optional[List[StrictInt]] = Field(default=None, alias="structItems")
    tauy: Optional[Union[StrictFloat, StrictInt]] = None
    taux: Optional[Union[StrictFloat, StrictInt]] = None
    tauxwf: Optional[Union[StrictFloat, StrictInt]] = None
    sigmawf: Optional[Union[StrictFloat, StrictInt]] = None
    weld_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldArea")
    length: Optional[Union[StrictFloat, StrictInt]] = None
    length_elem: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="lengthElem")
    forces_all_items: Optional[Dict[str, Dict[str, List[Union[StrictFloat, StrictInt]]]]] = Field(default=None, alias="forcesAllItems")
    weld_stress_diagram: Optional[List[List[Union[StrictFloat, StrictInt]]]] = Field(default=None, alias="weldStressDiagram")
    gamma_m0: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM0")
    gamma_m2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM2")
    gamma_mfi: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaMfi")
    kw_theta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="kwTheta")
    material_fu: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFu")
    beta_w: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaW")
    rnd: Optional[Union[StrictFloat, StrictInt]] = None
    fn: Optional[Union[StrictFloat, StrictInt]] = None
    plastic_strain: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="plasticStrain")
    weld_eval: Optional[StrictInt] = Field(default=None, alias="weldEval")
    plastic_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="plasticCapacity")
    plastic_capacity_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="plasticCapacityArea")
    plastic_capacity_area_val: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="plasticCapacityAreaVal")
    is_detailing_status_ok: Optional[StrictBool] = Field(default=None, alias="isDetailingStatusOK")
    is_detailing_status_for_report_ok: Optional[StrictBool] = Field(default=None, alias="isDetailingStatusForReportOK")
    theta: Optional[Union[StrictFloat, StrictInt]] = None
    is_closed_weld: Optional[StrictBool] = Field(default=None, alias="isClosedWeld")
    weld_check_method_hk: Optional[IdeaStatiCaConnectionBasicTypesDataWeldCheckMethodHKCIBasicTypes] = Field(default=None, alias="weldCheckMethodHK")
    phi_w: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiW")
    omega_w: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="omegaW")
    fuw: Optional[Union[StrictFloat, StrictInt]] = None
    checks_nonconformities: Optional[CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes] = Field(default=None, alias="checksNonconformities")
    detailing_checks_weld: Optional[CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes] = Field(default=None, alias="detailingChecksWeld")
    weld_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldResistance")
    weld_elem_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldElemArea")
    xu: Optional[Union[StrictFloat, StrictInt]] = None
    theta_weld: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="thetaWeld")
    aisc_directional_strength_increase: Optional[StrictBool] = Field(default=None, alias="aiscDirectionalStrengthIncrease")
    mw: Optional[Union[StrictFloat, StrictInt]] = None
    fusion_area_elem: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fusionAreaElem")
    fu_base_metal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fuBaseMetal")
    base_metal_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="baseMetalResistance")
    theta1_weld: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="theta1Weld")
    theta2_weld: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="theta2Weld")
    fn_weld: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fnWeld")
    length_elem_reduced: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="lengthElemReduced")
    length_reduced: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="lengthReduced")
    beta_f_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaF_SNIP")
    beta_z_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaZ_SNIP")
    rwf_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rwf_SNIP")
    rwz_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rwz_SNIP")
    gamma_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaC")
    gamma_wm_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaWm_SNIP")
    fexx: Optional[Union[StrictFloat, StrictInt]] = None
    fnbm: Optional[Union[StrictFloat, StrictInt]] = None
    awe: Optional[Union[StrictFloat, StrictInt]] = None
    abm: Optional[Union[StrictFloat, StrictInt]] = None
    base_metal_capacity: Optional[StrictBool] = Field(default=None, alias="baseMetalCapacity")
    beta_f_chn: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaF_CHN")
    is_butt_weld: Optional[StrictBool] = Field(default=None, alias="isButtWeld")
    gamma_mw_is: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaMw_IS")
    weld_longitudinal_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldLongitudinalForce")
    weld_transversal_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldTransversalForce")
    weld_longitudinal_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldLongitudinalResistance")
    weld_transversal_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldTransversalResistance")
    weld_theta_hk: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldTheta_HK")
    weld_coeff_k_hk: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldCoeffK_HK")
    is_weld_design_strength_table_value: Optional[StrictBool] = Field(default=None, alias="isWeldDesignStrengthTableValue")
    is_ecen_weld_material_and_electrode: Optional[StrictBool] = Field(default=None, alias="isEcenWeldMaterialAndElectrode")
    ue: Optional[Union[StrictFloat, StrictInt]] = None
    us: Optional[Union[StrictFloat, StrictInt]] = None
    weld_position_snip: Optional[IdeaStatiCaConnectionBasicTypesDataWeldPositionSNIPCIBasicTypes] = Field(default=None, alias="weldPositionSNIP")
    welding_type_snip: Optional[IdeaStatiCaConnectionBasicTypesDataWeldingTypeSNIPCIBasicTypes] = Field(default=None, alias="weldingTypeSNIP")
    fire_temperature: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fireTemperature")
    fire_design: Optional[StrictBool] = Field(default=None, alias="fireDesign")
    is_horizontal_tying: Optional[StrictBool] = Field(default=None, alias="isHorizontalTying")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["joinedItemName", "designedThickness", "thickness", "legSize", "maxEquivalentStress", "equivalentStressResistance", "sigmaPerpendicular", "sigmaPerpendicularMax", "sigmaPerpendicularResistance", "unityCheckStress", "unityCheckWeld", "unityCheckBaseMetal", "materialName", "weldType2", "weldWithContact", "items", "structItems", "tauy", "taux", "tauxwf", "sigmawf", "weldArea", "length", "lengthElem", "forcesAllItems", "weldStressDiagram", "gammaM0", "gammaM2", "gammaMfi", "kwTheta", "materialFu", "betaW", "rnd", "fn", "plasticStrain", "weldEval", "plasticCapacity", "plasticCapacityArea", "plasticCapacityAreaVal", "isDetailingStatusOK", "isDetailingStatusForReportOK", "theta", "isClosedWeld", "weldCheckMethodHK", "phiW", "omegaW", "fuw", "checksNonconformities", "detailingChecksWeld", "weldResistance", "weldElemArea", "xu", "thetaWeld", "aiscDirectionalStrengthIncrease", "mw", "fusionAreaElem", "fuBaseMetal", "baseMetalResistance", "theta1Weld", "theta2Weld", "fnWeld", "lengthElemReduced", "lengthReduced", "betaF_SNIP", "betaZ_SNIP", "rwf_SNIP", "rwz_SNIP", "gammaC", "gammaWm_SNIP", "fexx", "fnbm", "awe", "abm", "baseMetalCapacity", "betaF_CHN", "isButtWeld", "gammaMw_IS", "weldLongitudinalForce", "weldTransversalForce", "weldLongitudinalResistance", "weldTransversalResistance", "weldTheta_HK", "weldCoeffK_HK", "isWeldDesignStrengthTableValue", "isEcenWeldMaterialAndElectrode", "ue", "us", "weldPositionSNIP", "weldingTypeSNIP", "fireTemperature", "fireDesign", "isHorizontalTying", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of checks_nonconformities
        if self.checks_nonconformities:
            _dict['checksNonconformities'] = self.checks_nonconformities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of detailing_checks_weld
        if self.detailing_checks_weld:
            _dict['detailingChecksWeld'] = self.detailing_checks_weld.to_dict()
        # set to None if joined_item_name (nullable) is None
        # and model_fields_set contains the field
        if self.joined_item_name is None and "joined_item_name" in self.model_fields_set:
            _dict['joinedItemName'] = None

        # set to None if material_name (nullable) is None
        # and model_fields_set contains the field
        if self.material_name is None and "material_name" in self.model_fields_set:
            _dict['materialName'] = None

        # set to None if items (nullable) is None
        # and model_fields_set contains the field
        if self.items is None and "items" in self.model_fields_set:
            _dict['items'] = None

        # set to None if struct_items (nullable) is None
        # and model_fields_set contains the field
        if self.struct_items is None and "struct_items" in self.model_fields_set:
            _dict['structItems'] = None

        # set to None if forces_all_items (nullable) is None
        # and model_fields_set contains the field
        if self.forces_all_items is None and "forces_all_items" in self.model_fields_set:
            _dict['forcesAllItems'] = None

        # set to None if weld_stress_diagram (nullable) is None
        # and model_fields_set contains the field
        if self.weld_stress_diagram is None and "weld_stress_diagram" in self.model_fields_set:
            _dict['weldStressDiagram'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if load_case (nullable) is None
        # and model_fields_set contains the field
        if self.load_case is None and "load_case" in self.model_fields_set:
            _dict['loadCase'] = None

        # set to None if form (nullable) is None
        # and model_fields_set contains the field
        if self.form is None and "form" in self.model_fields_set:
            _dict['form'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "joinedItemName": obj.get("joinedItemName"),
            "designedThickness": obj.get("designedThickness"),
            "thickness": obj.get("thickness"),
            "legSize": obj.get("legSize"),
            "maxEquivalentStress": obj.get("maxEquivalentStress"),
            "equivalentStressResistance": obj.get("equivalentStressResistance"),
            "sigmaPerpendicular": obj.get("sigmaPerpendicular"),
            "sigmaPerpendicularMax": obj.get("sigmaPerpendicularMax"),
            "sigmaPerpendicularResistance": obj.get("sigmaPerpendicularResistance"),
            "unityCheckStress": obj.get("unityCheckStress"),
            "unityCheckWeld": obj.get("unityCheckWeld"),
            "unityCheckBaseMetal": obj.get("unityCheckBaseMetal"),
            "materialName": obj.get("materialName"),
            "weldType2": obj.get("weldType2"),
            "weldWithContact": obj.get("weldWithContact"),
            "items": obj.get("items"),
            "structItems": obj.get("structItems"),
            "tauy": obj.get("tauy"),
            "taux": obj.get("taux"),
            "tauxwf": obj.get("tauxwf"),
            "sigmawf": obj.get("sigmawf"),
            "weldArea": obj.get("weldArea"),
            "length": obj.get("length"),
            "lengthElem": obj.get("lengthElem"),
            "forcesAllItems": obj.get("forcesAllItems"),
            "weldStressDiagram": obj.get("weldStressDiagram"),
            "gammaM0": obj.get("gammaM0"),
            "gammaM2": obj.get("gammaM2"),
            "gammaMfi": obj.get("gammaMfi"),
            "kwTheta": obj.get("kwTheta"),
            "materialFu": obj.get("materialFu"),
            "betaW": obj.get("betaW"),
            "rnd": obj.get("rnd"),
            "fn": obj.get("fn"),
            "plasticStrain": obj.get("plasticStrain"),
            "weldEval": obj.get("weldEval"),
            "plasticCapacity": obj.get("plasticCapacity"),
            "plasticCapacityArea": obj.get("plasticCapacityArea"),
            "plasticCapacityAreaVal": obj.get("plasticCapacityAreaVal"),
            "isDetailingStatusOK": obj.get("isDetailingStatusOK"),
            "isDetailingStatusForReportOK": obj.get("isDetailingStatusForReportOK"),
            "theta": obj.get("theta"),
            "isClosedWeld": obj.get("isClosedWeld"),
            "weldCheckMethodHK": obj.get("weldCheckMethodHK"),
            "phiW": obj.get("phiW"),
            "omegaW": obj.get("omegaW"),
            "fuw": obj.get("fuw"),
            "checksNonconformities": CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes.from_dict(obj["checksNonconformities"]) if obj.get("checksNonconformities") is not None else None,
            "detailingChecksWeld": CIConnectionsDataDetailingDetailingChecksWeldCIBasicTypes.from_dict(obj["detailingChecksWeld"]) if obj.get("detailingChecksWeld") is not None else None,
            "weldResistance": obj.get("weldResistance"),
            "weldElemArea": obj.get("weldElemArea"),
            "xu": obj.get("xu"),
            "thetaWeld": obj.get("thetaWeld"),
            "aiscDirectionalStrengthIncrease": obj.get("aiscDirectionalStrengthIncrease"),
            "mw": obj.get("mw"),
            "fusionAreaElem": obj.get("fusionAreaElem"),
            "fuBaseMetal": obj.get("fuBaseMetal"),
            "baseMetalResistance": obj.get("baseMetalResistance"),
            "theta1Weld": obj.get("theta1Weld"),
            "theta2Weld": obj.get("theta2Weld"),
            "fnWeld": obj.get("fnWeld"),
            "lengthElemReduced": obj.get("lengthElemReduced"),
            "lengthReduced": obj.get("lengthReduced"),
            "betaF_SNIP": obj.get("betaF_SNIP"),
            "betaZ_SNIP": obj.get("betaZ_SNIP"),
            "rwf_SNIP": obj.get("rwf_SNIP"),
            "rwz_SNIP": obj.get("rwz_SNIP"),
            "gammaC": obj.get("gammaC"),
            "gammaWm_SNIP": obj.get("gammaWm_SNIP"),
            "fexx": obj.get("fexx"),
            "fnbm": obj.get("fnbm"),
            "awe": obj.get("awe"),
            "abm": obj.get("abm"),
            "baseMetalCapacity": obj.get("baseMetalCapacity"),
            "betaF_CHN": obj.get("betaF_CHN"),
            "isButtWeld": obj.get("isButtWeld"),
            "gammaMw_IS": obj.get("gammaMw_IS"),
            "weldLongitudinalForce": obj.get("weldLongitudinalForce"),
            "weldTransversalForce": obj.get("weldTransversalForce"),
            "weldLongitudinalResistance": obj.get("weldLongitudinalResistance"),
            "weldTransversalResistance": obj.get("weldTransversalResistance"),
            "weldTheta_HK": obj.get("weldTheta_HK"),
            "weldCoeffK_HK": obj.get("weldCoeffK_HK"),
            "isWeldDesignStrengthTableValue": obj.get("isWeldDesignStrengthTableValue"),
            "isEcenWeldMaterialAndElectrode": obj.get("isEcenWeldMaterialAndElectrode"),
            "ue": obj.get("ue"),
            "us": obj.get("us"),
            "weldPositionSNIP": obj.get("weldPositionSNIP"),
            "weldingTypeSNIP": obj.get("weldingTypeSNIP"),
            "fireTemperature": obj.get("fireTemperature"),
            "fireDesign": obj.get("fireDesign"),
            "isHorizontalTying": obj.get("isHorizontalTying"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "checkStatus": obj.get("checkStatus"),
            "limitCheckStatus": obj.get("limitCheckStatus"),
            "loadCaseId": obj.get("loadCaseId"),
            "loadCase": obj.get("loadCase"),
            "maxUnityCheck": obj.get("maxUnityCheck"),
            "form": obj.get("form")
        })
        return _obj


