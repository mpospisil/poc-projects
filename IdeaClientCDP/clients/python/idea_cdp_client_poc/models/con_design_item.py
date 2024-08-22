# coding: utf-8

"""
    ConDesignProposer API 1.0

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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from idea_cdp_client_poc.models.con_design_data import ConDesignData
from idea_cdp_client_poc.models.load_transfer_type import LoadTransferType
from typing import Optional, Set
from typing_extensions import Self

class ConDesignItem(BaseModel):
    """
    ConDesignItem
    """ # noqa: E501
    picture_id: Optional[StrictStr] = Field(default=None, alias="pictureId")
    version: Optional[StrictStr] = None
    name: Annotated[str, Field(min_length=1, strict=True)]
    owner_id: Optional[StrictStr] = Field(default=None, alias="ownerId")
    design_code: Optional[StrictStr] = Field(default=None, alias="designCode")
    con_design_set_id: Optional[StrictStr] = Field(default=None, alias="conDesignSetId")
    con_design_item_id: Optional[StrictStr] = Field(default=None, alias="conDesignItemId")
    design_data: Optional[ConDesignData] = Field(default=None, alias="designData")
    company_name: Optional[StrictStr] = Field(default=None, alias="companyName")
    created: Optional[datetime] = None
    load_transfer_type: Optional[LoadTransferType] = Field(default=None, alias="loadTransferType")
    author_name: Optional[StrictStr] = Field(default=None, alias="authorName")
    activity: Optional[StrictBool] = None
    priority: Optional[StrictBool] = None
    imported: Optional[StrictBool] = None
    is_parametric: Optional[StrictBool] = Field(default=None, alias="isParametric")
    __properties: ClassVar[List[str]] = ["pictureId", "version", "name", "ownerId", "designCode", "conDesignSetId", "conDesignItemId", "designData", "companyName", "created", "loadTransferType", "authorName", "activity", "priority", "imported", "isParametric"]

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
        """Create an instance of ConDesignItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of design_data
        if self.design_data:
            _dict['designData'] = self.design_data.to_dict()
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if owner_id (nullable) is None
        # and model_fields_set contains the field
        if self.owner_id is None and "owner_id" in self.model_fields_set:
            _dict['ownerId'] = None

        # set to None if design_code (nullable) is None
        # and model_fields_set contains the field
        if self.design_code is None and "design_code" in self.model_fields_set:
            _dict['designCode'] = None

        # set to None if company_name (nullable) is None
        # and model_fields_set contains the field
        if self.company_name is None and "company_name" in self.model_fields_set:
            _dict['companyName'] = None

        # set to None if author_name (nullable) is None
        # and model_fields_set contains the field
        if self.author_name is None and "author_name" in self.model_fields_set:
            _dict['authorName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConDesignItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pictureId": obj.get("pictureId"),
            "version": obj.get("version"),
            "name": obj.get("name"),
            "ownerId": obj.get("ownerId"),
            "designCode": obj.get("designCode"),
            "conDesignSetId": obj.get("conDesignSetId"),
            "conDesignItemId": obj.get("conDesignItemId"),
            "designData": ConDesignData.from_dict(obj["designData"]) if obj.get("designData") is not None else None,
            "companyName": obj.get("companyName"),
            "created": obj.get("created"),
            "loadTransferType": obj.get("loadTransferType"),
            "authorName": obj.get("authorName"),
            "activity": obj.get("activity"),
            "priority": obj.get("priority"),
            "imported": obj.get("imported"),
            "isParametric": obj.get("isParametric")
        })
        return _obj


