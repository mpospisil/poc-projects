# ResultMemberIdeaRSOpenModel

Member identification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_type** | [**ResultMemberTypeIdeaRSOpenModel**](ResultMemberTypeIdeaRSOpenModel.md) |  | [optional] 
**id** | **int** | Id of member | [optional] 

## Example

```python
from connection_restapi_client_poc.models.result_member_idea_rs_open_model import ResultMemberIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResultMemberIdeaRSOpenModel from a JSON string
result_member_idea_rs_open_model_instance = ResultMemberIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ResultMemberIdeaRSOpenModel.to_json())

# convert the object into a dict
result_member_idea_rs_open_model_dict = result_member_idea_rs_open_model_instance.to_dict()
# create an instance of ResultMemberIdeaRSOpenModel from a dict
result_member_idea_rs_open_model_from_dict = ResultMemberIdeaRSOpenModel.from_dict(result_member_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


