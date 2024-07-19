# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks(
                max_stress = 1.337,
                max_strain = 1.337,
                thickness = 1.337,
                material_name = '',
                material_fy_without_reduction = 1.337,
                material_fy = 1.337,
                material_design_fy = 1.337,
                material_fu_without_reduction = 1.337,
                material_modulus_of_elasticity = 1.337,
                items = [
                    56
                    ],
                overstrength_factor = 1.337,
                strain_hardening_factor = 1.337,
                material_fy_for_capacity_design = 1.337,
                is_dissipative_item = True,
                cf = 1.337,
                is_hss_reduction = True,
                is_analysis_type_fir = True,
                is_analysis_type_ht = True,
                contact_stress = 1.337,
                limit_plastic_strain = 1.337,
                fire_temperature = 1.337,
                fire_temperature_calculation_data = connection_restapi_client_poc.models.idea_rs_connection_calculator_fire_design_fire_temperature_calculation_data_idea_rs_connection_calculator.IdeaRS_ConnectionCalculator_FireDesign_FireTemperatureCalculationData-IdeaRS_ConnectionCalculator(
                    total_exposure_time = 56, 
                    time_interval = 56, 
                    init_temperature = 1.337, 
                    fire_temperature = 1.337, 
                    temperature_increase = 1.337, ),
                gamma_mfi = 1.337,
                material_safety_factor_for_fire = 1.337,
                material_service_factor_gamma_c_rus = 1.337,
                material_safety_factor_gamma_m_rus = 1.337,
                material_fy_reduced_by_gamma_m_rus = 1.337,
                connection_coefficient_chn = 1.337,
                material_safety_factor = 1.337,
                material_safety_factor_ht = 1.337,
                material_safety_factor_gamma_m1_hkg = 1.337,
                material_safety_factor_gamma_m2_hkg = 1.337,
                reduction_factor_ky_theta = 1.337,
                reduction_factor_kp_theta = 1.337,
                reduction_factor_ke_theta = 1.337,
                proportional_limit = 1.337,
                slope_of_linear_elastic_range = 1.337,
                id = 56,
                name = '',
                check_status = True,
                limit_check_status = True,
                load_case_id = 56,
                load_case = '',
                max_unity_check = 1.337,
                form = ''
            )
        else:
            return ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
