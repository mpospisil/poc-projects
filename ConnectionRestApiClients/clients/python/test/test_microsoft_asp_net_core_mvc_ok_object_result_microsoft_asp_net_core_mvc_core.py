# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.microsoft_asp_net_core_mvc_ok_object_result_microsoft_asp_net_core_mvc_core import MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore

class TestMicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore(unittest.TestCase):
    """MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore:
        """Test MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore`
        """
        model = MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore()
        if include_optional:
            return MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore(
                value = None,
                formatters = [
                    connection_restapi_client_poc.models.microsoft_asp_net_core_mvc_formatters_i_output_formatter_microsoft_asp_net_core_mvc_abstractions.Microsoft_AspNetCore_Mvc_Formatters_IOutputFormatter-Microsoft_AspNetCore_Mvc_Abstractions()
                    ],
                content_types = [
                    ''
                    ],
                declared_type = '',
                status_code = 56
            )
        else:
            return MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore(
        )
        """

    def testMicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore(self):
        """Test MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()