# AnalysisCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applied_load_percentage** | **float** |  | [optional] 
**critical_load_coeff** | **float** |  | [optional] 
**message** | **str** |  | [optional] 
**max_plate_eps** | **float** |  | [optional] 
**max_weld_eps** | **float** |  | [optional] 
**points** | [**List[CIGiCL2DPoint2DCIGeometry2D]**](CIGiCL2DPoint2DCIGeometry2D.md) |  | [optional] 
**singularity_detected** | **bool** |  | [optional] 
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
from connection_restapi_client_poc.models.analysis_check_res_data_idea_stati_ca_connection_checks import AnalysisCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisCheckResDataIdeaStatiCaConnectionChecks from a JSON string
analysis_check_res_data_idea_stati_ca_connection_checks_instance = AnalysisCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(AnalysisCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
analysis_check_res_data_idea_stati_ca_connection_checks_dict = analysis_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of AnalysisCheckResDataIdeaStatiCaConnectionChecks from a dict
analysis_check_res_data_idea_stati_ca_connection_checks_from_dict = AnalysisCheckResDataIdeaStatiCaConnectionChecks.from_dict(analysis_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


