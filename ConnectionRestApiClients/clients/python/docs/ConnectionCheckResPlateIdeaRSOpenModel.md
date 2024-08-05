# ConnectionCheckResPlateIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**check_status** | **bool** |  | [optional] 
**load_case_id** | **int** |  | [optional] 
**max_strain** | **float** |  | [optional] 
**max_stress** | **float** |  | [optional] 
**items** | **List[int]** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_check_res_plate_idea_rs_open_model import ConnectionCheckResPlateIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCheckResPlateIdeaRSOpenModel from a JSON string
connection_check_res_plate_idea_rs_open_model_instance = ConnectionCheckResPlateIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCheckResPlateIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_check_res_plate_idea_rs_open_model_dict = connection_check_res_plate_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCheckResPlateIdeaRSOpenModel from a dict
connection_check_res_plate_idea_rs_open_model_from_dict = ConnectionCheckResPlateIdeaRSOpenModel.from_dict(connection_check_res_plate_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


