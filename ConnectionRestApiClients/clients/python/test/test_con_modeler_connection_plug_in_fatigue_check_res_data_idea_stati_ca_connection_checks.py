# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_modeler_connection_plug_in_fatigue_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks(
                stress_diagram = [
                    [
                        1.337
                        ]
                    ],
                stress_diagram_tau = [
                    [
                        1.337
                        ]
                    ],
                plate_uid = [
                    56
                    ],
                joined_item_name = '',
                weld_type2 = 'notSpecified',
                designed_thickness = 1.337,
                normal_stress = 1.337,
                shear_stress = 1.337,
                normal_stress2 = 1.337,
                shear_stress2 = 1.337,
                plate_name = '',
                length = 1.337,
                origin_id = 1.337,
                section_line = [
                    [
                        ''
                        ]
                    ],
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
            return ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInFatigueCheckResDataIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()