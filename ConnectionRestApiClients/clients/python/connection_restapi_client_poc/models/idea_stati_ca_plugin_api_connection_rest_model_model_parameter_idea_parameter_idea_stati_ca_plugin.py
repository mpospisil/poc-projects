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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin(BaseModel):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin
    """ # noqa: E501
    key: Optional[StrictStr] = None
    expression: Optional[StrictStr] = None
    value: Optional[Any] = None
    unit: Optional[StrictStr] = None
    parameter_type: Optional[StrictStr] = Field(default=None, alias="parameterType")
    validation_expression: Optional[StrictStr] = Field(default=None, alias="validationExpression")
    description: Optional[StrictStr] = None
    validation_status: Optional[StrictStr] = Field(default=None, alias="validationStatus")
    is_visible: Optional[StrictBool] = Field(default=None, alias="isVisible")
    __properties: ClassVar[List[str]] = ["key", "expression", "value", "unit", "parameterType", "validationExpression", "description", "validationStatus", "isVisible"]

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
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin from a JSON string"""
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
        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if expression (nullable) is None
        # and model_fields_set contains the field
        if self.expression is None and "expression" in self.model_fields_set:
            _dict['expression'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if parameter_type (nullable) is None
        # and model_fields_set contains the field
        if self.parameter_type is None and "parameter_type" in self.model_fields_set:
            _dict['parameterType'] = None

        # set to None if validation_expression (nullable) is None
        # and model_fields_set contains the field
        if self.validation_expression is None and "validation_expression" in self.model_fields_set:
            _dict['validationExpression'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if validation_status (nullable) is None
        # and model_fields_set contains the field
        if self.validation_status is None and "validation_status" in self.model_fields_set:
            _dict['validationStatus'] = None

        # set to None if is_visible (nullable) is None
        # and model_fields_set contains the field
        if self.is_visible is None and "is_visible" in self.model_fields_set:
            _dict['isVisible'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "expression": obj.get("expression"),
            "value": obj.get("value"),
            "unit": obj.get("unit"),
            "parameterType": obj.get("parameterType"),
            "validationExpression": obj.get("validationExpression"),
            "description": obj.get("description"),
            "validationStatus": obj.get("validationStatus"),
            "isVisible": obj.get("isVisible")
        })
        return _obj

