# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.detail_base_plate3_d_idea_rs_open_model import DetailBasePlate3DIdeaRSOpenModel

class TestDetailBasePlate3DIdeaRSOpenModel(unittest.TestCase):
    """DetailBasePlate3DIdeaRSOpenModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DetailBasePlate3DIdeaRSOpenModel:
        """Test DetailBasePlate3DIdeaRSOpenModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DetailBasePlate3DIdeaRSOpenModel`
        """
        model = DetailBasePlate3DIdeaRSOpenModel()
        if include_optional:
            return DetailBasePlate3DIdeaRSOpenModel(
                id = 56
            )
        else:
            return DetailBasePlate3DIdeaRSOpenModel(
        )
        """

    def testDetailBasePlate3DIdeaRSOpenModel(self):
        """Test DetailBasePlate3DIdeaRSOpenModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
