# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_selected_element_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin

class TestIdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin(unittest.TestCase):
    """IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin:
        """Test IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin`
        """
        model = IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin()
        if include_optional:
            return IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin(
                name = '',
                table_id = '',
                element_id = '',
                container_type = 'CrossSection'
            )
        else:
            return IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin(
        )
        """

    def testIdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin(self):
        """Test IdeaStatiCaPluginApiConnectionRestModelModelTemplateSelectedElementIdeaStatiCaPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
