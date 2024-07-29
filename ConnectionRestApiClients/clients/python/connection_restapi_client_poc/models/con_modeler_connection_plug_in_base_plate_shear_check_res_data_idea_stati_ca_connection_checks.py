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
from connection_restapi_client_poc.models.idea_stati_ca_connection_basic_types_data_cone_breakout_check_type_ci_basic_types import IdeaStatiCaConnectionBasicTypesDataConeBreakoutCheckTypeCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    vrdf: Optional[Union[StrictFloat, StrictInt]] = None
    vrdx: Optional[Union[StrictFloat, StrictInt]] = None
    vrdy: Optional[Union[StrictFloat, StrictInt]] = None
    vx: Optional[Union[StrictFloat, StrictInt]] = None
    vy: Optional[Union[StrictFloat, StrictInt]] = None
    v: Optional[Union[StrictFloat, StrictInt]] = None
    vr: Optional[Union[StrictFloat, StrictInt]] = None
    pbr: Optional[Union[StrictFloat, StrictInt]] = None
    vcb: Optional[Union[StrictFloat, StrictInt]] = None
    friction_coefficient: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="frictionCoefficient")
    shear_iron_css: Optional[StrictStr] = Field(default=None, alias="shearIronCss")
    shear_iron_applied: Optional[StrictBool] = Field(default=None, alias="shearIronApplied")
    unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheck")
    avx: Optional[Union[StrictFloat, StrictInt]] = None
    avy: Optional[Union[StrictFloat, StrictInt]] = None
    fy: Optional[Union[StrictFloat, StrictInt]] = None
    nsd: Optional[Union[StrictFloat, StrictInt]] = None
    shear_force_transfer: Optional[StrictInt] = Field(default=None, alias="shearForceTransfer")
    gamma_m0: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM0")
    asd: Optional[StrictBool] = None
    phi_omega: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiOmega")
    bearing_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="bearingResistance")
    num_of_tensioned_anchors: Optional[StrictInt] = Field(default=None, alias="numOfTensionedAnchors")
    phi_br: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiBr")
    fc: Optional[Union[StrictFloat, StrictInt]] = None
    alpha_v: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="alphaV")
    psi_alpha_v: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="psiAlphaV")
    avc_cone_breakout_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="avcConeBreakoutArea")
    unity_check_cone_breakout_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckConeBreakoutResistance")
    unity_check_bearing_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckBearingCapacity")
    phi_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiC")
    omega_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="omegaC")
    phi_s: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiS")
    shear_lug_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shearLugForce")
    shear_lug_force_component: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shearLugForceComponent")
    cone_breakout_check_type: Optional[IdeaStatiCaConnectionBasicTypesDataConeBreakoutCheckTypeCIBasicTypes] = Field(default=None, alias="coneBreakoutCheckType")
    shear_lug_projection_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="shearLugProjectionArea")
    comp_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="compForce")
    kc: Optional[Union[StrictFloat, StrictInt]] = None
    connector_tensile_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectorTensileArea")
    connector_fy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="connectorFy")
    ny: Optional[Union[StrictFloat, StrictInt]] = None
    pa: Optional[Union[StrictFloat, StrictInt]] = None
    a: Optional[Union[StrictFloat, StrictInt]] = None
    l: Optional[Union[StrictFloat, StrictInt]] = None
    b: Optional[Union[StrictFloat, StrictInt]] = None
    gamma_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaC")
    v_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="vFactor")
    k1_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="k1Factor")
    sigma_rdmax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="sigmaRdmax")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["vrdf", "vrdx", "vrdy", "vx", "vy", "v", "vr", "pbr", "vcb", "frictionCoefficient", "shearIronCss", "shearIronApplied", "unityCheck", "avx", "avy", "fy", "nsd", "shearForceTransfer", "gammaM0", "asd", "phiOmega", "bearingResistance", "numOfTensionedAnchors", "phiBr", "fc", "alphaV", "psiAlphaV", "avcConeBreakoutArea", "unityCheckConeBreakoutResistance", "unityCheckBearingCapacity", "phiC", "omegaC", "phiS", "shearLugForce", "shearLugForceComponent", "coneBreakoutCheckType", "shearLugProjectionArea", "compForce", "kc", "connectorTensileArea", "connectorFy", "ny", "pa", "a", "l", "b", "gammaC", "vFactor", "k1Factor", "sigmaRdmax", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # set to None if shear_iron_css (nullable) is None
        # and model_fields_set contains the field
        if self.shear_iron_css is None and "shear_iron_css" in self.model_fields_set:
            _dict['shearIronCss'] = None

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
        """Create an instance of ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vrdf": obj.get("vrdf"),
            "vrdx": obj.get("vrdx"),
            "vrdy": obj.get("vrdy"),
            "vx": obj.get("vx"),
            "vy": obj.get("vy"),
            "v": obj.get("v"),
            "vr": obj.get("vr"),
            "pbr": obj.get("pbr"),
            "vcb": obj.get("vcb"),
            "frictionCoefficient": obj.get("frictionCoefficient"),
            "shearIronCss": obj.get("shearIronCss"),
            "shearIronApplied": obj.get("shearIronApplied"),
            "unityCheck": obj.get("unityCheck"),
            "avx": obj.get("avx"),
            "avy": obj.get("avy"),
            "fy": obj.get("fy"),
            "nsd": obj.get("nsd"),
            "shearForceTransfer": obj.get("shearForceTransfer"),
            "gammaM0": obj.get("gammaM0"),
            "asd": obj.get("asd"),
            "phiOmega": obj.get("phiOmega"),
            "bearingResistance": obj.get("bearingResistance"),
            "numOfTensionedAnchors": obj.get("numOfTensionedAnchors"),
            "phiBr": obj.get("phiBr"),
            "fc": obj.get("fc"),
            "alphaV": obj.get("alphaV"),
            "psiAlphaV": obj.get("psiAlphaV"),
            "avcConeBreakoutArea": obj.get("avcConeBreakoutArea"),
            "unityCheckConeBreakoutResistance": obj.get("unityCheckConeBreakoutResistance"),
            "unityCheckBearingCapacity": obj.get("unityCheckBearingCapacity"),
            "phiC": obj.get("phiC"),
            "omegaC": obj.get("omegaC"),
            "phiS": obj.get("phiS"),
            "shearLugForce": obj.get("shearLugForce"),
            "shearLugForceComponent": obj.get("shearLugForceComponent"),
            "coneBreakoutCheckType": obj.get("coneBreakoutCheckType"),
            "shearLugProjectionArea": obj.get("shearLugProjectionArea"),
            "compForce": obj.get("compForce"),
            "kc": obj.get("kc"),
            "connectorTensileArea": obj.get("connectorTensileArea"),
            "connectorFy": obj.get("connectorFy"),
            "ny": obj.get("ny"),
            "pa": obj.get("pa"),
            "a": obj.get("a"),
            "l": obj.get("l"),
            "b": obj.get("b"),
            "gammaC": obj.get("gammaC"),
            "vFactor": obj.get("vFactor"),
            "k1Factor": obj.get("k1Factor"),
            "sigmaRdmax": obj.get("sigmaRdmax"),
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


