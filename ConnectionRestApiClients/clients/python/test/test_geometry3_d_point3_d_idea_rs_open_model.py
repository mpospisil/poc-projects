# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.geometry3_d_point3_d_idea_rs_open_model import Geometry3DPoint3DIdeaRSOpenModel

class TestGeometry3DPoint3DIdeaRSOpenModel(unittest.TestCase):
    """Geometry3DPoint3DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Geometry3DPoint3DIdeaRSOpenModel:
        """Test Geometry3DPoint3DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Geometry3DPoint3DIdeaRSOpenModel`
        """
        model = Geometry3DPoint3DIdeaRSOpenModel()
        if include_optional:
            return Geometry3DPoint3DIdeaRSOpenModel(
                x = 1.337,
                y = 1.337,
                z = 1.337,
                id = 56
            )
        else:
            return Geometry3DPoint3DIdeaRSOpenModel(
        )
        """

    def testGeometry3DPoint3DIdeaRSOpenModel(self):
        """Test Geometry3DPoint3DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
