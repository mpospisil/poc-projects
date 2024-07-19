# ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steel_costs** | [**List[ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemSteelIdeaStatiCaConnectionChecks]**](ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemSteelIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fillet_weld_costs** | [**List[ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemWeldIdeaStatiCaConnectionChecks]**](ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemWeldIdeaStatiCaConnectionChecks.md) |  | [optional] 
**butt_weld_costs** | [**List[ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemWeldIdeaStatiCaConnectionChecks]**](ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemWeldIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolt_costs** | [**List[ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemBoltIdeaStatiCaConnectionChecks]**](ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationItemBoltIdeaStatiCaConnectionChecks.md) |  | [optional] 
**hole_drilling_cost** | **float** |  | [optional] 
**total_estimated_cost** | **float** |  | [optional] 
**log_message** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks import ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInDataContractCostEstimationDataCostEstimationResultsIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_data_contract_cost_estimation_data_cost_estimation_results_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


