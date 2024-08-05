# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.ci_connections_data_auto_design_shear_forces_in_shear_planes_ci_basic_types import CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes

class TestCIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes(unittest.TestCase):
    """CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes:
        """Test CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes`
        """
        model = CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes()
        if include_optional:
            return CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes(
                shear_forces = [
                    connection_restapi_client_poc.models.ci_connections_data_auto_design_internal_shear_forces_ci_basic_types.CI_Connections_Data_AutoDesign_InternalShearForces-CI_BasicTypes(
                        qy = 1.337, 
                        qz = 1.337, )
                    ],
                bolt_coordinate_system = connection_restapi_client_poc.models.ci_connections_data_auto_design_bolt_coordinate_system_ci_basic_types.CI_Connections_Data_AutoDesign_BoltCoordinateSystem-CI_BasicTypes(
                    origin = '', 
                    axis_x = connection_restapi_client_poc.models.ci_geometry3_d_vector3_d_ci_basic_types.CI_Geometry3D_Vector3D-CI_BasicTypes(
                        direction_x = 1.337, 
                        direction_y = 1.337, 
                        direction_z = 1.337, 
                        normalize = connection_restapi_client_poc.models.ci_geometry3_d_vector3_d_ci_basic_types.CI_Geometry3D_Vector3D-CI_BasicTypes(
                            direction_x = 1.337, 
                            direction_y = 1.337, 
                            direction_z = 1.337, 
                            magnitude = 1.337, 
                            magnitude_squared = 1.337, ), 
                        magnitude = 1.337, 
                        magnitude_squared = 1.337, ), 
                    axis_y = , 
                    axis_z = , )
            )
        else:
            return CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes(
        )
        """

    def testCIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes(self):
        """Test CIConnectionsDataAutoDesignShearForcesInShearPlanesCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()