# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.data_thin_plate_validity_ci_basic_types import DataThinPlateValidityCIBasicTypes

class TestDataThinPlateValidityCIBasicTypes(unittest.TestCase):
    """DataThinPlateValidityCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataThinPlateValidityCIBasicTypes:
        """Test DataThinPlateValidityCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataThinPlateValidityCIBasicTypes`
        """
        model = DataThinPlateValidityCIBasicTypes()
        if include_optional:
            return DataThinPlateValidityCIBasicTypes(
                related_plate_name = '',
                validity_criteria = [
                    connection_restapi_client_poc.models.data_thin_plate_validity_criterion_ci_basic_types.Data_ThinPlateValidityCriterion-CI_BasicTypes(
                        value_name = '', 
                        value = 1.337, 
                        limit = 1.337, )
                    ]
            )
        else:
            return DataThinPlateValidityCIBasicTypes(
        )
        """

    def testDataThinPlateValidityCIBasicTypes(self):
        """Test DataThinPlateValidityCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
