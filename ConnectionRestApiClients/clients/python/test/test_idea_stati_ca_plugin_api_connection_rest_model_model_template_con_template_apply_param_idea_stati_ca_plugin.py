# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_con_template_apply_param_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin

class TestIdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin(unittest.TestCase):
    """IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin:
        """Test IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin`
        """
        model = IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin()
        if include_optional:
            return IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin(
                connection_template = '',
                mapping = connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_template_conversions_idea_stati_ca_plugin.IdeaStatiCa_Plugin_Api_ConnectionRest_Model_Model_Template_TemplateConversions-IdeaStatiCa_Plugin(
                    conversions = [
                        connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_base_template_conversion_idea_stati_ca_plugin.IdeaStatiCa_Plugin_Api_ConnectionRest_Model_Model_Template_BaseTemplateConversion-IdeaStatiCa_Plugin(
                            original_value = '', 
                            original_template_id = '', 
                            new_value = '', 
                            description = '', 
                            new_template_id = '', 
                            new_element = connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_template_selected_element_idea_stati_ca_plugin.IdeaStatiCa_Plugin_Api_ConnectionRest_Model_Model_Template_SelectedElement-IdeaStatiCa_Plugin(
                                name = '', 
                                table_id = '', 
                                element_id = '', 
                                container_type = 'crossSection', ), )
                        ], 
                    country_code = '', )
            )
        else:
            return IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin(
        )
        """

    def testIdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin(self):
        """Test IdeaStatiCaPluginApiConnectionRestModelModelTemplateConTemplateApplyParamIdeaStatiCaPlugin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
