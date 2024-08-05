# WeldCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**joined_item_name** | **str** |  | [optional] 
**designed_thickness** | **float** |  | [optional] 
**thickness** | **float** |  | [optional] 
**leg_size** | **float** |  | [optional] 
**max_equivalent_stress** | **float** |  | [optional] 
**equivalent_stress_resistance** | **float** |  | [optional] 
**sigma_perpendicular** | **float** |  | [optional] 
**sigma_perpendicular_max** | **float** |  | [optional] 
**sigma_perpendicular_resistance** | **float** |  | [optional] 
**unity_check_stress** | **float** |  | [optional] 
**unity_check_weld** | **float** |  | [optional] 
**unity_check_base_metal** | **float** |  | [optional] 
**material_name** | **str** |  | [optional] 
**weld_type2** | [**DataWeldTypeCodeCIBasicTypes**](DataWeldTypeCodeCIBasicTypes.md) |  | [optional] 
**weld_with_contact** | **bool** |  | [optional] 
**items** | **List[int]** |  | [optional] 
**struct_items** | **List[int]** |  | [optional] 
**tauy** | **float** |  | [optional] 
**taux** | **float** |  | [optional] 
**tauxwf** | **float** |  | [optional] 
**sigmawf** | **float** |  | [optional] 
**weld_area** | **float** |  | [optional] 
**length** | **float** |  | [optional] 
**length_elem** | **float** |  | [optional] 
**forces_all_items** | **Dict[str, Dict[str, List[float]]]** |  | [optional] 
**weld_stress_diagram** | **List[List[float]]** |  | [optional] 
**gamma_m0** | **float** |  | [optional] 
**gamma_m2** | **float** |  | [optional] 
**gamma_mfi** | **float** |  | [optional] 
**kw_theta** | **float** |  | [optional] 
**material_fu** | **float** |  | [optional] 
**beta_w** | **float** |  | [optional] 
**rnd** | **float** |  | [optional] 
**fn** | **float** |  | [optional] 
**plastic_strain** | **float** |  | [optional] 
**weld_eval** | **int** |  | [optional] 
**plastic_capacity** | **float** |  | [optional] 
**plastic_capacity_area** | **float** |  | [optional] 
**plastic_capacity_area_val** | **float** |  | [optional] 
**is_detailing_status_ok** | **bool** |  | [optional] 
**is_detailing_status_for_report_ok** | **bool** |  | [optional] 
**theta** | **float** |  | [optional] 
**is_closed_weld** | **bool** |  | [optional] 
**weld_check_method_hk** | [**DataWeldCheckMethodHKCIBasicTypes**](DataWeldCheckMethodHKCIBasicTypes.md) |  | [optional] 
**phi_w** | **float** |  | [optional] 
**omega_w** | **float** |  | [optional] 
**fuw** | **float** |  | [optional] 
**checks_nonconformities** | [**DataDetailingDetailingChecksWeldCIBasicTypes**](DataDetailingDetailingChecksWeldCIBasicTypes.md) |  | [optional] 
**detailing_checks_weld** | [**DataDetailingDetailingChecksWeldCIBasicTypes**](DataDetailingDetailingChecksWeldCIBasicTypes.md) |  | [optional] 
**weld_resistance** | **float** |  | [optional] 
**weld_elem_area** | **float** |  | [optional] 
**xu** | **float** |  | [optional] 
**theta_weld** | **float** |  | [optional] 
**aisc_directional_strength_increase** | **bool** |  | [optional] 
**mw** | **float** |  | [optional] 
**fusion_area_elem** | **float** |  | [optional] 
**fu_base_metal** | **float** |  | [optional] 
**base_metal_resistance** | **float** |  | [optional] 
**theta1_weld** | **float** |  | [optional] 
**theta2_weld** | **float** |  | [optional] 
**fn_weld** | **float** |  | [optional] 
**length_elem_reduced** | **float** |  | [optional] 
**length_reduced** | **float** |  | [optional] 
**beta_f_snip** | **float** |  | [optional] 
**beta_z_snip** | **float** |  | [optional] 
**rwf_snip** | **float** |  | [optional] 
**rwz_snip** | **float** |  | [optional] 
**gamma_c** | **float** |  | [optional] 
**gamma_wm_snip** | **float** |  | [optional] 
**fexx** | **float** |  | [optional] 
**fnbm** | **float** |  | [optional] 
**awe** | **float** |  | [optional] 
**abm** | **float** |  | [optional] 
**base_metal_capacity** | **bool** |  | [optional] 
**beta_f_chn** | **float** |  | [optional] 
**is_butt_weld** | **bool** |  | [optional] 
**gamma_mw_is** | **float** |  | [optional] 
**weld_longitudinal_force** | **float** |  | [optional] 
**weld_transversal_force** | **float** |  | [optional] 
**weld_longitudinal_resistance** | **float** |  | [optional] 
**weld_transversal_resistance** | **float** |  | [optional] 
**weld_theta_hk** | **float** |  | [optional] 
**weld_coeff_k_hk** | **float** |  | [optional] 
**is_weld_design_strength_table_value** | **bool** |  | [optional] 
**is_ecen_weld_material_and_electrode** | **bool** |  | [optional] 
**ue** | **float** |  | [optional] 
**us** | **float** |  | [optional] 
**weld_position_snip** | [**DataWeldPositionSNIPCIBasicTypes**](DataWeldPositionSNIPCIBasicTypes.md) |  | [optional] 
**welding_type_snip** | [**DataWeldingTypeSNIPCIBasicTypes**](DataWeldingTypeSNIPCIBasicTypes.md) |  | [optional] 
**fire_temperature** | **float** |  | [optional] 
**fire_design** | **bool** |  | [optional] 
**is_horizontal_tying** | **bool** |  | [optional] 
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
from connection_restapi_client_poc.models.weld_check_res_data_idea_stati_ca_connection_checks import WeldCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of WeldCheckResDataIdeaStatiCaConnectionChecks from a JSON string
weld_check_res_data_idea_stati_ca_connection_checks_instance = WeldCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(WeldCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
weld_check_res_data_idea_stati_ca_connection_checks_dict = weld_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of WeldCheckResDataIdeaStatiCaConnectionChecks from a dict
weld_check_res_data_idea_stati_ca_connection_checks_from_dict = WeldCheckResDataIdeaStatiCaConnectionChecks.from_dict(weld_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


