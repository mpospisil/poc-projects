# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks(
                material_fy = 1.337,
                material_fy_phi = 1.337,
                material_fy_omega = 1.337,
                material_fy_design = 1.337,
                material_fu = 1.337,
                limit_plastic_strain = 1.337,
                gammaov = 1.337,
                gammash = 1.337,
                cf = 1.337,
                res_safety_factor = 1.337,
                material_fy_fem = 1.337,
                material_fy_reduced_by_gamma_m_rus = 1.337,
                origin_name = '',
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
            return ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
