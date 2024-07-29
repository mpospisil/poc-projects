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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin(BaseModel):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin
    """ # noqa: E501
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    project_number: Optional[StrictStr] = Field(default=None, alias="projectNumber")
    author: Optional[StrictStr] = None
    design_code: Optional[StrictStr] = Field(default=None, alias="designCode")
    var_date: Optional[datetime] = Field(default=None, alias="date")
    __properties: ClassVar[List[str]] = ["name", "description", "projectNumber", "author", "designCode", "date"]

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
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin from a JSON string"""
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

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if project_number (nullable) is None
        # and model_fields_set contains the field
        if self.project_number is None and "project_number" in self.model_fields_set:
            _dict['projectNumber'] = None

        # set to None if author (nullable) is None
        # and model_fields_set contains the field
        if self.author is None and "author" in self.model_fields_set:
            _dict['author'] = None

        # set to None if design_code (nullable) is None
        # and model_fields_set contains the field
        if self.design_code is None and "design_code" in self.model_fields_set:
            _dict['designCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "projectNumber": obj.get("projectNumber"),
            "author": obj.get("author"),
            "designCode": obj.get("designCode"),
            "date": obj.get("date")
        })
        return _obj


