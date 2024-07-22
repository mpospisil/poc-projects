# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_code_type_ci_basic_types import IdeaRSWsLibCssServiceCodeTypeCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks
    """ # noqa: E501
    bolt_tension_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltTensionResistance")
    bolt_punching_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltPunchingResistance")
    bolt_tension_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltTensionForce")
    bolt_shear_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearResistance")
    bolt_shear_resistance_tension: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearResistanceTension")
    bolt_bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltBearingResistance")
    bearing_resistance_bolt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bearingResistance_Bolt")
    bearing_resistance_con_part: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bearingResistance_ConPart")
    bolt_shear_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearForce")
    number_of_shear_planes: Optional[StrictInt] = Field(default=None, alias="numberOfShearPlanes")
    bolt_shear_forces: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="boltShearForces")
    unity_check_tension: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckTension")
    unity_check_tension_res: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckTensionRes")
    unity_check_shear: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckShear")
    bolt_assembly_name: Optional[StrictStr] = Field(default=None, alias="boltAssemblyName")
    bolt_tension_force_loadcase: Optional[StrictStr] = Field(default=None, alias="boltTensionForceLoadcase")
    bolt_shear_force_loadcase: Optional[StrictStr] = Field(default=None, alias="boltShearForceLoadcase")
    bolt_interaction_loadcase: Optional[StrictStr] = Field(default=None, alias="boltInteractionLoadcase")
    bolt_tension_force_loadcase_id: Optional[StrictInt] = Field(default=None, alias="boltTensionForceLoadcaseId")
    bolt_shear_force_loadcase_id: Optional[StrictInt] = Field(default=None, alias="boltShearForceLoadcaseId")
    bolt_interaction_loadcase_id: Optional[StrictInt] = Field(default=None, alias="boltInteractionLoadcaseId")
    forces_all_load_cases: Optional[Dict[str, List[Union[StrictFloat, StrictInt]]]] = Field(default=None, alias="forcesAllLoadCases")
    element_axis_y: Optional[StrictStr] = Field(default=None, alias="elementAxisY")
    element_axis_z: Optional[StrictStr] = Field(default=None, alias="elementAxisZ")
    unity_check_bearing: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckBearing")
    code_type: Optional[IdeaRSWsLibCssServiceCodeTypeCIBasicTypes] = Field(default=None, alias="codeType")
    connector_grip_length: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectorGripLength")
    filler_plates_pack_th: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fillerPlatesPackTh")
    angle: Optional[Union[StrictFloat, StrictInt]] = None
    fub: Optional[Union[StrictFloat, StrictInt]] = None
    a_ftrd: Optional[Union[StrictFloat, StrictInt]] = None
    a_fvrd: Optional[Union[StrictFloat, StrictInt]] = None
    k2: Optional[Union[StrictFloat, StrictInt]] = None
    alfa_v: Optional[Union[StrictFloat, StrictInt]] = None
    tp_bprd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tp_Bprd")
    fu_bprd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fu_Bprd")
    dm_bprd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="dm_Bprd")
    gamma_m2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM2")
    d_fbrd: Optional[Union[StrictFloat, StrictInt]] = None
    th_fbrd: Optional[Union[StrictFloat, StrictInt]] = None
    k1: Optional[Union[StrictFloat, StrictInt]] = None
    alpha_b: Optional[Union[StrictFloat, StrictInt]] = None
    gamma_m3: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM3")
    moment_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="momentResistance")
    unity_check_bending: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckBending")
    bolt_moment_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltMomentForce")
    bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bearingResistance")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["boltTensionResistance", "boltPunchingResistance", "boltTensionForce", "boltShearResistance", "boltShearResistanceTension", "boltBearingResistance", "bearingResistance_Bolt", "bearingResistance_ConPart", "boltShearForce", "numberOfShearPlanes", "boltShearForces", "unityCheckTension", "unityCheckTensionRes", "unityCheckShear", "boltAssemblyName", "boltTensionForceLoadcase", "boltShearForceLoadcase", "boltInteractionLoadcase", "boltTensionForceLoadcaseId", "boltShearForceLoadcaseId", "boltInteractionLoadcaseId", "forcesAllLoadCases", "elementAxisY", "elementAxisZ", "unityCheckBearing", "codeType", "connectorGripLength", "fillerPlatesPackTh", "angle", "fub", "a_ftrd", "a_fvrd", "k2", "alfa_v", "tp_Bprd", "fu_Bprd", "dm_Bprd", "gammaM2", "d_fbrd", "th_fbrd", "k1", "alpha_b", "gammaM3", "momentResistance", "unityCheckBending", "boltMomentForce", "bearingResistance", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks from a JSON string"""
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
        # set to None if bolt_shear_forces (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_shear_forces is None and "bolt_shear_forces" in self.model_fields_set:
            _dict['boltShearForces'] = None

        # set to None if bolt_assembly_name (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_assembly_name is None and "bolt_assembly_name" in self.model_fields_set:
            _dict['boltAssemblyName'] = None

        # set to None if bolt_tension_force_loadcase (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_tension_force_loadcase is None and "bolt_tension_force_loadcase" in self.model_fields_set:
            _dict['boltTensionForceLoadcase'] = None

        # set to None if bolt_shear_force_loadcase (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_shear_force_loadcase is None and "bolt_shear_force_loadcase" in self.model_fields_set:
            _dict['boltShearForceLoadcase'] = None

        # set to None if bolt_interaction_loadcase (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_interaction_loadcase is None and "bolt_interaction_loadcase" in self.model_fields_set:
            _dict['boltInteractionLoadcase'] = None

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
        """Create an instance of ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "boltTensionResistance": obj.get("boltTensionResistance"),
            "boltPunchingResistance": obj.get("boltPunchingResistance"),
            "boltTensionForce": obj.get("boltTensionForce"),
            "boltShearResistance": obj.get("boltShearResistance"),
            "boltShearResistanceTension": obj.get("boltShearResistanceTension"),
            "boltBearingResistance": obj.get("boltBearingResistance"),
            "bearingResistance_Bolt": obj.get("bearingResistance_Bolt"),
            "bearingResistance_ConPart": obj.get("bearingResistance_ConPart"),
            "boltShearForce": obj.get("boltShearForce"),
            "numberOfShearPlanes": obj.get("numberOfShearPlanes"),
            "boltShearForces": obj.get("boltShearForces"),
            "unityCheckTension": obj.get("unityCheckTension"),
            "unityCheckTensionRes": obj.get("unityCheckTensionRes"),
            "unityCheckShear": obj.get("unityCheckShear"),
            "boltAssemblyName": obj.get("boltAssemblyName"),
            "boltTensionForceLoadcase": obj.get("boltTensionForceLoadcase"),
            "boltShearForceLoadcase": obj.get("boltShearForceLoadcase"),
            "boltInteractionLoadcase": obj.get("boltInteractionLoadcase"),
            "boltTensionForceLoadcaseId": obj.get("boltTensionForceLoadcaseId"),
            "boltShearForceLoadcaseId": obj.get("boltShearForceLoadcaseId"),
            "boltInteractionLoadcaseId": obj.get("boltInteractionLoadcaseId"),
            "forcesAllLoadCases": obj.get("forcesAllLoadCases"),
            "elementAxisY": obj.get("elementAxisY"),
            "elementAxisZ": obj.get("elementAxisZ"),
            "unityCheckBearing": obj.get("unityCheckBearing"),
            "codeType": obj.get("codeType"),
            "connectorGripLength": obj.get("connectorGripLength"),
            "fillerPlatesPackTh": obj.get("fillerPlatesPackTh"),
            "angle": obj.get("angle"),
            "fub": obj.get("fub"),
            "a_ftrd": obj.get("a_ftrd"),
            "a_fvrd": obj.get("a_fvrd"),
            "k2": obj.get("k2"),
            "alfa_v": obj.get("alfa_v"),
            "tp_Bprd": obj.get("tp_Bprd"),
            "fu_Bprd": obj.get("fu_Bprd"),
            "dm_Bprd": obj.get("dm_Bprd"),
            "gammaM2": obj.get("gammaM2"),
            "d_fbrd": obj.get("d_fbrd"),
            "th_fbrd": obj.get("th_fbrd"),
            "k1": obj.get("k1"),
            "alpha_b": obj.get("alpha_b"),
            "gammaM3": obj.get("gammaM3"),
            "momentResistance": obj.get("momentResistance"),
            "unityCheckBending": obj.get("unityCheckBending"),
            "boltMomentForce": obj.get("boltMomentForce"),
            "bearingResistance": obj.get("bearingResistance"),
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

