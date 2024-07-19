# ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bolt_tension_resistance** | **float** |  | [optional] 
**bolt_punching_resistance** | **float** |  | [optional] 
**bolt_tension_force** | **float** |  | [optional] 
**bolt_shear_resistance** | **float** |  | [optional] 
**bolt_shear_resistance_tension** | **float** |  | [optional] 
**bolt_bearing_resistance** | **float** |  | [optional] 
**bearing_resistance_bolt** | **float** |  | [optional] 
**bearing_resistance_con_part** | **float** |  | [optional] 
**bolt_shear_force** | **float** |  | [optional] 
**number_of_shear_planes** | **int** |  | [optional] 
**bolt_shear_forces** | **List[float]** |  | [optional] 
**unity_check_tension** | **float** |  | [optional] 
**unity_check_tension_res** | **float** |  | [optional] 
**unity_check_shear** | **float** |  | [optional] 
**bolt_assembly_name** | **str** |  | [optional] 
**bolt_tension_force_loadcase** | **str** |  | [optional] 
**bolt_shear_force_loadcase** | **str** |  | [optional] 
**bolt_interaction_loadcase** | **str** |  | [optional] 
**bolt_tension_force_loadcase_id** | **int** |  | [optional] 
**bolt_shear_force_loadcase_id** | **int** |  | [optional] 
**bolt_interaction_loadcase_id** | **int** |  | [optional] 
**forces_all_load_cases** | **Dict[str, List[float]]** |  | [optional] 
**element_axis_y** | **str** |  | [optional] 
**element_axis_z** | **str** |  | [optional] 
**unity_check_bearing** | **float** |  | [optional] 
**code_type** | [**IdeaRSWsLibCssServiceCodeTypeCIBasicTypes**](IdeaRSWsLibCssServiceCodeTypeCIBasicTypes.md) |  | [optional] 
**connector_grip_length** | **float** |  | [optional] 
**filler_plates_pack_th** | **float** |  | [optional] 
**angle** | **float** |  | [optional] 
**fub** | **float** |  | [optional] 
**a_ftrd** | **float** |  | [optional] 
**a_fvrd** | **float** |  | [optional] 
**k2** | **float** |  | [optional] 
**alfa_v** | **float** |  | [optional] 
**tp_bprd** | **float** |  | [optional] 
**fu_bprd** | **float** |  | [optional] 
**dm_bprd** | **float** |  | [optional] 
**gamma_m2** | **float** |  | [optional] 
**d_fbrd** | **float** |  | [optional] 
**th_fbrd** | **float** |  | [optional] 
**k1** | **float** |  | [optional] 
**alpha_b** | **float** |  | [optional] 
**gamma_m3** | **float** |  | [optional] 
**moment_resistance** | **float** |  | [optional] 
**unity_check_bending** | **float** |  | [optional] 
**bolt_moment_force** | **float** |  | [optional] 
**bearing_resistance** | **float** |  | [optional] 
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
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks import ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInBoltCheckResDataTimberIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_bolt_check_res_data_timber_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


