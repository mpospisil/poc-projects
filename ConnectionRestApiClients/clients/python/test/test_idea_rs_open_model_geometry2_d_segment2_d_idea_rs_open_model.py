# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model import IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel

class TestIdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel:
        """Test IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel(
                end_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, )
            )
        else:
            return IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelGeometry2DSegment2DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
