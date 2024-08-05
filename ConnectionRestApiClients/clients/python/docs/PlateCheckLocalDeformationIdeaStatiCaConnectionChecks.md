# PlateCheckLocalDeformationIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_deformation** | **float** |  | [optional] 
**max_deformation_ratio** | **float** |  | [optional] 
**limit_deformation** | **float** |  | [optional] 
**thickness** | **float** |  | [optional] 
**csize** | **float** |  | [optional] 
**material_name** | **str** |  | [optional] 
**items** | **List[int]** |  | [optional] 
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
from connection_restapi_client_poc.models.plate_check_local_deformation_idea_stati_ca_connection_checks import PlateCheckLocalDeformationIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of PlateCheckLocalDeformationIdeaStatiCaConnectionChecks from a JSON string
plate_check_local_deformation_idea_stati_ca_connection_checks_instance = PlateCheckLocalDeformationIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(PlateCheckLocalDeformationIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
plate_check_local_deformation_idea_stati_ca_connection_checks_dict = plate_check_local_deformation_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of PlateCheckLocalDeformationIdeaStatiCaConnectionChecks from a dict
plate_check_local_deformation_idea_stati_ca_connection_checks_from_dict = PlateCheckLocalDeformationIdeaStatiCaConnectionChecks.from_dict(plate_check_local_deformation_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


