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
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks
    """ # noqa: E501
    bolt_tension_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltTensionResistance")
    compression_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="compressionResistance")
    moment_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="momentResistance")
    bolt_punching_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltPunchingResistance")
    bolt_shear_resistance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearResistance")
    bolt_shear_resistance_anchor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearResistanceAnchor")
    bolt_shear_resistance_tension: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltShearResistanceTension")
    anchor_stiffness: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="anchorStiffness")
    slip_resistance_coeff: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="slipResistanceCoeff")
    stand_off_gap: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="standOffGap")
    bolt_preloaded_force: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boltPreloadedForce")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["boltTensionResistance", "compressionResistance", "momentResistance", "boltPunchingResistance", "boltShearResistance", "boltShearResistanceAnchor", "boltShearResistanceTension", "anchorStiffness", "slipResistanceCoeff", "standOffGap", "boltPreloadedForce", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string"""
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
        """Create an instance of ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "boltTensionResistance": obj.get("boltTensionResistance"),
            "compressionResistance": obj.get("compressionResistance"),
            "momentResistance": obj.get("momentResistance"),
            "boltPunchingResistance": obj.get("boltPunchingResistance"),
            "boltShearResistance": obj.get("boltShearResistance"),
            "boltShearResistanceAnchor": obj.get("boltShearResistanceAnchor"),
            "boltShearResistanceTension": obj.get("boltShearResistanceTension"),
            "anchorStiffness": obj.get("anchorStiffness"),
            "slipResistanceCoeff": obj.get("slipResistanceCoeff"),
            "standOffGap": obj.get("standOffGap"),
            "boltPreloadedForce": obj.get("boltPreloadedForce"),
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


