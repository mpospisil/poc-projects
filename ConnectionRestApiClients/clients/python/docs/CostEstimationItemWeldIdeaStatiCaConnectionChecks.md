# CostEstimationItemWeldIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unique_id** | **int** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**cost** | **float** |  | [optional] 
**total_weight** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**throat_thickness** | **float** |  | [optional] 
**plate_thickness** | **float** |  | [optional] 
**leg_size** | **float** |  | [optional] 
**weld_type** | [**DataWeldTypeCodeCIBasicTypes**](DataWeldTypeCodeCIBasicTypes.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cost_estimation_item_weld_idea_stati_ca_connection_checks import CostEstimationItemWeldIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of CostEstimationItemWeldIdeaStatiCaConnectionChecks from a JSON string
cost_estimation_item_weld_idea_stati_ca_connection_checks_instance = CostEstimationItemWeldIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(CostEstimationItemWeldIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
cost_estimation_item_weld_idea_stati_ca_connection_checks_dict = cost_estimation_item_weld_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of CostEstimationItemWeldIdeaStatiCaConnectionChecks from a dict
cost_estimation_item_weld_idea_stati_ca_connection_checks_from_dict = CostEstimationItemWeldIdeaStatiCaConnectionChecks.from_dict(cost_estimation_item_weld_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


