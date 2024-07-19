# ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks


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
**welding_type** | [**IdeaStatiCaConnectionBasicTypesDataWeldingTypeSNIPCIBasicTypes**](IdeaStatiCaConnectionBasicTypesDataWeldingTypeSNIPCIBasicTypes.md) |  | [optional] 
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
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInWeldCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_weld_check_res_data_info_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


