# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.con_connection import ConConnection

class TestConConnection(unittest.TestCase):
    """ConConnection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConConnection:
        """Test ConConnection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConConnection`
        """
        model = ConConnection()
        if include_optional:
            return ConConnection(
                id = 56,
                identifier = '',
                name = '',
                description = '',
                analysis_type = 'stress_Strain',
                load_options = connection_restapi_client_poc.models.con_loading_options.ConLoadingOptions(
                    loads_in_equilibrium = True, 
                    loads_in_percentage = True, ),
                bearing_member_id = 56,
                is_calculated = True
            )
        else:
            return ConConnection(
        )
        """

    def testConConnection(self):
        """Test ConConnection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
