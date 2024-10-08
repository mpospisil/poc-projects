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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ideastatica_connection_api.models.open_model import OpenModel
from ideastatica_connection_api.models.open_model_result import OpenModelResult
from typing import Optional, Set
from typing_extensions import Self

class OpenModelContainer(BaseModel):
    """
    OpenModelContainer is used to keep structural data and results of a finite element analysis in one place.  The main reason is easier moving (passing) pass the instance of OpenModel and corresponding instace of OpenModelResults.
    """ # noqa: E501
    open_model: Optional[OpenModel] = Field(default=None, alias="openModel")
    open_model_result: Optional[OpenModelResult] = Field(default=None, alias="openModelResult")
    __properties: ClassVar[List[str]] = ["openModel", "openModelResult"]

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
        """Create an instance of OpenModelContainer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of open_model
        if self.open_model:
            _dict['openModel'] = self.open_model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of open_model_result
        if self.open_model_result:
            _dict['openModelResult'] = self.open_model_result.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OpenModelContainer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "openModel": OpenModel.from_dict(obj["openModel"]) if obj.get("openModel") is not None else None,
            "openModelResult": OpenModelResult.from_dict(obj["openModelResult"]) if obj.get("openModelResult") is not None else None
        })
        return _obj


