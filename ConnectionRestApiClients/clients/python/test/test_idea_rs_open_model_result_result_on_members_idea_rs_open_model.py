# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_open_model_result_result_on_members_idea_rs_open_model import IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel

class TestIdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel(unittest.TestCase):
    """IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel:
        """Test IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel`
        """
        model = IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel()
        if include_optional:
            return IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel(
                loading = connection_restapi_client_poc.models.idea_rs_open_model_result_loading_idea_rs_open_model.IdeaRS_OpenModel_Result_Loading-IdeaRS_OpenModel(
                    loading_type = 'LoadCase', 
                    id = 56, ),
                members = [
                    connection_restapi_client_poc.models.idea_rs_open_model_result_result_on_member_idea_rs_open_model.IdeaRS_OpenModel_Result_ResultOnMember-IdeaRS_OpenModel(
                        member = connection_restapi_client_poc.models.idea_rs_open_model_result_member_idea_rs_open_model.IdeaRS_OpenModel_Result_Member-IdeaRS_OpenModel(
                            member_type = 'Member1D', 
                            id = 56, ), 
                        result_type = 'InternalForces', 
                        local_system_type = 'Local', 
                        results = [
                            connection_restapi_client_poc.models.idea_rs_open_model_result_result_base_idea_rs_open_model.IdeaRS_OpenModel_Result_ResultBase-IdeaRS_OpenModel()
                            ], )
                    ]
            )
        else:
            return IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel(
        )
        """

    def testIdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel(self):
        """Test IdeaRSOpenModelResultResultOnMembersIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
