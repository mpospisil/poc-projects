# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.api.parameter_api import ParameterApi


class TestParameterApi(unittest.TestCase):
    """ParameterApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ParameterApi()

    def tearDown(self) -> None:
        pass

    def test_evaluate_expression(self) -> None:
        """Test case for evaluate_expression

        Evaluate the expression and return the result
        """
        pass

    def test_get_parameters(self) -> None:
        """Test case for get_parameters

        Get all parameters which are defined for projectId and connectionId
        """
        pass

    def test_update_parameters(self) -> None:
        """Test case for update_parameters

        Update parameters for the connection connectionId in the project projectId by values passed in parameters
        """
        pass


if __name__ == '__main__':
    unittest.main()
