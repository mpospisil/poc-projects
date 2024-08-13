# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.weld_check_res_data_info_idea_stati_ca_connection_checks import WeldCheckResDataInfoIdeaStatiCaConnectionChecks

class TestWeldCheckResDataInfoIdeaStatiCaConnectionChecks(unittest.TestCase):
    """WeldCheckResDataInfoIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WeldCheckResDataInfoIdeaStatiCaConnectionChecks:
        """Test WeldCheckResDataInfoIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WeldCheckResDataInfoIdeaStatiCaConnectionChecks`
        """
        model = WeldCheckResDataInfoIdeaStatiCaConnectionChecks()
        if include_optional:
            return WeldCheckResDataInfoIdeaStatiCaConnectionChecks(
                item_name = '',
                equivalent_stress_resistance = 1.337,
                sigma_perpendicular_resistance = 1.337,
                beta_w = 1.337,
                weld_strength = 1.337,
                e_nelectrode = True,
                flat_position = True,
                welding_type = 'manual',
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
            return WeldCheckResDataInfoIdeaStatiCaConnectionChecks(
        )
        """

    def testWeldCheckResDataInfoIdeaStatiCaConnectionChecks(self):
        """Test WeldCheckResDataInfoIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
