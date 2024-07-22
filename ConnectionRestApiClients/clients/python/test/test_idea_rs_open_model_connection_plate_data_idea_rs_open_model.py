# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_plate_data_idea_rs_open_model import IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel(
                name = '',
                thickness = 1.337,
                material = '',
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
                geometry = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_region2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Region2D-IdeaRS_OpenModel(
                    outline = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel(
                        start_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                            x = 1.337, 
                            y = 1.337, ), 
                        segments = [
                            connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_segment2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Segment2D-IdeaRS_OpenModel(
                                end_point = connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_point2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_Point2D-IdeaRS_OpenModel(
                                    x = 1.337, 
                                    y = 1.337, ), )
                            ], ), 
                    openings = [
                        connection_restapi_client_poc.models.idea_rs_open_model_geometry2_d_poly_line2_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry2D_PolyLine2D-IdeaRS_OpenModel()
                        ], ),
                original_model_id = '',
                is_negative_object = True,
                id = 56
            )
        else:
            return IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
