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
from connection_restapi_client_poc.models.point2_d import Point2D
from connection_restapi_client_poc.models.point3_d import Point3D
from connection_restapi_client_poc.models.vector3_d import Vector3D
from typing import Optional, Set
from typing_extensions import Self

class ConcreteBlockData(BaseModel):
    """
    Provides data of the single concrete block
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Plate unique ID")
    name: Optional[StrictStr] = Field(default=None, description="Name of the concrete block")
    depth: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Depth of the concrete block")
    material: Optional[StrictStr] = Field(default=None, description="Name of the material")
    center: Optional[Point3D] = None
    outline_points: Optional[List[Point2D]] = Field(default=None, description="Outline points", alias="outlinePoints")
    origin: Optional[Point3D] = None
    axis_x: Optional[Vector3D] = Field(default=None, alias="axisX")
    axis_y: Optional[Vector3D] = Field(default=None, alias="axisY")
    axis_z: Optional[Vector3D] = Field(default=None, alias="axisZ")
    region: Optional[StrictStr] = Field(default=None, description="Geometry of the concrete block in svg format")
    original_model_id: Optional[StrictStr] = Field(default=None, description="Get or set the identification in the original model  In the case of the imported connection from another application", alias="originalModelId")
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
        """Create an instance of ConcreteBlockData from a JSON string"""
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
            for _item in self.outline_points:
                if _item:
                    _items.append(_item.to_dict())
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
        """Create an instance of ConcreteBlockData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "depth": obj.get("depth"),
            "material": obj.get("material"),
            "center": Point3D.from_dict(obj["center"]) if obj.get("center") is not None else None,
            "outlinePoints": [Point2D.from_dict(_item) for _item in obj["outlinePoints"]] if obj.get("outlinePoints") is not None else None,
            "origin": Point3D.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "axisX": Vector3D.from_dict(obj["axisX"]) if obj.get("axisX") is not None else None,
            "axisY": Vector3D.from_dict(obj["axisY"]) if obj.get("axisY") is not None else None,
            "axisZ": Vector3D.from_dict(obj["axisZ"]) if obj.get("axisZ") is not None else None,
            "region": obj.get("region"),
            "originalModelId": obj.get("originalModelId")
        })
        return _obj


