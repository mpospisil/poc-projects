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


class IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel(str, Enum):
    """
    IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel
    """

    """
    allowed enum values
    """
    BOUNDINGBOX = 'BoundingBox'
    SURFACE = 'Surface'
    MITRE = 'Mitre'
    SURFACEALL = 'SurfaceAll'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdeaRSOpenModelConnectionCutMethodIdeaRSOpenModel from a JSON string"""
        return cls(json.loads(json_str))


