# WeldCheckResDataInfoIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_name** | **str** |  | [optional] 
**equivalent_stress_resistance** | **float** |  | [optional] 
**sigma_perpendicular_resistance** | **float** |  | [optional] 
**beta_w** | **float** |  | [optional] 
**weld_strength** | **float** |  | [optional] 
**e_nelectrode** | **bool** |  | [optional] 
**flat_position** | **bool** |  | [optional] 
**welding_type** | [**DataWeldingTypeSNIPCIBasicTypes**](DataWeldingTypeSNIPCIBasicTypes.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**check_status** | **bool** |  | [optional] 
**limit_check_status** | **bool** |  | [optional] 
**load_case_id** | **int** |  | [optional] 
**load_case** | **str** |  | [optional] 
**max_unity_check** | **float** |  | [optional] 
**form** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.weld_check_res_data_info_idea_stati_ca_connection_checks import WeldCheckResDataInfoIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of WeldCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string
weld_check_res_data_info_idea_stati_ca_connection_checks_instance = WeldCheckResDataInfoIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(WeldCheckResDataInfoIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
weld_check_res_data_info_idea_stati_ca_connection_checks_dict = weld_check_res_data_info_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of WeldCheckResDataInfoIdeaStatiCaConnectionChecks from a dict
weld_check_res_data_info_idea_stati_ca_connection_checks_from_dict = WeldCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(weld_check_res_data_info_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


