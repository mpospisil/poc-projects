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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin(BaseModel):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin
    """ # noqa: E501
    edge_plate: Optional[StrictStr] = Field(default=None, alias="edgePlate")
    surface_plate: Optional[StrictStr] = Field(default=None, alias="surfacePlate")
    edge_index: Optional[StrictInt] = Field(default=None, alias="edgeIndex")
    surface_index: Optional[StrictInt] = Field(default=None, alias="surfaceIndex")
    weld_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="weldSize")
    weld_type_code: Optional[StrictStr] = Field(default=None, alias="weldTypeCode")
    weld_material_name: Optional[StrictStr] = Field(default=None, alias="weldMaterialName")
    is_hollow_or_uncoiled_section: Optional[StrictBool] = Field(default=None, alias="isHollow_OrUncoiledSection")
    __properties: ClassVar[List[str]] = ["edgePlate", "surfacePlate", "edgeIndex", "surfaceIndex", "weldSize", "weldTypeCode", "weldMaterialName", "isHollow_OrUncoiledSection"]

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
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin from a JSON string"""
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
        # set to None if edge_plate (nullable) is None
        # and model_fields_set contains the field
        if self.edge_plate is None and "edge_plate" in self.model_fields_set:
            _dict['edgePlate'] = None

        # set to None if surface_plate (nullable) is None
        # and model_fields_set contains the field
        if self.surface_plate is None and "surface_plate" in self.model_fields_set:
            _dict['surfacePlate'] = None

        # set to None if weld_type_code (nullable) is None
        # and model_fields_set contains the field
        if self.weld_type_code is None and "weld_type_code" in self.model_fields_set:
            _dict['weldTypeCode'] = None

        # set to None if weld_material_name (nullable) is None
        # and model_fields_set contains the field
        if self.weld_material_name is None and "weld_material_name" in self.model_fields_set:
            _dict['weldMaterialName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edgePlate": obj.get("edgePlate"),
            "surfacePlate": obj.get("surfacePlate"),
            "edgeIndex": obj.get("edgeIndex"),
            "surfaceIndex": obj.get("surfaceIndex"),
            "weldSize": obj.get("weldSize"),
            "weldTypeCode": obj.get("weldTypeCode"),
            "weldMaterialName": obj.get("weldMaterialName"),
            "isHollow_OrUncoiledSection": obj.get("isHollow_OrUncoiledSection")
        })
        return _obj


