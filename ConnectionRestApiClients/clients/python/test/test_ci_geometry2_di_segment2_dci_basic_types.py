# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.ci_geometry2_di_segment2_dci_basic_types import CIGeometry2DISegment2DCIBasicTypes

class TestCIGeometry2DISegment2DCIBasicTypes(unittest.TestCase):
    """CIGeometry2DISegment2DCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CIGeometry2DISegment2DCIBasicTypes:
        """Test CIGeometry2DISegment2DCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CIGeometry2DISegment2DCIBasicTypes`
        """
        model = CIGeometry2DISegment2DCIBasicTypes()
        if include_optional:
            return CIGeometry2DISegment2DCIBasicTypes(
                end_point = openapi_client.models.ci_geometry2_d_ida_com_point2_d_ci_basic_types.CI_Geometry2D_IdaComPoint2D-CI_BasicTypes(
                    x = 1.337, 
                    y = 1.337, )
            )
        else:
            return CIGeometry2DISegment2DCIBasicTypes(
        )
        """

    def testCIGeometry2DISegment2DCIBasicTypes(self):
        """Test CIGeometry2DISegment2DCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
