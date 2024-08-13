# FatigueCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stress_diagram** | **List[List[float]]** |  | [optional] 
**stress_diagram_tau** | **List[List[float]]** |  | [optional] 
**plate_uid** | **List[int]** |  | [optional] 
**joined_item_name** | **str** |  | [optional] 
**weld_type2** | [**DataWeldTypeCodeCIBasicTypes**](DataWeldTypeCodeCIBasicTypes.md) |  | [optional] 
**designed_thickness** | **float** |  | [optional] 
**normal_stress** | **float** |  | [optional] 
**shear_stress** | **float** |  | [optional] 
**normal_stress2** | **float** |  | [optional] 
**shear_stress2** | **float** |  | [optional] 
**plate_name** | **str** |  | [optional] 
**length** | **float** |  | [optional] 
**origin_id** | **float** |  | [optional] 
**section_line** | **List[List[str]]** |  | [optional] 
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
from connection_restapi_client_poc.models.fatigue_check_res_data_idea_stati_ca_connection_checks import FatigueCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of FatigueCheckResDataIdeaStatiCaConnectionChecks from a JSON string
fatigue_check_res_data_idea_stati_ca_connection_checks_instance = FatigueCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(FatigueCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
fatigue_check_res_data_idea_stati_ca_connection_checks_dict = fatigue_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of FatigueCheckResDataIdeaStatiCaConnectionChecks from a dict
fatigue_check_res_data_idea_stati_ca_connection_checks_from_dict = FatigueCheckResDataIdeaStatiCaConnectionChecks.from_dict(fatigue_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

