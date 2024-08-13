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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.geometry2_d_point2_d_idea_rs_open_model import Geometry2DPoint2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model import Geometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry3_d_vector3_d_idea_rs_open_model import Geometry3DVector3DIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class ConnectionConcreteBlockDataIdeaRSOpenModel(BaseModel):
    """
    ConnectionConcreteBlockDataIdeaRSOpenModel
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    depth: Optional[Union[StrictFloat, StrictInt]] = None
    material: Optional[StrictStr] = None
    center: Optional[Geometry3DPoint3DIdeaRSOpenModel] = None
    outline_points: Optional[List[Geometry2DPoint2DIdeaRSOpenModel]] = Field(default=None, alias="outlinePoints")
    origin: Optional[Geometry3DPoint3DIdeaRSOpenModel] = None
    axis_x: Optional[Geometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisX")
    axis_y: Optional[Geometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisY")
    axis_z: Optional[Geometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisZ")
    region: Optional[StrictStr] = None
    original_model_id: Optional[StrictStr] = Field(default=None, alias="originalModelId")
    __properties: ClassVar[List[str]] = ["id", "name", "depth", "material", "center", "outlinePoints", "origin", "axisX", "axisY", "axisZ", "region", "originalModelId"]

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
        """Create an instance of ConnectionConcreteBlockDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of center
        if self.center:
            _dict['center'] = self.center.to_dict()
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
        """Create an instance of ConnectionConcreteBlockDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "depth": obj.get("depth"),
            "material": obj.get("material"),
            "center": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["center"]) if obj.get("center") is not None else None,
            "outlinePoints": [Geometry2DPoint2DIdeaRSOpenModel.from_dict(_item) for _item in obj["outlinePoints"]] if obj.get("outlinePoints") is not None else None,
            "origin": Geometry3DPoint3DIdeaRSOpenModel.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "axisX": Geometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisX"]) if obj.get("axisX") is not None else None,
            "axisY": Geometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisY"]) if obj.get("axisY") is not None else None,
            "axisZ": Geometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisZ"]) if obj.get("axisZ") is not None else None,
            "region": obj.get("region"),
            "originalModelId": obj.get("originalModelId")
        })
        return _obj

