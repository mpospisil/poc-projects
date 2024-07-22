# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_cut_data_idea_rs_open_model import IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionCutDataIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel(
                plane_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, ),
                normal_vector = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                direction = 'Default',
                offset = 1.337
            )
        else:
            return IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionCutDataIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionCutDataIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
