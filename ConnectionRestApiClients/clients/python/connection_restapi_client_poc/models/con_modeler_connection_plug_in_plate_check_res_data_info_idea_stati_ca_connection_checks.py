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
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks
    """ # noqa: E501
    material_fy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFy")
    material_fy_phi: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFy_Phi")
    material_fy_omega: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFy_Omega")
    material_fy_design: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFyDesign")
    material_fu: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFu")
    limit_plastic_strain: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="limitPlasticStrain")
    gammaov: Optional[Union[StrictFloat, StrictInt]] = None
    gammash: Optional[Union[StrictFloat, StrictInt]] = None
    cf: Optional[Union[StrictFloat, StrictInt]] = None
    res_safety_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="resSafetyFactor")
    material_fy_fem: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFyFEM")
    material_fy_reduced_by_gamma_m_rus: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="materialFyReducedByGammaM_RUS")
    origin_name: Optional[StrictStr] = Field(default=None, alias="originName")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["materialFy", "materialFy_Phi", "materialFy_Omega", "materialFyDesign", "materialFu", "limitPlasticStrain", "gammaov", "gammash", "cf", "resSafetyFactor", "materialFyFEM", "materialFyReducedByGammaM_RUS", "originName", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string"""
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
        # set to None if origin_name (nullable) is None
        # and model_fields_set contains the field
        if self.origin_name is None and "origin_name" in self.model_fields_set:
            _dict['originName'] = None

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
        """Create an instance of ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "materialFy": obj.get("materialFy"),
            "materialFy_Phi": obj.get("materialFy_Phi"),
            "materialFy_Omega": obj.get("materialFy_Omega"),
            "materialFyDesign": obj.get("materialFyDesign"),
            "materialFu": obj.get("materialFu"),
            "limitPlasticStrain": obj.get("limitPlasticStrain"),
            "gammaov": obj.get("gammaov"),
            "gammash": obj.get("gammash"),
            "cf": obj.get("cf"),
            "resSafetyFactor": obj.get("resSafetyFactor"),
            "materialFyFEM": obj.get("materialFyFEM"),
            "materialFyReducedByGammaM_RUS": obj.get("materialFyReducedByGammaM_RUS"),
            "originName": obj.get("originName"),
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


