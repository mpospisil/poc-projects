# ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_stress** | **float** |  | [optional] 
**max_strain** | **float** |  | [optional] 
**thickness** | **float** |  | [optional] 
**material_name** | **str** |  | [optional] 
**material_fy_without_reduction** | **float** |  | [optional] 
**material_fy** | **float** |  | [optional] 
**material_design_fy** | **float** |  | [optional] 
**material_fu_without_reduction** | **float** |  | [optional] 
**material_modulus_of_elasticity** | **float** |  | [optional] 
**items** | **List[int]** |  | [optional] 
**overstrength_factor** | **float** |  | [optional] 
**strain_hardening_factor** | **float** |  | [optional] 
**material_fy_for_capacity_design** | **float** |  | [optional] 
**is_dissipative_item** | **bool** |  | [optional] 
**cf** | **float** |  | [optional] 
**is_hss_reduction** | **bool** |  | [optional] 
**is_analysis_type_fir** | **bool** |  | [optional] 
**is_analysis_type_ht** | **bool** |  | [optional] 
**contact_stress** | **float** |  | [optional] 
**limit_plastic_strain** | **float** |  | [optional] 
**fire_temperature** | **float** |  | [optional] 
**fire_temperature_calculation_data** | [**IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator**](IdeaRSConnectionCalculatorFireDesignFireTemperatureCalculationDataIdeaRSConnectionCalculator.md) |  | [optional] 
**gamma_mfi** | **float** |  | [optional] 
**material_safety_factor_for_fire** | **float** |  | [optional] 
**material_service_factor_gamma_c_rus** | **float** |  | [optional] 
**material_safety_factor_gamma_m_rus** | **float** |  | [optional] 
**material_fy_reduced_by_gamma_m_rus** | **float** |  | [optional] 
**connection_coefficient_chn** | **float** |  | [optional] 
**material_safety_factor** | **float** |  | [optional] 
**material_safety_factor_ht** | **float** |  | [optional] 
**material_safety_factor_gamma_m1_hkg** | **float** |  | [optional] 
**material_safety_factor_gamma_m2_hkg** | **float** |  | [optional] 
**reduction_factor_ky_theta** | **float** |  | [optional] 
**reduction_factor_kp_theta** | **float** |  | [optional] 
**reduction_factor_ke_theta** | **float** |  | [optional] 
**proportional_limit** | **float** |  | [optional] 
**slope_of_linear_elastic_range** | **float** |  | [optional] 
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
from openapi_client.models.con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInPlateCheckResDataIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_plate_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


