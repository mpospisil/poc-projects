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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_rs_open_model_parameters_bolt_shear_type_idea_rs_open_model import IdeaRSOpenModelParametersBoltShearTypeIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel(BaseModel):
    """
    IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel
    """ # noqa: E501
    bolt_assembly_ref: Optional[StrictStr] = Field(default=None, alias="boltAssemblyRef")
    id: Optional[StrictInt] = None
    is_anchor: Optional[StrictBool] = Field(default=None, alias="isAnchor")
    anchor_len: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="anchorLen")
    hole_diameter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="holeDiameter")
    diameter: Optional[Union[StrictFloat, StrictInt]] = None
    head_diameter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="headDiameter")
    diagonal_head_diameter: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="diagonalHeadDiameter")
    head_height: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="headHeight")
    bore_hole: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="boreHole")
    tensile_stress_area: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tensileStressArea")
    nut_thickness: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nutThickness")
    bolt_assembly_name: Optional[StrictStr] = Field(default=None, alias="boltAssemblyName")
    standard: Optional[StrictStr] = None
    material: Optional[StrictStr] = None
    origin: Optional[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel] = None
    axis_x: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisX")
    axis_y: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisY")
    axis_z: Optional[IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel] = Field(default=None, alias="axisZ")
    positions: Optional[List[IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel]] = None
    connected_plates: Optional[List[StrictInt]] = Field(default=None, alias="connectedPlates")
    connected_part_ids: Optional[List[StrictStr]] = Field(default=None, alias="connectedPartIds")
    shear_in_thread: Optional[StrictBool] = Field(default=None, alias="shearInThread")
    bolt_interaction: Optional[IdeaRSOpenModelParametersBoltShearTypeIdeaRSOpenModel] = Field(default=None, alias="boltInteraction")
    __properties: ClassVar[List[str]] = ["boltAssemblyRef", "id", "isAnchor", "anchorLen", "holeDiameter", "diameter", "headDiameter", "diagonalHeadDiameter", "headHeight", "boreHole", "tensileStressArea", "nutThickness", "boltAssemblyName", "standard", "material", "origin", "axisX", "axisY", "axisZ", "positions", "connectedPlates", "connectedPartIds", "shearInThread", "boltInteraction"]

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
        """Create an instance of IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of origin
        if self.origin:
            _dict['origin'] = self.origin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_x
        if self.axis_x:
            _dict['axisX'] = self.axis_x.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_y
        if self.axis_y:
            _dict['axisY'] = self.axis_y.to_dict()
        # override the default output from pydantic by calling `to_dict()` of axis_z
        if self.axis_z:
            _dict['axisZ'] = self.axis_z.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in positions (list)
        _items = []
        if self.positions:
            for _item in self.positions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['positions'] = _items
        # set to None if bolt_assembly_ref (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_assembly_ref is None and "bolt_assembly_ref" in self.model_fields_set:
            _dict['boltAssemblyRef'] = None

        # set to None if bolt_assembly_name (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_assembly_name is None and "bolt_assembly_name" in self.model_fields_set:
            _dict['boltAssemblyName'] = None

        # set to None if standard (nullable) is None
        # and model_fields_set contains the field
        if self.standard is None and "standard" in self.model_fields_set:
            _dict['standard'] = None

        # set to None if material (nullable) is None
        # and model_fields_set contains the field
        if self.material is None and "material" in self.model_fields_set:
            _dict['material'] = None

        # set to None if positions (nullable) is None
        # and model_fields_set contains the field
        if self.positions is None and "positions" in self.model_fields_set:
            _dict['positions'] = None

        # set to None if connected_plates (nullable) is None
        # and model_fields_set contains the field
        if self.connected_plates is None and "connected_plates" in self.model_fields_set:
            _dict['connectedPlates'] = None

        # set to None if connected_part_ids (nullable) is None
        # and model_fields_set contains the field
        if self.connected_part_ids is None and "connected_part_ids" in self.model_fields_set:
            _dict['connectedPartIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "boltAssemblyRef": obj.get("boltAssemblyRef"),
            "id": obj.get("id"),
            "isAnchor": obj.get("isAnchor"),
            "anchorLen": obj.get("anchorLen"),
            "holeDiameter": obj.get("holeDiameter"),
            "diameter": obj.get("diameter"),
            "headDiameter": obj.get("headDiameter"),
            "diagonalHeadDiameter": obj.get("diagonalHeadDiameter"),
            "headHeight": obj.get("headHeight"),
            "boreHole": obj.get("boreHole"),
            "tensileStressArea": obj.get("tensileStressArea"),
            "nutThickness": obj.get("nutThickness"),
            "boltAssemblyName": obj.get("boltAssemblyName"),
            "standard": obj.get("standard"),
            "material": obj.get("material"),
            "origin": IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.from_dict(obj["origin"]) if obj.get("origin") is not None else None,
            "axisX": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisX"]) if obj.get("axisX") is not None else None,
            "axisY": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisY"]) if obj.get("axisY") is not None else None,
            "axisZ": IdeaRSOpenModelGeometry3DVector3DIdeaRSOpenModel.from_dict(obj["axisZ"]) if obj.get("axisZ") is not None else None,
            "positions": [IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel.from_dict(_item) for _item in obj["positions"]] if obj.get("positions") is not None else None,
            "connectedPlates": obj.get("connectedPlates"),
            "connectedPartIds": obj.get("connectedPartIds"),
            "shearInThread": obj.get("shearInThread"),
            "boltInteraction": obj.get("boltInteraction")
        })
        return _obj


