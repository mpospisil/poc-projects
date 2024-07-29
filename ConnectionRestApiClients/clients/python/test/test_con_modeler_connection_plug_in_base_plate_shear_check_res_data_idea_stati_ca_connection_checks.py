# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_modeler_connection_plug_in_base_plate_shear_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks(
                vrdf = 1.337,
                vrdx = 1.337,
                vrdy = 1.337,
                vx = 1.337,
                vy = 1.337,
                v = 1.337,
                vr = 1.337,
                pbr = 1.337,
                vcb = 1.337,
                friction_coefficient = 1.337,
                shear_iron_css = '',
                shear_iron_applied = True,
                unity_check = 1.337,
                avx = 1.337,
                avy = 1.337,
                fy = 1.337,
                nsd = 1.337,
                shear_force_transfer = 56,
                gamma_m0 = 1.337,
                asd = True,
                phi_omega = 1.337,
                bearing_resistance = 1.337,
                num_of_tensioned_anchors = 56,
                phi_br = 1.337,
                fc = 1.337,
                alpha_v = 1.337,
                psi_alpha_v = 1.337,
                avc_cone_breakout_area = 1.337,
                unity_check_cone_breakout_resistance = 1.337,
                unity_check_bearing_capacity = 1.337,
                phi_c = 1.337,
                omega_c = 1.337,
                phi_s = 1.337,
                shear_lug_force = 1.337,
                shear_lug_force_component = 1.337,
                cone_breakout_check_type = 'both',
                shear_lug_projection_area = 1.337,
                comp_force = 1.337,
                kc = 1.337,
                connector_tensile_area = 1.337,
                connector_fy = 1.337,
                ny = 1.337,
                pa = 1.337,
                a = 1.337,
                l = 1.337,
                b = 1.337,
                gamma_c = 1.337,
                v_factor = 1.337,
                k1_factor = 1.337,
                sigma_rdmax = 1.337,
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
            return ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInBasePlateShearCheckResDataIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
