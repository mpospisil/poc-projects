# StiffnessChekDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beam_id** | **int** |  | [optional] 
**component** | **str** |  | [optional] 
**component_id** | [**StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks**](StiffnessChekDataLoadComponentIdeaStatiCaConnectionChecks.md) |  | [optional] 
**myz** | **float** |  | [optional] 
**mx_start** | **float** |  | [optional] 
**my_start** | **float** |  | [optional] 
**mz_start** | **float** |  | [optional] 
**ryz** | **float** |  | [optional] 
**ryz_capacity** | **float** |  | [optional] 
**kyz** | **float** |  | [optional] 
**kyz_classification** | **str** |  | [optional] 
**kyz_limit_rigid** | **float** |  | [optional] 
**kyz_limit_pinned** | **float** |  | [optional] 
**nx** | **float** |  | [optional] 
**nx_start** | **float** |  | [optional] 
**dx** | **float** |  | [optional] 
**kx** | **float** |  | [optional] 
**points** | [**List[CIGiCL2DPoint2DCIGeometry2D]**](CIGiCL2DPoint2DCIGeometry2D.md) |  | [optional] 
**points_shell** | [**List[CIGiCL2DPoint2DCIGeometry2D]**](CIGiCL2DPoint2DCIGeometry2D.md) |  | [optional] 
**points_linear** | [**List[CIGiCL2DPoint2DCIGeometry2D]**](CIGiCL2DPoint2DCIGeometry2D.md) |  | [optional] 
**n_mcrd** | **float** |  | [optional] 
**n_mjrd** | **float** |  | [optional] 
**theoretical_length** | **float** |  | [optional] 
**sjini** | **float** |  | [optional] 
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
from connection_restapi_client_poc.models.stiffness_chek_data_idea_stati_ca_connection_checks import StiffnessChekDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of StiffnessChekDataIdeaStatiCaConnectionChecks from a JSON string
stiffness_chek_data_idea_stati_ca_connection_checks_instance = StiffnessChekDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(StiffnessChekDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
stiffness_chek_data_idea_stati_ca_connection_checks_dict = stiffness_chek_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of StiffnessChekDataIdeaStatiCaConnectionChecks from a dict
stiffness_chek_data_idea_stati_ca_connection_checks_from_dict = StiffnessChekDataIdeaStatiCaConnectionChecks.from_dict(stiffness_chek_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


