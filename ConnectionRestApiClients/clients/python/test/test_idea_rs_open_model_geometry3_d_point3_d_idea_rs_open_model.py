# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection-restapi-client-poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model import IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel

class TestIdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel:
        """Test IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel(
                x = 1.337,
                y = 1.337,
                z = 1.337,
                id = 56
            )
        else:
            return IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelGeometry3DPoint3DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
