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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_data_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin
from typing import Optional, Set
from typing_extensions import Self

class IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin(BaseModel):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
    """ # noqa: E501
    project_id: Optional[StrictStr] = Field(default=None, alias="projectId")
    project_info: Optional[IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin] = Field(default=None, alias="projectInfo")
    connections: Optional[List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin]] = None
    __properties: ClassVar[List[str]] = ["projectId", "projectInfo", "connections"]

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
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of project_info
        if self.project_info:
            _dict['projectInfo'] = self.project_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connections (list)
        _items = []
        if self.connections:
            for _item in self.connections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['connections'] = _items
        # set to None if connections (nullable) is None
        # and model_fields_set contains the field
        if self.connections is None and "connections" in self.model_fields_set:
            _dict['connections'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "projectId": obj.get("projectId"),
            "projectInfo": IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin.from_dict(obj["projectInfo"]) if obj.get("projectInfo") is not None else None,
            "connections": [IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.from_dict(_item) for _item in obj["connections"]] if obj.get("connections") is not None else None
        })
        return _obj


