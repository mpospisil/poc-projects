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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from idea_cdp_client_poc.models.con_design_item_lite import ConDesignItemLite
from typing import Optional, Set
from typing_extensions import Self

class ConDesignItemLitePaginatedConDesignItems(BaseModel):
    """
    ConDesignItemLitePaginatedConDesignItems
    """ # noqa: E501
    design_items: Optional[List[ConDesignItemLite]] = Field(default=None, alias="designItems")
    is_last_page: Optional[StrictBool] = Field(default=None, alias="isLastPage")
    page_size: Optional[StrictInt] = Field(default=None, alias="pageSize")
    total_items: Optional[StrictInt] = Field(default=None, alias="totalItems")
    __properties: ClassVar[List[str]] = ["designItems", "isLastPage", "pageSize", "totalItems"]

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
        """Create an instance of ConDesignItemLitePaginatedConDesignItems from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in design_items (list)
        _items = []
        if self.design_items:
            for _item in self.design_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['designItems'] = _items
        # set to None if design_items (nullable) is None
        # and model_fields_set contains the field
        if self.design_items is None and "design_items" in self.model_fields_set:
            _dict['designItems'] = None

        # set to None if is_last_page (nullable) is None
        # and model_fields_set contains the field
        if self.is_last_page is None and "is_last_page" in self.model_fields_set:
            _dict['isLastPage'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['pageSize'] = None

        # set to None if total_items (nullable) is None
        # and model_fields_set contains the field
        if self.total_items is None and "total_items" in self.model_fields_set:
            _dict['totalItems'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConDesignItemLitePaginatedConDesignItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "designItems": [ConDesignItemLite.from_dict(_item) for _item in obj["designItems"]] if obj.get("designItems") is not None else None,
            "isLastPage": obj.get("isLastPage"),
            "pageSize": obj.get("pageSize"),
            "totalItems": obj.get("totalItems")
        })
        return _obj


