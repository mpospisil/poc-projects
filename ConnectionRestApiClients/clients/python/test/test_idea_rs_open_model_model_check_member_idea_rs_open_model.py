# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_model_check_member_idea_rs_open_model import IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel

class TestIdeaRSOpenModelModelCheckMemberIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel:
        """Test IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel(
                id = 56
            )
        else:
            return IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelModelCheckMemberIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelModelCheckMemberIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
