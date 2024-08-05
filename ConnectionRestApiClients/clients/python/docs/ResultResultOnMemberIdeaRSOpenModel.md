# ResultResultOnMemberIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ResultMemberIdeaRSOpenModel**](ResultMemberIdeaRSOpenModel.md) |  | [optional] 
**result_type** | [**ResultResultTypeIdeaRSOpenModel**](ResultResultTypeIdeaRSOpenModel.md) |  | [optional] 
**local_system_type** | [**ResultResultLocalSystemTypeIdeaRSOpenModel**](ResultResultLocalSystemTypeIdeaRSOpenModel.md) |  | [optional] 
**results** | **List[object]** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.result_result_on_member_idea_rs_open_model import ResultResultOnMemberIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ResultResultOnMemberIdeaRSOpenModel from a JSON string
result_result_on_member_idea_rs_open_model_instance = ResultResultOnMemberIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ResultResultOnMemberIdeaRSOpenModel.to_json())

# convert the object into a dict
result_result_on_member_idea_rs_open_model_dict = result_result_on_member_idea_rs_open_model_instance.to_dict()
# create an instance of ResultResultOnMemberIdeaRSOpenModel from a dict
result_result_on_member_idea_rs_open_model_from_dict = ResultResultOnMemberIdeaRSOpenModel.from_dict(result_result_on_member_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


