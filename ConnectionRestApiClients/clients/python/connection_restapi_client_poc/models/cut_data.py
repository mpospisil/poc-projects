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
from connection_restapi_client_poc.models.cut_orientation import CutOrientation
from connection_restapi_client_poc.models.point3_d import Point3D
from connection_restapi_client_poc.models.vector3_d import Vector3D
from typing import Optional, Set
from typing_extensions import Self

class CutData(BaseModel):
    """
    Provides data of the cut beam
    """ # noqa: E501
    plane_point: Optional[Point3D] = Field(default=None, alias="planePoint")
    normal_vector: Optional[Vector3D] = Field(default=None, alias="normalVector")
    direction: Optional[CutOrientation] = None
    offset: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Offset - shift of cut")
    __properties: ClassVar[List[str]] = ["planePoint", "normalVector", "direction", "offset"]

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
        """Create an instance of CutData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of plane_point
        if self.plane_point:
            _dict['planePoint'] = self.plane_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of normal_vector
        if self.normal_vector:
            _dict['normalVector'] = self.normal_vector.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CutData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "planePoint": Point3D.from_dict(obj["planePoint"]) if obj.get("planePoint") is not None else None,
            "normalVector": Vector3D.from_dict(obj["normalVector"]) if obj.get("normalVector") is not None else None,
            "direction": obj.get("direction"),
            "offset": obj.get("offset")
        })
        return _obj

