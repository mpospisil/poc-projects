# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.con_modeler_connection_plug_in_weld_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks(
                joined_item_name = '',
                designed_thickness = 1.337,
                thickness = 1.337,
                leg_size = 1.337,
                max_equivalent_stress = 1.337,
                equivalent_stress_resistance = 1.337,
                sigma_perpendicular = 1.337,
                sigma_perpendicular_max = 1.337,
                sigma_perpendicular_resistance = 1.337,
                unity_check_stress = 1.337,
                unity_check_weld = 1.337,
                unity_check_base_metal = 1.337,
                material_name = '',
                weld_type2 = 'NotSpecified',
                weld_with_contact = True,
                items = [
                    56
                    ],
                struct_items = [
                    56
                    ],
                tauy = 1.337,
                taux = 1.337,
                tauxwf = 1.337,
                sigmawf = 1.337,
                weld_area = 1.337,
                length = 1.337,
                length_elem = 1.337,
                forces_all_items = {
                    'key' : {
                        'key' : [
                            1.337
                            ]
                        }
                    },
                weld_stress_diagram = [
                    [
                        1.337
                        ]
                    ],
                gamma_m0 = 1.337,
                gamma_m2 = 1.337,
                gamma_mfi = 1.337,
                kw_theta = 1.337,
                material_fu = 1.337,
                beta_w = 1.337,
                rnd = 1.337,
                fn = 1.337,
                plastic_strain = 1.337,
                weld_eval = 56,
                plastic_capacity = 1.337,
                plastic_capacity_area = 1.337,
                plastic_capacity_area_val = 1.337,
                is_detailing_status_ok = True,
                is_detailing_status_for_report_ok = True,
                theta = 1.337,
                is_closed_weld = True,
                weld_check_method_hk = 'Simplified',
                phi_w = 1.337,
                omega_w = 1.337,
                fuw = 1.337,
                checks_nonconformities = openapi_client.models.ci_connections_data_detailing_detailing_checks_weld_ci_basic_types.CI_Connections_Data_Detailing_DetailingChecksWeld-CI_BasicTypes(
                    use_fillet_weld_leg_size = True, 
                    is_pjp_weld = True, 
                    results = [
                        openapi_client.models.ci_connections_data_detailing_i_detailing_check_ci_basic_types.CI_Connections_Data_Detailing_IDetailingCheck-CI_BasicTypes(
                            constraint_value = 1.337, 
                            detailing_check_category = 'None', 
                            detailing_check_type = 'None', 
                            message_params = [
                                1.337
                                ], 
                            target_element_id = 56, 
                            target_element_name = '', )
                        ], ),
                detailing_checks_weld = openapi_client.models.ci_connections_data_detailing_detailing_checks_weld_ci_basic_types.CI_Connections_Data_Detailing_DetailingChecksWeld-CI_BasicTypes(
                    use_fillet_weld_leg_size = True, 
                    is_pjp_weld = True, 
                    results = [
                        openapi_client.models.ci_connections_data_detailing_i_detailing_check_ci_basic_types.CI_Connections_Data_Detailing_IDetailingCheck-CI_BasicTypes(
                            constraint_value = 1.337, 
                            detailing_check_category = 'None', 
                            detailing_check_type = 'None', 
                            message_params = [
                                1.337
                                ], 
                            target_element_id = 56, 
                            target_element_name = '', )
                        ], ),
                weld_resistance = 1.337,
                weld_elem_area = 1.337,
                xu = 1.337,
                theta_weld = 1.337,
                aisc_directional_strength_increase = True,
                mw = 1.337,
                fusion_area_elem = 1.337,
                fu_base_metal = 1.337,
                base_metal_resistance = 1.337,
                theta1_weld = 1.337,
                theta2_weld = 1.337,
                fn_weld = 1.337,
                length_elem_reduced = 1.337,
                length_reduced = 1.337,
                beta_f_snip = 1.337,
                beta_z_snip = 1.337,
                rwf_snip = 1.337,
                rwz_snip = 1.337,
                gamma_c = 1.337,
                gamma_wm_snip = 1.337,
                fexx = 1.337,
                fnbm = 1.337,
                awe = 1.337,
                abm = 1.337,
                base_metal_capacity = True,
                beta_f_chn = 1.337,
                is_butt_weld = True,
                gamma_mw_is = 1.337,
                weld_longitudinal_force = 1.337,
                weld_transversal_force = 1.337,
                weld_longitudinal_resistance = 1.337,
                weld_transversal_resistance = 1.337,
                weld_theta_hk = 1.337,
                weld_coeff_k_hk = 1.337,
                is_weld_design_strength_table_value = True,
                is_ecen_weld_material_and_electrode = True,
                ue = 1.337,
                us = 1.337,
                weld_position_snip = 'Gravity',
                welding_type_snip = 'Manual',
                fire_temperature = 1.337,
                fire_design = True,
                is_horizontal_tying = True,
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
            return ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInWeldCheckResDataIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
