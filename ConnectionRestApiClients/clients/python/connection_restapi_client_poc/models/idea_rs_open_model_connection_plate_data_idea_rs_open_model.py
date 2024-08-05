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
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel
    """ # noqa: E501
    name: Optional[StrictStr] = None
    thickness: Optional[Union[StrictFloat, StrictInt]] = None
    material: Optional[StrictStr] = None
    outline_points: Optional[List[IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel]] = Field(default=None, alias="outlinePoints")
    origin: Optional[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel] = None
    axis_x: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisX")
    axis_y: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisY")
    axis_z: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisZ")
    region: Optional[StrictStr] = None
    geometry: Optional[IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel] = None
    original_model_id: Optional[StrictStr] = Field(default=None, alias="originalModelId")
    is_negative_object: Optional[StrictBool] = Field(default=None, alias="isNegativeObject")
    id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["name", "thickness", "material", "outlinePoints", "origin", "axisX", "axisY", "axisZ", "region", "geometry", "originalModelId", "isNegativeObject", "id"]

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
        """Create an instance of IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in outline_points (list)
        _items = []
        if self.outline_points:
            for _item_outline_points in self.outline_points:
                if _item_outline_points:
                    _items.append(_item_outline_points.to_dict())
            _dict['outlinePoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of origin
        if self.origin:
            _dict['origin'] = self.origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_x
        if self.axis_x:
            _dict['axisX'] = self.axis_x.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_y
        if self.axis_y:
            _dict['axisY'] = self.axis_y.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_z
        if self.axis_z:
            _dict['axisZ'] = self.axis_z.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if outline_points (nullable) is None
        # and model_fields_set contains the field
        if self.outline_points is None and "outline_points" in self.model_fields_set:
            _dict['outlinePoints'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if original_model_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_model_id is None and "original_model_id" in self.model_fields_set:
            _dict['originalModelId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "thickness": obj.get("thickness"),
            "material": obj.get("material"),
            "outlinePoints": [IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel.from_dict(_item) for _item in obj["outlinePoints"]] if obj.get("outlinePoints") is not None else None,
            "origin": IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "axisX": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisX"]) if obj.get("axisX") is not None else None,
            "axisY": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisY"]) if obj.get("axisY") is not None else None,
            "axisZ": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisZ"]) if obj.get("axisZ") is not None else None,
            "region": obj.get("region"),
            "geometry": IdeaRSOpenModelGeometry2DRegion2DIdeaRSOpenModel.from_dict(obj["geometry"]) if obj.get("geometry") is not None else None,
            "originalModelId": obj.get("originalModelId"),
            "isNegativeObject": obj.get("isNegativeObject"),
            "id": obj.get("id")
        })
        return _obj

