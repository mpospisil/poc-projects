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
from openapi_client.models.idea_rs_open_model_connection_cut_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel
from openapi_client.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel
from openapi_client.models.idea_rs_open_model_reference_element_idea_rs_open_model import IdeaRSOpenModelReferenceElementIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel
    """ # noqa: E501
    name: Optional[StrictStr] = None
    plates: Optional[List[IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel]] = None
    cross_section_type: Optional[StrictStr] = Field(default=None, alias="crossSectionType")
    mprl_name: Optional[StrictStr] = Field(default=None, alias="mprlName")
    original_model_id: Optional[StrictStr] = Field(default=None, alias="originalModelId")
    cuts: Optional[List[IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel]] = None
    is_added: Optional[StrictBool] = Field(default=None, alias="isAdded")
    added_member_length: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="addedMemberLength")
    is_negative_object: Optional[StrictBool] = Field(default=None, alias="isNegativeObject")
    added_member: Optional[IdeaRSOpenModelReferenceElementIdeaRSOpenModel] = Field(default=None, alias="addedMember")
    mirror_y: Optional[StrictBool] = Field(default=None, alias="mirrorY")
    ref_line_in_center_of_gravity: Optional[StrictBool] = Field(default=None, alias="refLineInCenterOfGravity")
    is_bearing_member: Optional[StrictBool] = Field(default=None, alias="isBearingMember")
    auto_add_cut_by_workplane: Optional[StrictBool] = Field(default=None, alias="autoAddCutByWorkplane")
    id: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["name", "plates", "crossSectionType", "mprlName", "originalModelId", "cuts", "isAdded", "addedMemberLength", "isNegativeObject", "addedMember", "mirrorY", "refLineInCenterOfGravity", "isBearingMember", "autoAddCutByWorkplane", "id"]

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
        """Create an instance of IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in plates (list)
        _items = []
        if self.plates:
            for _item in self.plates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['plates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cuts (list)
        _items = []
        if self.cuts:
            for _item in self.cuts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cuts'] = _items
        # override the default output from pydantic by calling `to_dict()` of added_member
        if self.added_member:
            _dict['addedMember'] = self.added_member.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if plates (nullable) is None
        # and model_fields_set contains the field
        if self.plates is None and "plates" in self.model_fields_set:
            _dict['plates'] = None

        # set to None if cross_section_type (nullable) is None
        # and model_fields_set contains the field
        if self.cross_section_type is None and "cross_section_type" in self.model_fields_set:
            _dict['crossSectionType'] = None

        # set to None if mprl_name (nullable) is None
        # and model_fields_set contains the field
        if self.mprl_name is None and "mprl_name" in self.model_fields_set:
            _dict['mprlName'] = None

        # set to None if original_model_id (nullable) is None
        # and model_fields_set contains the field
        if self.original_model_id is None and "original_model_id" in self.model_fields_set:
            _dict['originalModelId'] = None

        # set to None if cuts (nullable) is None
        # and model_fields_set contains the field
        if self.cuts is None and "cuts" in self.model_fields_set:
            _dict['cuts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "plates": [IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.from_dict(_item) for _item in obj["plates"]] if obj.get("plates") is not None else None,
            "crossSectionType": obj.get("crossSectionType"),
            "mprlName": obj.get("mprlName"),
            "originalModelId": obj.get("originalModelId"),
            "cuts": [IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel.from_dict(_item) for _item in obj["cuts"]] if obj.get("cuts") is not None else None,
            "isAdded": obj.get("isAdded"),
            "addedMemberLength": obj.get("addedMemberLength"),
            "isNegativeObject": obj.get("isNegativeObject"),
            "addedMember": IdeaRSOpenModelReferenceElementIdeaRSOpenModel.from_dict(obj["addedMember"]) if obj.get("addedMember") is not None else None,
            "mirrorY": obj.get("mirrorY"),
            "refLineInCenterOfGravity": obj.get("refLineInCenterOfGravity"),
            "isBearingMember": obj.get("isBearingMember"),
            "autoAddCutByWorkplane": obj.get("autoAddCutByWorkplane"),
            "id": obj.get("id")
        })
        return _obj


