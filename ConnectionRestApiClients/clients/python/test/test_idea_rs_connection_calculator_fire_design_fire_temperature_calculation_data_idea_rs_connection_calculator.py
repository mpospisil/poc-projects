# coding: utf-8

"""
    Connection Rest API 1.1

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connection_restapi_client_poc.models.idea_rs_connection_calculator_fire_design_fire_temperature_calculation_data_idea_rs_connection_calculator import IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator

class TestIdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator(unittest.TestCase):
    """IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator:
        """Test IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator`
        """
        model = IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator()
        if include_optional:
            return IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator(
                total_exposure_time = 56,
                time_interval = 56,
                init_temperature = 1.337,
                fire_temperature = 1.337,
                temperature_increase = 1.337
            )
        else:
            return IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator(
        )
        """

    def testIdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator(self):
        """Test IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
