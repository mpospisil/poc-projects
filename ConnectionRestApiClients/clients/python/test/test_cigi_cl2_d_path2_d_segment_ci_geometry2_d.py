# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.cigi_cl2_d_path2_d_segment_ci_geometry2_d import CIGiCL2DPath2DSegmentCIGeometry2D

class TestCIGiCL2DPath2DSegmentCIGeometry2D(unittest.TestCase):
    """CIGiCL2DPath2DSegmentCIGeometry2D unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CIGiCL2DPath2DSegmentCIGeometry2D:
        """Test CIGiCL2DPath2DSegmentCIGeometry2D
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CIGiCL2DPath2DSegmentCIGeometry2D`
        """
        model = CIGiCL2DPath2DSegmentCIGeometry2D()
        if include_optional:
            return CIGiCL2DPath2DSegmentCIGeometry2D(
                end = ''
            )
        else:
            return CIGiCL2DPath2DSegmentCIGeometry2D(
        )
        """

    def testCIGiCL2DPath2DSegmentCIGeometry2D(self):
        """Test CIGiCL2DPath2DSegmentCIGeometry2D"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()