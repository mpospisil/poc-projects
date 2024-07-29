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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel
    """ # noqa: E501
    end_point: Optional[IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel] = Field(default=None, alias="endPoint")
    __properties: ClassVar[List[str]] = ["endPoint"]

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
        """Create an instance of IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of end_point
        if self.end_point:
            _dict['endPoint'] = self.end_point.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endPoint": IdeaRSOpenModelGeometry2DPoint2DIdeaRSOpenModel.from_dict(obj["endPoint"]) if obj.get("endPoint") is not None else None
        })
        return _obj


