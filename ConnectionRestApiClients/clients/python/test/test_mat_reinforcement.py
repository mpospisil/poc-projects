# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.mat_reinforcement import MatReinforcement

class TestMatReinforcement(unittest.TestCase):
    """MatReinforcement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MatReinforcement:
        """Test MatReinforcement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MatReinforcement`
        """
        model = MatReinforcement()
        if include_optional:
            return MatReinforcement(
                bar_surface = 'smooth',
                name = '',
                load_from_library = True,
                e = 1.337,
                g = 1.337,
                poisson = 1.337,
                unit_mass = 1.337,
                specific_heat = 1.337,
                thermal_expansion = 1.337,
                thermal_conductivity = 1.337,
                is_default_material = True,
                order_in_code = 56,
                state_of_thermal_expansion = 'none',
                state_of_thermal_conductivity = 'none',
                state_of_thermal_specific_heat = 'none',
                state_of_thermal_stress_strain = 'none',
                state_of_thermal_strain = 'none',
                user_thermal_specific_heat_curvature = connection_restapi_client_poc.models.polygon2_d.Polygon2D(
                    points = [
                        connection_restapi_client_poc.models.point2_d.Point2D(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                user_thermal_conductivity_curvature = connection_restapi_client_poc.models.polygon2_d.Polygon2D(
                    points = [
                        connection_restapi_client_poc.models.point2_d.Point2D(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                user_thermal_expansion_curvature = connection_restapi_client_poc.models.polygon2_d.Polygon2D(
                    points = [
                        connection_restapi_client_poc.models.point2_d.Point2D(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                user_thermal_strain_curvature = connection_restapi_client_poc.models.polygon2_d.Polygon2D(
                    points = [
                        connection_restapi_client_poc.models.point2_d.Point2D(
                            x = 1.337, 
                            y = 1.337, )
                        ], ),
                user_thermal_stress_strain_curvature = [
                    connection_restapi_client_poc.models.temperature_curve2_d.TemperatureCurve2D(
                        points = [
                            connection_restapi_client_poc.models.point2_d.Point2D(
                                x = 1.337, 
                                y = 1.337, )
                            ], )
                    ],
                id = 56
            )
        else:
            return MatReinforcement(
        )
        """

    def testMatReinforcement(self):
        """Test MatReinforcement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
