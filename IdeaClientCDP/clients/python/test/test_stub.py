# coding: utf-8

"""
    ConDesignProposer API 9.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 9.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from idea_cdp_client_poc.models.stub import Stub

class TestStub(unittest.TestCase):
    """Stub unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Stub:
        """Test Stub
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Stub`
        """
        model = Stub()
        if include_optional:
            return Stub(
                count = 56
            )
        else:
            return Stub(
        )
        """

    def testStub(self):
        """Test Stub"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
