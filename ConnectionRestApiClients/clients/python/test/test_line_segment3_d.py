# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.line_segment3_d import LineSegment3D

class TestLineSegment3D(unittest.TestCase):
    """LineSegment3D unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LineSegment3D:
        """Test LineSegment3D
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LineSegment3D`
        """
        model = LineSegment3D()
        if include_optional:
            return LineSegment3D(
                id = 56
            )
        else:
            return LineSegment3D(
        )
        """

    def testLineSegment3D(self):
        """Test LineSegment3D"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
