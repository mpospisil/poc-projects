# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin(str, Enum):
    """
    IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin
    """

    """
    allowed enum values
    """
    STRESS_STRAIN = 'Stress_Strain'
    STIFFNESS = 'Stiffness'
    CAPACITY_DESIGN = 'Capacity_Design'
    FATIGUES = 'Fatigues'
    TOTAL_DESIGN = 'Total_Design'
    HORIZONTALTYING = 'HorizontalTying'
    CAPACITYLOADLEVELS = 'CapacityLoadLevels'
    FIRERESTANCE = 'FireRestance'
    BUCKLING = 'Buckling'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin from a JSON string"""
        return cls(json.loads(json_str))

