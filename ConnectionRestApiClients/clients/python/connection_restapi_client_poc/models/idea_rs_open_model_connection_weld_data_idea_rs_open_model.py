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
from connection_restapi_client_poc.models.idea_rs_open_model_connection_weld_type_idea_rs_open_model import IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_reference_element_idea_rs_open_model import IdeaRSOpenModelReferenceElementIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    thickness: Optional[Union[StrictFloat, StrictInt]] = None
    material: Optional[StrictStr] = None
    weld_material: Optional[IdeaRSOpenModelReferenceElementIdeaRSOpenModel] = Field(default=None, alias="weldMaterial")
    weld_type: Optional[IdeaRSOpenModelConnectionWeldTypeIdeaRSOpenModel] = Field(default=None, alias="weldType")
    connected_part_ids: Optional[List[StrictStr]] = Field(default=None, alias="connectedPartIds")
    start: Optional[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel] = None
    end: Optional[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel] = None
    __properties: ClassVar[List[str]] = ["id", "name", "thickness", "material", "weldMaterial", "weldType", "connectedPartIds", "start", "end"]

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
        """Create an instance of IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of weld_material
        if self.weld_material:
            _dict['weldMaterial'] = self.weld_material.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start
        if self.start:
            _dict['start'] = self.start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end
        if self.end:
            _dict['end'] = self.end.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if connected_part_ids (nullable) is None
        # and model_fields_set contains the field
        if self.connected_part_ids is None and "connected_part_ids" in self.model_fields_set:
            _dict['connectedPartIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "thickness": obj.get("thickness"),
            "material": obj.get("material"),
            "weldMaterial": IdeaRSOpenModelReferenceElementIdeaRSOpenModel.from_dict(obj["weldMaterial"]) if obj.get("weldMaterial") is not None else None,
            "weldType": obj.get("weldType"),
            "connectedPartIds": obj.get("connectedPartIds"),
            "start": IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.from_dict(obj["start"]) if obj.get("start") is not None else None,
            "end": IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.from_dict(obj["end"]) if obj.get("end") is not None else None
        })
        return _obj


