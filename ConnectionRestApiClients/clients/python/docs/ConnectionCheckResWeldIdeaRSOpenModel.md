# ConnectionCheckResWeldIdeaRSOpenModel

Check value for Weld

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Weld | [optional] 
**id** | **int** | Unique id of weld | [optional] 
**unity_check** | **float** | Unity Check Stress | [optional] 
**check_status** | **bool** | Status of the Check | [optional] 
**load_case_id** | **int** | Id of Load Case | [optional] 
**items** | **List[int]** | In case of presentation of groups plates (uncoiled beams) | [optional] 

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


