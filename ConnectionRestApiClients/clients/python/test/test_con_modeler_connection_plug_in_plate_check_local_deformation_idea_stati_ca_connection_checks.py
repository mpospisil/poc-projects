# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.con_modeler_connection_plug_in_plate_check_local_deformation_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks(
                max_deformation = 1.337,
                max_deformation_ratio = 1.337,
                limit_deformation = 1.337,
                thickness = 1.337,
                csize = 1.337,
                material_name = '',
                items = [
                    56
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
            return ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInPlateCheckLocalDeformationIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
