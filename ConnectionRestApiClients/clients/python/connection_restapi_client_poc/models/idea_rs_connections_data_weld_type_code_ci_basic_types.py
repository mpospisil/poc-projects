# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes(str, Enum):
    """
    IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes
    """

    """
    allowed enum values
    """
    NOTSPECIFIED = 'notSpecified'
    FILLET = 'fillet'
    DOUBLEFILLET = 'doubleFillet'
    BEVEL = 'bevel'
    PJP = 'pjp'
    PJPREAR = 'pjpRear'
    LENGTHATHAUNCH = 'lengthAtHaunch'
    FILLETREAR = 'filletRear'
    CONTACT = 'contact'
    INTERMITTENT = 'intermittent'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdeaRSConnectionsDataWeldTypeCodeCIBasicTypes from a JSON string"""
        return cls(json.loads(json_str))


