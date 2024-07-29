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
from connection_restapi_client_poc.models.cigi_cl2_d_point2_dci_geometry2_d import CIGiCL2DPoint2DCIGeometry2D
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_stiffness_chek_data_load_component_idea_stati_ca_connection_checks import ConModelerConnectionPlugInStiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInStiffnessChekDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInStiffnessChekDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    beam_id: Optional[StrictInt] = Field(default=None, alias="beamId")
    component: Optional[StrictStr] = None
    component_id: Optional[ConModelerConnectionPlugInStiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks] = Field(default=None, alias="componentId")
    myz: Optional[Union[StrictFloat, StrictInt]] = None
    mx_start: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="mxStart")
    my_start: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="myStart")
    mz_start: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="mzStart")
    ryz: Optional[Union[StrictFloat, StrictInt]] = None
    ryz_capacity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="ryzCapacity")
    kyz: Optional[Union[StrictFloat, StrictInt]] = None
    kyz_classification: Optional[StrictStr] = Field(default=None, alias="kyzClassification")
    kyz_limit_rigid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="kyzLimitRigid")
    kyz_limit_pinned: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="kyzLimitPinned")
    nx: Optional[Union[StrictFloat, StrictInt]] = None
    nx_start: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nxStart")
    dx: Optional[Union[StrictFloat, StrictInt]] = None
    kx: Optional[Union[StrictFloat, StrictInt]] = None
    points: Optional[List[CIGiCL2DPoint2DCIGeometry2D]] = None
    points_shell: Optional[List[CIGiCL2DPoint2DCIGeometry2D]] = Field(default=None, alias="pointsShell")
    points_linear: Optional[List[CIGiCL2DPoint2DCIGeometry2D]] = Field(default=None, alias="pointsLinear")
    n_mcrd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nMcrd")
    n_mjrd: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nMjrd")
    theoretical_length: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="theoreticalLength")
    sjini: Optional[Union[StrictFloat, StrictInt]] = None
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["beamId", "component", "componentId", "myz", "mxStart", "myStart", "mzStart", "ryz", "ryzCapacity", "kyz", "kyzClassification", "kyzLimitRigid", "kyzLimitPinned", "nx", "nxStart", "dx", "kx", "points", "pointsShell", "pointsLinear", "nMcrd", "nMjrd", "theoreticalLength", "sjini", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInStiffnessChekDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in points (list)
        _items = []
        if self.points:
            for _item_points in self.points:
                if _item_points:
                    _items.append(_item_points.to_dict())
            _dict['points'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in points_shell (list)
        _items = []
        if self.points_shell:
            for _item_points_shell in self.points_shell:
                if _item_points_shell:
                    _items.append(_item_points_shell.to_dict())
            _dict['pointsShell'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in points_linear (list)
        _items = []
        if self.points_linear:
            for _item_points_linear in self.points_linear:
                if _item_points_linear:
                    _items.append(_item_points_linear.to_dict())
            _dict['pointsLinear'] = _items
        # set to None if component (nullable) is None
        # and model_fields_set contains the field
        if self.component is None and "component" in self.model_fields_set:
            _dict['component'] = None

        # set to None if kyz_classification (nullable) is None
        # and model_fields_set contains the field
        if self.kyz_classification is None and "kyz_classification" in self.model_fields_set:
            _dict['kyzClassification'] = None

        # set to None if points (nullable) is None
        # and model_fields_set contains the field
        if self.points is None and "points" in self.model_fields_set:
            _dict['points'] = None

        # set to None if points_shell (nullable) is None
        # and model_fields_set contains the field
        if self.points_shell is None and "points_shell" in self.model_fields_set:
            _dict['pointsShell'] = None

        # set to None if points_linear (nullable) is None
        # and model_fields_set contains the field
        if self.points_linear is None and "points_linear" in self.model_fields_set:
            _dict['pointsLinear'] = None

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
        """Create an instance of ConModelerConnectionPlugInStiffnessChekDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "beamId": obj.get("beamId"),
            "component": obj.get("component"),
            "componentId": obj.get("componentId"),
            "myz": obj.get("myz"),
            "mxStart": obj.get("mxStart"),
            "myStart": obj.get("myStart"),
            "mzStart": obj.get("mzStart"),
            "ryz": obj.get("ryz"),
            "ryzCapacity": obj.get("ryzCapacity"),
            "kyz": obj.get("kyz"),
            "kyzClassification": obj.get("kyzClassification"),
            "kyzLimitRigid": obj.get("kyzLimitRigid"),
            "kyzLimitPinned": obj.get("kyzLimitPinned"),
            "nx": obj.get("nx"),
            "nxStart": obj.get("nxStart"),
            "dx": obj.get("dx"),
            "kx": obj.get("kx"),
            "points": [CIGiCL2DPoint2DCIGeometry2D.from_dict(_item) for _item in obj["points"]] if obj.get("points") is not None else None,
            "pointsShell": [CIGiCL2DPoint2DCIGeometry2D.from_dict(_item) for _item in obj["pointsShell"]] if obj.get("pointsShell") is not None else None,
            "pointsLinear": [CIGiCL2DPoint2DCIGeometry2D.from_dict(_item) for _item in obj["pointsLinear"]] if obj.get("pointsLinear") is not None else None,
            "nMcrd": obj.get("nMcrd"),
            "nMjrd": obj.get("nMjrd"),
            "theoreticalLength": obj.get("theoreticalLength"),
            "sjini": obj.get("sjini"),
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


