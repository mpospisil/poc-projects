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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from idea_cdp_client_poc.models.connection_rigidity import ConnectionRigidity
from idea_cdp_client_poc.models.continuity_type import ContinuityType
from idea_cdp_client_poc.models.css_data import CssData
from typing import Optional, Set
from typing_extensions import Self

class BearingMemberData(BaseModel):
    """
    BearingMemberData
    """ # noqa: E501
    operation_id: Optional[StrictInt] = Field(default=None, alias="operationId")
    order: Optional[StrictInt] = None
    inclination: Optional[Union[StrictFloat, StrictInt]] = None
    continuity_type: Optional[ContinuityType] = Field(default=None, alias="continuityType")
    css_meta_data: Optional[CssData] = Field(default=None, alias="cssMetaData")
    rigidity: Optional[ConnectionRigidity] = None
    static_behaviour: Optional[StrictInt] = Field(default=None, alias="staticBehaviour")
    __properties: ClassVar[List[str]] = ["operationId", "order", "inclination", "continuityType", "cssMetaData", "rigidity", "staticBehaviour"]

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
        """Create an instance of BearingMemberData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of css_meta_data
        if self.css_meta_data:
            _dict['cssMetaData'] = self.css_meta_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BearingMemberData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operationId": obj.get("operationId"),
            "order": obj.get("order"),
            "inclination": obj.get("inclination"),
            "continuityType": obj.get("continuityType"),
            "cssMetaData": CssData.from_dict(obj["cssMetaData"]) if obj.get("cssMetaData") is not None else None,
            "rigidity": obj.get("rigidity"),
            "staticBehaviour": obj.get("staticBehaviour")
        })
        return _obj


