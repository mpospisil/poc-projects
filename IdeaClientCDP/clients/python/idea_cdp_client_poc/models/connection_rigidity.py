# coding: utf-8

"""
    ConDesignProposer API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ConnectionRigidity(int, Enum):
    """
    ConnectionRigidity
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_4 = 4
    NUMBER_8 = 8
    NUMBER_9 = 9
    NUMBER_16 = 16
    NUMBER_18 = 18
    NUMBER_32 = 32
    NUMBER_36 = 36

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConnectionRigidity from a JSON string"""
        return cls(json.loads(json_str))


