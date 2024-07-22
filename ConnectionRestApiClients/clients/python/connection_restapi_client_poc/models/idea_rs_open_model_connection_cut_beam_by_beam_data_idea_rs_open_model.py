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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_method_idea_rs_open_model import IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_orientation_idea_rs_open_model import IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_part_idea_rs_open_model import IdeaRSOpenModelConnectionCutPartIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_distance_comparison_idea_rs_open_model import IdeaRSOpenModelConnectionDistanceComparisonIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_weld_type_idea_rs_open_model import IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model import IdeaRSOpenModelReferenceElementIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel
    """ # noqa: E501
    modified_object: Optional[IdeaRSOpenModelReferenceElementIdeaRSOpenModel] = Field(default=None, alias="modifiedObject")
    cutting_object: Optional[IdeaRSOpenModelReferenceElementIdeaRSOpenModel] = Field(default=None, alias="cuttingObject")
    is_weld: Optional[StrictBool] = Field(default=None, alias="isWeld")
    weld_thickness: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldThickness")
    weld_type: Optional[IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel] = Field(default=None, alias="weldType")
    offset: Optional[Union[StrictFloat, StrictInt]] = None
    method: Optional[IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel] = None
    orientation: Optional[IdeaRSOpenModelConnectionCutOrientationIdeaRSOpenModel] = None
    plane_on_cutting_object: Optional[IdeaRSOpenModelConnectionDistanceComparisonIdeaRSOpenModel] = Field(default=None, alias="planeOnCuttingObject")
    cut_part: Optional[IdeaRSOpenModelConnectionCutPartIdeaRSOpenModel] = Field(default=None, alias="cutPart")
    __properties: ClassVar[List[str]] = ["modifiedObject", "cuttingObject", "isWeld", "weldThickness", "weldType", "offset", "method", "orientation", "planeOnCuttingObject", "cutPart"]

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
        """Create an instance of IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of modified_object
        if self.modified_object:
            _dict['modifiedObject'] = self.modified_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cutting_object
        if self.cutting_object:
            _dict['cuttingObject'] = self.cutting_object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "modifiedObject": IdeaRSOpenModelReferenceElementIdeaRSOpenModel.from_dict(obj["modifiedObject"]) if obj.get("modifiedObject") is not None else None,
            "cuttingObject": IdeaRSOpenModelReferenceElementIdeaRSOpenModel.from_dict(obj["cuttingObject"]) if obj.get("cuttingObject") is not None else None,
            "isWeld": obj.get("isWeld"),
            "weldThickness": obj.get("weldThickness"),
            "weldType": obj.get("weldType"),
            "offset": obj.get("offset"),
            "method": obj.get("method"),
            "orientation": obj.get("orientation"),
            "planeOnCuttingObject": obj.get("planeOnCuttingObject"),
            "cutPart": obj.get("cutPart")
        })
        return _obj


