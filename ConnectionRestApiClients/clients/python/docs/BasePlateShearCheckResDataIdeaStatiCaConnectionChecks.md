# BasePlateShearCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vrdf** | **float** |  | [optional] 
**vrdx** | **float** |  | [optional] 
**vrdy** | **float** |  | [optional] 
**vx** | **float** |  | [optional] 
**vy** | **float** |  | [optional] 
**v** | **float** |  | [optional] 
**vr** | **float** |  | [optional] 
**pbr** | **float** |  | [optional] 
**vcb** | **float** |  | [optional] 
**friction_coefficient** | **float** |  | [optional] 
**shear_iron_css** | **str** |  | [optional] 
**shear_iron_applied** | **bool** |  | [optional] 
**unity_check** | **float** |  | [optional] 
**avx** | **float** |  | [optional] 
**avy** | **float** |  | [optional] 
**fy** | **float** |  | [optional] 
**nsd** | **float** |  | [optional] 
**shear_force_transfer** | **int** |  | [optional] 
**gamma_m0** | **float** |  | [optional] 
**asd** | **bool** |  | [optional] 
**phi_omega** | **float** |  | [optional] 
**bearing_resistance** | **float** |  | [optional] 
**num_of_tensioned_anchors** | **int** |  | [optional] 
**phi_br** | **float** |  | [optional] 
**fc** | **float** |  | [optional] 
**alpha_v** | **float** |  | [optional] 
**psi_alpha_v** | **float** |  | [optional] 
**avc_cone_breakout_area** | **float** |  | [optional] 
**unity_check_cone_breakout_resistance** | **float** |  | [optional] 
**unity_check_bearing_capacity** | **float** |  | [optional] 
**phi_c** | **float** |  | [optional] 
**omega_c** | **float** |  | [optional] 
**phi_s** | **float** |  | [optional] 
**shear_lug_force** | **float** |  | [optional] 
**shear_lug_force_component** | **float** |  | [optional] 
**cone_breakout_check_type** | [**DataConeBreakoutCheckTypeCIBasicTypes**](DataConeBreakoutCheckTypeCIBasicTypes.md) |  | [optional] 
**shear_lug_projection_area** | **float** |  | [optional] 
**comp_force** | **float** |  | [optional] 
**kc** | **float** |  | [optional] 
**connector_tensile_area** | **float** |  | [optional] 
**connector_fy** | **float** |  | [optional] 
**ny** | **float** |  | [optional] 
**pa** | **float** |  | [optional] 
**a** | **float** |  | [optional] 
**l** | **float** |  | [optional] 
**b** | **float** |  | [optional] 
**gamma_c** | **float** |  | [optional] 
**v_factor** | **float** |  | [optional] 
**k1_factor** | **float** |  | [optional] 
**sigma_rdmax** | **float** |  | [optional] 
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
from connection_restapi_client_poc.models.base_plate_shear_check_res_data_idea_stati_ca_connection_checks import BasePlateShearCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of BasePlateShearCheckResDataIdeaStatiCaConnectionChecks from a JSON string
base_plate_shear_check_res_data_idea_stati_ca_connection_checks_instance = BasePlateShearCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(BasePlateShearCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
base_plate_shear_check_res_data_idea_stati_ca_connection_checks_dict = base_plate_shear_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of BasePlateShearCheckResDataIdeaStatiCaConnectionChecks from a dict
base_plate_shear_check_res_data_idea_stati_ca_connection_checks_from_dict = BasePlateShearCheckResDataIdeaStatiCaConnectionChecks.from_dict(base_plate_shear_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


