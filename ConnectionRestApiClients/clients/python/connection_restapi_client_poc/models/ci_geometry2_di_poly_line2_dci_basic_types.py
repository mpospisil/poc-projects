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
from connection_restapi_client_poc.models.ci_geometry2_d_ida_com_point2_dci_basic_types import CIGeometry2DIdaComPoint2DCIBasicTypes
from connection_restapi_client_poc.models.ci_geometry2_di_segment2_dci_basic_types import CIGeometry2DISegment2DCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class CIGeometry2DIPolyLine2DCIBasicTypes(BaseModel):
    """
    CIGeometry2DIPolyLine2DCIBasicTypes
    """ # noqa: E501
    start_point: Optional[CIGeometry2DIdaComPoint2DCIBasicTypes] = Field(default=None, alias="startPoint")
    is_closed: Optional[StrictBool] = Field(default=None, alias="isClosed")
    segments: Optional[List[CIGeometry2DISegment2DCIBasicTypes]] = None
    length: Optional[Union[StrictFloat, StrictInt]] = None
    bounds: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["startPoint", "isClosed", "segments", "length", "bounds", "id"]

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
        """Create an instance of CIGeometry2DIPolyLine2DCIBasicTypes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_closed",
            "segments",
            "length",
            "bounds",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of start_point
        if self.start_point:
            _dict['startPoint'] = self.start_point.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in segments (list)
        _items = []
        if self.segments:
            for _item in self.segments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['segments'] = _items
        # set to None if segments (nullable) is None
        # and model_fields_set contains the field
        if self.segments is None and "segments" in self.model_fields_set:
            _dict['segments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CIGeometry2DIPolyLine2DCIBasicTypes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "startPoint": CIGeometry2DIdaComPoint2DCIBasicTypes.from_dict(obj["startPoint"]) if obj.get("startPoint") is not None else None,
            "isClosed": obj.get("isClosed"),
            "segments": [CIGeometry2DISegment2DCIBasicTypes.from_dict(_item) for _item in obj["segments"]] if obj.get("segments") is not None else None,
            "length": obj.get("length"),
            "bounds": obj.get("bounds"),
            "id": obj.get("id")
        })
        return _obj


