# CostEstimationResultsIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steel_costs** | [**List[CostEstimationItemSteelIdeaStatiCaConnectionChecks]**](CostEstimationItemSteelIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fillet_weld_costs** | [**List[CostEstimationItemWeldIdeaStatiCaConnectionChecks]**](CostEstimationItemWeldIdeaStatiCaConnectionChecks.md) |  | [optional] 
**butt_weld_costs** | [**List[CostEstimationItemWeldIdeaStatiCaConnectionChecks]**](CostEstimationItemWeldIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolt_costs** | [**List[CostEstimationItemBoltIdeaStatiCaConnectionChecks]**](CostEstimationItemBoltIdeaStatiCaConnectionChecks.md) |  | [optional] 
**hole_drilling_cost** | **float** |  | [optional] 
**total_estimated_cost** | **float** |  | [optional] 
**log_message** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cost_estimation_results_idea_stati_ca_connection_checks import CostEstimationResultsIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of CostEstimationResultsIdeaStatiCaConnectionChecks from a JSON string
cost_estimation_results_idea_stati_ca_connection_checks_instance = CostEstimationResultsIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(CostEstimationResultsIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
cost_estimation_results_idea_stati_ca_connection_checks_dict = cost_estimation_results_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of CostEstimationResultsIdeaStatiCaConnectionChecks from a dict
cost_estimation_results_idea_stati_ca_connection_checks_from_dict = CostEstimationResultsIdeaStatiCaConnectionChecks.from_dict(cost_estimation_results_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


