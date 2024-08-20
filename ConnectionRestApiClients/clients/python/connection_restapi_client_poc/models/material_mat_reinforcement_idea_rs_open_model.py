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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from connection_restapi_client_poc.models.geometry2_d_polygon2_d_idea_rs_open_model import Geometry2DPolygon2DIdeaRSOpenModel
from connection_restapi_client_poc.models.geometry2_d_temperature_curve2_d_idea_rs_open_model import Geometry2DTemperatureCurve2DIdeaRSOpenModel
from connection_restapi_client_poc.models.material_reinf_bar_surface_idea_rs_open_model import MaterialReinfBarSurfaceIdeaRSOpenModel
from connection_restapi_client_poc.models.material_thermal_conductivity_state_idea_rs_open_model import MaterialThermalConductivityStateIdeaRSOpenModel
from connection_restapi_client_poc.models.material_thermal_expansion_state_idea_rs_open_model import MaterialThermalExpansionStateIdeaRSOpenModel
from connection_restapi_client_poc.models.material_thermal_specific_heat_state_idea_rs_open_model import MaterialThermalSpecificHeatStateIdeaRSOpenModel
from connection_restapi_client_poc.models.material_thermal_strain_state_idea_rs_open_model import MaterialThermalStrainStateIdeaRSOpenModel
from connection_restapi_client_poc.models.material_thermal_stress_strain_state_idea_rs_open_model import MaterialThermalStressStrainStateIdeaRSOpenModel
from typing import Optional, Set
from typing_extensions import Self

class MaterialMatReinforcementIdeaRSOpenModel(BaseModel):
    """
    Material reinforcement base class
    """ # noqa: E501
    bar_surface: Optional[MaterialReinfBarSurfaceIdeaRSOpenModel] = Field(default=None, alias="barSurface")
    name: Optional[StrictStr] = Field(default=None, description="Name of material")
    load_from_library: Optional[StrictBool] = Field(default=None, description="Load from library - try override properties from library find material by name", alias="loadFromLibrary")
    e: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Young's modulus")
    g: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Shear modulus")
    poisson: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Poisson's ratio")
    unit_mass: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Unit weight", alias="unitMass")
    specific_heat: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Specific heat capacity", alias="specificHeat")
    thermal_expansion: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Thermal expansion", alias="thermalExpansion")
    thermal_conductivity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Thermal conductivity", alias="thermalConductivity")
    is_default_material: Optional[StrictBool] = Field(default=None, description="True if material is default material from the code", alias="isDefaultMaterial")
    order_in_code: Optional[StrictInt] = Field(default=None, description="Order of this material in the code", alias="orderInCode")
    state_of_thermal_expansion: Optional[MaterialThermalExpansionStateIdeaRSOpenModel] = Field(default=None, alias="stateOfThermalExpansion")
    state_of_thermal_conductivity: Optional[MaterialThermalConductivityStateIdeaRSOpenModel] = Field(default=None, alias="stateOfThermalConductivity")
    state_of_thermal_specific_heat: Optional[MaterialThermalSpecificHeatStateIdeaRSOpenModel] = Field(default=None, alias="stateOfThermalSpecificHeat")
    state_of_thermal_stress_strain: Optional[MaterialThermalStressStrainStateIdeaRSOpenModel] = Field(default=None, alias="stateOfThermalStressStrain")
    state_of_thermal_strain: Optional[MaterialThermalStrainStateIdeaRSOpenModel] = Field(default=None, alias="stateOfThermalStrain")
    user_thermal_specific_heat_curvature: Optional[Geometry2DPolygon2DIdeaRSOpenModel] = Field(default=None, alias="userThermalSpecificHeatCurvature")
    user_thermal_conductivity_curvature: Optional[Geometry2DPolygon2DIdeaRSOpenModel] = Field(default=None, alias="userThermalConductivityCurvature")
    user_thermal_expansion_curvature: Optional[Geometry2DPolygon2DIdeaRSOpenModel] = Field(default=None, alias="userThermalExpansionCurvature")
    user_thermal_strain_curvature: Optional[Geometry2DPolygon2DIdeaRSOpenModel] = Field(default=None, alias="userThermalStrainCurvature")
    user_thermal_stress_strain_curvature: Optional[List[Geometry2DTemperatureCurve2DIdeaRSOpenModel]] = Field(default=None, description="User-defined curvature for thermal stress,strain { Temperature = Θ[K], {x = ε[-], y = σ[Pa]}}", alias="userThermalStressStrainCurvature")
    id: Optional[StrictInt] = Field(default=None, description="Element Id")
    __properties: ClassVar[List[str]] = ["barSurface", "name", "loadFromLibrary", "e", "g", "poisson", "unitMass", "specificHeat", "thermalExpansion", "thermalConductivity", "isDefaultMaterial", "orderInCode", "stateOfThermalExpansion", "stateOfThermalConductivity", "stateOfThermalSpecificHeat", "stateOfThermalStressStrain", "stateOfThermalStrain", "userThermalSpecificHeatCurvature", "userThermalConductivityCurvature", "userThermalExpansionCurvature", "userThermalStrainCurvature", "userThermalStressStrainCurvature", "id"]

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
        """Create an instance of MaterialMatReinforcementIdeaRSOpenModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_thermal_specific_heat_curvature
        if self.user_thermal_specific_heat_curvature:
            _dict['userThermalSpecificHeatCurvature'] = self.user_thermal_specific_heat_curvature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_thermal_conductivity_curvature
        if self.user_thermal_conductivity_curvature:
            _dict['userThermalConductivityCurvature'] = self.user_thermal_conductivity_curvature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_thermal_expansion_curvature
        if self.user_thermal_expansion_curvature:
            _dict['userThermalExpansionCurvature'] = self.user_thermal_expansion_curvature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_thermal_strain_curvature
        if self.user_thermal_strain_curvature:
            _dict['userThermalStrainCurvature'] = self.user_thermal_strain_curvature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_thermal_stress_strain_curvature (list)
        _items = []
        if self.user_thermal_stress_strain_curvature:
            for _item_user_thermal_stress_strain_curvature in self.user_thermal_stress_strain_curvature:
                if _item_user_thermal_stress_strain_curvature:
                    _items.append(_item_user_thermal_stress_strain_curvature.to_dict())
            _dict['userThermalStressStrainCurvature'] = _items
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if user_thermal_stress_strain_curvature (nullable) is None
        # and model_fields_set contains the field
        if self.user_thermal_stress_strain_curvature is None and "user_thermal_stress_strain_curvature" in self.model_fields_set:
            _dict['userThermalStressStrainCurvature'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaterialMatReinforcementIdeaRSOpenModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "barSurface": obj.get("barSurface"),
            "name": obj.get("name"),
            "loadFromLibrary": obj.get("loadFromLibrary"),
            "e": obj.get("e"),
            "g": obj.get("g"),
            "poisson": obj.get("poisson"),
            "unitMass": obj.get("unitMass"),
            "specificHeat": obj.get("specificHeat"),
            "thermalExpansion": obj.get("thermalExpansion"),
            "thermalConductivity": obj.get("thermalConductivity"),
            "isDefaultMaterial": obj.get("isDefaultMaterial"),
            "orderInCode": obj.get("orderInCode"),
            "stateOfThermalExpansion": obj.get("stateOfThermalExpansion"),
            "stateOfThermalConductivity": obj.get("stateOfThermalConductivity"),
            "stateOfThermalSpecificHeat": obj.get("stateOfThermalSpecificHeat"),
            "stateOfThermalStressStrain": obj.get("stateOfThermalStressStrain"),
            "stateOfThermalStrain": obj.get("stateOfThermalStrain"),
            "userThermalSpecificHeatCurvature": Geometry2DPolygon2DIdeaRSOpenModel.from_dict(obj["userThermalSpecificHeatCurvature"]) if obj.get("userThermalSpecificHeatCurvature") is not None else None,
            "userThermalConductivityCurvature": Geometry2DPolygon2DIdeaRSOpenModel.from_dict(obj["userThermalConductivityCurvature"]) if obj.get("userThermalConductivityCurvature") is not None else None,
            "userThermalExpansionCurvature": Geometry2DPolygon2DIdeaRSOpenModel.from_dict(obj["userThermalExpansionCurvature"]) if obj.get("userThermalExpansionCurvature") is not None else None,
            "userThermalStrainCurvature": Geometry2DPolygon2DIdeaRSOpenModel.from_dict(obj["userThermalStrainCurvature"]) if obj.get("userThermalStrainCurvature") is not None else None,
            "userThermalStressStrainCurvature": [Geometry2DTemperatureCurve2DIdeaRSOpenModel.from_dict(_item) for _item in obj["userThermalStressStrainCurvature"]] if obj.get("userThermalStressStrainCurvature") is not None else None,
            "id": obj.get("id")
        })
        return _obj


