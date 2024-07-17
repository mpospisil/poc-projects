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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.idea_rs_open_model_connection_bend_data_idea_rs_open_model import IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel
from openapi_client.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel
    """ # noqa: E501
    plates: Optional[List[IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel]] = None
    bends: Optional[List[IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel]] = None
    __properties: ClassVar[List[str]] = ["plates", "bends"]

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
        """Create an instance of IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bends (list)
        _items = []
        if self.bends:
            for _item in self.bends:
                if _item:
                    _items.append(_item.to_dict())
            _dict['bends'] = _items
        # set to None if plates (nullable) is None
        # and model_fields_set contains the field
        if self.plates is None and "plates" in self.model_fields_set:
            _dict['plates'] = None

        # set to None if bends (nullable) is None
        # and model_fields_set contains the field
        if self.bends is None and "bends" in self.model_fields_set:
            _dict['bends'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plates": [IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.from_dict(_item) for _item in obj["plates"]] if obj.get("plates") is not None else None,
            "bends": [IdeaRSOpenModelConnectionBendDataIdeaRSOpenModel.from_dict(_item) for _item in obj["bends"]] if obj.get("bends") is not None else None
        })
        return _obj


