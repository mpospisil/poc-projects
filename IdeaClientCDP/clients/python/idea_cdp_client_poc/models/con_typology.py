# coding: utf-8

"""
    ConDesignProposer API 9.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from idea_cdp_client_poc.models.bearing_member_data import BearingMemberData
from idea_cdp_client_poc.models.connected_member_data import ConnectedMemberData
from typing import Optional, Set
from typing_extensions import Self

class ConTypology(BaseModel):
    """
    ConTypology
    """ # noqa: E501
    bearing_member: Optional[BearingMemberData] = Field(default=None, alias="bearingMember")
    connected_members: Optional[List[ConnectedMemberData]] = Field(default=None, alias="connectedMembers")
    typology_code: Optional[StrictStr] = Field(default=None, alias="typologyCode")
    __properties: ClassVar[List[str]] = ["bearingMember", "connectedMembers", "typologyCode"]

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
        """Create an instance of ConTypology from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bearing_member
        if self.bearing_member:
            _dict['bearingMember'] = self.bearing_member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in connected_members (list)
        _items = []
        if self.connected_members:
            for _item in self.connected_members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['connectedMembers'] = _items
        # set to None if connected_members (nullable) is None
        # and model_fields_set contains the field
        if self.connected_members is None and "connected_members" in self.model_fields_set:
            _dict['connectedMembers'] = None

        # set to None if typology_code (nullable) is None
        # and model_fields_set contains the field
        if self.typology_code is None and "typology_code" in self.model_fields_set:
            _dict['typologyCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConTypology from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bearingMember": BearingMemberData.from_dict(obj["bearingMember"]) if obj.get("bearingMember") is not None else None,
            "connectedMembers": [ConnectedMemberData.from_dict(_item) for _item in obj["connectedMembers"]] if obj.get("connectedMembers") is not None else None,
            "typologyCode": obj.get("typologyCode")
        })
        return _obj


