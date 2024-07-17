# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.ci_connections_data_detailing_detailing_checks_pin_ci_basic_types import CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    pin_assembly_name: Optional[StrictStr] = Field(default=None, alias="pinAssemblyName")
    pin_shear_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinShearResistance")
    pin_bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinBearingResistance")
    pin_replaceable_bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinReplaceableBearingResistance")
    pin_bending_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinBendingResistance")
    pin_replaceable_bending_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinReplaceableBendingResistance")
    pin_combined_shear_and_bending_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinCombinedShearAndBendingResistance")
    contact_bearing_stress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="contactBearingStress")
    contact_bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="contactBearingResistance")
    unity_check_pin_shear: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinShear")
    unity_check_pin_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinBearing")
    unity_check_pin_replaceable_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinReplaceableBearing")
    unity_check_pin_bearing_decisive: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinBearingDecisive")
    unity_check_pin_bending: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinBending")
    unity_check_pin_replaceable_bending: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinReplaceableBending")
    unity_check_pin_bending_decisive: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinBendingDecisive")
    unity_check_pin_combined_shear_and_bending: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinCombinedShearAndBending")
    unity_check_pin_replaceable_contact_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckPinReplaceableContactBearing")
    max_unity_check_shear: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheckShear")
    is_pin_replaceable: Optional[StrictBool] = Field(default=None, alias="isPinReplaceable")
    pin_all_elements_all_sections_forces_for_diagram: Optional[Dict[str, List[List[Union[StrictFloat, StrictInt]]]]] = Field(default=None, alias="pinAllElementsAllSectionsForcesForDiagram")
    pin_shear_forces: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="pinShearForces")
    pin_bearing_forces: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="pinBearingForces")
    pin_bearing_forces_by_plate_id: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, alias="pinBearingForcesByPlateID")
    pin_bending_forces: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="pinBendingForces")
    pin_shear_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinShearForce")
    pin_bearing_force_for_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinBearingForceForBearing")
    pin_bending_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinBendingForce")
    pin_cross_sectional_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinCrossSectionalArea")
    pin_section_modulus: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinSectionModulus")
    pin_diameter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinDiameter")
    pin_hole_diameter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinHoleDiameter")
    pin_ultimate_tensile_strength: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinUltimateTensileStrength")
    pin_yield_strength: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinYieldStrength")
    connected_part_yield_strength: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectedPartYieldStrength")
    connected_part_thickness_for_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectedPartThicknessForBearing")
    decisive_yield_strength_for_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="decisiveYieldStrengthForBearing")
    modulus_of_elasticity_for_contact_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="modulusOfElasticityForContactBearing")
    yield_strength_for_contact_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="yieldStrengthForContactBearing")
    connected_part_thickness_for_contact_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectedPartThicknessForContactBearing")
    pin_bearing_force_for_contact_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="pinBearingForceForContactBearing")
    gamma_m0: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM0")
    gamma_m2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM2")
    gamma_m6ser: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM6ser")
    gamma_mfi: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaMfi")
    is_fire_design: Optional[StrictBool] = Field(default=None, alias="isFireDesign")
    fire_temperature: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fireTemperature")
    factor_kb_theta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="factorKbTheta")
    detailing_checks_pin: Optional[CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes] = Field(default=None, alias="detailingChecksPin")
    is_detailing_status_ok: Optional[StrictBool] = Field(default=None, alias="isDetailingStatusOK")
    is_detailing_status_for_report_ok: Optional[StrictBool] = Field(default=None, alias="isDetailingStatusForReportOK")
    forces_all_load_cases: Optional[Dict[str, List[Union[StrictFloat, StrictInt]]]] = Field(default=None, alias="forcesAllLoadCases")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["pinAssemblyName", "pinShearResistance", "pinBearingResistance", "pinReplaceableBearingResistance", "pinBendingResistance", "pinReplaceableBendingResistance", "pinCombinedShearAndBendingResistance", "contactBearingStress", "contactBearingResistance", "unityCheckPinShear", "unityCheckPinBearing", "unityCheckPinReplaceableBearing", "unityCheckPinBearingDecisive", "unityCheckPinBending", "unityCheckPinReplaceableBending", "unityCheckPinBendingDecisive", "unityCheckPinCombinedShearAndBending", "unityCheckPinReplaceableContactBearing", "maxUnityCheckShear", "isPinReplaceable", "pinAllElementsAllSectionsForcesForDiagram", "pinShearForces", "pinBearingForces", "pinBearingForcesByPlateID", "pinBendingForces", "pinShearForce", "pinBearingForceForBearing", "pinBendingForce", "pinCrossSectionalArea", "pinSectionModulus", "pinDiameter", "pinHoleDiameter", "pinUltimateTensileStrength", "pinYieldStrength", "connectedPartYieldStrength", "connectedPartThicknessForBearing", "decisiveYieldStrengthForBearing", "modulusOfElasticityForContactBearing", "yieldStrengthForContactBearing", "connectedPartThicknessForContactBearing", "pinBearingForceForContactBearing", "gammaM0", "gammaM2", "gammaM6ser", "gammaMfi", "isFireDesign", "fireTemperature", "factorKbTheta", "detailingChecksPin", "isDetailingStatusOK", "isDetailingStatusForReportOK", "forcesAllLoadCases", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of detailing_checks_pin
        if self.detailing_checks_pin:
            _dict['detailingChecksPin'] = self.detailing_checks_pin.to_dict()
        # set to None if pin_assembly_name (nullable) is None
        # and model_fields_set contains the field
        if self.pin_assembly_name is None and "pin_assembly_name" in self.model_fields_set:
            _dict['pinAssemblyName'] = None

        # set to None if pin_all_elements_all_sections_forces_for_diagram (nullable) is None
        # and model_fields_set contains the field
        if self.pin_all_elements_all_sections_forces_for_diagram is None and "pin_all_elements_all_sections_forces_for_diagram" in self.model_fields_set:
            _dict['pinAllElementsAllSectionsForcesForDiagram'] = None

        # set to None if pin_shear_forces (nullable) is None
        # and model_fields_set contains the field
        if self.pin_shear_forces is None and "pin_shear_forces" in self.model_fields_set:
            _dict['pinShearForces'] = None

        # set to None if pin_bearing_forces (nullable) is None
        # and model_fields_set contains the field
        if self.pin_bearing_forces is None and "pin_bearing_forces" in self.model_fields_set:
            _dict['pinBearingForces'] = None

        # set to None if pin_bearing_forces_by_plate_id (nullable) is None
        # and model_fields_set contains the field
        if self.pin_bearing_forces_by_plate_id is None and "pin_bearing_forces_by_plate_id" in self.model_fields_set:
            _dict['pinBearingForcesByPlateID'] = None

        # set to None if pin_bending_forces (nullable) is None
        # and model_fields_set contains the field
        if self.pin_bending_forces is None and "pin_bending_forces" in self.model_fields_set:
            _dict['pinBendingForces'] = None

        # set to None if forces_all_load_cases (nullable) is None
        # and model_fields_set contains the field
        if self.forces_all_load_cases is None and "forces_all_load_cases" in self.model_fields_set:
            _dict['forcesAllLoadCases'] = None

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
        """Create an instance of ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pinAssemblyName": obj.get("pinAssemblyName"),
            "pinShearResistance": obj.get("pinShearResistance"),
            "pinBearingResistance": obj.get("pinBearingResistance"),
            "pinReplaceableBearingResistance": obj.get("pinReplaceableBearingResistance"),
            "pinBendingResistance": obj.get("pinBendingResistance"),
            "pinReplaceableBendingResistance": obj.get("pinReplaceableBendingResistance"),
            "pinCombinedShearAndBendingResistance": obj.get("pinCombinedShearAndBendingResistance"),
            "contactBearingStress": obj.get("contactBearingStress"),
            "contactBearingResistance": obj.get("contactBearingResistance"),
            "unityCheckPinShear": obj.get("unityCheckPinShear"),
            "unityCheckPinBearing": obj.get("unityCheckPinBearing"),
            "unityCheckPinReplaceableBearing": obj.get("unityCheckPinReplaceableBearing"),
            "unityCheckPinBearingDecisive": obj.get("unityCheckPinBearingDecisive"),
            "unityCheckPinBending": obj.get("unityCheckPinBending"),
            "unityCheckPinReplaceableBending": obj.get("unityCheckPinReplaceableBending"),
            "unityCheckPinBendingDecisive": obj.get("unityCheckPinBendingDecisive"),
            "unityCheckPinCombinedShearAndBending": obj.get("unityCheckPinCombinedShearAndBending"),
            "unityCheckPinReplaceableContactBearing": obj.get("unityCheckPinReplaceableContactBearing"),
            "maxUnityCheckShear": obj.get("maxUnityCheckShear"),
            "isPinReplaceable": obj.get("isPinReplaceable"),
            "pinAllElementsAllSectionsForcesForDiagram": obj.get("pinAllElementsAllSectionsForcesForDiagram"),
            "pinShearForces": obj.get("pinShearForces"),
            "pinBearingForces": obj.get("pinBearingForces"),
            "pinBearingForcesByPlateID": obj.get("pinBearingForcesByPlateID"),
            "pinBendingForces": obj.get("pinBendingForces"),
            "pinShearForce": obj.get("pinShearForce"),
            "pinBearingForceForBearing": obj.get("pinBearingForceForBearing"),
            "pinBendingForce": obj.get("pinBendingForce"),
            "pinCrossSectionalArea": obj.get("pinCrossSectionalArea"),
            "pinSectionModulus": obj.get("pinSectionModulus"),
            "pinDiameter": obj.get("pinDiameter"),
            "pinHoleDiameter": obj.get("pinHoleDiameter"),
            "pinUltimateTensileStrength": obj.get("pinUltimateTensileStrength"),
            "pinYieldStrength": obj.get("pinYieldStrength"),
            "connectedPartYieldStrength": obj.get("connectedPartYieldStrength"),
            "connectedPartThicknessForBearing": obj.get("connectedPartThicknessForBearing"),
            "decisiveYieldStrengthForBearing": obj.get("decisiveYieldStrengthForBearing"),
            "modulusOfElasticityForContactBearing": obj.get("modulusOfElasticityForContactBearing"),
            "yieldStrengthForContactBearing": obj.get("yieldStrengthForContactBearing"),
            "connectedPartThicknessForContactBearing": obj.get("connectedPartThicknessForContactBearing"),
            "pinBearingForceForContactBearing": obj.get("pinBearingForceForContactBearing"),
            "gammaM0": obj.get("gammaM0"),
            "gammaM2": obj.get("gammaM2"),
            "gammaM6ser": obj.get("gammaM6ser"),
            "gammaMfi": obj.get("gammaMfi"),
            "isFireDesign": obj.get("isFireDesign"),
            "fireTemperature": obj.get("fireTemperature"),
            "factorKbTheta": obj.get("factorKbTheta"),
            "detailingChecksPin": CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes.from_dict(obj["detailingChecksPin"]) if obj.get("detailingChecksPin") is not None else None,
            "isDetailingStatusOK": obj.get("isDetailingStatusOK"),
            "isDetailingStatusForReportOK": obj.get("isDetailingStatusForReportOK"),
            "forcesAllLoadCases": obj.get("forcesAllLoadCases"),
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


