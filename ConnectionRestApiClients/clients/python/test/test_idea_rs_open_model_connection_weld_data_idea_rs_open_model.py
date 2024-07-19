# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection-restapi-client-poc.models.idea_rs_open_model_connection_weld_data_idea_rs_open_model import IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel(
                id = 56,
                name = '',
                thickness = 1.337,
                material = '',
                weld_material = connection-restapi-client-poc.models.idea_rs_open_model_reference_element_idea_rs_open_model.IdeaRS_OpenModel_ReferenceElement-IdeaRS_OpenModel(
                    type_name = '', 
                    id = 56, 
                    element = connection-restapi-client-poc.models.idea_rs_open_model_open_element_id_idea_rs_open_model.IdeaRS_OpenModel_OpenElementId-IdeaRS_OpenModel(
                        id = 56, ), ),
                weld_type = 'NotSpecified',
                connected_part_ids = [
                    ''
                    ],
                start = connection-restapi-client-poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, ),
                end = connection-restapi-client-poc.models.idea_rs_open_model_geometry3_d_point3_d_idea_rs_open_model.IdeaRS_OpenModel_Geometry3D_Point3D-IdeaRS_OpenModel(
                    x = 1.337, 
                    y = 1.337, 
                    z = 1.337, 
                    id = 56, )
            )
        else:
            return IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
