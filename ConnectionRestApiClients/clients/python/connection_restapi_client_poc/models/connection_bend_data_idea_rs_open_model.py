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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model import Geometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_vector3_d_idea_rs_open_model import Geometry3DVector3DIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class ConnectionBendDataIdeaRSOpenModel(BaseModel):
    """
    Provides data of bend
    """ # noqa: E501
    plate1_id: Optional[StrictInt] = Field(default=None, description="First plate", alias="plate1Id")
    plate2_id: Optional[StrictInt] = Field(default=None, description="Second plate", alias="plate2Id")
    radius: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Radius of bend")
    point1_of_side_boundary1: Optional[Geometry3DPoint3DIdeaRSOpenModel] = Field(default=None, alias="point1OfSideBoundary1")
    point2_of_side_boundary1: Optional[Geometry3DPoint3DIdeaRSOpenModel] = Field(default=None, alias="point2OfSideBoundary1")
    end_face_normal1: Optional[Geometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="endFaceNormal1")
    point1_of_side_boundary2: Optional[Geometry3DPoint3DIdeaRSOpenModel] = Field(default=None, alias="point1OfSideBoundary2")
    point2_of_side_boundary2: Optional[Geometry3DPoint3DIdeaRSOpenModel] = Field(default=None, alias="point2OfSideBoundary2")
    __properties: ClassVar[List[str]] = ["plate1Id", "plate2Id", "radius", "point1OfSideBoundary1", "point2OfSideBoundary1", "endFaceNormal1", "point1OfSideBoundary2", "point2OfSideBoundary2"]

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
        """Create an instance of ConnectionBendDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of point1_of_side_boundary1
        if self.point1_of_side_boundary1:
            _dict['point1OfSideBoundary1'] = self.point1_of_side_boundary1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of point2_of_side_boundary1
        if self.point2_of_side_boundary1:
            _dict['point2OfSideBoundary1'] = self.point2_of_side_boundary1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_face_normal1
        if self.end_face_normal1:
            _dict['endFaceNormal1'] = self.end_face_normal1.to_dict()
        # override the default output from pydantic by calling `to_dict()` of point1_of_side_boundary2
        if self.point1_of_side_boundary2:
            _dict['point1OfSideBoundary2'] = self.point1_of_side_boundary2.to_dict()
        # override the default output from pydantic by calling `to_dict()` of point2_of_side_boundary2
        if self.point2_of_side_boundary2:
            _dict['point2OfSideBoundary2'] = self.point2_of_side_boundary2.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConnectionBendDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plate1Id": obj.get("plate1Id"),
            "plate2Id": obj.get("plate2Id"),
            "radius": obj.get("radius"),
            "point1OfSideBoundary1": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["point1OfSideBoundary1"]) if obj.get("point1OfSideBoundary1") is not None else None,
            "point2OfSideBoundary1": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["point2OfSideBoundary1"]) if obj.get("point2OfSideBoundary1") is not None else None,
            "endFaceNormal1": Geometry3DVector3DIdeaRSOpenModel.from_dict(obj["endFaceNormal1"]) if obj.get("endFaceNormal1") is not None else None,
            "point1OfSideBoundary2": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["point1OfSideBoundary2"]) if obj.get("point1OfSideBoundary2") is not None else None,
            "point2OfSideBoundary2": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["point2OfSideBoundary2"]) if obj.get("point2OfSideBoundary2") is not None else None
        })
        return _obj


