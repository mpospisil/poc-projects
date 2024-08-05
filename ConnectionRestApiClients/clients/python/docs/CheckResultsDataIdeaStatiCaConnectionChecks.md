# CheckResultsDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code_type** | [**IdeaRSWsLibCssServiceCodeTypeCIBasicTypes**](IdeaRSWsLibCssServiceCodeTypeCIBasicTypes.md) |  | [optional] 
**plates_deformation** | [**Dict[str, PlateCheckLocalDeformationIdeaStatiCaConnectionChecks]**](PlateCheckLocalDeformationIdeaStatiCaConnectionChecks.md) |  | [optional] 
**plates** | [**Dict[str, PlateCheckResDataIdeaStatiCaConnectionChecks]**](PlateCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**plates_info** | [**Dict[str, PlateCheckResDataInfoIdeaStatiCaConnectionChecks]**](PlateCheckResDataInfoIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolts** | [**Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]**](BoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolts_info** | [**Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]**](BoltCheckResDataInfoIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolts_anchor** | [**Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]**](BoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolts_anchor_compression** | [**Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]**](BoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolts_anchor_info** | [**Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]**](BoltCheckResDataInfoIdeaStatiCaConnectionChecks.md) |  | [optional] 
**pre_bolts** | [**Dict[str, BoltCheckResDataIdeaStatiCaConnectionChecks]**](BoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**pre_bolts_info** | [**Dict[str, BoltCheckResDataInfoIdeaStatiCaConnectionChecks]**](BoltCheckResDataInfoIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bolt_check_res_data_timbers** | [**Dict[str, BoltCheckResDataTimberIdeaStatiCaConnectionChecks]**](BoltCheckResDataTimberIdeaStatiCaConnectionChecks.md) |  | [optional] 
**pins** | [**Dict[str, PinCheckResDataIdeaStatiCaConnectionChecks]**](PinCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**welds** | [**Dict[str, WeldCheckResDataIdeaStatiCaConnectionChecks]**](WeldCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**welds_info** | [**Dict[str, WeldCheckResDataInfoIdeaStatiCaConnectionChecks]**](WeldCheckResDataInfoIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fatigue_checks** | [**Dict[str, FatigueCheckResDataIdeaStatiCaConnectionChecks]**](FatigueCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fatigue_sections_checks** | [**Dict[str, FatigueCheckResDataIdeaStatiCaConnectionChecks]**](FatigueCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fatigue_bolt_checks** | [**Dict[str, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks]**](FatigueBoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fatigue_anchor_checks** | [**Dict[str, FatigueBoltCheckResDataIdeaStatiCaConnectionChecks]**](FatigueBoltCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**fatigue_welds** | [**Dict[str, WeldCheckResDataIdeaStatiCaConnectionChecks]**](WeldCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**concrete_blocks** | [**Dict[str, ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks]**](ConcreteBlockCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**summary** | [**Dict[str, SummaryCheckResDataIdeaStatiCaConnectionChecks]**](SummaryCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**project_item** | [**Dict[str, ProjectCheckResDataIdeaStatiCaConnectionChecks]**](ProjectCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**analysis** | [**Dict[str, AnalysisCheckResDataIdeaStatiCaConnectionChecks]**](AnalysisCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**total_capacity** | [**Dict[str, AnalysisCheckResDataIdeaStatiCaConnectionChecks]**](AnalysisCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**base_plate_shear** | [**Dict[str, BasePlateShearCheckResDataIdeaStatiCaConnectionChecks]**](BasePlateShearCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**stiffnesess** | [**Dict[str, StiffnessChekDataIdeaStatiCaConnectionChecks]**](StiffnessChekDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**stiffnesess_axial** | [**Dict[str, StiffnessChekDataIdeaStatiCaConnectionChecks]**](StiffnessChekDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**bucklings** | [**Dict[str, BucklingCheckDataIdeaStatiCaConnectionChecks]**](BucklingCheckDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**nonconformity** | [**List[SummaryCheckResDataIdeaStatiCaConnectionChecks]**](SummaryCheckResDataIdeaStatiCaConnectionChecks.md) |  | [optional] 
**cost_estimation_results** | [**CostEstimationResultsIdeaStatiCaConnectionChecks**](CostEstimationResultsIdeaStatiCaConnectionChecks.md) |  | [optional] 
**welds_data_load_levels** | [**Dict[str, WeldDataLoadLevelIdeaStatiCaConnectionChecks]**](WeldDataLoadLevelIdeaStatiCaConnectionChecks.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.check_results_data_idea_stati_ca_connection_checks import CheckResultsDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResultsDataIdeaStatiCaConnectionChecks from a JSON string
check_results_data_idea_stati_ca_connection_checks_instance = CheckResultsDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(CheckResultsDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
check_results_data_idea_stati_ca_connection_checks_dict = check_results_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of CheckResultsDataIdeaStatiCaConnectionChecks from a dict
check_results_data_idea_stati_ca_connection_checks_from_dict = CheckResultsDataIdeaStatiCaConnectionChecks.from_dict(check_results_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


