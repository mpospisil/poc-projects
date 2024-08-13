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
from connection_restapi_client_poc.models.analysis_check_res_data_idea_stati_ca_connection_checks import AnalysisCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.base_plate_shear_check_res_data_idea_stati_ca_connection_checks import BasePlateShearCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_idea_stati_ca_connection_checks import BoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_info_idea_stati_ca_connection_checks import BoltCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.bolt_check_res_data_timber_idea_stati_ca_connection_checks import BoltCheckResDataTimberIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.buckling_check_data_idea_stati_ca_connection_checks import BucklingCheckDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.concrete_block_check_res_data_idea_stati_ca_connection_checks import ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.cost_estimation_results_idea_stati_ca_connection_checks import CostEstimationResultsIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.fatigue_bolt_check_res_data_idea_stati_ca_connection_checks import FatigueBoltCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.fatigue_check_res_data_idea_stati_ca_connection_checks import FatigueCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_code_type_ci_basic_types import IdeaRSWsLibCssServiceCodeTypeCIBasicTypes
from connection_restapi_client_poc.models.pin_check_res_data_idea_stati_ca_connection_checks import PinCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_local_deformation_idea_stati_ca_connection_checks import PlateCheckLocalDeformationIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_res_data_idea_stati_ca_connection_checks import PlateCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.plate_check_res_data_info_idea_stati_ca_connection_checks import PlateCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.project_check_res_data_idea_stati_ca_connection_checks import ProjectCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.stiffness_chek_data_idea_stati_ca_connection_checks import StiffnessChekDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.summary_check_res_data_idea_stati_ca_connection_checks import SummaryCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_check_res_data_idea_stati_ca_connection_checks import WeldCheckResDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_check_res_data_info_idea_stati_ca_connection_checks import WeldCheckResDataInfoIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.weld_data_load_level_idea_stati_ca_connection_checks import WeldDataLoadLevelIdeaStatiCaConnectionChecks
from typing import Optional, Set
from typing_extensions import Self

class CheckResultsDataIdeaStatiCaConnectionChecks(BaseModel):
    """
    CheckResultsDataIdeaStatiCaConnectionChecks
    """ # noqa: E501
    code_type: Optional[IdeaRSWsLibCssServiceCodeTypeCIBasicTypes] = Field(default=None, alias="codeType")
    plates_deformation: Optional[Dict[str, PlateCheckLocalDeformationIdeaStatiCaConnectionChecks]] = Field(default=None, alias="platesDeformation")
    plates: Optional[Dict[str, PlateCheckResDataIdeaStatiCaConnectionChecks]] = None
    plates_info: Optional[Dict[str, PlateCheckResDataInfoIdeaStatiCaConnectionChecks]] = Field(default=None, alias="platesInfo")
    bolts: Optional[Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]] = None
    bolts_info: Optional[Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]] = Field(default=None, alias="boltsInfo")
    bolts_anchor: Optional[Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="boltsAnchor")
    bolts_anchor_compression: Optional[Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="boltsAnchorCompression")
    bolts_anchor_info: Optional[Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]] = Field(default=None, alias="boltsAnchorInfo")
    pre_bolts: Optional[Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="preBolts")
    pre_bolts_info: Optional[Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]] = Field(default=None, alias="preBoltsInfo")
    bolt_check_res_data_timbers: Optional[Dict[str, BoltCheckResDataTimberIdeaStatiCaConnectionChecks]] = Field(default=None, alias="boltCheckResDataTimbers")
    pins: Optional[Dict[str, PinCheckResDataIdeaStatiCaConnectionChecks]] = None
    welds: Optional[Dict[str, WeldCheckResDataIdeaStatiCaConnectionChecks]] = None
    welds_info: Optional[Dict[str, WeldCheckResDataInfoIdeaStatiCaConnectionChecks]] = Field(default=None, alias="weldsInfo")
    fatigue_checks: Optional[Dict[str, FatigueCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="fatigueChecks")
    fatigue_sections_checks: Optional[Dict[str, FatigueCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="fatigueSectionsChecks")
    fatigue_bolt_checks: Optional[Dict[str, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="fatigueBoltChecks")
    fatigue_anchor_checks: Optional[Dict[str, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="fatigueAnchorChecks")
    fatigue_welds: Optional[Dict[str, WeldCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="fatigueWelds")
    concrete_blocks: Optional[Dict[str, ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="concreteBlocks")
    summary: Optional[Dict[str, SummaryCheckResDataIdeaStatiCaConnectionChecks]] = None
    project_item: Optional[Dict[str, ProjectCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="projectItem")
    analysis: Optional[Dict[str, AnalysisCheckResDataIdeaStatiCaConnectionChecks]] = None
    total_capacity: Optional[Dict[str, AnalysisCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="totalCapacity")
    base_plate_shear: Optional[Dict[str, BasePlateShearCheckResDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="basePlateShear")
    stiffnesess: Optional[Dict[str, StiffnessChekDataIdeaStatiCaConnectionChecks]] = None
    stiffnesess_axial: Optional[Dict[str, StiffnessChekDataIdeaStatiCaConnectionChecks]] = Field(default=None, alias="stiffnesessAxial")
    bucklings: Optional[Dict[str, BucklingCheckDataIdeaStatiCaConnectionChecks]] = None
    nonconformity: Optional[List[SummaryCheckResDataIdeaStatiCaConnectionChecks]] = None
    cost_estimation_results: Optional[CostEstimationResultsIdeaStatiCaConnectionChecks] = Field(default=None, alias="costEstimationResults")
    welds_data_load_levels: Optional[Dict[str, WeldDataLoadLevelIdeaStatiCaConnectionChecks]] = Field(default=None, alias="weldsDataLoadLevels")
    __properties: ClassVar[List[str]] = ["codeType", "platesDeformation", "plates", "platesInfo", "bolts", "boltsInfo", "boltsAnchor", "boltsAnchorCompression", "boltsAnchorInfo", "preBolts", "preBoltsInfo", "boltCheckResDataTimbers", "pins", "welds", "weldsInfo", "fatigueChecks", "fatigueSectionsChecks", "fatigueBoltChecks", "fatigueAnchorChecks", "fatigueWelds", "concreteBlocks", "summary", "projectItem", "analysis", "totalCapacity", "basePlateShear", "stiffnesess", "stiffnesessAxial", "bucklings", "nonconformity", "costEstimationResults", "weldsDataLoadLevels"]

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
        """Create an instance of CheckResultsDataIdeaStatiCaConnectionChecks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in plates_deformation (dict)
        _field_dict = {}
        if self.plates_deformation:
            for _key_plates_deformation in self.plates_deformation:
                if self.plates_deformation[_key_plates_deformation]:
                    _field_dict[_key_plates_deformation] = self.plates_deformation[_key_plates_deformation].to_dict()
            _dict['platesDeformation'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in plates (dict)
        _field_dict = {}
        if self.plates:
            for _key_plates in self.plates:
                if self.plates[_key_plates]:
                    _field_dict[_key_plates] = self.plates[_key_plates].to_dict()
            _dict['plates'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in plates_info (dict)
        _field_dict = {}
        if self.plates_info:
            for _key_plates_info in self.plates_info:
                if self.plates_info[_key_plates_info]:
                    _field_dict[_key_plates_info] = self.plates_info[_key_plates_info].to_dict()
            _dict['platesInfo'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolts (dict)
        _field_dict = {}
        if self.bolts:
            for _key_bolts in self.bolts:
                if self.bolts[_key_bolts]:
                    _field_dict[_key_bolts] = self.bolts[_key_bolts].to_dict()
            _dict['bolts'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolts_info (dict)
        _field_dict = {}
        if self.bolts_info:
            for _key_bolts_info in self.bolts_info:
                if self.bolts_info[_key_bolts_info]:
                    _field_dict[_key_bolts_info] = self.bolts_info[_key_bolts_info].to_dict()
            _dict['boltsInfo'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolts_anchor (dict)
        _field_dict = {}
        if self.bolts_anchor:
            for _key_bolts_anchor in self.bolts_anchor:
                if self.bolts_anchor[_key_bolts_anchor]:
                    _field_dict[_key_bolts_anchor] = self.bolts_anchor[_key_bolts_anchor].to_dict()
            _dict['boltsAnchor'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolts_anchor_compression (dict)
        _field_dict = {}
        if self.bolts_anchor_compression:
            for _key_bolts_anchor_compression in self.bolts_anchor_compression:
                if self.bolts_anchor_compression[_key_bolts_anchor_compression]:
                    _field_dict[_key_bolts_anchor_compression] = self.bolts_anchor_compression[_key_bolts_anchor_compression].to_dict()
            _dict['boltsAnchorCompression'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolts_anchor_info (dict)
        _field_dict = {}
        if self.bolts_anchor_info:
            for _key_bolts_anchor_info in self.bolts_anchor_info:
                if self.bolts_anchor_info[_key_bolts_anchor_info]:
                    _field_dict[_key_bolts_anchor_info] = self.bolts_anchor_info[_key_bolts_anchor_info].to_dict()
            _dict['boltsAnchorInfo'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in pre_bolts (dict)
        _field_dict = {}
        if self.pre_bolts:
            for _key_pre_bolts in self.pre_bolts:
                if self.pre_bolts[_key_pre_bolts]:
                    _field_dict[_key_pre_bolts] = self.pre_bolts[_key_pre_bolts].to_dict()
            _dict['preBolts'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in pre_bolts_info (dict)
        _field_dict = {}
        if self.pre_bolts_info:
            for _key_pre_bolts_info in self.pre_bolts_info:
                if self.pre_bolts_info[_key_pre_bolts_info]:
                    _field_dict[_key_pre_bolts_info] = self.pre_bolts_info[_key_pre_bolts_info].to_dict()
            _dict['preBoltsInfo'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bolt_check_res_data_timbers (dict)
        _field_dict = {}
        if self.bolt_check_res_data_timbers:
            for _key_bolt_check_res_data_timbers in self.bolt_check_res_data_timbers:
                if self.bolt_check_res_data_timbers[_key_bolt_check_res_data_timbers]:
                    _field_dict[_key_bolt_check_res_data_timbers] = self.bolt_check_res_data_timbers[_key_bolt_check_res_data_timbers].to_dict()
            _dict['boltCheckResDataTimbers'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in pins (dict)
        _field_dict = {}
        if self.pins:
            for _key_pins in self.pins:
                if self.pins[_key_pins]:
                    _field_dict[_key_pins] = self.pins[_key_pins].to_dict()
            _dict['pins'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in welds (dict)
        _field_dict = {}
        if self.welds:
            for _key_welds in self.welds:
                if self.welds[_key_welds]:
                    _field_dict[_key_welds] = self.welds[_key_welds].to_dict()
            _dict['welds'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in welds_info (dict)
        _field_dict = {}
        if self.welds_info:
            for _key_welds_info in self.welds_info:
                if self.welds_info[_key_welds_info]:
                    _field_dict[_key_welds_info] = self.welds_info[_key_welds_info].to_dict()
            _dict['weldsInfo'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in fatigue_checks (dict)
        _field_dict = {}
        if self.fatigue_checks:
            for _key_fatigue_checks in self.fatigue_checks:
                if self.fatigue_checks[_key_fatigue_checks]:
                    _field_dict[_key_fatigue_checks] = self.fatigue_checks[_key_fatigue_checks].to_dict()
            _dict['fatigueChecks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in fatigue_sections_checks (dict)
        _field_dict = {}
        if self.fatigue_sections_checks:
            for _key_fatigue_sections_checks in self.fatigue_sections_checks:
                if self.fatigue_sections_checks[_key_fatigue_sections_checks]:
                    _field_dict[_key_fatigue_sections_checks] = self.fatigue_sections_checks[_key_fatigue_sections_checks].to_dict()
            _dict['fatigueSectionsChecks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in fatigue_bolt_checks (dict)
        _field_dict = {}
        if self.fatigue_bolt_checks:
            for _key_fatigue_bolt_checks in self.fatigue_bolt_checks:
                if self.fatigue_bolt_checks[_key_fatigue_bolt_checks]:
                    _field_dict[_key_fatigue_bolt_checks] = self.fatigue_bolt_checks[_key_fatigue_bolt_checks].to_dict()
            _dict['fatigueBoltChecks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in fatigue_anchor_checks (dict)
        _field_dict = {}
        if self.fatigue_anchor_checks:
            for _key_fatigue_anchor_checks in self.fatigue_anchor_checks:
                if self.fatigue_anchor_checks[_key_fatigue_anchor_checks]:
                    _field_dict[_key_fatigue_anchor_checks] = self.fatigue_anchor_checks[_key_fatigue_anchor_checks].to_dict()
            _dict['fatigueAnchorChecks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in fatigue_welds (dict)
        _field_dict = {}
        if self.fatigue_welds:
            for _key_fatigue_welds in self.fatigue_welds:
                if self.fatigue_welds[_key_fatigue_welds]:
                    _field_dict[_key_fatigue_welds] = self.fatigue_welds[_key_fatigue_welds].to_dict()
            _dict['fatigueWelds'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in concrete_blocks (dict)
        _field_dict = {}
        if self.concrete_blocks:
            for _key_concrete_blocks in self.concrete_blocks:
                if self.concrete_blocks[_key_concrete_blocks]:
                    _field_dict[_key_concrete_blocks] = self.concrete_blocks[_key_concrete_blocks].to_dict()
            _dict['concreteBlocks'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in summary (dict)
        _field_dict = {}
        if self.summary:
            for _key_summary in self.summary:
                if self.summary[_key_summary]:
                    _field_dict[_key_summary] = self.summary[_key_summary].to_dict()
            _dict['summary'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in project_item (dict)
        _field_dict = {}
        if self.project_item:
            for _key_project_item in self.project_item:
                if self.project_item[_key_project_item]:
                    _field_dict[_key_project_item] = self.project_item[_key_project_item].to_dict()
            _dict['projectItem'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in analysis (dict)
        _field_dict = {}
        if self.analysis:
            for _key_analysis in self.analysis:
                if self.analysis[_key_analysis]:
                    _field_dict[_key_analysis] = self.analysis[_key_analysis].to_dict()
            _dict['analysis'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in total_capacity (dict)
        _field_dict = {}
        if self.total_capacity:
            for _key_total_capacity in self.total_capacity:
                if self.total_capacity[_key_total_capacity]:
                    _field_dict[_key_total_capacity] = self.total_capacity[_key_total_capacity].to_dict()
            _dict['totalCapacity'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in base_plate_shear (dict)
        _field_dict = {}
        if self.base_plate_shear:
            for _key_base_plate_shear in self.base_plate_shear:
                if self.base_plate_shear[_key_base_plate_shear]:
                    _field_dict[_key_base_plate_shear] = self.base_plate_shear[_key_base_plate_shear].to_dict()
            _dict['basePlateShear'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in stiffnesess (dict)
        _field_dict = {}
        if self.stiffnesess:
            for _key_stiffnesess in self.stiffnesess:
                if self.stiffnesess[_key_stiffnesess]:
                    _field_dict[_key_stiffnesess] = self.stiffnesess[_key_stiffnesess].to_dict()
            _dict['stiffnesess'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in stiffnesess_axial (dict)
        _field_dict = {}
        if self.stiffnesess_axial:
            for _key_stiffnesess_axial in self.stiffnesess_axial:
                if self.stiffnesess_axial[_key_stiffnesess_axial]:
                    _field_dict[_key_stiffnesess_axial] = self.stiffnesess_axial[_key_stiffnesess_axial].to_dict()
            _dict['stiffnesessAxial'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in bucklings (dict)
        _field_dict = {}
        if self.bucklings:
            for _key_bucklings in self.bucklings:
                if self.bucklings[_key_bucklings]:
                    _field_dict[_key_bucklings] = self.bucklings[_key_bucklings].to_dict()
            _dict['bucklings'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each item in nonconformity (list)
        _items = []
        if self.nonconformity:
            for _item_nonconformity in self.nonconformity:
                if _item_nonconformity:
                    _items.append(_item_nonconformity.to_dict())
            _dict['nonconformity'] = _items
        # override the default output from pydantic by calling `to_dict()` of cost_estimation_results
        if self.cost_estimation_results:
            _dict['costEstimationResults'] = self.cost_estimation_results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in welds_data_load_levels (dict)
        _field_dict = {}
        if self.welds_data_load_levels:
            for _key_welds_data_load_levels in self.welds_data_load_levels:
                if self.welds_data_load_levels[_key_welds_data_load_levels]:
                    _field_dict[_key_welds_data_load_levels] = self.welds_data_load_levels[_key_welds_data_load_levels].to_dict()
            _dict['weldsDataLoadLevels'] = _field_dict
        # set to None if plates_deformation (nullable) is None
        # and model_fields_set contains the field
        if self.plates_deformation is None and "plates_deformation" in self.model_fields_set:
            _dict['platesDeformation'] = None

        # set to None if plates (nullable) is None
        # and model_fields_set contains the field
        if self.plates is None and "plates" in self.model_fields_set:
            _dict['plates'] = None

        # set to None if plates_info (nullable) is None
        # and model_fields_set contains the field
        if self.plates_info is None and "plates_info" in self.model_fields_set:
            _dict['platesInfo'] = None

        # set to None if bolts (nullable) is None
        # and model_fields_set contains the field
        if self.bolts is None and "bolts" in self.model_fields_set:
            _dict['bolts'] = None

        # set to None if bolts_info (nullable) is None
        # and model_fields_set contains the field
        if self.bolts_info is None and "bolts_info" in self.model_fields_set:
            _dict['boltsInfo'] = None

        # set to None if bolts_anchor (nullable) is None
        # and model_fields_set contains the field
        if self.bolts_anchor is None and "bolts_anchor" in self.model_fields_set:
            _dict['boltsAnchor'] = None

        # set to None if bolts_anchor_compression (nullable) is None
        # and model_fields_set contains the field
        if self.bolts_anchor_compression is None and "bolts_anchor_compression" in self.model_fields_set:
            _dict['boltsAnchorCompression'] = None

        # set to None if bolts_anchor_info (nullable) is None
        # and model_fields_set contains the field
        if self.bolts_anchor_info is None and "bolts_anchor_info" in self.model_fields_set:
            _dict['boltsAnchorInfo'] = None

        # set to None if pre_bolts (nullable) is None
        # and model_fields_set contains the field
        if self.pre_bolts is None and "pre_bolts" in self.model_fields_set:
            _dict['preBolts'] = None

        # set to None if pre_bolts_info (nullable) is None
        # and model_fields_set contains the field
        if self.pre_bolts_info is None and "pre_bolts_info" in self.model_fields_set:
            _dict['preBoltsInfo'] = None

        # set to None if bolt_check_res_data_timbers (nullable) is None
        # and model_fields_set contains the field
        if self.bolt_check_res_data_timbers is None and "bolt_check_res_data_timbers" in self.model_fields_set:
            _dict['boltCheckResDataTimbers'] = None

        # set to None if pins (nullable) is None
        # and model_fields_set contains the field
        if self.pins is None and "pins" in self.model_fields_set:
            _dict['pins'] = None

        # set to None if welds (nullable) is None
        # and model_fields_set contains the field
        if self.welds is None and "welds" in self.model_fields_set:
            _dict['welds'] = None

        # set to None if welds_info (nullable) is None
        # and model_fields_set contains the field
        if self.welds_info is None and "welds_info" in self.model_fields_set:
            _dict['weldsInfo'] = None

        # set to None if fatigue_checks (nullable) is None
        # and model_fields_set contains the field
        if self.fatigue_checks is None and "fatigue_checks" in self.model_fields_set:
            _dict['fatigueChecks'] = None

        # set to None if fatigue_sections_checks (nullable) is None
        # and model_fields_set contains the field
        if self.fatigue_sections_checks is None and "fatigue_sections_checks" in self.model_fields_set:
            _dict['fatigueSectionsChecks'] = None

        # set to None if fatigue_bolt_checks (nullable) is None
        # and model_fields_set contains the field
        if self.fatigue_bolt_checks is None and "fatigue_bolt_checks" in self.model_fields_set:
            _dict['fatigueBoltChecks'] = None

        # set to None if fatigue_anchor_checks (nullable) is None
        # and model_fields_set contains the field
        if self.fatigue_anchor_checks is None and "fatigue_anchor_checks" in self.model_fields_set:
            _dict['fatigueAnchorChecks'] = None

        # set to None if fatigue_welds (nullable) is None
        # and model_fields_set contains the field
        if self.fatigue_welds is None and "fatigue_welds" in self.model_fields_set:
            _dict['fatigueWelds'] = None

        # set to None if concrete_blocks (nullable) is None
        # and model_fields_set contains the field
        if self.concrete_blocks is None and "concrete_blocks" in self.model_fields_set:
            _dict['concreteBlocks'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if project_item (nullable) is None
        # and model_fields_set contains the field
        if self.project_item is None and "project_item" in self.model_fields_set:
            _dict['projectItem'] = None

        # set to None if analysis (nullable) is None
        # and model_fields_set contains the field
        if self.analysis is None and "analysis" in self.model_fields_set:
            _dict['analysis'] = None

        # set to None if total_capacity (nullable) is None
        # and model_fields_set contains the field
        if self.total_capacity is None and "total_capacity" in self.model_fields_set:
            _dict['totalCapacity'] = None

        # set to None if base_plate_shear (nullable) is None
        # and model_fields_set contains the field
        if self.base_plate_shear is None and "base_plate_shear" in self.model_fields_set:
            _dict['basePlateShear'] = None

        # set to None if stiffnesess (nullable) is None
        # and model_fields_set contains the field
        if self.stiffnesess is None and "stiffnesess" in self.model_fields_set:
            _dict['stiffnesess'] = None

        # set to None if stiffnesess_axial (nullable) is None
        # and model_fields_set contains the field
        if self.stiffnesess_axial is None and "stiffnesess_axial" in self.model_fields_set:
            _dict['stiffnesessAxial'] = None

        # set to None if bucklings (nullable) is None
        # and model_fields_set contains the field
        if self.bucklings is None and "bucklings" in self.model_fields_set:
            _dict['bucklings'] = None

        # set to None if nonconformity (nullable) is None
        # and model_fields_set contains the field
        if self.nonconformity is None and "nonconformity" in self.model_fields_set:
            _dict['nonconformity'] = None

        # set to None if welds_data_load_levels (nullable) is None
        # and model_fields_set contains the field
        if self.welds_data_load_levels is None and "welds_data_load_levels" in self.model_fields_set:
            _dict['weldsDataLoadLevels'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CheckResultsDataIdeaStatiCaConnectionChecks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "codeType": obj.get("codeType"),
            "platesDeformation": dict(
                (_k, PlateCheckLocalDeformationIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["platesDeformation"].items()
            )
            if obj.get("platesDeformation") is not None
            else None,
            "plates": dict(
                (_k, PlateCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["plates"].items()
            )
            if obj.get("plates") is not None
            else None,
            "platesInfo": dict(
                (_k, PlateCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["platesInfo"].items()
            )
            if obj.get("platesInfo") is not None
            else None,
            "bolts": dict(
                (_k, BoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["bolts"].items()
            )
            if obj.get("bolts") is not None
            else None,
            "boltsInfo": dict(
                (_k, BoltCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["boltsInfo"].items()
            )
            if obj.get("boltsInfo") is not None
            else None,
            "boltsAnchor": dict(
                (_k, BoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["boltsAnchor"].items()
            )
            if obj.get("boltsAnchor") is not None
            else None,
            "boltsAnchorCompression": dict(
                (_k, BoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["boltsAnchorCompression"].items()
            )
            if obj.get("boltsAnchorCompression") is not None
            else None,
            "boltsAnchorInfo": dict(
                (_k, BoltCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["boltsAnchorInfo"].items()
            )
            if obj.get("boltsAnchorInfo") is not None
            else None,
            "preBolts": dict(
                (_k, BoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["preBolts"].items()
            )
            if obj.get("preBolts") is not None
            else None,
            "preBoltsInfo": dict(
                (_k, BoltCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["preBoltsInfo"].items()
            )
            if obj.get("preBoltsInfo") is not None
            else None,
            "boltCheckResDataTimbers": dict(
                (_k, BoltCheckResDataTimberIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["boltCheckResDataTimbers"].items()
            )
            if obj.get("boltCheckResDataTimbers") is not None
            else None,
            "pins": dict(
                (_k, PinCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["pins"].items()
            )
            if obj.get("pins") is not None
            else None,
            "welds": dict(
                (_k, WeldCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["welds"].items()
            )
            if obj.get("welds") is not None
            else None,
            "weldsInfo": dict(
                (_k, WeldCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["weldsInfo"].items()
            )
            if obj.get("weldsInfo") is not None
            else None,
            "fatigueChecks": dict(
                (_k, FatigueCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["fatigueChecks"].items()
            )
            if obj.get("fatigueChecks") is not None
            else None,
            "fatigueSectionsChecks": dict(
                (_k, FatigueCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["fatigueSectionsChecks"].items()
            )
            if obj.get("fatigueSectionsChecks") is not None
            else None,
            "fatigueBoltChecks": dict(
                (_k, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["fatigueBoltChecks"].items()
            )
            if obj.get("fatigueBoltChecks") is not None
            else None,
            "fatigueAnchorChecks": dict(
                (_k, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["fatigueAnchorChecks"].items()
            )
            if obj.get("fatigueAnchorChecks") is not None
            else None,
            "fatigueWelds": dict(
                (_k, WeldCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["fatigueWelds"].items()
            )
            if obj.get("fatigueWelds") is not None
            else None,
            "concreteBlocks": dict(
                (_k, ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["concreteBlocks"].items()
            )
            if obj.get("concreteBlocks") is not None
            else None,
            "summary": dict(
                (_k, SummaryCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["summary"].items()
            )
            if obj.get("summary") is not None
            else None,
            "projectItem": dict(
                (_k, ProjectCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["projectItem"].items()
            )
            if obj.get("projectItem") is not None
            else None,
            "analysis": dict(
                (_k, AnalysisCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["analysis"].items()
            )
            if obj.get("analysis") is not None
            else None,
            "totalCapacity": dict(
                (_k, AnalysisCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["totalCapacity"].items()
            )
            if obj.get("totalCapacity") is not None
            else None,
            "basePlateShear": dict(
                (_k, BasePlateShearCheckResDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["basePlateShear"].items()
            )
            if obj.get("basePlateShear") is not None
            else None,
            "stiffnesess": dict(
                (_k, StiffnessChekDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["stiffnesess"].items()
            )
            if obj.get("stiffnesess") is not None
            else None,
            "stiffnesessAxial": dict(
                (_k, StiffnessChekDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["stiffnesessAxial"].items()
            )
            if obj.get("stiffnesessAxial") is not None
            else None,
            "bucklings": dict(
                (_k, BucklingCheckDataIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["bucklings"].items()
            )
            if obj.get("bucklings") is not None
            else None,
            "nonconformity": [SummaryCheckResDataIdeaStatiCaConnectionChecks.from_dict(_item) for _item in obj["nonconformity"]] if obj.get("nonconformity") is not None else None,
            "costEstimationResults": CostEstimationResultsIdeaStatiCaConnectionChecks.from_dict(obj["costEstimationResults"]) if obj.get("costEstimationResults") is not None else None,
            "weldsDataLoadLevels": dict(
                (_k, WeldDataLoadLevelIdeaStatiCaConnectionChecks.from_dict(_v))
                for _k, _v in obj["weldsDataLoadLevels"].items()
            )
            if obj.get("weldsDataLoadLevels") is not None
            else None
        })
        return _obj

