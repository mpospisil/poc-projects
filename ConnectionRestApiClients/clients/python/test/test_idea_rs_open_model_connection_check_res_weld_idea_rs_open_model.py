# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_weld_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel

class TestIdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel:
        """Test IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel(
                name = '',
                id = 56,
                unity_check = 1.337,
                check_status = True,
                load_case_id = 56,
                items = [
                    56
                    ]
            )
        else:
            return IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
