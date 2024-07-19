# ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bolt_tension_resistance** | **float** |  | [optional] 
**compression_resistance** | **float** |  | [optional] 
**moment_resistance** | **float** |  | [optional] 
**bolt_punching_resistance** | **float** |  | [optional] 
**bolt_shear_resistance** | **float** |  | [optional] 
**bolt_shear_resistance_anchor** | **float** |  | [optional] 
**bolt_shear_resistance_tension** | **float** |  | [optional] 
**anchor_stiffness** | **float** |  | [optional] 
**slip_resistance_coeff** | **float** |  | [optional] 
**stand_off_gap** | **float** |  | [optional] 
**bolt_preloaded_force** | **float** |  | [optional] 
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
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInBoltCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_bolt_check_res_data_info_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


