# ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fjd** | **float** |  | [optional] 
**average_stress** | **float** |  | [optional] 
**nsd** | **float** |  | [optional] 
**aeff** | **float** |  | [optional] 
**aeff_center_gravity** | **str** |  | [optional] 
**center_tension** | **str** |  | [optional] 
**center_compression** | **str** |  | [optional] 
**aeff2** | **float** |  | [optional] 
**supporting_regions** | [**List[CIGeometry2DIRegion2DCIBasicTypes]**](CIGeometry2DIRegion2DCIBasicTypes.md) |  | [optional] 
**aeff_net** | **float** |  | [optional] 
**unity_check_stress** | **float** |  | [optional] 
**kj** | **float** |  | [optional] 
**add_bearing_width** | **float** |  | [optional] 
**eff_area_of_base_plates** | **Dict[str, List[List[List[CIGiCL2DPath2DSegmentCIGeometry2D]]]]** |  | [optional] 
**gamma_c** | **float** |  | [optional] 
**fck** | **float** |  | [optional] 
**fck_factored** | **float** |  | [optional] 
**betaj** | **float** |  | [optional] 
**alpha_cc** | **float** |  | [optional] 
**fc** | **float** |  | [optional] 
**phi_crt** | **float** |  | [optional] 
**omega_crt** | **float** |  | [optional] 
**fck_ext1** | **float** |  | [optional] 
**fck_ext2** | **float** |  | [optional] 
**fck_ext** | **float** |  | [optional] 
**crt_bearing_strength** | **float** |  | [optional] 
**phi_c** | **float** |  | [optional] 
**psi_snip** | **float** |  | [optional] 
**phi_b_snip** | **float** |  | [optional] 
**gamma_b_snip** | **float** |  | [optional] 
**beta_c_chn** | **float** |  | [optional] 
**beta_l_chn** | **float** |  | [optional] 
**reinforced_concrete_pad** | **bool** |  | [optional] 
**omega_factor** | **float** |  | [optional] 
**crt_comp_check_is** | [**IdeaStatiCaConnectionBasicTypesDataCrtCompCheckISCIBasicTypes**](IdeaStatiCaConnectionBasicTypesDataCrtCompCheckISCIBasicTypes.md) |  | [optional] 
**gamma_m0_is** | **float** |  | [optional] 
**base_plate_thickness** | **float** |  | [optional] 
**base_plate_fy** | **float** |  | [optional] 
**eff_area_offset** | **float** |  | [optional] 
**concrete_grade** | **str** |  | [optional] 
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
from connection_restapi_client_poc.models.con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks from a JSON string
con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks_instance = ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks_dict = con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks from a dict
con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks_from_dict = ConModelerConnectionPlugInConcreteBlockCheckResDataIdeaStatiCaConnectionChecks.from_dict(con_modeler_connection_plug_in_concrete_block_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


