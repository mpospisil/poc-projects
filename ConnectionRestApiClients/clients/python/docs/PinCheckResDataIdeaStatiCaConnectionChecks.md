# PinCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin_assembly_name** | **str** |  | [optional] 
**pin_shear_resistance** | **float** |  | [optional] 
**pin_bearing_resistance** | **float** |  | [optional] 
**pin_replaceable_bearing_resistance** | **float** |  | [optional] 
**pin_bending_resistance** | **float** |  | [optional] 
**pin_replaceable_bending_resistance** | **float** |  | [optional] 
**pin_combined_shear_and_bending_resistance** | **float** |  | [optional] 
**contact_bearing_stress** | **float** |  | [optional] 
**contact_bearing_resistance** | **float** |  | [optional] 
**unity_check_pin_shear** | **float** |  | [optional] 
**unity_check_pin_bearing** | **float** |  | [optional] 
**unity_check_pin_replaceable_bearing** | **float** |  | [optional] 
**unity_check_pin_bearing_decisive** | **float** |  | [optional] 
**unity_check_pin_bending** | **float** |  | [optional] 
**unity_check_pin_replaceable_bending** | **float** |  | [optional] 
**unity_check_pin_bending_decisive** | **float** |  | [optional] 
**unity_check_pin_combined_shear_and_bending** | **float** |  | [optional] 
**unity_check_pin_replaceable_contact_bearing** | **float** |  | [optional] 
**max_unity_check_shear** | **float** |  | [optional] 
**is_pin_replaceable** | **bool** |  | [optional] 
**pin_all_elements_all_sections_forces_for_diagram** | **Dict[str, List[List[float]]]** |  | [optional] 
**pin_shear_forces** | **List[float]** |  | [optional] 
**pin_bearing_forces** | **List[float]** |  | [optional] 
**pin_bearing_forces_by_plate_id** | **Dict[str, float]** |  | [optional] 
**pin_bending_forces** | **List[float]** |  | [optional] 
**pin_shear_force** | **float** |  | [optional] 
**pin_bearing_force_for_bearing** | **float** |  | [optional] 
**pin_bending_force** | **float** |  | [optional] 
**pin_cross_sectional_area** | **float** |  | [optional] 
**pin_section_modulus** | **float** |  | [optional] 
**pin_diameter** | **float** |  | [optional] 
**pin_hole_diameter** | **float** |  | [optional] 
**pin_ultimate_tensile_strength** | **float** |  | [optional] 
**pin_yield_strength** | **float** |  | [optional] 
**connected_part_yield_strength** | **float** |  | [optional] 
**connected_part_thickness_for_bearing** | **float** |  | [optional] 
**decisive_yield_strength_for_bearing** | **float** |  | [optional] 
**modulus_of_elasticity_for_contact_bearing** | **float** |  | [optional] 
**yield_strength_for_contact_bearing** | **float** |  | [optional] 
**connected_part_thickness_for_contact_bearing** | **float** |  | [optional] 
**pin_bearing_force_for_contact_bearing** | **float** |  | [optional] 
**gamma_m0** | **float** |  | [optional] 
**gamma_m2** | **float** |  | [optional] 
**gamma_m6ser** | **float** |  | [optional] 
**gamma_mfi** | **float** |  | [optional] 
**is_fire_design** | **bool** |  | [optional] 
**fire_temperature** | **float** |  | [optional] 
**factor_kb_theta** | **float** |  | [optional] 
**detailing_checks_pin** | [**DataDetailingDetailingChecksPinCIBasicTypes**](DataDetailingDetailingChecksPinCIBasicTypes.md) |  | [optional] 
**is_detailing_status_ok** | **bool** |  | [optional] 
**is_detailing_status_for_report_ok** | **bool** |  | [optional] 
**forces_all_load_cases** | **Dict[str, List[float]]** |  | [optional] 
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
from connection_restapi_client_poc.models.pin_check_res_data_idea_stati_ca_connection_checks import PinCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of PinCheckResDataIdeaStatiCaConnectionChecks from a JSON string
pin_check_res_data_idea_stati_ca_connection_checks_instance = PinCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(PinCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
pin_check_res_data_idea_stati_ca_connection_checks_dict = pin_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of PinCheckResDataIdeaStatiCaConnectionChecks from a dict
pin_check_res_data_idea_stati_ca_connection_checks_from_dict = PinCheckResDataIdeaStatiCaConnectionChecks.from_dict(pin_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


