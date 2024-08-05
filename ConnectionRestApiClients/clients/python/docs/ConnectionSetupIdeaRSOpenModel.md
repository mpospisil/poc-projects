# ConnectionSetupIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**steel_setup** | **object** |  | [optional] 
**concrete_setup** | [**ConcreteConcreteSetupIdeaRSOpenModel**](ConcreteConcreteSetupIdeaRSOpenModel.md) |  | [optional] 
**stop_at_limit_strain** | **bool** |  | [optional] 
**weld_evaluation_data** | [**WeldEvaluationIdeaRSOpenModel**](WeldEvaluationIdeaRSOpenModel.md) |  | [optional] 
**check_detailing** | **bool** |  | [optional] 
**apply_cone_breakout_check** | [**ConeBreakoutCheckTypeIdeaRSOpenModel**](ConeBreakoutCheckTypeIdeaRSOpenModel.md) |  | [optional] 
**pretension_force_fpc** | **float** |  | [optional] 
**gamma_inst** | **float** |  | [optional] 
**gamma_c** | **float** |  | [optional] 
**gamma_m3** | **float** |  | [optional] 
**anchor_length_for_stiffness** | **int** |  | [optional] 
**joint_beta_factor** | **float** |  | [optional] 
**effective_area_stress_coeff** | **float** |  | [optional] 
**effective_area_stress_coeff_aisc** | **float** |  | [optional] 
**friction_coefficient** | **float** |  | [optional] 
**limit_plastic_strain** | **float** |  | [optional] 
**limit_deformation** | **float** |  | [optional] 
**limit_deformation_check** | **bool** |  | [optional] 
**analysis_gnl** | **bool** |  | [optional] 
**analysis_all_gnl** | **bool** |  | [optional] 
**warn_plastic_strain** | **float** |  | [optional] 
**warn_check_level** | **float** |  | [optional] 
**optimal_check_level** | **float** |  | [optional] 
**distance_between_bolts** | **float** |  | [optional] 
**distance_diameter_between_bp** | **float** |  | [optional] 
**distance_between_bolts_edge** | **float** |  | [optional] 
**bearing_angle** | **float** |  | [optional] 
**decreasing_ftrd** | **float** |  | [optional] 
**braced_system** | **bool** |  | [optional] 
**bearing_check** | **bool** |  | [optional] 
**apply_betap_influence** | **bool** |  | [optional] 
**member_length_ratio** | **float** |  | [optional] 
**division_of_surface_of_chs** | **int** |  | [optional] 
**division_of_arcs_of_rhs** | **int** |  | [optional] 
**num_element** | **int** |  | [optional] 
**number_iterations** | **int** |  | [optional] 
**mdiv** | **int** |  | [optional] 
**min_size** | **float** |  | [optional] 
**max_size** | **float** |  | [optional] 
**num_element_rhs** | **int** |  | [optional] 
**num_element_plate** | **int** |  | [optional] 
**rigid_bp** | **bool** |  | [optional] 
**alpha_cc** | **float** |  | [optional] 
**cracked_concrete** | **bool** |  | [optional] 
**developed_fillers** | **bool** |  | [optional] 
**deformation_bolt_hole** | **bool** |  | [optional] 
**extension_length_ration_open_sections** | **float** |  | [optional] 
**extension_length_ration_close_sections** | **float** |  | [optional] 
**factor_preload_bolt** | **float** |  | [optional] 
**base_metal_capacity** | **bool** |  | [optional] 
**apply_bearing_check** | **bool** |  | [optional] 
**friction_coefficient_pbolt** | **float** |  | [optional] 
**crt_comp_check_is** | [**CrtCompCheckISIdeaRSOpenModel**](CrtCompCheckISIdeaRSOpenModel.md) |  | [optional] 
**bolt_max_grip_length_coeff** | **float** |  | [optional] 
**fatigue_section_offset** | **float** |  | [optional] 
**condensed_element_length_factor** | **float** |  | [optional] 
**gamma_mu** | **float** |  | [optional] 
**hss_limit_plastic_strain** | **float** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_setup_idea_rs_open_model import ConnectionSetupIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionSetupIdeaRSOpenModel from a JSON string
connection_setup_idea_rs_open_model_instance = ConnectionSetupIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionSetupIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_setup_idea_rs_open_model_dict = connection_setup_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionSetupIdeaRSOpenModel from a dict
connection_setup_idea_rs_open_model_from_dict = ConnectionSetupIdeaRSOpenModel.from_dict(connection_setup_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


