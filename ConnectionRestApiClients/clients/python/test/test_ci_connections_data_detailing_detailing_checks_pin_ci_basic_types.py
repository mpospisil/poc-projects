# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.ci_connections_data_detailing_detailing_checks_pin_ci_basic_types import CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes

class TestCIConnectionsDataDetailingDetailingChecksPinCIBasicTypes(unittest.TestCase):
    """CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes:
        """Test CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes`
        """
        model = CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes()
        if include_optional:
            return CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes(
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
                    ]
            )
        else:
            return CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes(
        )
        """

    def testCIConnectionsDataDetailingDetailingChecksPinCIBasicTypes(self):
        """Test CIConnectionsDataDetailingDetailingChecksPinCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()