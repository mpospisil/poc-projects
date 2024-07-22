# coding: utf-8

"""
    Connection Rest API 1.2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_rs_open_model_result_loading_idea_rs_open_model import IdeaRSOpenModelResultLoadingIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_result_result_on_member_idea_rs_open_model import IdeaRSOpenModelResultResultOnMemberIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel
    """ # noqa: E501
    loading: Optional[IdeaRSOpenModelResultLoadingIdeaRSOpenModel] = None
    members: Optional[List[IdeaRSOpenModelResultResultOnMemberIdeaRSOpenModel]] = None
    __properties: ClassVar[List[str]] = ["loading", "members"]

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
        """Create an instance of IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of loading
        if self.loading:
            _dict['loading'] = self.loading.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item in self.members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members'] = _items
        # set to None if members (nullable) is None
        # and model_fields_set contains the field
        if self.members is None and "members" in self.model_fields_set:
            _dict['members'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loading": IdeaRSOpenModelResultLoadingIdeaRSOpenModel.from_dict(obj["loading"]) if obj.get("loading") is not None else None,
            "members": [IdeaRSOpenModelResultResultOnMemberIdeaRSOpenModel.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None
        })
        return _obj


