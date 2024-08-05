# ConnectionCheckResWeldIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**unity_check** | **float** |  | [optional] 
**check_status** | **bool** |  | [optional] 
**load_case_id** | **int** |  | [optional] 
**items** | **List[int]** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_check_res_weld_idea_rs_open_model import ConnectionCheckResWeldIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCheckResWeldIdeaRSOpenModel from a JSON string
connection_check_res_weld_idea_rs_open_model_instance = ConnectionCheckResWeldIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCheckResWeldIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_check_res_weld_idea_rs_open_model_dict = connection_check_res_weld_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCheckResWeldIdeaRSOpenModel from a dict
connection_check_res_weld_idea_rs_open_model_from_dict = ConnectionCheckResWeldIdeaRSOpenModel.from_dict(connection_check_res_weld_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


