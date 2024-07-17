# coding: utf-8

"""
    Connection Rest API 1.0

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks

class TestConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks(unittest.TestCase):
    """ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks:
        """Test ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks`
        """
        model = ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks()
        if include_optional:
            return ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks(
                steel_costs = [
                    openapi_client.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_steel_idea_stati_ca_connection_checks.ConModeler_ConnectionPlugIn_DataContract_CostEstimationData_CostEstimationItemSteel-IdeaStatiCa_ConnectionChecks(
                        unique_id = 56, 
                        unit_cost = 1.337, 
                        cost = 1.337, 
                        total_weight = 1.337, 
                        name = '', 
                        grade = 1.337, 
                        plate_thickness = 1.337, )
                    ],
                fillet_weld_costs = [
                    openapi_client.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_weld_idea_stati_ca_connection_checks.ConModeler_ConnectionPlugIn_DataContract_CostEstimationData_CostEstimationItemWeld-IdeaStatiCa_ConnectionChecks(
                        unique_id = 56, 
                        unit_cost = 1.337, 
                        cost = 1.337, 
                        total_weight = 1.337, 
                        name = '', 
                        throat_thickness = 1.337, 
                        plate_thickness = 1.337, 
                        leg_size = 1.337, 
                        weld_type = 'NotSpecified', )
                    ],
                butt_weld_costs = [
                    openapi_client.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_weld_idea_stati_ca_connection_checks.ConModeler_ConnectionPlugIn_DataContract_CostEstimationData_CostEstimationItemWeld-IdeaStatiCa_ConnectionChecks(
                        unique_id = 56, 
                        unit_cost = 1.337, 
                        cost = 1.337, 
                        total_weight = 1.337, 
                        name = '', 
                        throat_thickness = 1.337, 
                        plate_thickness = 1.337, 
                        leg_size = 1.337, 
                        weld_type = 'NotSpecified', )
                    ],
                bolt_costs = [
                    openapi_client.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_item_bolt_idea_stati_ca_connection_checks.ConModeler_ConnectionPlugIn_DataContract_CostEstimationData_CostEstimationItemBolt-IdeaStatiCa_ConnectionChecks(
                        unique_id = 56, 
                        unit_cost = 1.337, 
                        cost = 1.337, 
                        total_weight = 1.337, 
                        name = '', 
                        grade = 1.337, )
                    ],
                hole_drilling_cost = 1.337,
                total_estimated_cost = 1.337,
                log_message = ''
            )
        else:
            return ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks(
        )
        """

    def testConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks(self):
        """Test ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
