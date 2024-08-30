# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.open_model_result import OpenModelResult

class TestOpenModelResult(unittest.TestCase):
    """OpenModelResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenModelResult:
        """Test OpenModelResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenModelResult`
        """
        model = OpenModelResult()
        if include_optional:
            return OpenModelResult(
                result_on_members = [
                    connection_restapi_client_poc.models.result_on_members.ResultOnMembers(
                        loading = connection_restapi_client_poc.models.loading.Loading(
                            loading_type = 'loadCase', 
                            id = 56, ), 
                        members = [
                            connection_restapi_client_poc.models.result_on_member.ResultOnMember(
                                member = connection_restapi_client_poc.models.member.Member(
                                    member_type = 'member1D', 
                                    id = 56, ), 
                                result_type = 'internalForces', 
                                local_system_type = 'local', 
                                results = [
                                    connection_restapi_client_poc.models.result_base.ResultBase()
                                    ], )
                            ], )
                    ]
            )
        else:
            return OpenModelResult(
        )
        """

    def testOpenModelResult(self):
        """Test OpenModelResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
