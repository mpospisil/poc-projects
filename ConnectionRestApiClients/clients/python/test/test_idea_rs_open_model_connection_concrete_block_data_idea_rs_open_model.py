# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_concrete_block_data_idea_rs_open_model import IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel(
                id = 56,
                name = '',
                depth = 1.337,
                material = '',
                center = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, ),
                outline_points = [
                    connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                        x = 1.337, 
                        y = 1.337, )
                    ],
                origin = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, ),
                axis_x = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                axis_y = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                axis_z = connection_restapi_client_poc.models.idea_rs_open_model_geometry3_d_vector3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Vector3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, ),
                region = '',
                original_model_id = ''
            )
        else:
            return IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
