# ConnectionCheckResConcreteBlockIdeaRSOpenModel

Check value for Concrete Block

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Concrete Block | [optional] 
**unity_check** | **float** | Unity Check | [optional] 
**check_status** | **bool** | Status of the Check | [optional] 
**load_case_id** | **int** | Id of Load Case | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_check_res_concrete_block_idea_rs_open_model import ConnectionCheckResConcreteBlockIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCheckResConcreteBlockIdeaRSOpenModel from a JSON string
connection_check_res_concrete_block_idea_rs_open_model_instance = ConnectionCheckResConcreteBlockIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCheckResConcreteBlockIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_check_res_concrete_block_idea_rs_open_model_dict = connection_check_res_concrete_block_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCheckResConcreteBlockIdeaRSOpenModel from a dict
connection_check_res_concrete_block_idea_rs_open_model_from_dict = ConnectionCheckResConcreteBlockIdeaRSOpenModel.from_dict(connection_check_res_concrete_block_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


