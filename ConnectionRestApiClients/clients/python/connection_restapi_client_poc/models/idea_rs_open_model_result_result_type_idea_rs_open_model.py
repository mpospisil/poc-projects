# coding: utf-8

"""
    Connection Rest API 1.2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IdeaRSOpenModelResultResultTypeIdeaRSOpenModel(str, Enum):
    """
    IdeaRSOpenModelResultResultTypeIdeaRSOpenModel
    """

    """
    allowed enum values
    """
    INTERNALFORCES = 'InternalForces'
    DEFORMATION = 'Deformation'
    CROSSSECTIONNLA = 'CrossSectionNLA'
    CROSSSECTIONTA = 'CrossSectionTA'
    INTERACTIONDIAGRAM = 'InteractionDiagram'
    CROSSSECTIONMESH = 'CrossSectionMesh'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdeaRSOpenModelResultResultTypeIdeaRSOpenModel from a JSON string"""
        return cls(json.loads(json_str))


