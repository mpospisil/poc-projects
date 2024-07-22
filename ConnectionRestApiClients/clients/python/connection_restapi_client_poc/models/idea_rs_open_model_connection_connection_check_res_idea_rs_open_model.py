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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_rs_open_model_connection_buckling_res_idea_rs_open_model import IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_anchor_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_bolt_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_concrete_block_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_plate_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_summary_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_weld_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_message_open_messages_idea_rs_open_model import IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel
    """ # noqa: E501
    check_res_summary: Optional[List[IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel]] = Field(default=None, alias="checkResSummary")
    check_res_plate: Optional[List[IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel]] = Field(default=None, alias="checkResPlate")
    check_res_weld: Optional[List[IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel]] = Field(default=None, alias="checkResWeld")
    check_res_bolt: Optional[List[IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel]] = Field(default=None, alias="checkResBolt")
    check_res_anchor: Optional[List[IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel]] = Field(default=None, alias="checkResAnchor")
    check_res_concrete_block: Optional[List[IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel]] = Field(default=None, alias="checkResConcreteBlock")
    buckling_results: Optional[List[IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel]] = Field(default=None, alias="bucklingResults")
    name: Optional[StrictStr] = None
    connection_id: Optional[StrictStr] = Field(default=None, alias="connectionID")
    id: Optional[StrictInt] = None
    messages: Optional[IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel] = None
    __properties: ClassVar[List[str]] = ["checkResSummary", "checkResPlate", "checkResWeld", "checkResBolt", "checkResAnchor", "checkResConcreteBlock", "bucklingResults", "name", "connectionID", "id", "messages"]

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
        """Create an instance of IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_summary (list)
        _items = []
        if self.check_res_summary:
            for _item in self.check_res_summary:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResSummary'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_plate (list)
        _items = []
        if self.check_res_plate:
            for _item in self.check_res_plate:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResPlate'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_weld (list)
        _items = []
        if self.check_res_weld:
            for _item in self.check_res_weld:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResWeld'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_bolt (list)
        _items = []
        if self.check_res_bolt:
            for _item in self.check_res_bolt:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResBolt'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_anchor (list)
        _items = []
        if self.check_res_anchor:
            for _item in self.check_res_anchor:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResAnchor'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in check_res_concrete_block (list)
        _items = []
        if self.check_res_concrete_block:
            for _item in self.check_res_concrete_block:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checkResConcreteBlock'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in buckling_results (list)
        _items = []
        if self.buckling_results:
            for _item in self.buckling_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bucklingResults'] = _items
        # override the default output from pydantic by calling `to_dict()` of messages
        if self.messages:
            _dict['messages'] = self.messages.to_dict()
        # set to None if check_res_summary (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_summary is None and "check_res_summary" in self.model_fields_set:
            _dict['checkResSummary'] = None

        # set to None if check_res_plate (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_plate is None and "check_res_plate" in self.model_fields_set:
            _dict['checkResPlate'] = None

        # set to None if check_res_weld (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_weld is None and "check_res_weld" in self.model_fields_set:
            _dict['checkResWeld'] = None

        # set to None if check_res_bolt (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_bolt is None and "check_res_bolt" in self.model_fields_set:
            _dict['checkResBolt'] = None

        # set to None if check_res_anchor (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_anchor is None and "check_res_anchor" in self.model_fields_set:
            _dict['checkResAnchor'] = None

        # set to None if check_res_concrete_block (nullable) is None
        # and model_fields_set contains the field
        if self.check_res_concrete_block is None and "check_res_concrete_block" in self.model_fields_set:
            _dict['checkResConcreteBlock'] = None

        # set to None if buckling_results (nullable) is None
        # and model_fields_set contains the field
        if self.buckling_results is None and "buckling_results" in self.model_fields_set:
            _dict['bucklingResults'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "checkResSummary": [IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResSummary"]] if obj.get("checkResSummary") is not None else None,
            "checkResPlate": [IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResPlate"]] if obj.get("checkResPlate") is not None else None,
            "checkResWeld": [IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResWeld"]] if obj.get("checkResWeld") is not None else None,
            "checkResBolt": [IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResBolt"]] if obj.get("checkResBolt") is not None else None,
            "checkResAnchor": [IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResAnchor"]] if obj.get("checkResAnchor") is not None else None,
            "checkResConcreteBlock": [IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel.from_dict(_item) for _item in obj["checkResConcreteBlock"]] if obj.get("checkResConcreteBlock") is not None else None,
            "bucklingResults": [IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel.from_dict(_item) for _item in obj["bucklingResults"]] if obj.get("bucklingResults") is not None else None,
            "name": obj.get("name"),
            "connectionID": obj.get("connectionID"),
            "id": obj.get("id"),
            "messages": IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel.from_dict(obj["messages"]) if obj.get("messages") is not None else None
        })
        return _obj


