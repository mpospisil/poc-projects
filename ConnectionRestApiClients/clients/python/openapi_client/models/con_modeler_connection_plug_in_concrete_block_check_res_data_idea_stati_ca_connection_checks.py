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
from openapi_client.models.ci_geometry2_di_region2_dci_basic_types import CIGeometry2DIRegion2DCIBasicTypes
from openapi_client.models.cigi_cl2_d_path2_d_segment_ci_geometry2_d import CIGiCL2DPath2DSegmentCIGeometry2D
from openapi_client.models.idea_stati_ca_connection_basic_types_data_crt_comp_check_isci_basic_types import IdeaStatiCaConnectionBasicTypesDataCrtCompCheckISCIBasicTypes
from typing import Optional, Set
from typing_extensions import Self

class ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    fjd: Optional[Union[StrictFloat, StrictInt]] = None
    average_stress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="averageStress")
    nsd: Optional[Union[StrictFloat, StrictInt]] = None
    aeff: Optional[Union[StrictFloat, StrictInt]] = None
    aeff_center_gravity: Optional[StrictStr] = Field(default=None, alias="aeffCenterGravity")
    center_tension: Optional[StrictStr] = Field(default=None, alias="centerTension")
    center_compression: Optional[StrictStr] = Field(default=None, alias="centerCompression")
    aeff2: Optional[Union[StrictFloat, StrictInt]] = None
    supporting_regions: Optional[List[CIGeometry2DIRegion2DCIBasicTypes]] = Field(default=None, alias="supportingRegions")
    aeff_net: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="aeffNet")
    unity_check_stress: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="unityCheckStress")
    kj: Optional[Union[StrictFloat, StrictInt]] = None
    add_bearing_width: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="addBearingWidth")
    eff_area_of_base_plates: Optional[Dict[str, List[List[List[CIGiCL2DPath2DSegmentCIGeometry2D]]]]] = Field(default=None, alias="effAreaOfBasePlates")
    gamma_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaC")
    fck: Optional[Union[StrictFloat, StrictInt]] = None
    fck_factored: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fckFactored")
    betaj: Optional[Union[StrictFloat, StrictInt]] = None
    alpha_cc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="alphaCC")
    fc: Optional[Union[StrictFloat, StrictInt]] = None
    phi_crt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiCrt")
    omega_crt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="omegaCrt")
    fck_ext1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fckExt1")
    fck_ext2: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fckExt2")
    fck_ext: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="fckExt")
    crt_bearing_strength: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="crtBearingStrength")
    phi_c: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiC")
    psi_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="psi_SNIP")
    phi_b_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="phiB_SNIP")
    gamma_b_snip: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaB_SNIP")
    beta_c_chn: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaC_CHN")
    beta_l_chn: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="betaL_CHN")
    reinforced_concrete_pad: Optional[StrictBool] = Field(default=None, alias="reinforcedConcretePad")
    omega_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="omegaFactor")
    crt_comp_check_is: Optional[IdeaStatiCaConnectionBasicTypesDataCrtCompCheckISCIBasicTypes] = Field(default=None, alias="crtCompCheckIS")
    gamma_m0_is: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gammaM0_IS")
    base_plate_thickness: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="basePlateThickness")
    base_plate_fy: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="basePlateFy")
    eff_area_offset: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="effAreaOffset")
    concrete_grade: Optional[StrictStr] = Field(default=None, alias="concreteGrade")
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    check_status: Optional[StrictBool] = Field(default=None, alias="checkStatus")
    limit_check_status: Optional[StrictBool] = Field(default=None, alias="limitCheckStatus")
    load_case_id: Optional[StrictInt] = Field(default=None, alias="loadCaseId")
    load_case: Optional[StrictStr] = Field(default=None, alias="loadCase")
    max_unity_check: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUnityCheck")
    form: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["fjd", "averageStress", "nsd", "aeff", "aeffCenterGravity", "centerTension", "centerCompression", "aeff2", "supportingRegions", "aeffNet", "unityCheckStress", "kj", "addBearingWidth", "effAreaOfBasePlates", "gammaC", "fck", "fckFactored", "betaj", "alphaCC", "fc", "phiCrt", "omegaCrt", "fckExt1", "fckExt2", "fckExt", "crtBearingStrength", "phiC", "psi_SNIP", "phiB_SNIP", "gammaB_SNIP", "betaC_CHN", "betaL_CHN", "reinforcedConcretePad", "omegaFactor", "crtCompCheckIS", "gammaM0_IS", "basePlateThickness", "basePlateFy", "effAreaOffset", "concreteGrade", "id", "name", "checkStatus", "limitCheckStatus", "loadCaseId", "loadCase", "maxUnityCheck", "form"]

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
        """Create an instance of ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in supporting_regions (list)
        _items = []
        if self.supporting_regions:
            for _item in self.supporting_regions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['supportingRegions'] = _items
        # set to None if supporting_regions (nullable) is None
        # and model_fields_set contains the field
        if self.supporting_regions is None and "supporting_regions" in self.model_fields_set:
            _dict['supportingRegions'] = None

        # set to None if eff_area_of_base_plates (nullable) is None
        # and model_fields_set contains the field
        if self.eff_area_of_base_plates is None and "eff_area_of_base_plates" in self.model_fields_set:
            _dict['effAreaOfBasePlates'] = None

        # set to None if concrete_grade (nullable) is None
        # and model_fields_set contains the field
        if self.concrete_grade is None and "concrete_grade" in self.model_fields_set:
            _dict['concreteGrade'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if load_case (nullable) is None
        # and model_fields_set contains the field
        if self.load_case is None and "load_case" in self.model_fields_set:
            _dict['loadCase'] = None

        # set to None if form (nullable) is None
        # and model_fields_set contains the field
        if self.form is None and "form" in self.model_fields_set:
            _dict['form'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fjd": obj.get("fjd"),
            "averageStress": obj.get("averageStress"),
            "nsd": obj.get("nsd"),
            "aeff": obj.get("aeff"),
            "aeffCenterGravity": obj.get("aeffCenterGravity"),
            "centerTension": obj.get("centerTension"),
            "centerCompression": obj.get("centerCompression"),
            "aeff2": obj.get("aeff2"),
            "supportingRegions": [CIGeometry2DIRegion2DCIBasicTypes.from_dict(_item) for _item in obj["supportingRegions"]] if obj.get("supportingRegions") is not None else None,
            "aeffNet": obj.get("aeffNet"),
            "unityCheckStress": obj.get("unityCheckStress"),
            "kj": obj.get("kj"),
            "addBearingWidth": obj.get("addBearingWidth"),
            "effAreaOfBasePlates": obj.get("effAreaOfBasePlates"),
            "gammaC": obj.get("gammaC"),
            "fck": obj.get("fck"),
            "fckFactored": obj.get("fckFactored"),
            "betaj": obj.get("betaj"),
            "alphaCC": obj.get("alphaCC"),
            "fc": obj.get("fc"),
            "phiCrt": obj.get("phiCrt"),
            "omegaCrt": obj.get("omegaCrt"),
            "fckExt1": obj.get("fckExt1"),
            "fckExt2": obj.get("fckExt2"),
            "fckExt": obj.get("fckExt"),
            "crtBearingStrength": obj.get("crtBearingStrength"),
            "phiC": obj.get("phiC"),
            "psi_SNIP": obj.get("psi_SNIP"),
            "phiB_SNIP": obj.get("phiB_SNIP"),
            "gammaB_SNIP": obj.get("gammaB_SNIP"),
            "betaC_CHN": obj.get("betaC_CHN"),
            "betaL_CHN": obj.get("betaL_CHN"),
            "reinforcedConcretePad": obj.get("reinforcedConcretePad"),
            "omegaFactor": obj.get("omegaFactor"),
            "crtCompCheckIS": obj.get("crtCompCheckIS"),
            "gammaM0_IS": obj.get("gammaM0_IS"),
            "basePlateThickness": obj.get("basePlateThickness"),
            "basePlateFy": obj.get("basePlateFy"),
            "effAreaOffset": obj.get("effAreaOffset"),
            "concreteGrade": obj.get("concreteGrade"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "checkStatus": obj.get("checkStatus"),
            "limitCheckStatus": obj.get("limitCheckStatus"),
            "loadCaseId": obj.get("loadCaseId"),
            "loadCase": obj.get("loadCase"),
            "maxUnityCheck": obj.get("maxUnityCheck"),
            "form": obj.get("form")
        })
        return _obj


