# ConnectionCheckResSummaryIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_value** | **float** |  | [optional] 
**check_status** | **bool** |  | [optional] 
**load_case_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**unity_check_message** | **str** |  | [optional] 
**skipped** | **bool** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_check_res_summary_idea_rs_open_model import ConnectionCheckResSummaryIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCheckResSummaryIdeaRSOpenModel from a JSON string
connection_check_res_summary_idea_rs_open_model_instance = ConnectionCheckResSummaryIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCheckResSummaryIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_check_res_summary_idea_rs_open_model_dict = connection_check_res_summary_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCheckResSummaryIdeaRSOpenModel from a dict
connection_check_res_summary_idea_rs_open_model_from_dict = ConnectionCheckResSummaryIdeaRSOpenModel.from_dict(connection_check_res_summary_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


