# ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**material_fy** | **float** |  | [optional] 
**material_fy_phi** | **float** |  | [optional] 
**material_fy_omega** | **float** |  | [optional] 
**material_fy_design** | **float** |  | [optional] 
**material_fu** | **float** |  | [optional] 
**limit_plastic_strain** | **float** |  | [optional] 
**gammaov** | **float** |  | [optional] 
**gammash** | **float** |  | [optional] 
**cf** | **float** |  | [optional] 
**res_safety_factor** | **float** |  | [optional] 
**material_fy_fem** | **float** |  | [optional] 
**material_fy_reduced_by_gamma_m_rus** | **float** |  | [optional] 
**origin_name** | **str** |  | [optional] 
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
from openapi_client.models.con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInPlateCheckResDataInfoIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_plate_check_res_data_info_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


