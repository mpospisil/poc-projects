# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection-restapi-client-poc.models.idea_rs_connections_data_thin_plate_validity_ci_basic_types import IdeaRSConnectionsDataThinPlateValidityCIBasicTypes

class TestIdeaRSConnectionsDataThinPlateValidityCIBasicTypes(unittest.TestCase):
    """IdeaRSConnectionsDataThinPlateValidityCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSConnectionsDataThinPlateValidityCIBasicTypes:
        """Test IdeaRSConnectionsDataThinPlateValidityCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSConnectionsDataThinPlateValidityCIBasicTypes`
        """
        model = IdeaRSConnectionsDataThinPlateValidityCIBasicTypes()
        if include_optional:
            return IdeaRSConnectionsDataThinPlateValidityCIBasicTypes(
                related_plate_name = '',
                validity_criteria = [
                    connection-restapi-client-poc.models.idea_rs_connections_data_thin_plate_validity_criterion_ci_basic_types.IdeaRS_Connections_Data_ThinPlateValidityCriterion-CI_BasicTypes(
                        value_name = '', 
                        value = 1.337, 
                        limit = 1.337, )
                    ]
            )
        else:
            return IdeaRSConnectionsDataThinPlateValidityCIBasicTypes(
        )
        """

    def testIdeaRSConnectionsDataThinPlateValidityCIBasicTypes(self):
        """Test IdeaRSConnectionsDataThinPlateValidityCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
