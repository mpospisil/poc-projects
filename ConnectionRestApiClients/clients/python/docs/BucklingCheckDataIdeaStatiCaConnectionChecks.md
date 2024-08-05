# BucklingCheckDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shape** | **int** |  | [optional] 
**shape_inx** | **int** |  | [optional] 
**bucklig_load_coefficient** | **float** |  | [optional] 
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
from connection_restapi_client_poc.models.buckling_check_data_idea_stati_ca_connection_checks import BucklingCheckDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of BucklingCheckDataIdeaStatiCaConnectionChecks from a JSON string
buckling_check_data_idea_stati_ca_connection_checks_instance = BucklingCheckDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(BucklingCheckDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
buckling_check_data_idea_stati_ca_connection_checks_dict = buckling_check_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of BucklingCheckDataIdeaStatiCaConnectionChecks from a dict
buckling_check_data_idea_stati_ca_connection_checks_from_dict = BucklingCheckDataIdeaStatiCaConnectionChecks.from_dict(buckling_check_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


