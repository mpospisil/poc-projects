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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_base_template_conversion_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateBaseTemplateConversionIdeaStatiCaPlugin
from typing import Optional, Set
from typing_extensions import Self

class IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin(BaseModel):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin
    """ # noqa: E501
    conversions: Optional[List[IdeaStatiCaPluginApiConnectionRestModelModelTemplateBaseTemplateConversionIdeaStatiCaPlugin]] = None
    country_code: Optional[StrictStr] = Field(default=None, alias="countryCode")
    __properties: ClassVar[List[str]] = ["conversions", "countryCode"]

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
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conversions (list)
        _items = []
        if self.conversions:
            for _item in self.conversions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['conversions'] = _items
        # set to None if conversions (nullable) is None
        # and model_fields_set contains the field
        if self.conversions is None and "conversions" in self.model_fields_set:
            _dict['conversions'] = None

        # set to None if country_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_code is None and "country_code" in self.model_fields_set:
            _dict['countryCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelTemplateTemplateConversionsIdeaStatiCaPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "conversions": [IdeaStatiCaPluginApiConnectionRestModelModelTemplateBaseTemplateConversionIdeaStatiCaPlugin.from_dict(_item) for _item in obj["conversions"]] if obj.get("conversions") is not None else None,
            "countryCode": obj.get("countryCode")
        })
        return _obj


