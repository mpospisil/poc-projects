# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from connection_restapi_client_poc.models.idea_rs_connections_data_thin_plate_validity_criterion_ci_basic_types import IdeaRSConnectionsDataThinPlateValidityCriterionCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSConnectionsDataThinPlateValidityCIBasicTypes(BaseModel):
    """
    IdeaRSConnectionsDataThinPlateValidityCIBasicTypes
    """ # noqa: E501
    related_plate_name: Optional[StrictStr] = Field(default=None, alias="relatedPlateName")
    validity_criteria: Optional[List[IdeaRSConnectionsDataThinPlateValidityCriterionCIBasicTypes]] = Field(default=None, alias="validityCriteria")
    __properties: ClassVar[List[str]] = ["relatedPlateName", "validityCriteria"]

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
        """Create an instance of IdeaRSConnectionsDataThinPlateValidityCIBasicTypes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in validity_criteria (list)
        _items = []
        if self.validity_criteria:
            for _item in self.validity_criteria:
                if _item:
                    _items.append(_item.to_dict())
            _dict['validityCriteria'] = _items
        # set to None if related_plate_name (nullable) is None
        # and model_fields_set contains the field
        if self.related_plate_name is None and "related_plate_name" in self.model_fields_set:
            _dict['relatedPlateName'] = None

        # set to None if validity_criteria (nullable) is None
        # and model_fields_set contains the field
        if self.validity_criteria is None and "validity_criteria" in self.model_fields_set:
            _dict['validityCriteria'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSConnectionsDataThinPlateValidityCIBasicTypes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "relatedPlateName": obj.get("relatedPlateName"),
            "validityCriteria": [IdeaRSConnectionsDataThinPlateValidityCriterionCIBasicTypes.from_dict(_item) for _item in obj["validityCriteria"]] if obj.get("validityCriteria") is not None else None
        })
        return _obj


