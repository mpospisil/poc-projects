# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.data_thin_plate_validity_criterion_ci_basic_types import DataThinPlateValidityCriterionCIBasicTypes

class TestDataThinPlateValidityCriterionCIBasicTypes(unittest.TestCase):
    """DataThinPlateValidityCriterionCIBasicTypes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataThinPlateValidityCriterionCIBasicTypes:
        """Test DataThinPlateValidityCriterionCIBasicTypes
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataThinPlateValidityCriterionCIBasicTypes`
        """
        model = DataThinPlateValidityCriterionCIBasicTypes()
        if include_optional:
            return DataThinPlateValidityCriterionCIBasicTypes(
                value_name = '',
                value = 1.337,
                limit = 1.337
            )
        else:
            return DataThinPlateValidityCriterionCIBasicTypes(
        )
        """

    def testDataThinPlateValidityCriterionCIBasicTypes(self):
        """Test DataThinPlateValidityCriterionCIBasicTypes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
