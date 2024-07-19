# IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel


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
from connection_restapi_client_poc.models.idea_rs_open_model_connection_check_res_plate_idea_rs_open_model import IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_check_res_plate_idea_rs_open_model_instance = IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_check_res_plate_idea_rs_open_model_dict = idea_rs_open_model_connection_check_res_plate_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel from a dict
idea_rs_open_model_connection_check_res_plate_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_check_res_plate_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


