# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionSetupIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionSetupIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionSetupIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionSetupIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionSetupIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionSetupIdeaRSOpenModel(
                steel_setup = None,
                concrete_setup = connection_restapi_client_poc.models.idea_rs_open_model_concrete_concrete_setup_idea_rs_open_model.IdeaRS_OpenModel_Concrete_ConcreteSetup-IdeaRS_OpenModel(
                    id = 56, ),
                stop_at_limit_strain = True,
                weld_evaluation_data = 'maxForceElement',
                check_detailing = True,
                apply_cone_breakout_check = 'both',
                pretension_force_fpc = 1.337,
                gamma_inst = 1.337,
                gamma_c = 1.337,
                gamma_m3 = 1.337,
                anchor_length_for_stiffness = 56,
                joint_beta_factor = 1.337,
                effective_area_stress_coeff = 1.337,
                effective_area_stress_coeff_aisc = 1.337,
                friction_coefficient = 1.337,
                limit_plastic_strain = 1.337,
                limit_deformation = 1.337,
                limit_deformation_check = True,
                analysis_gnl = True,
                analysis_all_gnl = True,
                warn_plastic_strain = 1.337,
                warn_check_level = 1.337,
                optimal_check_level = 1.337,
                distance_between_bolts = 1.337,
                distance_diameter_between_bp = 1.337,
                distance_between_bolts_edge = 1.337,
                bearing_angle = 1.337,
                decreasing_ftrd = 1.337,
                braced_system = True,
                bearing_check = True,
                apply_betap_influence = True,
                member_length_ratio = 1.337,
                division_of_surface_of_chs = 56,
                division_of_arcs_of_rhs = 56,
                num_element = 56,
                number_iterations = 56,
                mdiv = 56,
                min_size = 1.337,
                max_size = 1.337,
                num_element_rhs = 56,
                num_element_plate = 56,
                rigid_bp = True,
                alpha_cc = 1.337,
                cracked_concrete = True,
                developed_fillers = True,
                deformation_bolt_hole = True,
                extension_length_ration_open_sections = 1.337,
                extension_length_ration_close_sections = 1.337,
                factor_preload_bolt = 1.337,
                base_metal_capacity = True,
                apply_bearing_check = True,
                friction_coefficient_pbolt = 1.337,
                crt_comp_check_is = 'iS800_Cl_7_4',
                bolt_max_grip_length_coeff = 1.337,
                fatigue_section_offset = 1.337,
                condensed_element_length_factor = 1.337,
                gamma_mu = 1.337,
                hss_limit_plastic_strain = 1.337
            )
        else:
            return IdeaRSOpenModelConnectionSetupIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionSetupIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionSetupIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()