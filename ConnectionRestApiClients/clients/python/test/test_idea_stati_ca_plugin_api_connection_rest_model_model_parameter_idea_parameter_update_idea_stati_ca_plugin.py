# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin

class TestIdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin(unittest.TestCase):
    """IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin:
        """Test IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin`
        """
        model = IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin()
        if include_optional:
            return IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin(
                key = '',
                expression = ''
            )
        else:
            return IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin(
        )
        """

    def testIdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin(self):
        """Test IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
