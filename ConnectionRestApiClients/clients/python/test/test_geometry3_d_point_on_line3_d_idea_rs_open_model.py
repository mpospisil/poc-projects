# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.geometry3_d_point_on_line3_d_idea_rs_open_model import Geometry3DPointOnLine3DIdeaRSOpenModel

class TestGeometry3DPointOnLine3DIdeaRSOpenModel(unittest.TestCase):
    """Geometry3DPointOnLine3DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Geometry3DPointOnLine3DIdeaRSOpenModel:
        """Test Geometry3DPointOnLine3DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Geometry3DPointOnLine3DIdeaRSOpenModel`
        """
        model = Geometry3DPointOnLine3DIdeaRSOpenModel()
        if include_optional:
            return Geometry3DPointOnLine3DIdeaRSOpenModel(
                id = 56
            )
        else:
            return Geometry3DPointOnLine3DIdeaRSOpenModel(
        )
        """

    def testGeometry3DPointOnLine3DIdeaRSOpenModel(self):
        """Test Geometry3DPointOnLine3DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
