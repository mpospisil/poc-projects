# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_modeler_connection_plug_in_pin_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks(
                pin_assembly_name = '',
                pin_shear_resistance = 1.337,
                pin_bearing_resistance = 1.337,
                pin_replaceable_bearing_resistance = 1.337,
                pin_bending_resistance = 1.337,
                pin_replaceable_bending_resistance = 1.337,
                pin_combined_shear_and_bending_resistance = 1.337,
                contact_bearing_stress = 1.337,
                contact_bearing_resistance = 1.337,
                unity_check_pin_shear = 1.337,
                unity_check_pin_bearing = 1.337,
                unity_check_pin_replaceable_bearing = 1.337,
                unity_check_pin_bearing_decisive = 1.337,
                unity_check_pin_bending = 1.337,
                unity_check_pin_replaceable_bending = 1.337,
                unity_check_pin_bending_decisive = 1.337,
                unity_check_pin_combined_shear_and_bending = 1.337,
                unity_check_pin_replaceable_contact_bearing = 1.337,
                max_unity_check_shear = 1.337,
                is_pin_replaceable = True,
                pin_all_elements_all_sections_forces_for_diagram = {
                    'key' : [
                        [
                            1.337
                            ]
                        ]
                    },
                pin_shear_forces = [
                    1.337
                    ],
                pin_bearing_forces = [
                    1.337
                    ],
                pin_bearing_forces_by_plate_id = {
                    'key' : 1.337
                    },
                pin_bending_forces = [
                    1.337
                    ],
                pin_shear_force = 1.337,
                pin_bearing_force_for_bearing = 1.337,
                pin_bending_force = 1.337,
                pin_cross_sectional_area = 1.337,
                pin_section_modulus = 1.337,
                pin_diameter = 1.337,
                pin_hole_diameter = 1.337,
                pin_ultimate_tensile_strength = 1.337,
                pin_yield_strength = 1.337,
                connected_part_yield_strength = 1.337,
                connected_part_thickness_for_bearing = 1.337,
                decisive_yield_strength_for_bearing = 1.337,
                modulus_of_elasticity_for_contact_bearing = 1.337,
                yield_strength_for_contact_bearing = 1.337,
                connected_part_thickness_for_contact_bearing = 1.337,
                pin_bearing_force_for_contact_bearing = 1.337,
                gamma_m0 = 1.337,
                gamma_m2 = 1.337,
                gamma_m6ser = 1.337,
                gamma_mfi = 1.337,
                is_fire_design = True,
                fire_temperature = 1.337,
                factor_kb_theta = 1.337,
                detailing_checks_pin = connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_pin_ci_basic_types.CI_Connections_Data_Detailing_DetailingChecksPin-CI_BasicTypes(
                    results = [
                        connection_restapi_client_poc.models.ci_connections_data_detailing_i_detailing_check_ci_basic_types.CI_Connections_Data_Detailing_IDetailingCheck-CI_BasicTypes(
                            constraint_value = 1.337, 
                            detailing_check_category = 'None', 
                            detailing_check_type = 'None', 
                            message_params = [
                                1.337
                                ], 
                            target_element_id = 56, 
                            target_element_name = '', )
                        ], ),
                is_detailing_status_ok = True,
                is_detailing_status_for_report_ok = True,
                forces_all_load_cases = {
                    'key' : [
                        1.337
                        ]
                    },
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
            return ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInPinCheckResDataIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
