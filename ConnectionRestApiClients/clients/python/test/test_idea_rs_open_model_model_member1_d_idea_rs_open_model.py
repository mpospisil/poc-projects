# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection-restapi-client-poc.models.idea_rs_open_model_model_member1_d_idea_rs_open_model import IdeaRSOpenModelModelMember1DIdeaRSOpenModel

class TestIdeaRSOpenModelModelMember1DIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelModelMember1DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelModelMember1DIdeaRSOpenModel:
        """Test IdeaRSOpenModelModelMember1DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelModelMember1DIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelModelMember1DIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelModelMember1DIdeaRSOpenModel(
                id = 56
            )
        else:
            return IdeaRSOpenModelModelMember1DIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelModelMember1DIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelModelMember1DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
