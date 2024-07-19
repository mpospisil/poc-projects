# ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bolt_assembly_name** | **str** |  | [optional] 
**forces_all_load_cases** | **Dict[str, List[float]]** |  | [optional] 
**slotted_hole** | **bool** |  | [optional] 
**normal_stress** | **float** |  | [optional] 
**shear_stress** | **float** |  | [optional] 
**plate_name** | **str** |  | [optional] 
**length** | **float** |  | [optional] 
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
from connection-restapi-client-poc.models.con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInFatigueBoltCheckResDataIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_fatigue_bolt_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


