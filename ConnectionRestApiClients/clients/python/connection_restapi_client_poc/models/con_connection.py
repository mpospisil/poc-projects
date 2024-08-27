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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.con_analysis_type_enum import ConAnalysisTypeEnum
from connection_restapi_client_poc.models.con_loading_options import ConLoadingOptions
from typing import Optional, Set
from typing_extensions import Self

class ConConnection(BaseModel):
    """
    ConConnection
    """ # noqa: E501
    id: Optional[StrictInt] = None
    identifier: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    analysis_type: Optional[ConAnalysisTypeEnum] = Field(default=None, alias="analysisType")
    load_options: Optional[ConLoadingOptions] = Field(default=None, alias="loadOptions")
    bearing_member_id: Optional[StrictInt] = Field(default=None, alias="bearingMemberId")
    is_calculated: Optional[StrictBool] = Field(default=None, alias="isCalculated")
    __properties: ClassVar[List[str]] = ["id", "identifier", "name", "description", "analysisType", "loadOptions", "bearingMemberId", "isCalculated"]

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
        """Create an instance of ConConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "is_calculated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of load_options
        if self.load_options:
            _dict['loadOptions'] = self.load_options.to_dict()
        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "identifier": obj.get("identifier"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "analysisType": obj.get("analysisType"),
            "loadOptions": ConLoadingOptions.from_dict(obj["loadOptions"]) if obj.get("loadOptions") is not None else None,
            "bearingMemberId": obj.get("bearingMemberId"),
            "isCalculated": obj.get("isCalculated")
        })
        return _obj


